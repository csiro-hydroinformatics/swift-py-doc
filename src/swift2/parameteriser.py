from typing import TYPE_CHECKING, Any, Dict, List, Sequence

import numpy as np
import pandas as pd
from refcount.interop import (
    CffiNativeHandle,
    DeletableCffiNativeHandle,
    is_cffi_native_handle,
)

if TYPE_CHECKING:
    from swift2.classes import (
        CompositeParameteriser,
        HypercubeParameteriser,
        ObjectiveScores,
        SceTerminationCondition,
        Simulation,
        TransformParameteriser,
    )
import swift2.wrap.swift_wrap_custom as swc
import swift2.wrap.swift_wrap_generated as swg
from swift2.common import _df_from_dict, _npf
from swift2.const import VecNum, VecStr
from swift2.utils import is_common_iterable


def _sapply_parameter_set(parameteriser, variable_name, value, api_func):

    # stopifnot(len(variable_name) == len(value) )
    if isinstance(variable_name, str):
        variable_name = [variable_name]
        value = [value]
    for i in range(len(variable_name)):
        api_func(parameteriser, variable_name[i], value[i])


#' Sets the value of a model parameter value
#'
#' Sets the value of a model parameter value
#'
#' @param parameteriser A SWIFT native parameteriser.
#' @param variable_name character, model variable state identifier(s)
#' @param value numeric value(s)
#' @export
def set_parameter_value(parameteriser, variable_name, value):
    """Sets the value of a model parameter value

    Args:
        parameteriser (HypercubeParameteriser): A HypercubeParameteriser wrapper, or a type inheriting from it
        variable_name (str or iterable of str): model variable state identifier(s)
        value (numeric or iterable of numeric): value(s)
    """
    _sapply_parameter_set(parameteriser, variable_name, value, swg.SetParameterValue_py)


#' Sets the maximum value of a model parameter value
#'
#' Sets the maximum value of a model parameter value
#'
#' @param parameteriser A SWIFT native parameteriser.
#' @param variable_name character, model variable state identifier(s)
#' @param value numeric value(s)
#' @export
def set_max_parameter_value(parameteriser, variable_name, value):
    """Sets the maximum value of a model parameter value

    Args:
        parameteriser (HypercubeParameteriser): A HypercubeParameteriser wrapper, or a type inheriting from it
        variable_name (str or iterable of str): model variable state identifier(s)
        value (numeric or iterable of numeric): value(s)
    """
    _sapply_parameter_set(
        parameteriser, variable_name, value, swg.SetMaxParameterValue_py
    )


#' Sets the minimum value of a model parameter value
#'
#' Sets the minimum value of a model parameter value
#'
#' @param parameteriser A SWIFT native parameteriser.
#' @param variable_name character, model variable state identifier(s)
#' @param value numeric value(s)
#' @export
def set_min_parameter_value(parameteriser, variable_name, value):
    """Sets the minimum value of a model parameter value

    Args:
        parameteriser (HypercubeParameteriser): A HypercubeParameteriser wrapper, or a type inheriting from it
        variable_name (str or iterable of str): model variable state identifier(s)
        value (numeric or iterable of numeric): value(s)
    """
    _sapply_parameter_set(
        parameteriser, variable_name, value, swg.SetMinParameterValue_py
    )


#' Create a SWIFT parameteriser
#'
#' Create a SWIFT parameteriser
#'
#' @param type A string identifying the (likely SWIFT-specific) type of parameteriser to use. Recognised types are (case insensitive) 'log-likelihood', 'generic', 'subareas', 'links', 'nodes' and 'muskingum'.
#'      These can be a combination, e.g. 'generic subarea' means that the parameteriser is a list of parameter names applicable to each subarea in the catchment.
#' @param specs An optional data frame description of the parameter set, with at least columns Name, Min, Max, Value.
#' @return an external pointer, a parameteriser (a.k.a a system configuration)
#' @examples
#' \dontrun{
#' (pspec_gr4j = joki::getFreeParams('GR4J'))
#' pspec_gr4j$Name = paste0('subarea.Subarea.', pspec_gr4j$Name)
#' p = createParameterizer(type='Generic', pspec_gr4j)
#' parameteriserAsDataFrame(p)
#' ms = createSubareaSimulation(data_id='MMH', simul_start='1990-01-01', simul_end='2005-12-31', model_id='GR4J', tstep='daily', varname_rain='P', varname_pet='E')
#' applySysConfig(p, ms)
#' }
#' @export
def create_parameteriser(type="Generic subareas", specs: pd.DataFrame = None):
    """Create a SWIFT parameteriser

    Args:
        type (str, optional): A string identifying the (likely SWIFT-specific) type of parameteriser to use. Recognised types are (case insensitive) 'log-likelihood', 'generic', 'subareas', 'links', 'nodes' and 'muskingum'. Defaults to "Generic subareas".
        specs (pd.DataFrame, optional): An optional data frame description of the parameter set, with at least columns Name, Min, Max, Value. Defaults to None.

    Returns:
        [HypercubeParameteriser]: new parameteriser
    """
    p = swg.CreateHypercubeParameterizer_py(strategy=type)
    # TODO: consider how to reuse mh::setHyperCube without introducing an undesirable package dependency
    # Maybe pass a function to a function in the mh package
    if specs is not None:
        add_to_hypercube(p, specs)
    return p


def subcatchment_parameteriser(parameteriser, subcatchment):
    """Create a parameteriser that gets applied to a subset of a whole catchment

    Args:
        parameteriser (HypercubeParameteriser): A HypercubeParameteriser wrapper, or a type inheriting from it
        subcatchment (Simulation): the subcatchment, subset of a whole catchment, identifying which elements (subareas, nodes, links) will be parameterised by the new parameteriser. Other catchment elements are untouched.

    Returns:
        [HypercubeParameteriser]: New parameteriser whose application is limited to the subcatchment.

    Examples:
        >>> sub_cats = simulation.split_to_subcatchments(["node.node_7", "node.node_10"])
        >>> sc = sub_cats["node.node_7"]
        >>> p = sp.create_parameteriser('generic subarea')
        >>> p.add_parameter_to_hypercube("x1", 32, 1, 6e3)
        >>> sp = p.subcatchment_parameteriser(sc)
        >>> sp.apply_sys_config(simulation)

    """
    p = swg.CreateSubcatchmentHypercubeParameterizer_py(parameteriser, subcatchment)
    return p


#' Add entries to a hypercube
#'
#' Add entries to a hypercube
#'
#' @param parameteriser an S4 object 'ExternalObjRef' [package "cinterop"] with external pointer type HYPERCUBE_PTR, or coercible to it
#' @param specs A data frame description of the additional parameters, with at least columns Name, Min, Max, Value.
#' @export
def add_to_hypercube(parameteriser, specs):
    """Add entries to a hypercube

    Args:
        parameteriser (HypercubeParameteriser): A HypercubeParameteriser wrapper, or a type inheriting from it
        specs (pd.DataFrame): An optional data frame description of the parameter set, with at least columns Name, Min, Max, Value.
    """
    swc.add_parameters_pkg(parameteriser, specs)


def set_hypercube(parameteriser: "HypercubeParameteriser", specs: pd.DataFrame):
    """Set the properties of a hypercube parameteriser

    Args:
        parameteriser (HypercubeParameteriser): A HypercubeParameteriser wrapper, or a type inheriting from it
        specs (pd.DataFrame): An optional data frame description of the parameter set, with at least columns Name, Min, Max, Value.
    """
    swc.set_parameters_pkg(parameteriser, specs)


#'
#' @param parameteriser A SWIFT native parameteriser.
#' @return A SWIFT catchment parameteriser for a model structure
#' @export
#' @examples
#' \dontrun{
#' ref_area = 250
#' time_span = as.integer(lubridate::dhours(1))
#' p = gr4jScaledParameterizer(ref_area, time_span)
#' (pspec_gr4j = joki::getFreeParams('GR4J'))
#' pspec_gr4j$Min = c(1.0E+00, -2.70E+01, 1.0E+00, 1.0E+00)
#' pspec_gr4j$Max = c(5.0E+03,  2.70E+01, 6.6E+02, 2.4E+02)
#' setHyperCube(p, pspec_gr4j)
#' parameteriserAsDataFrame(p)
#' ptrans = wrapTransform(p)
#' addTransform(ptrans, 'log_x4', 'x4', 'log10')
#' parameteriserAsDataFrame(ptrans)
#' parameteriserAsDataFrame(backtransform(p))
#' }
def wrap_transform(parameteriser):
    """Create a parameteriser for which parameter transformations can be defined.

    This allows to define e.g. a virtual parameter log_X instead of calibrating on the parameter X.

    Args:
        parameteriser (HypercubeParameteriser): A HypercubeParameteriser wrapper, or a type inheriting from it

    Returns:
        TransformParameteriser: A new parameteriser (TransformParameteriser) which has methods to define parameter transforms
    """
    return swg.CreateTransformParameterizer_py(parameteriser)


#'
#' @param parameteriser A SWIFT native parameteriser.
#' @return A SWIFT catchment parameteriser for a model structure
#' @export
#' @examples
#' \dontrun{
#' ref_area = 250
#' time_span = as.integer(lubridate::dhours(1))
#' p = gr4jScaledParameterizer(ref_area, time_span)
#' (pspec_gr4j = joki::getFreeParams('GR4J'))
#' pspec_gr4j$Min = c(1.0E+00, -2.70E+01, 1.0E+00, 1.0E+00)
#' pspec_gr4j$Max = c(5.0E+03,  2.70E+01, 6.6E+02, 2.4E+02)
#' setHyperCube(p, pspec_gr4j)
#' parameteriserAsDataFrame(p)
#' ptrans = wrapTransform(p)
#' addTransform(ptrans, 'log_x4', 'x4', 'log10')
#' parameteriserAsDataFrame(ptrans)
#' parameteriserAsDataFrame(backtransform(p))
#' }
def backtransform(parameteriser):
    """Get the parameteriser values in the untransformed space

    Get the parameteriser values in the untransformed space, i.e. remove any transform added via wrapTransform.
    This allows to transform back e.g. from a virtual parameter log_X to the underlying model (or even virtual/meta) parameter X.

    Args:
        parameteriser (HypercubeParameteriser): A HypercubeParameteriser wrapper, or a type inheriting from it

    Returns:
        [HypercubeParameteriser]: The parameters definitions without the transforms (if there are any)
    """
    return swg.UntransformHypercubeParameterizer_py(parameteriser)


#' Create a parameteriser for which parameter transformations can be defined
#'
#' This allows to define e.g. a virtual parameter log_X instead of calibrating on the parameter X.
#'
#' @param parameteriser A SWIFT native parameteriser.
#' @param param_name the name of the meta-parameter. Note that it can be the same value as inner_param_name, but this is NOT recommended.
#' @param inner_param_name the name of the parameter being transformed
#' @param transform_id identifier for a known bijective univariate function
#' @param a parameter in Y = F(ax+b). Default 1
#' @param b parameter in Y = F(ax+b). Default 0
#' @export
#' @examples
#' \dontrun{
#' ref_area = 250
#' time_span = as.integer(lubridate::dhours(1))
#' p = gr4jScaledParameterizer(ref_area, time_span)
#' pTran = wrapTransform(p)
#' parameteriserAsDataFrame(pTran)
#' addTransform(pTran, 'log_x4', 'x4', 'log10')
#' parameteriserAsDataFrame(pTran)
#' }
def add_transform(
    parameteriser: "TransformParameteriser",
    param_name: str,
    inner_param_name: str,
    transform_id: str,
    a=1.0,
    b=0.0,
):
    """Create a parameteriser for which parameter transformations can be defined

        This allows to define e.g. a virtual parameter log_X instead of calibrating on the parameter X.

    Args:
        parameteriser (TransformParameteriser): A TransformParameteriser wrapper, or a type inheriting from it
        param_name (str): the name of the meta-parameter. Note that it can be the same value as inner_param_name, but this is NOT recommended.
        inner_param_name (str): the name of the parameter being transformed
        transform_id (str): identifier for a known bijective univariate function
        a (float, optional): parameter in Y = F(ax+b). Defaults to 1.0.
        b (float, optional): parameter in Y = F(ax+b). Defaults to 0.0.
    """
    swg.AddParameterTransform_py(
        parameteriser, param_name, inner_param_name, transform_id, a, b
    )


#' Create a scaled parameteriser
#'
#' Create a scaled parameteriser. This allows to define tied parameters where pval = a * modelStateVal. Note that having a constant added is nascent 'under the hood' but not yet exposed.
#'
#' @param param_name
#' @param state_name
#' @param scalingVarName
#' @param minPval
#' @param maxPval
#' @param value
#' @param selectorType
#' @return A SWIFT catchment parameteriser for a model structure
#' @export
#' @examples
#' \dontrun{
#' # Define an initial soil moisture store 'S0', as a fraction of the model store capacity 'Smax'. The model state to initialise is 'S'
#' p = linearParameterizer(
#'           c('S0','R0'),
#'           c('S','R'),
#'           c('Smax','Rmax'),
#'           rep(0,2),
#'           rep(1.0,2),
#'           rep(0.5,2),
#'           'subareas')
#' }


def linear_parameteriser(
    param_name: VecStr,
    state_name: VecStr,
    scaling_var_name: VecStr,
    min_p_val: VecNum,
    max_p_val: VecNum,
    value: VecNum,
    selector_type: str = "subareas",
    intercept: VecNum = 0.0,
):
    """Create a scaled linear parameteriser, tying by a linear transformation a (resp several) model state to a (resp several) parameter values

    This allows to define tied parameters where pval = a * modelStateVal + intercept.
    The intent in particular is to define virtual model parameters such as initial store value as a fraction of the maximum storage capacity.

    Args:

        param_name (VecStr): the name of the meta-parameter. Note that it can be the same value as inner_param_name without interference, though this may be confusing a choice.
        state_name (VecStr): the name of the model state to modify, based on the value of the meta-parameter and the state found in 'scalingVarName'
        scaling_var_name (VecStr): the name of the parameter for each subarea model, to which to apply the area scaled value.
        min_p_val (VecNum): minimum value allowed for the meta-parameter
        max_p_val (VecNum): minimum value allowed for the meta-parameter
        value (VecNum): value for the meta parameter.
        selector_type (str, optional): an identifier to define to which catchment element(s) the parameteriser will be applied. Defaults to "subareas".
        intercept (VecNum, optional): intercepts in the linear relationship(s). Defaults to 0.0.

    Returns:
        [ScalingParameteriser]: new ScalingParameteriser
    """
    # stopifnot(len(selectorType) == 1)
    param_name, state_name, scaling_var_name, min_p_val, max_p_val, value = listify(
        param_name, state_name, scaling_var_name, min_p_val, max_p_val, value
    )
    lengths = [
        len(x)
        for x in [param_name, state_name, scaling_var_name, min_p_val, max_p_val, value]
    ]
    if len(set(lengths)) != 1:
        raise Exception(
            "arguments must all be vectors of same length: param_name, state_name, scalingVarName, minPval, maxPval, value"
        )
    if not is_common_iterable(intercept):
        intercept = np.repeat(intercept, lengths[0])
    elif len(intercept) != lengths[0]:
        raise Exception(
            'argument "intercept" be of length 1 or the same as: param_name, state_name, scalingVarName, minPval, maxPval, value'
        )
    p = swg.CreateTargetScalingParameterizer_py(selector_type)
    for i in range(lengths[0]):
        swg.AddLinearScalingParameterizer_py(
            p,
            param_name[i],
            state_name[i],
            scaling_var_name[i],
            intercept[i],
            min_p_val[i],
            max_p_val[i],
            value[i],
        )
    return p


PARAM_NAME_COL = "param_name"
STATE_NAME_COL = "state_name"
SCALING_VAR_NAME_COL = "scaling_var_name"
MIN_VALUE_COL = "min_value"
MAX_VALUE_COL = "max_value"
VALUE_COL = "value"
INTERCEPT_COL = "intercept"


def linear_parameteriser_from(
    data_frame: pd.DataFrame, selector_type: str = "subareas"
):
    """Create a scaled linear parameteriser, tying by a linear transformation a (resp several) model state to a (resp several) parameter values

    This allows to define tied parameters where pval = a * modelStateVal + intercept.
    The intent in particular is to define virtual model parameters such as initial store value as a fraction of the maximum storage capacity.
    Args:
        data_frame (pd.DataFrame): data frame with columns "param_name", "state_name", "scaling_var_name", "min_value", "max_value", "value", "intercept",
        selector_type (str, optional): [description]. Defaults to "subareas".

    Returns:
        [ScalingParameteriser]: ScalingParameteriser
    """
    return linear_parameteriser(
        param_name=data_frame[[PARAM_NAME_COL]],
        state_name=data_frame[[STATE_NAME_COL]],
        scaling_var_name=data_frame[[SCALING_VAR_NAME_COL]],
        min_p_val=data_frame[[MIN_VALUE_COL]],
        max_p_val=data_frame[[MAX_VALUE_COL]],
        value=data_frame[[VALUE_COL]],
        selector_type=selector_type,
        intercept=data_frame[[INTERCEPT_COL]],
    )


def _mk_list(x):
    from swift2.utils import is_common_iterable

    if not is_common_iterable(x):
        return [x]
    return x


def listify(*args):
    return (_mk_list(x) for x in args)


#' Create a parameteriser with Muskingum-type constraints
#'
#' Create a parameteriser with Muskingum-type constraints. Given an existing parameteriser, create a wrapper that adds constraints on two of its parameters.
#'
#' @param inner_parameters A SWIFT parameteriser object.
#' @param delta_t the simulation time step in HOURS.
#' @param param_name_k the variable identifier to use for the delay parameter of the Muskingum routing
#' @param param_name_x the variable identifier to use for the attenuation parameter of the Muskingum routing
#' @param simulation the model simulation from which link properties are inspected to define constraints. The links' parameters must already be set.
#' @return  an S4 object 'ExternalObjRef' [package "cinterop"] with external pointer type HYPERCUBE_PTR, or coercible to it
#' @export
#' @examples
#' \dontrun{
#' library(swift)
#' data_id = 'MMH'
#' simulation = createTestCatchment(nSubareas=4, data_id=data_id, varname_data_rain='rain', varname_data_pet='evap')
#' link_ids = paste0('link.',getLinkIds(simulation))
#' for(i in 1:len(link_ids)):
#'   linkId=link_ids[i]
#'   setStateValue(simulation, paste0(linkId, '.Slope'), 0.001*i)
#'   setStateValue(simulation, paste0(linkId, '.Length'), 1e4*i)
#'   setStateValue(simulation, paste0(linkId, '.f'), 1)
#'   setStateValue(simulation, paste0(linkId, '.ManningsN'), 1)
#' }
#'
#' simulation = swap_model(simulation, 'MuskingumNonLinear', 'channel_routing')
#'
#' paramN = data.frame(Name = "N", Value = 1.00, Min = 1.00, Max = 1.00, stringsAsFactors = False)
#' mkLinearMusk = createParameterizer(type='Generic links', specs=paramN)
#' rm(mkLinearMusk)
#' p_spec_nlm = data.frame(Name = c("X", "Alpha"),
#'                        Value = c(2.18420E-01, 2.73530E+00),
#'                        Min = c(1.00000E-03, 1.00000E-03),
#'                        Max = c(0.50000, 5.0000E+00),
#'                        stringsAsFactors = False)
#' muskParameterizer = createParameterizer(type='Generic links', specs=p_spec_nlm)
#' p_setAsDataFrame(muskParameterizer)
#' muskParameterizer = createMuskingumParamConstraints(muskParameterizer, delta_t=24, "Alpha", "X", simulation)
#' p_setAsDataFrame(muskParameterizer)
#' }
def create_muskingum_param_constraints(
    inner_parameters, delta_t=1, param_name_k="K", param_name_x="X", simulation=None
):
    """Create a parameteriser with Muskingum-type constraints. Given an existing parameteriser, create a wrapper that adds constraints on two of its parameters.

    Args:
        inner_parameters ([HypercubeParameteriser]): A SWIFT parameteriser object.
        delta_t (int, optional): the simulation time step in HOURS. Defaults to 1.
        param_name_k (str, optional): the variable identifier to use for the delay parameter of the Muskingum routing. Defaults to "K".
        param_name_x (str, optional): the variable identifier to use for the attenuation parameter of the Muskingum routing. Defaults to "X".
        simulation ([Simulation], optional): the model simulation from which link properties are inspected to define constraints. The links' parameters must already be set.. Defaults to None.

    Raises:
        ValueError: [description]

    Returns:
        [ConstraintParameteriser]: [description]
    """
    if simulation is None:
        raise ValueError("simulation argument must not be None")
    p = swg.CreateMuskingumConstraint_py(
        inner_parameters, delta_t, param_name_k, param_name_x, simulation
    )
    return p


#' @export
def feasible_muskingum_bounds(simulation: "Simulation", delta_t_hours=1):
    """[summary]

    Args:
        simulation (Simulation): [description]
        delta_t_hours (int, optional): [description]. Defaults to 1.

    Returns:
        [type]: [description]
    """
    return swg.GetFeasibleMuskingumBounds_py(simulation, delta_t_hours)


#' Concatenate SWIFT parameteriser
#'
#' Concatenate SWIFT parameteriser
#'
#' @param ... two or more SWIFT parameterisers
#' @return  an S4 object 'ExternalObjRef' [package "cinterop"] with external pointer type HYPERCUBE_PTR, or coercible to it
#' @examples
#' \dontrun{
#' ref_area = 250
#' time_span = as.integer(dhours(1))
#' p = gr4jScaledParameterizer(ref_area, time_span)
#' parameteriserAsDataFrame(p)
#'
#' p_states = linearParameterizer(
#'      c("S0","R0"),
#'      c("S","R"),
#'      c("x1","x3"),
#'      c(0.0,0.0),
#'      c(1.0,1.0),
#'      c(0.9,0.9),
#'      'each subarea')
#' init_parameteriser = makeStateInitParameterizer(p_states)
#' parameteriserAsDataFrame(init_parameteriser)
#'
#' p = concatenateParameterizers(p, init_parameteriser)
#' parameteriserAsDataFrame(p)
#' }
#' @export


def concatenate_parameterisers(
    *args: Sequence['HypercubeParameteriser'], strategy: str = ""
) -> "CompositeParameteriser":
    """Concatenate hypercubes to a single parameteriser

    Args:
        strategy (str, optional): The strategy to contatenate. Defaults to "", equivalent to "composite", the only available. May have other options in the future.

    Returns:
        CompositeParameteriser: A concatenated parameteriser
    """
    parameterisers = [x for x in args]
    return swc.aggregate_parameterisers_pkg(strategy, parameterisers)


#' Create a parameteriser used for model state initialisation
#'
#' This allows to define tied parameters where pval = a * modelStateVal. Note that having a constant added is nascent 'under the hood' but not yet exposed.
#'
#' @param parameteriser A SWIFT native parameteriser. Typically a linear scaling parameteriser to define initial some initial model states.
#' @return A SWIFT catchment parameteriser for a model structure
#' @export
#' @examples
#' \dontrun{
#' # Define an initial soil moisture store 'S0', as a fraction of the model store capacity 'Smax'. The model state to initialise is 'S'
#' p = linearParameterizer(
#'           c('S0','R0'),
#'           c('S','R'),
#'           c('Smax','Rmax'),
#'           rep(0,2),
#'           rep(1.0,2),
#'           rep(0.5,2),
#'           'subareas')
#' p = makeStateInitParameterizer(p)
#' }
def make_state_init_parameteriser(parameteriser):
    """[summary]

    Args:
        parameteriser (HypercubeParameteriser): A HypercubeParameteriser wrapper, or a type inheriting from it

    Returns:
        [StateInitParameteriser]: new state initialisation parameteriser
    """
    return swg.CreateStateInitParameterizer_py(parameteriser)


#' Create an termination criterion based on the rate of marginal fitness improvement
#'
#' Create an termination criterion based on the rate of marginal fitness improvement
#'
#' @param tolerance
#' @param cutoff_no_improvement
#' @param max_hours
#' @return a termination criterion to use with an optimiser
#' @export
def get_marginal_termination(tolerance=1e-06, cutoff_no_improvement=10, max_hours=0.05):
    """Create an termination criterion based on the rate of marginal fitness improvement

    Args:
        tolerance ([type], optional): the increment in the objective below which the improvement is considered negligible. Defaults to 1e-06.
        cutoff_no_improvement (int, optional): the maximum number of successive times the algorithm fails to improve the objective function.. Defaults to 10.
        max_hours (float, optional): the maximum wall time runtime for the optimisation. Defaults to 0.05.

    Returns:
        [SceTerminationCondition]: [description]
    """
    return swg.CreateSceMarginalTerminationWila_py(
        tolerance=tolerance,
        cutoffNoImprovement=cutoff_no_improvement,
        maxHours=max_hours,
    )


#' Create an termination criterion based on the wall clock runtime
#'
#' Create an termination criterion based on the wall clock runtime
#'
#' @param max_hours	the maximum wall time runtime for the optimisation
#' @return a termination criterion to use with an optimiser
#' @export
def get_max_runtime_termination(max_hours=0.05):
    """Create an termination criterion based on the wall clock runtime

    Args:
        max_hours (float, optional): the maximum wall time runtime in hours for the optimisation. Defaults to 0.05.

    Returns:
        [SceTerminationCondition]: [description]
    """
    return swg.CreateSceMaxRuntimeTerminationWila_py(maxHours=max_hours)


#' Create an termination criterion based on the number of objective evaluations
#'
#' Create an termination criterion based on the number of objective evaluations
#'
#' @param max_iterations	number of iterations, which, if less than total count of optim objective evaluations, defines optim termination.
#' @return a termination criterion to use with an optimiser
#' @export
def get_max_iteration_termination(max_iterations=1000):
    """Create an termination criterion based on the number of objective evaluations

    Args:
        max_iterations (int, optional): number of iterations, which, if less than total count of optim objective evaluations, defines optim termination.. Defaults to 1000.

    Returns:
        [SceTerminationCondition]: [description]
    """
    return swg.CreateSceMaxIterationTerminationWila_py(maxIterations=max_iterations)


#' Build an SCE optimiser for a SWIFT model
#'
#' Build an SCE optimiser for a SWIFT model
#'
#' @param objective an objective calculator
#' @param terminationCriterion An object that can be passed to SCE for testing the completion of the algorithm.
#' @param SCEPars optional; parameters controlling the behavior of the SCE optimisers.
#' @param populationInitializer an S4 object 'ExternalObjRef' [package "cinterop"] with external pointer type HYPERCUBE_PTR or coercible to it, or a type of object that can seed a sampler i.e. coercible to a type CANDIDATE_FACTORY_SEED_WILA_PTR. If the argument is a hypercube, a uniform random sampler is created.
#' @return a Shuffled Complex Evolution optimiser
#' @export
def create_sce_optim_swift(
    objective, termination_criterion, sce_params, population_initialiser
):
    """Build an SCE optimiser for a SWIFT model

    Args:
        objective ('ObjectiveEvaluator'):  an objective calculator
        termination_criterion ('SceTerminationCondition'):  An object that can be passed to SCE for testing the completion of the algorithm.
        sce_params (dict):  optional; parameters controlling the behavior of the SCE optimisers.
        population_initialiser ('CandidateFactorySeed'):  an S4 object 'ExternalObjRef' [package "cinterop"] with external pointer type HYPERCUBE_PTR or coercible to it, or a type of object that can seed a sampler i.e. coercible to a type CANDIDATE_FACTORY_SEED_WILA_PTR. If the argument is a hypercube, a uniform random sampler is created.

    Returns:
        [Optimiser]: [description]
    """

    if is_sampler_seeding(population_initialiser):
        # nothing to do.
        pass
    elif is_hypercube(population_initialiser):
        population_initialiser = create_parameter_sampler(
            0, population_initialiser, "urs"
        )
    else:
        raise ValueError(
            "population_initialiser must be provided (can be a sampler or a hypercube)"
        )
    # if(missing(terminationCriterion)) terminationCriterion = maxWallTimeTermination()
    # if(missing(SCEpars)) SCEpars = getDefaultSceParameters()
    if termination_criterion is None:
        max_hours = str(10 / 3600)
        termination_criterion = create_sce_termination_wila(
            "relative standard deviation", ["0.002", max_hours]
        )
    if sce_params is None:
        sce_params = get_default_sce_parameters()
    return swg.CreateShuffledComplexEvolutionWila_py(
        objective, termination_criterion, sce_params, population_initialiser
    )


def create_sce_termination_wila(
    type: str, arguments: Sequence[str]
) -> "SceTerminationCondition":
    """Create a type of termination criteria suitable for the SCE algorithm.

    Args:
        type (str): A type of termination criterion; currently at least "relative standard deviation" and "maximum evaluations" are valid options
        arguments (Sequence[str]): Arguments, in string forms even for numeric values, options for the selected type.

    Returns:
        SceTerminationCondition: [description]
    """
    return swg.CreateSceTerminationWila_py(type, arguments, len(arguments))


def is_sampler_seeding(obj: CffiNativeHandle):
    """Is the argument a native object that is a seeded candidate parameteriser factory

    Args:
        obj (CffiNativeHandle): [description]

    Returns:
        [type]: [description]
    """
    # KLUDGE:
    from refcount.interop import is_cffi_native_handle

    return is_cffi_native_handle(obj, "CANDIDATE_FACTORY_SEED_WILA_PTR")


#' @export
def is_hypercube(p_set: CffiNativeHandle):
    """Is the object a native parameteriser that can be cast as a hypercube?

    Args:
        p_set (CffiNativeHandle): [description]

    Returns:
        [type]: [description]
    """
    # TODO: implement a SWIFT API function to check this.
    # KLUDGE:
    from refcount.interop import is_cffi_native_handle

    return is_cffi_native_handle(p_set) and p_set.type_id in [
        "HYPERCUBE_PTR",
        "COMPOSITE_PARAMETERIZER_PTR",
        "FUNCTIONS_PARAMETERIZER_PTR",
        "CONSTRAINT_PARAMETERIZER_PTR",
        "SCALING_PARAMETERIZER_PTR",
        "STATE_INIT_PARAMETERIZER_PTR",
        "TRANSFORM_PARAMETERIZER_PTR",
        "STATE_INITIALIZER_PTR",
        "SUBAREAS_SCALING_PARAMETERIZER_PTR",
        "HYPERCUBE_WILA_PTR",
        "XPtr<OpaquePointer>",  # TODO this is to circumvent issues now that some functions are generated from Rcpp code rather than API. See e.g. aggregate_parameterisers_pkg
    ]


#' @export
def is_score(x):
    """OBJECTIVE_SCORES_WILA_PTR

    Args:
        x ([type]): [description]

    Returns:
        [type]: [description]
    """
    # TODO: implement a SWIFT API function to check this.
    # KLUDGE?:
    return is_cffi_native_handle(x, type_id="OBJECTIVE_SCORES_WILA_PTR")


#' @export
def is_set_of_scores(x):
    """VEC_OBJECTIVE_SCORES_PTR

    Args:
        x ([type]): [description]

    Returns:
        [type]: [description]
    """
    return is_cffi_native_handle(x, type_id="VEC_OBJECTIVE_SCORES_PTR")


#' @export
def get_default_sce_parameters():
    """[summary]

    Returns:
        [type]: [description]
    """
    from swift2.wrap.swift_wrap_custom import default_sce_parameters_pkg

    return default_sce_parameters_pkg()


#' Create a parameter sampler for use in initialization of populations of parameterisers
#'
#' Create a parameter sampler for use in initialization of populations of parameterisers
#'
#' @param seed integer, the seed to use for the sampler
#' @param parameteriser an S4 object 'ExternalObjRef' [package "cinterop"] with external pointer type HYPERCUBE_PTR, or coercible to it
#' @param type a character, identifying a method such as 'urs' for uniform random sampling.
#' @return a population sampler, an S4 object 'ExternalObjRef'
#' @export
def create_parameter_sampler(seed, parameteriser, type: str):
    """

    Args:
        seed ([type]): seed integer, the seed to use for the sampler
        parameteriser (HypercubeParameteriser): A HypercubeParameteriser wrapper, or a type inheriting from it
        type (str): identifying a method such as 'urs' for uniform random sampling.

    Returns:
        [type]: [description]
    """
    return swg.CreateCandidateFactorySeedWila_py(parameteriser, type, seed)


#' Convert an external object hypercube parameteriser to an R data frame
#'
#' Convert an external object hypercube parameteriser to an R data frame
#'
#' @param parameteriser an S4 object 'ExternalObjRef' [package "cinterop"] with external pointer type HYPERCUBE_PTR, or coercible to it
#' @return a data frame
#' @export
def parameteriser_as_dataframe(parameteriser):
    """Convert an external object hypercube parameteriser to a pandas data frame

    Args:
        parameteriser (HypercubeParameteriser): A HypercubeParameteriser wrapper, or a type inheriting from it

    Returns:
        [type]: [a data frame]
    """
    return swc.parameteriser_to_data_frame_pkg(parameteriser)


def num_free_parameters(parameteriser) -> int:
    p = parameteriser.as_dataframe()
    return np.sum(p.Max - p.Min > 0)


#' Launch an optimization task
#'
#' Launch an optimization task, as defined by the object passed as an argument
#'
#' @param optimiser the instance of the optimiser that has been created for the optimisation task about to be launched.
#' @return a reference to an object that holds the results of the calibration.
#' @export
def execute_optimisation(optimiser):
    """Launch an optimization task, as defined by the object passed as an argument

    Args:
        optimiser (Optimiser): the instance of the optimiser that has been created for the optimisation task about to be launched.

    Returns:
        [VectorObjectiveScores]: [description]
    """
    return swg.ExecuteOptimizerWila_py(optimiser)


def scores_as_dataframe(scores_population):
    """Convert objective scores to a pandas data frame representation

    Args:
        scores_population ([type]): [description]

    Returns:
        [type]: [description]
    """
    return swc.vec_scores_as_dataframe_pkg(scores_population)


#' Sort objective scores according to one of the objective values
#'
#'
#'
#' @param scores_population
#' @param score_name
#' @return an S4 object 'ExternalObjRef' [package "cinterop"] with external pointer type VEC_OBJECTIVE_SCORES_PTR
#' @export
def sort_by_score(scores_population, score_name="NSE"):
    """Sort objective scores according to one of the objective values

    Args:
        scores_population ([type]): an S4 object 'ExternalObjRef' [package "cinterop"] with external pointer type VEC_OBJECTIVE_SCORES_PTR
        score_name (str, optional): name of the objective to use for sorting. Defaults to "NSE".

    Returns:
        VectorObjectiveScores: an S4 object 'ExternalObjRef' [package "cinterop"] with external pointer type VEC_OBJECTIVE_SCORES_PTR
    """
    return swg.SortSetOfScoresBy_py(scores_population, score_name)


#' Get an objective scores in a vector thereof
#'
#' Get an objective scores in a vector thereof
#'
#' @param scores_population
#' @param index
#' @return an S4 object 'ExternalObjRef' [package "cinterop"] with external pointer type OBJECTIVE_SCORES_WILA_PTR
#' @export
def get_score_at_index(scores_population, index: int):
    """Get an objective scores in a vector thereof

    Args:
        scores_population ([type]): an S4 object 'ExternalObjRef' [package "cinterop"] with external pointer type VEC_OBJECTIVE_SCORES_PTR
        index (int): one-based index in the population

    Returns:
        [ObjectiveScores]: [description]
    """
    return swg.GetScoresAtIndex_py(scores_population, index - 1)


#' Gets the best score in a population for a given objective
#'
#' Gets the best score in a population for a given objective
#'
#' @param scores_population an S4 object 'ExternalObjRef' [package "cinterop"] with external pointer type VEC_OBJECTIVE_SCORES_PTR
#' @param score_name name of the objective to use for sorting.
#' @param convert_to_py should the returned score be converted to an R representation. Default False.
#' @return an S4 object 'ExternalObjRef' [package "cinterop"] with external pointer type OBJECTIVE_SCORES_WILA_PTR
#' @export
def get_best_score(scores_population, score_name="NSE", convert_to_py=False):
    """Gets the best score in a population for a given objective

    Args:
        scores_population ([type]): an S4 object 'ExternalObjRef' [package "cinterop"] with external pointer type VEC_OBJECTIVE_SCORES_PTR
        score_name (str, optional): name of the objective to use for sorting. Defaults to "NSE".
        convert_to_py (bool, optional): should the returned score be converted to an R representation. Default False. Defaults to False.

    Returns:
        [ObjectiveScores or Dict]: [description]
    """
    sorted_results = sort_by_score(scores_population, score_name)
    s = get_score_at_index(sorted_results, 1)
    if convert_to_py:
        return swc.scores_as_rpy_dict_pkg(s)
    else:
        return s


def as_py_structure(x: Any):
    """Try to convert an external pointer to a native python representation

    Args:
        x (Any): object, presumably wrapper around an Xptr, to convert to a 'pure' python representation

    Returns:
        [type]: [description]
    """
    if not is_cffi_native_handle(x):
        return x
    if is_score(x):
        return swc.scores_as_rpy_dict_pkg(x)
    elif is_set_of_scores(x):
        return scores_as_dataframe(x)
    else:
        return x


#' Gets the parameteriser for a score
#'
#' Gets the parameteriser for a score
#'
#' @param score an S4 object 'ExternalObjRef' [package "cinterop"] with external pointer type OBJECTIVE_SCORES_WILA_PTR
#' @return an S4 object 'ExternalObjRef' [package "cinterop"] with external pointer type HYPERCUBE_PTR or related
def parameteriser_for_score(score:'ObjectiveScores'):
    """Gets the parameteriser for a score

    Args:
        score ([type]): [description]

    Returns:
        [HypercubeParameteriser]: [description]
    """
    return swg.GetSystemConfigurationWila_py(score)


#' Computes the value of an objective for a given set of parameters
#'
#'
#'
#' @param objective an objective calculator
#' @param parameteriser an S4 object 'ExternalObjRef' [package "cinterop"] with external pointer type HYPERCUBE_PTR, or coercible to it.
#' @export
def evaluate_score_for_parameters(objective, parameteriser):
    """Computes the value of an objective for a given set of parameters

    Args:
        objective ([type]): an objective calculator
        parameteriser (HypercubeParameteriser): A HypercubeParameteriser wrapper, or a type inheriting from it

    Returns:
        [type]: [description]
    """
    return swc.evaluate_score_wila_pkg(objective, parameteriser)


#' Apply a model configuration to a simulation
#'
#' Apply a model configuration to a simulation
#'
#' @param simulation an S4 object 'ExternalObjRef' [package "cinterop"] with external pointer type MODEL_SIMULATION_PTR
#' @param parameteriser an S4 object 'ExternalObjRef' [package "cinterop"] with external pointer type HYPERCUBE_PTR, or coercible to it
#' @export
def apply_sys_config(parameteriser, simulation):
    """Apply a model configuration to a simulation

    Args:
        parameteriser (HypercubeParameteriser): A HypercubeParameteriser wrapper, or a type inheriting from it
        simulation (Simulation): simulation
    """
    if is_score(parameteriser):
        parameteriser = swg.GetSystemConfigurationWila_py(parameteriser)
    assert is_hypercube(parameteriser)
    swg.ApplyConfiguration_py(parameteriser, simulation)


#' Sets logging on an optimiser
#'
#' Sets logging on an optimiser, so as to record a detail of the optimisation process for post-optimisation analysis.
#'
#' @param optimiser the instance of the optimiser that has been created for the optimisation task about to be launched.
#' @param type currently ignored, placeholder for future options. The type of logger to use.
#' @return a reference to the logger that has been created and attached to the optimiser
#' @export
def set_calibration_logger(optimiser, type=""):
    """Sets logging on an optimiser, so as to record a detail of the optimisation process for post-optimisation analysis.

    Args:
        optimiser ([type]): [description]
        type (str, optional): [description]. Defaults to "".

    Returns:
        [type]: [description]
    """
    return swg.SetOptimizerLoggerWila_py(optimiser, type)


from swift2.wrap.swift_wrap_custom import convert_optimisation_logger


#' Gets logger content
#'
#' Gets logger content on an optimiser, recorded detail of the optimisation process for post-optimisation analysis.
#'
#' @param optimiser the instance of the optimiser that has been created for the optimisation task about to be launched.
#' @export
def get_logger_content(optimiser:DeletableCffiNativeHandle, add_numbering:bool=False) -> pd.DataFrame:
    """Gets logger content on an optimiser, recorded detail of the optimisation process for post-optimisation analysis.

    Args:
        optimiser ([type]): the instance of the optimiser that has been created for the optimisation task about to be launched.
        add_numbering (bool, optional): Add an explicit column for numbering the lines of the log. Defaults to False.

    Returns:
        pd.DataFrame: The data log of the optimiser
    """
    # coercion to data.frame is a workaround for https://jira.csiro.au/browse/WIRADA-245
    if is_cffi_native_handle(optimiser, type_id="ERRIS_STAGED_CALIBRATION_PTR"):
        log_data = swg.GetERRISCalibrationLog_py(optimiser)
    else:
        log_data = swg.GetOptimizerLogDataWila_py(optimiser)
    return convert_optimisation_logger(log_data, add_numbering)


#' Get examples of typical parameterisers
#'
#' Get examples of typical parameterisers
#'
#' @param type character, identifier for a type of parameteriser including 'log-likelihood'
#' @param strict logical, default False. If True an error is raised if the type is not found, otherwise a dummy empty parameteriser is returned.
#' @export
def example_parameteriser(type: str, strict=False):
    """Get examples of typical parameterisers

    Args:
        type (str): identifier for a type of parameteriser including 'log-likelihood'
        strict (bool, optional): If True an error is raised if the type is not found, otherwise a dummy empty parameteriser is returned.. Defaults to False.

    Returns:
        [HypercubeParameteriser]: [description]
    """
    type = type.lower()
    if type == "log-likelihood":
        p = create_parameteriser(type="no apply")
        calc_m_and_s = 1.0  # meaning true
        censopt = 0.0
        add_to_hypercube(
            p,
            _df_from_dict(
                Name=["b", "m", "s", "a", "maxobs", "ct", "censopt", "calc_mod_m_s"],
                Min=_npf([-30, 0, 1, -30, 100.0, 0.01, censopt, calc_m_and_s]),
                Max=_npf([0, 0, 1000, 1, 100.0, 0.01, censopt, calc_m_and_s]),
                Value=_npf([-7, 0, 100, -10, 100.0, 0.01, censopt, calc_m_and_s]),
            ),
        )
        return p
    if not strict:
        return create_parameteriser(type="Generic")
    else:
        raise Exception("No example parameteriser yet for type " + type)


#' Builds a parameteriser usable with a multisite multiobjective calculator.
#'
#' Builds a parameteriser usable with a multisite multiobjective calculator.
#'
#' @param func_parameterisers list of external pointers, parameterisers for each function of a multiobjective calculation.
#' @param func_identifiers character, identifiers for each of the objectives defined in an multisite objective definition.
#' @param prefixes character, default None. Optional prefixes to use to disambiguate short parameter names used in each function of a multiobjective calculator.
#' @param mix_func_parameteriser parameteriser, default None. (FUTURE) Optional parameteriser used in mixing the multiple objectives.
#' @param hydro_parameteriser parameteriser, default None. Optional parameteriser applied to the simulation model.
#' @examples
#' \dontrun{
#' ms = createTestCatchment()
#' nodeids = c('node.n2', 'node.n4')
#'
#' p = exampleParameterizer('log-likelihood')
#' (parameteriserAsDataFrame(p))
#'
#' func_parameterisers = list(p, clone(p))
#' catchment_pzer = gr4jScaledParameterizer()
#' fp = createMultisiteObjParameterizer(func_parameterisers, nodeids, prefixes=paste0(nodeids, '.'), mix_func_parameteriser=NULL, hydro_parameteriser=catchment_pzer)
#' (parameteriserAsDataFrame(fp))
#'
#' #
#' mvids = mk_full_data_id(nodeids, 'OutflowRate')
#' record_state(ms, mvids)
#' execSimulation(ms)
#' # create synthetic flows
#' modFlows = getRecorded(ms)
#' (span = get_simulation_span_pkg(ms))
#' w = c(1.0, 2.0)
#' names(w) = mvids
#'
#' statspec = multi_statistic_definition(mvids, rep('log-likelihood', 2), nodeids, mvids, rep(span$Start, 2), rep(span$End, 2) )
#' # Create synthetic observations
#' observations = list(
#'   modFlows[,mvids[1]] * 0.33,
#'   modFlows[,mvids[2]] * 0.77
#' )
#'
#' obj = createMultisiteObjective(ms, statspec, observations, w)
#' dummy = createParameterizer()
#' # the following will fail but this is expected and desirable - missing mandatory log-likelihood parameters
#' EvaluateScoresForParametersWila_Pkg(obj, dummy)
#'
#' EvaluateScoresForParametersWila_Pkg(obj, fp)
#' getScore(obj, fp)
#'
#' ffp = filteredParameters(fp)
#' parameteriserAsDataFrame(ffp)
#' hideParameters(ffp, nodeids, starts_with=True)
#' parameteriserAsDataFrame(ffp)
#' # hidden parameters are still retrievable by the objective functions
#' EvaluateScoresForParametersWila_Pkg(obj, fp)
#' }
#' @export
def create_multisite_obj_parameteriser(
    func_parameterisers,
    func_identifiers,
    prefixes=None,
    mix_func_parameteriser=None,
    hydro_parameteriser=None,
):
    """Builds a parameteriser usable with a multisite multiobjective calculator.

    This is an advanced topic; users may refer to [this sample workflow](https://csiro-hydroinformatics.github.io/swift-py-doc/notebooks/calibrate_multisite/)

    Args:
        func_parameterisers ([type]): list of external pointers, parameterisers for each function of a multiobjective calculation.
        func_identifiers ([type]): character, identifiers for each of the objectives defined in an multisite objective definition.
        prefixes ([type], optional): Optional prefixes to use to disambiguate short parameter names used in each function of a multiobjective calculator.. Defaults to None.
        mix_func_parameteriser ([type], optional): parameteriser, default None. (FUTURE) Optional parameteriser used in mixing the multiple objectives.. Defaults to None.
        hydro_parameteriser ([type], optional): parameteriser, default None. Optional parameteriser applied to the simulation model.. Defaults to None.

    Returns:
        [FunctionsParameteriser]: [description]
    """
    # stopifnot(is.list(func_parameterisers))
    # stopifnot(len(func_parameterisers) == len(func_identifiers))
    if not prefixes is None:
        assert len(func_parameterisers) == len(prefixes)
    cp = swg.CreateCompositeParameterizer_py()
    n = len(func_parameterisers)
    for i in range(n):
        swg.TagParameterizer_py(func_parameterisers[i], func_identifiers[i])
        if not prefixes is None:
            pp = swg.CreatePrefixingParameterizer_py(
                func_parameterisers[i], prefixes[i]
            )
            swg.AddToCompositeParameterizer_py(cp, pp)
        # else:
        #     TODO: what? forgot and the R implementation had a minor bug I think
        #     swg.AddToCompositeParameterizer_py(cp, pp)
    if not mix_func_parameteriser is None:
        swg.TagParameterizer_py(mix_func_parameteriser, "mixing_function")
        pmix_func_parameteriser = swg.CreatePrefixingParameterizer_py(
            mix_func_parameteriser, "mixing_function."
        )
        swg.AddToCompositeParameterizer_py(cp, pmix_func_parameteriser)
    if hydro_parameteriser is None:  # create a dummy
        hydro_parameteriser = swg.CreateHypercubeParameterizer_py("no apply")
    fp = swg.CreateFunctionsParameterizer_py(hydro_parameteriser, cp)
    return fp


#' Wrap a parameteriser in a filter that can hide some parameters
#'
#' Wrap a parameteriser in a filter that can hide some parameters
#'
#' @param parameteriser A SWIFT native parameteriser.
#' @return A new SWIFT native parameteriser. A deep copy of the input is taken.
#' @seealso \code{\link{createMultisiteObjParameterizer}} for sample code
#' @export
def filtered_parameters(parameteriser):
    """Wrap a parameteriser in a filter that can hide some parameters

    Args:
        parameteriser (HypercubeParameteriser): A HypercubeParameteriser wrapper, or a type inheriting from it. A deep copy of the input is taken.

    Returns:
        [FilteringParameteriser]: [description]
    """
    return swg.CreateFilteringParameterizer_py(parameteriser)


#' Hide some parameters in a filter parameteriser
#'
#' Hide some parameters (from the outside e.g. optimisers) in a filter parameteriser
#'
#' @param parameteriser A SWIFT native parameteriser.
#' @param patterns character, one or more pattern to match and hide matching parameters. Match according to other parameters.
#' @param regex logical, defaults False, should the patterns be used as regular expressions.
#' @param starts_with logical, defaults False. Ignored if regex is True. Should the patterns be used as starting strings in the parameter names.
#' @param strict logical, default False. Used only if regex and starts_with are False. If True, raises an error if one of the "patterns" has no exact match in the parameters.
#' @seealso \code{\link{createMultisiteObjParameterizer}} for sample code
#' @export
def hide_parameters(
    parameteriser, patterns, regex=False, starts_with=False, strict=False
):
    """Hide some parameters (from the outside e.g. optimisers) in a filter parameteriser

    Args:
        parameteriser (HypercubeParameteriser): A HypercubeParameteriser wrapper, or a type inheriting from it
        patterns ([type]):  character, one or more pattern to match and hide matching parameters. Match according to other parameters.
        regex (bool, optional): logical, defaults False, should the patterns be used as regular expressions.. Defaults to False.
        starts_with (bool, optional): logical, defaults False. Ignored if regex is True. Should the patterns be used as starting strings in the parameter names.. Defaults to False.
        strict (bool, optional): logical, default False. Used only if regex and starts_with are False. If True, raises an error if one of the "patterns" has no exact match in the parameters.. Defaults to False.
    """
    swg.HideParameters_py(parameteriser, patterns, regex, starts_with, strict)


#' Show some parameters in a filter parameteriser
#'
#' Show some parameters (from the outside e.g. optimisers) in a filter parameteriser
#'
#' @param parameteriser A SWIFT native parameteriser.
#' @param patterns character, one or more pattern to match and show matching parameters. Match according to other parameters.
#' @param regex logical, defaults False, should the patterns be used as regular expressions.
#' @param starts_with logical, defaults False, should the patterns be used as starting strings in the parameter names.
#' @seealso \code{\link{createMultisiteObjParameterizer}} for sample code
#' @export
def show_parameters(parameteriser, patterns, regex=False, starts_with=False):
    """Show some parameters (from the outside e.g. optimisers) in a filter parameteriser

    Args:
        parameteriser (HypercubeParameteriser): A HypercubeParameteriser wrapper, or a type inheriting from it
        patterns ([type]):  character, one or more pattern to match and show matching parameters. Match according to other parameters
        regex (bool, optional): should the patterns be used as regular expressions. Defaults to False.
        starts_with (bool, optional): should the patterns be used as starting strings in the parameter names. Defaults to False.
    """
    swg.ShowParameters_py(parameteriser, patterns, regex, starts_with)


#' min/max bound a column in a data frame
#'
#' min/max bound a column in a data frame
#'
#' @param x
#' @param colname
#' @param lim
#' @return a data frame
#' @export
def bound_values_df(x, colname, lim=None):
    """min/max bound a column in a data frame

    Args:
        x ([type]):   a data frame
        colname ([type]): a character vector, name of the column to bound
        lim ([type], optional): a num vector of the min/max limits to apply, for instance c(0, 1). Defaults to None.

    Returns:
        [type]: [description]
    """
    if lim is None:
        return x
    return x.assign(**{colname: bound_values(x[[colname]], lim)})


import numpy as np


def bound_values(x, lim: List = None):
    if lim is None:
        return x
    if isinstance(x, pd.Series):
        x = x.values
    return np.maximum(np.minimum(x, lim[1]), lim[0])


class MhData:
    """Data log from metaheuristic calibration processes"""

    def __init__(
        self,
        data: pd.DataFrame,
        fitness: str = "NSE",
        messages: str = "Message",
        categories: str = "Category",
    ) -> None:
        self._fitness = fitness
        self._messages: str = messages
        self._categories: str = categories
        self._data: pd.DataFrame = data

    @property
    def data(self) -> pd.DataFrame:
        """The inner data of this data log"""
        return self._data

    def rename_columns(self, colnames_map: Dict[str, str]) -> None:
        """Rename the columns of the data log according to a mapping. 

        This is handy for instance to change fully qualified parameter names 
        such as 'subarea.Wolf_Creek.x1' to just 'x1' to produce more legible plots.

        Args:
            colnames_map (Dict[str, str]): mapping
        """        
        d = self._data.rename(colnames_map, axis=1, inplace=False)
        self._data = d

    def subset_by_pattern(self, colname: str, pattern: str) -> "MhData":
        """Subset the log by filtering an attribute by a regexp pattern

        Args:
            colname (str): column name to filter on
            pattern (str): regexp pattern, filter definition

        Returns:
            Any: New MhData object with subset data
        """
        criterion: pd.DataFrame = self._data[[colname]]
        indices = criterion.squeeze().str.match(pattern)
        data = self._data.loc[indices.values]
        return MhData(data, self._fitness, self._messages, self._categories)

    def bound_fitness(self, obj_lims: Sequence[float] = None) -> pd.DataFrame:
        """Return a copy of the log data with the fitness measure bound by min/max limits

        Args:
            obj_lims (Sequence[float], optional): min/max limits, length 2. Defaults to None.

        Returns:
            pd.DataFrame: log data with bound fitness
        """
        if obj_lims is None:
            return self._data
        d = self._data.copy()
        d = bound_values_df(d, self._fitness, obj_lims)
        return d

    def subset_by_message(
        self, pattern: str = "Initial.*|Reflec.*|Contrac.*|Add.*"
    ) -> "MhData":
        """Subset the log by filtering the 'Message' column by a regexp pattern

        Args:
            pattern (str): regexp pattern, filter definition

        Returns:
            Any: New MhData object with subset data
        """
        return self.subset_by_pattern(self._messages, pattern)

    def facet_plot(
        self,
        y: str,
        facet_category: str = "Message",
        col_wrap: int = 3,
        x: str = "PointNumber",
        fig_width_in=15,
        fig_heigth_in=10,
    ):
        """Facet plot of parameter value evolution, facetted by a category.

        This method requires the package `seaborn` to be installed.

        Args:
            y (str): variable name (model parameter) to use for the y-axis, e.g. "x4" for GR4J
            facet_category (str, optional): Data attribute to use to facet. Defaults to "Message".
            col_wrap (int, optional): Max number of columns in the plot. Defaults to 3.
            x (str, optional): variable name (calibration iteration, or model parameter) to use for the x-axis. Defaults to "PointNumber".
            fig_width_in (int, optional): figure width in inches. Defaults to 15.
            fig_heigth_in (int, optional): figure height in inches. Defaults to 10.

        Returns:
            FacetGrid: The plot to display
        """
        import seaborn as sns
        df = self.data
        grid = sns.FacetGrid(df, col = facet_category, col_wrap=col_wrap)
        grid.map(sns.scatterplot, x, y)
        grid.figure.set_size_inches(fig_width_in, fig_heigth_in)
        grid.add_legend()
        return grid


def mk_optim_log(
    log_dataframe: pd.DataFrame,
    fitness="NSE",
    messages="Message",
    categories="Category",
):
    df_names = log_dataframe.columns

    def check_valid_name(x, name):
        if not fitness in df_names:
            raise ValueError(
                'specified string "'
                + x
                + '" for "'
                + name
                + '" not found in data frame names: '
                + ", ".join(df_names)
            )

    check_valid_name(fitness, "fitness")
    check_valid_name(messages, "messages")
    check_valid_name(categories, "categories")
    return MhData(
        data=log_dataframe, fitness=fitness, messages=messages, categories=categories
    )


def extract_optimisation_log(estimator, fitness_name="log.likelihood") -> 'MhData':
    """Extract the logger from a parameter extimator (optimiser or related)

    Args:
        estimator (Optimiser): the optimiser instance
        fitness_name (str, optional): name of the fitness function to extract. Defaults to "log.likelihood".

    Returns:
        MhData: an object with methods to analyse the optimisation log
    """
    optim_log = get_logger_content(estimator, add_numbering=True)
    log_mh = mk_optim_log(
        optim_log, fitness=fitness_name, messages="Message", categories="Category"
    )
    # geom_ops = log_mh.subset_by_message()
    # return {"data": log_mh, "geom_ops": geom_ops}
    return log_mh


_default_params = {
    "GR5H": [
        ["x1", "x2", "x3", "x4", "x5"],
        [44.6, 30.0, 10.0, 14.0, 200.0],
        [1, 1, 0, 1, 1],
        [1000, 400, 1000, 240, 1000],
    ],
    "GR6J":
    # per202 2014-09-25
    # I take some values for the parameters from the unit tests, but the min/max bounds are PURE guesses. Q/A TBC.
    [
        ["x1", "x2", "x3", "x4", "x5", "x6"],
        [20, -2, 10, 2, 0, 1],
        [1, -5, 0, 1, 0, 0],
        [1000, 400, 1000, 240, 1, 1],
    ],
    "PDM":
    # per202 2014-11-13
    #
    [
        ["cmax", "cminrat", "b", "be", "kg", "bg", "Strat", "k1", "k2rat", "kb"],
        [400, 0.5, 1.8, 1.0, 1300.0, 1.0, 0.5, 35.0, 0.3, 2.4],
        [1, 0, 0.001, 1.0, 1.0, 1.0, 0.0, 1.0, 0.0001, 1.0],
        [3000, 1, 2.0, 2.0, 50000.0, 1.0, 1.0, 300.0, 1.0000, 2000.0],
    ],
    "SAC":
    # rob635 2015-01-11
    #
    [
        [
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
        ],
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
        ],
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
        ],
    ],
    "SACSMA_NSW":
    # rob635 2023-01-04
    # default parameters taken from ewater Source user guide
    [
        [
            "uztwm",
            "uzfwm",
            "lztwm",
            "lzfsm",
            "lzfpm",
            "uzk",
            "lzsk",
            "lzpk",
            "zperc",
            "rexp",
            "pctim",
            "sarva",
            "side",
            "ssout",
            "adimp",
            "pfree",
            "rserv",
            "ord_1",
            "ord_2",
            "ord_3",
            "ord_4",
            "ord_5",
            "ord_6",
            "ord_7",
            "ord_8",
            "ord_9",
            "ord_10",
            "ord_11",
            "ord_12",
            "ord_13",
            "ord_14",
            "ord_15",
            "ord_16",
            "ord_17",
            "ord_18",
            "ord_19",
            "ord_20",
        ],
        [
            50,
            40,
            130,
            25,
            60,
            0.3,
            0.05,
            0.01,
            40,
            1,
            0.01,
            0,
            0,
            0,
            0,
            0.06,
            0.3,
            1,
            0,
            0,
            0,
            0,
            0,
            0,
            0,
            0,
            0,
            0,
            0,
            0,
            0,
            0,
            0,
            0,
            0,
            0,
            0,
        ],
        [
            25,
            10,
            75,
            15,
            40,
            0.2,
            0.03,
            0.001,
            0,
            0,
            0,
            0,
            0,
            0,
            0,
            0,
            0,
            0,
            0,
            0,
            0,
            0,
            0,
            0,
            0,
            0,
            0,
            0,
            0,
            0,
            0,
            0,
            0,
            0,
            0,
            0,
            0,
        ],
        [
            125,
            75,
            300,
            300,
            600,
            0.5,
            0.2,
            0.015,
            80,
            3,
            0.05,
            0.1,
            0.8,
            0.1,
            0.2,
            0.5,
            0.4,
            1,
            1,
            1,
            1,
            1,
            1,
            1,
            1,
            1,
            1,
            1,
            1,
            1,
            1,
            1,
            1,
            1,
            1,
            1,
            1,
        ],
    ],
    "GR4J": [
        ["x1", "x2", "x3", "x4"],
        [6.50488e02, -2.80648e-01, 7.89123e00, 1.89172e01],
        [1, -27, 1, 1],
        [3.00000e03, 2.70000e01, 6.60000e02, 2.40000e02],
    ],
    "GR2M": [
        ["x1", "x2"],
        [6.50488e02, -2.80648e-01],
        [1, 1e-4],  # X2 should not be negative.
        [3.00000e03, 2.70000e01],
    ],
}

_default_params.update({"SACSMA": _default_params["SAC"]})


def parameters_for(model_id: str, as_pandas_df=False):
    pname, pvals, pmin, pmax = _default_params[model_id]
    # id_prefix = 'subarea.Subarea.'
    # pname = [id_prefix + n for n in pname]
    p_spec = _df_from_dict(
        Name=pname,
        Value=_npf(pvals),
        Min=_npf(pmin),
        Max=_npf(pmax),
    )
    if as_pandas_df:
        return p_spec
    else:
        return create_parameteriser("Generic", p_spec)
