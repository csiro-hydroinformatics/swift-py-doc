from datetime import datetime
from typing import TYPE_CHECKING
from cinterop.cffi.marshal import CffiMarshal
from cinterop.timeseries import  as_timestamp
from refcount.interop import OwningCffiNativeHandle
from swift2.internal import (
    TS_INTEROP_GEOM_KEY,
    TS_INTEROP_VALUES_KEY,
    is_singular_simulation,
    simplify_time_series,
)
from swift2.parameteriser import get_max_runtime_termination, is_hypercube

import swift2.wrap.swift_wrap_generated as swg

if TYPE_CHECKING:
    from swift2.classes import SceTerminationCondition, HypercubeParameteriser

from cinterop.cffi.marshal import (
    TimeSeriesLike,
)

# ## #' Function name
# ## #'
# ## #' Function description
# ## #'
# ## #' @param sampleId TODO
# ## #' @return something
# ## #' @export
# ## getSampleModel(sampleId) {
# ## }


# #' @export
# prepareEnsembleModelRunner(simulation, warmup_start, warmup_end, observed_ts, error_model_element_id) {
#   stopifnot(xts::is.xts(observed_ts))
#   stopifnot(ncol(observed_ts) == 1)
#   simple_ts = simplifyTimeSeries(observed_ts)
#   warmup_start = as_timestamp(warmup_start, tz='UTC')
#   warmup_end = as_timestamp(warmup_end, tz='UTC')


#   emr = PrepareEnsembleModelRunner_R(simulation, warmup_start, warmup_end,
#     simple_ts$tsvalues[[1]], simple_ts$tsgeom, error_model_element_id)
#   return(emr)
# }

# #' @export
# setupEnsembleModelRunner(ensembleRunner, forecastStart, ensemble_size, forecastHorizonLength) {
#   SetupEnsembleModelRunner_R(ensembleRunner, forecastStart, ensemble_size, forecastHorizonLength)
# }

# #' @export
# recordEnsembleModelRunner(ensembleRunner, outputVarIdent) {
#   RecordEnsembleModelRunner_R(ensembleRunner, outputVarIdent)
# }

# #' Load a legacy text based SWIFT catchment definition.
# #'
# #' Load a legacy text based SWIFT catchment definition.
# #'
# #' @param controlFile a Unix style file path, or a windows style path which would look like e.g. '\\\\wron\\path\\to\\some\\controlfile.txt'
# #' @param dataDir (NOTE: KLUDGE) name of the directory containing the legacy TXT formats climate files e.g. for rainfall, evap and streamflow.
# #' @param simulation A SWIFT simulation object (i.e. a model runner)
# #' @export
# #' @examples
# #' \dontrun{
# #' library(ophct)
# #' controlFile = '\\\\OSM-01-MEL.it.csiro.au\\CLW_HYDROFORECAST_common\\Projects\\WIRADA_4_1\\Data\\Catchment_Data\\Ovens\\Ovens_for_CSIRO\\catchments\\ovens\\Setup\\SWIFT_Control.txt'
# #' dataDir = 'F:\\Data\\stsf\\ovens'
# #' ms = loadSwiftV1TextDef(controlFile, dataDir)
# #' flowRateName = 'Catchment|StreamflowRate'
# #' record_state(ms, flowRateName)
# #' execSimulation(ms)
# #' outflow = getRecorded(ms, flowRateName)
# #' plot(outflow)
# #' }
# loadSwiftV1TextDef (controlFile, dataDir) {
#   controlFile = mkPathToPlatform(controlFile)
#   dataDir = mkPathToPlatform(dataDir)
#   return(LoadVersionOneControlFile_R(controlFile, dataDir))
# }

# #' @export
# testNullReference(hydro_params)
# {
#   useHydroParams = True
#   if(is.null(hydro_params)) {
#     useHydroParams = False
#     hydro_params = createParameterizer()
#   }
#   TestNullReference_Pkg(useHydroParams, cinterop::getExternalXptr(hydro_params))
# }


#' @export
def create_erris_parameter_estimator(
    simulation,
    observed_ts,
    error_model_element_id,
    estimation_start,
    estimation_end,
    cens_thr,
    cens_opt,
    termination_condition=None,
    restriction_on=True,
    weighted_least_square=False,
):
    # stopifnot(xts::is.xts(observed_ts))
    # stopifnot(ncol(observed_ts) == 1)
    simple_ts = simplify_time_series(observed_ts)

    if termination_condition is None:
        termination_condition = get_max_runtime_termination()

    obs_values = simple_ts[TS_INTEROP_VALUES_KEY]
    obs_geom = simple_ts[TS_INTEROP_GEOM_KEY]

    return swg.CreateERRISParameterEstimator_py(
        simulation,
        obs_values,
        obs_geom,
        error_model_element_id,
        estimation_start,
        estimation_end,
        cens_thr,
        cens_opt,
        termination_condition,
        restriction_on,
        weighted_least_square,
    )


from swift2.wrap.ffi_interop import marshal

#' Estimates ERRIS model parameters
#'
#' Estimates ERRIS parameters
#'
#' @param simulation SWIFT simulation
#' @return a SWIFT parameteriser
#' @export
def estimate_erris_parameters(
    simulation,
    observed_ts,
    error_model_element_id,
    warmup_start,
    warmup_end,
    warmup,
    estimation_start,
    estimation_end,
    cens_thr,
    cens_opt,
    exclusion_start,
    exclusion_end,
    exclusion,
    termination_condition,
    hydro_params=None,
    erris_params=None,
    restriction_on=True,
    weighted_least_square=False,
):

    # stopifnot(xts::is.xts(observed_ts))
    # stopifnot(ncol(observed_ts) == 1)
    simple_ts = simplify_time_series(observed_ts)

    if hydro_params is None:
        hydro_params = OwningCffiNativeHandle(marshal.nullptr)

    if erris_params is None:
        erris_params = OwningCffiNativeHandle(marshal.nullptr)

    warmup_start = as_timestamp(warmup_start)
    warmup_end = as_timestamp(warmup_end)
    estimation_start = as_timestamp(estimation_start)
    estimation_end = as_timestamp(estimation_end)
    exclusion_start = as_timestamp(exclusion_start)
    estimation_end = as_timestamp(estimation_end)

    if termination_condition is None:
        termination_condition = get_max_runtime_termination()

    return swg.EstimateERRISParameters_py(
        simulation=simulation,
        obsValues=simple_ts[TS_INTEROP_VALUES_KEY],
        obsGeom=simple_ts[TS_INTEROP_GEOM_KEY],
        errorModelElementId=error_model_element_id,
        warmupStart=warmup_start,
        warmupEnd=warmup_end,
        warmup=warmup,
        estimationStart=estimation_start,
        estimationEnd=estimation_end,
        censThr=cens_thr,
        censOpt=cens_opt,
        exclusionStart=exclusion_start,
        exclusionEnd=exclusion_end,
        exclusion=exclusion,
        terminationCondition=termination_condition,
        # useErrisParams=useErrisParams,
        errisParams=erris_params,
        # useHydroParams=useHydroParams,
        hydroParams=hydro_params,
        restrictionOn=restriction_on,
        weightedLeastSquare=weighted_least_square,
    )


# #' Estimates Dual Pass Error correction model parameters
# #'
# #' Estimates Dual Pass Error correction model parameters
# #'
# #' @param simulation SWIFT simulation
# #' @return a SWIFT parameteriser
# #' @export
# EstimateDualPassParameters(simulation, observed_ts, error_model_element_id, warmup_start, warmup_end, warmup, estimation_start, estimation_end, windowL, windowDecayL, windowDecayS, useLongPass,objFuncDescYaml, exclusion_start, exclusion_end, exclusion,termination_condition)
# {
#   stopifnot(xts::is.xts(observed_ts))
#   stopifnot(ncol(observed_ts) == 1)
#   simple_ts = simplifyTimeSeries(observed_ts)

#   warmup_start = as_timestamp(warmup_start, tz='UTC')
#   warmup_end = as_timestamp(warmup_end, tz='UTC')
#   estimation_start = as_timestamp(estimation_start, tz='UTC')
#   estimation_end = as_timestamp(estimation_end, tz='UTC')
#   exclusion_start = as_timestamp(exclusion_start, tz='UTC')
#   estimation_end = as_timestamp(estimation_end, tz='UTC')

#   if(missing(termination_condition) || is.null(termination_condition)) {
#     termination_condition = getMaxRuntimeTermination()
#   }

#   return(EstimateDualPassParameters_R(simulation, simple_ts$tsvalues[[1]], simple_ts$tsgeom, error_model_element_id, warmup_start, warmup_end, warmup, estimation_start, estimation_end, windowL, windowDecayL, windowDecayS, useLongPass, objFuncDescYaml, exclusion_start, exclusion_end, exclusion,termination_condition))

# }

# #' Estimates Parmeters of a log-sinh transformed normal distribution
# #'
# #' Estimates Parmeters of a log-sinh transformed normal distribution using a parameteriser
# #'
# #' @param observed_ts  An timeseries of observed data
# #' @param estimation_start Start of estimation period (POSIXct)
# #' @param estimation_end End of estimation period (POSIXct)
# #' @param censor_threshold The value below which observations are treated a censored data (Default=0.0)
# #' @param exclusion_start Start of period exclued from estimation (POSIXct)
# #' @param exclusion_end End of period exclued from estimation (POSIXct)
# #' @param exclusion Use the exclusion period (bool)
# #' @param termination_condition A SWIFT termination condition used by the optimisation
# #' @param Params  A SWIFT parameteriser for the log-sinh transformation
# #' @return a SWIFT parameteriser
# #' @export
# EstimateTransformationParametersFlexi(observed_ts,  estimation_start, estimation_end, exclusion_start, exclusion_end, exclusion,termination_condition, Params)
# {
#   stopifnot(xts::is.xts(observed_ts))
#   stopifnot(ncol(observed_ts) == 1)
#   simple_ts = simplifyTimeSeries(observed_ts)

#    stopifnot(!is.null(Params))
#   estimation_start = as_timestamp(estimation_start, tz='UTC')
#   estimation_end = as_timestamp(estimation_end, tz='UTC')
#   exclusion_start = as_timestamp(exclusion_start, tz='UTC')
#   estimation_end = as_timestamp(estimation_end, tz='UTC')


#   if(missing(termination_condition) || is.null(termination_condition)) {
#     termination_condition = getMaxRuntimeTermination()
#   }

#   output = EstimateTransformationParametersMS_R(simple_ts$tsvalues[[1]], simple_ts$tsgeom,estimation_start, estimation_end, exclusion_start, exclusion_end, exclusion,termination_condition,Params)

#   return(output)

# }


# #' A function that creates a simple SWIFT catchment structure
# #'
# #' A function that creates a simple SWIFT catchment structure. This is available mostly for dual use in documentation (example code) and unit tests.
# #'  A simple text representation of the structure is:
# #'
# #'        s-a for lnk4(1.2)
# #'                 |
# #'                \|/         s-a for lnk3(4.4)
# #'         n3 --- lnk4 ---> \          |
# #'                           \        \|/
# #'     s-a for lnk5(2.3)      n4 --- lnk3 ---> \
# #'                |          /                  \      s-a for lnk1(1.5)
# #'               \|/        /                    \           |
# #'         n1 --- lnk5 --->/  s-a for lnk2(2.2)   \         \|/
# #'                                      |          n2 --- lnk1 ---> n6
# #'                                     \|/        /
# #'                              n5 --- lnk2 ---> /
# #'
# #' @return a named list of numeric and character vectors defining the connectivity of catchment nodes and links
# #' @export
# createDefaultTestCatchmentDefinition() {

#   node_ids=paste0('n', 1:6)
#   link_ids = paste0('lnk', 1:5)
#   defn = list(
#     node_ids=node_ids,
#     node_names = paste0(node_ids, '_name'),
#     link_ids=link_ids,
#     link_names = paste0(link_ids, '_name'),
#     from_node = paste0('n', c(2,5,4,3,1)),
#     to_node = paste0('n', c(6,2,2,4,4)),
#     areas_km2 = c(1.2, 2.3, 4.4, 2.2, 1.5),
#     runoff_model = 'GR4J'
#   )
#   defn
# }

# #' A function that creates a simple SWIFT catchment structure
# #'
# #' A function that creates a simple SWIFT catchment structure. This is available mostly for dual use in documentation (example code) and unit tests.
# #'
# #' @param defn a list with at least the named items "node_ids"     "node_names"   "link_ids"     "link_names"   "from_node"    "to_node"      "areas_km2"    "runoff_model"
# #' @export
# createTestCatchment(defn=createDefaultTestCatchmentDefinition(), data_id = "MMH", simul_start = "1990-01-01",
#     simul_end = "1995-12-31", model_id = "GR4J", tstep = "daily",
#     varname_rain = "P", varname_pet = "E") {
#   defnNames = c(
#     'node_ids',
#     'node_names',
#     'link_ids',
#     'link_names',
#     'from_node',
#     'to_node',
#     'areas_km2',
#     'runoff_model')
#   missingNames = defnNames[ !  (defnNames %in% names(defn))]
#   if(length(missingNames) > 0) stop(paste0('missing names in the expected list: ', paste(missingNames, collapse=', ')))
#   ms = createCatchment(defn$node_ids, defn$node_names, defn$link_ids, defn$link_names, defn$from_node, defn$to_node, defn$runoff_model, defn$areas_km2)
#   s_span = paste0(simul_start, "/", simul_end)
#   rain = sample_series(data_id, "rain")[s_span]
#   evap = sample_series(data_id, "evap")[s_span]
#   s = start(rain)
#   e = end(rain)
#   set_simulation_span(ms, s, e)
#   set_simulation_time_step(ms, tstep)
#   saIds = get_subarea_ids(ms)
#   for (saId in saIds) {
#     playSubareaInput(ms, input = rain, saId, varname_rain)
#     playSubareaInput(ms, input = evap, saId, varname_pet)
#   }
#   ms
# }


def estimate_transformation_parameters(
    calib_obs: TimeSeriesLike,
    estimation_start: datetime,
    estimation_end: datetime,
    censor_threshold: float,
    exclusion: bool,
    exclusion_start: datetime,
    exclusion_end: datetime,
    termination_condition: "SceTerminationCondition" = None,
) -> "HypercubeParameteriser":
    """Estimate the transformation parameters for a log-likelihood for a series of observations

    Args:
        calib_obs (TimeSeriesLike):  An timeseries of observed data
        estimation_start (datetime): Start of estimation period
        estimation_end (datetime): End of estimation period
        censor_threshold (float): The value below which observations are treated a censored data (Default=0.0)
        exclusion (bool): Start of period exclued from estimation
        exclusion_start (datetime): End of period exclued from estimation
        exclusion_end (datetime): Use the exclusion period (bool)
        termination_condition (SceTerminationCondition): A SWIFT termination condition used by the optimisation. Default max runtime of ~3 minutes if None.

    Returns:
        HypercubeParameteriser: transformation parameters
    """
    import swift2.internal as si

    CENS_OPTION = 2
    simple_ts = si.simplify_time_series(calib_obs)
    if termination_condition is None:
        termination_condition = get_max_runtime_termination()

    return swg.EstimateTransformationParameters_py(
        obsValues=simple_ts[si.TS_INTEROP_VALUES_KEY],
        obsGeom=simple_ts[si.TS_INTEROP_GEOM_KEY],
        estimationStart=estimation_start,
        estimationEnd=estimation_end,
        censThr=censor_threshold,
        censOpt=CENS_OPTION,
        exclusionStart=exclusion_start,
        exclusionEnd=exclusion_end,
        exclusion=exclusion,
        terminationCondition=termination_condition,
    )


#' @export
def clone(external_ptr):
    from refcount.interop import is_cffi_native_handle

    if not is_cffi_native_handle(external_ptr):
        raise Exception(
            "the clone function is only for wrapped external pointers; got an object of type "
            + str(type(external_ptr))
        )
    if is_hypercube(external_ptr):
        return swg.CloneHypercubeParameterizer_py(external_ptr)
    elif is_singular_simulation(external_ptr):
        return swg.CloneModel_py(external_ptr)
    else:
        raise Exception(
            "Clone operation not possible or not yet supported for external resource of native type "
            + str(external_ptr.type_id)
        )
