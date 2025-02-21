from typing import List, Optional, Dict
from cinterop.timeseries import start_ts, end_ts
import numpy as np

import os
import json
import jsonpickle


from swift2.parameteriser import (
    add_to_hypercube,
    add_transform,
    apply_sys_config,
    concatenate_parameterisers,
    create_muskingum_param_constraints,
    create_parameteriser,
    get_default_sce_parameters,
    linear_parameteriser,
    make_state_init_parameteriser,
    set_hypercube,
    wrap_transform,
)

from swift2.simulation import *
from swift2.utils import c, mk_full_data_id


_test_data_dir = os.path.join(os.path.dirname(__file__), "data", "samples")

_sample_data_obj = None


def set_sample_data(
    model_sim,
    site_id="MMH",
    rain_data_var="rain",
    evap_data_var="evap",
    rain_model_var="P",
    evap_model_var="E",
    t_step="daily",
):
    """
    Sets sample input data into a model simulation

    Sets input data from the included sample data into a model simulation

    Args:
        model_sim (Any): an S4 object 'ExternalObjRef' [package "cinterop"] with external pointer type "MODEL_SIMULATION_PTR"
        site_id (Any): sample data site identifier
        rain_data_var (Any): time series ID for the rainfall in the sample data
        evap_data_var (Any): time series ID for the evaporation in the sample data
        rain_model_var (Any): sub-area runoff model state identifier for the rainfall, e.g. 'P'
        evap_model_var (Any): sub-area runoff model state identifier for the evaporation, e.g. 'E'
        t_step (Any): identifier for the time step to set the simulation to.

    """

    rain = sample_series(site_id, var_name=rain_data_var)
    evap = sample_series(site_id, var_name=evap_data_var)
    sa_ids = get_subarea_ids(model_sim)
    for sa_id in sa_ids:
        play_subarea_input(model_sim, rain, sa_id, rain_model_var)
        play_subarea_input(model_sim, evap, sa_id, evap_model_var)
    set_simulation_time_step(model_sim, t_step)
    set_simulation_span(model_sim, start_ts(rain), end_ts(rain))


def inspect(simulation: "Simulation", element="link", id="1", full_names=False):
    """
    Inspect an element of a catchment model

    Inspect the current state values of an element of a catchment model

    Args:
        simulation (Simulation): A swift simulation object
        element (Any): type of top level element, within c('link','node','subarea')
        id (Any): SWIFT simulation
        full_names (Any): if TRUE returns the full names of state variable ids (e.g. link.link_1.OutlfowRate)

    Returns:
        named numeric vector, the current state values of the catchment model element

    Examples:
        TODO
    """
    # Examples:
    #     >>> # ms <- createTestCatchmentStructure()$model
    #     >>> # inspect(ms, element='link', id='lnk1')
    #     >>> # inspect(ms, element='subarea', id='lnk1')
    #     >>> # inspect(ms, element='subarea', id='lnk1', fullNames=TRUE)
    all_f_ids = get_variable_ids(simulation, mk_full_data_id(element, id), full_id=True)
    all_f_ids = np.sort([s for s in set(all_f_ids)])
    x = get_state_value(simulation, all_f_ids)

    def last_in_vec(v):
        if len(v) > 0:
            return v[-1]
        else:
            return ""

    if not full_names:
        new_k = dict([(k, last_in_vec(k.split("."))) for k in x.keys()])
        # if len(new_k) != len(set(new_k)): raise Exception()
        new_x = dict([(new_k[k], x[k]) for k in x.keys()])
        x = new_x
    return x


#' @export
def configure_test_simulation(
    simulation: "Simulation",
    data_id="MMH",
    simul_start="1990-01-01",
    simul_end="2005-12-31",
    tstep="daily",
    varname_rain="P",
    varname_pet="E",
    varname_data_rain="P",
    varname_data_pet="E",
):
    from swift2.internal import _end, _start

    s_span = slice(as_timestamp(simul_start), as_timestamp(simul_end))
    rain = sample_series(site_id=data_id, var_name=varname_data_rain)[s_span]
    evap = sample_series(site_id=data_id, var_name=varname_data_pet)[s_span]
    sa_ids = get_subarea_ids(simulation)
    for id in sa_ids:
        play_subarea_input(simulation, rain, id, varname_rain)
        play_subarea_input(simulation, evap, id, varname_pet)
    set_simulation_time_step(simulation, tstep)
    set_simulation_span(simulation, _start(rain), _end(rain))
    return simulation


def testdata_dir():
    global _test_data_dir
    return _test_data_dir


def _sample_data():
    global _sample_data_obj
    if _sample_data_obj is None:
        with open(os.path.join(testdata_dir(), "swift_sample_data.json.dat"), "r") as f:
            dat = json.load(f)
        _sample_data_obj = jsonpickle.loads(dat[0])
    return _sample_data_obj


def sample_series(site_id="MMH", var_name="rain"):
    """
    Deserialize information to a UTC time series

    Deserialize information to a UTC time series. This function is overcoming some behaviors in saving/loading xts series to/from binary RData format. Usage is not intended for most users.

    Args:
        site_id (Any): a site identifier
        var_name (Any): a variable identifier valid for the given site_id

    Returns:
        an xts time series with UTC time indexing

    """
    s = _sample_data()
    siteData = s[site_id]
    varData = siteData[var_name]
    # if (varData)) stop(paste('Sample data for site', site_id, 'and variable name', var_name, 'not found'))
    return deserialise_sample_series(varData)


import pandas as pd
import numpy as np


def deserialise_sample_series(serialised: Dict):
    dt = [pd.Timestamp(i, unit="s") for i in serialised["utcInt"]]
    assert isinstance(serialised["x"], list)
    assert len(serialised["x"]) > 0

    d = np.array(serialised["x"])
    if d.dtype != float:
        d = pd.to_numeric(d, errors="coerce")
    if isinstance(serialised["x"][0], list):
        res = pd.DataFrame(d, columns=serialised["name"], index=dt)
    else:
        res = pd.Series(d, index=dt)
        # res.name = serialised['name'][0] # TODO?
    return res


def sample_catchment_model(site_id="South_Esk", config_id="catchment"):
    """
    Deserialize a basic catchment structure from the package sample data

    Deserialize a basic catchment structure from the package sample data. This function is mostly for documentation purposes.

    Args:
        site_id (Any): a site identifier
        config_id (Any): a variable identifier for a model structure valid for the given site_id

    Returns:
        a model simulation

    """
    # if not exists('swiftSampleData')) data(swift_sample_data)
    s = _sample_data()
    site_data: Dict = s[site_id]
    if config_id not in site_data.keys():
        raise ValueError(
            "Sample catchment model for site "
            + site_id
            + " identified by "
            + config_id
            + " not found"
        )
    cat_structure = site_data[config_id]
    return create_catchment_model_from_structure(cat_structure)


#' @export
def create_catchment_model_from_structure(cat_structure: Dict[str, List]):
    # stopifnot( all(c('Node', 'Link', 'Subarea', 'NodeLink') %in% names(cat_structure)))
    df_defn = dict([(k, pd.DataFrame(cat_structure[k])) for k in cat_structure])
    # not used yet.
    # slc = cat_structure[['SubareaLink']]
    # rownames(slc) = slc['Id']
    # slc = slc[cat_structure[['Link']]['Id'],]

    link_ids = df_defn["Link"]["Id"].values
    link_names = df_defn["Link"]["Name"].values
    node_ids = df_defn["Node"]["Id"].values
    node_names = df_defn["Node"]["Name"].values
    from_node = df_defn["NodeLink"]["UpstreamId"].values
    to_node = df_defn["NodeLink"]["DownstreamId"].values
    areas = df_defn["Subarea"]["AreaKm2"].values

    simulation = create_catchment(
        node_ids=node_ids,
        node_names=node_names,
        link_ids=link_ids,
        link_names=link_names,
        link_from_node=from_node,
        link_to_node=to_node,
        runoff_model_name="GR4J",
        areas_km2=areas,
    )
    links = df_defn["Link"]
    set_state_value(
        simulation,
        paste0("link.", link_ids, ".Length"),
        links["LengthMetres"].values.astype(float),
    )
    set_state_value(
        simulation, paste0("link.", link_ids, ".f"), links["f"].values.astype(float)
    )
    set_state_value(
        simulation,
        paste0("link.", link_ids, ".ManningsN"),
        links["ManningsN"].values.astype(float),
    )
    set_state_value(
        simulation,
        paste0("link.", link_ids, ".Slope"),
        links["Slope"].values.astype(float),
    )
    return simulation


#' @export
def create_test_catchment_structure(
    node_ids=None,
    link_ids=None,
    from_node=None,
    to_node=None,
    areas_km2=None,
    runoff_model="GR4J",
):

    #  sa for lnk4(1.2) -->   n3 --- lnk4 ---> \
    #                                           \
    #                   sa for lnk3(4.4) -->     n4 --- lnk3 ---> \
    #                                           /                  \
    #  sa for lnk5(2.3) -->   n1 --- lnk5 ---> /                    \
    #                                                                \
    #                                        sa for lnk1(1.5) -->    n2 --- lnk1 ---> n6
    #                                                                /
    #                       sa for lnk2(2.2) -->   n5 --- lnk2 ---> /
    if node_ids is None:
        node_ids = paste0("n", [i + 1 for i in range(6)])
    if link_ids is None:
        link_ids = paste0("lnk", [i + 1 for i in range(5)])
    if from_node is None:
        from_node = paste0("n", [2, 5, 4, 3, 1])
    if to_node is None:
        to_node = paste0("n", [6, 2, 2, 4, 4])
    if areas_km2 is None:
        areas_km2 = 1.1 * np.arange(1, len(link_ids) + 1)
    # stopifnot(len(from_node)==len(to_node))
    # stopifnot(len(areas_km2)==len(link_ids))

    node_names = paste0(node_ids, "_name")
    link_names = paste0(link_ids, "_name")

    defn = {
        "node_ids": node_ids,
        "node_names": node_names,
        "link_ids": link_ids,
        "link_names": link_names,
        "from_node": from_node,
        "to_node": to_node,
        "areas_km2": areas_km2,
        "runoff_model": runoff_model,
    }
    ms = create_catchment(
        node_ids,
        node_names,
        link_ids,
        link_names,
        from_node,
        to_node,
        runoff_model,
        areas_km2,
    )
    return defn, ms


def get_catchment_dot_graph(simulation):
    """
    Gets a catchment representation in Graphviz DOT format

    Gets a catchment representation in Graphviz DOT format

    Args:
        simulation (Simulation): A swift simulation object

    Returns:
        a string in a notation usable by the DiagrammeR package.

    Examples:
        TODO

    """
    # Examples:
    # >>> # library(swift)
    # >>> # library('DiagrammeR')
    # >>> # dataId <- 'MMH'
    # >>> # simulation <- createTestCatchment(nSubareas=4, dataId=dataId, varNameDataRain='rain', varNameDataPet='evap')
    # >>> # DiagrammeR(getCatchmentDotGraph(simulation))
    return swg.GetCatchmentDOTGraph_py(simulation)


def create_gr4jh_parameters():
    """
    Get a parameter set that configures GR4J for hourly operations

    Get a parameter set that configures GR4J for hourly operations

    Returns:
        HyperCubeParameteriser: a parameter set that can be applied to SWIFT systems with GR4J

    """
    # Configure for GR4J but with changed parameters, supposed to be OK for hourly operations.
    return create_parameteriser(
        specs=_df_from_dict(
            Name=["PercFactor", "UHExponent"],
            Value=_npf([4, 5 / 4]),
            Min=_npf([4, 5 / 4]),
            Max=_npf([4, 5 / 4]),
        )
    )


def configure_hourly_gr4j(simulation):
    """
    Configure a simulation with GR4J models for hourly time step modelling

    Configure a simulation with GR4J models for hourly time step modelling

    Args:
        simulation (Simulation): A swift simulation object

    """
    pGr4jHourly = create_gr4jh_parameters()
    apply_sys_config(pGr4jHourly, simulation)


def define_gr4j_scaled_parameter(ref_area:float=250, time_span:int=3600, pspec_gr4j:Optional[pd.DataFrame]=None):
    """
    define a scaled and transformed parameterizer for GR4J

    define a scaled and transformed parameterizer for GR4J

    Args:
        ref_area (float): the reference area in square kilometres
        time_span (int): the time span of the simulation intented for this model, in seconds
        pspec_gr4j (pd.DataFrame): optional - data frame specifying the feasible parameter space for parameters x1 to x2 of GR4J

    Returns:
        TransformParameteriser: a parameterizer for GR4J, combining time and area scaling and superimposed with log10 transforms for x1, x3, x4 and arc-sinh for x2
    """
    time_span = int(time_span)
    parameteriser = gr4j_scaled_parameteriser(ref_area, time_span)
    if pspec_gr4j is None:
        pspec_gr4j = _df_from_dict(
            Name=["x1", "x2", "x3", "x4"],
            Value=_npf([3.21137e00, 6.95511e00, 2.06740e00, 2.02033e00]),
            Min=_npf([1.0e00, -27.0, 1.0e00, 1.0e00]),
            Max=_npf([6.0e03, 27.0, 1.0e03, 2.4e02]),
        )
    set_hypercube(parameteriser, pspec_gr4j)
    parameteriser = wrap_transform(parameteriser)
    add_transform(parameteriser, "log_x4", "x4", "log10")
    add_transform(parameteriser, "log_x1", "x1", "log10")
    add_transform(parameteriser, "log_x3", "x3", "log10")
    add_transform(parameteriser, "asinh_x2", "x2", "asinh")

    return parameteriser


def set_muskingum_routing_to_linear(simulation):
    from swift2.common import _df_from_dict

    # ####################################################################################################
    #   Add Muskingum Routing parameters to parameteriser
    paramN = _df_from_dict(Name=["N"], Value=[1.00], Min=[1.00], Max=[1.00])
    mkLinearMusk = create_parameteriser(type="Generic links", specs=paramN)
    apply_sys_config(mkLinearMusk, simulation)


def default_pspec_nlm():
    from swift2.common import _df_from_dict

    return _df_from_dict(
        Name=c("X", "Alpha"),
        Value=c(2.00000e-03, 5.00000e-01),
        Min=c(1.00000e-03, 1.00000e-03),
        Max=c(0.350000, 1.0000e03),
    )


def add_mln_and_loglik(
    parameteriser, simulation, p_spec_nlm, delta_t, param_name_k="Alpha", objfun=None
):
    muskParameterizer = create_parameteriser(type="Generic links", specs=p_spec_nlm)
    # error("FIXIT: noticed that this function was using a 'simulation' not passed as a parameter. Fix!")
    muskParameterizer = create_muskingum_param_constraints(
        muskParameterizer,
        delta_t=delta_t,
        param_name_k=param_name_k,
        simulation=simulation,
    )
    # parameteriserAsDataFrame(muskParameterizer)
    parameteriser = concatenate_parameterisers(parameteriser, muskParameterizer)
    ####################################################################################################
    #
    #   Add transformation parameters and variance to parameteriser
    #
    if objfun in c("Log-Likelihood", "WeightedLeastSquares"):
        parameteriser = add_loglikelihood_params(parameteriser)
    return parameteriser


def add_loglikelihood_params(parameteriser):
    from swift2.common import _df_from_dict

    ####################################################################################################
    #
    #   Add transformation parameters and variance to parameteriser
    #
    set_loglik_param_keys(a="epsilon", b="lambda", m="m", s="s")
    loglik = create_parameteriser(type="Log-Likelihood")
    llikespec = _df_from_dict(
        Name=c("lambda", "epsilon", "m", "s"),
        Value=c(0, -4, 0, 2),
        Min=c(-10, 0, 0, -1),
        Max=c(10, -30, 0, np.log(10000)),
    )

    add_to_hypercube(loglik, llikespec)
    #   clrCall(loglik, "Add", "lambda", -30, 0, -4);
    #   clrCall(loglik, "Add", "epsilon", -30, 0, -4);
    #   clrCall(loglik, "Add", "m", 0, 0, 0);
    #   clrCall(loglik, "Add", "s", -1, log(10000), 2);
    return concatenate_parameterisers(parameteriser, loglik)


#' @export
def define_parameteriser_gr4j_muskingum(
    ref_area=250,
    time_span=3600,
    p_spec_nlm=None,
    simulation=None,
    objfun=None,
    delta_t=1,
    param_name_k="K",
):  # delta_t in hours??????? - NEEDS EXPLAINING!
    parameteriser = define_gr4j_scaled_parameter(ref_area, time_span)
    p_states = linear_parameteriser(
        param_name=c("S0", "R0"),
        state_name=c("S", "R"),
        scaling_var_name=c("x1", "x3"),
        min_p_val=c(0.5, 0.0),
        max_p_val=c(0.5, 0.0),
        value=c(0.5, 0.0),
        selector_type="each subarea",
    )

    init_parameteriser = make_state_init_parameteriser(p_states)
    parameteriser = concatenate_parameterisers(parameteriser, init_parameteriser)

    set_muskingum_routing_to_linear(simulation)
    if p_spec_nlm is None:
        p_spec_nlm = default_pspec_nlm()
    parameteriser = add_mln_and_loglik(
        parameteriser, simulation, p_spec_nlm, delta_t, param_name_k, objfun
    )
    return parameteriser


def gr4j_scaled_parameteriser(reference_area: float = 240, t_step_seconds: int = 3600):
    """
    Get a time step and area scaled parameterizer for the GR4 model structure

    Get a time step and area scaled parameterizer for the GR4 model structure

    Args:
        reference_area (Any): The reference area in km^2 for the parameter x4
        t_step_seconds (Any): The simulation time step in seconds.

    Returns:
        A SWIFT catchment parameterizer for GR4 model structures

    """
    return swg.CreateGr4ScaledParameterizer_py(reference_area, t_step_seconds)


#' @export
# def lag_and_route_parameteriser(reference_area=240, t_step_seconds=3600): ????
def lag_and_route_parameteriser():
    p = _df_from_dict(
        Name=["theta1", "qstar", "Tau"],
        Value=_npf([1, 1, 2.5]),
        Min=_npf([1, 1, 2.5]),
        Max=_npf([1, 1, 2.5]),
    )
    p = create_parameteriser("Generic links", p)
    return p


def sce_parameter(nparams: int, nshuffle: int = 40) -> Dict[str, float]:
    """Create SCE parameters suited for a given number of parameters.

    Args:
        nparams (int): number of free model parameters
        nshuffle (int, optional): maximum number of shuffles to do, if no other termination criterion. Defaults to 40.

    Returns:
        Dict[str,float]: SCE hyperparameters
    """
    sce_params = get_default_sce_parameters()
    sce_params["P"] = nparams + 2
    sce_params["Pmin"] = nparams + 2
    sce_params["M"] = 2 * nparams + 1
    sce_params["Q"] = max(sce_params["M"] - 2, 2)
    sce_params["NumShuffle"] = nshuffle
    return sce_params


def short_var_id(var_ids: "VecStr") -> "VecStr":
    """
    Shorten long model variable identifiers to the short model variable name

    Shorten long model variable identifiers to the short model variable name. This is useful for instance to prepare time series names for multi-plot displays.

    Args:
        var_ids (Any): character vector

    Returns:
        the short model variable identifiers

    Examples:
        >>> short_var_id('elementtype|elementname|varid')
        >>> short_var_id('elementtype.elementname.varid')

    """
    if is_common_iterable(var_ids):
        return [short_var_id(v) for v in var_ids]
    else:
        return var_ids.split("|")[-1].split["."][-1]


def set_loglik_param_keys(
    a="a", b="b", m="m", s="s", maxobs="maxobs", ct="ct", censopt="CensOpt"
):
    """
    Specify the global parameter names to use in the log-likelihood calculation

    Specify the global parameter names to use in the log-likelihood calculation. Consequence of prehistoric legacy.

    Args:
        a (str): the name of the a parameter
        b (str): the name of the b parameter
        m (str): the name of the m parameter
        s (str): the name of the s parameter
        maxobs (str): the name of the maxobs parameter
        ct (str): the name of the ct parameter
        censopt (str): the name of the censopt parameter

    Examples:
        TODO
    """
    # Examples:
    #     >>> # set_loglik_param_keys('lambda', 'epsilon', 'm', 's')
    #     >>> # pSpecGr4j = get_free_params('GR4J')
    #     >>> # # pSpecGr4j$Value = c(542.1981111, -0.4127542, 7.7403390, 1.2388548)
    #     >>> # # pSpecGr4j$Min = c(1,-30, 1,1)
    #     >>> # # pSpecGr4j$Max = c(3000, 30, 1000, 240)
    #     >>> # # pSpecGr4j$Name = paste0(rootId, pSpecGr4j$Name)
    #     >>> # pgr4 = create_parameterizer(type='Generic', specs=pSpecGr4j)
    #     >>> # p = create_parameterizer(type='log-likelihood')
    #     >>> # p.add("epsilon", -30, 0, -7)
    #     >>> # p.add("m", 0, 0, 0)
    #     >>> # p.add("s", 1, 1000, 100)
    #     >>> # p.add("lambda", -30, 1, -10)
    #     >>> # parameterizer = concatenate_parameterisers(pgr4, p)
    #     >>> # print(parameterizer)
    swg.SetLogLikelihoodVariableNames_py(a, b, m, s, maxobs, ct, censopt)


# #' One At a Time basic sensitivity analysis
# #'
# #' One At a Time basic sensitivity analysis
# #'
# #' @param simulation A SWIFT simulation object (i.e. a model runner)
# #' @param parameters A system configuration suitable for SWIFT models
# #' @param param_name name of the parameter to swoop
# #' @param from the lower bound of the parameter
# #' @param to   the upper bound of the parameter
# #' @param num number of parameter values trialed
# #' @param stateName The name identifying the model state variable to calibrate against the observation
# #' @param observations an xts time series, or at least something that can be merged with an xts time series
# #' @param startTime the start date of the desired time window for the output. Ignored if NA (default)
# #' @param endTime the end date of the desired time window for the output. Ignored if NA (default)
# #' @return a multivariate xts time series, one series per parameter value tried
# #' @export
# oat(simulation, parameters, param_name, from, to, num=10, stateName=CATCHMENT_FLOWRATE_VARID, startTime=NA, endTime=NA):
#   swoop = seq(from=from, by=(to-from)/(num-1), length.out=num)
#   pTmp = CloneHypercubeParameterizer_py(parameters)
#   func(pval):
#     SetParameterValue_py(pTmp, param_name, pval)
#     ApplyConfiguration_py(pTmp, simulation)
#     simulation.exec_simulation()
#     z = getRecorded(simulation, stateName)
#     startTime = ifelse(is.na(startTime), start(z), startTime)
#     endTime = ifelse(is.na(endTime), end(z), endTime)
#     window(z, start=startTime, end=endTime)
#   }
#   tmp = lapply(as.list(swoop), func)
#   res = tmp[[1]]
#   for (i in 2:len(tmp)):
#     res = merge(res, tmp[[i]])
#   }
#   names(res) = as.character(swoop)
#   res
# }

from swift2.common import _df_from_dict, _npf


def get_free_params(model_id):
    """
    Get a default parameter set for models

    Get a default parameter set for models, as a data frame

    Args:
        model_id (Any): an identifier for the model, e.g. 'GR5H'

    Returns:
        a data frame with Min, Max, Value, Name

    """
    pSpec = None
    if model_id == "GR5H":
        pSpec = _df_from_dict(
            Name=["x1", "x2", "x3", "x4", "x5"],
            Value=_npf([44.6, 30.0, 10.0, 14.0, 200.0]),
            Min=_npf([1, 1, 0, 1, 1]),
            Max=_npf([1000, 400, 1000, 240, 1000.0]),
        )
    elif model_id == "GR6J":
        # per202 2014-09-25
        # I take some values for the parameters from the unit tests, but the min/max bounds are PURE guesses. Q/A TBC.
        pSpec = _df_from_dict(
            Name=["x1", "x2", "x3", "x4", "x5", "x6"],
            Value=_npf([20, -2, 10, 2, 0, 1]),
            Min=_npf([1, -5, 0, 1, 0, 0]),
            Max=_npf([1000, 400, 1000, 240, 1, 1]),
        )
    elif model_id == "PDM":
        # per202 2014-11-13
        #
        pSpec = _df_from_dict(
            Name=[
                "cmax",
                "cminrat",
                "b",
                "be",
                "kg",
                "bg",
                "Strat",
                "k1",
                "k2rat",
                "kb",
            ],
            Value=_npf([400, 0.5, 1.8, 1.0, 1300.0, 1.0, 0.5, 35.0, 0.3, 2.4]),
            Min=_npf([1, 0, 0.001, 1.0, 1.0, 1.0, 0.0, 1.0, 0.0001, 1.0]),
            Max=_npf([3000, 1, 2.0, 2.0, 50000.0, 1.0, 1.0, 300.0, 1.0000, 2000.0]),
        )
    elif model_id == "SAC" or model_id == "SACSMA":
        # rob635 2015-01-11
        #
        pSpec = _df_from_dict(
            Name=[
                "UZTWM",
                "UZFWM",
                "UZK",
                "PCTIM",
                "ADIMP",
                "RIVA",
                "REXP",
                "LZTWM",
                "LZFSM",
                "LZFPM",
                "LZSK",
                "LZPK",
                "PFREE",
                "RSERV",
                "SIDE",
            ],
            Value=_npf(
                [
                    50,
                    40,
                    0.245,
                    0.01,
                    0.00,
                    0.01,
                    2.00,
                    130.0,
                    23.0,
                    40.0,
                    0.043,
                    0.009,
                    0.10,
                    0.30,
                    0.00,
                ]
            ),
            Min=_npf(
                [
                    10,
                    5,
                    0.100,
                    0.00,
                    0.00,
                    0.00,
                    1.00,
                    10.0,
                    5.0,
                    10.0,
                    0.001,
                    0.001,
                    0.00,
                    0.00,
                    0.00,
                ]
            ),
            Max=_npf(
                [
                    300,
                    150,
                    0.750,
                    1.00,
                    1.00,
                    1.00,
                    5.00,
                    500.0,
                    400.0,
                    1000.0,
                    0.350,
                    0.050,
                    0.80,
                    1.00,
                    1.00,
                ]
            ),
        )
    elif model_id == "GR4J":
        # \\OSM-01-MEL.it.csiro.au\CLW_HYDROFORECAST_common\Projects\WIRADA_4_1\Work\2013_2014_Act2_Flood_Cal\SWIFT_hourly\C-F2+F3+F5\South_Esk\Output\Out_CaliPara.txt
        # \\OSM-01-MEL.it.csiro.au\CLW_HYDROFORECAST_common\Projects\WIRADA_4_1\Work\2013_2014_Act2_Flood_Cal\SWIFT_hourly\C-F2+F3+F5\South_Esk\Setup\Model_Parameters.txt
        pSpec = _df_from_dict(
            # Name                 X1             X2             X3             X4
            # Number                1              2              3              4
            # Fit(Y\N)              1              1              1              1
            # LowBound    1.00000E+00   -2.70000E+01    1.00000E+00    1.00000E+00
            # UpBound     3.00000E+03    2.70000E+01    6.60000E+02    2.40000E+02
            # #-Calibrated parameters-----------------------------------------------------------------
            # Chmt_001    6.50488E+02   -2.80648E-01    7.89123E+00    1.89172E+01
            Name=["x1", "x2", "x3", "x4"],
            Value=_npf([6.50488e02, -2.80648e-01, 7.89123e00, 1.89172e01]),
            Min=_npf([1, -27, 1, 1]),
            Max=_npf([3.00000e03, 2.70000e01, 6.60000e02, 2.40000e02]),
        )
    elif model_id == "SAC" or model_id == "SACSMA":
        # rob635 2015-01-11
        #
        pSpec = _df_from_dict(
            Name=[
                "UZTWM",
                "UZFWM",
                "UZK",
                "PCTIM",
                "ADIMP",
                "RIVA",
                "REXP",
                "LZTWM",
                "LZFSM",
                "LZFPM",
                "LZSK",
                "LZPK",
                "PFREE",
                "RSERV",
                "SIDE",
            ],
            Value=_npf(
                [
                    50,
                    40,
                    0.245,
                    0.01,
                    0.00,
                    0.01,
                    2.00,
                    130.0,
                    23.0,
                    40.0,
                    0.043,
                    0.009,
                    0.10,
                    0.30,
                    0.00,
                ]
            ),
            Min=_npf(
                [
                    10,
                    5,
                    0.100,
                    0.00,
                    0.00,
                    0.00,
                    1.00,
                    10.0,
                    5.0,
                    10.0,
                    0.001,
                    0.001,
                    0.00,
                    0.00,
                    0.00,
                ]
            ),
            Max=_npf(
                [
                    300,
                    150,
                    0.750,
                    1.00,
                    1.00,
                    1.00,
                    5.00,
                    500.0,
                    400.0,
                    1000.0,
                    0.350,
                    0.050,
                    0.80,
                    1.00,
                    1.00,
                ]
            ),
        )
    else:
        raise Exception("Model identifier not recognised: " + model_id)
    return pSpec
