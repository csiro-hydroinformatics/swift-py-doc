# Module classes

# classes

Classes:

- **`CandidateFactorySeed`** –
- **`CompositeParameteriser`** – A parameteriser defined as the concatenation of several parameterisers.
- **`ConstraintParameteriser`** –
- **`EnsembleForecastSimulation`** –
- **`EnsembleSimulation`** – A simulation designed to facilitate model runs over ensemble of inputs
- **`ErrisStagedCalibration`** –
- **`FilteringParameteriser`** – A parameteriser designed to only show a subset to an optimiser, while applying more to a simulation. Used in log-likelihood contexts.
- **`FunctionsParameteriser`** – A parameteriser usable with a multisite multiobjective calculator.
- **`HypercubeParameteriser`** –
- **`MaerrisStagedCalibration`** –
- **`MemoryStates`** –
- **`ObjectiveEvaluator`** – Objective Evaluator
- **`ObjectiveScores`** –
- **`Optimiser`** –
- **`Parameteriser`** – Wrapper around a native parameteriser.
- **`ScalingParameteriser`** –
- **`SceTerminationCondition`** –
- **`Simulation`** – Wrapper around single dimension simulation objects
- **`SimulationMixin`** – A parent class for simulation objects. Most users are unlikely to explicitly use it.
- **`StateInitParameteriser`** – Parameteriser designed to apply to simulations by setting initial states.
- **`StateInitialiser`** –
- **`TransformParameteriser`** – Parameteriser projecting parameters in a transformed space for optimisation.
- **`VectorObjectiveScores`** –

Functions:

- **`wrap_cffi_native_handle`** –

## CandidateFactorySeed

```
CandidateFactorySeed(handle: CffiData, release_native: Callable[[CffiData], None], type_id: Optional[str] = None, prior_ref_count: int = 0)
```

Bases: `DeletableCffiNativeHandle`

## CompositeParameteriser

```
CompositeParameteriser(handle: CffiData, release_native: Callable[[CffiData], None], type_id: Optional[str] = None, prior_ref_count: int = 0)
```

Bases: `HypercubeParameteriser`

A parameteriser defined as the concatenation of several parameterisers.

Methods:

- **`add_parameter_to_hypercube`** – Add a parameter to a hypercube. Must be a type of object that is expandable, otherwise may raise an exception
- **`add_to_hypercube`** – Add entries to a hypercube. Must be a type of object that is expandable, otherwise may raise an exception.
- **`append`** – Append a parameteriser to this composite parameteriser
- **`apply_sys_config`** – Apply a model configuration to a simulation
- **`as_dataframe`** – Convert this hypercube parameteriser to a pandas data frame representation
- **`backtransform`** – Get the parameteriser values in the untransformed space
- **`clone`** –
- **`concatenate`** – Concatenates some hypercubes to a single parameteriser
- **`create_parameter_sampler`** – Creates a sampler for this parameteriser
- **`empty_composite`** – Creates an empty parameteriser to be populated with other parameterisers
- **`filtered_parameters`** – Wrap this parameteriser in a filter that can hide some parameters from an optimiser.
- **`from_dataframe`** – Create a parameteriser
- **`make_state_init_parameteriser`** – Create a parameteriser used for model state initialisation
- **`num_free_parameters`** – Number of free parameters in this hypercube parameteriser
- **`score_for_objective`** – Computes the value of an objective for this given set of parameters
- **`set_hypercube`** – Set the properties of a hypercube parameteriser. An exception will ve raised if any parameter name is unknown.
- **`set_max_parameter_value`** – Sets the value(s) of the upper bound of one or more parameter(s)
- **`set_min_parameter_value`** – Sets the value(s) of the lower bound of one or more parameter(s)
- **`set_parameter_definition`** – Sets the feasible range and value for a parameter
- **`set_parameter_value`** – Sets the value(s) of one or more parameter(s)
- **`subcatchment_parameteriser`** – Create a parameteriser that gets applied to a subset of a whole catchment
- **`supports_thread_safe_cloning`** – Is this parameteriser clonable as a deep copy, safe for multi-threading?
- **`wrap_transform`** – Create a parameteriser for which parameter transformations can be defined.

### add_parameter_to_hypercube

```
add_parameter_to_hypercube(name: str, value: float, min: float, max: float)
```

Add a parameter to a hypercube. Must be a type of object that is expandable, otherwise may raise an exception

### add_to_hypercube

```
add_to_hypercube(specs: DataFrame)
```

Add entries to a hypercube. Must be a type of object that is expandable, otherwise may raise an exception.

Parameters:

- **`specs`** (`DataFrame`) – An optional data frame description of the parameter set, with at least columns Name, Min, Max, Value.

> > > from swift2.parameteriser import create_parameteriser loglik = create_parameteriser(type='no apply') loglik.add_to_hypercube( pd.DataFrame({ "Name": c('b','m','s','a','maxobs','ct', 'censopt'), "Min": c(-30, 0, -10, -20, maxobs, censor_threshold, censopt), "Max": c(5, 0, 10, 0, maxobs, censor_threshold, censopt), "Value": c(-7, 0, 0, -10, maxobs, censor_threshold, censopt), } ) )

### append

```
append(p: HypercubeParameteriser)
```

Append a parameteriser to this composite parameteriser

Parameters:

- **`p`** (`HypercubeParameteriser`) – hypercube to append to this

### apply_sys_config

```
apply_sys_config(simulation: Simulation)
```

Apply a model configuration to a simulation

Parameters:

- **`simulation`** (`Simulation`) – simulation

### as_dataframe

```
as_dataframe() -> DataFrame
```

Convert this hypercube parameteriser to a pandas data frame representation

Returns:

- `DataFrame` – pd.DataFrame: pandas data frame

### backtransform

```
backtransform() -> HypercubeParameteriser
```

Get the parameteriser values in the untransformed space

Get the parameteriser values in the untransformed space, i.e. remove any transform added via HypercubeParameteriser.wrap_transform. This allows to transform back e.g. from a virtual parameter log_X to the underlying model (or even virtual/meta) parameter X.

Returns:

- **`HypercubeParameteriser`** ( `HypercubeParameteriser` ) – The parameters definitions without the transforms (if there are any)

Examples:

```
>>> ref_area = 250
>>> time_span = 3600
>>> ptrans = sdh.define_gr4j_scaled_parameter(ref_area, time_span)
>>> ptrans
    Name     Value       Min       Max
0    log_x4  0.305422  0.000000  2.380211
1    log_x1  0.506690  0.000000  3.778151
2    log_x3  0.315425  0.000000  3.000000
3  asinh_x2  2.637752 -3.989327  3.989327
>>> ptrans.backtransform()
Name    Value   Min     Max
0   x2  6.95511 -27.0    27.0
1   x3  2.06740   1.0  1000.0
2   x4  2.02033   1.0   240.0
3   x1  3.21137   1.0  6000.0
>>>
```

### clone

```
clone() -> HypercubeParameteriser
```

### concatenate

```
concatenate(*args: Sequence[HypercubeParameteriser], strategy: str = '') -> CompositeParameteriser
```

Concatenates some hypercubes to a single parameteriser

Parameters:

- **`strategy`** (`str`, default: `''` ) – The strategy to contatenate. Defaults to "", equivalent to "composite", the only available. May have other options in the future.

Returns:

- **`CompositeParameteriser`** ( `CompositeParameteriser` ) – A concatenated parameteriser

### create_parameter_sampler

```
create_parameter_sampler(seed: int = 0, type: str = 'urs') -> CandidateFactorySeed
```

Creates a sampler for this parameteriser

Parameters:

- **`seed`** (`int`, default: `0` ) – a seed for the sampler. Defaults to 0.
- **`type`** (`str`, default: `'urs'` ) – the type of sampler. Defaults to "urs" for Uniform Random Sampling. This is the only option supported as of 2023-01.

Returns:

- **`CandidateFactorySeed`** ( `CandidateFactorySeed` ) – a sampler, aka candidate factory

### empty_composite

```
empty_composite() -> CompositeParameteriser
```

Creates an empty parameteriser to be populated with other parameterisers

Returns:

- **`CompositeParameteriser`** ( `CompositeParameteriser` ) – composite parameteriser

### filtered_parameters

```
filtered_parameters() -> FilteringParameteriser
```

Wrap this parameteriser in a filter that can hide some parameters from an optimiser.

Used for instance in calibration with log-likelihood contexts.

Returns:

- `FilteringParameteriser` – an parameteriser designed to only show a subset to an optimiser, while applying more to a simulation.

### from_dataframe

```
from_dataframe(type='Generic subareas', definition: Optional[DataFrame] = None) -> HypercubeParameteriser
```

Create a parameteriser

Parameters:

- **`type`** (`str`, default: `'Generic subareas'` ) – A string identifying the type of parameteriser to use. Recognised types are (case insensitive) 'log-likelihood', 'generic', 'subareas', 'links', 'nodes' and 'muskingum'. Defaults to "Generic subareas".
- **`specs`** (`DataFrame`) – An optional data frame description of the parameter set, with at least columns Name, Min, Max, Value. Defaults to None.

Returns:

- **`HypercubeParameteriser`** ( `HypercubeParameteriser` ) – new parameteriser

Examples:

```
>>> d = pd.DataFrame(
...     dict(
...         Name=c("alpha", "inverse_velocity"),
...         Value=c(1, 1),
...         Min=c(1e-3, 1e-3),
...         Max=c(1e2, 1e2),
...     )
... )
>>> p = HypercubeParameteriser.from_dataframe("Generic links", d)
>>> p
```

### make_state_init_parameteriser

```
make_state_init_parameteriser() -> StateInitParameteriser
```

Create a parameteriser used for model state initialisation

This allows to define tied parameters where, for instance, pval = a * modelStateVal. A more concrete use case is to define an initial soil moisture store 'S0', as a fraction of the model store capacity 'Smax'. The model state to initialise is 'S'

Note

See also swift2.classes.ScalingParameteriser for typical joint usage.

Returns:

- **`StateInitParameteriser`** ( `StateInitParameteriser` ) – state initialisation parameteriser

Examples:

```
>>> # Use case: Set gr4j initial stores at simulation as a function of x1/x3 parameters.
>>> import swift2.parameteriser as sp
>>> # Let's define _S0_ and _R0_ parameters such that for each GR4J model instance, _S = S0 * x1_ and _R = R0 * x3_
>>> p_states = sp.linear_parameteriser(
                param_name=c("S0","R0"), # new virtual parameters to optimise
                state_name=c("S","R"), 
                scaling_var_name=c("x1","x3"),
                min_p_val=c(0.0,0.0), 
                max_p_val=c(1.0,1.0), 
                value=c(0.9,0.9), 
                selector_type='each subarea')
>>> init_parameteriser = p_states.make_state_init_parameteriser()
```

### num_free_parameters

```
num_free_parameters() -> int
```

Number of free parameters in this hypercube parameteriser

Returns:

- **`int`** ( `int` ) – Number of free parameters

### score_for_objective

```
score_for_objective(objective: ObjectiveEvaluator) -> Dict[str, Any]
```

Computes the value of an objective for this given set of parameters

### set_hypercube

```
set_hypercube(specs: DataFrame)
```

Set the properties of a hypercube parameteriser. An exception will ve raised if any parameter name is unknown.

Parameters:

- **`specs`** (`DataFrame`) – An optional data frame description of the parameter set, with at least columns Name, Min, Max, Value.

Examples:

```
>>> # e.g. if `p` is a typical parameteriser for GR4J with 
>>> # set x4 bounds to be in "days", not hours
>>> p_x4 = pd.DataFrame.from_dict({
    "Name": ["x4"],
    "Value": [1.0],
    "Min": [0.25],
    "Max": [10.0],
})
>>> p.set_hypercube(p_x4)
```

### set_max_parameter_value

```
set_max_parameter_value(variable_name: VecStr, value: VecScalars)
```

Sets the value(s) of the upper bound of one or more parameter(s)

Parameters:

- **`variable_name`** (`VecStr`) – one or more parameter name(s)
- **`value`** (`VecScalars`) – one or more parameter value(s)

### set_min_parameter_value

```
set_min_parameter_value(variable_name: VecStr, value: VecScalars)
```

Sets the value(s) of the lower bound of one or more parameter(s)

Parameters:

- **`variable_name`** (`VecStr`) – one or more parameter name(s)
- **`value`** (`VecScalars`) – one or more parameter value(s)

### set_parameter_definition

```
set_parameter_definition(variable_name: str, min: float, max: float, value: float)
```

Sets the feasible range and value for a parameter

Parameters:

- **`variable_name`** (`str`) – parameter name
- **`min`** (`float`) – min
- **`max`** (`float`) – max
- **`value`** (`float`) – value

### set_parameter_value

```
set_parameter_value(variable_name: VecStr, value: VecScalars)
```

Sets the value(s) of one or more parameter(s)

Parameters:

- **`variable_name`** (`VecStr`) – one or more parameter name(s)
- **`value`** (`VecScalars`) – one or more parameter value(s)

### subcatchment_parameteriser

```
subcatchment_parameteriser(subcatchment)
```

Create a parameteriser that gets applied to a subset of a whole catchment

Parameters:

- **`subcatchment`** (`Simulation`) – the subcatchment, subset of a whole catchment, identifying which elements (subareas, nodes, links) will be parameterised by the new parameteriser. Other catchment elements are untouched.

Returns:

- **`HypercubeParameteriser`** – New parameteriser whose application is limited to the subcatchment.

Examples:

```
>>> sub_cats = simulation.split_to_subcatchments(["node.node_7", "node.node_10"])
>>> sc = sub_cats["node.node_7"]
>>> p = sp.create_parameteriser('generic subarea')
>>> p.add_parameter_to_hypercube("x1", 32, 1, 6e3)
>>> sp = p.subcatchment_parameteriser(sc)
>>> sp.apply_sys_config(simulation)
```

### supports_thread_safe_cloning

```
supports_thread_safe_cloning() -> bool
```

Is this parameteriser clonable as a deep copy, safe for multi-threading?

### wrap_transform

```
wrap_transform() -> TransformParameteriser
```

Create a parameteriser for which parameter transformations can be defined.

This allows to define e.g. a virtual parameter log_X instead of calibrating on the parameter X.

Returns:

- **`TransformParameteriser`** ( `TransformParameteriser` ) – A new parameteriser (TransformParameteriser) which has methods to define parameter transforms

## ConstraintParameteriser

```
ConstraintParameteriser(handle: CffiData, release_native: Callable[[CffiData], None], type_id: Optional[str] = None, prior_ref_count: int = 0)
```

Bases: `HypercubeParameteriser`

Methods:

- **`add_parameter_to_hypercube`** – Add a parameter to a hypercube. Must be a type of object that is expandable, otherwise may raise an exception
- **`add_to_hypercube`** – Add entries to a hypercube. Must be a type of object that is expandable, otherwise may raise an exception.
- **`apply_sys_config`** – Apply a model configuration to a simulation
- **`as_dataframe`** – Convert this hypercube parameteriser to a pandas data frame representation
- **`backtransform`** – Get the parameteriser values in the untransformed space
- **`clone`** –
- **`create_parameter_sampler`** – Creates a sampler for this parameteriser
- **`filtered_parameters`** – Wrap this parameteriser in a filter that can hide some parameters from an optimiser.
- **`from_dataframe`** – Create a parameteriser
- **`make_state_init_parameteriser`** – Create a parameteriser used for model state initialisation
- **`num_free_parameters`** – Number of free parameters in this hypercube parameteriser
- **`score_for_objective`** – Computes the value of an objective for this given set of parameters
- **`set_hypercube`** – Set the properties of a hypercube parameteriser. An exception will ve raised if any parameter name is unknown.
- **`set_max_parameter_value`** – Sets the value(s) of the upper bound of one or more parameter(s)
- **`set_min_parameter_value`** – Sets the value(s) of the lower bound of one or more parameter(s)
- **`set_parameter_definition`** – Sets the feasible range and value for a parameter
- **`set_parameter_value`** – Sets the value(s) of one or more parameter(s)
- **`subcatchment_parameteriser`** – Create a parameteriser that gets applied to a subset of a whole catchment
- **`supports_thread_safe_cloning`** – Is this parameteriser clonable as a deep copy, safe for multi-threading?
- **`wrap_transform`** – Create a parameteriser for which parameter transformations can be defined.

### add_parameter_to_hypercube

```
add_parameter_to_hypercube(name: str, value: float, min: float, max: float)
```

Add a parameter to a hypercube. Must be a type of object that is expandable, otherwise may raise an exception

### add_to_hypercube

```
add_to_hypercube(specs: DataFrame)
```

Add entries to a hypercube. Must be a type of object that is expandable, otherwise may raise an exception.

Parameters:

- **`specs`** (`DataFrame`) – An optional data frame description of the parameter set, with at least columns Name, Min, Max, Value.

> > > from swift2.parameteriser import create_parameteriser loglik = create_parameteriser(type='no apply') loglik.add_to_hypercube( pd.DataFrame({ "Name": c('b','m','s','a','maxobs','ct', 'censopt'), "Min": c(-30, 0, -10, -20, maxobs, censor_threshold, censopt), "Max": c(5, 0, 10, 0, maxobs, censor_threshold, censopt), "Value": c(-7, 0, 0, -10, maxobs, censor_threshold, censopt), } ) )

### apply_sys_config

```
apply_sys_config(simulation: Simulation)
```

Apply a model configuration to a simulation

Parameters:

- **`simulation`** (`Simulation`) – simulation

### as_dataframe

```
as_dataframe() -> DataFrame
```

Convert this hypercube parameteriser to a pandas data frame representation

Returns:

- `DataFrame` – pd.DataFrame: pandas data frame

### backtransform

```
backtransform() -> HypercubeParameteriser
```

Get the parameteriser values in the untransformed space

Get the parameteriser values in the untransformed space, i.e. remove any transform added via HypercubeParameteriser.wrap_transform. This allows to transform back e.g. from a virtual parameter log_X to the underlying model (or even virtual/meta) parameter X.

Returns:

- **`HypercubeParameteriser`** ( `HypercubeParameteriser` ) – The parameters definitions without the transforms (if there are any)

Examples:

```
>>> ref_area = 250
>>> time_span = 3600
>>> ptrans = sdh.define_gr4j_scaled_parameter(ref_area, time_span)
>>> ptrans
    Name     Value       Min       Max
0    log_x4  0.305422  0.000000  2.380211
1    log_x1  0.506690  0.000000  3.778151
2    log_x3  0.315425  0.000000  3.000000
3  asinh_x2  2.637752 -3.989327  3.989327
>>> ptrans.backtransform()
Name    Value   Min     Max
0   x2  6.95511 -27.0    27.0
1   x3  2.06740   1.0  1000.0
2   x4  2.02033   1.0   240.0
3   x1  3.21137   1.0  6000.0
>>>
```

### clone

```
clone() -> HypercubeParameteriser
```

### create_parameter_sampler

```
create_parameter_sampler(seed: int = 0, type: str = 'urs') -> CandidateFactorySeed
```

Creates a sampler for this parameteriser

Parameters:

- **`seed`** (`int`, default: `0` ) – a seed for the sampler. Defaults to 0.
- **`type`** (`str`, default: `'urs'` ) – the type of sampler. Defaults to "urs" for Uniform Random Sampling. This is the only option supported as of 2023-01.

Returns:

- **`CandidateFactorySeed`** ( `CandidateFactorySeed` ) – a sampler, aka candidate factory

### filtered_parameters

```
filtered_parameters() -> FilteringParameteriser
```

Wrap this parameteriser in a filter that can hide some parameters from an optimiser.

Used for instance in calibration with log-likelihood contexts.

Returns:

- `FilteringParameteriser` – an parameteriser designed to only show a subset to an optimiser, while applying more to a simulation.

### from_dataframe

```
from_dataframe(type='Generic subareas', definition: Optional[DataFrame] = None) -> HypercubeParameteriser
```

Create a parameteriser

Parameters:

- **`type`** (`str`, default: `'Generic subareas'` ) – A string identifying the type of parameteriser to use. Recognised types are (case insensitive) 'log-likelihood', 'generic', 'subareas', 'links', 'nodes' and 'muskingum'. Defaults to "Generic subareas".
- **`specs`** (`DataFrame`) – An optional data frame description of the parameter set, with at least columns Name, Min, Max, Value. Defaults to None.

Returns:

- **`HypercubeParameteriser`** ( `HypercubeParameteriser` ) – new parameteriser

Examples:

```
>>> d = pd.DataFrame(
...     dict(
...         Name=c("alpha", "inverse_velocity"),
...         Value=c(1, 1),
...         Min=c(1e-3, 1e-3),
...         Max=c(1e2, 1e2),
...     )
... )
>>> p = HypercubeParameteriser.from_dataframe("Generic links", d)
>>> p
```

### make_state_init_parameteriser

```
make_state_init_parameteriser() -> StateInitParameteriser
```

Create a parameteriser used for model state initialisation

This allows to define tied parameters where, for instance, pval = a * modelStateVal. A more concrete use case is to define an initial soil moisture store 'S0', as a fraction of the model store capacity 'Smax'. The model state to initialise is 'S'

Note

See also swift2.classes.ScalingParameteriser for typical joint usage.

Returns:

- **`StateInitParameteriser`** ( `StateInitParameteriser` ) – state initialisation parameteriser

Examples:

```
>>> # Use case: Set gr4j initial stores at simulation as a function of x1/x3 parameters.
>>> import swift2.parameteriser as sp
>>> # Let's define _S0_ and _R0_ parameters such that for each GR4J model instance, _S = S0 * x1_ and _R = R0 * x3_
>>> p_states = sp.linear_parameteriser(
                param_name=c("S0","R0"), # new virtual parameters to optimise
                state_name=c("S","R"), 
                scaling_var_name=c("x1","x3"),
                min_p_val=c(0.0,0.0), 
                max_p_val=c(1.0,1.0), 
                value=c(0.9,0.9), 
                selector_type='each subarea')
>>> init_parameteriser = p_states.make_state_init_parameteriser()
```

### num_free_parameters

```
num_free_parameters() -> int
```

Number of free parameters in this hypercube parameteriser

Returns:

- **`int`** ( `int` ) – Number of free parameters

### score_for_objective

```
score_for_objective(objective: ObjectiveEvaluator) -> Dict[str, Any]
```

Computes the value of an objective for this given set of parameters

### set_hypercube

```
set_hypercube(specs: DataFrame)
```

Set the properties of a hypercube parameteriser. An exception will ve raised if any parameter name is unknown.

Parameters:

- **`specs`** (`DataFrame`) – An optional data frame description of the parameter set, with at least columns Name, Min, Max, Value.

Examples:

```
>>> # e.g. if `p` is a typical parameteriser for GR4J with 
>>> # set x4 bounds to be in "days", not hours
>>> p_x4 = pd.DataFrame.from_dict({
    "Name": ["x4"],
    "Value": [1.0],
    "Min": [0.25],
    "Max": [10.0],
})
>>> p.set_hypercube(p_x4)
```

### set_max_parameter_value

```
set_max_parameter_value(variable_name: VecStr, value: VecScalars)
```

Sets the value(s) of the upper bound of one or more parameter(s)

Parameters:

- **`variable_name`** (`VecStr`) – one or more parameter name(s)
- **`value`** (`VecScalars`) – one or more parameter value(s)

### set_min_parameter_value

```
set_min_parameter_value(variable_name: VecStr, value: VecScalars)
```

Sets the value(s) of the lower bound of one or more parameter(s)

Parameters:

- **`variable_name`** (`VecStr`) – one or more parameter name(s)
- **`value`** (`VecScalars`) – one or more parameter value(s)

### set_parameter_definition

```
set_parameter_definition(variable_name: str, min: float, max: float, value: float)
```

Sets the feasible range and value for a parameter

Parameters:

- **`variable_name`** (`str`) – parameter name
- **`min`** (`float`) – min
- **`max`** (`float`) – max
- **`value`** (`float`) – value

### set_parameter_value

```
set_parameter_value(variable_name: VecStr, value: VecScalars)
```

Sets the value(s) of one or more parameter(s)

Parameters:

- **`variable_name`** (`VecStr`) – one or more parameter name(s)
- **`value`** (`VecScalars`) – one or more parameter value(s)

### subcatchment_parameteriser

```
subcatchment_parameteriser(subcatchment)
```

Create a parameteriser that gets applied to a subset of a whole catchment

Parameters:

- **`subcatchment`** (`Simulation`) – the subcatchment, subset of a whole catchment, identifying which elements (subareas, nodes, links) will be parameterised by the new parameteriser. Other catchment elements are untouched.

Returns:

- **`HypercubeParameteriser`** – New parameteriser whose application is limited to the subcatchment.

Examples:

```
>>> sub_cats = simulation.split_to_subcatchments(["node.node_7", "node.node_10"])
>>> sc = sub_cats["node.node_7"]
>>> p = sp.create_parameteriser('generic subarea')
>>> p.add_parameter_to_hypercube("x1", 32, 1, 6e3)
>>> sp = p.subcatchment_parameteriser(sc)
>>> sp.apply_sys_config(simulation)
```

### supports_thread_safe_cloning

```
supports_thread_safe_cloning() -> bool
```

Is this parameteriser clonable as a deep copy, safe for multi-threading?

### wrap_transform

```
wrap_transform() -> TransformParameteriser
```

Create a parameteriser for which parameter transformations can be defined.

This allows to define e.g. a virtual parameter log_X instead of calibrating on the parameter X.

Returns:

- **`TransformParameteriser`** ( `TransformParameteriser` ) – A new parameteriser (TransformParameteriser) which has methods to define parameter transforms

## EnsembleForecastSimulation

```
EnsembleForecastSimulation(handle: CffiData, release_native: Callable[[CffiData], None], type_id: Optional[str] = None, prior_ref_count: int = 0)
```

Bases: `DeletableCffiNativeHandle`, `SimulationMixin`

Methods:

- **`exec_simulation`** – Execute a simulation
- **`get_played_varnames`** – Gets all the names of states fed an input time series
- **`get_recorded_ensemble_forecast`** –
- **`get_recorded_varnames`** – Gets all the names of the recorded states
- **`get_simulation_span`** –
- **`record_ensemble_forecast_state`** –
- **`record_state`** – Record a time series of one of the state of the model

### exec_simulation

```
exec_simulation(reset_initial_states: bool = True) -> None
```

Execute a simulation

Parameters:

- **`reset_initial_states`** (`bool`, default: `True` ) – logical, should the states of the model be reinitialized before the first time step.

### get_played_varnames

```
get_played_varnames() -> List[str]
```

Gets all the names of states fed an input time series

Returns:

- `List[str]` – List\[str\]: The names of the state variables fed over the simulation with values from a time series

### get_recorded_ensemble_forecast

```
get_recorded_ensemble_forecast(var_id: str, start_time: ConvertibleToTimestamp = None, end_time: ConvertibleToTimestamp = None) -> EnsembleForecastTimeSeries
```

### get_recorded_varnames

```
get_recorded_varnames() -> List[str]
```

Gets all the names of the recorded states

Returns:

- `List[str]` – List\[str\]: The names of the state variables being recorded into time series

### get_simulation_span

```
get_simulation_span()
```

### record_ensemble_forecast_state

```
record_ensemble_forecast_state(var_ids: VecStr = CATCHMENT_FLOWRATE_VARID, recording_provider: Optional[TimeSeriesLibrary] = None, data_ids: Optional[VecStr] = None) -> None
```

### record_state

```
record_state(var_ids: VecStr = CATCHMENT_FLOWRATE_VARID, recording_provider: Optional[TimeSeriesLibrary] = None, data_ids: Optional[VecStr] = None) -> None
```

Record a time series of one of the state of the model

Parameters:

- **`var_ids`** (`VecStr`, default: `CATCHMENT_FLOWRATE_VARID` ) – identifier(s) of the output variable recorded to a time series, e.g. 'Catchment|StreamflowRate' or 'subcatchment.Subarea.runoff'. Defaults to CATCHMENT_FLOWRATE_VARID.
- **`recording_provider`** (`TimeSeriesLibrary`, default: `None` ) – description. Defaults to None.
- **`data_ids`** (`VecStr`, default: `None` ) – description. Defaults to None.

Raises:

- `ValueError` – description

## EnsembleSimulation

```
EnsembleSimulation(handle: CffiData, release_native: Callable[[CffiData], None], type_id: Optional[str] = None, prior_ref_count: int = 0)
```

Bases: `DeletableCffiNativeHandle`

A simulation designed to facilitate model runs over ensemble of inputs

Methods:

- **`get_simulation_span`** – Gets the span of the simulation: start, end, time step
- **`record`** – Records a state variable of the simualtion
- **`record_ensemble_state`** – Records one or more state values from an ensemble simulation
- **`setup`** – Sets up this ensemble simulation

### get_simulation_span

```
get_simulation_span() -> Dict[str, Any]
```

Gets the span of the simulation: start, end, time step

Returns:

- `Dict[str, Any]` – Dict\[str, Any\]: simulation span

### record

```
record(variable_id: str) -> None
```

Records a state variable of the simualtion

Parameters:

- **`variable_id`** (`str`) – state variable identifier

### record_ensemble_state

```
record_ensemble_state(var_ids: VecStr = CATCHMENT_FLOWRATE_VARID, recording_provider: Optional[TimeSeriesLibrary] = None, data_ids: Optional[VecStr] = None) -> None
```

Records one or more state values from an ensemble simulation

Parameters:

- **`var_ids`** (`VecStr`, default: `CATCHMENT_FLOWRATE_VARID` ) – Model variable identierfier(s). Defaults to CATCHMENT_FLOWRATE_VARID.
- **`recording_provider`** (`Optional[TimeSeriesLibrary]`, default: `None` ) – An optional time series library to record to. Defaults to None.
- **`data_ids`** (`Optional[VecStr]`, default: `None` ) – Data identifier(s). Defaults to None.

### setup

```
setup(forecast_start: datetime, ensemble_size: int, forecast_horizon_length: int) -> None
```

Sets up this ensemble simulation

Parameters:

- **`forecast_start`** (`datetime`) – Start date for the simulation
- **`ensemble_size`** (`int`) – size of the ensemble
- **`forecast_horizon_length`** (`int`) – length of the simulation in numbers of time steps.

## ErrisStagedCalibration

```
ErrisStagedCalibration(handle: CffiData, release_native: Callable[[CffiData], None], type_id: Optional[str] = None, prior_ref_count: int = 0)
```

Bases: `DeletableCffiNativeHandle`

Methods:

- **`extract_optimisation_log`** –

### extract_optimisation_log

```
extract_optimisation_log(fitness_name='log.likelihood')
```

## FilteringParameteriser

```
FilteringParameteriser(handle: CffiData, release_native: Callable[[CffiData], None], type_id: Optional[str] = None, prior_ref_count: int = 0)
```

Bases: `HypercubeParameteriser`

A parameteriser designed to only show a subset to an optimiser, while applying more to a simulation. Used in log-likelihood contexts.

Methods:

- **`add_parameter_to_hypercube`** – Add a parameter to a hypercube. Must be a type of object that is expandable, otherwise may raise an exception
- **`add_to_hypercube`** – Add entries to a hypercube. Must be a type of object that is expandable, otherwise may raise an exception.
- **`apply_sys_config`** – Apply a model configuration to a simulation
- **`as_dataframe`** – Convert this hypercube parameteriser to a pandas data frame representation
- **`backtransform`** – Get the parameteriser values in the untransformed space
- **`clone`** –
- **`create_parameter_sampler`** – Creates a sampler for this parameteriser
- **`filtered_parameters`** – Wrap this parameteriser in a filter that can hide some parameters from an optimiser.
- **`from_dataframe`** – Create a parameteriser
- **`hide_parameters`** – Hide some parameters (from the outside e.g. optimisers) in a filter parameteriser
- **`make_state_init_parameteriser`** – Create a parameteriser used for model state initialisation
- **`num_free_parameters`** – Number of free parameters in this hypercube parameteriser
- **`score_for_objective`** – Computes the value of an objective for this given set of parameters
- **`set_hypercube`** – Set the properties of a hypercube parameteriser. An exception will ve raised if any parameter name is unknown.
- **`set_max_parameter_value`** – Sets the value(s) of the upper bound of one or more parameter(s)
- **`set_min_parameter_value`** – Sets the value(s) of the lower bound of one or more parameter(s)
- **`set_parameter_definition`** – Sets the feasible range and value for a parameter
- **`set_parameter_value`** – Sets the value(s) of one or more parameter(s)
- **`show_parameters`** – Show some parameters (from the outside e.g. optimisers) in a filter parameteriser
- **`subcatchment_parameteriser`** – Create a parameteriser that gets applied to a subset of a whole catchment
- **`supports_thread_safe_cloning`** – Is this parameteriser clonable as a deep copy, safe for multi-threading?
- **`wrap_transform`** – Create a parameteriser for which parameter transformations can be defined.

### add_parameter_to_hypercube

```
add_parameter_to_hypercube(name: str, value: float, min: float, max: float)
```

Add a parameter to a hypercube. Must be a type of object that is expandable, otherwise may raise an exception

### add_to_hypercube

```
add_to_hypercube(specs: DataFrame)
```

Add entries to a hypercube. Must be a type of object that is expandable, otherwise may raise an exception.

Parameters:

- **`specs`** (`DataFrame`) – An optional data frame description of the parameter set, with at least columns Name, Min, Max, Value.

> > > from swift2.parameteriser import create_parameteriser loglik = create_parameteriser(type='no apply') loglik.add_to_hypercube( pd.DataFrame({ "Name": c('b','m','s','a','maxobs','ct', 'censopt'), "Min": c(-30, 0, -10, -20, maxobs, censor_threshold, censopt), "Max": c(5, 0, 10, 0, maxobs, censor_threshold, censopt), "Value": c(-7, 0, 0, -10, maxobs, censor_threshold, censopt), } ) )

### apply_sys_config

```
apply_sys_config(simulation: Simulation)
```

Apply a model configuration to a simulation

Parameters:

- **`simulation`** (`Simulation`) – simulation

### as_dataframe

```
as_dataframe() -> DataFrame
```

Convert this hypercube parameteriser to a pandas data frame representation

Returns:

- `DataFrame` – pd.DataFrame: pandas data frame

### backtransform

```
backtransform() -> HypercubeParameteriser
```

Get the parameteriser values in the untransformed space

Get the parameteriser values in the untransformed space, i.e. remove any transform added via HypercubeParameteriser.wrap_transform. This allows to transform back e.g. from a virtual parameter log_X to the underlying model (or even virtual/meta) parameter X.

Returns:

- **`HypercubeParameteriser`** ( `HypercubeParameteriser` ) – The parameters definitions without the transforms (if there are any)

Examples:

```
>>> ref_area = 250
>>> time_span = 3600
>>> ptrans = sdh.define_gr4j_scaled_parameter(ref_area, time_span)
>>> ptrans
    Name     Value       Min       Max
0    log_x4  0.305422  0.000000  2.380211
1    log_x1  0.506690  0.000000  3.778151
2    log_x3  0.315425  0.000000  3.000000
3  asinh_x2  2.637752 -3.989327  3.989327
>>> ptrans.backtransform()
Name    Value   Min     Max
0   x2  6.95511 -27.0    27.0
1   x3  2.06740   1.0  1000.0
2   x4  2.02033   1.0   240.0
3   x1  3.21137   1.0  6000.0
>>>
```

### clone

```
clone() -> HypercubeParameteriser
```

### create_parameter_sampler

```
create_parameter_sampler(seed: int = 0, type: str = 'urs') -> CandidateFactorySeed
```

Creates a sampler for this parameteriser

Parameters:

- **`seed`** (`int`, default: `0` ) – a seed for the sampler. Defaults to 0.
- **`type`** (`str`, default: `'urs'` ) – the type of sampler. Defaults to "urs" for Uniform Random Sampling. This is the only option supported as of 2023-01.

Returns:

- **`CandidateFactorySeed`** ( `CandidateFactorySeed` ) – a sampler, aka candidate factory

### filtered_parameters

```
filtered_parameters() -> FilteringParameteriser
```

Wrap this parameteriser in a filter that can hide some parameters from an optimiser.

Used for instance in calibration with log-likelihood contexts.

Returns:

- `FilteringParameteriser` – an parameteriser designed to only show a subset to an optimiser, while applying more to a simulation.

### from_dataframe

```
from_dataframe(type='Generic subareas', definition: Optional[DataFrame] = None) -> HypercubeParameteriser
```

Create a parameteriser

Parameters:

- **`type`** (`str`, default: `'Generic subareas'` ) – A string identifying the type of parameteriser to use. Recognised types are (case insensitive) 'log-likelihood', 'generic', 'subareas', 'links', 'nodes' and 'muskingum'. Defaults to "Generic subareas".
- **`specs`** (`DataFrame`) – An optional data frame description of the parameter set, with at least columns Name, Min, Max, Value. Defaults to None.

Returns:

- **`HypercubeParameteriser`** ( `HypercubeParameteriser` ) – new parameteriser

Examples:

```
>>> d = pd.DataFrame(
...     dict(
...         Name=c("alpha", "inverse_velocity"),
...         Value=c(1, 1),
...         Min=c(1e-3, 1e-3),
...         Max=c(1e2, 1e2),
...     )
... )
>>> p = HypercubeParameteriser.from_dataframe("Generic links", d)
>>> p
```

### hide_parameters

```
hide_parameters(patterns, regex=False, starts_with=False, strict=False)
```

Hide some parameters (from the outside e.g. optimisers) in a filter parameteriser

Parameters:

- **`patterns`** (`[type]`) – character, one or more pattern to match and hide matching parameters. Match according to other parameters.
- **`regex`** (`bool`, default: `False` ) – logical, defaults False, should the patterns be used as regular expressions.. Defaults to False.
- **`starts_with`** (`bool`, default: `False` ) – logical, defaults False. Ignored if regex is True. Should the patterns be used as starting strings in the parameter names.. Defaults to False.
- **`strict`** (`bool`, default: `False` ) – logical, default False. Used only if regex and starts_with are False. If True, raises an error if one of the "patterns" has no exact match in the parameters.. Defaults to False.

### make_state_init_parameteriser

```
make_state_init_parameteriser() -> StateInitParameteriser
```

Create a parameteriser used for model state initialisation

This allows to define tied parameters where, for instance, pval = a * modelStateVal. A more concrete use case is to define an initial soil moisture store 'S0', as a fraction of the model store capacity 'Smax'. The model state to initialise is 'S'

Note

See also swift2.classes.ScalingParameteriser for typical joint usage.

Returns:

- **`StateInitParameteriser`** ( `StateInitParameteriser` ) – state initialisation parameteriser

Examples:

```
>>> # Use case: Set gr4j initial stores at simulation as a function of x1/x3 parameters.
>>> import swift2.parameteriser as sp
>>> # Let's define _S0_ and _R0_ parameters such that for each GR4J model instance, _S = S0 * x1_ and _R = R0 * x3_
>>> p_states = sp.linear_parameteriser(
                param_name=c("S0","R0"), # new virtual parameters to optimise
                state_name=c("S","R"), 
                scaling_var_name=c("x1","x3"),
                min_p_val=c(0.0,0.0), 
                max_p_val=c(1.0,1.0), 
                value=c(0.9,0.9), 
                selector_type='each subarea')
>>> init_parameteriser = p_states.make_state_init_parameteriser()
```

### num_free_parameters

```
num_free_parameters() -> int
```

Number of free parameters in this hypercube parameteriser

Returns:

- **`int`** ( `int` ) – Number of free parameters

### score_for_objective

```
score_for_objective(objective: ObjectiveEvaluator) -> Dict[str, Any]
```

Computes the value of an objective for this given set of parameters

### set_hypercube

```
set_hypercube(specs: DataFrame)
```

Set the properties of a hypercube parameteriser. An exception will ve raised if any parameter name is unknown.

Parameters:

- **`specs`** (`DataFrame`) – An optional data frame description of the parameter set, with at least columns Name, Min, Max, Value.

Examples:

```
>>> # e.g. if `p` is a typical parameteriser for GR4J with 
>>> # set x4 bounds to be in "days", not hours
>>> p_x4 = pd.DataFrame.from_dict({
    "Name": ["x4"],
    "Value": [1.0],
    "Min": [0.25],
    "Max": [10.0],
})
>>> p.set_hypercube(p_x4)
```

### set_max_parameter_value

```
set_max_parameter_value(variable_name: VecStr, value: VecScalars)
```

Sets the value(s) of the upper bound of one or more parameter(s)

Parameters:

- **`variable_name`** (`VecStr`) – one or more parameter name(s)
- **`value`** (`VecScalars`) – one or more parameter value(s)

### set_min_parameter_value

```
set_min_parameter_value(variable_name: VecStr, value: VecScalars)
```

Sets the value(s) of the lower bound of one or more parameter(s)

Parameters:

- **`variable_name`** (`VecStr`) – one or more parameter name(s)
- **`value`** (`VecScalars`) – one or more parameter value(s)

### set_parameter_definition

```
set_parameter_definition(variable_name: str, min: float, max: float, value: float)
```

Sets the feasible range and value for a parameter

Parameters:

- **`variable_name`** (`str`) – parameter name
- **`min`** (`float`) – min
- **`max`** (`float`) – max
- **`value`** (`float`) – value

### set_parameter_value

```
set_parameter_value(variable_name: VecStr, value: VecScalars)
```

Sets the value(s) of one or more parameter(s)

Parameters:

- **`variable_name`** (`VecStr`) – one or more parameter name(s)
- **`value`** (`VecScalars`) – one or more parameter value(s)

### show_parameters

```
show_parameters(patterns, regex=False, starts_with=False)
```

Show some parameters (from the outside e.g. optimisers) in a filter parameteriser

Parameters:

- **`patterns`** (`[type]`) – character, one or more pattern to match and show matching parameters. Match according to other parameters
- **`regex`** (`bool`, default: `False` ) – should the patterns be used as regular expressions. Defaults to False.
- **`starts_with`** (`bool`, default: `False` ) – should the patterns be used as starting strings in the parameter names. Defaults to False.

### subcatchment_parameteriser

```
subcatchment_parameteriser(subcatchment)
```

Create a parameteriser that gets applied to a subset of a whole catchment

Parameters:

- **`subcatchment`** (`Simulation`) – the subcatchment, subset of a whole catchment, identifying which elements (subareas, nodes, links) will be parameterised by the new parameteriser. Other catchment elements are untouched.

Returns:

- **`HypercubeParameteriser`** – New parameteriser whose application is limited to the subcatchment.

Examples:

```
>>> sub_cats = simulation.split_to_subcatchments(["node.node_7", "node.node_10"])
>>> sc = sub_cats["node.node_7"]
>>> p = sp.create_parameteriser('generic subarea')
>>> p.add_parameter_to_hypercube("x1", 32, 1, 6e3)
>>> sp = p.subcatchment_parameteriser(sc)
>>> sp.apply_sys_config(simulation)
```

### supports_thread_safe_cloning

```
supports_thread_safe_cloning() -> bool
```

Is this parameteriser clonable as a deep copy, safe for multi-threading?

### wrap_transform

```
wrap_transform() -> TransformParameteriser
```

Create a parameteriser for which parameter transformations can be defined.

This allows to define e.g. a virtual parameter log_X instead of calibrating on the parameter X.

Returns:

- **`TransformParameteriser`** ( `TransformParameteriser` ) – A new parameteriser (TransformParameteriser) which has methods to define parameter transforms

## FunctionsParameteriser

```
FunctionsParameteriser(handle: CffiData, release_native: Callable[[CffiData], None], type_id: Optional[str] = None, prior_ref_count: int = 0)
```

Bases: `HypercubeParameteriser`

A parameteriser usable with a multisite multiobjective calculator.

This is an advanced topic, see function `create_multisite_obj_parameteriser`. Users may refer to [this sample workflow](https://csiro-hydroinformatics.github.io/swift-py-doc/notebooks/calibrate_multisite/)

Methods:

- **`add_parameter_to_hypercube`** – Add a parameter to a hypercube. Must be a type of object that is expandable, otherwise may raise an exception
- **`add_to_hypercube`** – Add entries to a hypercube. Must be a type of object that is expandable, otherwise may raise an exception.
- **`apply_sys_config`** – Apply a model configuration to a simulation
- **`as_dataframe`** – Convert this hypercube parameteriser to a pandas data frame representation
- **`backtransform`** – Get the parameteriser values in the untransformed space
- **`clone`** –
- **`create_parameter_sampler`** – Creates a sampler for this parameteriser
- **`filtered_parameters`** – Wrap this parameteriser in a filter that can hide some parameters from an optimiser.
- **`from_dataframe`** – Create a parameteriser
- **`make_state_init_parameteriser`** – Create a parameteriser used for model state initialisation
- **`num_free_parameters`** – Number of free parameters in this hypercube parameteriser
- **`score_for_objective`** – Computes the value of an objective for this given set of parameters
- **`set_hypercube`** – Set the properties of a hypercube parameteriser. An exception will ve raised if any parameter name is unknown.
- **`set_max_parameter_value`** – Sets the value(s) of the upper bound of one or more parameter(s)
- **`set_min_parameter_value`** – Sets the value(s) of the lower bound of one or more parameter(s)
- **`set_parameter_definition`** – Sets the feasible range and value for a parameter
- **`set_parameter_value`** – Sets the value(s) of one or more parameter(s)
- **`subcatchment_parameteriser`** – Create a parameteriser that gets applied to a subset of a whole catchment
- **`supports_thread_safe_cloning`** – Is this parameteriser clonable as a deep copy, safe for multi-threading?
- **`wrap_transform`** – Create a parameteriser for which parameter transformations can be defined.

### add_parameter_to_hypercube

```
add_parameter_to_hypercube(name: str, value: float, min: float, max: float)
```

Add a parameter to a hypercube. Must be a type of object that is expandable, otherwise may raise an exception

### add_to_hypercube

```
add_to_hypercube(specs: DataFrame)
```

Add entries to a hypercube. Must be a type of object that is expandable, otherwise may raise an exception.

Parameters:

- **`specs`** (`DataFrame`) – An optional data frame description of the parameter set, with at least columns Name, Min, Max, Value.

> > > from swift2.parameteriser import create_parameteriser loglik = create_parameteriser(type='no apply') loglik.add_to_hypercube( pd.DataFrame({ "Name": c('b','m','s','a','maxobs','ct', 'censopt'), "Min": c(-30, 0, -10, -20, maxobs, censor_threshold, censopt), "Max": c(5, 0, 10, 0, maxobs, censor_threshold, censopt), "Value": c(-7, 0, 0, -10, maxobs, censor_threshold, censopt), } ) )

### apply_sys_config

```
apply_sys_config(simulation: Simulation)
```

Apply a model configuration to a simulation

Parameters:

- **`simulation`** (`Simulation`) – simulation

### as_dataframe

```
as_dataframe() -> DataFrame
```

Convert this hypercube parameteriser to a pandas data frame representation

Returns:

- `DataFrame` – pd.DataFrame: pandas data frame

### backtransform

```
backtransform() -> HypercubeParameteriser
```

Get the parameteriser values in the untransformed space

Get the parameteriser values in the untransformed space, i.e. remove any transform added via HypercubeParameteriser.wrap_transform. This allows to transform back e.g. from a virtual parameter log_X to the underlying model (or even virtual/meta) parameter X.

Returns:

- **`HypercubeParameteriser`** ( `HypercubeParameteriser` ) – The parameters definitions without the transforms (if there are any)

Examples:

```
>>> ref_area = 250
>>> time_span = 3600
>>> ptrans = sdh.define_gr4j_scaled_parameter(ref_area, time_span)
>>> ptrans
    Name     Value       Min       Max
0    log_x4  0.305422  0.000000  2.380211
1    log_x1  0.506690  0.000000  3.778151
2    log_x3  0.315425  0.000000  3.000000
3  asinh_x2  2.637752 -3.989327  3.989327
>>> ptrans.backtransform()
Name    Value   Min     Max
0   x2  6.95511 -27.0    27.0
1   x3  2.06740   1.0  1000.0
2   x4  2.02033   1.0   240.0
3   x1  3.21137   1.0  6000.0
>>>
```

### clone

```
clone() -> HypercubeParameteriser
```

### create_parameter_sampler

```
create_parameter_sampler(seed: int = 0, type: str = 'urs') -> CandidateFactorySeed
```

Creates a sampler for this parameteriser

Parameters:

- **`seed`** (`int`, default: `0` ) – a seed for the sampler. Defaults to 0.
- **`type`** (`str`, default: `'urs'` ) – the type of sampler. Defaults to "urs" for Uniform Random Sampling. This is the only option supported as of 2023-01.

Returns:

- **`CandidateFactorySeed`** ( `CandidateFactorySeed` ) – a sampler, aka candidate factory

### filtered_parameters

```
filtered_parameters() -> FilteringParameteriser
```

Wrap this parameteriser in a filter that can hide some parameters from an optimiser.

Used for instance in calibration with log-likelihood contexts.

Returns:

- `FilteringParameteriser` – an parameteriser designed to only show a subset to an optimiser, while applying more to a simulation.

### from_dataframe

```
from_dataframe(type='Generic subareas', definition: Optional[DataFrame] = None) -> HypercubeParameteriser
```

Create a parameteriser

Parameters:

- **`type`** (`str`, default: `'Generic subareas'` ) – A string identifying the type of parameteriser to use. Recognised types are (case insensitive) 'log-likelihood', 'generic', 'subareas', 'links', 'nodes' and 'muskingum'. Defaults to "Generic subareas".
- **`specs`** (`DataFrame`) – An optional data frame description of the parameter set, with at least columns Name, Min, Max, Value. Defaults to None.

Returns:

- **`HypercubeParameteriser`** ( `HypercubeParameteriser` ) – new parameteriser

Examples:

```
>>> d = pd.DataFrame(
...     dict(
...         Name=c("alpha", "inverse_velocity"),
...         Value=c(1, 1),
...         Min=c(1e-3, 1e-3),
...         Max=c(1e2, 1e2),
...     )
... )
>>> p = HypercubeParameteriser.from_dataframe("Generic links", d)
>>> p
```

### make_state_init_parameteriser

```
make_state_init_parameteriser() -> StateInitParameteriser
```

Create a parameteriser used for model state initialisation

This allows to define tied parameters where, for instance, pval = a * modelStateVal. A more concrete use case is to define an initial soil moisture store 'S0', as a fraction of the model store capacity 'Smax'. The model state to initialise is 'S'

Note

See also swift2.classes.ScalingParameteriser for typical joint usage.

Returns:

- **`StateInitParameteriser`** ( `StateInitParameteriser` ) – state initialisation parameteriser

Examples:

```
>>> # Use case: Set gr4j initial stores at simulation as a function of x1/x3 parameters.
>>> import swift2.parameteriser as sp
>>> # Let's define _S0_ and _R0_ parameters such that for each GR4J model instance, _S = S0 * x1_ and _R = R0 * x3_
>>> p_states = sp.linear_parameteriser(
                param_name=c("S0","R0"), # new virtual parameters to optimise
                state_name=c("S","R"), 
                scaling_var_name=c("x1","x3"),
                min_p_val=c(0.0,0.0), 
                max_p_val=c(1.0,1.0), 
                value=c(0.9,0.9), 
                selector_type='each subarea')
>>> init_parameteriser = p_states.make_state_init_parameteriser()
```

### num_free_parameters

```
num_free_parameters() -> int
```

Number of free parameters in this hypercube parameteriser

Returns:

- **`int`** ( `int` ) – Number of free parameters

### score_for_objective

```
score_for_objective(objective: ObjectiveEvaluator) -> Dict[str, Any]
```

Computes the value of an objective for this given set of parameters

### set_hypercube

```
set_hypercube(specs: DataFrame)
```

Set the properties of a hypercube parameteriser. An exception will ve raised if any parameter name is unknown.

Parameters:

- **`specs`** (`DataFrame`) – An optional data frame description of the parameter set, with at least columns Name, Min, Max, Value.

Examples:

```
>>> # e.g. if `p` is a typical parameteriser for GR4J with 
>>> # set x4 bounds to be in "days", not hours
>>> p_x4 = pd.DataFrame.from_dict({
    "Name": ["x4"],
    "Value": [1.0],
    "Min": [0.25],
    "Max": [10.0],
})
>>> p.set_hypercube(p_x4)
```

### set_max_parameter_value

```
set_max_parameter_value(variable_name: VecStr, value: VecScalars)
```

Sets the value(s) of the upper bound of one or more parameter(s)

Parameters:

- **`variable_name`** (`VecStr`) – one or more parameter name(s)
- **`value`** (`VecScalars`) – one or more parameter value(s)

### set_min_parameter_value

```
set_min_parameter_value(variable_name: VecStr, value: VecScalars)
```

Sets the value(s) of the lower bound of one or more parameter(s)

Parameters:

- **`variable_name`** (`VecStr`) – one or more parameter name(s)
- **`value`** (`VecScalars`) – one or more parameter value(s)

### set_parameter_definition

```
set_parameter_definition(variable_name: str, min: float, max: float, value: float)
```

Sets the feasible range and value for a parameter

Parameters:

- **`variable_name`** (`str`) – parameter name
- **`min`** (`float`) – min
- **`max`** (`float`) – max
- **`value`** (`float`) – value

### set_parameter_value

```
set_parameter_value(variable_name: VecStr, value: VecScalars)
```

Sets the value(s) of one or more parameter(s)

Parameters:

- **`variable_name`** (`VecStr`) – one or more parameter name(s)
- **`value`** (`VecScalars`) – one or more parameter value(s)

### subcatchment_parameteriser

```
subcatchment_parameteriser(subcatchment)
```

Create a parameteriser that gets applied to a subset of a whole catchment

Parameters:

- **`subcatchment`** (`Simulation`) – the subcatchment, subset of a whole catchment, identifying which elements (subareas, nodes, links) will be parameterised by the new parameteriser. Other catchment elements are untouched.

Returns:

- **`HypercubeParameteriser`** – New parameteriser whose application is limited to the subcatchment.

Examples:

```
>>> sub_cats = simulation.split_to_subcatchments(["node.node_7", "node.node_10"])
>>> sc = sub_cats["node.node_7"]
>>> p = sp.create_parameteriser('generic subarea')
>>> p.add_parameter_to_hypercube("x1", 32, 1, 6e3)
>>> sp = p.subcatchment_parameteriser(sc)
>>> sp.apply_sys_config(simulation)
```

### supports_thread_safe_cloning

```
supports_thread_safe_cloning() -> bool
```

Is this parameteriser clonable as a deep copy, safe for multi-threading?

### wrap_transform

```
wrap_transform() -> TransformParameteriser
```

Create a parameteriser for which parameter transformations can be defined.

This allows to define e.g. a virtual parameter log_X instead of calibrating on the parameter X.

Returns:

- **`TransformParameteriser`** ( `TransformParameteriser` ) – A new parameteriser (TransformParameteriser) which has methods to define parameter transforms

## HypercubeParameteriser

```
HypercubeParameteriser(handle: CffiData, release_native: Callable[[CffiData], None], type_id: Optional[str] = None, prior_ref_count: int = 0)
```

Bases: `Parameteriser`

Methods:

- **`add_parameter_to_hypercube`** – Add a parameter to a hypercube. Must be a type of object that is expandable, otherwise may raise an exception
- **`add_to_hypercube`** – Add entries to a hypercube. Must be a type of object that is expandable, otherwise may raise an exception.
- **`apply_sys_config`** – Apply a model configuration to a simulation
- **`as_dataframe`** – Convert this hypercube parameteriser to a pandas data frame representation
- **`backtransform`** – Get the parameteriser values in the untransformed space
- **`clone`** –
- **`create_parameter_sampler`** – Creates a sampler for this parameteriser
- **`filtered_parameters`** – Wrap this parameteriser in a filter that can hide some parameters from an optimiser.
- **`from_dataframe`** – Create a parameteriser
- **`make_state_init_parameteriser`** – Create a parameteriser used for model state initialisation
- **`num_free_parameters`** – Number of free parameters in this hypercube parameteriser
- **`score_for_objective`** – Computes the value of an objective for this given set of parameters
- **`set_hypercube`** – Set the properties of a hypercube parameteriser. An exception will ve raised if any parameter name is unknown.
- **`set_max_parameter_value`** – Sets the value(s) of the upper bound of one or more parameter(s)
- **`set_min_parameter_value`** – Sets the value(s) of the lower bound of one or more parameter(s)
- **`set_parameter_definition`** – Sets the feasible range and value for a parameter
- **`set_parameter_value`** – Sets the value(s) of one or more parameter(s)
- **`subcatchment_parameteriser`** – Create a parameteriser that gets applied to a subset of a whole catchment
- **`supports_thread_safe_cloning`** – Is this parameteriser clonable as a deep copy, safe for multi-threading?
- **`wrap_transform`** – Create a parameteriser for which parameter transformations can be defined.

### add_parameter_to_hypercube

```
add_parameter_to_hypercube(name: str, value: float, min: float, max: float)
```

Add a parameter to a hypercube. Must be a type of object that is expandable, otherwise may raise an exception

### add_to_hypercube

```
add_to_hypercube(specs: DataFrame)
```

Add entries to a hypercube. Must be a type of object that is expandable, otherwise may raise an exception.

Parameters:

- **`specs`** (`DataFrame`) – An optional data frame description of the parameter set, with at least columns Name, Min, Max, Value.

> > > from swift2.parameteriser import create_parameteriser loglik = create_parameteriser(type='no apply') loglik.add_to_hypercube( pd.DataFrame({ "Name": c('b','m','s','a','maxobs','ct', 'censopt'), "Min": c(-30, 0, -10, -20, maxobs, censor_threshold, censopt), "Max": c(5, 0, 10, 0, maxobs, censor_threshold, censopt), "Value": c(-7, 0, 0, -10, maxobs, censor_threshold, censopt), } ) )

### apply_sys_config

```
apply_sys_config(simulation: Simulation)
```

Apply a model configuration to a simulation

Parameters:

- **`simulation`** (`Simulation`) – simulation

### as_dataframe

```
as_dataframe() -> DataFrame
```

Convert this hypercube parameteriser to a pandas data frame representation

Returns:

- `DataFrame` – pd.DataFrame: pandas data frame

### backtransform

```
backtransform() -> HypercubeParameteriser
```

Get the parameteriser values in the untransformed space

Get the parameteriser values in the untransformed space, i.e. remove any transform added via HypercubeParameteriser.wrap_transform. This allows to transform back e.g. from a virtual parameter log_X to the underlying model (or even virtual/meta) parameter X.

Returns:

- **`HypercubeParameteriser`** ( `HypercubeParameteriser` ) – The parameters definitions without the transforms (if there are any)

Examples:

```
>>> ref_area = 250
>>> time_span = 3600
>>> ptrans = sdh.define_gr4j_scaled_parameter(ref_area, time_span)
>>> ptrans
    Name     Value       Min       Max
0    log_x4  0.305422  0.000000  2.380211
1    log_x1  0.506690  0.000000  3.778151
2    log_x3  0.315425  0.000000  3.000000
3  asinh_x2  2.637752 -3.989327  3.989327
>>> ptrans.backtransform()
Name    Value   Min     Max
0   x2  6.95511 -27.0    27.0
1   x3  2.06740   1.0  1000.0
2   x4  2.02033   1.0   240.0
3   x1  3.21137   1.0  6000.0
>>>
```

### clone

```
clone() -> HypercubeParameteriser
```

### create_parameter_sampler

```
create_parameter_sampler(seed: int = 0, type: str = 'urs') -> CandidateFactorySeed
```

Creates a sampler for this parameteriser

Parameters:

- **`seed`** (`int`, default: `0` ) – a seed for the sampler. Defaults to 0.
- **`type`** (`str`, default: `'urs'` ) – the type of sampler. Defaults to "urs" for Uniform Random Sampling. This is the only option supported as of 2023-01.

Returns:

- **`CandidateFactorySeed`** ( `CandidateFactorySeed` ) – a sampler, aka candidate factory

### filtered_parameters

```
filtered_parameters() -> FilteringParameteriser
```

Wrap this parameteriser in a filter that can hide some parameters from an optimiser.

Used for instance in calibration with log-likelihood contexts.

Returns:

- `FilteringParameteriser` – an parameteriser designed to only show a subset to an optimiser, while applying more to a simulation.

### from_dataframe

```
from_dataframe(type='Generic subareas', definition: Optional[DataFrame] = None) -> HypercubeParameteriser
```

Create a parameteriser

Parameters:

- **`type`** (`str`, default: `'Generic subareas'` ) – A string identifying the type of parameteriser to use. Recognised types are (case insensitive) 'log-likelihood', 'generic', 'subareas', 'links', 'nodes' and 'muskingum'. Defaults to "Generic subareas".
- **`specs`** (`DataFrame`) – An optional data frame description of the parameter set, with at least columns Name, Min, Max, Value. Defaults to None.

Returns:

- **`HypercubeParameteriser`** ( `HypercubeParameteriser` ) – new parameteriser

Examples:

```
>>> d = pd.DataFrame(
...     dict(
...         Name=c("alpha", "inverse_velocity"),
...         Value=c(1, 1),
...         Min=c(1e-3, 1e-3),
...         Max=c(1e2, 1e2),
...     )
... )
>>> p = HypercubeParameteriser.from_dataframe("Generic links", d)
>>> p
```

### make_state_init_parameteriser

```
make_state_init_parameteriser() -> StateInitParameteriser
```

Create a parameteriser used for model state initialisation

This allows to define tied parameters where, for instance, pval = a * modelStateVal. A more concrete use case is to define an initial soil moisture store 'S0', as a fraction of the model store capacity 'Smax'. The model state to initialise is 'S'

Note

See also swift2.classes.ScalingParameteriser for typical joint usage.

Returns:

- **`StateInitParameteriser`** ( `StateInitParameteriser` ) – state initialisation parameteriser

Examples:

```
>>> # Use case: Set gr4j initial stores at simulation as a function of x1/x3 parameters.
>>> import swift2.parameteriser as sp
>>> # Let's define _S0_ and _R0_ parameters such that for each GR4J model instance, _S = S0 * x1_ and _R = R0 * x3_
>>> p_states = sp.linear_parameteriser(
                param_name=c("S0","R0"), # new virtual parameters to optimise
                state_name=c("S","R"), 
                scaling_var_name=c("x1","x3"),
                min_p_val=c(0.0,0.0), 
                max_p_val=c(1.0,1.0), 
                value=c(0.9,0.9), 
                selector_type='each subarea')
>>> init_parameteriser = p_states.make_state_init_parameteriser()
```

### num_free_parameters

```
num_free_parameters() -> int
```

Number of free parameters in this hypercube parameteriser

Returns:

- **`int`** ( `int` ) – Number of free parameters

### score_for_objective

```
score_for_objective(objective: ObjectiveEvaluator) -> Dict[str, Any]
```

Computes the value of an objective for this given set of parameters

### set_hypercube

```
set_hypercube(specs: DataFrame)
```

Set the properties of a hypercube parameteriser. An exception will ve raised if any parameter name is unknown.

Parameters:

- **`specs`** (`DataFrame`) – An optional data frame description of the parameter set, with at least columns Name, Min, Max, Value.

Examples:

```
>>> # e.g. if `p` is a typical parameteriser for GR4J with 
>>> # set x4 bounds to be in "days", not hours
>>> p_x4 = pd.DataFrame.from_dict({
    "Name": ["x4"],
    "Value": [1.0],
    "Min": [0.25],
    "Max": [10.0],
})
>>> p.set_hypercube(p_x4)
```

### set_max_parameter_value

```
set_max_parameter_value(variable_name: VecStr, value: VecScalars)
```

Sets the value(s) of the upper bound of one or more parameter(s)

Parameters:

- **`variable_name`** (`VecStr`) – one or more parameter name(s)
- **`value`** (`VecScalars`) – one or more parameter value(s)

### set_min_parameter_value

```
set_min_parameter_value(variable_name: VecStr, value: VecScalars)
```

Sets the value(s) of the lower bound of one or more parameter(s)

Parameters:

- **`variable_name`** (`VecStr`) – one or more parameter name(s)
- **`value`** (`VecScalars`) – one or more parameter value(s)

### set_parameter_definition

```
set_parameter_definition(variable_name: str, min: float, max: float, value: float)
```

Sets the feasible range and value for a parameter

Parameters:

- **`variable_name`** (`str`) – parameter name
- **`min`** (`float`) – min
- **`max`** (`float`) – max
- **`value`** (`float`) – value

### set_parameter_value

```
set_parameter_value(variable_name: VecStr, value: VecScalars)
```

Sets the value(s) of one or more parameter(s)

Parameters:

- **`variable_name`** (`VecStr`) – one or more parameter name(s)
- **`value`** (`VecScalars`) – one or more parameter value(s)

### subcatchment_parameteriser

```
subcatchment_parameteriser(subcatchment)
```

Create a parameteriser that gets applied to a subset of a whole catchment

Parameters:

- **`subcatchment`** (`Simulation`) – the subcatchment, subset of a whole catchment, identifying which elements (subareas, nodes, links) will be parameterised by the new parameteriser. Other catchment elements are untouched.

Returns:

- **`HypercubeParameteriser`** – New parameteriser whose application is limited to the subcatchment.

Examples:

```
>>> sub_cats = simulation.split_to_subcatchments(["node.node_7", "node.node_10"])
>>> sc = sub_cats["node.node_7"]
>>> p = sp.create_parameteriser('generic subarea')
>>> p.add_parameter_to_hypercube("x1", 32, 1, 6e3)
>>> sp = p.subcatchment_parameteriser(sc)
>>> sp.apply_sys_config(simulation)
```

### supports_thread_safe_cloning

```
supports_thread_safe_cloning() -> bool
```

Is this parameteriser clonable as a deep copy, safe for multi-threading?

### wrap_transform

```
wrap_transform() -> TransformParameteriser
```

Create a parameteriser for which parameter transformations can be defined.

This allows to define e.g. a virtual parameter log_X instead of calibrating on the parameter X.

Returns:

- **`TransformParameteriser`** ( `TransformParameteriser` ) – A new parameteriser (TransformParameteriser) which has methods to define parameter transforms

## MaerrisStagedCalibration

```
MaerrisStagedCalibration(handle: CffiData, release_native: Callable[[CffiData], None], type_id: Optional[str] = None, prior_ref_count: int = 0)
```

Bases: `DeletableCffiNativeHandle`

Methods:

- **`extract_optimisation_log`** –

### extract_optimisation_log

```
extract_optimisation_log(fitness_name='log.likelihood')
```

## MemoryStates

```
MemoryStates(handle: CffiData, release_native: Callable[[CffiData], None], type_id: Optional[str] = None, prior_ref_count: int = 0)
```

Bases: `DeletableCffiNativeHandle`

## ObjectiveEvaluator

```
ObjectiveEvaluator(handle: CffiData, release_native: Callable[[CffiData], None], type_id: Optional[str] = None, prior_ref_count: int = 0)
```

Bases: `DeletableCffiNativeHandle`

Objective Evaluator

Methods:

- **`create_composite_objective`** – Creates a composite objective, weighted average of several objectives
- **`create_sce_optim_swift`** – Creates a shuffled complex optimiser for this objective
- **`get_score`** – Evaluate this objective for a given parameterisation
- **`get_scores`** – Evaluate this objective for a given parameterisation

### create_composite_objective

```
create_composite_objective(objectives: Sequence[ObjectiveEvaluator], weights: Sequence[float], names: Sequence[str]) -> ObjectiveEvaluator
```

Creates a composite objective, weighted average of several objectives

Parameters:

- **`objectives`** (`Sequence[&quot;ObjectiveEvaluator&quot;]`) – objective evaluators, for instance measures at several points in the catchment
- **`weights`** (`Sequence[float]`) – Weights to use to average the objectives. This may not add to one, but must not sum to zero
- **`names`** (`Sequence[str]`) – Names of individual objectives

Returns:

- **`ObjectiveEvaluator`** ( `ObjectiveEvaluator` ) – An objective evaluator that can be use by an optimiser

### create_sce_optim_swift

```
create_sce_optim_swift(termination_criterion: Optional[SceTerminationCondition] = None, sce_params: Optional[Dict[str, float]] = None, population_initialiser: Optional[Union[CandidateFactorySeed, HypercubeParameteriser]] = None) -> Optimiser
```

Creates a shuffled complex optimiser for this objective

Parameters:

- **`termination_criterion`** (`Optional[&quot;SceTerminationCondition&quot;]`, default: `None` ) – A termination criterion for the optimiser. Defaults to None, in which case an arbitrary "relative standard deviation" is set up.
- **`sce_params`** (`Optional[Dict[str, float]]`, default: `None` ) – hyperparameters controlling SCE. Defaults to None, in which case swift2.parameteriser.get_default_sce_parameters is used.
- **`population_initialiser`** (`Optional[&quot;CandidateFactorySeed&quot;]`, default: `None` ) – A candidate factory to initialise the population of parameters the optimiser starts from, or a hypercube. In the latter case, uniform random sampling is used. Defaults to None, which leads to an error (for legacy reasons).

Returns:

- **`Optimiser`** ( `Optimiser` ) – SCE optimiser

### get_score

```
get_score(p_set: HypercubeParameteriser) -> Dict[str, Any]
```

Evaluate this objective for a given parameterisation

Parameters:

- **`p_set`** (`HypercubeParameteriser`) – parameteriser

Returns:

- `Dict[str, Any]` – Dict\[str,Any\]: score(s), and a data frame representation of the input parameters.

### get_scores

```
get_scores(p_set: HypercubeParameteriser) -> Dict[str, float]
```

Evaluate this objective for a given parameterisation

Parameters:

- **`p_set`** (`HypercubeParameteriser`) – parameteriser

Returns:

- `Dict[str, float]` – Dict\[str,float\]: score(s)

## ObjectiveScores

```
ObjectiveScores(handle: CffiData, release_native: Callable[[CffiData], None], type_id: Optional[str] = None, prior_ref_count: int = 0)
```

Bases: `DeletableCffiNativeHandle`

Methods:

- **`apply_sys_config`** – Apply the model configuration (parameteriser) associated with this object to a simulation
- **`as_py_structure`** –

Attributes:

- **`num_scores`** (`int`) –
- **`parameteriser`** (`HypercubeParameteriser`) – The parameteriser associated with this object
- **`scores`** (`Dict[str, float]`) –

### num_scores

```
num_scores: int
```

### parameteriser

```
parameteriser: HypercubeParameteriser
```

The parameteriser associated with this object

### scores

```
scores: Dict[str, float]
```

### apply_sys_config

```
apply_sys_config(simulation: Simulation) -> None
```

Apply the model configuration (parameteriser) associated with this object to a simulation

Parameters:

- **`simulation`** (`Simulation`) – simulation

### as_py_structure

```
as_py_structure()
```

## Optimiser

```
Optimiser(handle: CffiData, release_native: Callable[[CffiData], None], type_id: Optional[str] = None, prior_ref_count: int = 0)
```

Bases: `DeletableCffiNativeHandle`

Methods:

- **`execute_optimisation`** –
- **`extract_optimisation_log`** – Extract the logger from a parameter extimator (optimiser or related)
- **`get_default_maximum_threads`** –
- **`set_calibration_logger`** – Set the type of calibration logger to use
- **`set_default_maximum_threads`** –
- **`set_maximum_threads`** – Set the maximum number of threads (compute cores) to use in the optimisation, if possible. -1 means "as many as available".
- **`set_maximum_threads_free_cores`** – Set the maximum number of threads (compute cores) to use in the optimisation, such that at least n_free_cores are left for other tasks, if feasible given hardware constraints.

### execute_optimisation

```
execute_optimisation()
```

### extract_optimisation_log

```
extract_optimisation_log(fitness_name: str = 'log.likelihood') -> MhData
```

Extract the logger from a parameter extimator (optimiser or related)

Parameters:

- **`fitness_name`** (`str`, default: `'log.likelihood'` ) – name of the fitness function to extract. Defaults to "log.likelihood".

Returns:

- **`MhData`** ( `MhData` ) – an object with methods to analyse the optimisation log

### get_default_maximum_threads

```
get_default_maximum_threads() -> int
```

### set_calibration_logger

```
set_calibration_logger(type: str = '') -> None
```

Set the type of calibration logger to use

Parameters:

- **`type`** (`str`, default: `''` ) – The type of logger. Unused for now, future option e.g. 'text', 'database'. Defaults to "".

### set_default_maximum_threads

```
set_default_maximum_threads(n_threads: int)
```

### set_maximum_threads

```
set_maximum_threads(n_threads: int = -1)
```

Set the maximum number of threads (compute cores) to use in the optimisation, if possible. -1 means "as many as available".

### set_maximum_threads_free_cores

```
set_maximum_threads_free_cores(n_free_cores: int = 1)
```

Set the maximum number of threads (compute cores) to use in the optimisation, such that at least `n_free_cores` are left for other tasks, if feasible given hardware constraints.

## Parameteriser

```
Parameteriser(handle: CffiData, release_native: Callable[[CffiData], None], type_id: Optional[str] = None, prior_ref_count: int = 0)
```

Bases: `DeletableCffiNativeHandle`

Wrapper around a native parameteriser.

Note

This is a parent class for more common types such as swift2.classes.HypercubeParameteriser

Methods:

- **`apply_sys_config`** – Apply a model configuration to a simulation
- **`score_for_objective`** – Computes the value of an objective for this given set of parameters
- **`subcatchment_parameteriser`** – Create a parameteriser that gets applied to a subset of a whole catchment
- **`supports_thread_safe_cloning`** – Is this parameteriser clonable as a deep copy, safe for multi-threading?

### apply_sys_config

```
apply_sys_config(simulation: Simulation)
```

Apply a model configuration to a simulation

Parameters:

- **`simulation`** (`Simulation`) – simulation

### score_for_objective

```
score_for_objective(objective: ObjectiveEvaluator) -> Dict[str, Any]
```

Computes the value of an objective for this given set of parameters

### subcatchment_parameteriser

```
subcatchment_parameteriser(subcatchment)
```

Create a parameteriser that gets applied to a subset of a whole catchment

Parameters:

- **`subcatchment`** (`Simulation`) – the subcatchment, subset of a whole catchment, identifying which elements (subareas, nodes, links) will be parameterised by the new parameteriser. Other catchment elements are untouched.

Returns:

- **`HypercubeParameteriser`** – New parameteriser whose application is limited to the subcatchment.

Examples:

```
>>> sub_cats = simulation.split_to_subcatchments(["node.node_7", "node.node_10"])
>>> sc = sub_cats["node.node_7"]
>>> p = sp.create_parameteriser('generic subarea')
>>> p.add_parameter_to_hypercube("x1", 32, 1, 6e3)
>>> sp = p.subcatchment_parameteriser(sc)
>>> sp.apply_sys_config(simulation)
```

### supports_thread_safe_cloning

```
supports_thread_safe_cloning() -> bool
```

Is this parameteriser clonable as a deep copy, safe for multi-threading?

## ScalingParameteriser

```
ScalingParameteriser(handle: CffiData, release_native: Callable[[CffiData], None], type_id: Optional[str] = None, prior_ref_count: int = 0)
```

Bases: `TransformParameteriser`

Methods:

- **`add_linear_scaled_parameter`** –
- **`add_parameter_to_hypercube`** – Add a parameter to a hypercube. Must be a type of object that is expandable, otherwise may raise an exception
- **`add_to_hypercube`** – Add entries to a hypercube. Must be a type of object that is expandable, otherwise may raise an exception.
- **`add_transform`** – Create a parameteriser for which parameter transformations can be defined
- **`apply_sys_config`** – Apply a model configuration to a simulation
- **`as_dataframe`** – Convert this hypercube parameteriser to a pandas data frame representation
- **`backtransform`** – Get the parameteriser values in the untransformed space
- **`clone`** –
- **`create_parameter_sampler`** – Creates a sampler for this parameteriser
- **`filtered_parameters`** – Wrap this parameteriser in a filter that can hide some parameters from an optimiser.
- **`from_dataframe`** – Create a parameteriser
- **`linear_parameteriser`** – Create a scaled linear parameteriser, tying by a linear transformation a (resp several) model state to a (resp several) parameter values
- **`linear_parameteriser_from`** – Create a scaled linear parameteriser, tying by a linear transformation a (resp several) model state to a (resp several) parameter values
- **`make_state_init_parameteriser`** – Create a parameteriser used for model state initialisation
- **`num_free_parameters`** – Number of free parameters in this hypercube parameteriser
- **`score_for_objective`** – Computes the value of an objective for this given set of parameters
- **`set_hypercube`** – Set the properties of a hypercube parameteriser. An exception will ve raised if any parameter name is unknown.
- **`set_max_parameter_value`** – Sets the value(s) of the upper bound of one or more parameter(s)
- **`set_min_parameter_value`** – Sets the value(s) of the lower bound of one or more parameter(s)
- **`set_parameter_definition`** – Sets the feasible range and value for a parameter
- **`set_parameter_value`** – Sets the value(s) of one or more parameter(s)
- **`subcatchment_parameteriser`** – Create a parameteriser that gets applied to a subset of a whole catchment
- **`supports_thread_safe_cloning`** – Is this parameteriser clonable as a deep copy, safe for multi-threading?
- **`wrap_transform`** – Create a parameteriser for which parameter transformations can be defined.

### add_linear_scaled_parameter

```
add_linear_scaled_parameter(param_name: str, state_name: str, scaling_var_name: str, min_p_val: float, max_p_val: float, value: float, intercept: float = 0.0)
```

### add_parameter_to_hypercube

```
add_parameter_to_hypercube(name: str, value: float, min: float, max: float)
```

Add a parameter to a hypercube. Must be a type of object that is expandable, otherwise may raise an exception

### add_to_hypercube

```
add_to_hypercube(specs: DataFrame)
```

Add entries to a hypercube. Must be a type of object that is expandable, otherwise may raise an exception.

Parameters:

- **`specs`** (`DataFrame`) – An optional data frame description of the parameter set, with at least columns Name, Min, Max, Value.

> > > from swift2.parameteriser import create_parameteriser loglik = create_parameteriser(type='no apply') loglik.add_to_hypercube( pd.DataFrame({ "Name": c('b','m','s','a','maxobs','ct', 'censopt'), "Min": c(-30, 0, -10, -20, maxobs, censor_threshold, censopt), "Max": c(5, 0, 10, 0, maxobs, censor_threshold, censopt), "Value": c(-7, 0, 0, -10, maxobs, censor_threshold, censopt), } ) )

### add_transform

```
add_transform(param_name: str, inner_param_name: str, transform_id: str, a: float = 1.0, b: float = 0.0)
```

Create a parameteriser for which parameter transformations can be defined

```
This allows to define e.g. a virtual parameter log_X instead of calibrating on the parameter X.
```

Parameters:

- **`param_name`** (`str`) – the name of the meta-parameter. Note that it can be the same value as inner_param_name, but this is NOT recommended.
- **`inner_param_name`** (`str`) – the name of the parameter being transformed
- **`transform_id`** (`str`) – identifier for a known bijective univariate function
- **`a`** (`float`, default: `1.0` ) – parameter in Y = F(ax+b). Defaults to 1.0.
- **`b`** (`float`, default: `0.0` ) – parameter in Y = F(ax+b). Defaults to 0.0.

Examples:

```
>>> from swift2.doc_helper import get_free_params
>>> pspec_gr4j = get_free_params('GR4J')
>>> p = HypercubeParameteriser.from_dataframe("generic subarea", pspec_gr4j)
>>> p
Name       Value   Min     Max
0   x1  650.488000   1.0  3000.0
1   x2   -0.280648 -27.0    27.0
2   x3    7.891230   1.0   660.0
3   x4   18.917200   1.0   240.0
>>> p = p.wrap_transform()
>>> p.add_transform("log_x4", "x4", "log10")
>>> p
    Name       Value   Min          Max
0  log_x4    1.276857   0.0     2.380211
1      x1  650.488000   1.0  3000.000000
2      x2   -0.280648 -27.0    27.000000
3      x3    7.891230   1.0   660.000000
>>> p.backtransform()
Name       Value   Min     Max
0   x1  650.488000   1.0  3000.0
1   x2   -0.280648 -27.0    27.0
2   x3    7.891230   1.0   660.0
3   x4   18.917200   1.0   240.0
>>>
```

### apply_sys_config

```
apply_sys_config(simulation: Simulation)
```

Apply a model configuration to a simulation

Parameters:

- **`simulation`** (`Simulation`) – simulation

### as_dataframe

```
as_dataframe() -> DataFrame
```

Convert this hypercube parameteriser to a pandas data frame representation

Returns:

- `DataFrame` – pd.DataFrame: pandas data frame

### backtransform

```
backtransform() -> HypercubeParameteriser
```

Get the parameteriser values in the untransformed space

Get the parameteriser values in the untransformed space, i.e. remove any transform added via HypercubeParameteriser.wrap_transform. This allows to transform back e.g. from a virtual parameter log_X to the underlying model (or even virtual/meta) parameter X.

Returns:

- **`HypercubeParameteriser`** ( `HypercubeParameteriser` ) – The parameters definitions without the transforms (if there are any)

Examples:

```
>>> ref_area = 250
>>> time_span = 3600
>>> ptrans = sdh.define_gr4j_scaled_parameter(ref_area, time_span)
>>> ptrans
    Name     Value       Min       Max
0    log_x4  0.305422  0.000000  2.380211
1    log_x1  0.506690  0.000000  3.778151
2    log_x3  0.315425  0.000000  3.000000
3  asinh_x2  2.637752 -3.989327  3.989327
>>> ptrans.backtransform()
Name    Value   Min     Max
0   x2  6.95511 -27.0    27.0
1   x3  2.06740   1.0  1000.0
2   x4  2.02033   1.0   240.0
3   x1  3.21137   1.0  6000.0
>>>
```

### clone

```
clone() -> HypercubeParameteriser
```

### create_parameter_sampler

```
create_parameter_sampler(seed: int = 0, type: str = 'urs') -> CandidateFactorySeed
```

Creates a sampler for this parameteriser

Parameters:

- **`seed`** (`int`, default: `0` ) – a seed for the sampler. Defaults to 0.
- **`type`** (`str`, default: `'urs'` ) – the type of sampler. Defaults to "urs" for Uniform Random Sampling. This is the only option supported as of 2023-01.

Returns:

- **`CandidateFactorySeed`** ( `CandidateFactorySeed` ) – a sampler, aka candidate factory

### filtered_parameters

```
filtered_parameters() -> FilteringParameteriser
```

Wrap this parameteriser in a filter that can hide some parameters from an optimiser.

Used for instance in calibration with log-likelihood contexts.

Returns:

- `FilteringParameteriser` – an parameteriser designed to only show a subset to an optimiser, while applying more to a simulation.

### from_dataframe

```
from_dataframe(type='Generic subareas', definition: Optional[DataFrame] = None) -> HypercubeParameteriser
```

Create a parameteriser

Parameters:

- **`type`** (`str`, default: `'Generic subareas'` ) – A string identifying the type of parameteriser to use. Recognised types are (case insensitive) 'log-likelihood', 'generic', 'subareas', 'links', 'nodes' and 'muskingum'. Defaults to "Generic subareas".
- **`specs`** (`DataFrame`) – An optional data frame description of the parameter set, with at least columns Name, Min, Max, Value. Defaults to None.

Returns:

- **`HypercubeParameteriser`** ( `HypercubeParameteriser` ) – new parameteriser

Examples:

```
>>> d = pd.DataFrame(
...     dict(
...         Name=c("alpha", "inverse_velocity"),
...         Value=c(1, 1),
...         Min=c(1e-3, 1e-3),
...         Max=c(1e2, 1e2),
...     )
... )
>>> p = HypercubeParameteriser.from_dataframe("Generic links", d)
>>> p
```

### linear_parameteriser

```
linear_parameteriser(param_name: VecStr, state_name: VecStr, scaling_var_name: VecStr, min_p_val: VecNum, max_p_val: VecNum, value: VecNum, selector_type: str = 'subareas', intercept: VecNum = 0.0)
```

Create a scaled linear parameteriser, tying by a linear transformation a (resp several) model state to a (resp several) parameter values

This allows to define tied parameters where pval = a * modelStateVal + intercept. The intent in particular is to define virtual model parameters such as initial store value as a fraction of the maximum storage capacity.

Args:

```
param_name (VecStr): the name of the meta-parameter. Note that it can be the same value as inner_param_name without interference, though this may be confusing a choice.
state_name (VecStr): the name of the model state to modify, based on the value of the meta-parameter and the state found in 'scalingVarName'
scaling_var_name (VecStr): the name of the parameter for each subarea model, to which to apply the area scaled value.
min_p_val (VecNum): minimum value allowed for the meta-parameter
max_p_val (VecNum): minimum value allowed for the meta-parameter
value (VecNum): value for the meta parameter.
selector_type (str, optional): an identifier to define to which catchment element(s) the parameteriser will be applied. Defaults to "subareas".
intercept (VecNum, optional): [description]. Defaults to 0.0.
```

Returns:

- **`ScalingParameteriser`** – new ScalingParameteriser

### linear_parameteriser_from

```
linear_parameteriser_from(data_frame: DataFrame, selector_type: str = 'subareas')
```

Create a scaled linear parameteriser, tying by a linear transformation a (resp several) model state to a (resp several) parameter values This allows to define tied parameters where pval = a * modelStateVal + intercept. The intent in particular is to define virtual model parameters such as initial store value as a fraction of the maximum storage capacity.

Parameters:

- **`data_frame`** (`DataFrame`) – data frame with columns "param_name", "state_name", "scaling_var_name", "min_value", "max_value", "value", "intercept",
- **`selector_type`** (`str`, default: `'subareas'` ) – [description]. Defaults to "subareas".

Returns:

- **`ScalingParameteriser`** – ScalingParameteriser

### make_state_init_parameteriser

```
make_state_init_parameteriser() -> StateInitParameteriser
```

Create a parameteriser used for model state initialisation

This allows to define tied parameters where, for instance, pval = a * modelStateVal. A more concrete use case is to define an initial soil moisture store 'S0', as a fraction of the model store capacity 'Smax'. The model state to initialise is 'S'

Note

See also swift2.classes.ScalingParameteriser for typical joint usage.

Returns:

- **`StateInitParameteriser`** ( `StateInitParameteriser` ) – state initialisation parameteriser

Examples:

```
>>> # Use case: Set gr4j initial stores at simulation as a function of x1/x3 parameters.
>>> import swift2.parameteriser as sp
>>> # Let's define _S0_ and _R0_ parameters such that for each GR4J model instance, _S = S0 * x1_ and _R = R0 * x3_
>>> p_states = sp.linear_parameteriser(
                param_name=c("S0","R0"), # new virtual parameters to optimise
                state_name=c("S","R"), 
                scaling_var_name=c("x1","x3"),
                min_p_val=c(0.0,0.0), 
                max_p_val=c(1.0,1.0), 
                value=c(0.9,0.9), 
                selector_type='each subarea')
>>> init_parameteriser = p_states.make_state_init_parameteriser()
```

### num_free_parameters

```
num_free_parameters() -> int
```

Number of free parameters in this hypercube parameteriser

Returns:

- **`int`** ( `int` ) – Number of free parameters

### score_for_objective

```
score_for_objective(objective: ObjectiveEvaluator) -> Dict[str, Any]
```

Computes the value of an objective for this given set of parameters

### set_hypercube

```
set_hypercube(specs: DataFrame)
```

Set the properties of a hypercube parameteriser. An exception will ve raised if any parameter name is unknown.

Parameters:

- **`specs`** (`DataFrame`) – An optional data frame description of the parameter set, with at least columns Name, Min, Max, Value.

Examples:

```
>>> # e.g. if `p` is a typical parameteriser for GR4J with 
>>> # set x4 bounds to be in "days", not hours
>>> p_x4 = pd.DataFrame.from_dict({
    "Name": ["x4"],
    "Value": [1.0],
    "Min": [0.25],
    "Max": [10.0],
})
>>> p.set_hypercube(p_x4)
```

### set_max_parameter_value

```
set_max_parameter_value(variable_name: VecStr, value: VecScalars)
```

Sets the value(s) of the upper bound of one or more parameter(s)

Parameters:

- **`variable_name`** (`VecStr`) – one or more parameter name(s)
- **`value`** (`VecScalars`) – one or more parameter value(s)

### set_min_parameter_value

```
set_min_parameter_value(variable_name: VecStr, value: VecScalars)
```

Sets the value(s) of the lower bound of one or more parameter(s)

Parameters:

- **`variable_name`** (`VecStr`) – one or more parameter name(s)
- **`value`** (`VecScalars`) – one or more parameter value(s)

### set_parameter_definition

```
set_parameter_definition(variable_name: str, min: float, max: float, value: float)
```

Sets the feasible range and value for a parameter

Parameters:

- **`variable_name`** (`str`) – parameter name
- **`min`** (`float`) – min
- **`max`** (`float`) – max
- **`value`** (`float`) – value

### set_parameter_value

```
set_parameter_value(variable_name: VecStr, value: VecScalars)
```

Sets the value(s) of one or more parameter(s)

Parameters:

- **`variable_name`** (`VecStr`) – one or more parameter name(s)
- **`value`** (`VecScalars`) – one or more parameter value(s)

### subcatchment_parameteriser

```
subcatchment_parameteriser(subcatchment)
```

Create a parameteriser that gets applied to a subset of a whole catchment

Parameters:

- **`subcatchment`** (`Simulation`) – the subcatchment, subset of a whole catchment, identifying which elements (subareas, nodes, links) will be parameterised by the new parameteriser. Other catchment elements are untouched.

Returns:

- **`HypercubeParameteriser`** – New parameteriser whose application is limited to the subcatchment.

Examples:

```
>>> sub_cats = simulation.split_to_subcatchments(["node.node_7", "node.node_10"])
>>> sc = sub_cats["node.node_7"]
>>> p = sp.create_parameteriser('generic subarea')
>>> p.add_parameter_to_hypercube("x1", 32, 1, 6e3)
>>> sp = p.subcatchment_parameteriser(sc)
>>> sp.apply_sys_config(simulation)
```

### supports_thread_safe_cloning

```
supports_thread_safe_cloning() -> bool
```

Is this parameteriser clonable as a deep copy, safe for multi-threading?

### wrap_transform

```
wrap_transform() -> TransformParameteriser
```

Create a parameteriser for which parameter transformations can be defined.

This allows to define e.g. a virtual parameter log_X instead of calibrating on the parameter X.

Returns:

- **`TransformParameteriser`** ( `TransformParameteriser` ) – A new parameteriser (TransformParameteriser) which has methods to define parameter transforms

## SceTerminationCondition

```
SceTerminationCondition(handle: CffiData, release_native: Callable[[CffiData], None], type_id: Optional[str] = None, prior_ref_count: int = 0)
```

Bases: `DeletableCffiNativeHandle`

## Simulation

```
Simulation(handle: CffiData, release_native: Callable[[CffiData], None], type_id: Optional[str] = None, prior_ref_count: int = 0)
```

Bases: `DeletableCffiNativeHandle`, `SimulationMixin`

Wrapper around single dimension simulation objects

Methods:

- **`add_state_initialiser`** – Adds a state initialiser to any prior list of state initialisers
- **`apply_recording_function`** – DRAFT Advanced/technical. Record states to a record provider using a callable function.
- **`check_simulation`** – Checks whether a simulation is configured to a state where it is executable
- **`clone`** – Clone this simulation (deep copy)
- **`cookie_cut_dendritic_catchment`** – cookie cut a dendritic catchment (without confluences)
- **`create_ensemble_forecast_simulation`** – Create an ensemble forecast simulation
- **`create_multisite_objective`** – Creates an objective that combines multiple statistics. Used for joined, "whole of catchment" calibration
- **`create_objective`** – Creates an objective calculator
- **`describe`** – Describe the catchment model structure using simple python representations
- **`ensemble_simulation`** – Create an ensemble simulation templated from this simulation
- **`erris_ensemble_simulation`** – Creates an ensemble simulation templated on this simulation, with an ERRIS model on one of the network element
- **`exec_simulation`** – Execute a simulation
- **`from_json_file`** – Create a model simulation from a file with a JSON serialisation.
- **`get_all_played`** – Gets all the time series of models variables into which input time series is/are played
- **`get_all_recorded`** – Gets all the time series of models variables recorded from
- **`get_catchment_structure`** – Gets the essential connective structure of a catchment
- **`get_link_ids`** – Gets all the identifiers of the links in the catchment
- **`get_link_names`** – Gets all the names of the links in the catchment
- **`get_node_ids`** – Gets all the identifiers of the nodes in the catchment
- **`get_node_names`** – Gets all the names of the nodes in the catchment
- **`get_played`** – Retrieves one or more played (input) time series from a simulation
- **`get_played_varnames`** – Gets all the names of model states fed an input time series
- **`get_recorded`** – Retrieves a recorded time series from a simulation
- **`get_recorded_varnames`** – Gets all the names of the recorded states
- **`get_simulation_span`** – Gets the simulation span of this simulation
- **`get_state_value`** – Gets the value(s) of a model state(s)
- **`get_subarea_ids`** – Gets all the identifiers of the subareas in the catchment
- **`get_subarea_names`** – Gets all the names of the subareas in the catchment
- **`get_variable_ids`** – Gets all the names of the variables of an element (link, node, subarea) within a catchment
- **`is_variable_id`** – Are one or more model state identifier(s) valid
- **`muskingum_param_constraints`** – Create a parameteriser with Muskingum-type constraints.
- **`play_input`** – Sets one or more time series as input(s) to a simulation
- **`play_inputs`** – Assign input time series from a time series library to a model simulation
- **`play_subarea_input`** – Sets time series as input to a simulation
- **`prepare_dual_pass_forecasting`** – Create an ensemble simulation for forecasting with the Dual Pass error correction method
- **`prepare_erris_forecasting`** – Create an ensemble simulation for forecasting with ERRIS
- **`record_singular_state`** – DRAFT Advanced/technical. Record states to a record provider.
- **`record_state`** – Record a time series of one of the state of the model
- **`remove_state_initialisers`** – Forces the removal of any state initialiser.
- **`reset_model_states`** – Reset the model states of a simulation, and apply one or more state initialers if the simulation is configured with any.
- **`set_error_correction_model`** – Add an error correction model to an element in a catchment
- **`set_reservoir_geometry`** – Sets the geometry of a reservoir
- **`set_reservoir_max_discharge`** – Sets a reservoir operating curve, maximum release for a given level
- **`set_reservoir_min_discharge`** – Sets a reservoir operating curve, minimum release for a given level
- **`set_reservoir_model`** – Sets a new reservoir model on an element
- **`set_simulation_span`** – Sets the simulation span
- **`set_simulation_time_step`** – Sets the time step of this simulation
- **`set_state_value`** – Sets the value of a model state
- **`set_states`** – Apply memory states to a simulation
- **`snapshot_state`** – Take a snapshot of the memory states of a simulation
- **`sort_by_execution_order`** – Sort the specified element ids according to the execution order of the simulation
- **`split_to_subcatchments`** – Split a catchment in subcatchments, given a list of node/link element identifiers
- **`subset_catchment`** – Subsets a catchment, keeping only a portion above or below a node, link or subarea.
- **`swap_model`** – Clone and change a simulation, using another model
- **`to_json_file`** – Save a model simulation from a file with a JSON serialisation.
- **`use_state_initialises`** – Sets the state initialiser to use for a simulation. This forces the removal of any prior state initialiser.

### add_state_initialiser

```
add_state_initialiser(state_initialiser: StateInitialiser)
```

Adds a state initialiser to any prior list of state initialisers

### apply_recording_function

```
apply_recording_function(recording_func: Optional[RecordToSignature], var_ids: VecStr, recording_provider, data_ids: VecStr) -> None
```

DRAFT Advanced/technical. Record states to a record provider using a callable function.

Likely not for end users. This is used by methods such as EnsembleSimulation.record_ensemble_state.

### check_simulation

```
check_simulation() -> Dict
```

Checks whether a simulation is configured to a state where it is executable

### clone

```
clone() -> Simulation
```

Clone this simulation (deep copy)

Returns:

- **`Simulation`** ( `Simulation` ) – A new simulation object

### cookie_cut_dendritic_catchment

```
cookie_cut_dendritic_catchment(bottom_element_id: str, top_element_ids: Optional[VecStr])
```

cookie cut a dendritic catchment (without confluences)

Parameters:

- **`bottom_element_id`** (`str`) – identifier of the most downstream element to keep
- **`top_element_ids`** (`Optional[VecStr]`) – identifier(s) of the most upstream element(s) to keep. Empty list or None means no upstream cuts.

Returns:

- **`Simulation`** – a subcatchment simulation, cookie cut from the base simulation. Deep clone of objects.

Example

> > > #### sdh swift2.doc_helper
> > >
> > > \_, simulation = sdh.create_test_catchment_structure() e_ids = ['node.n2', 'node.n4'] above_n2 = simulation.cookie_cut_dendritic_catchment(e_ids[0], []) above_n2.describe() {'subareas': {'lnk2': 'lnk2_name', 'lnk3': 'lnk3_name', 'lnk4': 'lnk4_name', 'lnk5': 'lnk5_name'}, 'nodes': {'n2': 'n2_name', 'n5': 'n5_name', 'n4': 'n4_name', 'n3': 'n3_name', 'n1': 'n1_name'}, 'links': {'lnk2': 'lnk2_name', 'lnk3': 'lnk3_name', 'lnk4': 'lnk4_name', 'lnk5': 'lnk5_name'}} above_n2_below_n4 = simulation.cookie_cut_dendritic_catchment(e_ids[0], \[e_ids[1]\]) above_n2_below_n4.describe() {'subareas': {'lnk2': 'lnk2_name', 'lnk3': 'lnk3_name'}, 'nodes': {'n2': 'n2_name', 'n5': 'n5_name'}, 'links': {'lnk2': 'lnk2_name', 'lnk3': 'lnk3_name'}}

### create_ensemble_forecast_simulation

```
create_ensemble_forecast_simulation(data_library, start: ConvertibleToTimestamp, end: ConvertibleToTimestamp, input_map: Dict[str, List[str]], lead_time: int, ensemble_size: int, n_time_steps_between_forecasts: int) -> EnsembleForecastSimulation
```

Create an ensemble forecast simulation

Parameters:

- **`data_library`** (`Any`) – external pointer type ENSEMBLE_DATA_SET_PTR, or a Python class wrapper around it
- **`start`** (`ConvertibleToTimestamp`) – the start date of the simulation. The time zone will be forced to UTC.
- **`end`** (`ConvertibleToTimestamp`) – the end date of the simulation. The time zone will be forced to UTC.
- **`input_map`** (`dict`) – a named list were names are the data library data identifiers, and values are character vectors with model state identifiers.
- **`lead_time`** (`int`) – integer, the length in time steps of the forecasts.
- **`ensemble_size`** (`int`) – ensemble size
- **`n_time_steps_between_forecasts`** (`int`) – nTimeStepsBetweenForecasts

Returns:

- `EnsembleForecastSimulation` – An external pointer

### create_multisite_objective

```
create_multisite_objective(statspec: DataFrame, observations: Sequence[TimeSeriesLike], weights: Dict[str, float]) -> ObjectiveEvaluator
```

Creates an objective that combines multiple statistics. Used for joined, "whole of catchment" calibration

Parameters:

- **`statspec`** (`DataFrame`) – dataframe defining the objectives used. See function multi_statistic_definition to help build this dataframe.
- **`observations`** (`Sequence[TimeSeriesLike]`) – A list of (time series) observations to calculated the statistics. Must be of same length as the number of rows of statspec.
- **`weights`** (`Dict[str, float]`) – numeric vector of weights to ponderate each objective.

Returns:

- **`ObjectiveEvaluator`** ( `ObjectiveEvaluator` ) – an objective evaluator

Examples:

```
>>> _, ms = sdh.create_test_catchment_structure()
>>> from swift2.utils import mk_full_data_id
>>> 
>>> nodeids = ['node.n2', 'node.n4']
>>> mvids = mk_full_data_id(nodeids, 'OutflowRate')
>>> 
>>> sdh.configure_test_simulation(
...     ms,
...     data_id='MMH',
...     simul_start='1990-01-01',
...     simul_end='2005-12-31',
...     tstep='daily',
...     varname_rain='P',
...     varname_pet='E',
...     varname_data_rain='rain',
...     varname_data_pet='evap',
... )
>>>
```

```
>>> ms.record_state(mvids)
>>> ms.exec_simulation()
>>> 
>>> modFlows = ms.get_recorded()
>>>
```

```
>>> w = dict(zip(mvids, [1.0, 2.0]))
>>> w
{'node.n2.OutflowRate': 1.0, 'node.n4.OutflowRate': 2.0}
>>> span = ms.get_simulation_span()
>>>
```

```
>>> from swift2.utils import rep
>>> statspec = sst.multi_statistic_definition(mvids, rep('nse', 2), mvids, mvids, rep(span['start'], 2), rep(span['end'], 2) )
>>> 
>>> statspec
            ModelVarId StatisticId          ObjectiveId        ObjectiveName      Start        End
0  node.n2.OutflowRate         nse  node.n2.OutflowRate  node.n2.OutflowRate 1990-01-01 2005-12-31
1  node.n4.OutflowRate         nse  node.n4.OutflowRate  node.n4.OutflowRate 1990-01-01 2005-12-31
>>> 
>>> # Create synthetic observations
>>> observations = [
...     modFlows.sel(variable_identifiers=mvids[0]) * 0.33,
...     modFlows.sel(variable_identifiers=mvids[1]) * 0.77
... ]
>>> 
>>> obj = ms.create_multisite_objective(statspec, observations, w)
>>>
```

```
>>> dummy = sp.create_parameteriser()
>>> obj.get_scores(dummy)
{'node.n2.OutflowRate': -4.152338377267432, 'node.n4.OutflowRate': 0.8884789439301954}
>>>
```

```
>>> obj.get_score(dummy)
{'scores': {'MultisiteObjectives': 0.7917934964690136}, 'sysconfig': Empty DataFrame
Columns: [Name, Value, Min, Max]
Index: []}
>>>
```

### create_objective

```
create_objective(state_name: str, observation: TimeSeriesLike, statistic: str, start_date: ConvertibleToTimestamp, end_date: ConvertibleToTimestamp) -> ObjectiveEvaluator
```

Creates an objective calculator

Parameters:

- **`state_name`** (`str`) – The name identifying the model state variable to calibrate against the observation
- **`observation`** (`TimeSeriesLike`) – an xts
- **`statistic`** (`str`) – statistic identifier, e.g. "NSE"
- **`start_date`** (`ConvertibleToTimestamp`) – start date of the period to calculate statistics on
- **`end_date`** (`ConvertibleToTimestamp`) – end date of the period to calculate statistics on

Returns:

- **`ObjectiveEvaluator`** ( `ObjectiveEvaluator` ) – single objective evaluator

### describe

```
describe(verbosity: Optional[int] = None) -> Dict
```

Describe the catchment model structure using simple python representations

Parameters:

- **`verbosity`** (`Optional[int]`, default: `None` ) – Future option, unused for now. Defaults to None.

Returns:

- **`Dict`** ( `Dict` ) – A dictionary representation of the catchment structure

### ensemble_simulation

```
ensemble_simulation(ensemble_size: int) -> EnsembleSimulation
```

Create an ensemble simulation templated from this simulation

Parameters:

- **`ensemble_size`** (`int`) – The size of the ensemble dimension

Returns:

- **`EnsembleSimulation`** ( `EnsembleSimulation` ) – Ensemble simulation (ensemble simulation runner)

### erris_ensemble_simulation

```
erris_ensemble_simulation(warmup_start: ConvertibleToTimestamp, warmup_end: ConvertibleToTimestamp, observed_ts: TimeSeriesLike, error_model_element_id: str) -> EnsembleSimulation
```

Creates an ensemble simulation templated on this simulation, with an ERRIS model on one of the network element

Parameters:

- **`warmup_start`** (`ConvertibleToTimestamp`) – start time stamp for the warmup period
- **`warmup_end`** (`ConvertibleToTimestamp`) – end time stamp for the warmup period
- **`observed_ts`** (`TimeSeriesLike`) – Time series of observations to correct prediction against
- **`error_model_element_id`** (`str`) – model element identifier where to set up an ERRIS correction model

Returns:

- **`EnsembleSimulation`** ( `EnsembleSimulation` ) – Ensemble simulation (ensemble simulation runner)

### exec_simulation

```
exec_simulation(reset_initial_states: bool = True) -> None
```

Execute a simulation

Parameters:

- **`reset_initial_states`** (`bool`, default: `True` ) – logical, should the states of the model be reinitialized before the first time step.

### from_json_file

```
from_json_file(file_path: str) -> Simulation
```

Create a model simulation from a file with a JSON serialisation.

Parameters:

- **`file_path`** (`str`) – valid file path.

Returns:

- **`Simulation`** ( `Simulation` ) – a catchment simulation.

### get_all_played

```
get_all_played() -> DataArray
```

Gets all the time series of models variables into which input time series is/are played

### get_all_recorded

```
get_all_recorded() -> DataArray
```

Gets all the time series of models variables recorded from

### get_catchment_structure

```
get_catchment_structure() -> Dict[str, Any]
```

Gets the essential connective structure of a catchment

Parameters:

- **`simulation`** (`Simulation`) – base catchment simulation

Returns:

- `Dict[str, Any]` – Dict\[str, Any\]: A nested dictionary describing the catchment connectivity of subareas, links, and nodes

Examples:

```
>>> _, simulation = sdh.create_test_catchment_structure()
>>> simulation.get_catchment_structure()
{'Node':    Id     Name
0  n1  n1_name
1  n2  n2_name
2  n3  n3_name
3  n4  n4_name
4  n5  n5_name
5  n6  n6_name, 'Link':      Id       Name  LengthMetres    f  ManningsN  Slope
0  lnk1  lnk1_name           0.0  0.0        0.0    0.0
1  lnk2  lnk2_name           0.0  0.0        0.0    0.0
2  lnk3  lnk3_name           0.0  0.0        0.0    0.0
3  lnk4  lnk4_name           0.0  0.0        0.0    0.0
4  lnk5  lnk5_name           0.0  0.0        0.0    0.0, 'Subarea':      Id       Name  AreaKm2
0  lnk1  lnk1_name      1.1
1  lnk2  lnk2_name      2.2
2  lnk3  lnk3_name      3.3
3  lnk4  lnk4_name      4.4
4  lnk5  lnk5_name      5.5, 'NodeLink':   DownstreamId UpstreamId LinkId
0           n6         n2   lnk1
1           n2         n5   lnk2
2           n2         n4   lnk3
3           n4         n3   lnk4
4           n4         n1   lnk5, 'SubareaLink':   LinkId SubareaId
0   lnk1      lnk1
1   lnk2      lnk2
2   lnk3      lnk3
3   lnk4      lnk4
```

### get_link_ids

```
get_link_ids() -> List[str]
```

Gets all the identifiers of the links in the catchment

### get_link_names

```
get_link_names() -> List[str]
```

Gets all the names of the links in the catchment

### get_node_ids

```
get_node_ids() -> List[str]
```

Gets all the identifiers of the nodes in the catchment

### get_node_names

```
get_node_names() -> List[str]
```

Gets all the names of the nodes in the catchment

### get_played

```
get_played(var_ids: Optional[VecStr] = None, start_time: Optional[ConvertibleToTimestamp] = None, end_time: Optional[ConvertibleToTimestamp] = None) -> DataArray
```

Retrieves one or more played (input) time series from a simulation

Parameters:

- **`var_ids`** (`optional str or sequence of str`, default: `None` ) – name(s) of the model variable(s) into which a time series is played as input. e.g. 'Catchment.StreamflowRate'. If missing, a multivariate time series of all played states is returned; this may be a large amount of data.
- **`start_time`** (`datetime like`, default: `None` ) – An optional parameter, the start of a period to subset the time series
- **`end_time`** (`datetime like`, default: `None` ) – An optional parameter, the end of a period to subset the time series

Returns:

- `DataArray` – xr.DataArray: a time series, possibly multivariate.

### get_played_varnames

```
get_played_varnames() -> List[str]
```

Gets all the names of model states fed an input time series

### get_recorded

```
get_recorded(var_ids: Optional[VecStr] = None, start_time: Optional[ConvertibleToTimestamp] = None, end_time: Optional[ConvertibleToTimestamp] = None) -> DataArray
```

Retrieves a recorded time series from a simulation

Parameters:

- **`var_ids`** (`optional str or sequence of str`, default: `None` ) – name(s) of the model variable(s) recorded to a time series. e.g. 'Catchment.StreamflowRate'. If missing, a multivariate time series of all played states is returned; this may be a large amount of data.
- **`start_time`** (`datetime like`, default: `None` ) – An optional parameter, the start of a period to subset the time series
- **`end_time`** (`datetime like`, default: `None` ) – An optional parameter, the end of a period to subset the time series

Returns:

- `DataArray` – xr.DataArray: a time series, possibly multivariate.

### get_recorded_varnames

```
get_recorded_varnames() -> List[str]
```

Gets all the names of the recorded states

Returns:

- `List[str]` – List\[str\]: The names of the state variables being recorded into time series

### get_simulation_span

```
get_simulation_span() -> Dict[str, Any]
```

Gets the simulation span of this simulation

Returns:

- `Dict[str, Any]` – Dict\[str,Any\]: information on the start and end of the simulation, and the time step

### get_state_value

```
get_state_value(var_id: VecStr) -> Union[Dict[str, float], float]
```

Gets the value(s) of a model state(s)

Parameters:

- **`var_id`** (`VecStr`) – string or sequence of str, model variable state identifier(s)

Returns:

- `Union[Dict[str, float], float]` – value(s) of the requested model states

### get_subarea_ids

```
get_subarea_ids() -> List[str]
```

Gets all the identifiers of the subareas in the catchment

### get_subarea_names

```
get_subarea_names() -> List[str]
```

Gets all the names of the subareas in the catchment

### get_variable_ids

```
get_variable_ids(element_id: Optional[str] = None, full_id: bool = True) -> List[str]
```

Gets all the names of the variables of an element (link, node, subarea) within a catchment

Parameters:

- **`element_id`** (`Optional[str]`, default: `None` ) – a character, identifier of the element within the catchment
- **`full_id`** (`bool`, default: `True` ) – boolean, if TRUE return the full hierarchical identifier

### is_variable_id

```
is_variable_id(var_id: VecStr) -> Union[Dict[str, bool], bool]
```

Are one or more model state identifier(s) valid

Parameters:

- **`var_id`** (`VecStr`) – model identifier(s)

Returns:

- `Union[Dict[str, bool], bool]` – Union\[Dict[str, bool], bool\]: whether the identifier(s) are valid. A dictionary is returned if the input is vectorised rather than scalar.

### muskingum_param_constraints

```
muskingum_param_constraints(inner_parameters: HypercubeParameteriser, delta_t: float = 1.0, param_name_k: str = 'K', param_name_x: str = 'X') -> ConstraintParameteriser
```

Create a parameteriser with Muskingum-type constraints.

Given an existing parameteriser, create a wrapper that adds constraints on two of its parameters.

Parameters:

- **`inner_parameters`** (`HypercubeParameteriser`) – A SWIFT parameteriser object that contains two Muskingum-type attenuation and delay parameters.
- **`delta_t`** (`int`, default: `1.0` ) – the simulation time step in HOURS. Defaults to 1.
- **`param_name_k`** (`str`, default: `'K'` ) – the variable identifier to use for the delay parameter of the Muskingum routing. Defaults to "K".
- **`param_name_x`** (`str`, default: `'X'` ) – the variable identifier to use for the attenuation parameter of the Muskingum routing. Defaults to "X".

Returns:

- **`ConstraintParameteriser`** ( `ConstraintParameteriser` ) – A parameteriser with constraints on the feasibility of the attenuation / delay parameters

Examples:

```
>>> todo()
```

### play_input

```
play_input(input_ts: TimeSeriesLike, var_ids: Optional[VecStr] = None) -> None
```

Sets one or more time series as input(s) to a simulation

Parameters:

- **`input_ts`** (`TimeSeriesLike`) – univariate time series. If an xts time series column names must be valid model variable identifiers, unless explicitely provided via varIds
- **`var_ids`** (`optional str or sequence of str`, default: `None` ) – optional character, the variable identifiers to use, overriding the column names of the inputTs. If not NULL, must be of length equal to the number of columns in inputTs

### play_inputs

```
play_inputs(data_library: TimeSeriesLibrary, model_var_id: VecStr, data_id: VecStr, resample: VecStr = '') -> None
```

Assign input time series from a time series library to a model simulation

Parameters:

- **`data_library`** (`TimeSeriesLibrary`) – external pointer type ENSEMBLE_DATA_SET_PTR, or a Python class wrapper around it
- **`model_var_id`** (`str or sequence of str`) – model state variable unique identifier(s)
- **`data_id`** (`str or sequence of str`) – identifier(s) for data in the data_library. If length is not the same as model_var_id, the elements of data_id are reused to match it
- **`resample`** (`str or sequence of str`, default: `''` ) – identifier(s) for how the series is resampled (aggregated or disaggregated). If length is not the same as model_var_id, the elements of resample are reused to match it

### play_subarea_input

```
play_subarea_input(input: TimeSeriesLike, subarea_name: str, input_name: str) -> None
```

Sets time series as input to a simulation

Parameters:

- **`input`** (`TimeSeriesLike`) – univariate time series.
- **`subarea_name`** (`str`) – a valid name of the subarea
- **`input_name`** (`str`) – the name of the input variable to the model (i.e. 'P' for the precip of GR5H)

### prepare_dual_pass_forecasting

```
prepare_dual_pass_forecasting(observation: TimeSeriesLike, error_model_element_id: str, warmup_start: ConvertibleToTimestamp, warmup_end: ConvertibleToTimestamp, required_windows_percentage: float) -> EnsembleSimulation
```

Create an ensemble simulation for forecasting with the Dual Pass error correction method

Parameters:

- **`observation`** (`TimeSeriesLike`) – Time series of observations to correct prediction against
- **`error_model_element_id`** (`str`) – model element identifier where to set up an ERRIS correction model
- **`warmup_start`** (`ConvertibleToTimestamp`) – start time stamp for the warmup period
- **`warmup_end`** (`ConvertibleToTimestamp`) – end time stamp for the warmup period
- **`required_windows_percentage`** (`float`) – required_windows_percentage

Returns:

- **`EnsembleSimulation`** ( `EnsembleSimulation` ) – Ensemble simulation (ensemble simulation runner)

### prepare_erris_forecasting

```
prepare_erris_forecasting(observation: TimeSeriesLike, error_model_element_id: str, warmup_start: ConvertibleToTimestamp, warmup_end: ConvertibleToTimestamp) -> EnsembleSimulation
```

Create an ensemble simulation for forecasting with ERRIS

Parameters:

- **`observation`** (`TimeSeriesLike`) – Time series of observations to correct prediction against
- **`error_model_element_id`** (`str`) – model element identifier where to set up an ERRIS correction model
- **`warmup_start`** (`ConvertibleToTimestamp`) – start time stamp for the warmup period
- **`warmup_end`** (`ConvertibleToTimestamp`) – end time stamp for the warmup period

Returns:

- **`EnsembleSimulation`** ( `EnsembleSimulation` ) – Ensemble simulation (ensemble simulation runner)

### record_singular_state

```
record_singular_state(var_ids: VecStr = CATCHMENT_FLOWRATE_VARID, recording_provider: Optional[TimeSeriesLibrary] = None, data_ids: Optional[VecStr] = None) -> None
```

DRAFT Advanced/technical. Record states to a record provider.

Likely not for end users.

### record_state

```
record_state(var_ids: VecStr = CATCHMENT_FLOWRATE_VARID, recording_provider: Optional[TimeSeriesLibrary] = None, data_ids: Optional[VecStr] = None) -> None
```

Record a time series of one of the state of the model

Parameters:

- **`var_ids`** (`VecStr`, default: `CATCHMENT_FLOWRATE_VARID` ) – identifier(s) of the output variable recorded to a time series, e.g. 'Catchment|StreamflowRate' or 'subcatchment.Subarea.runoff'. Defaults to CATCHMENT_FLOWRATE_VARID.
- **`recording_provider`** (`TimeSeriesLibrary`, default: `None` ) – description. Defaults to None.
- **`data_ids`** (`VecStr`, default: `None` ) – description. Defaults to None.

Raises:

- `ValueError` – description

### remove_state_initialisers

```
remove_state_initialisers()
```

Forces the removal of any state initialiser.

### reset_model_states

```
reset_model_states() -> None
```

Reset the model states of a simulation, and apply one or more state initialers if the simulation is configured with any.

### set_error_correction_model

```
set_error_correction_model(model_id: str, element_id: str, length: int = 1, seed: int = 0) -> None
```

Add an error correction model to an element in a catchment

Parameters:

- **`model_id`** (`str`) – the identifier of the new model to use, e.g. 'ERRIS'
- **`element_id`** (`str`) – the identifier of the catchment element (node, link, subcatchment) whose outflow rate is corrected.
- **`length`** (`int`, default: `1` ) – other parameters to pass to the creation of the error correction model. Currently length of the AR model only supported.
- **`seed`** (`int`, default: `0` ) – other parameters to pass to the creation of the error correction model. Currently length of the AR model only supported.

### set_reservoir_geometry

```
set_reservoir_geometry(element_id: str, level: ndarray, storage: ndarray, area: ndarray) -> None
```

Sets the geometry of a reservoir

Parameters:

- **`element_id`** (`str`) – Element with a suitable reservoir supporting a geometry description
- **`level`** (`ndarray`) – array of water surface levels, in S.I. units (m) TO BE CONFIRMED
- **`storage`** (`ndarray`) – array of volume storages, in S.I. units (m3) TO BE CONFIRMED
- **`area`** (`ndarray`) – array of surfce areas, in S.I. units (m2) TO BE CONFIRMED

### set_reservoir_max_discharge

```
set_reservoir_max_discharge(element_id: str, level: ndarray, discharge: ndarray) -> None
```

Sets a reservoir operating curve, maximum release for a given level

Parameters:

- **`element_id`** (`str`) – Element with a suitable reservoir supporting a geometry description
- **`level`** (`ndarray`) – array of levels (m)
- **`discharge`** (`ndarray`) – array of maximum discharges (m3/s)

### set_reservoir_min_discharge

```
set_reservoir_min_discharge(element_id: str, level: ndarray, discharge: ndarray) -> None
```

Sets a reservoir operating curve, minimum release for a given level

Parameters:

- **`element_id`** (`str`) – Element with a suitable reservoir supporting a geometry description
- **`level`** (`ndarray`) – array of levels (m)
- **`discharge`** (`ndarray`) – array of minimum discharges (m3/s)

### set_reservoir_model

```
set_reservoir_model(new_model_id: str, element_id: str) -> None
```

Sets a new reservoir model on an element

Parameters:

- **`new_model_id`** (`str`) – Currently one of: "ControlledReleaseReservoir", "LevelVolumeAreaReservoir", "FarmDamReservoir";
- **`element_id`** (`str`) – description

### set_simulation_span

```
set_simulation_span(start: ConvertibleToTimestamp, end: ConvertibleToTimestamp) -> None
```

Sets the simulation span

Parameters:

- **`start`** (`ConvertibleToTimestamp`) – the start date of the simulation. The time zone will be forced to UTC.
- **`end`** (`ConvertibleToTimestamp`) – the end date of the simulation. The time zone will be forced to UTC.

### set_simulation_time_step

```
set_simulation_time_step(name: str) -> None
```

Sets the time step of this simulation

Parameters:

- **`name`** (`str`) – a time step identifier, currently 'daily' or 'hourly' are supported. The identifier is made lower case in the function.

### set_state_value

```
set_state_value(var_id: Union[str, Sequence[str]], value: Union[float, int, bool, Sequence] = None) -> None
```

Sets the value of a model state

Parameters:

- **`var_id`** (`Any`) – character, model variable state identifier(s)
- **`value`** (`Any`, default: `None` ) – numeric value(s)

### set_states

```
set_states(states: MemoryStates) -> None
```

Apply memory states to a simulation

Parameters:

- **`states`** (`MemoryStates`) – memory states

### snapshot_state

```
snapshot_state() -> MemoryStates
```

Take a snapshot of the memory states of a simulation

Returns:

- **`MemoryStates`** ( `MemoryStates` ) – memory states, that can be stored and reapplied

### sort_by_execution_order

```
sort_by_execution_order(split_element_ids: Sequence[str], sorting_option: str = '') -> List[str]
```

Sort the specified element ids according to the execution order of the simulation

Parameters:

- **`split_element_ids`** (`Sequence[str]`) – a character vector with element identifiers such as 'node.n1', 'link.linkId_2'
- **`sorting_option`** (`str`, default: `''` ) – a character - for future options. Ignored for now.

Returns:

- `List[str]` – List\[str\]: values in split_element_ids sorted by simulation execution order

### split_to_subcatchments

```
split_to_subcatchments(split_element_ids: Sequence[str], include_upstream: Sequence[bool] = None) -> OrderedDict[str, Simulation]
```

Split a catchment in subcatchments, given a list of node/link element identifiers

Parameters:

- **`split_element_ids`** (`str`) – element identifiers such as 'node.n1', 'link.linkId_2'
- **`include_upstream`** (`bool`, default: `None` ) – indicates whether for each element in split_element_ids it should be including in the upstream portion of the subcatchment. Defaults to None.

Returns:

- **`OrderedDict`** ( `OrderedDict[str, Simulation]` ) – list of subcatchments resulting from the split

Examples:

```
>>> _, simulation = sdh.create_test_catchment_structure()
>>> e_ids = ['node.n2', 'node.n4']
>>> sub_sims = simulation.split_to_subcatchments(e_ids)
>>> for k in sub_sims:
>>>     print(k)
>>>     print(sub_sims[k].get_node_ids())
>>>     print(sub_sims[k].get_node_names())
node.n4
['n4', 'n3', 'n1']
['n4_name', 'n3_name', 'n1_name']
node.n2
['n2', 'n5']
['n2_name', 'n5_name']
remainder
['n6']
['n6_name']
```

### subset_catchment

```
subset_catchment(element_id: str, action: str = 'keep_above')
```

Subsets a catchment, keeping only a portion above or below a node, link or subarea.

Parameters:

- **`element_id`** (`str`) – id of the element to cut at.
- **`action`** (`str`, default: `'keep_above'` ) – how to cut. combinations of 'keep', implied but better explicit, and 'above' or 'below'. You can also have 'exclusive' to exclude the cut point from the result, but this is rarely useful. Examples: 'keep_above', 'keep above', 'keep below exclusive'. See examples.

Returns:

- **`Simulation`** – a subcatchment simulation, cookie cut from the base simulation. Deep clone of objects.

Examples:

```
>>> # sdh  swift2.doc_helper
>>> _, simulation = sdh.create_test_catchment_structure()
>>> n2_id, n4_id = 'node.n2', 'node.n4'
>>> simulation.subset_catchment(n2_id, 'keep below').describe()
{'subareas': {'lnk1': 'lnk1_name'}, 'nodes': {'n2': 'n2_name', 'n6': 'n6_name'}, 'links': {'lnk1': 'lnk1_name'}}
>>> simulation.subset_catchment(n4_id, 'keep above').describe()
{'subareas': {'lnk4': 'lnk4_name', 'lnk5': 'lnk5_name'}, 'nodes': {'n4': 'n4_name', 'n3': 'n3_name', 'n1': 'n1_name'}, 'links': {'lnk4': 'lnk4_name', 'lnk5': 'lnk5_name'}}
>>> # Keep all above node 4, but exclude node 4
>>> simulation.subset_catchment(n4_id, 'keep above exclusive').describe()
{'subareas': {'lnk4': 'lnk4_name', 'lnk5': 'lnk5_name'}, 'nodes': {'n3': 'n3_name', 'n1': 'n1_name'}, 'links': {'lnk4': 'lnk4_name', 'lnk5': 'lnk5_name'}}
>>> # to keep only a headwter catchment with its link:
>>> simulation.subset_catchment("link.lnk5", 'keep above').describe()
{'subareas': {'lnk5': 'lnk5_name'}, 'nodes': {'n1': 'n1_name'}, 'links': {'lnk5': 'lnk5_name'}}
>>> # to keep only a headwter catchment with its link:
>>> simulation.subset_catchment("node.n5", 'keep above exclusive').describe()
{'subareas': {}, 'nodes': {}, 'links': {}}
>>> # below will not work at the time of writing, but maybe should:
>>> simulation.subset_catchment("subarea.lnk5", 'keep above').describe()
Traceback (most recent call last):
```

### swap_model

```
swap_model(model_id: str, what: str = 'runoff') -> Simulation
```

Clone and change a simulation, using another model

Parameters:

- **`model_id`** (`str`) – the identifier of the new model to use, e.g. 'GR4J'
- **`what`** (`str`, default: `'runoff'` ) – character identifying the type of structure replaced: 'runoff', 'channel_routing'

Returns:

- **`Simulation`** ( `Simulation` ) – A SWIFT simulation object, clone of the simulation but with a new model type in use.

### to_json_file

```
to_json_file(file_path: str) -> None
```

Save a model simulation from a file with a JSON serialisation.

Parameters:

- **`file_path`** (`str`) – file path to save to

### use_state_initialises

```
use_state_initialises(state_initialiser: StateInitialiser)
```

Sets the state initialiser to use for a simulation. This forces the removal of any prior state initialiser.

Parameters:

- **`state_initialiser`** (`StateInitialiser`) – the new state initialiser to use

## SimulationMixin

```
SimulationMixin()
```

A parent class for simulation objects. Most users are unlikely to explicitly use it.

Methods:

- **`exec_simulation`** – Execute a simulation
- **`get_played_varnames`** – Gets all the names of states fed an input time series
- **`get_recorded_varnames`** – Gets all the names of the recorded states
- **`record_state`** – Record a time series of one of the state of the model

### exec_simulation

```
exec_simulation(reset_initial_states: bool = True) -> None
```

Execute a simulation

Parameters:

- **`reset_initial_states`** (`bool`, default: `True` ) – logical, should the states of the model be reinitialized before the first time step.

### get_played_varnames

```
get_played_varnames() -> List[str]
```

Gets all the names of states fed an input time series

Returns:

- `List[str]` – List\[str\]: The names of the state variables fed over the simulation with values from a time series

### get_recorded_varnames

```
get_recorded_varnames() -> List[str]
```

Gets all the names of the recorded states

Returns:

- `List[str]` – List\[str\]: The names of the state variables being recorded into time series

### record_state

```
record_state(var_ids: VecStr = CATCHMENT_FLOWRATE_VARID, recording_provider: Optional[TimeSeriesLibrary] = None, data_ids: Optional[VecStr] = None) -> None
```

Record a time series of one of the state of the model

Parameters:

- **`var_ids`** (`VecStr`, default: `CATCHMENT_FLOWRATE_VARID` ) – identifier(s) of the output variable recorded to a time series, e.g. 'Catchment|StreamflowRate' or 'subcatchment.Subarea.runoff'. Defaults to CATCHMENT_FLOWRATE_VARID.
- **`recording_provider`** (`TimeSeriesLibrary`, default: `None` ) – description. Defaults to None.
- **`data_ids`** (`VecStr`, default: `None` ) – description. Defaults to None.

Raises:

- `ValueError` – description

## StateInitParameteriser

```
StateInitParameteriser(handle: CffiData, release_native: Callable[[CffiData], None], type_id: Optional[str] = None, prior_ref_count: int = 0)
```

Bases: `HypercubeParameteriser`

Parameteriser designed to apply to simulations by setting initial states.

Methods:

- **`add_parameter_to_hypercube`** – Add a parameter to a hypercube. Must be a type of object that is expandable, otherwise may raise an exception
- **`add_to_hypercube`** – Add entries to a hypercube. Must be a type of object that is expandable, otherwise may raise an exception.
- **`apply_sys_config`** – Apply a model configuration to a simulation
- **`as_dataframe`** – Convert this hypercube parameteriser to a pandas data frame representation
- **`backtransform`** – Get the parameteriser values in the untransformed space
- **`clone`** –
- **`create_parameter_sampler`** – Creates a sampler for this parameteriser
- **`filtered_parameters`** – Wrap this parameteriser in a filter that can hide some parameters from an optimiser.
- **`from_dataframe`** – Create a parameteriser
- **`make_state_init_parameteriser`** – Create a parameteriser used for model state initialisation
- **`num_free_parameters`** – Number of free parameters in this hypercube parameteriser
- **`score_for_objective`** – Computes the value of an objective for this given set of parameters
- **`set_hypercube`** – Set the properties of a hypercube parameteriser. An exception will ve raised if any parameter name is unknown.
- **`set_max_parameter_value`** – Sets the value(s) of the upper bound of one or more parameter(s)
- **`set_min_parameter_value`** – Sets the value(s) of the lower bound of one or more parameter(s)
- **`set_parameter_definition`** – Sets the feasible range and value for a parameter
- **`set_parameter_value`** – Sets the value(s) of one or more parameter(s)
- **`subcatchment_parameteriser`** – Create a parameteriser that gets applied to a subset of a whole catchment
- **`supports_thread_safe_cloning`** – Is this parameteriser clonable as a deep copy, safe for multi-threading?
- **`wrap_transform`** – Create a parameteriser for which parameter transformations can be defined.

### add_parameter_to_hypercube

```
add_parameter_to_hypercube(name: str, value: float, min: float, max: float)
```

Add a parameter to a hypercube. Must be a type of object that is expandable, otherwise may raise an exception

### add_to_hypercube

```
add_to_hypercube(specs: DataFrame)
```

Add entries to a hypercube. Must be a type of object that is expandable, otherwise may raise an exception.

Parameters:

- **`specs`** (`DataFrame`) – An optional data frame description of the parameter set, with at least columns Name, Min, Max, Value.

> > > from swift2.parameteriser import create_parameteriser loglik = create_parameteriser(type='no apply') loglik.add_to_hypercube( pd.DataFrame({ "Name": c('b','m','s','a','maxobs','ct', 'censopt'), "Min": c(-30, 0, -10, -20, maxobs, censor_threshold, censopt), "Max": c(5, 0, 10, 0, maxobs, censor_threshold, censopt), "Value": c(-7, 0, 0, -10, maxobs, censor_threshold, censopt), } ) )

### apply_sys_config

```
apply_sys_config(simulation: Simulation)
```

Apply a model configuration to a simulation

Parameters:

- **`simulation`** (`Simulation`) – simulation

### as_dataframe

```
as_dataframe() -> DataFrame
```

Convert this hypercube parameteriser to a pandas data frame representation

Returns:

- `DataFrame` – pd.DataFrame: pandas data frame

### backtransform

```
backtransform() -> HypercubeParameteriser
```

Get the parameteriser values in the untransformed space

Get the parameteriser values in the untransformed space, i.e. remove any transform added via HypercubeParameteriser.wrap_transform. This allows to transform back e.g. from a virtual parameter log_X to the underlying model (or even virtual/meta) parameter X.

Returns:

- **`HypercubeParameteriser`** ( `HypercubeParameteriser` ) – The parameters definitions without the transforms (if there are any)

Examples:

```
>>> ref_area = 250
>>> time_span = 3600
>>> ptrans = sdh.define_gr4j_scaled_parameter(ref_area, time_span)
>>> ptrans
    Name     Value       Min       Max
0    log_x4  0.305422  0.000000  2.380211
1    log_x1  0.506690  0.000000  3.778151
2    log_x3  0.315425  0.000000  3.000000
3  asinh_x2  2.637752 -3.989327  3.989327
>>> ptrans.backtransform()
Name    Value   Min     Max
0   x2  6.95511 -27.0    27.0
1   x3  2.06740   1.0  1000.0
2   x4  2.02033   1.0   240.0
3   x1  3.21137   1.0  6000.0
>>>
```

### clone

```
clone() -> HypercubeParameteriser
```

### create_parameter_sampler

```
create_parameter_sampler(seed: int = 0, type: str = 'urs') -> CandidateFactorySeed
```

Creates a sampler for this parameteriser

Parameters:

- **`seed`** (`int`, default: `0` ) – a seed for the sampler. Defaults to 0.
- **`type`** (`str`, default: `'urs'` ) – the type of sampler. Defaults to "urs" for Uniform Random Sampling. This is the only option supported as of 2023-01.

Returns:

- **`CandidateFactorySeed`** ( `CandidateFactorySeed` ) – a sampler, aka candidate factory

### filtered_parameters

```
filtered_parameters() -> FilteringParameteriser
```

Wrap this parameteriser in a filter that can hide some parameters from an optimiser.

Used for instance in calibration with log-likelihood contexts.

Returns:

- `FilteringParameteriser` – an parameteriser designed to only show a subset to an optimiser, while applying more to a simulation.

### from_dataframe

```
from_dataframe(type='Generic subareas', definition: Optional[DataFrame] = None) -> HypercubeParameteriser
```

Create a parameteriser

Parameters:

- **`type`** (`str`, default: `'Generic subareas'` ) – A string identifying the type of parameteriser to use. Recognised types are (case insensitive) 'log-likelihood', 'generic', 'subareas', 'links', 'nodes' and 'muskingum'. Defaults to "Generic subareas".
- **`specs`** (`DataFrame`) – An optional data frame description of the parameter set, with at least columns Name, Min, Max, Value. Defaults to None.

Returns:

- **`HypercubeParameteriser`** ( `HypercubeParameteriser` ) – new parameteriser

Examples:

```
>>> d = pd.DataFrame(
...     dict(
...         Name=c("alpha", "inverse_velocity"),
...         Value=c(1, 1),
...         Min=c(1e-3, 1e-3),
...         Max=c(1e2, 1e2),
...     )
... )
>>> p = HypercubeParameteriser.from_dataframe("Generic links", d)
>>> p
```

### make_state_init_parameteriser

```
make_state_init_parameteriser() -> StateInitParameteriser
```

Create a parameteriser used for model state initialisation

This allows to define tied parameters where, for instance, pval = a * modelStateVal. A more concrete use case is to define an initial soil moisture store 'S0', as a fraction of the model store capacity 'Smax'. The model state to initialise is 'S'

Note

See also swift2.classes.ScalingParameteriser for typical joint usage.

Returns:

- **`StateInitParameteriser`** ( `StateInitParameteriser` ) – state initialisation parameteriser

Examples:

```
>>> # Use case: Set gr4j initial stores at simulation as a function of x1/x3 parameters.
>>> import swift2.parameteriser as sp
>>> # Let's define _S0_ and _R0_ parameters such that for each GR4J model instance, _S = S0 * x1_ and _R = R0 * x3_
>>> p_states = sp.linear_parameteriser(
                param_name=c("S0","R0"), # new virtual parameters to optimise
                state_name=c("S","R"), 
                scaling_var_name=c("x1","x3"),
                min_p_val=c(0.0,0.0), 
                max_p_val=c(1.0,1.0), 
                value=c(0.9,0.9), 
                selector_type='each subarea')
>>> init_parameteriser = p_states.make_state_init_parameteriser()
```

### num_free_parameters

```
num_free_parameters() -> int
```

Number of free parameters in this hypercube parameteriser

Returns:

- **`int`** ( `int` ) – Number of free parameters

### score_for_objective

```
score_for_objective(objective: ObjectiveEvaluator) -> Dict[str, Any]
```

Computes the value of an objective for this given set of parameters

### set_hypercube

```
set_hypercube(specs: DataFrame)
```

Set the properties of a hypercube parameteriser. An exception will ve raised if any parameter name is unknown.

Parameters:

- **`specs`** (`DataFrame`) – An optional data frame description of the parameter set, with at least columns Name, Min, Max, Value.

Examples:

```
>>> # e.g. if `p` is a typical parameteriser for GR4J with 
>>> # set x4 bounds to be in "days", not hours
>>> p_x4 = pd.DataFrame.from_dict({
    "Name": ["x4"],
    "Value": [1.0],
    "Min": [0.25],
    "Max": [10.0],
})
>>> p.set_hypercube(p_x4)
```

### set_max_parameter_value

```
set_max_parameter_value(variable_name: VecStr, value: VecScalars)
```

Sets the value(s) of the upper bound of one or more parameter(s)

Parameters:

- **`variable_name`** (`VecStr`) – one or more parameter name(s)
- **`value`** (`VecScalars`) – one or more parameter value(s)

### set_min_parameter_value

```
set_min_parameter_value(variable_name: VecStr, value: VecScalars)
```

Sets the value(s) of the lower bound of one or more parameter(s)

Parameters:

- **`variable_name`** (`VecStr`) – one or more parameter name(s)
- **`value`** (`VecScalars`) – one or more parameter value(s)

### set_parameter_definition

```
set_parameter_definition(variable_name: str, min: float, max: float, value: float)
```

Sets the feasible range and value for a parameter

Parameters:

- **`variable_name`** (`str`) – parameter name
- **`min`** (`float`) – min
- **`max`** (`float`) – max
- **`value`** (`float`) – value

### set_parameter_value

```
set_parameter_value(variable_name: VecStr, value: VecScalars)
```

Sets the value(s) of one or more parameter(s)

Parameters:

- **`variable_name`** (`VecStr`) – one or more parameter name(s)
- **`value`** (`VecScalars`) – one or more parameter value(s)

### subcatchment_parameteriser

```
subcatchment_parameteriser(subcatchment)
```

Create a parameteriser that gets applied to a subset of a whole catchment

Parameters:

- **`subcatchment`** (`Simulation`) – the subcatchment, subset of a whole catchment, identifying which elements (subareas, nodes, links) will be parameterised by the new parameteriser. Other catchment elements are untouched.

Returns:

- **`HypercubeParameteriser`** – New parameteriser whose application is limited to the subcatchment.

Examples:

```
>>> sub_cats = simulation.split_to_subcatchments(["node.node_7", "node.node_10"])
>>> sc = sub_cats["node.node_7"]
>>> p = sp.create_parameteriser('generic subarea')
>>> p.add_parameter_to_hypercube("x1", 32, 1, 6e3)
>>> sp = p.subcatchment_parameteriser(sc)
>>> sp.apply_sys_config(simulation)
```

### supports_thread_safe_cloning

```
supports_thread_safe_cloning() -> bool
```

Is this parameteriser clonable as a deep copy, safe for multi-threading?

### wrap_transform

```
wrap_transform() -> TransformParameteriser
```

Create a parameteriser for which parameter transformations can be defined.

This allows to define e.g. a virtual parameter log_X instead of calibrating on the parameter X.

Returns:

- **`TransformParameteriser`** ( `TransformParameteriser` ) – A new parameteriser (TransformParameteriser) which has methods to define parameter transforms

## StateInitialiser

```
StateInitialiser(handle: CffiData, release_native: Callable[[CffiData], None], type_id: Optional[str] = None, prior_ref_count: int = 0)
```

Bases: `DeletableCffiNativeHandle`

Methods:

- **`clone`** –
- **`is_dictionary_like`** –

### clone

```
clone() -> StateInitialiser
```

### is_dictionary_like

```
is_dictionary_like() -> bool
```

## TransformParameteriser

```
TransformParameteriser(handle: CffiData, release_native: Callable[[CffiData], None], type_id: Optional[str] = None, prior_ref_count: int = 0)
```

Bases: `HypercubeParameteriser`

Parameteriser projecting parameters in a transformed space for optimisation.

Methods:

- **`add_parameter_to_hypercube`** – Add a parameter to a hypercube. Must be a type of object that is expandable, otherwise may raise an exception
- **`add_to_hypercube`** – Add entries to a hypercube. Must be a type of object that is expandable, otherwise may raise an exception.
- **`add_transform`** – Create a parameteriser for which parameter transformations can be defined
- **`apply_sys_config`** – Apply a model configuration to a simulation
- **`as_dataframe`** – Convert this hypercube parameteriser to a pandas data frame representation
- **`backtransform`** – Get the parameteriser values in the untransformed space
- **`clone`** –
- **`create_parameter_sampler`** – Creates a sampler for this parameteriser
- **`filtered_parameters`** – Wrap this parameteriser in a filter that can hide some parameters from an optimiser.
- **`from_dataframe`** – Create a parameteriser
- **`make_state_init_parameteriser`** – Create a parameteriser used for model state initialisation
- **`num_free_parameters`** – Number of free parameters in this hypercube parameteriser
- **`score_for_objective`** – Computes the value of an objective for this given set of parameters
- **`set_hypercube`** – Set the properties of a hypercube parameteriser. An exception will ve raised if any parameter name is unknown.
- **`set_max_parameter_value`** – Sets the value(s) of the upper bound of one or more parameter(s)
- **`set_min_parameter_value`** – Sets the value(s) of the lower bound of one or more parameter(s)
- **`set_parameter_definition`** – Sets the feasible range and value for a parameter
- **`set_parameter_value`** – Sets the value(s) of one or more parameter(s)
- **`subcatchment_parameteriser`** – Create a parameteriser that gets applied to a subset of a whole catchment
- **`supports_thread_safe_cloning`** – Is this parameteriser clonable as a deep copy, safe for multi-threading?
- **`wrap_transform`** – Create a parameteriser for which parameter transformations can be defined.

### add_parameter_to_hypercube

```
add_parameter_to_hypercube(name: str, value: float, min: float, max: float)
```

Add a parameter to a hypercube. Must be a type of object that is expandable, otherwise may raise an exception

### add_to_hypercube

```
add_to_hypercube(specs: DataFrame)
```

Add entries to a hypercube. Must be a type of object that is expandable, otherwise may raise an exception.

Parameters:

- **`specs`** (`DataFrame`) – An optional data frame description of the parameter set, with at least columns Name, Min, Max, Value.

> > > from swift2.parameteriser import create_parameteriser loglik = create_parameteriser(type='no apply') loglik.add_to_hypercube( pd.DataFrame({ "Name": c('b','m','s','a','maxobs','ct', 'censopt'), "Min": c(-30, 0, -10, -20, maxobs, censor_threshold, censopt), "Max": c(5, 0, 10, 0, maxobs, censor_threshold, censopt), "Value": c(-7, 0, 0, -10, maxobs, censor_threshold, censopt), } ) )

### add_transform

```
add_transform(param_name: str, inner_param_name: str, transform_id: str, a: float = 1.0, b: float = 0.0)
```

Create a parameteriser for which parameter transformations can be defined

```
This allows to define e.g. a virtual parameter log_X instead of calibrating on the parameter X.
```

Parameters:

- **`param_name`** (`str`) – the name of the meta-parameter. Note that it can be the same value as inner_param_name, but this is NOT recommended.
- **`inner_param_name`** (`str`) – the name of the parameter being transformed
- **`transform_id`** (`str`) – identifier for a known bijective univariate function
- **`a`** (`float`, default: `1.0` ) – parameter in Y = F(ax+b). Defaults to 1.0.
- **`b`** (`float`, default: `0.0` ) – parameter in Y = F(ax+b). Defaults to 0.0.

Examples:

```
>>> from swift2.doc_helper import get_free_params
>>> pspec_gr4j = get_free_params('GR4J')
>>> p = HypercubeParameteriser.from_dataframe("generic subarea", pspec_gr4j)
>>> p
Name       Value   Min     Max
0   x1  650.488000   1.0  3000.0
1   x2   -0.280648 -27.0    27.0
2   x3    7.891230   1.0   660.0
3   x4   18.917200   1.0   240.0
>>> p = p.wrap_transform()
>>> p.add_transform("log_x4", "x4", "log10")
>>> p
    Name       Value   Min          Max
0  log_x4    1.276857   0.0     2.380211
1      x1  650.488000   1.0  3000.000000
2      x2   -0.280648 -27.0    27.000000
3      x3    7.891230   1.0   660.000000
>>> p.backtransform()
Name       Value   Min     Max
0   x1  650.488000   1.0  3000.0
1   x2   -0.280648 -27.0    27.0
2   x3    7.891230   1.0   660.0
3   x4   18.917200   1.0   240.0
>>>
```

### apply_sys_config

```
apply_sys_config(simulation: Simulation)
```

Apply a model configuration to a simulation

Parameters:

- **`simulation`** (`Simulation`) – simulation

### as_dataframe

```
as_dataframe() -> DataFrame
```

Convert this hypercube parameteriser to a pandas data frame representation

Returns:

- `DataFrame` – pd.DataFrame: pandas data frame

### backtransform

```
backtransform() -> HypercubeParameteriser
```

Get the parameteriser values in the untransformed space

Get the parameteriser values in the untransformed space, i.e. remove any transform added via HypercubeParameteriser.wrap_transform. This allows to transform back e.g. from a virtual parameter log_X to the underlying model (or even virtual/meta) parameter X.

Returns:

- **`HypercubeParameteriser`** ( `HypercubeParameteriser` ) – The parameters definitions without the transforms (if there are any)

Examples:

```
>>> ref_area = 250
>>> time_span = 3600
>>> ptrans = sdh.define_gr4j_scaled_parameter(ref_area, time_span)
>>> ptrans
    Name     Value       Min       Max
0    log_x4  0.305422  0.000000  2.380211
1    log_x1  0.506690  0.000000  3.778151
2    log_x3  0.315425  0.000000  3.000000
3  asinh_x2  2.637752 -3.989327  3.989327
>>> ptrans.backtransform()
Name    Value   Min     Max
0   x2  6.95511 -27.0    27.0
1   x3  2.06740   1.0  1000.0
2   x4  2.02033   1.0   240.0
3   x1  3.21137   1.0  6000.0
>>>
```

### clone

```
clone() -> HypercubeParameteriser
```

### create_parameter_sampler

```
create_parameter_sampler(seed: int = 0, type: str = 'urs') -> CandidateFactorySeed
```

Creates a sampler for this parameteriser

Parameters:

- **`seed`** (`int`, default: `0` ) – a seed for the sampler. Defaults to 0.
- **`type`** (`str`, default: `'urs'` ) – the type of sampler. Defaults to "urs" for Uniform Random Sampling. This is the only option supported as of 2023-01.

Returns:

- **`CandidateFactorySeed`** ( `CandidateFactorySeed` ) – a sampler, aka candidate factory

### filtered_parameters

```
filtered_parameters() -> FilteringParameteriser
```

Wrap this parameteriser in a filter that can hide some parameters from an optimiser.

Used for instance in calibration with log-likelihood contexts.

Returns:

- `FilteringParameteriser` – an parameteriser designed to only show a subset to an optimiser, while applying more to a simulation.

### from_dataframe

```
from_dataframe(type='Generic subareas', definition: Optional[DataFrame] = None) -> HypercubeParameteriser
```

Create a parameteriser

Parameters:

- **`type`** (`str`, default: `'Generic subareas'` ) – A string identifying the type of parameteriser to use. Recognised types are (case insensitive) 'log-likelihood', 'generic', 'subareas', 'links', 'nodes' and 'muskingum'. Defaults to "Generic subareas".
- **`specs`** (`DataFrame`) – An optional data frame description of the parameter set, with at least columns Name, Min, Max, Value. Defaults to None.

Returns:

- **`HypercubeParameteriser`** ( `HypercubeParameteriser` ) – new parameteriser

Examples:

```
>>> d = pd.DataFrame(
...     dict(
...         Name=c("alpha", "inverse_velocity"),
...         Value=c(1, 1),
...         Min=c(1e-3, 1e-3),
...         Max=c(1e2, 1e2),
...     )
... )
>>> p = HypercubeParameteriser.from_dataframe("Generic links", d)
>>> p
```

### make_state_init_parameteriser

```
make_state_init_parameteriser() -> StateInitParameteriser
```

Create a parameteriser used for model state initialisation

This allows to define tied parameters where, for instance, pval = a * modelStateVal. A more concrete use case is to define an initial soil moisture store 'S0', as a fraction of the model store capacity 'Smax'. The model state to initialise is 'S'

Note

See also swift2.classes.ScalingParameteriser for typical joint usage.

Returns:

- **`StateInitParameteriser`** ( `StateInitParameteriser` ) – state initialisation parameteriser

Examples:

```
>>> # Use case: Set gr4j initial stores at simulation as a function of x1/x3 parameters.
>>> import swift2.parameteriser as sp
>>> # Let's define _S0_ and _R0_ parameters such that for each GR4J model instance, _S = S0 * x1_ and _R = R0 * x3_
>>> p_states = sp.linear_parameteriser(
                param_name=c("S0","R0"), # new virtual parameters to optimise
                state_name=c("S","R"), 
                scaling_var_name=c("x1","x3"),
                min_p_val=c(0.0,0.0), 
                max_p_val=c(1.0,1.0), 
                value=c(0.9,0.9), 
                selector_type='each subarea')
>>> init_parameteriser = p_states.make_state_init_parameteriser()
```

### num_free_parameters

```
num_free_parameters() -> int
```

Number of free parameters in this hypercube parameteriser

Returns:

- **`int`** ( `int` ) – Number of free parameters

### score_for_objective

```
score_for_objective(objective: ObjectiveEvaluator) -> Dict[str, Any]
```

Computes the value of an objective for this given set of parameters

### set_hypercube

```
set_hypercube(specs: DataFrame)
```

Set the properties of a hypercube parameteriser. An exception will ve raised if any parameter name is unknown.

Parameters:

- **`specs`** (`DataFrame`) – An optional data frame description of the parameter set, with at least columns Name, Min, Max, Value.

Examples:

```
>>> # e.g. if `p` is a typical parameteriser for GR4J with 
>>> # set x4 bounds to be in "days", not hours
>>> p_x4 = pd.DataFrame.from_dict({
    "Name": ["x4"],
    "Value": [1.0],
    "Min": [0.25],
    "Max": [10.0],
})
>>> p.set_hypercube(p_x4)
```

### set_max_parameter_value

```
set_max_parameter_value(variable_name: VecStr, value: VecScalars)
```

Sets the value(s) of the upper bound of one or more parameter(s)

Parameters:

- **`variable_name`** (`VecStr`) – one or more parameter name(s)
- **`value`** (`VecScalars`) – one or more parameter value(s)

### set_min_parameter_value

```
set_min_parameter_value(variable_name: VecStr, value: VecScalars)
```

Sets the value(s) of the lower bound of one or more parameter(s)

Parameters:

- **`variable_name`** (`VecStr`) – one or more parameter name(s)
- **`value`** (`VecScalars`) – one or more parameter value(s)

### set_parameter_definition

```
set_parameter_definition(variable_name: str, min: float, max: float, value: float)
```

Sets the feasible range and value for a parameter

Parameters:

- **`variable_name`** (`str`) – parameter name
- **`min`** (`float`) – min
- **`max`** (`float`) – max
- **`value`** (`float`) – value

### set_parameter_value

```
set_parameter_value(variable_name: VecStr, value: VecScalars)
```

Sets the value(s) of one or more parameter(s)

Parameters:

- **`variable_name`** (`VecStr`) – one or more parameter name(s)
- **`value`** (`VecScalars`) – one or more parameter value(s)

### subcatchment_parameteriser

```
subcatchment_parameteriser(subcatchment)
```

Create a parameteriser that gets applied to a subset of a whole catchment

Parameters:

- **`subcatchment`** (`Simulation`) – the subcatchment, subset of a whole catchment, identifying which elements (subareas, nodes, links) will be parameterised by the new parameteriser. Other catchment elements are untouched.

Returns:

- **`HypercubeParameteriser`** – New parameteriser whose application is limited to the subcatchment.

Examples:

```
>>> sub_cats = simulation.split_to_subcatchments(["node.node_7", "node.node_10"])
>>> sc = sub_cats["node.node_7"]
>>> p = sp.create_parameteriser('generic subarea')
>>> p.add_parameter_to_hypercube("x1", 32, 1, 6e3)
>>> sp = p.subcatchment_parameteriser(sc)
>>> sp.apply_sys_config(simulation)
```

### supports_thread_safe_cloning

```
supports_thread_safe_cloning() -> bool
```

Is this parameteriser clonable as a deep copy, safe for multi-threading?

### wrap_transform

```
wrap_transform() -> TransformParameteriser
```

Create a parameteriser for which parameter transformations can be defined.

This allows to define e.g. a virtual parameter log_X instead of calibrating on the parameter X.

Returns:

- **`TransformParameteriser`** ( `TransformParameteriser` ) – A new parameteriser (TransformParameteriser) which has methods to define parameter transforms

## VectorObjectiveScores

```
VectorObjectiveScores(handle: CffiData, release_native: Callable[[CffiData], None], type_id: Optional[str] = None, prior_ref_count: int = 0)
```

Bases: `DeletableCffiNativeHandle`

Methods:

- **`as_dataframe`** –
- **`get_best_score`** –
- **`get_parameters_at_index`** –
- **`get_score_at_index`** –
- **`sort_by_score`** –

Attributes:

- **`size`** (`int`) –

### size

```
size: int
```

### as_dataframe

```
as_dataframe()
```

### get_best_score

```
get_best_score(score_name='NSE', convert_to_py=False)
```

### get_parameters_at_index

```
get_parameters_at_index(index)
```

### get_score_at_index

```
get_score_at_index(index)
```

### sort_by_score

```
sort_by_score(score_name='NSE')
```

## wrap_cffi_native_handle

```
wrap_cffi_native_handle(obj: Any, type_id: str, release_native: Callable)
```
