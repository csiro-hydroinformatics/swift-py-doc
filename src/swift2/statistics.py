from typing import Any, Dict, Sequence, TYPE_CHECKING
from swift2.internal import (
    TS_INTEROP_GEOM_KEY,
    TS_INTEROP_VALUES_KEY,
    simplify_time_series,
)

import swift2.wrap.swift_wrap_generated as swg
import swift2.wrap.swift_wrap_custom as swc
import pandas as pd
from cinterop.timeseries import TimeSeriesLike

if TYPE_CHECKING:
    from swift2.classes import Simulation, HypercubeParameteriser
    from swift2.classes import ObjectiveEvaluator


def multi_statistic_definition(
    model_var_ids, statistic_ids, objective_ids, objective_names, starts, ends
):
    """
    Collate information for use in multisite multiobjective definition

    Collate information for use in multisite multiobjective definition

    Args:
        model_var_ids (Any): character vector, model state identifiers where statistics are calculated
        statistic_ids (Any): character vector, identifiers for bivariate statistics (e.g. nse, lognse, et.)
        objective_ids (Any): character vector, identifiers for the objectives. Can be the same as modelVarIds.
        objective_names (Any): character vector, display names for the objectives. Can be the same as modelVarIds.
        starts (Any): POSIXct vector of start dates for statistics
        ends (Any): POSIXct vector of end dates for statistics

    """
    # stopifnot(is.character(model_var_ids))
    # stopifnot(is.character(statistic_ids))
    # stopifnot(is.character(objective_ids))
    # stopifnot(is.character(objective_names))
    # stopifnot(is.numeric(starts)) # TODO but not the right check. POSIXct
    # stopifnot(is.numeric(ends))

    return pd.DataFrame.from_dict(
        {
            "ModelVarId": model_var_ids,
            "StatisticId": statistic_ids,
            "ObjectiveId": objective_ids,
            "ObjectiveName": objective_names,
            "Start": starts,
            "End": ends,
        }
    )


def create_multisite_objective(
    simulation: "Simulation", 
    statspec: pd.DataFrame,
    observations: Sequence[TimeSeriesLike],
    weights: Dict[str, float],
):
    """
    Creates an objective that combines multiple statistics

    Creates an objective that combines multiple statistics. Used for joined, "whole of catchment" calibration

    Args:
        simulation (Simulation): A SWIFT simulation object (i.e. a model runner)
        statspec (pd.DataFrame): dataframe defining the objectives used. See function [`multi_statistic_definition`][swift2.statistics.multi_statistic_definition] to help build this dataframe.
        observations (Sequence[TimeSeriesLike]): A list of (time series) observations to calculated the statistics. Must be of same length as the number of rows of statspec.
        weights (Dict[str, float]): numeric vector of weights to ponderate each objective.

        Examples:
            >>> todo()
    """
    from swift2.wrap.ffi_interop import marshal

    # stopifnot(is.list(observations))
    # stopifnot(nrow(statspec) == length(observations))
    # stopifnot(nrow(statspec) == length(weights))
    interop_obs = [marshal.as_native_time_series(x) for x in observations]
    defn = {
        "Length": len(statspec),
        "Statistics": statspec,
        "Observations": interop_obs,
    }
    obj = swg.CreateMultisiteObjectiveEvaluator_py(simulation, defn, weights)
    return swg.WrapObjectiveEvaluatorWila_py(obj, True)


from cinterop.timeseries import ConvertibleToTimestamp


def create_objective(
    simulation: "Simulation",
    state_name: str,
    observation: TimeSeriesLike,
    statistic: str,
    start_date: ConvertibleToTimestamp,
    end_date: ConvertibleToTimestamp,
):
    """
    Creates an objective calculator

    Args:
        simulation (Simulation): A SWIFT simulation object (i.e. a model runner)
        state_name (Any): The name identifying the model state variable to calibrate against the observation
        observation (TimeSeriesLike): an xts
        statistic (str): statistic identifier, e.g. "NSE"
        start_date (ConvertibleToTimestamp): start date of the period to calculate statistics on
        end_date (ConvertibleToTimestamp): end date of the period to calculate statistics on
    """
    from swift2.internal import simplify_time_series
    from cinterop.timeseries import ts_window, as_timestamp

    start_date = as_timestamp(start_date)
    end_date = as_timestamp(end_date)

    # if(!is.xts(observation)):
    #     stop('observation must be an xts object')
    # }
    # if(ncol(observation) != 1):
    #     stop('observation must have exactly one series')
    # }
    observation = ts_window(observation, start_date, end_date)
    simple_ts = simplify_time_series(observation)
    return swg.CreateSingleObservationObjectiveEvaluatorWila_py(
        simulation,
        state_name,
        simple_ts[TS_INTEROP_VALUES_KEY],
        simple_ts[TS_INTEROP_GEOM_KEY],
        statistic,
    )


def createCompositeObjective(
    simulation, state_name, observation, yamlstring_statistic, start_date, end_date
):
    """
    Creates a composite objective calculator

    Creates a composite objective calculator

    Args:
        simulation (Simulation): A SWIFT simulation object (i.e. a model runner)
        state_name (Any): The name identifying the model state variable to calibrate against the observation
        observation (Any): an xts
        yamlstring_statistic (Any): a yaml string representing objective functions and weights eg...
        start_date (Any): start date of the period to calculate statistics on
        end_date (Any): end date of the period to calculate statistics on

    Returns:
        objective evaluator

    """
    import xarray as xr
    from cinterop.timeseries import ts_window

    # if not isinstance(observation, xr.DataArray):
    #     raise ValueError('observation must be an xts object')
    # if(ncol(observation) != 1):
    #     stop('observation must have exactly one series')
    # }
    observation = ts_window(observation, start_date, end_date)
    simple_ts = simplify_time_series(observation)
    return swg.CreateCompositeObservationObjectiveEvaluator_py(
        simulation,
        state_name,
        simple_ts[TS_INTEROP_VALUES_KEY],
        simple_ts[TS_INTEROP_GEOM_KEY],
        yamlstring_statistic,
    )


def _add_to_composite_obj(composite_obj, objective, weight: float, name: str):
    from refcount.interop import is_cffi_native_handle

    if is_cffi_native_handle(objective, "OBJECTIVE_EVALUATOR_PTR"):
        obj = objective
    elif is_cffi_native_handle(objective, "OBJECTIVE_EVALUATOR_WILA_PTR"):
        obj = swg.UnwrapObjectiveEvaluatorWila_py(objective)
    else:
        raise ValueError("Unsupported type of objective evaluator")
    swg.AddSingleObservationObjectiveEvaluator_py(composite_obj, obj, weight, name)


def create_composite_objective(
    objectives: Sequence["ObjectiveEvaluator"],
    weights: Sequence[float],
    names: Sequence[str],
) -> "ObjectiveEvaluator":
    assert len(objectives) == len(weights)
    assert len(objectives) == len(names)
    co = swg.CreateEmptyCompositeObjectiveEvaluator_py()
    for i, obj in enumerate(objectives):
        _add_to_composite_obj(co, obj, weights[i], names[i])
    co = swg.WrapObjectiveEvaluatorWila_py(co, clone=True)
    return co


def get_score(
    objective_evaluator: "ObjectiveEvaluator", p_set: "HypercubeParameteriser"
) -> Dict[str, Any]:
    """Evaluate an objective for a given parameterisation

    Args:
        objective_evaluator (ObjectiveEvaluator): objective evaluator
        p_set (HypercubeParameteriser): parameteriser

    Returns:
        Dict[str,Any]: score(s), and a data frame representation of the input parameters.
    """
    #  if (p_set.type_id == "HYPERCUBE_PTR"):
    #    p_set = ToHypercubeWila_py(p_set);
    #  }
    #  stopifnot(p_set.type_id=='HYPERCUBE_WILA_PTR')
    return swc.evaluate_score_wila_pkg(objective_evaluator, p_set)
