# This file contains code that cannot (yet?) be generated
# You can add features here, but this is not recommended. See rcpp_generated.cpp for
# prefered way to generate code from the SWIFT C API

from typing import TYPE_CHECKING, Dict, List, Sequence, Tuple, Any

import pandas as pd
import numpy as np

from refcount.interop import DeletableCffiNativeHandle, wrap_as_pointer_handle
from cinterop.cffi.marshal import as_bytes, geom_to_xarray_time_series, dtts_as_datetime
import uchronia.wrap.uchronia_wrap_generated as uwg
from swift2.wrap.ffi_interop import marshal, swift_so, check_exceptions
import swift2.wrap.swift_wrap_generated as swg

if TYPE_CHECKING:
    from swift2.classes import (
        Simulation,
        EnsembleSimulation,
        HypercubeParameteriser,
        CompositeParameteriser,
        FunctionsParameteriser,
        FilteringParameteriser,
        ObjectiveEvaluator,
        StateInitParameteriser,
        TransformParameteriser,
        ConstraintParameteriser,
        ScalingParameteriser,
        Optimiser,
        SceTerminationCondition,
        CandidateFactorySeed,
        ObjectiveScores,
        VectorObjectiveScores,
        ErrisStagedCalibration,
        MaerrisStagedCalibration,
        StateInitialiser,
        MemoryStates,
        EnsembleForecastSimulation,
    )
    from uchronia.classes import (
        EnsembleTimeSeries,
        TimeSeriesLibrary,
        EnsembleForecastTimeSeries,
        TimeSeries,
        EnsemblePtrTimeSeries,
        TimeSeriesProvider,
    )


# include "rcpp_custom.h"
# include "swift_struct_interop.h"

# using namespace Rcpp;
# using namespace cinterop::utils;

# define OPAQUE_POINTER void*
# define REF_HANDLE_OPAQUE_POINTER void* # opaque, but helps code readability and remember to reclaim these if transient objects in functions

# void callGc()
# {
#    Rcpp::Function gc("gc");
#    gc();
# }

# # Provide implementations for cinterop forward declarations
# delete_ansi_string_array(char** values, int arrayLength)
# {
#     DeleteAnsiStringArray(values, arrayLength);
# }

# delete_array(double* values)
# {
#     if (values != nullptr)
#         delete[] values;
# }

# # KLUDGE? needed to keep compiling this package as of Apr 2017.
# free_ansi_char_array(char** s, size_t length)
# {
#     if (s != nullptr)
#     {
#         for (size_t i = 0; i < length; i++)
#         {
#             if (s[i] != nullptr)
#                 delete[] s[i];
#         }
#         delete[] s;
#     }
# }

# MarshaledDateTime toDateTimeStruct(const Datetime& dt)
# {
#     return cinterop::utils::to_date_time_to_second(dt);
# }

# Datetime toDateTime(const MarshaledDateTime& mdt)
# {
#     return cinterop::utils::from_date_time_to_second<Rcpp::Datetime>(mdt);
# }

# NumericMatrix toNumericMatrix(const MultiTimeSeriesData& mts)
# {
#     return cinterop::rcpp::to_r_numeric_matrix(mts);
# }

# template <typename T>
# getIdName(T* x, int size, vector<string>& ids, vector<string>& names)
# {
#     ids = vector<string>(size);
#     names = vector<string>(size);
#     for (int i = 0; i < size; i++)
#     {
#         ids[i] = string(x[i].Id);
#         names[i] = string(x[i].Name);
#     }
# }

# SceParameters toSceParameters(const NumericVector& sce_params)
# {
#     return mhcpp::interop::r::ToSceParameters(sce_params);
# }

# NumericVector toPosixCtDateTime(const MarshaledDateTime& mdt)
# {
#     return cinterop::utils::to_posix_ct_date_time<Rcpp::NumericVector>(mdt);
# }

# toMarshalledTsinfo(const Rcpp::S4& rTsInfo, regular_time_series_geometry& mts)
# {
#     cinterop::timeseries::to_regular_time_series_geometry(rTsInfo, mts);
# }

# regular_time_series_geometry toMarshalledTsinfo(const Rcpp::S4& rTsInfo)
# {
#     return cinterop::timeseries::to_regular_time_series_geometry(rTsInfo);
# }

# regular_time_series_geometry* toMarshalledTsinfoPtr(const Rcpp::S4& rTsInfo)
# {
#     return cinterop::timeseries::to_regular_time_series_geometry_ptr(rTsInfo);
# }

# Rcpp::S4 fromMarshalledTsinfo(const MarshaledTsGeometry& mts)
# {
#     return cinterop::timeseries::from_regular_time_series_geometry<Rcpp::S4>(mts);
# }

# Rcpp::S4 createSwiftRef(const XPtr<opaque_pointer_handle>& xptr, const string& type = "")
# {
#     return cinterop::create_rcpp_xptr_wrapper<opaque_pointer_handle>(xptr, type);
# }

# Rcpp::S4 createSwiftRef(OPAQUE_POINTER swiftApiResult, const string& type = "")
# {
#     return cinterop::create_rcpp_xptr_wrapper<opaque_pointer_handle>(swiftApiResult, type);
# }

# /**
#  * \fn    MultiTimeSeriesData toMultiTimeSeriesData(const Rcpp::S4& timeSeriesEnsemble)
#  *
#  * \brief    Converts a timeSeriesEnsemble to a multi time series data.
#  *
#  * \param    timeSeriesEnsemble    The time series ensemble, as an S4 object of type SwiftMultiTimeSeriesData
#  *
#  * \return    timeSeriesEnsemble as a MultiTimeSeriesData.
#  */

# multi_regular_time_series_data toMultiTimeSeriesData(const Rcpp::S4& timeSeriesEnsemble)
# {
#     return cinterop::timeseries::to_multi_regular_time_series_data(timeSeriesEnsemble);
# }

# Rcpp::S4 toRMultiTimeSeriesData(const multi_regular_time_series_data& mts)
# {
#     return cinterop::timeseries::from_multi_regular_time_series_data<Rcpp::S4>(mts);
# }

# PkgDisposeMultiTimeSeriesData(MultiTimeSeriesData& d)
# {
#     cinterop::disposal::dispose_of<multi_regular_time_series_data>(d);
# }


def _array_for_geom(mtsg) -> np.ndarray:
    return np.empty((mtsg.length,))


def _get_pp_data(simulation: Any, variable_identifier: str, mtsg, gaom_func, data_func):
    # v = marshal.as_charptr(variable_identifier, True)
    gaom_func(simulation, variable_identifier, mtsg)
    values = _array_for_geom(mtsg)
    data_func(simulation.ptr, variable_identifier, values, mtsg.length)
    return values


def get_played_data(simulation: Any, variable_identifier: str, mtsg):
    return _get_pp_data(
        simulation,
        variable_identifier,
        mtsg,
        swg.GetPlayedTsGeometry_py,
        swg.GetPlayed_py,
    )


def get_recorded_data(simulation: Any, variable_identifier: str, mtsg):
    return _get_pp_data(
        simulation,
        variable_identifier,
        mtsg,
        swg.GetRecordedTsGeometry_py,
        swg.GetRecorded_py,
    )


def get_played_pkg(simulation: "Simulation", variable_identifier):
    mtsg = marshal.new_native_tsgeom()
    values = get_played_data(simulation, variable_identifier, mtsg)
    return geom_to_xarray_time_series(mtsg, values)


def get_recorded_pkg(simulation: "Simulation", variable_identifier):
    mtsg = marshal.new_native_tsgeom()
    values = get_recorded_data(simulation, variable_identifier, mtsg)
    return geom_to_xarray_time_series(mtsg, values)


def get_time_series_data_from_provider(provider: Any, variable_identifier, mtsg):
    uwg.GetProviderTsGeometry_py(provider, variable_identifier, mtsg)
    values = _array_for_geom(mtsg)
    uwg.GetProviderTimeSeriesValues_py(
        provider, variable_identifier, values, mtsg.length
    )
    return values


def _get_param_space(p: pd.DataFrame):
    pnames = p["Name"].values
    minima = p["Min"].values
    maxima = p["Max"].values
    values = p["Value"].values
    return (pnames, minima, maxima, values)


# [[Rcpp::export]]
def add_parameters_pkg(parameteriser, parameter_specs: pd.DataFrame):
    ps = parameter_specs
    p = parameteriser
    pnames, minima, maxima, values = _get_param_space(ps)
    for i in range(len(parameter_specs)):
        swg.AddParameterDefinition_py(p, pnames[i], minima[i], maxima[i], values[i])


# [[Rcpp::export]]
def set_parameters_pkg(parameteriser, parameter_specs):
    ps = parameter_specs
    p = parameteriser
    pnames, minima, maxima, values = _get_param_space(ps)
    for i in range(len(parameter_specs)):
        swg.SetParameterDefinition_py(p, pnames[i], minima[i], maxima[i], values[i])


# std::vector<mhcpp::interop::ParameterDefinition> InspectHypercube(OPAQUE_POINTER hypercube)
# {
#     using mhcpp::interop::ParameterDefinition;
#     # This may be pushed to the SWIFT C API later on.
#     OPAQUE_POINTER p = hypercube;
#     std::vector<ParameterDefinition> result;

#     int n = GetNumParameters(p);
#     for i in range(n):
#     {
#         ParameterDefinition pd;
#         char * pName = GetParameterName(p, i);
#         pd.Name = pName;
#         pd.Min = GetParameterMinValue(p, pName);
#         pd.Max = GetParameterMaxValue(p, pName);
#         pd.Value = GetParameterValue(p, pName );
#         DeleteAnsiString(pName);
#         result.push_back(pd);
#     }
#     return result;
# }

# DataFrame HypercubeToDataFrame(OPAQUE_POINTER hypercube)
# {
#     mhcpp::interop::ParameterSetDefinition<> pdef(InspectHypercube(hypercube));
#     return mhcpp::interop::r::HypercubeToDataFrame<>(pdef);
# }

# [[Rcpp::export]]
def parameteriser_to_data_frame_pkg(parameteriser):
    from swift2.common import _df_from_dict

    n = swg.GetNumParameters_py(parameteriser)
    # return HypercubeToDataFrame(parameteriser)
    pnames = [swg.GetParameterName_py(parameteriser, i) for i in range(n)]
    minima = [swg.GetParameterMinValue_py(parameteriser, pnames[i]) for i in range(n)]
    maxima = [swg.GetParameterMaxValue_py(parameteriser, pnames[i]) for i in range(n)]
    values = [swg.GetParameterValue_py(parameteriser, pnames[i]) for i in range(n)]

    return _df_from_dict(Name=pnames, Value=values, Min=minima, Max=maxima)


def _get_scores(scores):
    n = swg.GetNumScoresWila_py(scores)
    names = [swg.GetScoreNameWila_py(scores, i) for i in range(n)]
    values = [swg.GetScoreWila_py(scores, i) for i in range(n)]
    return (values, names)


def _scores_as_flat_dict(scores):
    values, names = _get_scores(scores)
    s = dict(zip(names, values))
    p = swg.GetSystemConfigurationWila_py(scores)
    n = swg.GetNumParameters_py(p)
    pnames = [swg.GetParameterName_py(p, i) for i in range(n)]
    pvalues = [swg.GetParameterValue_py(p, pnames[i]) for i in range(n)]
    s.update(zip(pnames, pvalues))
    return s

def fitnesses_as_rpy_dict(scores: "ObjectiveScores") -> Dict[str, float]:
    values, names = _get_scores(scores)
    return dict(zip(names, values))

def scores_as_rpy_dict(scores: "ObjectiveScores") -> Dict[str, Any]:
    values, names = _get_scores(scores)
    swift_hc_parameteriser = swg.GetSystemConfigurationWila_py(scores)

    result = {
        "scores": dict(zip(names, values)),
        "sysconfig": parameteriser_to_data_frame_pkg(swift_hc_parameteriser),
    }
    # dispose_reference_handle(swift_hc_parameteriser);
    return result


# [[Rcpp::export]]
def scores_as_rpy_dict_pkg(scores_wrapper: Any):
    return scores_as_rpy_dict(scores_wrapper)


# [[Rcpp::export]]
def evaluate_score_wila_pkg(objectives, parameteriser):
    scores = swg.EvaluateScoreForParametersWila_py(objectives, parameteriser)
    result = scores_as_rpy_dict(scores)
    # dispose_reference_handle(scores);
    return result


# # [[Rcpp::export]]
# List EvaluateScoreWilaInitState_Pkg(XPtr<opaque_pointer_handle> objectives, XPtr<opaque_pointer_handle> parameteriser)
# {
#     REF_HANDLE_OPAQUE_POINTER scores = EvaluateScoreForParametersWilaInitState(objectives, parameteriser);
#     List result = scores_as_rpy_dict(scores);
#     dispose_reference_handle(scores);
#     return result;
# }

# # [[Rcpp::export]]
# List get_recorded_pkg(XPtr<opaque_pointer_handle> simulation, CharacterVector variable_identifier)
# {
#     MarshaledTsGeometry mtsg;
#     auto values = get_recorded_data(simulation, variable_identifier, mtsg);
#     return CreateTsInfo(values, mtsg);
# }


# SwiftNativeExceptionHandler(const char * str)
# {
#     std::string msg(str);
#     # Because Rcpp has its own exception handling meachanism, we just rethrow
#     throw std::runtime_error(msg);
#     # Calling Rcpp::stop(msg) is no good,  it seems, as it leads to buffer overrun in Release mode.
#     #Rcpp::stop(msg);
# }

# # [[Rcpp::export]]
# RegisterExceptionCallback_Pkg()
# {
#     OPAQUE_POINTER exceptionHandlerFun = (OPAQUE_POINTER)(&SwiftNativeExceptionHandler);
#     RegisterExceptionCallback(exceptionHandlerFun);

# }

# [[Rcpp::export]]
def default_sce_parameters_pkg(n=4, nshuffle=40):
    # TODO: consider whether need to expose C++ template. Tricky if not in the C API.
    # SceParameters s = CreateDefaultSceParameters<SceParameters>()
    m = 2 * n + 1
    return {
        "P": n + 2,
        "Pmin": n + 2,
        "M": 2 * n + 1,
        "Q": max(m - 2, 2),
        "Alpha": 1,
        "Beta": m,
        "NumShuffle": nshuffle,
        "TrapezoidalDensityParameter": 1.0,
        "ReflectionRatio": -1.0,
        "ContractionRatio": 0.5,
    }
    # return FromSceParameters<NumericVector>(s);


# [[Rcpp::export]]
def vec_scores_as_dataframe_pkg(setOfScores) -> pd.DataFrame:
    vectorOfScores = setOfScores
    n = swg.GetLengthSetOfScores_py(vectorOfScores)
    rows = [
        _scores_as_flat_dict(swg.GetScoresAtIndex_py(vectorOfScores, i))
        for i in range(n)
    ]
    return pd.DataFrame(rows)


# std::vector<std::string> CreateVecStr(char** values, int length)
# {
#     std::vector<std::string> res;
#     for (int i = 0; i < length; i++)
#     {
#         res.push_back(string(values[i]));
#     }
#     return res;
# }

from swift2.common import _df_from_dict


def convert_optimisation_logger(
    log_data: DeletableCffiNativeHandle, add_numbering=False
):
    if log_data is None:
        raise ValueError("OptimizerLogData* log_data cannot be nullptr")

    ptr = log_data.ptr
    numRows = ptr.LogLength
    if numRows == 0:
        return pd.DataFrame()

    names = marshal.c_charptrptr_as_string_list(
        ptr.NamesStringData, ptr.StringDataCount
    )
    num_names = marshal.c_charptrptr_as_string_list(
        ptr.NamesNumericData, ptr.NumericDataCount
    )
    # columns with categorical values (strings)
    str_data = [
        (names[i], marshal.c_charptrptr_as_string_list(ptr.StringData[i], numRows))
        for i in range(ptr.StringDataCount)
    ]
    # columns with numeric values (parameter values, objectives)
    num_data = [
        (num_names[i], marshal.as_numeric_np_array(ptr.NumericData[i], numRows))
        for i in range(ptr.NumericDataCount)
    ]
    nbs = []
    if add_numbering:
        nbs = [("PointNumber", np.arange(1, numRows + 1, dtype=int))]
    d = dict(str_data + num_data + nbs)
    return _df_from_dict(**d)


# # [[Rcpp::export]]
# DataFrame GetOptimizationLogWila_Pkg(XPtr<opaque_pointer_handle> optimiser)
# {
#     OPAQUE_POINTER opt = optimiser;
#     OptimizerLogData* log_data = GetOptimizerLogDataWila(opt);
#     return convert_optimisation_logger(log_data);
# }

# # [[Rcpp::export]]
# DataFrame GetOptimizationLogWilaERRIS_Pkg(XPtr<opaque_pointer_handle> optimiser)
# {
#     OPAQUE_POINTER opt = optimiser;
#     OptimizerLogData* log_data = GetERRISCalibrationLog(opt);
#     return convert_optimisation_logger(log_data);
# }

# [[Rcpp::export]]
def aggregate_parameterisers_pkg(
    strategy: str, parameterisers: Sequence[DeletableCffiNativeHandle]
):
    n = len(parameterisers)
    ct = marshal.new_ctype_array("void*", n)
    for i in range(n):
        ct[i] = parameterisers[i].ptr
    return swg.AggregateParameterizers_py(strategy, ct, n)
    # OPAQUE_POINTER* ptrs = new OPAQUE_POINTER[n];
    # for i in range(n):
    # {
    #     XPtr<opaque_pointer_handle> xptr = Rcpp::as<XPtr<opaque_pointer_handle>>(parameterisers[i]);
    #     ptrs[i] = (xptr);
    # }
    # OPAQUE_POINTER result = AggregateParameterizers(strategy[0], ptrs, n);
    # delete[] ptrs;
    # auto x = XPtr<opaque_pointer_handle>(new opaque_pointer_handle(result));
    # return createSwiftRef(x, string("COMPOSITE_PARAMETERIZER_PTR"));


# [[Rcpp::export]]
@check_exceptions
def subset_model_pkg(
    simulation,
    element_name: str,
    select_network_above_element: bool,
    include_element_in_selection: bool,
    invert_selection: bool,
) -> "Simulation":

    termination_elements_charpp = marshal.nullptr
    termination_elements_length: int = 0
    simulation_xptr = wrap_as_pointer_handle(simulation)
    element_name_c_charp = wrap_as_pointer_handle(as_bytes(element_name))
    result = swift_so.SubsetModel(
        simulation_xptr.ptr,
        element_name_c_charp.ptr,
        select_network_above_element,
        include_element_in_selection,
        invert_selection,
        termination_elements_charpp,
        termination_elements_length,
    )
    return swg.custom_wrap_cffi_native_handle(result, "MODEL_SIMULATION_PTR")


# # [[Rcpp::export]]
# List GetTimeSeriesFromProvider_Pkg(XPtr<opaque_pointer_handle> provider, CharacterVector variable_identifier)
# {
#     MarshaledTsGeometry mtsg;
#     auto values = get_time_series_data_from_provider(provider, variable_identifier, mtsg);
#     return CreateTsInfo(values, mtsg);
# }

# [[Rcpp::export]]
def sort_simulation_elements_by_run_order_pkg(
    simulation, elements_ids, ordering_option
):
    return swg.SortSimulationElementsByRunOrder_py(
        simulation, elements_ids, len(elements_ids), ordering_option
    )


# [[Rcpp::export]]
def get_catchment_structure_pkg(simulation):

    # raise NotImplementedError("get_catchment_structure_pkg not implemented")
    cat_struct = swg.GetCatchmentStructure_py(simulation)
    c = cat_struct.ptr
    n_nodes = c.NumNodes
    n_links = c.NumLinks
    n_sa = c.NumSubareas
    linklengths = []
    f = []
    manningsN = []
    slope = []
    subareaAreas = []
    nlcDown = []
    nlcUp = []
    nlcIds = []
    nodeids = []
    nodenames = []
    linkids = []
    linknames = []
    saids = []
    sanames = []
    # getIdName<NodeInfo>(c.Nodes, c.NumNodes, nodeids, nodenames);
    # getIdName<LinkInfo>(c.Links, c.NumLinks, linkids, linknames);
    # getIdName<SubareaInfo>(c.Subareas, c.NumSubareas, saids, sanames);
    # vector<double> linklengths(c.NumLinks), f(c.NumLinks), manningsN(c.NumLinks), slope(c.NumLinks), subareaAreas(c.NumSubareas);

    from swift2.wrap.ffi_interop import marshal
    def as_str(x):
        return marshal.c_string_as_py_string(x)

    for i in range(n_nodes):
        n = c.Nodes[i]
        nodeids.append(as_str(n.Id))
        nodenames.append(as_str(n.Name))

    for i in range(n_links):
        lnk = c.Links[i]
        linkids.append(as_str(lnk.Id))
        linknames.append(as_str(lnk.Name))
        linklengths.append(lnk.LengthMetres)
        f.append(lnk.f)
        manningsN.append(lnk.ManningsN)
        slope.append(lnk.Slope)

    for i in range(n_sa):
        sa = c.Subareas[i]
        saids.append(as_str(sa.Id))
        sanames.append(as_str(sa.Name))
        subareaAreas.append(sa.SubareaSurfaceKm2)

    # CharacterVector nlcDown(c.NumNodeLinkConnections);
    # CharacterVector nlcUp(c.NumNodeLinkConnections);
    # CharacterVector nlcIds(c.NumNodeLinkConnections);
    for i in range(c.NumNodeLinkConnections):
        nlc = c.NodeLinkConnections[i]
        nlcDown.append(as_str(nlc.DownstreamNodeId))
        nlcUp.append(as_str(nlc.UpstreamNodeId))
        nlcIds.append(as_str(nlc.LinkId))

    slcSubarea = []
    slcLink = []
    # CharacterVector slcSubarea(c.NumSubareaLinkConnections);
    # CharacterVector slcLink(c.NumSubareaLinkConnections);
    for i in range(c.NumSubareaLinkConnections):
        slc = c.SubareaLinkConnections[i]
        slcSubarea.append(as_str(slc.SubareaId))
        slcLink.append(as_str(slc.LinkId))
    # }



    NAME_ITEM_NAME = "Name"
    NODE_ITEM_NAME = "Node"
    LINK_ITEM_NAME = "Link"
    ID_ITEM_NAME = "Id"

    result = {
        NODE_ITEM_NAME: pd.DataFrame(
            {
                ID_ITEM_NAME: nodeids,
                NAME_ITEM_NAME: nodenames,
            }
        ),
        LINK_ITEM_NAME: pd.DataFrame(
            {
                ID_ITEM_NAME: linkids,
                NAME_ITEM_NAME: linknames,
                "LengthMetres": linklengths,
                "f": f,
                "ManningsN": manningsN,
                "Slope": slope,
            }
        ),
        "Subarea": pd.DataFrame(
            {
                ID_ITEM_NAME: saids,
                NAME_ITEM_NAME: sanames,
                "AreaKm2": subareaAreas,
            }
        ),
        "NodeLink": pd.DataFrame(
            {
                "DownstreamId": nlcDown,
                "UpstreamId": nlcUp,
                "LinkId": nlcIds,
            }
        ),
        "SubareaLink": pd.DataFrame(
            {
                "LinkId": slcLink,
                "SubareaId": slcSubarea,
            }
        ),
    }

    return result


# TestTestNullReference(OPAQUE_POINTER ptr)
# {
#     if (!(ptr == nullptr)) Rcpp::warning(string("Failed nullptr test"));
# }

# # 2016-01 A test function only
# # [[Rcpp::export]]
# TestNullReference_Pkg(LogicalVector useHydroParams, XPtr<opaque_pointer_handle> hydro_parameterisers)
# {
#     bool b = useHydroParams[0];
#     OPAQUE_POINTER hcp = b ? hydro_parameterisers : nullptr;
#     TestTestNullReference(hcp);
# }

# # 2016-01 allowing nullptr to be passed as an argument to ERRIS
# # [[Rcpp::export]]
# S4 EstimateERRISParameters_Pkg(XPtr<opaque_pointer_handle> simulation, NumericVector obsValues, const Rcpp::S4& obsGeom, CharacterVector errorModelElementId, Rcpp::Datetime warmupStart, Rcpp::Datetime warmupEnd, LogicalVector warmup, Rcpp::Datetime estimationStart, Rcpp::Datetime estimationEnd, NumericVector censThr, NumericVector censOpt, Rcpp::Datetime exclusionStart, Rcpp::Datetime exclusionEnd, LogicalVector exclusion, XPtr<opaque_pointer_handle> terminationCriterion, LogicalVector useErrisParams, XPtr<opaque_pointer_handle> errisParams, LogicalVector useHydroParams, XPtr<opaque_pointer_handle> hydro_parameterisers, LogicalVector restrictionOn, LogicalVector weightedLeastSquare)
# {
#     MarshaledTsGeometry* obsGeom_tsgeom = toMarshalledTsinfoPtr(obsGeom);
#     MarshaledDateTime warmupStart_datetime = toDateTimeStruct(warmupStart);
#     MarshaledDateTime warmupEnd_datetime = toDateTimeStruct(warmupEnd);
#     MarshaledDateTime estimationStart_datetime = toDateTimeStruct(estimationStart);
#     MarshaledDateTime estimationEnd_datetime = toDateTimeStruct(estimationEnd);
#     MarshaledDateTime exclusionStart_datetime = toDateTimeStruct(exclusionStart);
#     MarshaledDateTime exclusionEnd_datetime = toDateTimeStruct(exclusionEnd);

#     bool b = useHydroParams[0];
#     OPAQUE_POINTER pHydroParams = b ? hydro_parameterisers : nullptr;
#     b = useErrisParams[0];
#     OPAQUE_POINTER pErrisParams = b ? errisParams : nullptr;
#     OPAQUE_POINTER tc = terminationCriterion;
#     OPAQUE_POINTER result = EstimateERRISParameters(simulation, &(obsValues[0]), obsGeom_tsgeom, errorModelElementId[0], warmupStart_datetime, warmupEnd_datetime, as<bool>(warmup),
#         estimationStart_datetime, estimationEnd_datetime, as<double>(censThr), as<double>(censOpt), exclusionStart_datetime, exclusionEnd_datetime, as<bool>(exclusion),
#         tc, pErrisParams, pHydroParams, as<bool>(restrictionOn), as<bool>(weightedLeastSquare));
#     delete obsGeom_tsgeom;
#     # warmupStart_datetime - no cleanup needed
#     # warmupEnd_datetime - no cleanup needed
#     # estimationStart_datetime - no cleanup needed
#     # estimationEnd_datetime - no cleanup needed
#     # exclusionStart_datetime - no cleanup needed
#     # exclusionEnd_datetime - no cleanup needed
#     auto x = createSwiftRef(result, string("HYPERCUBE_PTR"));
#     return x;
# }

# [[Rcpp::export]]
def get_simulation_span_pkg(simulation):
    start = marshal.new_date_time_to_second()
    end = marshal.new_date_time_to_second()
    swg.GetStart_py(simulation, start)
    swg.GetEnd_py(simulation, end)
    tstep_char = swg.GetTimeStepName_py(simulation)
    return {
        "start": dtts_as_datetime(start.ptr),
        "end": dtts_as_datetime(end.ptr),
        "time step": tstep_char,
    }


# # [[Rcpp::export]]
# CharacterVector GetModelConfigurationSwift_Pkg(XPtr<opaque_pointer_handle> simulation, CharacterVector elementId)
# {
#     string_string_map* models = GetModelConfigurationSwift(simulation, elementId[0]);
#     return cinterop::utils::from_string_string_map_ptr<CharacterVector>(models, false);
#     DisposeStringStringMapSwift(models);
# }

# import cinterop
# # [[Rcpp::export]]
# def EvaluateScoresForParametersWila_Pkg(objectiveEvaluator, parameteriser):
#     scores = swg.EvaluateScoresForParametersWila_py(objectiveEvaluator, parameteriser)
#     marshal.named_values_to_dict(scores)
#     res = cinterop::utils::from_named_values_vector_ptr<NumericVector>(scores, false)
#     DisposeNamedValuedVectorsSwift(scores);
# }
