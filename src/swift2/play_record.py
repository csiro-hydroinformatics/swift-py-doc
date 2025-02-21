from typing import Optional, Union, TYPE_CHECKING
from swift2.const import CATCHMENT_FLOWRATE_VARID, VecStr

if TYPE_CHECKING:
    from swift2.classes import (
        Simulation,
        EnsembleSimulation,
        EnsembleForecastSimulation,
    )
    from uchronia.classes import TimeSeriesLibrary, EnsembleForecastTimeSeries
    from swift2.const import NdSimulation, RecordToSignature

from cinterop.timeseries import TimeSeriesLike

import uchronia.wrap.uchronia_wrap_generated as uwg
import uchronia.data_set as uds
import pandas as pd

import swift2.wrap.swift_wrap_generated as swg
import swift2.internal as si
from swift2.utils import is_common_iterable
from swift2.internal import simplify_time_series
import uchronia.classes as uc

def play_inputs(
    simulation: "Simulation", data_library:uc.TimeSeriesLibrary, model_var_id:"VecStr", data_id:"VecStr", resample:"VecStr"=""
):
    """
    Assign input time series from a time series library to a model simulation

    Args:
        simulation (Simulation): A swift simulation object
        data_library (TimeSeriesLibrary): external pointer type ENSEMBLE_DATA_SET_PTR, or a Python class wrapper around it 
        model_var_id (str or sequence of str): model state variable unique identifier(s)
        data_id (str or sequence of str): identifier(s) for data in the data_library. If length is not the same as model_var_id, the elements of data_id are reused to match it
        resample (str or sequence of str): identifier(s) for how the series is resampled (aggregated or disaggregated). If length is not the same as model_var_id, the elements of resample are reused to match it

    """
    # model_var_id <- as.character(model_var_id)
    # data_id <- as.character(data_id)
    # resample <- as.character(resample)
    # TODO: match the behavior of R, perhaps.
    assert len(model_var_id) == len(data_id)
    assert len(model_var_id) == len(resample)
    # if(len(model_var_id) != len(data_id)):
    #     # warning('Reusing argument `data_id` to match length of `model_var_id`')
    #     data_id = np.repeat(data_id, length.out=length(model_var_id))

    # if(length(resample)!=length(model_var_id)) {
    # if(length(resample) != 1 || resample[1] != '') warning('Reusing argument `resample` to match the length of `model_var_id`')
    # resample <- rep(resample, length.out=length(model_var_id))
    # }
    swg.PlayDatasetInputs_py(
        simulation, data_library, model_var_id, data_id, resample, len(model_var_id)
    )


def _mkid(*args):
    return ".".join(args)


def play_subarea_input(simulation: "Simulation", input, subarea_name, input_name):
    """
    Sets time series as input to a simulation

    Sets time series as input to a simulation

    Args:
        simulation (Simulation): A swift simulation object
        input (Any): an xts time series.
        subarea_name (Any): a valid name of the subarea
        input_name (Any): the name of the input variable to the model (i.e. 'P' for the precip of GR5H)

    """
    play_input(simulation, input, _mkid("subarea", subarea_name, input_name))



def play_input(
    simulation: "NdSimulation", input_ts: "TimeSeriesLike", var_ids: VecStr = None
) -> None:
    """
    Sets time series as input to a simulation

    Sets time series as input to a simulation

    Args:
        simulation (Simulation): A swift simulation object
        input_ts (Any): an xts time series, or an S4 object 'ExternalObjRef' [package "cinterop"] with external pointer type "ENSEMBLE_FORECAST_TIME_SERIES_PTR". if an xts time series column names must be valid model variable identifiers, unless explicitely provided via varIds
        var_ids (Any): optional character, the variable identifiers to use, overriding the column names of the inputTs. If not NULL, must be of length equal to the number of columns in inputTs

    """
    if si.is_ensemble_forecast_simulation(
        simulation
    ) and si.is_ensemble_forecast_time_series(input_ts):
        play_ensemble_forecast_input(simulation, input_ts, var_ids)
    elif si.is_ensemble_simulation(
        simulation
    ):  # ??? and si.is_ensemble_forecast_time_series(input_ts):
        raise NotImplementedError("play input into ensemble simulation not supported")
    # } else {
    # stopifnot(is.xts(input_ts))
    else:
        play_singular_simulation(simulation, input_ts, var_ids)


def play_singular_simulation(simulation, input_ts, var_ids):
    if var_ids is None:
        if not isinstance(input_ts, pd.DataFrame):
            raise NotImplementedError(
                "missing var_ids, but input_ts is not a dataframe"
            )
        var_ids = input_ts.columns
        if var_ids is None:
            raise ValueError(
                "no explicit variable identifiers, and no column names found on the dataframe as input time series"
            )
        # }
        # stopifnot(is.character(var_ids))
        # if(length(var_ids) != ncol(input_ts)) raise Exception('if the variable identifiers are explicitly provided, it must be of same length as the input multivariate time series')
    simple_ts = simplify_time_series(input_ts)
    ts_values = simple_ts[si.TS_INTEROP_VALUES_KEY]
    ts_geom = simple_ts[si.TS_INTEROP_GEOM_KEY]
    if isinstance(var_ids, str):
        assert len(ts_values.shape) == 1
        swg.Play_py(
            simulation,
            var_ids,
            ts_values,
            ts_geom,
        )
    elif is_common_iterable(var_ids):
        if len(var_ids) == 1:
            assert len(ts_values.shape) == 1
            swg.Play_py(
                simulation,
                var_ids[0],
                ts_values,
                ts_geom,
            )
        else:
            if isinstance(input_ts, pd.DataFrame):
                assert len(input_ts.columns) == len(var_ids)
            assert len(ts_values.shape) == 2
            assert ts_values.shape[1] == len(var_ids)
            for i, v in enumerate(var_ids):
                swg.Play_py(
                    simulation,
                    v,
                    ts_values[:, i],
                    ts_geom,
                )


def play_ensemble_forecast_input(
    simulation: "EnsembleForecastSimulation",
    input_ts: "EnsembleForecastTimeSeries",
    var_id: str,
) -> None:
    """
    Sets time series as input to a simulation

    Sets time series as input to a simulation

    Args:
        simulation (Any): an S4 object 'ExternalObjRef' [package "cinterop"] with external pointer type "ENSEMBLE_FORECAST_SIMULATION_PTR"
        input_ts (Any): an S4 object 'ExternalObjRef' [package "cinterop"] with external pointer type "ENSEMBLE_FORECAST_TIME_SERIES_PTR"
        var_id (Any): character of length one, the variable identifier to use

    """
    si.check_ensemble_forecast_simulation(simulation)
    si.check_ensemble_forecast_time_series(input_ts)
    assert isinstance(var_id, str)
    swg.PlayEnsembleForecastTimeSeries_py(simulation, input_ts, var_id)


#' Retrieves a played time series from a simulation
#'
#' Retrieves a played time series from a simulation.
#'
#' @param simulation an S4 object 'ExternalObjRef' [package "cinterop"] with external pointer type "MODEL_SIMULATION_PTR"
#' @param var_ids name of the output variable played to a time series. 'Catchment|StreamflowRate'. If missing, a multivariate time series of all played states is returned; this may be a large amount of data.
#' @param start_time An optional parameter, the start of a period to subset the time series
#' @param end_time An optional parameter, the end of a period to subset the time series
#' @return an xts time series, possibly multivariate.
#' @export
#' @import xts


def get_played(simulation: "Simulation", var_ids=None, start_time=None, end_time=None):
    """
    Retrieves a played time series from a simulation

    Retrieves a played time series from a simulation.

    Args:
        simulation (Simulation): A swift simulation object
        var_ids (Any): name of the output variable played to a time series. 'Catchment|StreamflowRate'. If missing, a multivariate time series of all played states is returned; this may be a large amount of data.
        start_time (Any): An optional parameter, the start of a period to subset the time series
        end_time (Any): An optional parameter, the end of a period to subset the time series

    Returns:
        an xts time series, possibly multivariate.

    """

    series = None
    if var_ids is None:
        var_ids = get_played_varnames(simulation)
    series = si.internal_get_played_tts(simulation, var_ids)
    return si.get_ts_window(series, start_time, end_time)


def get_played_varnames(simulation):
    """
    Gets all the names of states fed an input time series

    Gets all the names of states fed an input time series

    Args:
        simulation (Simulation): A swift simulation object

    Returns:
        The names of the state variables fed over the simulation with values from a time series

    """
    return swg.GetPlayedVariableNames_py(simulation)


def get_recorded(
    simulation: "Simulation", var_ids=None, start_time=None, end_time=None
):
    """
    Retrieves a recorded time series from a simulation

    Retrieves a recorded time series from a simulation.

    Args:
        simulation (Simulation): A swift simulation object
        var_ids (Any): name of the output variable recorded to a time series. 'Catchment|StreamflowRate'. If missing, a multivariate time series of all recorded states is returned; this may be a large amount of data.
        start_time (Any): An optional parameter, the start of a period to subset the time series
        end_time (Any): An optional parameter, the end of a period to subset the time series

    Returns:
        an xts time series, possibly multivariate.

    """
    if si.is_ensemble_forecast_simulation(simulation):
        return get_recorded_ensemble_forecast(simulation, var_ids, start_time, end_time)
    else:
        series = None
        if var_ids is None:
            var_ids = get_recorded_varnames(simulation)
        series = si.internal_get_recorded_tts(simulation, var_ids)
        return si.get_ts_window(series, start_time, end_time)


def get_all_recorded(simulation):
    all_ids = get_recorded_varnames(simulation)
    return uds.get_multiple_time_series_from_provider(
        simulation, all_ids, si.internal_get_recorded_tts
    )


def get_all_played(simulation):
    all_ids = get_played_varnames(simulation)
    return uds.get_multiple_time_series_from_provider(
        simulation, all_ids, si.internal_get_played_tts
    )


def get_recorded_ensemble_forecast(
    simulation, var_id: str, start_time=None, end_time=None
):
    """
    Retrieves a recorded time series from a simulation

    Retrieves a recorded time series from a simulation.

    Args:
        simulation (Simulation): A swift simulation object
        var_ids (Any): name of the output variable recorded to a time series. 'Catchment|StreamflowRate'. If missing, a multivariate time series of all recorded states is returned; this may be a large amount of data.
        start_time (Any): NOT USED YET An optional parameter, the start of a period to subset the time series
        end_time (Any): NOT USED YET An optional parameter, the end of a period to subset the time series

    Returns:
        an xts time series, possibly multivariate.

    """
    si.check_ensemble_forecast_simulation(simulation)
    return swg.GetRecordedEnsembleForecastTimeSeries_py(simulation, var_id)
    # TODO
    # getTsWindow(series, start_time, end_time)


def get_recorded_varnames(simulation):
    """
    Gets all the names of the recorded states

    Gets all the names of the recorded states

    Args:
        simulation (Simulation): A swift simulation object

    Returns:
        The names of the state variables being recorded into time series

    """
    return swg.GetRecordedVariableNames_py(simulation)


# #' Gets a trace of some states of the model simulation
# #'
# #' Gets a trace of some states of the model simulation
# #'
# #' @param simulation an S4 object 'ExternalObjRef' [package "cinterop"] with external pointer type "MODEL_SIMULATION_PTR"
# #' @param var_ids character vector of known model variable identifiers. Will record all states already set to be recorded otherwise (beware this may be a large amount of data)
# #' @param funNames function to transform the default names of the returned time series. character to character.
# #' @return a time series of the states
# #' @export
# getStateTrace(modelSimulation, var_ids, funNames) {
#   execSimulation(modelSimulation)
#   if(missing(var_ids)) {
#     tts <- getRecorded(modelSimulation)
#   } else {
#     tts <- getRecorded(modelSimulation, var_ids)
#   }
#   if(!missing(funNames)) names(tts) <- funNames(names(tts))
#   tts
# }


def record_state(
    simulation,
    var_ids: VecStr = CATCHMENT_FLOWRATE_VARID,
    recording_provider: "TimeSeriesLibrary" = None,
    data_ids: "VecStr" = None,
):
    """
    Record a time series of one of the state of the model

    Record a time series of one of the state of the model

    Args:
        simulation (Any): an S4 object 'ExternalObjRef' [package "cinterop"] with external pointer type "MODEL_SIMULATION_PTR", "ENSEMBLE_SIMULATION_PTR" or "ENSEMBLE_FORECAST_SIMULATION_PTR"
        var_ids (VecStr, optional): identifier(s) of the output variable recorded to a time series, e.g. 'Catchment|StreamflowRate' or 'subcatchment.Subarea.runoff'. Defaults to CATCHMENT_FLOWRATE_VARID.
        recording_provider (TimeSeriesLibrary, optional): _description_. Defaults to None.
        data_ids (VecStr, optional): _description_. Defaults to None.

    Raises:
        ValueError: _description_
    """
    # checkRecordingConsistency(var_ids, recording_provider, data_ids)
    # var_ids <- as.character(var_ids)
    # data_ids <- as.character(data_ids)
    # recordSingularState(simulation, var_ids, recording_provider, data_ids)Err
    if si.is_ensemble_forecast_simulation(simulation):
        record_ensemble_forecast_state(
            simulation, var_ids, recording_provider, data_ids
        )
    elif si.is_ensemble_simulation(simulation):
        record_ensemble_state(simulation, var_ids, recording_provider, data_ids)
    elif si.is_singular_simulation(simulation):
        record_singular_state(simulation, var_ids, recording_provider, data_ids)
    else:
        raise ValueError("Unknown type of simulation")


# checkRecordingConsistency(var_ids, recording_provider, data_ids) {
#   if(!is.null(recording_provider)) {
#     if(length(var_ids) != length(data_ids)) {
#       raise Exception('The lengths of data_ids and var_ids must be equal for recording time series to a recording provider')
#     }
#   }
# }


def _v_apply(ids, func):
    if is_common_iterable(ids):
        for v in ids:
            func(v)
    # elif isinstance(var_ids, str):
    #     swg.Record_py(simulation, var_ids)
    # else:
    #     raise ValueError("Unhandled type for state identification: " + str(type(var_ids)))
    else:
        func(ids)


def apply_recording_function(
    simulation: "Simulation",
    recording_func: Optional["RecordToSignature"],
    var_ids: VecStr,
    recording_provider,
    data_ids,
):
    if is_common_iterable(var_ids):
        for i in range(len(var_ids)):
            recording_func(simulation, var_ids[i], recording_provider, data_ids[i])
    else:
        recording_func(simulation, var_ids, recording_provider, data_ids)


def record_singular_state(
    simulation: "Simulation",
    var_ids: VecStr = CATCHMENT_FLOWRATE_VARID,
    recording_provider: "TimeSeriesLibrary" = None,
    data_ids: "VecStr" = None,
):
    # checkSingularSimulation(simulation)
    # var_ids <- as.character(var_ids)
    # checkRecordingConsistency(var_ids, recording_provider, data_ids)
    # data_ids <- as.character(data_ids)
    if recording_provider is None:

        def func(v):
            swg.Record_py(simulation, v)

        _v_apply(var_ids, func)
    else:
        raise NotImplementedError(
            "applyRecordingFunction(RecordTo_py, var_ids, recording_provider, data_ids)"
        )


# #' Record a time series of one of the state of the model
# #'
# #' Record a time series of one of the state of the model
# #'
# #' @param simulation an S4 object 'ExternalObjRef' [package "cinterop"] with external pointer type "ENSEMBLE_SIMULATION_PTR"
# #' @param var_ids identifier(s) of the output variable recorded to a time series, e.g. 'Catchment|StreamflowRate' or 'subcatchment.Subarea.runoff'
# #' @export
def record_ensemble_state(
    simulation: "EnsembleSimulation",
    var_ids: VecStr = CATCHMENT_FLOWRATE_VARID,
    recording_provider: "TimeSeriesLibrary" = None,
    data_ids: "VecStr" = None,
):
    si.check_ensemble_simulation(simulation)
    # checkRecordingConsistency(var_ids, recording_provider, data_ids)
    if recording_provider is None:

        def func(v):
            swg.RecordEnsembleModelRunner_py(simulation, v)

        _v_apply(var_ids, func)
    else:
        apply_recording_function(
            simulation, swg.RecordEnsembleTo_py, var_ids, recording_provider, data_ids
        )


# #' Record a time series of one of the state of the model
# #'
# #' Record a time series of one of the state of the model
# #'
# #' @param simulation an S4 object 'ExternalObjRef' [package "cinterop"] with external pointer type "ENSEMBLE_FORECAST_SIMULATION_PTR"
# #' @param var_ids identifier(s) of the output variable recorded to a time series, e.g. 'Catchment|StreamflowRate' or 'subcatchment.Subarea.runoff'
# #' @export
def record_ensemble_forecast_state(
    simulation: "EnsembleForecastSimulation",
    var_ids: VecStr = CATCHMENT_FLOWRATE_VARID,
    recording_provider: "TimeSeriesLibrary" = None,
    data_ids: "VecStr" = None,
):
    si.check_ensemble_forecast_simulation(simulation)
    # checkRecordingConsistency(var_ids, recording_provider, data_ids)
    # var_ids <- as.character(var_ids)
    # data_ids <- as.character(data_ids)
    if recording_provider is None:

        def func(v):
            swg.RecordEnsembleForecastTimeSeries_py(simulation, v)

        _v_apply(var_ids, func)
    else:
        apply_recording_function(
            simulation,
            swg.RecordEnsembleForecastToRecorder_py,
            var_ids,
            recording_provider,
            data_ids,
        )
