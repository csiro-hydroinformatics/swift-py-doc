"""Prototypes
"""

import os
from pathlib import Path

#############
# 2022-05 Refactored out from ozrr package devised for DWL
#############

# TODO down the track we'd want to remove this dependency on ozrr_data
# from ozrr_data.conventions import STATIONS_DIM_NAME
from ozrr_data.repository import OzDataProvider, to_pd_series

import pandas as pd

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from swift2.classes import Simulation

import swift2.simulation as ss
import swift2.play_record as spr
from swift2.common import _df_from_dict, _npf

import swift2.parameteriser as sp
import swift2.doc_helper as std

OBSERVED_SERIES_COLNAME = "Observed"
MODELLED_SERIES_COLNAME = "Modelled"


class PbmModelFactory:
    def __init__(self, data_repo: OzDataProvider) -> None:
        self.data_repo = data_repo

    def new_monthly_lumped_model(
        self, station_id: str, model_id: str, rain_varid="P", evap_varid="E"
    ):
        id_prefix = "subarea.Subarea."
        runoff_id = id_prefix + "runoff"
        d = self.data_repo.data_for_station(station_id)
        area_km2 = float(d["area_corrected[km2]"])
        sim = ss.create_subarea(model_id, area_km2)
        ss.set_simulation_time_step(sim, "monthly")
        rain = d.rain_mm_mth
        evap = d.evap_mm_mth
        r_pd = to_pd_series(rain)
        e_pd = to_pd_series(evap)
        ss.play_subarea_input(sim, r_pd, "Subarea", rain_varid)
        ss.play_subarea_input(sim, e_pd, "Subarea", evap_varid)
        spr.record_state(sim, runoff_id)
        return sim


class PbmCalibration:
    def __init__(
        self,
        station_id: str,
        model_id,
        simulation: "Simulation",
        data_repo: OzDataProvider,
    ) -> None:
        self._simulation = simulation
        self.data_repo = data_repo
        self.station_id = station_id
        self.model_id = model_id
        self.objective_id = "NSE"

        self.run_start = pd.Timestamp("1950-01-01")
        self.calib_start = pd.Timestamp("1952-01-01")
        self.calib_end = pd.Timestamp("1995-12-01")
        self.valid_start = pd.Timestamp("1996-01-01")
        self.valid_end = pd.Timestamp("2014-12-01")

        self.s_calib = slice(self.calib_start, self.calib_end)
        self.s_valid = slice(self.valid_start, self.valid_end)

        self.runoff_id = "subarea.Subarea.runoff"
        self.runoff_ts = self.data_repo.monthly_data(
            self.station_id, "runoff", cf_time=True
        )

        self.optimiser = None
        self.opt_log = None
        self.parameter_template = parameters_for(self.model_id)

    def max_walltime_seconds(self, sec: int):
        self.max_hours_walltime = sec / 3600

    def set_metrics(self, metrics):
        self.metrics = metrics

    def calibrate(self):
        sim = self._simulation.clone()
        sim.set_simulation_span(self.run_start, self.calib_end)
        sim.record_state(self.runoff_id)
        objective = sim.create_objective(
            self.runoff_id,
            self.runoff_ts,
            self.objective_id,
            self.calib_start,
            self.calib_end,
        )
        term = sp.create_sce_termination_wila(
            "relative standard deviation",
            [str(self.convergence_criterion), str(self.max_hours_walltime)],
        )
        sce_params = std.sce_parameter(5, nshuffle=40)
        urs = sp.create_parameter_sampler(0, self.parameter_template, "urs")
        optimizer = sp.create_sce_optim_swift(objective, term, sce_params, urs)
        optimizer.set_calibration_logger("")
        self.optimiser = optimizer
        self.opt_log = None
        self.calib_results = self.optimiser.execute_optimisation()
        self.best_params = self.calib_results.get_best_score(
            score_name=self.objective_id, convert_to_py=False
        ).parameteriser
        self.best_score = self.calib_results.get_best_score(
            score_name=self.objective_id, convert_to_py=True
        )
        # sim.set_simulation_span(self.run_start, self.valid_end)
        # self.best_params.apply_sys_config(sim)
        # sim.exec_simulation()
        # self.runoff
        # sim.get_recorded(self.runoff_id)

    def get_geom_ops(self):
        return self.extract_optimisation_log()["geom_ops"]

    def extract_optimisation_log(self):
        if self.opt_log is None:
            self.opt_log = self.optimiser.extract_optimisation_log(
                fitness_name=self.objective_id
            )
        return self.opt_log

    def best_modelled_runoff(self):
        sim = self._simulation.clone()
        sim.set_simulation_span(self.run_start, self.valid_end)
        self.best_params.apply_sys_config(sim)
        sim.exec_simulation()
        return sim.get_recorded(self.runoff_id)

    def validate(self):
        best_p = self.calib_results.get_best_score(
            score_name=self.objective_id, convert_to_py=False
        ).parameteriser
        simul_validation = self._simulation.clone()
        simul_validation.set_simulation_span(self.run_start, self.valid_end)
        best_p.apply_sys_config(simul_validation)
        simul_validation.exec_simulation()
        objective_verif = simul_validation.create_objective(
            self.runoff_id,
            self.runoff_ts,
            self.objective_id,
            self.valid_start,
            self.valid_end,
        )
        verif_score = objective_verif.get_score(best_p)
        self.verif_score = verif_score

        return self.best_score, self.verif_score

    def _scatter_plot(self, title: str, slice_time):
        best_modelled = self.best_modelled_runoff()
        scatter_plot(
            self.runoff_ts.sel(time=slice_time),
            best_modelled.sel(time=slice_time),
            title="{} {}".format(self.station_id, title),
        )

    def scatter_plot_calib(self):
        self._scatter_plot("Best fit, calibration period", self.s_calib)

    def scatter_plot_valid(self):
        self._scatter_plot("Verification period, calibrated parameters", self.s_valid)

    def save_to(self, root_path: str = None):
        if root_path is None:
            root_path = "/home/per202/tmp/out"
        import json

        best_score, verif_score = self.best_score, self.verif_score
        df: pd.DataFrame = best_score["sysconfig"]
        d = dict(
            station_id=self.station_id,
            run_start=str(self.run_start),
            calib_start=str(self.calib_start),
            calib_end=str(self.calib_end),
            valid_start=str(self.valid_start),
            valid_end=str(self.valid_end),
            calib_scores=best_score["scores"],
            verif_scores=verif_score["scores"],
            parameters=df.to_dict(),
        )
        root_output_folder = Path(root_path)

        if not os.path.exists(root_output_folder):
            os.mkdir(root_output_folder)

        output_folder = root_output_folder / self.model_id

        if not os.path.exists(output_folder):
            os.mkdir(output_folder)

        output_file = output_folder / "results_{}.json".format(self.station_id)
        with open(output_file, "w") as f:
            json.dump(d, f)
        output_file_p = output_folder / "params_{}.csv".format(self.station_id)
        df.to_csv(output_file_p)
        x = self.best_runoff_series()
        output_file_ts = output_folder / "series_{}.csv".format(self.station_id)
        x.to_csv(output_file_ts)

    def best_runoff_series(self):
        # important to remove extraneous dimensions otherwise pd.series index is not intuitive:
        best_modelled_s = self.best_modelled_runoff().squeeze(drop=True).to_series()
        x = pd.concat([self.runoff_ts.to_series(), best_modelled_s], axis=1)
        x.columns = [OBSERVED_SERIES_COLNAME, MODELLED_SERIES_COLNAME]
        return x

    # def fit_metrics(self, bivar_metrics: Sequence[Callable]):
    #     x = self.best_runoff_series()
    #     return None


class PbmCalibrationBuilder:
    def __init__(self, model_factory: PbmModelFactory) -> None:
        self.model_factory = model_factory
        self.objective_id = "NSE"
        self.max_walltime_seconds(10)
        self.convergence_criterion = 0.002

    def set_sampling_periods(
        self,
        run_start="1950-01-01",
        calib_start="1952-01-01",
        calib_end="1995-12-01",
        valid_start="1996-01-01",
        valid_end="2014-12-01",
    ):
        self.run_start = pd.Timestamp(run_start)
        self.calib_start = pd.Timestamp(calib_start)
        self.calib_end = pd.Timestamp(calib_end)
        self.valid_start = pd.Timestamp(valid_start)
        self.valid_end = pd.Timestamp(valid_end)
        self.s_calib = slice(self.calib_start, self.calib_end)
        self.s_valid = slice(self.valid_start, self.valid_end)

    def max_walltime_seconds(self, sec: int):
        self.max_hours_walltime = sec / 3600

    def build_calibration(self, station_id, model_id):
        sim = self.model_factory.new_monthly_lumped_model(station_id, model_id)
        calib = PbmCalibration(station_id, model_id, sim, self.model_factory.data_repo)
        calib.calib_start = self.calib_start
        calib.calib_end = self.calib_end
        calib.valid_start = self.valid_start
        calib.valid_end = self.valid_end
        calib.s_calib = self.s_calib
        calib.s_valid = self.s_valid
        calib.max_hours_walltime = self.max_hours_walltime
        calib.convergence_criterion = self.convergence_criterion
        return calib

def ts_plot(x, title, y_units):
    import matplotlib.pyplot as plt
    x.squeeze().plot(figsize = (8,5))
    plt.title(title)
    plt.ylabel(y_units)


def scatter_plot(obs_runoff_ts, mod_runoff_ts, title):
    import matplotlib.pyplot as plt
    plt.figure(figsize=(10, 10))
    plt.scatter(obs_runoff_ts.values, mod_runoff_ts.values)
    plt.ylabel("Modelled [mm/mth]")
    plt.xlabel("Observed [mm/mth]")
    plt.title(title)


# "WAPABA"
# https://doi.org/10.1016/j.jhydrol.2011.04.027
# Symbol	Range	Unit	Name
# Smax	5–1000	mm	Maximum water holding capacity of soil store
# α1	1–10	–	Catchment consumption curve parameter
# α2	1–10	–	Evapotranspiration curve parameter
# β	0–1	–	Proportion of catchment yield as groundwater
# K−1	1/3650–1	day−1	Inverse of groundwater store time constant

_params = {
    "WAPABA": [
        [
            "alpha1",
            "alpha2",
            "Beta",
            "Smax",
            "InvK",
        ],
        [2.0, 2.0, 0.5, 0.0, 0.5],
        [1.0, 1.0, 0.0, 5.0, 1 / 3650.0],
        [
            10.0,
            10.0,
            1.0,
            6000.0,  # really let that go far, to cater a few extreme cases
            1.0,
        ],
    ],
    #     [16:14] Robertson, David (L&W, Clayton)
    # pSpecGr4j <- getFreeParams("GR4J")
    # pSpecGr2M <- pSpecGr4j
    # pSpecGr2M$Name <- c("x1","x2", "x5", "x4")
    # pSpecGr2M$Value <- c(3.21137, 1.0, 1.0,50.)
    # pSpecGr2M$Min <- c(1.0, -10.0, 0.010, 0.01)
    # pSpecGr2M$Max <- c(1000.0, 10.0, 1.0, 3000.00)
    # parameterizer <- createParameterizer(type = 'Generic subareas', specs = pSpecGr2M)
    # AddParameterDefinition_R(parameterizer,"x3",0.01,1000,10)
    # parameterizer <- wrapTransform(parameterizer)
    # addTransform(parameterizer, "asinh_x2", "x2", "asinh")
    # addTransform(parameterizer, "log_x1", "x1", "log10")
    # addTransform(parameterizer, "log_x5", "x5", "log10")
    # addTransform(parameterizer, "log_x4", "x4", "log10")
    # addTransform(parameterizer, "log_x3", "x3", "log10")
    "GR2M_MOD": [
        [
            "x1",
            "x2",
            "x3",
            "x4",
            "x5",
        ],
        [
            250,
            0.77,
            60.0,
            60.0,
            1.0,
        ],
        [
            1.0,
            -10.0,
            0.01,
            0.01,
            0.01,
        ],
        [
            1000.0,
            10.0,
            1000,
            6000.0,  # really let that go far, to cater a few extreme cases
            1.0,
        ],
    ],
}


def parameters_for(model_id: str):
    pname, pvals, pmin, pmax = _params[model_id]
    id_prefix = "subarea.Subarea."
    pname = [id_prefix + n for n in pname]
    p_spec = _df_from_dict(
        Name=pname,
        Value=_npf(pvals),
        Min=_npf(pmin),
        Max=_npf(pmax),
    )
    return sp.create_parameteriser("Generic", p_spec)
