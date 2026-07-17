# Module classes

# classes

Classes:

- **`CandidateFactorySeed`** – Generates initial parameter sets for optimisation algorithms using specified sampling strategies (e.g., uniform random sampling).
- **`CompositeParameteriser`** – Combines multiple parameterisers into a single unit, useful for calibrating different model components with distinct parameter sets.
- **`ConstraintParameteriser`** – Enforces feasibility constraints on parameter combinations (e.g., Muskingum routing stability conditions).
- **`EnsembleForecastSimulation`** – Manages sequential ensemble forecast runs with regular forecast initialisation times and specified lead times.
- **`EnsembleSimulation`** – UNDER CONSTRUCTION - Manages ensemble simulations over replicate inputs series, allowing for setup, state recording, and retrieval of simulation spans.
- **`ErrisStagedCalibration`** – Orchestrates multi-stage calibration where hydrologic parameters and ERRIS error model parameters are estimated sequentially.
- **`FilteringParameteriser`** – Shows only a subset of parameters to optimizers while applying all parameters to simulations, used in log-likelihood calibration.
- **`FunctionsParameteriser`** – Manages parameters for multisite multi-objective calibration where different statistics are computed at multiple locations.
- **`HypercubeParameteriser`** – Defines parameter bounds, values, and names as a hypercube for optimisation and sensitivity analysis.
- **`MaerrisStagedCalibration`** – Performs staged calibration using the MAERRIS error correction approach with separate hydrologic and error model phases.
- **`MemoryStates`** – Captures a snapshot of all model states at a point in time for later restoration or analysis.
- **`ObjectiveEvaluator`** – Calculates goodness-of-fit statistics by comparing simulated outputs to observations over a specified period.
- **`ObjectiveScores`** – Holds the results of an objective evaluation including score values and the associated parameter set.
- **`Optimiser`** – Executes parameter estimation algorithms (typically SCE-UA) to find optimal parameter values for a given objective.
- **`Parameteriser`** – Base class for objects that define and apply parameter configurations to simulations.
- **`ScalingParameteriser`** – Defines linear relationships between virtual parameters and model states (e.g., initial storage as fraction of capacity).
- **`SceTerminationCondition`** – Specifies when the SCE-UA optimizer should stop (e.g., max iterations, convergence tolerance, wall time).
- **`Simulation`** – Represents a catchment model with its structure, states, and configuration; executes time-stepping simulations.
- **`SimulationMixin`** – Provides common simulation methods shared by Simulation, EnsembleSimulation, and EnsembleForecastSimulation classes.
- **`StateInitParameteriser`** – Defines how to initialize model states based on parameter values at the start of each simulation run.
- **`StateInitialiser`** – Sets initial conditions for model states before simulation execution begins.
- **`TransformParameteriser`** – Applies mathematical transformations (e.g., log, arcsinh) to parameters optimisation in transformed space.
- **`VectorObjectiveScores`** – Collection of multiple ObjectiveScores, typically a capture of a from a population-based optimizer's iteration.

Functions:

- **`wrap_cffi_native_handle`** –

## CandidateFactorySeed

```
CandidateFactorySeed(handle: CffiData, release_native: Callable[[CffiData], None], type_id: Optional[str] = None, prior_ref_count: int = 0)
```

Bases: `DeletableCffiNativeHandle`

Generates initial parameter sets for optimisation algorithms using specified sampling strategies (e.g., uniform random sampling).

## CompositeParameteriser

```
CompositeParameteriser(handle: CffiData, release_native: Callable[[CffiData], None], type_id: Optional[str] = None, prior_ref_count: int = 0)
```

Bases: `HypercubeParameteriser`

Combines multiple parameterisers into a single unit, useful for calibrating different model components with distinct parameter sets.

Methods:

- **`add_parameter_to_hypercube`** – Add a parameter to a hypercube. Must be a type of object that is expandable, otherwise may raise an exception
- **`add_to_hypercube`** – Add entries to a hypercube. Must be a type of object that is expandable, otherwise may raise an exception.
- **`append`** – Appends a parameteriser to this composite parameteriser.
- **`apply_sys_config`** – Apply a model configuration to a simulation
- **`as_dataframe`** – Convert this hypercube parameteriser to a pandas data frame representation
- **`backtransform`** – Get the parameteriser values in the untransformed space
- **`clone`** –
- **`concatenate`** – Concatenates some hypercubes to a single parameteriser
- **`create_parameter_sampler`** – Creates a sampler for this parameteriser
- **`empty_composite`** – Creates an empty parameteriser to be populated with other parameterisers
- **`filtered_parameters`** – Wrap this parameteriser in a filter that can hide some parameters from an optimiser.
- **`from_dataframe`** – Creates a parameteriser from a parameter specification.
- **`from_json_file`** – Load a parameteriser from a file with a JSON serialisation.
- **`make_state_init_parameteriser`** – Converts this parameteriser into a StateInitParameteriser.
- **`num_free_parameters`** – Number of free parameters in this hypercube parameteriser
- **`score_for_objective`** – Computes the value of an objective for this given set of parameters
- **`set_hypercube`** – Updates parameter properties for an existing parameteriser.
- **`set_max_parameter_value`** – Sets the value(s) of the upper bound of one or more parameter(s)
- **`set_min_parameter_value`** – Sets the value(s) of the lower bound of one or more parameter(s)
- **`set_parameter_definition`** – Sets the feasible range and value for a parameter
- **`set_parameter_value`** – Sets the value(s) of one or more parameter(s)
- **`subcatchment_parameteriser`** – Create a parameteriser that gets applied to a subset of a whole catchment
- **`supports_thread_safe_cloning`** – Is this parameteriser clonable as a deep copy, safe for multi-threading?
- **`to_json_file`** – Save this parameteriser to a file with a JSON serialisation.
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

Appends a parameteriser to this composite parameteriser.

Adds another parameteriser to the end of this composite. The order matters: when applied to a simulation, parameterisers are processed in the order they were appended. Later parameterisers can override values set by earlier ones if they affect the same model elements.

Parameters:

- **`p`** (`HypercubeParameteriser`) – Parameteriser to append. Can be any HypercubeParameteriser subclass including another CompositeParameteriser.

Note

The appended parameteriser is deep-copied before being added, so subsequent changes to `p` do not affect this composite.

Examples:

```
>>> # Combine runoff and routing parameters
>>> p_runoff = HypercubeParameteriser.from_dataframe('generic subareas', gr4j_spec)
>>> p_routing = HypercubeParameteriser.from_dataframe('generic links', routing_spec)
>>> 
>>> p_composite = CompositeParameteriser.empty_composite()
>>> p_composite.append(p_runoff)
>>> p_composite.append(p_routing)
>>> p_composite.apply_sys_config(simulation)
```

```
>>> # Combine parameters for different subcatchments
>>> p_upper = create_parameteriser_for_upper_catchment()
>>> p_lower = create_parameteriser_for_lower_catchment()
>>> p_all = CompositeParameteriser.empty_composite()
>>> p_all.append(p_upper)
>>> p_all.append(p_lower)
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
from_dataframe(type: str = 'Generic subareas', definition: Optional[DataFrame] = None) -> HypercubeParameteriser
```

Creates a parameteriser from a parameter specification.

Factory method to create different types of parameterisers based on the 'type' string. The type determines which model elements (subareas, links, nodes) the parameters will be applied to.

Parameters:

- **`type`** (`str`, default: `'Generic subareas'` ) – Parameteriser type identifier (case-insensitive). Valid options:
  - 'generic' or 'generic subareas': Apply to all subareas (default)
  - 'links' or 'generic links': Apply to channel routing in links
  - 'nodes' or 'generic nodes': Apply to nodes
  - 'muskingum': Muskingum channel routing parameters
  - 'log-likelihood': Parameters for log-likelihood transformation (advanced) Defaults to "Generic subareas".
- **`definition`** (`DataFrame`, default: `None` ) – Parameter specifications with columns:
  - 'Name': Parameter name (e.g., 'x1', 'x2', 'alpha')
  - 'Min': Minimum feasible value
  - 'Max': Maximum feasible value
  - 'Value': Initial/current value If None, creates an empty parameteriser that can be populated later. Defaults to None.

Returns:

- **`HypercubeParameteriser`** ( `HypercubeParameteriser` ) – New parameteriser configured according to the type.

Examples:

```
>>> # Create GR4J parameters for subareas
>>> import pandas as pd
>>> from swift2.utils import c
>>> pspec = pd.DataFrame({
...     'Name': c('x1', 'x2', 'x3', 'x4'),
...     'Value': c(350, -0.5, 50, 2),
...     'Min': c(1, -27, 1, 1),
...     'Max': c(3000, 27, 1000, 240)
... })
>>> p = HypercubeParameteriser.from_dataframe('generic subareas', pspec)
```

```
>>> # Create link routing parameters
>>> link_spec = pd.DataFrame({
...     'Name': c('alpha', 'inverse_velocity'),
...     'Value': c(1, 1),
...     'Min': c(1e-3, 1e-3),
...     'Max': c(1e2, 1e2)
... })
>>> p_links = HypercubeParameteriser.from_dataframe('generic links', link_spec)
```

```
>>> # Create empty parameteriser to populate later
>>> p_empty = HypercubeParameteriser.from_dataframe('generic')
>>> p_empty.add_parameter_to_hypercube('x1', value=350, min=1, max=3000)
```

### from_json_file

```
from_json_file(file_path: str) -> HypercubeParameteriser
```

Load a parameteriser from a file with a JSON serialisation.

Parameters:

- **`file_path`** (`str`) – file path to load from

Returns:

- **`HypercubeParameteriser`** ( `HypercubeParameteriser` ) – loaded parameteriser

### make_state_init_parameteriser

```
make_state_init_parameteriser() -> StateInitParameteriser
```

Converts this parameteriser into a StateInitParameteriser.

Creates a StateInitParameteriser object that can be applied to simulations to set initial model states based on parameter values, as part of an optimisation process i.e. optimising some initial states. This is typically the subsequent step after defining scaled parameter relationships using ScalingParameteriser methods, and before inclusion in an optimisation workflow.

Returns:

- **`StateInitParameteriser`** ( `StateInitParameteriser` ) – Parameteriser with features to set model initial states via state initialisers,
- `StateInitParameteriser` – overriding the default simulation for model reset of initial states.

Typical Workflow

1. Create a ScalingParameteriser with linear_parameteriser() or linear_parameteriser_from()
1. Define relationships between virtual parameters and model states
1. Call make_state_init_parameteriser() to create the StateInitParameteriser
1. Use the StateInitParameteriser in an optimisation or sensitivity analysis workflow

Use Cases

- Setting initial soil moisture as a fraction of maximum capacity (S0 = 0.9 * x1 for GR4J)
- Initialising routing stores as fractions of their capacities
- Calibrating initial states alongside model parameters
- Ensuring physically consistent initial conditions

Note

The scaling variables (e.g., x1, x3) must exist as parameters in the simulation's model. If they don't exist or have incompatible dimensions, an error will occur when the initialiser is applied during simulation execution.

Examples:

```
>>> # Use case: Set gr4j initial stores at simulation as a function of x1/x3 parameters.
>>> # and calibrate both model parameters and the virtual initial state parameters S0 and R0.
>>> # `some_other_parameteriser` may be a parameteriser for GR4J parameters x1 to x4.
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
>>> parameteriser = sp.concatenate_parameterisers(some_other_parameteriser, init_parameteriser)
>>> # Now use 'parameteriser' in an optimisation workflow to calibrate both model parameters and initial states.
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

Updates parameter properties for an existing parameteriser.

Modifies the bounds and values of parameters already defined in this parameteriser. Unlike from_dataframe() which creates a new parameteriser, this method updates the current one. All parameter names in the specs must already exist in the parameteriser.

Parameters:

- **`specs`** (`DataFrame`) – Parameter specifications with columns:
  - 'Name': Parameter name (must match existing parameters)
  - 'Min': New minimum feasible value
  - 'Max': New maximum feasible value
  - 'Value': New initial/current value All columns are required for each parameter being updated.

Raises:

- `Exception` – If any parameter name in specs doesn't exist in this parameteriser.

Note

This is useful for adjusting parameter bounds after initial creation, such as converting time-step-dependent parameters (e.g., GR4J x4 from hours to days) or tightening bounds based on prior calibration results.

Examples:

```
>>> # Create GR4J parameteriser with default hourly time step
>>> p = HypercubeParameteriser.from_dataframe('generic subareas', gr4j_hourly_spec)
>>> 
>>> # Convert x4 bounds from hours to days for daily time step
>>> p_x4_daily = pd.DataFrame({
...     'Name': ['x4'],
...     'Value': [1.0],
...     'Min': [0.25],
...     'Max': [10.0]  # 10 days instead of 240 hours
... })
>>> p.set_hypercube(p_x4_daily)
```

```
>>> # Update multiple parameters after preliminary calibration
>>> tighter_bounds = pd.DataFrame({
...     'Name': ['x1', 'x3'],
...     'Value': [450, 75],
...     'Min': [300, 50],
...     'Max': [600, 100]
... })
>>> p.set_hypercube(tighter_bounds)
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
subcatchment_parameteriser(subcatchment: Simulation) -> HypercubeParameteriser
```

Create a parameteriser that gets applied to a subset of a whole catchment

Parameters:

- **`subcatchment`** (`Simulation`) – the subcatchment, subset of a whole catchment, identifying which elements (subareas, nodes, links) will be parameterised by the new parameteriser. Other catchment elements are untouched.

Returns:

- **`HypercubeParameteriser`** ( `HypercubeParameteriser` ) – New parameteriser whose application is limited to the subcatchment.

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

### to_json_file

```
to_json_file(file_path: str) -> None
```

Save this parameteriser to a file with a JSON serialisation.

Parameters:

- **`file_path`** (`str`) – file path to save to

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

Enforces feasibility constraints on parameter combinations (e.g., Muskingum routing stability conditions).

Methods:

- **`add_parameter_to_hypercube`** – Add a parameter to a hypercube. Must be a type of object that is expandable, otherwise may raise an exception
- **`add_to_hypercube`** – Add entries to a hypercube. Must be a type of object that is expandable, otherwise may raise an exception.
- **`apply_sys_config`** – Apply a model configuration to a simulation
- **`as_dataframe`** – Convert this hypercube parameteriser to a pandas data frame representation
- **`backtransform`** – Get the parameteriser values in the untransformed space
- **`clone`** –
- **`create_parameter_sampler`** – Creates a sampler for this parameteriser
- **`filtered_parameters`** – Wrap this parameteriser in a filter that can hide some parameters from an optimiser.
- **`from_dataframe`** – Creates a parameteriser from a parameter specification.
- **`from_json_file`** – Load a parameteriser from a file with a JSON serialisation.
- **`make_state_init_parameteriser`** – Converts this parameteriser into a StateInitParameteriser.
- **`num_free_parameters`** – Number of free parameters in this hypercube parameteriser
- **`score_for_objective`** – Computes the value of an objective for this given set of parameters
- **`set_hypercube`** – Updates parameter properties for an existing parameteriser.
- **`set_max_parameter_value`** – Sets the value(s) of the upper bound of one or more parameter(s)
- **`set_min_parameter_value`** – Sets the value(s) of the lower bound of one or more parameter(s)
- **`set_parameter_definition`** – Sets the feasible range and value for a parameter
- **`set_parameter_value`** – Sets the value(s) of one or more parameter(s)
- **`subcatchment_parameteriser`** – Create a parameteriser that gets applied to a subset of a whole catchment
- **`supports_thread_safe_cloning`** – Is this parameteriser clonable as a deep copy, safe for multi-threading?
- **`to_json_file`** – Save this parameteriser to a file with a JSON serialisation.
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
from_dataframe(type: str = 'Generic subareas', definition: Optional[DataFrame] = None) -> HypercubeParameteriser
```

Creates a parameteriser from a parameter specification.

Factory method to create different types of parameterisers based on the 'type' string. The type determines which model elements (subareas, links, nodes) the parameters will be applied to.

Parameters:

- **`type`** (`str`, default: `'Generic subareas'` ) – Parameteriser type identifier (case-insensitive). Valid options:
  - 'generic' or 'generic subareas': Apply to all subareas (default)
  - 'links' or 'generic links': Apply to channel routing in links
  - 'nodes' or 'generic nodes': Apply to nodes
  - 'muskingum': Muskingum channel routing parameters
  - 'log-likelihood': Parameters for log-likelihood transformation (advanced) Defaults to "Generic subareas".
- **`definition`** (`DataFrame`, default: `None` ) – Parameter specifications with columns:
  - 'Name': Parameter name (e.g., 'x1', 'x2', 'alpha')
  - 'Min': Minimum feasible value
  - 'Max': Maximum feasible value
  - 'Value': Initial/current value If None, creates an empty parameteriser that can be populated later. Defaults to None.

Returns:

- **`HypercubeParameteriser`** ( `HypercubeParameteriser` ) – New parameteriser configured according to the type.

Examples:

```
>>> # Create GR4J parameters for subareas
>>> import pandas as pd
>>> from swift2.utils import c
>>> pspec = pd.DataFrame({
...     'Name': c('x1', 'x2', 'x3', 'x4'),
...     'Value': c(350, -0.5, 50, 2),
...     'Min': c(1, -27, 1, 1),
...     'Max': c(3000, 27, 1000, 240)
... })
>>> p = HypercubeParameteriser.from_dataframe('generic subareas', pspec)
```

```
>>> # Create link routing parameters
>>> link_spec = pd.DataFrame({
...     'Name': c('alpha', 'inverse_velocity'),
...     'Value': c(1, 1),
...     'Min': c(1e-3, 1e-3),
...     'Max': c(1e2, 1e2)
... })
>>> p_links = HypercubeParameteriser.from_dataframe('generic links', link_spec)
```

```
>>> # Create empty parameteriser to populate later
>>> p_empty = HypercubeParameteriser.from_dataframe('generic')
>>> p_empty.add_parameter_to_hypercube('x1', value=350, min=1, max=3000)
```

### from_json_file

```
from_json_file(file_path: str) -> HypercubeParameteriser
```

Load a parameteriser from a file with a JSON serialisation.

Parameters:

- **`file_path`** (`str`) – file path to load from

Returns:

- **`HypercubeParameteriser`** ( `HypercubeParameteriser` ) – loaded parameteriser

### make_state_init_parameteriser

```
make_state_init_parameteriser() -> StateInitParameteriser
```

Converts this parameteriser into a StateInitParameteriser.

Creates a StateInitParameteriser object that can be applied to simulations to set initial model states based on parameter values, as part of an optimisation process i.e. optimising some initial states. This is typically the subsequent step after defining scaled parameter relationships using ScalingParameteriser methods, and before inclusion in an optimisation workflow.

Returns:

- **`StateInitParameteriser`** ( `StateInitParameteriser` ) – Parameteriser with features to set model initial states via state initialisers,
- `StateInitParameteriser` – overriding the default simulation for model reset of initial states.

Typical Workflow

1. Create a ScalingParameteriser with linear_parameteriser() or linear_parameteriser_from()
1. Define relationships between virtual parameters and model states
1. Call make_state_init_parameteriser() to create the StateInitParameteriser
1. Use the StateInitParameteriser in an optimisation or sensitivity analysis workflow

Use Cases

- Setting initial soil moisture as a fraction of maximum capacity (S0 = 0.9 * x1 for GR4J)
- Initialising routing stores as fractions of their capacities
- Calibrating initial states alongside model parameters
- Ensuring physically consistent initial conditions

Note

The scaling variables (e.g., x1, x3) must exist as parameters in the simulation's model. If they don't exist or have incompatible dimensions, an error will occur when the initialiser is applied during simulation execution.

Examples:

```
>>> # Use case: Set gr4j initial stores at simulation as a function of x1/x3 parameters.
>>> # and calibrate both model parameters and the virtual initial state parameters S0 and R0.
>>> # `some_other_parameteriser` may be a parameteriser for GR4J parameters x1 to x4.
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
>>> parameteriser = sp.concatenate_parameterisers(some_other_parameteriser, init_parameteriser)
>>> # Now use 'parameteriser' in an optimisation workflow to calibrate both model parameters and initial states.
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

Updates parameter properties for an existing parameteriser.

Modifies the bounds and values of parameters already defined in this parameteriser. Unlike from_dataframe() which creates a new parameteriser, this method updates the current one. All parameter names in the specs must already exist in the parameteriser.

Parameters:

- **`specs`** (`DataFrame`) – Parameter specifications with columns:
  - 'Name': Parameter name (must match existing parameters)
  - 'Min': New minimum feasible value
  - 'Max': New maximum feasible value
  - 'Value': New initial/current value All columns are required for each parameter being updated.

Raises:

- `Exception` – If any parameter name in specs doesn't exist in this parameteriser.

Note

This is useful for adjusting parameter bounds after initial creation, such as converting time-step-dependent parameters (e.g., GR4J x4 from hours to days) or tightening bounds based on prior calibration results.

Examples:

```
>>> # Create GR4J parameteriser with default hourly time step
>>> p = HypercubeParameteriser.from_dataframe('generic subareas', gr4j_hourly_spec)
>>> 
>>> # Convert x4 bounds from hours to days for daily time step
>>> p_x4_daily = pd.DataFrame({
...     'Name': ['x4'],
...     'Value': [1.0],
...     'Min': [0.25],
...     'Max': [10.0]  # 10 days instead of 240 hours
... })
>>> p.set_hypercube(p_x4_daily)
```

```
>>> # Update multiple parameters after preliminary calibration
>>> tighter_bounds = pd.DataFrame({
...     'Name': ['x1', 'x3'],
...     'Value': [450, 75],
...     'Min': [300, 50],
...     'Max': [600, 100]
... })
>>> p.set_hypercube(tighter_bounds)
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
subcatchment_parameteriser(subcatchment: Simulation) -> HypercubeParameteriser
```

Create a parameteriser that gets applied to a subset of a whole catchment

Parameters:

- **`subcatchment`** (`Simulation`) – the subcatchment, subset of a whole catchment, identifying which elements (subareas, nodes, links) will be parameterised by the new parameteriser. Other catchment elements are untouched.

Returns:

- **`HypercubeParameteriser`** ( `HypercubeParameteriser` ) – New parameteriser whose application is limited to the subcatchment.

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

### to_json_file

```
to_json_file(file_path: str) -> None
```

Save this parameteriser to a file with a JSON serialisation.

Parameters:

- **`file_path`** (`str`) – file path to save to

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

Manages sequential ensemble forecast runs with regular forecast initialisation times and specified lead times.

Methods:

- **`exec_simulation`** – Executes the simulation over its configured time span.
- **`get_played_varnames`** – Gets all the names of states fed an input time series
- **`get_recorded_ensemble_forecast`** –
- **`get_recorded_varnames`** – Gets all the names of the recorded states
- **`get_simulation_span`** –
- **`record_ensemble_forecast_state`** –
- **`record_state`** – Records a time series of model state variable(s) during simulation execution.

### exec_simulation

```
exec_simulation(reset_initial_states: bool = True) -> None
```

Executes the simulation over its configured time span.

Runs the model forward in time from the simulation start to end date, using the configured time step. Input time series (set via play_input) are read and applied at each step, and any recorded state variables (set via record_state) are stored for later retrieval.

Parameters:

- **`reset_initial_states`** (`bool`, default: `True` ) – Whether to reset all model states to their initial values before starting the simulation. If True (default), any state initialisers configured on the simulation are also applied. Set to False to continue from current model states (useful for sequential simulation periods). Defaults to True.

Note

Before calling this method, ensure you have:

- Set the simulation span via set_simulation_span()
- Configured input time series via play_input() or play_inputs()
- Set up recording via record_state() for any outputs you need

Examples:

```
>>> # Standard simulation run
>>> simulation.set_simulation_span('2000-01-01', '2005-12-31')
>>> simulation.play_input(rainfall_ts, 'subarea.Subarea.P')
>>> simulation.record_state('Catchment.StreamflowRate')
>>> simulation.exec_simulation()
>>> flow = simulation.get_recorded()
```

```
>>> # Continue simulation without resetting states
>>> simulation.set_simulation_span('2006-01-01', '2010-12-31')
>>> simulation.exec_simulation(reset_initial_states=False)
```

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

Records a time series of model state variable(s) during simulation execution.

This method instructs the simulation to store values of specified state variables at each time step. Recorded data can be retrieved after execution using get_recorded(). By default, values are stored in memory, but can optionally be written to an external time series library.

Parameters:

- **`var_ids`** (`VecStr`, default: `CATCHMENT_FLOWRATE_VARID` ) – State variable identifier(s) to record. Common examples include 'Catchment.StreamflowRate' for outlet flow, 'subarea.{name}.runoff' for subarea runoff, or 'node.{name}.OutflowRate' for node outflows. Defaults to CATCHMENT_FLOWRATE_VARID (the main outlet streamflow).
- **`recording_provider`** (`TimeSeriesLibrary`, default: `None` ) – External time series library for storage. If None (default), values are stored in memory and retrieved via get_recorded().
- **`data_ids`** (`VecStr`, default: `None` ) – Identifier(s) for data in the recording_provider. Only used when recording_provider is specified. Must match the length of var_ids.

Raises:

- `ValueError` – If data_ids length doesn't match var_ids when recording_provider is specified.

Examples:

```
>>> # Record outlet streamflow (default)
>>> simulation.record_state()
```

```
>>> # Record multiple state variables
>>> simulation.record_state(['node.n1.OutflowRate', 'node.n2.OutflowRate'])
```

```
>>> # Record after simulation and retrieve
>>> simulation.record_state('subarea.Subarea.runoff')
>>> simulation.exec_simulation()
>>> runoff = simulation.get_recorded('subarea.Subarea.runoff')
```

## EnsembleSimulation

```
EnsembleSimulation(handle: CffiData, release_native: Callable[[CffiData], None], type_id: Optional[str] = None, prior_ref_count: int = 0)
```

Bases: `DeletableCffiNativeHandle`

UNDER CONSTRUCTION - Manages ensemble simulations over replicate inputs series, allowing for setup, state recording, and retrieval of simulation spans.

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

Orchestrates multi-stage calibration where hydrologic parameters and ERRIS error model parameters are estimated sequentially.

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

Shows only a subset of parameters to optimizers while applying all parameters to simulations, used in log-likelihood calibration.

Methods:

- **`add_parameter_to_hypercube`** – Add a parameter to a hypercube. Must be a type of object that is expandable, otherwise may raise an exception
- **`add_to_hypercube`** – Add entries to a hypercube. Must be a type of object that is expandable, otherwise may raise an exception.
- **`apply_sys_config`** – Apply a model configuration to a simulation
- **`as_dataframe`** – Convert this hypercube parameteriser to a pandas data frame representation
- **`backtransform`** – Get the parameteriser values in the untransformed space
- **`clone`** –
- **`create_parameter_sampler`** – Creates a sampler for this parameteriser
- **`filtered_parameters`** – Wrap this parameteriser in a filter that can hide some parameters from an optimiser.
- **`from_dataframe`** – Creates a parameteriser from a parameter specification.
- **`from_json_file`** – Load a parameteriser from a file with a JSON serialisation.
- **`hide_parameters`** – Hides parameters from optimisers while still applying them to simulations.
- **`make_state_init_parameteriser`** – Converts this parameteriser into a StateInitParameteriser.
- **`num_free_parameters`** – Number of free parameters in this hypercube parameteriser
- **`score_for_objective`** – Computes the value of an objective for this given set of parameters
- **`set_hypercube`** – Updates parameter properties for an existing parameteriser.
- **`set_max_parameter_value`** – Sets the value(s) of the upper bound of one or more parameter(s)
- **`set_min_parameter_value`** – Sets the value(s) of the lower bound of one or more parameter(s)
- **`set_parameter_definition`** – Sets the feasible range and value for a parameter
- **`set_parameter_value`** – Sets the value(s) of one or more parameter(s)
- **`show_parameters`** – Show some parameters (from the outside e.g. optimisers) in a filter parameteriser
- **`subcatchment_parameteriser`** – Create a parameteriser that gets applied to a subset of a whole catchment
- **`supports_thread_safe_cloning`** – Is this parameteriser clonable as a deep copy, safe for multi-threading?
- **`to_json_file`** – Save this parameteriser to a file with a JSON serialisation.
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
from_dataframe(type: str = 'Generic subareas', definition: Optional[DataFrame] = None) -> HypercubeParameteriser
```

Creates a parameteriser from a parameter specification.

Factory method to create different types of parameterisers based on the 'type' string. The type determines which model elements (subareas, links, nodes) the parameters will be applied to.

Parameters:

- **`type`** (`str`, default: `'Generic subareas'` ) – Parameteriser type identifier (case-insensitive). Valid options:
  - 'generic' or 'generic subareas': Apply to all subareas (default)
  - 'links' or 'generic links': Apply to channel routing in links
  - 'nodes' or 'generic nodes': Apply to nodes
  - 'muskingum': Muskingum channel routing parameters
  - 'log-likelihood': Parameters for log-likelihood transformation (advanced) Defaults to "Generic subareas".
- **`definition`** (`DataFrame`, default: `None` ) – Parameter specifications with columns:
  - 'Name': Parameter name (e.g., 'x1', 'x2', 'alpha')
  - 'Min': Minimum feasible value
  - 'Max': Maximum feasible value
  - 'Value': Initial/current value If None, creates an empty parameteriser that can be populated later. Defaults to None.

Returns:

- **`HypercubeParameteriser`** ( `HypercubeParameteriser` ) – New parameteriser configured according to the type.

Examples:

```
>>> # Create GR4J parameters for subareas
>>> import pandas as pd
>>> from swift2.utils import c
>>> pspec = pd.DataFrame({
...     'Name': c('x1', 'x2', 'x3', 'x4'),
...     'Value': c(350, -0.5, 50, 2),
...     'Min': c(1, -27, 1, 1),
...     'Max': c(3000, 27, 1000, 240)
... })
>>> p = HypercubeParameteriser.from_dataframe('generic subareas', pspec)
```

```
>>> # Create link routing parameters
>>> link_spec = pd.DataFrame({
...     'Name': c('alpha', 'inverse_velocity'),
...     'Value': c(1, 1),
...     'Min': c(1e-3, 1e-3),
...     'Max': c(1e2, 1e2)
... })
>>> p_links = HypercubeParameteriser.from_dataframe('generic links', link_spec)
```

```
>>> # Create empty parameteriser to populate later
>>> p_empty = HypercubeParameteriser.from_dataframe('generic')
>>> p_empty.add_parameter_to_hypercube('x1', value=350, min=1, max=3000)
```

### from_json_file

```
from_json_file(file_path: str) -> HypercubeParameteriser
```

Load a parameteriser from a file with a JSON serialisation.

Parameters:

- **`file_path`** (`str`) – file path to load from

Returns:

- **`HypercubeParameteriser`** ( `HypercubeParameteriser` ) – loaded parameteriser

### hide_parameters

```
hide_parameters(patterns, regex=False, starts_with=False, strict=False)
```

Hides parameters from optimisers while still applying them to simulations.

This creates a filter where certain parameters are invisible to the optimisation algorithm but are still applied when the parameteriser configures a simulation. Useful in log-likelihood calibration where transformation parameters (b, m, s, a) should be fixed while hydrologic parameters are optimised.

Parameters:

- **`patterns`** (`str or sequence of str`) – One or more patterns to match parameter names for hiding. Matching behaviour depends on regex and starts_with flags.
- **`regex`** (`bool`, default: `False` ) – If True, patterns are treated as regular expressions. Defaults to False.
- **`starts_with`** (`bool`, default: `False` ) – If True (and regex is False), patterns match parameter names that start with the pattern string. Defaults to False.
- **`strict`** (`bool`, default: `False` ) – Only used when regex=False and starts_with=False. If True, raises an error if any pattern has no exact match in the parameters. Useful for catching typos. Defaults to False.

Note

Hidden parameters retain their current values when applied to simulations. To change hidden parameter values, use set_parameter_value() on the underlying parameteriser before wrapping it in the filter.

Examples:

```
>>> # Hide transformation parameters in log-likelihood calibration
>>> p = HypercubeParameteriser.from_dataframe('generic', all_params)
>>> p_filtered = p.filtered_parameters()
>>> p_filtered.hide_parameters(['b', 'm', 's', 'a'], strict=True)
>>> # Now optimiser only sees hydrologic parameters, but all are applied
```

```
>>> # Hide all parameters starting with 'log_'
>>> p_filtered.hide_parameters(['log_'], starts_with=True)
```

```
>>> # Hide using regex pattern
>>> p_filtered.hide_parameters([r'x[1-3]'], regex=True)  # Hides x1, x2, x3
```

### make_state_init_parameteriser

```
make_state_init_parameteriser() -> StateInitParameteriser
```

Converts this parameteriser into a StateInitParameteriser.

Creates a StateInitParameteriser object that can be applied to simulations to set initial model states based on parameter values, as part of an optimisation process i.e. optimising some initial states. This is typically the subsequent step after defining scaled parameter relationships using ScalingParameteriser methods, and before inclusion in an optimisation workflow.

Returns:

- **`StateInitParameteriser`** ( `StateInitParameteriser` ) – Parameteriser with features to set model initial states via state initialisers,
- `StateInitParameteriser` – overriding the default simulation for model reset of initial states.

Typical Workflow

1. Create a ScalingParameteriser with linear_parameteriser() or linear_parameteriser_from()
1. Define relationships between virtual parameters and model states
1. Call make_state_init_parameteriser() to create the StateInitParameteriser
1. Use the StateInitParameteriser in an optimisation or sensitivity analysis workflow

Use Cases

- Setting initial soil moisture as a fraction of maximum capacity (S0 = 0.9 * x1 for GR4J)
- Initialising routing stores as fractions of their capacities
- Calibrating initial states alongside model parameters
- Ensuring physically consistent initial conditions

Note

The scaling variables (e.g., x1, x3) must exist as parameters in the simulation's model. If they don't exist or have incompatible dimensions, an error will occur when the initialiser is applied during simulation execution.

Examples:

```
>>> # Use case: Set gr4j initial stores at simulation as a function of x1/x3 parameters.
>>> # and calibrate both model parameters and the virtual initial state parameters S0 and R0.
>>> # `some_other_parameteriser` may be a parameteriser for GR4J parameters x1 to x4.
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
>>> parameteriser = sp.concatenate_parameterisers(some_other_parameteriser, init_parameteriser)
>>> # Now use 'parameteriser' in an optimisation workflow to calibrate both model parameters and initial states.
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

Updates parameter properties for an existing parameteriser.

Modifies the bounds and values of parameters already defined in this parameteriser. Unlike from_dataframe() which creates a new parameteriser, this method updates the current one. All parameter names in the specs must already exist in the parameteriser.

Parameters:

- **`specs`** (`DataFrame`) – Parameter specifications with columns:
  - 'Name': Parameter name (must match existing parameters)
  - 'Min': New minimum feasible value
  - 'Max': New maximum feasible value
  - 'Value': New initial/current value All columns are required for each parameter being updated.

Raises:

- `Exception` – If any parameter name in specs doesn't exist in this parameteriser.

Note

This is useful for adjusting parameter bounds after initial creation, such as converting time-step-dependent parameters (e.g., GR4J x4 from hours to days) or tightening bounds based on prior calibration results.

Examples:

```
>>> # Create GR4J parameteriser with default hourly time step
>>> p = HypercubeParameteriser.from_dataframe('generic subareas', gr4j_hourly_spec)
>>> 
>>> # Convert x4 bounds from hours to days for daily time step
>>> p_x4_daily = pd.DataFrame({
...     'Name': ['x4'],
...     'Value': [1.0],
...     'Min': [0.25],
...     'Max': [10.0]  # 10 days instead of 240 hours
... })
>>> p.set_hypercube(p_x4_daily)
```

```
>>> # Update multiple parameters after preliminary calibration
>>> tighter_bounds = pd.DataFrame({
...     'Name': ['x1', 'x3'],
...     'Value': [450, 75],
...     'Min': [300, 50],
...     'Max': [600, 100]
... })
>>> p.set_hypercube(tighter_bounds)
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
subcatchment_parameteriser(subcatchment: Simulation) -> HypercubeParameteriser
```

Create a parameteriser that gets applied to a subset of a whole catchment

Parameters:

- **`subcatchment`** (`Simulation`) – the subcatchment, subset of a whole catchment, identifying which elements (subareas, nodes, links) will be parameterised by the new parameteriser. Other catchment elements are untouched.

Returns:

- **`HypercubeParameteriser`** ( `HypercubeParameteriser` ) – New parameteriser whose application is limited to the subcatchment.

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

### to_json_file

```
to_json_file(file_path: str) -> None
```

Save this parameteriser to a file with a JSON serialisation.

Parameters:

- **`file_path`** (`str`) – file path to save to

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

Manages parameters for multisite multi-objective calibration where different statistics are computed at multiple locations.

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
- **`from_dataframe`** – Creates a parameteriser from a parameter specification.
- **`from_json_file`** – Load a parameteriser from a file with a JSON serialisation.
- **`make_state_init_parameteriser`** – Converts this parameteriser into a StateInitParameteriser.
- **`num_free_parameters`** – Number of free parameters in this hypercube parameteriser
- **`score_for_objective`** – Computes the value of an objective for this given set of parameters
- **`set_hypercube`** – Updates parameter properties for an existing parameteriser.
- **`set_max_parameter_value`** – Sets the value(s) of the upper bound of one or more parameter(s)
- **`set_min_parameter_value`** – Sets the value(s) of the lower bound of one or more parameter(s)
- **`set_parameter_definition`** – Sets the feasible range and value for a parameter
- **`set_parameter_value`** – Sets the value(s) of one or more parameter(s)
- **`subcatchment_parameteriser`** – Create a parameteriser that gets applied to a subset of a whole catchment
- **`supports_thread_safe_cloning`** – Is this parameteriser clonable as a deep copy, safe for multi-threading?
- **`to_json_file`** – Save this parameteriser to a file with a JSON serialisation.
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
from_dataframe(type: str = 'Generic subareas', definition: Optional[DataFrame] = None) -> HypercubeParameteriser
```

Creates a parameteriser from a parameter specification.

Factory method to create different types of parameterisers based on the 'type' string. The type determines which model elements (subareas, links, nodes) the parameters will be applied to.

Parameters:

- **`type`** (`str`, default: `'Generic subareas'` ) – Parameteriser type identifier (case-insensitive). Valid options:
  - 'generic' or 'generic subareas': Apply to all subareas (default)
  - 'links' or 'generic links': Apply to channel routing in links
  - 'nodes' or 'generic nodes': Apply to nodes
  - 'muskingum': Muskingum channel routing parameters
  - 'log-likelihood': Parameters for log-likelihood transformation (advanced) Defaults to "Generic subareas".
- **`definition`** (`DataFrame`, default: `None` ) – Parameter specifications with columns:
  - 'Name': Parameter name (e.g., 'x1', 'x2', 'alpha')
  - 'Min': Minimum feasible value
  - 'Max': Maximum feasible value
  - 'Value': Initial/current value If None, creates an empty parameteriser that can be populated later. Defaults to None.

Returns:

- **`HypercubeParameteriser`** ( `HypercubeParameteriser` ) – New parameteriser configured according to the type.

Examples:

```
>>> # Create GR4J parameters for subareas
>>> import pandas as pd
>>> from swift2.utils import c
>>> pspec = pd.DataFrame({
...     'Name': c('x1', 'x2', 'x3', 'x4'),
...     'Value': c(350, -0.5, 50, 2),
...     'Min': c(1, -27, 1, 1),
...     'Max': c(3000, 27, 1000, 240)
... })
>>> p = HypercubeParameteriser.from_dataframe('generic subareas', pspec)
```

```
>>> # Create link routing parameters
>>> link_spec = pd.DataFrame({
...     'Name': c('alpha', 'inverse_velocity'),
...     'Value': c(1, 1),
...     'Min': c(1e-3, 1e-3),
...     'Max': c(1e2, 1e2)
... })
>>> p_links = HypercubeParameteriser.from_dataframe('generic links', link_spec)
```

```
>>> # Create empty parameteriser to populate later
>>> p_empty = HypercubeParameteriser.from_dataframe('generic')
>>> p_empty.add_parameter_to_hypercube('x1', value=350, min=1, max=3000)
```

### from_json_file

```
from_json_file(file_path: str) -> HypercubeParameteriser
```

Load a parameteriser from a file with a JSON serialisation.

Parameters:

- **`file_path`** (`str`) – file path to load from

Returns:

- **`HypercubeParameteriser`** ( `HypercubeParameteriser` ) – loaded parameteriser

### make_state_init_parameteriser

```
make_state_init_parameteriser() -> StateInitParameteriser
```

Converts this parameteriser into a StateInitParameteriser.

Creates a StateInitParameteriser object that can be applied to simulations to set initial model states based on parameter values, as part of an optimisation process i.e. optimising some initial states. This is typically the subsequent step after defining scaled parameter relationships using ScalingParameteriser methods, and before inclusion in an optimisation workflow.

Returns:

- **`StateInitParameteriser`** ( `StateInitParameteriser` ) – Parameteriser with features to set model initial states via state initialisers,
- `StateInitParameteriser` – overriding the default simulation for model reset of initial states.

Typical Workflow

1. Create a ScalingParameteriser with linear_parameteriser() or linear_parameteriser_from()
1. Define relationships between virtual parameters and model states
1. Call make_state_init_parameteriser() to create the StateInitParameteriser
1. Use the StateInitParameteriser in an optimisation or sensitivity analysis workflow

Use Cases

- Setting initial soil moisture as a fraction of maximum capacity (S0 = 0.9 * x1 for GR4J)
- Initialising routing stores as fractions of their capacities
- Calibrating initial states alongside model parameters
- Ensuring physically consistent initial conditions

Note

The scaling variables (e.g., x1, x3) must exist as parameters in the simulation's model. If they don't exist or have incompatible dimensions, an error will occur when the initialiser is applied during simulation execution.

Examples:

```
>>> # Use case: Set gr4j initial stores at simulation as a function of x1/x3 parameters.
>>> # and calibrate both model parameters and the virtual initial state parameters S0 and R0.
>>> # `some_other_parameteriser` may be a parameteriser for GR4J parameters x1 to x4.
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
>>> parameteriser = sp.concatenate_parameterisers(some_other_parameteriser, init_parameteriser)
>>> # Now use 'parameteriser' in an optimisation workflow to calibrate both model parameters and initial states.
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

Updates parameter properties for an existing parameteriser.

Modifies the bounds and values of parameters already defined in this parameteriser. Unlike from_dataframe() which creates a new parameteriser, this method updates the current one. All parameter names in the specs must already exist in the parameteriser.

Parameters:

- **`specs`** (`DataFrame`) – Parameter specifications with columns:
  - 'Name': Parameter name (must match existing parameters)
  - 'Min': New minimum feasible value
  - 'Max': New maximum feasible value
  - 'Value': New initial/current value All columns are required for each parameter being updated.

Raises:

- `Exception` – If any parameter name in specs doesn't exist in this parameteriser.

Note

This is useful for adjusting parameter bounds after initial creation, such as converting time-step-dependent parameters (e.g., GR4J x4 from hours to days) or tightening bounds based on prior calibration results.

Examples:

```
>>> # Create GR4J parameteriser with default hourly time step
>>> p = HypercubeParameteriser.from_dataframe('generic subareas', gr4j_hourly_spec)
>>> 
>>> # Convert x4 bounds from hours to days for daily time step
>>> p_x4_daily = pd.DataFrame({
...     'Name': ['x4'],
...     'Value': [1.0],
...     'Min': [0.25],
...     'Max': [10.0]  # 10 days instead of 240 hours
... })
>>> p.set_hypercube(p_x4_daily)
```

```
>>> # Update multiple parameters after preliminary calibration
>>> tighter_bounds = pd.DataFrame({
...     'Name': ['x1', 'x3'],
...     'Value': [450, 75],
...     'Min': [300, 50],
...     'Max': [600, 100]
... })
>>> p.set_hypercube(tighter_bounds)
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
subcatchment_parameteriser(subcatchment: Simulation) -> HypercubeParameteriser
```

Create a parameteriser that gets applied to a subset of a whole catchment

Parameters:

- **`subcatchment`** (`Simulation`) – the subcatchment, subset of a whole catchment, identifying which elements (subareas, nodes, links) will be parameterised by the new parameteriser. Other catchment elements are untouched.

Returns:

- **`HypercubeParameteriser`** ( `HypercubeParameteriser` ) – New parameteriser whose application is limited to the subcatchment.

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

### to_json_file

```
to_json_file(file_path: str) -> None
```

Save this parameteriser to a file with a JSON serialisation.

Parameters:

- **`file_path`** (`str`) – file path to save to

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

Defines parameter bounds, values, and names as a hypercube for optimisation and sensitivity analysis.

Methods:

- **`add_parameter_to_hypercube`** – Add a parameter to a hypercube. Must be a type of object that is expandable, otherwise may raise an exception
- **`add_to_hypercube`** – Add entries to a hypercube. Must be a type of object that is expandable, otherwise may raise an exception.
- **`apply_sys_config`** – Apply a model configuration to a simulation
- **`as_dataframe`** – Convert this hypercube parameteriser to a pandas data frame representation
- **`backtransform`** – Get the parameteriser values in the untransformed space
- **`clone`** –
- **`create_parameter_sampler`** – Creates a sampler for this parameteriser
- **`filtered_parameters`** – Wrap this parameteriser in a filter that can hide some parameters from an optimiser.
- **`from_dataframe`** – Creates a parameteriser from a parameter specification.
- **`from_json_file`** – Load a parameteriser from a file with a JSON serialisation.
- **`make_state_init_parameteriser`** – Converts this parameteriser into a StateInitParameteriser.
- **`num_free_parameters`** – Number of free parameters in this hypercube parameteriser
- **`score_for_objective`** – Computes the value of an objective for this given set of parameters
- **`set_hypercube`** – Updates parameter properties for an existing parameteriser.
- **`set_max_parameter_value`** – Sets the value(s) of the upper bound of one or more parameter(s)
- **`set_min_parameter_value`** – Sets the value(s) of the lower bound of one or more parameter(s)
- **`set_parameter_definition`** – Sets the feasible range and value for a parameter
- **`set_parameter_value`** – Sets the value(s) of one or more parameter(s)
- **`subcatchment_parameteriser`** – Create a parameteriser that gets applied to a subset of a whole catchment
- **`supports_thread_safe_cloning`** – Is this parameteriser clonable as a deep copy, safe for multi-threading?
- **`to_json_file`** – Save this parameteriser to a file with a JSON serialisation.
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
from_dataframe(type: str = 'Generic subareas', definition: Optional[DataFrame] = None) -> HypercubeParameteriser
```

Creates a parameteriser from a parameter specification.

Factory method to create different types of parameterisers based on the 'type' string. The type determines which model elements (subareas, links, nodes) the parameters will be applied to.

Parameters:

- **`type`** (`str`, default: `'Generic subareas'` ) – Parameteriser type identifier (case-insensitive). Valid options:
  - 'generic' or 'generic subareas': Apply to all subareas (default)
  - 'links' or 'generic links': Apply to channel routing in links
  - 'nodes' or 'generic nodes': Apply to nodes
  - 'muskingum': Muskingum channel routing parameters
  - 'log-likelihood': Parameters for log-likelihood transformation (advanced) Defaults to "Generic subareas".
- **`definition`** (`DataFrame`, default: `None` ) – Parameter specifications with columns:
  - 'Name': Parameter name (e.g., 'x1', 'x2', 'alpha')
  - 'Min': Minimum feasible value
  - 'Max': Maximum feasible value
  - 'Value': Initial/current value If None, creates an empty parameteriser that can be populated later. Defaults to None.

Returns:

- **`HypercubeParameteriser`** ( `HypercubeParameteriser` ) – New parameteriser configured according to the type.

Examples:

```
>>> # Create GR4J parameters for subareas
>>> import pandas as pd
>>> from swift2.utils import c
>>> pspec = pd.DataFrame({
...     'Name': c('x1', 'x2', 'x3', 'x4'),
...     'Value': c(350, -0.5, 50, 2),
...     'Min': c(1, -27, 1, 1),
...     'Max': c(3000, 27, 1000, 240)
... })
>>> p = HypercubeParameteriser.from_dataframe('generic subareas', pspec)
```

```
>>> # Create link routing parameters
>>> link_spec = pd.DataFrame({
...     'Name': c('alpha', 'inverse_velocity'),
...     'Value': c(1, 1),
...     'Min': c(1e-3, 1e-3),
...     'Max': c(1e2, 1e2)
... })
>>> p_links = HypercubeParameteriser.from_dataframe('generic links', link_spec)
```

```
>>> # Create empty parameteriser to populate later
>>> p_empty = HypercubeParameteriser.from_dataframe('generic')
>>> p_empty.add_parameter_to_hypercube('x1', value=350, min=1, max=3000)
```

### from_json_file

```
from_json_file(file_path: str) -> HypercubeParameteriser
```

Load a parameteriser from a file with a JSON serialisation.

Parameters:

- **`file_path`** (`str`) – file path to load from

Returns:

- **`HypercubeParameteriser`** ( `HypercubeParameteriser` ) – loaded parameteriser

### make_state_init_parameteriser

```
make_state_init_parameteriser() -> StateInitParameteriser
```

Converts this parameteriser into a StateInitParameteriser.

Creates a StateInitParameteriser object that can be applied to simulations to set initial model states based on parameter values, as part of an optimisation process i.e. optimising some initial states. This is typically the subsequent step after defining scaled parameter relationships using ScalingParameteriser methods, and before inclusion in an optimisation workflow.

Returns:

- **`StateInitParameteriser`** ( `StateInitParameteriser` ) – Parameteriser with features to set model initial states via state initialisers,
- `StateInitParameteriser` – overriding the default simulation for model reset of initial states.

Typical Workflow

1. Create a ScalingParameteriser with linear_parameteriser() or linear_parameteriser_from()
1. Define relationships between virtual parameters and model states
1. Call make_state_init_parameteriser() to create the StateInitParameteriser
1. Use the StateInitParameteriser in an optimisation or sensitivity analysis workflow

Use Cases

- Setting initial soil moisture as a fraction of maximum capacity (S0 = 0.9 * x1 for GR4J)
- Initialising routing stores as fractions of their capacities
- Calibrating initial states alongside model parameters
- Ensuring physically consistent initial conditions

Note

The scaling variables (e.g., x1, x3) must exist as parameters in the simulation's model. If they don't exist or have incompatible dimensions, an error will occur when the initialiser is applied during simulation execution.

Examples:

```
>>> # Use case: Set gr4j initial stores at simulation as a function of x1/x3 parameters.
>>> # and calibrate both model parameters and the virtual initial state parameters S0 and R0.
>>> # `some_other_parameteriser` may be a parameteriser for GR4J parameters x1 to x4.
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
>>> parameteriser = sp.concatenate_parameterisers(some_other_parameteriser, init_parameteriser)
>>> # Now use 'parameteriser' in an optimisation workflow to calibrate both model parameters and initial states.
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

Updates parameter properties for an existing parameteriser.

Modifies the bounds and values of parameters already defined in this parameteriser. Unlike from_dataframe() which creates a new parameteriser, this method updates the current one. All parameter names in the specs must already exist in the parameteriser.

Parameters:

- **`specs`** (`DataFrame`) – Parameter specifications with columns:
  - 'Name': Parameter name (must match existing parameters)
  - 'Min': New minimum feasible value
  - 'Max': New maximum feasible value
  - 'Value': New initial/current value All columns are required for each parameter being updated.

Raises:

- `Exception` – If any parameter name in specs doesn't exist in this parameteriser.

Note

This is useful for adjusting parameter bounds after initial creation, such as converting time-step-dependent parameters (e.g., GR4J x4 from hours to days) or tightening bounds based on prior calibration results.

Examples:

```
>>> # Create GR4J parameteriser with default hourly time step
>>> p = HypercubeParameteriser.from_dataframe('generic subareas', gr4j_hourly_spec)
>>> 
>>> # Convert x4 bounds from hours to days for daily time step
>>> p_x4_daily = pd.DataFrame({
...     'Name': ['x4'],
...     'Value': [1.0],
...     'Min': [0.25],
...     'Max': [10.0]  # 10 days instead of 240 hours
... })
>>> p.set_hypercube(p_x4_daily)
```

```
>>> # Update multiple parameters after preliminary calibration
>>> tighter_bounds = pd.DataFrame({
...     'Name': ['x1', 'x3'],
...     'Value': [450, 75],
...     'Min': [300, 50],
...     'Max': [600, 100]
... })
>>> p.set_hypercube(tighter_bounds)
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
subcatchment_parameteriser(subcatchment: Simulation) -> HypercubeParameteriser
```

Create a parameteriser that gets applied to a subset of a whole catchment

Parameters:

- **`subcatchment`** (`Simulation`) – the subcatchment, subset of a whole catchment, identifying which elements (subareas, nodes, links) will be parameterised by the new parameteriser. Other catchment elements are untouched.

Returns:

- **`HypercubeParameteriser`** ( `HypercubeParameteriser` ) – New parameteriser whose application is limited to the subcatchment.

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

### to_json_file

```
to_json_file(file_path: str) -> None
```

Save this parameteriser to a file with a JSON serialisation.

Parameters:

- **`file_path`** (`str`) – file path to save to

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

Performs staged calibration using the MAERRIS error correction approach with separate hydrologic and error model phases.

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

Captures a snapshot of all model states at a point in time for later restoration or analysis.

## ObjectiveEvaluator

```
ObjectiveEvaluator(handle: CffiData, release_native: Callable[[CffiData], None], type_id: Optional[str] = None, prior_ref_count: int = 0)
```

Bases: `DeletableCffiNativeHandle`

Calculates goodness-of-fit statistics by comparing simulated outputs to observations over a specified period.

Methods:

- **`create_composite_objective`** – Creates a composite objective, weighted average of several objectives
- **`create_sce_optim_swift`** – Creates an SCE-UA optimiser for this objective.
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

Creates an SCE-UA optimiser for this objective.

Builds a Shuffled Complex Evolution optimiser configured to minimise (or maximise) this objective. The optimiser will search the parameter space defined by the parameteriser to find optimal values.

Parameters:

- **`termination_criterion`** (`Optional[SceTerminationCondition]`, default: `None` ) – Stopping condition for the optimiser. If None, creates a default criterion based on relative standard deviation of the objective across complexes. See get_marginal_termination() or get_max_runtime_termination() for alternatives. Defaults to None.
- **`sce_params`** (`Optional[Dict[str, float]]`, default: `None` ) – SCE algorithm hyperparameters controlling complex size, evolution strategy, etc. If None, uses get_default_sce_parameters(). Keys typically include 'NumShuffle', 'NumComplexes', etc. Defaults to None.
- **`population_initialiser`** (`Optional[Union[CandidateFactorySeed, HypercubeParameteriser]]`, default: `None` ) – Defines how to generate the initial parameter population. Can be:
  - A CandidateFactorySeed for custom sampling (e.g., Latin hypercube)
  - A HypercubeParameteriser, in which case uniform random sampling is used
  - None raises an error (required argument for historical reasons) Defaults to None.

Returns:

- **`Optimiser`** ( `Optimiser` ) – Configured SCE-UA optimiser ready to run via execute_optimisation().

Note

The interaction between these parameters matters:

- termination_criterion controls when to stop
- sce_params controls how the algorithm explores parameter space
- population_initialiser controls where the algorithm starts

For most users, providing just the population_initialiser (the parameter space) is sufficient.

Examples:

```
>>> # Basic calibration with default settings
>>> objective = simulation.create_objective('Catchment.StreamflowRate', 
...                                         observed, 'NSE', start, end)
>>> parameteriser = HypercubeParameteriser.from_dataframe('generic', param_spec)
>>> optimiser = objective.create_sce_optim_swift(
...     population_initialiser=parameteriser
... )
>>> optimiser.execute_optimisation()
```

```
>>> # Calibration with wall-time limit
>>> from swift2.parameteriser import get_max_runtime_termination
>>> term_crit = get_max_runtime_termination(max_hours=2.0)
>>> optimiser = objective.create_sce_optim_swift(
...     termination_criterion=term_crit,
...     population_initialiser=parameteriser
... )
```

```
>>> # Calibration with custom SCE parameters
>>> sce_config = {'NumShuffle': 20, 'NumComplexes': 5}
>>> optimiser = objective.create_sce_optim_swift(
...     sce_params=sce_config,
...     population_initialiser=parameteriser
... )
```

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

Holds the results of an objective evaluation including score values and the associated parameter set.

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

Executes parameter estimation algorithms (typically SCE-UA) to find optimal parameter values for a given objective.

Methods:

- **`execute_optimisation`** – Executes the parameter optimisation process.
- **`extract_optimisation_log`** – Extract the logger from a parameter extimator (optimiser or related)
- **`get_default_maximum_threads`** –
- **`set_calibration_logger`** – Set the type of calibration logger to use
- **`set_default_maximum_threads`** –
- **`set_maximum_threads`** – Set the maximum number of threads (compute cores) to use in the optimisation, if possible. -1 means "as many as available".
- **`set_maximum_threads_free_cores`** – Set the maximum number of threads (compute cores) to use in the optimisation, such that at least n_free_cores are left for other tasks, if feasible given hardware constraints.

### execute_optimisation

```
execute_optimisation() -> ObjectiveScores
```

Executes the parameter optimisation process.

Runs the configured optimisation algorithm (typically SCE-UA) to find optimal parameter values for the associated objective. The optimiser iteratively evaluates the objective function, evolving the parameter population towards better solutions until the termination criterion is met.

Returns:

- **`ObjectiveScores`** ( `ObjectiveScores` ) – The best parameter set found and its associated objective score(s). Access the optimal parameters via result.parameteriser and scores via result.scores.

Note

- This method can take significant time depending on the termination criterion and number of parameters.
- Progress is logged if set_calibration_logger() was called beforehand.
- The optimisation log can be extracted after completion using extract_optimisation_log() for detailed analysis of the search process.
- For multi-core systems, you can set thread count via set_maximum_threads() before calling this. By default, n_core-1 is used at most, to leave one free for user interactions.

Side Effects

- Runs the simulation many times (typically hundreds to thousands of evaluations)
- Modifies the simulation's parameter values during search
- Records detailed optimisation history if logging is enabled

Examples:

```
>>> # Basic optimisation
>>> objective = simulation.create_objective('Catchment.StreamflowRate',
...                                         observed, 'NSE', start, end)
>>> parameteriser = HypercubeParameteriser.from_dataframe('generic', param_spec)
>>> optimiser = objective.create_sce_optim_swift(population_initialiser=parameteriser)
>>> best_params = optimiser.execute_optimisation()
>>> print(f"Best NSE: {best_params.scores['NSE']}")
>>> print(f"Optimal parameters:\n{best_params.parameteriser}")
```

```
>>> # With logging for post-analysis
>>> optimiser.set_calibration_logger()
>>> best_params = optimiser.execute_optimisation()
>>> log = optimiser.extract_optimisation_log()
>>> log.facet_plot('x1', facet_category='Message')  # Visualise parameter evolution
```

```
>>> # Apply best parameters and run validation
>>> best_params.apply_sys_config(simulation)
>>> simulation.set_simulation_span(valid_start, valid_end)
>>> simulation.exec_simulation()
>>> validation_flow = simulation.get_recorded()
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

Base class for objects that define and apply parameter configurations to simulations.

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
subcatchment_parameteriser(subcatchment: Simulation) -> HypercubeParameteriser
```

Create a parameteriser that gets applied to a subset of a whole catchment

Parameters:

- **`subcatchment`** (`Simulation`) – the subcatchment, subset of a whole catchment, identifying which elements (subareas, nodes, links) will be parameterised by the new parameteriser. Other catchment elements are untouched.

Returns:

- **`HypercubeParameteriser`** ( `HypercubeParameteriser` ) – New parameteriser whose application is limited to the subcatchment.

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

Defines linear relationships between virtual parameters and model states (e.g., initial storage as fraction of capacity).

Methods:

- **`add_linear_scaled_parameter`** – Adds a single linearly scaled parameter relationship.
- **`add_parameter_to_hypercube`** – Add a parameter to a hypercube. Must be a type of object that is expandable, otherwise may raise an exception
- **`add_to_hypercube`** – Add entries to a hypercube. Must be a type of object that is expandable, otherwise may raise an exception.
- **`add_transform`** – Adds a mathematical transformation to a parameter for optimisation in transformed space.
- **`apply_sys_config`** – Apply a model configuration to a simulation
- **`as_dataframe`** – Convert this hypercube parameteriser to a pandas data frame representation
- **`backtransform`** – Get the parameteriser values in the untransformed space
- **`clone`** –
- **`create_parameter_sampler`** – Creates a sampler for this parameteriser
- **`filtered_parameters`** – Wrap this parameteriser in a filter that can hide some parameters from an optimiser.
- **`from_dataframe`** – Creates a parameteriser from a parameter specification.
- **`from_json_file`** – Load a parameteriser from a file with a JSON serialisation.
- **`linear_parameteriser`** – Create a scaled linear parameteriser, tying by a linear transformation a (resp several) model state to a (resp several) parameter values
- **`linear_parameteriser_from`** – Create a scaled linear parameteriser, tying by a linear transformation a (resp several) model state to a (resp several) parameter values
- **`make_state_init_parameteriser`** – Converts this parameteriser into a StateInitParameteriser.
- **`num_free_parameters`** – Number of free parameters in this hypercube parameteriser
- **`score_for_objective`** – Computes the value of an objective for this given set of parameters
- **`set_hypercube`** – Updates parameter properties for an existing parameteriser.
- **`set_max_parameter_value`** – Sets the value(s) of the upper bound of one or more parameter(s)
- **`set_min_parameter_value`** – Sets the value(s) of the lower bound of one or more parameter(s)
- **`set_parameter_definition`** – Sets the feasible range and value for a parameter
- **`set_parameter_value`** – Sets the value(s) of one or more parameter(s)
- **`subcatchment_parameteriser`** – Create a parameteriser that gets applied to a subset of a whole catchment
- **`supports_thread_safe_cloning`** – Is this parameteriser clonable as a deep copy, safe for multi-threading?
- **`to_json_file`** – Save this parameteriser to a file with a JSON serialisation.
- **`wrap_transform`** – Create a parameteriser for which parameter transformations can be defined.

### add_linear_scaled_parameter

```
add_linear_scaled_parameter(param_name: str, state_name: str, scaling_var_name: str, min_p_val: float, max_p_val: float, value: float, intercept: float = 0.0)
```

Adds a single linearly scaled parameter relationship.

Defines a virtual parameter whose value determines a model state through a linear relationship: model_state = virtual_param * scaling_var + intercept. This is typically used for state initialisation, such as setting initial soil moisture as a fraction of maximum capacity.

Parameters:

- **`param_name`** (`str`) – Name of the virtual parameter to create (e.g., 'S0').
- **`state_name`** (`str`) – Name of the model state to initialise (e.g., 'S' for soil moisture store).
- **`scaling_var_name`** (`str`) – Name of the model parameter that scales the relationship (e.g., 'x1' for GR4J maximum soil capacity). The model state will be set to: state = param_name_value * scaling_var_name_value + intercept.
- **`min_p_val`** (`float`) – Minimum feasible value for the virtual parameter.
- **`max_p_val`** (`float`) – Maximum feasible value for the virtual parameter.
- **`value`** (`float`) – Initial value for the virtual parameter (scaling factor).
- **`intercept`** (`float`, default: `0.0` ) – Constant offset in the linear relationship. Typically 0.0, meaning the state is purely a scaled fraction of the scaling variable. Defaults to 0.0.

Note

After adding scaled parameters, call make_state_init_parameteriser() to create a state initialiser that can be applied to simulations. The `scaling_var_name` parameter must already exist in the simulation's model.

Examples:

```
>>> # Set GR4J initial soil moisture as 90% of capacity (x1)
>>> p_states = ScalingParameteriser.linear_parameteriser(
...     param_name=['S0'],
...     state_name=['S'],
...     scaling_var_name=['x1'],
...     min_p_val=[0.0],
...     max_p_val=[1.0],
...     value=[0.9],
...     selector_type='each subarea'
... )
>>> p_states.add_linear_scaled_parameter('R0', 'R', 'x3', 0.0, 1.0, 0.5)
>>> init = p_states.make_state_init_parameteriser()
>>> simulation.use_state_initialiser(init)
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

Adds a mathematical transformation to a parameter for optimisation in transformed space.

This allows you to define a virtual parameter (e.g., log_X) that gets optimised instead of the original parameter X. The transformation is automatically inverted when applying parameters to the simulation. Common use cases include log transforms for strictly positive parameters or arcsinh for parameters that can be negative.

Parameters:

- **`param_name`** (`str`) – Name of the new transformed parameter (e.g., 'log_x4'). This is what the optimiser will see and adjust. Should differ from inner_param_name to avoid confusion.
- **`inner_param_name`** (`str`) – Name of the underlying parameter being transformed (e.g., 'x4'). Must already exist in the parameteriser.
- **`transform_id`** (`str`) – Identifier for the transformation function. Available options as of 2025-11:
  - 'log10': Base-10 logarithm (for positive parameters, or made positive via a and b)
  - '10\*\*x': Base-10 exponentiation (inverse of log10)
  - '1/x': Reciprocal
  - 'x': Identity (no transformation). Structurally useful in edge cases but normally not needed.
  - 'asinh': Inverse hyperbolic sine
  - 'sinh': Hyperbolic sine
  - 'atanh': Inverse hyperbolic tangent
  - 'tanh': Hyperbolic tangent
  - 'sqrt': Square root (for non-negative parameters or made non-negative via a and b)
  - 'square': square function
  - 'logit': Logit function (for parameters in (0,1))
- **`a`** (`float`, default: `1.0` ) – Scaling factor applied before transformation: Y = F(a\*x + b). Defaults to 1.0.
- **`b`** (`float`, default: `0.0` ) – Offset applied before transformation: Y = F(a\*x + b). Defaults to 0.0.

Note

After transformation, the optimiser works with param_name, but the simulation receives the back-transformed values for inner_param_name. Use backtransform() to retrieve parameters in the original space.

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
from_dataframe(type: str = 'Generic subareas', definition: Optional[DataFrame] = None) -> HypercubeParameteriser
```

Creates a parameteriser from a parameter specification.

Factory method to create different types of parameterisers based on the 'type' string. The type determines which model elements (subareas, links, nodes) the parameters will be applied to.

Parameters:

- **`type`** (`str`, default: `'Generic subareas'` ) – Parameteriser type identifier (case-insensitive). Valid options:
  - 'generic' or 'generic subareas': Apply to all subareas (default)
  - 'links' or 'generic links': Apply to channel routing in links
  - 'nodes' or 'generic nodes': Apply to nodes
  - 'muskingum': Muskingum channel routing parameters
  - 'log-likelihood': Parameters for log-likelihood transformation (advanced) Defaults to "Generic subareas".
- **`definition`** (`DataFrame`, default: `None` ) – Parameter specifications with columns:
  - 'Name': Parameter name (e.g., 'x1', 'x2', 'alpha')
  - 'Min': Minimum feasible value
  - 'Max': Maximum feasible value
  - 'Value': Initial/current value If None, creates an empty parameteriser that can be populated later. Defaults to None.

Returns:

- **`HypercubeParameteriser`** ( `HypercubeParameteriser` ) – New parameteriser configured according to the type.

Examples:

```
>>> # Create GR4J parameters for subareas
>>> import pandas as pd
>>> from swift2.utils import c
>>> pspec = pd.DataFrame({
...     'Name': c('x1', 'x2', 'x3', 'x4'),
...     'Value': c(350, -0.5, 50, 2),
...     'Min': c(1, -27, 1, 1),
...     'Max': c(3000, 27, 1000, 240)
... })
>>> p = HypercubeParameteriser.from_dataframe('generic subareas', pspec)
```

```
>>> # Create link routing parameters
>>> link_spec = pd.DataFrame({
...     'Name': c('alpha', 'inverse_velocity'),
...     'Value': c(1, 1),
...     'Min': c(1e-3, 1e-3),
...     'Max': c(1e2, 1e2)
... })
>>> p_links = HypercubeParameteriser.from_dataframe('generic links', link_spec)
```

```
>>> # Create empty parameteriser to populate later
>>> p_empty = HypercubeParameteriser.from_dataframe('generic')
>>> p_empty.add_parameter_to_hypercube('x1', value=350, min=1, max=3000)
```

### from_json_file

```
from_json_file(file_path: str) -> HypercubeParameteriser
```

Load a parameteriser from a file with a JSON serialisation.

Parameters:

- **`file_path`** (`str`) – file path to load from

Returns:

- **`HypercubeParameteriser`** ( `HypercubeParameteriser` ) – loaded parameteriser

### linear_parameteriser

```
linear_parameteriser(param_name: VecStr, state_name: VecStr, scaling_var_name: VecStr, min_p_val: VecNum, max_p_val: VecNum, value: VecNum, selector_type: str = 'subareas', intercept: VecNum = 0.0) -> ScalingParameteriser
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

- **`ScalingParameteriser`** ( `ScalingParameteriser` ) – new ScalingParameteriser

### linear_parameteriser_from

```
linear_parameteriser_from(data_frame: DataFrame, selector_type: str = 'subareas') -> ScalingParameteriser
```

Create a scaled linear parameteriser, tying by a linear transformation a (resp several) model state to a (resp several) parameter values This allows to define tied parameters where pval = a * modelStateVal + intercept. The intent in particular is to define virtual model parameters such as initial store value as a fraction of the maximum storage capacity.

Parameters:

- **`data_frame`** (`DataFrame`) – data frame with columns "param_name", "state_name", "scaling_var_name", "min_value", "max_value", "value", "intercept",
- **`selector_type`** (`str`, default: `'subareas'` ) – [description]. Defaults to "subareas".

Returns:

- **`ScalingParameteriser`** ( `ScalingParameteriser` ) – ScalingParameteriser

### make_state_init_parameteriser

```
make_state_init_parameteriser() -> StateInitParameteriser
```

Converts this parameteriser into a StateInitParameteriser.

Creates a StateInitParameteriser object that can be applied to simulations to set initial model states based on parameter values, as part of an optimisation process i.e. optimising some initial states. This is typically the subsequent step after defining scaled parameter relationships using ScalingParameteriser methods, and before inclusion in an optimisation workflow.

Returns:

- **`StateInitParameteriser`** ( `StateInitParameteriser` ) – Parameteriser with features to set model initial states via state initialisers,
- `StateInitParameteriser` – overriding the default simulation for model reset of initial states.

Typical Workflow

1. Create a ScalingParameteriser with linear_parameteriser() or linear_parameteriser_from()
1. Define relationships between virtual parameters and model states
1. Call make_state_init_parameteriser() to create the StateInitParameteriser
1. Use the StateInitParameteriser in an optimisation or sensitivity analysis workflow

Use Cases

- Setting initial soil moisture as a fraction of maximum capacity (S0 = 0.9 * x1 for GR4J)
- Initialising routing stores as fractions of their capacities
- Calibrating initial states alongside model parameters
- Ensuring physically consistent initial conditions

Note

The scaling variables (e.g., x1, x3) must exist as parameters in the simulation's model. If they don't exist or have incompatible dimensions, an error will occur when the initialiser is applied during simulation execution.

Examples:

```
>>> # Use case: Set gr4j initial stores at simulation as a function of x1/x3 parameters.
>>> # and calibrate both model parameters and the virtual initial state parameters S0 and R0.
>>> # `some_other_parameteriser` may be a parameteriser for GR4J parameters x1 to x4.
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
>>> parameteriser = sp.concatenate_parameterisers(some_other_parameteriser, init_parameteriser)
>>> # Now use 'parameteriser' in an optimisation workflow to calibrate both model parameters and initial states.
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

Updates parameter properties for an existing parameteriser.

Modifies the bounds and values of parameters already defined in this parameteriser. Unlike from_dataframe() which creates a new parameteriser, this method updates the current one. All parameter names in the specs must already exist in the parameteriser.

Parameters:

- **`specs`** (`DataFrame`) – Parameter specifications with columns:
  - 'Name': Parameter name (must match existing parameters)
  - 'Min': New minimum feasible value
  - 'Max': New maximum feasible value
  - 'Value': New initial/current value All columns are required for each parameter being updated.

Raises:

- `Exception` – If any parameter name in specs doesn't exist in this parameteriser.

Note

This is useful for adjusting parameter bounds after initial creation, such as converting time-step-dependent parameters (e.g., GR4J x4 from hours to days) or tightening bounds based on prior calibration results.

Examples:

```
>>> # Create GR4J parameteriser with default hourly time step
>>> p = HypercubeParameteriser.from_dataframe('generic subareas', gr4j_hourly_spec)
>>> 
>>> # Convert x4 bounds from hours to days for daily time step
>>> p_x4_daily = pd.DataFrame({
...     'Name': ['x4'],
...     'Value': [1.0],
...     'Min': [0.25],
...     'Max': [10.0]  # 10 days instead of 240 hours
... })
>>> p.set_hypercube(p_x4_daily)
```

```
>>> # Update multiple parameters after preliminary calibration
>>> tighter_bounds = pd.DataFrame({
...     'Name': ['x1', 'x3'],
...     'Value': [450, 75],
...     'Min': [300, 50],
...     'Max': [600, 100]
... })
>>> p.set_hypercube(tighter_bounds)
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
subcatchment_parameteriser(subcatchment: Simulation) -> HypercubeParameteriser
```

Create a parameteriser that gets applied to a subset of a whole catchment

Parameters:

- **`subcatchment`** (`Simulation`) – the subcatchment, subset of a whole catchment, identifying which elements (subareas, nodes, links) will be parameterised by the new parameteriser. Other catchment elements are untouched.

Returns:

- **`HypercubeParameteriser`** ( `HypercubeParameteriser` ) – New parameteriser whose application is limited to the subcatchment.

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

### to_json_file

```
to_json_file(file_path: str) -> None
```

Save this parameteriser to a file with a JSON serialisation.

Parameters:

- **`file_path`** (`str`) – file path to save to

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

Specifies when the SCE-UA optimizer should stop (e.g., max iterations, convergence tolerance, wall time).

## Simulation

```
Simulation(handle: CffiData, release_native: Callable[[CffiData], None], type_id: Optional[str] = None, prior_ref_count: int = 0)
```

Bases: `DeletableCffiNativeHandle`, `SimulationMixin`

Represents a catchment model with its structure, states, and configuration; executes time-stepping simulations.

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
- **`exec_simulation`** – Executes the simulation over its configured time span.
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
- **`get_recorded`** – Retrieves recorded time series from the simulation.
- **`get_recorded_varnames`** – Gets all the names of the recorded states
- **`get_simulation_span`** – Gets the simulation span of this simulation
- **`get_state_value`** – Gets the value(s) of a model state(s)
- **`get_state_value_bool`** –
- **`get_state_value_int`** –
- **`get_subarea_ids`** – Gets all the identifiers of the subareas in the catchment
- **`get_subarea_names`** – Gets all the names of the subareas in the catchment
- **`get_variable_ids`** – Gets all the names of the variables of an element (link, node, subarea) within a catchment
- **`is_variable_id`** – Are one or more model state identifier(s) valid
- **`muskingum_param_constraints`** – Create a parameteriser with Muskingum-type constraints.
- **`play_input`** – Sets one or more time series as input(s) to a simulation.
- **`play_inputs`** – Assign input time series from a time series library to a model simulation
- **`play_subarea_input`** – Sets time series as input to a simulation
- **`prepare_dual_pass_forecasting`** – Create an ensemble simulation for forecasting with the Dual Pass error correction method
- **`prepare_erris_forecasting`** – Create an ensemble simulation for forecasting with ERRIS
- **`record_singular_state`** – DRAFT Advanced/technical. Record states to a record provider.
- **`record_state`** – Records a time series of model state variable(s) during simulation execution.
- **`remove_played_input`** –
- **`remove_recorded`** –
- **`remove_state_initialisers`** – Forces the removal of any state initialiser.
- **`reset_model_states`** – Reset the model states of a simulation, and apply one or more state initialers if the simulation is configured with any.
- **`set_error_correction_model`** – Add an error correction model to an element in a catchment
- **`set_reservoir_fill_curve`** – Sets a reservoir fill curve
- **`set_reservoir_geometry`** – Sets the geometry of a reservoir
- **`set_reservoir_max_discharge`** – Sets a reservoir operating curve, maximum release for a given level
- **`set_reservoir_min_discharge`** – Sets a reservoir operating curve, minimum release for a given level
- **`set_reservoir_model`** – Sets a new reservoir model on an element
- **`set_reservoir_return_curve`** – Sets a reservoir return curve
- **`set_reservoir_spill_curve`** – Sets a reservoir spill curve
- **`set_simulation_span`** – Sets the simulation span
- **`set_simulation_time_step`** – Sets the time step of this simulation
- **`set_state_value`** – Sets the value of a model state
- **`set_state_value_bool`** –
- **`set_state_value_int`** –
- **`set_states`** – Restores model states from a previously captured snapshot.
- **`snapshot_state`** – Captures a snapshot of all current model states for later restoration.
- **`sort_by_execution_order`** – Sort the specified element ids according to the execution order of the simulation
- **`split_to_subcatchments`** – Splits a catchment into subcatchments at specified network elements.
- **`subset_catchment`** – Subsets a catchment, keeping only elements above or below a specified element.
- **`swap_model`** – Clone and change a simulation, using another model
- **`to_json_file`** – Save a model simulation from a file with a JSON serialisation.
- **`use_state_initialiser`** – Sets the state initialiser to use for a simulation. This forces the removal of any prior state initialiser.

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
cookie_cut_dendritic_catchment(bottom_element_id: str, top_element_ids: Optional[VecStr]) -> Simulation
```

cookie cut a dendritic catchment (without confluences)

Parameters:

- **`bottom_element_id`** (`str`) – identifier of the most downstream element to keep
- **`top_element_ids`** (`Optional[VecStr]`) – identifier(s) of the most upstream element(s) to keep. Empty list or None means no upstream cuts.

Returns:

- **`Simulation`** ( `Simulation` ) – a subcatchment simulation, cookie cut from the base simulation. Deep clone of objects.

Examples:

```
>>> # sdh  swift2.doc_helper
>>> _, simulation = sdh.create_test_catchment_structure()
>>> e_ids = ['node.n2', 'node.n4']
>>> above_n2 = simulation.cookie_cut_dendritic_catchment(e_ids[0], [])
>>> above_n2.describe()
{'subareas': {'lnk2': 'lnk2_name', 'lnk3': 'lnk3_name', 'lnk4': 'lnk4_name', 'lnk5': 'lnk5_name'}, 'nodes': {'n2': 'n2_name', 'n5': 'n5_name', 'n4': 'n4_name', 'n3': 'n3_name', 'n1': 'n1_name'}, 'links': {'lnk2': 'lnk2_name', 'lnk3': 'lnk3_name', 'lnk4': 'lnk4_name', 'lnk5': 'lnk5_name'}}
>>> above_n2_below_n4 = simulation.cookie_cut_dendritic_catchment(e_ids[0], [e_ids[1]])
>>> above_n2_below_n4.describe()
{'subareas': {'lnk2': 'lnk2_name', 'lnk3': 'lnk3_name'}, 'nodes': {'n2': 'n2_name', 'n5': 'n5_name'}, 'links': {'lnk2': 'lnk2_name', 'lnk3': 'lnk3_name'}}
>>>
```

### create_ensemble_forecast_simulation

```
create_ensemble_forecast_simulation(data_library, start: ConvertibleToTimestamp, end: ConvertibleToTimestamp, input_map: Dict[str, List[str]], lead_time: int, ensemble_size: int, n_time_steps_between_forecasts: int) -> EnsembleForecastSimulation
```

Create an ensemble forecast simulation

Parameters:

- **`data_library`** (`Any`) – external pointer type ENSEMBLE_DATA_SET_PTR, or a Python class wrapper around it
- **`start`** (`ConvertibleToTimestamp`) – the start date of the simulation. Time zone aware timestamps are not supported..
- **`end`** (`ConvertibleToTimestamp`) – the end date of the simulation. Time zone aware timestamps are not supported..
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

Executes the simulation over its configured time span.

Runs the model forward in time from the simulation start to end date, using the configured time step. Input time series (set via play_input) are read and applied at each step, and any recorded state variables (set via record_state) are stored for later retrieval.

Parameters:

- **`reset_initial_states`** (`bool`, default: `True` ) – Whether to reset all model states to their initial values before starting the simulation. If True (default), any state initialisers configured on the simulation are also applied. Set to False to continue from current model states (useful for sequential simulation periods). Defaults to True.

Note

Before calling this method, ensure you have:

- Set the simulation span via set_simulation_span()
- Configured input time series via play_input() or play_inputs()
- Set up recording via record_state() for any outputs you need

Examples:

```
>>> # Standard simulation run
>>> simulation.set_simulation_span('2000-01-01', '2005-12-31')
>>> simulation.play_input(rainfall_ts, 'subarea.Subarea.P')
>>> simulation.record_state('Catchment.StreamflowRate')
>>> simulation.exec_simulation()
>>> flow = simulation.get_recorded()
```

```
>>> # Continue simulation without resetting states
>>> simulation.set_simulation_span('2006-01-01', '2010-12-31')
>>> simulation.exec_simulation(reset_initial_states=False)
```

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

Retrieves recorded time series from the simulation.

Returns time series data for state variables that were configured for recording via record_state(). If no var_ids are specified, returns all recorded variables as a multivariate time series.

Parameters:

- **`var_ids`** (`optional str or sequence of str`, default: `None` ) – State variable identifier(s) to retrieve. If None, returns all recorded variables (may be a large multivariate dataset). Examples: 'Catchment.StreamflowRate', 'node.n1.OutflowRate', 'subarea.Subarea.runoff'.
- **`start_time`** (`datetime like`, default: `None` ) – Start of period to subset the time series. If None, returns from the beginning of the simulation.
- **`end_time`** (`datetime like`, default: `None` ) – End of period to subset the time series. If None, returns to the end of the simulation.

Returns:

- `DataArray` – xr.DataArray: Time series with 'time' dimension and 'variable_identifiers' coordinate. For single variables, use .sel(variable_identifiers='var_name') to extract. For multiple variables, the result is already multivariate.

Examples:

```
>>> # Get single recorded variable
>>> simulation.record_state('Catchment.StreamflowRate')
>>> simulation.exec_simulation()
>>> flow = simulation.get_recorded('Catchment.StreamflowRate')
```

```
>>> # Get all recorded variables
>>> simulation.record_state(['node.n1.OutflowRate', 'node.n2.OutflowRate'])
>>> simulation.exec_simulation()
>>> all_flows = simulation.get_recorded()  # Returns both series
```

```
>>> # Get subset of time period
>>> flow_subset = simulation.get_recorded('Catchment.StreamflowRate', 
...                                       start_time='2001-01-01',
...                                       end_time='2002-12-31')
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

### get_state_value_bool

```
get_state_value_bool(var_id: str) -> bool
```

### get_state_value_int

```
get_state_value_int(var_id: str) -> int
```

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

Sets one or more time series as input(s) to a simulation.

This method assigns time series data to model state variables (such as rainfall to 'P' or evaporation to 'E' for runoff models). The time series will be played into the simulation during execution.

Parameters:

- **`input_ts`** (`TimeSeriesLike`) – Time series data to play into the simulation. Can be univariate or multivariate. If multivariate (e.g., xarray DataArray), column names must be valid model variable identifiers unless explicitly overridden via var_ids.
- **`var_ids`** (`optional str or sequence of str`, default: `None` ) – Model variable identifier(s) to receive the input data, overriding any column names in input_ts. If provided, must match the number of columns/variables in input_ts. Common examples: 'subarea.{name}.P' for rainfall, 'subarea.{name}.E' for evaporation.

Examples:

```
>>> # Play rainfall into a single subarea model
>>> rain_ts = ... # xarray DataArray with rainfall data
>>> simulation.play_input(rain_ts, 'subarea.Subarea.P')
```

```
>>> # Play multiple inputs using column names
>>> inputs = xr.DataArray(...)  # with columns 'subarea.Subarea.P' and 'subarea.Subarea.E'
>>> simulation.play_input(inputs)
```

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

Records a time series of model state variable(s) during simulation execution.

This method instructs the simulation to store values of specified state variables at each time step. Recorded data can be retrieved after execution using get_recorded(). By default, values are stored in memory, but can optionally be written to an external time series library.

Parameters:

- **`var_ids`** (`VecStr`, default: `CATCHMENT_FLOWRATE_VARID` ) – State variable identifier(s) to record. Common examples include 'Catchment.StreamflowRate' for outlet flow, 'subarea.{name}.runoff' for subarea runoff, or 'node.{name}.OutflowRate' for node outflows. Defaults to CATCHMENT_FLOWRATE_VARID (the main outlet streamflow).
- **`recording_provider`** (`TimeSeriesLibrary`, default: `None` ) – External time series library for storage. If None (default), values are stored in memory and retrieved via get_recorded().
- **`data_ids`** (`VecStr`, default: `None` ) – Identifier(s) for data in the recording_provider. Only used when recording_provider is specified. Must match the length of var_ids.

Raises:

- `ValueError` – If data_ids length doesn't match var_ids when recording_provider is specified.

Examples:

```
>>> # Record outlet streamflow (default)
>>> simulation.record_state()
```

```
>>> # Record multiple state variables
>>> simulation.record_state(['node.n1.OutflowRate', 'node.n2.OutflowRate'])
```

```
>>> # Record after simulation and retrieve
>>> simulation.record_state('subarea.Subarea.runoff')
>>> simulation.exec_simulation()
>>> runoff = simulation.get_recorded('subarea.Subarea.runoff')
```

### remove_played_input

```
remove_played_input(var_ids: VecStr) -> None
```

### remove_recorded

```
remove_recorded(var_ids: VecStr) -> None
```

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

- **`model_id`** (`str`) – the identifier of the new model to use, at least: * autoregressive * ERRIS * MAERRIS * DualPass * OverrideOutflow
- **`element_id`** (`str`) – the identifier of the catchment element (node, link, subcatchment) whose outflow rate is corrected.
- **`length`** (`int`, default: `1` ) – other parameters to pass to the creation of the error correction model. Currently length of the AR model only supported.
- **`seed`** (`int`, default: `0` ) – other parameters to pass to the creation of the error correction model. Currently length of the AR model only supported.

### set_reservoir_fill_curve

```
set_reservoir_fill_curve(element_id: str, inflow_rate: ndarray, fill_rate: ndarray) -> None
```

Sets a reservoir fill curve

Parameters:

- **`element_id`** (`str`) – Element with a suitable reservoir supporting a geometry description
- **`inflow_rate`** (`ndarray`) – array of inflow rates (m3/s)
- **`fill_rate`** (`ndarray`) – array of fill rates (m3/s)

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

### set_reservoir_return_curve

```
set_reservoir_return_curve(element_id: str, level: ndarray, return_rate: ndarray) -> None
```

Sets a reservoir return curve

Parameters:

- **`element_id`** (`str`) – Element with a suitable reservoir supporting a geometry description
- **`level`** (`ndarray`) – array of levels (m)
- **`return_rate`** (`ndarray`) – array of return rates (m3/s)

### set_reservoir_spill_curve

```
set_reservoir_spill_curve(element_id: str, level: ndarray, spill: ndarray) -> None
```

Sets a reservoir spill curve

Parameters:

- **`element_id`** (`str`) – Element with a suitable reservoir supporting a geometry description
- **`level`** (`ndarray`) – array of levels (m)
- **`spill`** (`ndarray`) – array of spillway discharges (m3/s)

### set_simulation_span

```
set_simulation_span(start: ConvertibleToTimestamp, end: ConvertibleToTimestamp) -> None
```

Sets the simulation span

Parameters:

- **`start`** (`ConvertibleToTimestamp`) – the start date of the simulation. Time zone aware timestamps are not supported..
- **`end`** (`ConvertibleToTimestamp`) – the end date of the simulation. Time zone aware timestamps are not supported..

### set_simulation_time_step

```
set_simulation_time_step(name: str) -> None
```

Sets the time step of this simulation

Parameters:

- **`name`** (`str`) – a time step identifier, currently 'daily' or 'hourly' are supported. The identifier is made lower case in the function.

### set_state_value

```
set_state_value(var_id: Union[str, Sequence[str]], value: Union[float, int, bool, Sequence]) -> None
```

Sets the value of a model state

Parameters:

- **`var_id`** (`Any`) – character, model variable state identifier(s)
- **`value`** (`Any`) – numeric value(s)

### set_state_value_bool

```
set_state_value_bool(var_id: str, value: bool)
```

### set_state_value_int

```
set_state_value_int(var_id: str, value: int)
```

### set_states

```
set_states(states: MemoryStates) -> None
```

Restores model states from a previously captured snapshot.

Applies a complete state snapshot (created via snapshot_state()) to this simulation, overwriting all current model states. This allows continuing simulation from a saved point without re-running previous time steps.

Parameters:

- **`states`** (`MemoryStates`) – State snapshot to restore, obtained from snapshot_state(). Must come from a simulation with the same catchment structure.

Note

- This method does NOT affect state initialisers configured on the simulation
- After restoring states, typically call exec_simulation(reset_initial_states=False) to continue from the restored point rather than re-initialising
- The states object must match the simulation's structure (same elements and model types)

Relationship to State Initialisers

State initialisers (set via use_state_initialiser()) define how to initialise states at the start of a simulation when reset_initial_states=True. They are applied during exec_simulation(), not by set_states(). If you restore states with set_states() and then call exec_simulation(reset_initial_states=True), the initialisers will overwrite your restored states.

Examples:

```
>>> # Save and restore states for ensemble forecasting
>>> simulation.exec_simulation()  # Warmup period
>>> initial_state = simulation.snapshot_state()
>>> 
>>> # Run ensemble members
>>> for member in range(ensemble_size):
...     simulation.set_states(initial_state)  # Start from same point
...     simulation.play_input(ensemble_inputs[member], 'subarea.Subarea.P')
...     simulation.exec_simulation(reset_initial_states=False)  # Continue from restored state
...     forecasts[member] = simulation.get_recorded()
```

```
>>> # Incorrect usage - states will be overwritten
>>> simulation.set_states(saved_state)
>>> simulation.exec_simulation(reset_initial_states=True)  # BAD: ignores saved_state
```

```
>>> # Correct usage - continue from restored state
>>> simulation.set_states(saved_state)
>>> simulation.exec_simulation(reset_initial_states=False)  # GOOD: uses saved_state
```

### snapshot_state

```
snapshot_state() -> MemoryStates
```

Captures a snapshot of all current model states for later restoration.

Takes a complete copy of the simulation's internal state at the current point in time, including all storages, fluxes, and memory variables across all model elements (subareas, links, nodes). The snapshot can be restored later using set_states() to continue simulation from this exact point.

Returns:

- **`MemoryStates`** ( `MemoryStates` ) – Object containing the complete model state. Can be stored and reapplied to this or a cloned simulation.

Use Cases

- Saving state after a warmup period to run multiple scenarios from the same starting point
- Implementing custom ensemble forecasting workflows
- Debugging by comparing states at different points in a simulation
- Avoiding re-running expensive warmup periods for multiple forecast runs

Note

The snapshot is specific to the simulation's structure (number and type of model elements). It cannot be applied to a simulation with a different catchment configuration with different element names and/or models.

Examples:

```
>>> # Run warmup and save state
>>> simulation.set_simulation_span('2000-01-01', '2005-12-31')
>>> simulation.exec_simulation()
>>> warmup_state = simulation.snapshot_state()
>>> 
>>> # Run multiple scenarios from the same starting point
>>> for scenario in scenarios:
...     simulation.set_states(warmup_state)  # Restore warmup state
...     simulation.play_input(scenario.inputs, 'subarea.Subarea.P')
...     simulation.set_simulation_span('2006-01-01', '2010-12-31')
...     simulation.exec_simulation(reset_initial_states=False)
...     results[scenario.name] = simulation.get_recorded()
```

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

Splits a catchment into subcatchments at specified network elements.

Creates independent subcatchment simulations by recursively cutting the network at specified nodes or links. Each resulting subcatchment includes all upstream elements, minus further upstream subcatchments already cut. A 'remainder' subcatchment contains any final, downstream elements not included in the upstream portions.

Parameters:

- **`split_element_ids`** (`Sequence[str]`) – Element identifiers where to split the catchment, such as 'node.n1', 'link.linkId_2'. Elements are processed in execution order (upstream to downstream), not in the order provided by the user.
- **`include_upstream`** (`Sequence[bool]`, default: `None` ) – For each element in split_element_ids, whether to include that element in the upstream subcatchment (True) or the downstream remainder (False). If None, defaults to True for all elements. Must match the length of split_element_ids if provided. Defaults to None.

Returns:

- `OrderedDict[str, Simulation]` – OrderedDict\[str, Simulation\]: Dictionary mapping element IDs to their upstream subcatchment simulations, plus a 'remainder' key for downstream elements. Each simulation is a deep copy with independent state.

Note

The split creates deep copies, so modifications to subcatchments don't affect the original simulation. All subcatchments inherit the model configuration and time settings from the original but have independent parameter values and states.

Examples:

```
>>> _, simulation = sdh.create_test_catchment_structure()
>>> e_ids = ['node.n2', 'node.n4']
>>> sub_sims = simulation.split_to_subcatchments(e_ids)
>>> 
>>> for k in sub_sims:
...     print(k)
...     print(sub_sims[k].get_node_ids())
...     print(sub_sims[k].get_node_names())
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

Subsets a catchment, keeping only elements above or below a specified element.

Creates a new simulation containing only the portion of the catchment upstream or downstream of a cut point. Useful for focusing calibration on specific subcatchments or analysing contributions from different parts of a river network.

Parameters:

- **`element_id`** (`str`) – Identifier of the element to cut at (e.g., 'node.n1', 'link.lnk5', 'subarea.sub1'). The action parameter determines what is kept relative to this point.
- **`action`** (`str`, default: `'keep_above'` ) – How to subset the catchment. Combinations of keywords:
  - 'above' or 'below': Direction to keep relative to element_id
  - 'keep': Explicit (implied if omitted) - keep the specified direction
  - 'exclusive': Exclude the cut element itself from the result Examples: 'keep_above', 'keep above', 'below', 'keep above exclusive'. Defaults to "keep_above".

Returns:

- **`Simulation`** – A new subcatchment simulation containing only the specified portion. Deep copy with independent state from the original.

Note

- 'above' means upstream (towards headwaters)
- 'below' means downstream (towards outlet)
- The cut element is included by default unless 'exclusive' is specified
- For headwater catchments, 'keep above exclusive' may return an empty catchment

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
>>> # to keep only a headwater catchment with its link:
>>> simulation.subset_catchment("link.lnk5", 'keep above').describe()
{'subareas': {'lnk5': 'lnk5_name'}, 'nodes': {'n1': 'n1_name'}, 'links': {'lnk5': 'lnk5_name'}}
>>> # to keep only a headwater catchment with its link:
>>> simulation.subset_catchment("node.n5", 'keep above exclusive').describe()
{'subareas': {}, 'nodes': {}, 'links': {}}
>>> # below will not work at the time of writing, but maybe should:
>>> simulation.subset_catchment("subarea.lnk5", 'keep above').describe()
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

### use_state_initialiser

```
use_state_initialiser(state_initialiser: StateInitialiser)
```

Sets the state initialiser to use for a simulation. This forces the removal of any prior state initialiser.

Parameters:

- **`state_initialiser`** (`StateInitialiser`) – the new state initialiser to use

## SimulationMixin

```
SimulationMixin()
```

Provides common simulation methods shared by Simulation, EnsembleSimulation, and EnsembleForecastSimulation classes.

Methods:

- **`exec_simulation`** – Executes the simulation over its configured time span.
- **`get_played_varnames`** – Gets all the names of states fed an input time series
- **`get_recorded_varnames`** – Gets all the names of the recorded states
- **`record_state`** – Records a time series of model state variable(s) during simulation execution.

### exec_simulation

```
exec_simulation(reset_initial_states: bool = True) -> None
```

Executes the simulation over its configured time span.

Runs the model forward in time from the simulation start to end date, using the configured time step. Input time series (set via play_input) are read and applied at each step, and any recorded state variables (set via record_state) are stored for later retrieval.

Parameters:

- **`reset_initial_states`** (`bool`, default: `True` ) – Whether to reset all model states to their initial values before starting the simulation. If True (default), any state initialisers configured on the simulation are also applied. Set to False to continue from current model states (useful for sequential simulation periods). Defaults to True.

Note

Before calling this method, ensure you have:

- Set the simulation span via set_simulation_span()
- Configured input time series via play_input() or play_inputs()
- Set up recording via record_state() for any outputs you need

Examples:

```
>>> # Standard simulation run
>>> simulation.set_simulation_span('2000-01-01', '2005-12-31')
>>> simulation.play_input(rainfall_ts, 'subarea.Subarea.P')
>>> simulation.record_state('Catchment.StreamflowRate')
>>> simulation.exec_simulation()
>>> flow = simulation.get_recorded()
```

```
>>> # Continue simulation without resetting states
>>> simulation.set_simulation_span('2006-01-01', '2010-12-31')
>>> simulation.exec_simulation(reset_initial_states=False)
```

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

Records a time series of model state variable(s) during simulation execution.

This method instructs the simulation to store values of specified state variables at each time step. Recorded data can be retrieved after execution using get_recorded(). By default, values are stored in memory, but can optionally be written to an external time series library.

Parameters:

- **`var_ids`** (`VecStr`, default: `CATCHMENT_FLOWRATE_VARID` ) – State variable identifier(s) to record. Common examples include 'Catchment.StreamflowRate' for outlet flow, 'subarea.{name}.runoff' for subarea runoff, or 'node.{name}.OutflowRate' for node outflows. Defaults to CATCHMENT_FLOWRATE_VARID (the main outlet streamflow).
- **`recording_provider`** (`TimeSeriesLibrary`, default: `None` ) – External time series library for storage. If None (default), values are stored in memory and retrieved via get_recorded().
- **`data_ids`** (`VecStr`, default: `None` ) – Identifier(s) for data in the recording_provider. Only used when recording_provider is specified. Must match the length of var_ids.

Raises:

- `ValueError` – If data_ids length doesn't match var_ids when recording_provider is specified.

Examples:

```
>>> # Record outlet streamflow (default)
>>> simulation.record_state()
```

```
>>> # Record multiple state variables
>>> simulation.record_state(['node.n1.OutflowRate', 'node.n2.OutflowRate'])
```

```
>>> # Record after simulation and retrieve
>>> simulation.record_state('subarea.Subarea.runoff')
>>> simulation.exec_simulation()
>>> runoff = simulation.get_recorded('subarea.Subarea.runoff')
```

## StateInitParameteriser

```
StateInitParameteriser(handle: CffiData, release_native: Callable[[CffiData], None], type_id: Optional[str] = None, prior_ref_count: int = 0)
```

Bases: `HypercubeParameteriser`

Defines how to initialize model states based on parameter values at the start of each simulation run.

Methods:

- **`add_parameter_to_hypercube`** – Add a parameter to a hypercube. Must be a type of object that is expandable, otherwise may raise an exception
- **`add_to_hypercube`** – Add entries to a hypercube. Must be a type of object that is expandable, otherwise may raise an exception.
- **`apply_sys_config`** – Apply a model configuration to a simulation
- **`as_dataframe`** – Convert this hypercube parameteriser to a pandas data frame representation
- **`backtransform`** – Get the parameteriser values in the untransformed space
- **`clone`** –
- **`create_parameter_sampler`** – Creates a sampler for this parameteriser
- **`filtered_parameters`** – Wrap this parameteriser in a filter that can hide some parameters from an optimiser.
- **`from_dataframe`** – Creates a parameteriser from a parameter specification.
- **`from_json_file`** – Load a parameteriser from a file with a JSON serialisation.
- **`make_state_init_parameteriser`** – Converts this parameteriser into a StateInitParameteriser.
- **`num_free_parameters`** – Number of free parameters in this hypercube parameteriser
- **`score_for_objective`** – Computes the value of an objective for this given set of parameters
- **`set_hypercube`** – Updates parameter properties for an existing parameteriser.
- **`set_max_parameter_value`** – Sets the value(s) of the upper bound of one or more parameter(s)
- **`set_min_parameter_value`** – Sets the value(s) of the lower bound of one or more parameter(s)
- **`set_parameter_definition`** – Sets the feasible range and value for a parameter
- **`set_parameter_value`** – Sets the value(s) of one or more parameter(s)
- **`subcatchment_parameteriser`** – Create a parameteriser that gets applied to a subset of a whole catchment
- **`supports_thread_safe_cloning`** – Is this parameteriser clonable as a deep copy, safe for multi-threading?
- **`to_json_file`** – Save this parameteriser to a file with a JSON serialisation.
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
from_dataframe(type: str = 'Generic subareas', definition: Optional[DataFrame] = None) -> HypercubeParameteriser
```

Creates a parameteriser from a parameter specification.

Factory method to create different types of parameterisers based on the 'type' string. The type determines which model elements (subareas, links, nodes) the parameters will be applied to.

Parameters:

- **`type`** (`str`, default: `'Generic subareas'` ) – Parameteriser type identifier (case-insensitive). Valid options:
  - 'generic' or 'generic subareas': Apply to all subareas (default)
  - 'links' or 'generic links': Apply to channel routing in links
  - 'nodes' or 'generic nodes': Apply to nodes
  - 'muskingum': Muskingum channel routing parameters
  - 'log-likelihood': Parameters for log-likelihood transformation (advanced) Defaults to "Generic subareas".
- **`definition`** (`DataFrame`, default: `None` ) – Parameter specifications with columns:
  - 'Name': Parameter name (e.g., 'x1', 'x2', 'alpha')
  - 'Min': Minimum feasible value
  - 'Max': Maximum feasible value
  - 'Value': Initial/current value If None, creates an empty parameteriser that can be populated later. Defaults to None.

Returns:

- **`HypercubeParameteriser`** ( `HypercubeParameteriser` ) – New parameteriser configured according to the type.

Examples:

```
>>> # Create GR4J parameters for subareas
>>> import pandas as pd
>>> from swift2.utils import c
>>> pspec = pd.DataFrame({
...     'Name': c('x1', 'x2', 'x3', 'x4'),
...     'Value': c(350, -0.5, 50, 2),
...     'Min': c(1, -27, 1, 1),
...     'Max': c(3000, 27, 1000, 240)
... })
>>> p = HypercubeParameteriser.from_dataframe('generic subareas', pspec)
```

```
>>> # Create link routing parameters
>>> link_spec = pd.DataFrame({
...     'Name': c('alpha', 'inverse_velocity'),
...     'Value': c(1, 1),
...     'Min': c(1e-3, 1e-3),
...     'Max': c(1e2, 1e2)
... })
>>> p_links = HypercubeParameteriser.from_dataframe('generic links', link_spec)
```

```
>>> # Create empty parameteriser to populate later
>>> p_empty = HypercubeParameteriser.from_dataframe('generic')
>>> p_empty.add_parameter_to_hypercube('x1', value=350, min=1, max=3000)
```

### from_json_file

```
from_json_file(file_path: str) -> HypercubeParameteriser
```

Load a parameteriser from a file with a JSON serialisation.

Parameters:

- **`file_path`** (`str`) – file path to load from

Returns:

- **`HypercubeParameteriser`** ( `HypercubeParameteriser` ) – loaded parameteriser

### make_state_init_parameteriser

```
make_state_init_parameteriser() -> StateInitParameteriser
```

Converts this parameteriser into a StateInitParameteriser.

Creates a StateInitParameteriser object that can be applied to simulations to set initial model states based on parameter values, as part of an optimisation process i.e. optimising some initial states. This is typically the subsequent step after defining scaled parameter relationships using ScalingParameteriser methods, and before inclusion in an optimisation workflow.

Returns:

- **`StateInitParameteriser`** ( `StateInitParameteriser` ) – Parameteriser with features to set model initial states via state initialisers,
- `StateInitParameteriser` – overriding the default simulation for model reset of initial states.

Typical Workflow

1. Create a ScalingParameteriser with linear_parameteriser() or linear_parameteriser_from()
1. Define relationships between virtual parameters and model states
1. Call make_state_init_parameteriser() to create the StateInitParameteriser
1. Use the StateInitParameteriser in an optimisation or sensitivity analysis workflow

Use Cases

- Setting initial soil moisture as a fraction of maximum capacity (S0 = 0.9 * x1 for GR4J)
- Initialising routing stores as fractions of their capacities
- Calibrating initial states alongside model parameters
- Ensuring physically consistent initial conditions

Note

The scaling variables (e.g., x1, x3) must exist as parameters in the simulation's model. If they don't exist or have incompatible dimensions, an error will occur when the initialiser is applied during simulation execution.

Examples:

```
>>> # Use case: Set gr4j initial stores at simulation as a function of x1/x3 parameters.
>>> # and calibrate both model parameters and the virtual initial state parameters S0 and R0.
>>> # `some_other_parameteriser` may be a parameteriser for GR4J parameters x1 to x4.
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
>>> parameteriser = sp.concatenate_parameterisers(some_other_parameteriser, init_parameteriser)
>>> # Now use 'parameteriser' in an optimisation workflow to calibrate both model parameters and initial states.
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

Updates parameter properties for an existing parameteriser.

Modifies the bounds and values of parameters already defined in this parameteriser. Unlike from_dataframe() which creates a new parameteriser, this method updates the current one. All parameter names in the specs must already exist in the parameteriser.

Parameters:

- **`specs`** (`DataFrame`) – Parameter specifications with columns:
  - 'Name': Parameter name (must match existing parameters)
  - 'Min': New minimum feasible value
  - 'Max': New maximum feasible value
  - 'Value': New initial/current value All columns are required for each parameter being updated.

Raises:

- `Exception` – If any parameter name in specs doesn't exist in this parameteriser.

Note

This is useful for adjusting parameter bounds after initial creation, such as converting time-step-dependent parameters (e.g., GR4J x4 from hours to days) or tightening bounds based on prior calibration results.

Examples:

```
>>> # Create GR4J parameteriser with default hourly time step
>>> p = HypercubeParameteriser.from_dataframe('generic subareas', gr4j_hourly_spec)
>>> 
>>> # Convert x4 bounds from hours to days for daily time step
>>> p_x4_daily = pd.DataFrame({
...     'Name': ['x4'],
...     'Value': [1.0],
...     'Min': [0.25],
...     'Max': [10.0]  # 10 days instead of 240 hours
... })
>>> p.set_hypercube(p_x4_daily)
```

```
>>> # Update multiple parameters after preliminary calibration
>>> tighter_bounds = pd.DataFrame({
...     'Name': ['x1', 'x3'],
...     'Value': [450, 75],
...     'Min': [300, 50],
...     'Max': [600, 100]
... })
>>> p.set_hypercube(tighter_bounds)
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
subcatchment_parameteriser(subcatchment: Simulation) -> HypercubeParameteriser
```

Create a parameteriser that gets applied to a subset of a whole catchment

Parameters:

- **`subcatchment`** (`Simulation`) – the subcatchment, subset of a whole catchment, identifying which elements (subareas, nodes, links) will be parameterised by the new parameteriser. Other catchment elements are untouched.

Returns:

- **`HypercubeParameteriser`** ( `HypercubeParameteriser` ) – New parameteriser whose application is limited to the subcatchment.

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

### to_json_file

```
to_json_file(file_path: str) -> None
```

Save this parameteriser to a file with a JSON serialisation.

Parameters:

- **`file_path`** (`str`) – file path to save to

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

Sets initial conditions for model states before simulation execution begins.

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

Applies mathematical transformations (e.g., log, arcsinh) to parameters optimisation in transformed space.

Methods:

- **`add_parameter_to_hypercube`** – Add a parameter to a hypercube. Must be a type of object that is expandable, otherwise may raise an exception
- **`add_to_hypercube`** – Add entries to a hypercube. Must be a type of object that is expandable, otherwise may raise an exception.
- **`add_transform`** – Adds a mathematical transformation to a parameter for optimisation in transformed space.
- **`apply_sys_config`** – Apply a model configuration to a simulation
- **`as_dataframe`** – Convert this hypercube parameteriser to a pandas data frame representation
- **`backtransform`** – Get the parameteriser values in the untransformed space
- **`clone`** –
- **`create_parameter_sampler`** – Creates a sampler for this parameteriser
- **`filtered_parameters`** – Wrap this parameteriser in a filter that can hide some parameters from an optimiser.
- **`from_dataframe`** – Creates a parameteriser from a parameter specification.
- **`from_json_file`** – Load a parameteriser from a file with a JSON serialisation.
- **`make_state_init_parameteriser`** – Converts this parameteriser into a StateInitParameteriser.
- **`num_free_parameters`** – Number of free parameters in this hypercube parameteriser
- **`score_for_objective`** – Computes the value of an objective for this given set of parameters
- **`set_hypercube`** – Updates parameter properties for an existing parameteriser.
- **`set_max_parameter_value`** – Sets the value(s) of the upper bound of one or more parameter(s)
- **`set_min_parameter_value`** – Sets the value(s) of the lower bound of one or more parameter(s)
- **`set_parameter_definition`** – Sets the feasible range and value for a parameter
- **`set_parameter_value`** – Sets the value(s) of one or more parameter(s)
- **`subcatchment_parameteriser`** – Create a parameteriser that gets applied to a subset of a whole catchment
- **`supports_thread_safe_cloning`** – Is this parameteriser clonable as a deep copy, safe for multi-threading?
- **`to_json_file`** – Save this parameteriser to a file with a JSON serialisation.
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

Adds a mathematical transformation to a parameter for optimisation in transformed space.

This allows you to define a virtual parameter (e.g., log_X) that gets optimised instead of the original parameter X. The transformation is automatically inverted when applying parameters to the simulation. Common use cases include log transforms for strictly positive parameters or arcsinh for parameters that can be negative.

Parameters:

- **`param_name`** (`str`) – Name of the new transformed parameter (e.g., 'log_x4'). This is what the optimiser will see and adjust. Should differ from inner_param_name to avoid confusion.
- **`inner_param_name`** (`str`) – Name of the underlying parameter being transformed (e.g., 'x4'). Must already exist in the parameteriser.
- **`transform_id`** (`str`) – Identifier for the transformation function. Available options as of 2025-11:
  - 'log10': Base-10 logarithm (for positive parameters, or made positive via a and b)
  - '10\*\*x': Base-10 exponentiation (inverse of log10)
  - '1/x': Reciprocal
  - 'x': Identity (no transformation). Structurally useful in edge cases but normally not needed.
  - 'asinh': Inverse hyperbolic sine
  - 'sinh': Hyperbolic sine
  - 'atanh': Inverse hyperbolic tangent
  - 'tanh': Hyperbolic tangent
  - 'sqrt': Square root (for non-negative parameters or made non-negative via a and b)
  - 'square': square function
  - 'logit': Logit function (for parameters in (0,1))
- **`a`** (`float`, default: `1.0` ) – Scaling factor applied before transformation: Y = F(a\*x + b). Defaults to 1.0.
- **`b`** (`float`, default: `0.0` ) – Offset applied before transformation: Y = F(a\*x + b). Defaults to 0.0.

Note

After transformation, the optimiser works with param_name, but the simulation receives the back-transformed values for inner_param_name. Use backtransform() to retrieve parameters in the original space.

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
from_dataframe(type: str = 'Generic subareas', definition: Optional[DataFrame] = None) -> HypercubeParameteriser
```

Creates a parameteriser from a parameter specification.

Factory method to create different types of parameterisers based on the 'type' string. The type determines which model elements (subareas, links, nodes) the parameters will be applied to.

Parameters:

- **`type`** (`str`, default: `'Generic subareas'` ) – Parameteriser type identifier (case-insensitive). Valid options:
  - 'generic' or 'generic subareas': Apply to all subareas (default)
  - 'links' or 'generic links': Apply to channel routing in links
  - 'nodes' or 'generic nodes': Apply to nodes
  - 'muskingum': Muskingum channel routing parameters
  - 'log-likelihood': Parameters for log-likelihood transformation (advanced) Defaults to "Generic subareas".
- **`definition`** (`DataFrame`, default: `None` ) – Parameter specifications with columns:
  - 'Name': Parameter name (e.g., 'x1', 'x2', 'alpha')
  - 'Min': Minimum feasible value
  - 'Max': Maximum feasible value
  - 'Value': Initial/current value If None, creates an empty parameteriser that can be populated later. Defaults to None.

Returns:

- **`HypercubeParameteriser`** ( `HypercubeParameteriser` ) – New parameteriser configured according to the type.

Examples:

```
>>> # Create GR4J parameters for subareas
>>> import pandas as pd
>>> from swift2.utils import c
>>> pspec = pd.DataFrame({
...     'Name': c('x1', 'x2', 'x3', 'x4'),
...     'Value': c(350, -0.5, 50, 2),
...     'Min': c(1, -27, 1, 1),
...     'Max': c(3000, 27, 1000, 240)
... })
>>> p = HypercubeParameteriser.from_dataframe('generic subareas', pspec)
```

```
>>> # Create link routing parameters
>>> link_spec = pd.DataFrame({
...     'Name': c('alpha', 'inverse_velocity'),
...     'Value': c(1, 1),
...     'Min': c(1e-3, 1e-3),
...     'Max': c(1e2, 1e2)
... })
>>> p_links = HypercubeParameteriser.from_dataframe('generic links', link_spec)
```

```
>>> # Create empty parameteriser to populate later
>>> p_empty = HypercubeParameteriser.from_dataframe('generic')
>>> p_empty.add_parameter_to_hypercube('x1', value=350, min=1, max=3000)
```

### from_json_file

```
from_json_file(file_path: str) -> HypercubeParameteriser
```

Load a parameteriser from a file with a JSON serialisation.

Parameters:

- **`file_path`** (`str`) – file path to load from

Returns:

- **`HypercubeParameteriser`** ( `HypercubeParameteriser` ) – loaded parameteriser

### make_state_init_parameteriser

```
make_state_init_parameteriser() -> StateInitParameteriser
```

Converts this parameteriser into a StateInitParameteriser.

Creates a StateInitParameteriser object that can be applied to simulations to set initial model states based on parameter values, as part of an optimisation process i.e. optimising some initial states. This is typically the subsequent step after defining scaled parameter relationships using ScalingParameteriser methods, and before inclusion in an optimisation workflow.

Returns:

- **`StateInitParameteriser`** ( `StateInitParameteriser` ) – Parameteriser with features to set model initial states via state initialisers,
- `StateInitParameteriser` – overriding the default simulation for model reset of initial states.

Typical Workflow

1. Create a ScalingParameteriser with linear_parameteriser() or linear_parameteriser_from()
1. Define relationships between virtual parameters and model states
1. Call make_state_init_parameteriser() to create the StateInitParameteriser
1. Use the StateInitParameteriser in an optimisation or sensitivity analysis workflow

Use Cases

- Setting initial soil moisture as a fraction of maximum capacity (S0 = 0.9 * x1 for GR4J)
- Initialising routing stores as fractions of their capacities
- Calibrating initial states alongside model parameters
- Ensuring physically consistent initial conditions

Note

The scaling variables (e.g., x1, x3) must exist as parameters in the simulation's model. If they don't exist or have incompatible dimensions, an error will occur when the initialiser is applied during simulation execution.

Examples:

```
>>> # Use case: Set gr4j initial stores at simulation as a function of x1/x3 parameters.
>>> # and calibrate both model parameters and the virtual initial state parameters S0 and R0.
>>> # `some_other_parameteriser` may be a parameteriser for GR4J parameters x1 to x4.
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
>>> parameteriser = sp.concatenate_parameterisers(some_other_parameteriser, init_parameteriser)
>>> # Now use 'parameteriser' in an optimisation workflow to calibrate both model parameters and initial states.
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

Updates parameter properties for an existing parameteriser.

Modifies the bounds and values of parameters already defined in this parameteriser. Unlike from_dataframe() which creates a new parameteriser, this method updates the current one. All parameter names in the specs must already exist in the parameteriser.

Parameters:

- **`specs`** (`DataFrame`) – Parameter specifications with columns:
  - 'Name': Parameter name (must match existing parameters)
  - 'Min': New minimum feasible value
  - 'Max': New maximum feasible value
  - 'Value': New initial/current value All columns are required for each parameter being updated.

Raises:

- `Exception` – If any parameter name in specs doesn't exist in this parameteriser.

Note

This is useful for adjusting parameter bounds after initial creation, such as converting time-step-dependent parameters (e.g., GR4J x4 from hours to days) or tightening bounds based on prior calibration results.

Examples:

```
>>> # Create GR4J parameteriser with default hourly time step
>>> p = HypercubeParameteriser.from_dataframe('generic subareas', gr4j_hourly_spec)
>>> 
>>> # Convert x4 bounds from hours to days for daily time step
>>> p_x4_daily = pd.DataFrame({
...     'Name': ['x4'],
...     'Value': [1.0],
...     'Min': [0.25],
...     'Max': [10.0]  # 10 days instead of 240 hours
... })
>>> p.set_hypercube(p_x4_daily)
```

```
>>> # Update multiple parameters after preliminary calibration
>>> tighter_bounds = pd.DataFrame({
...     'Name': ['x1', 'x3'],
...     'Value': [450, 75],
...     'Min': [300, 50],
...     'Max': [600, 100]
... })
>>> p.set_hypercube(tighter_bounds)
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
subcatchment_parameteriser(subcatchment: Simulation) -> HypercubeParameteriser
```

Create a parameteriser that gets applied to a subset of a whole catchment

Parameters:

- **`subcatchment`** (`Simulation`) – the subcatchment, subset of a whole catchment, identifying which elements (subareas, nodes, links) will be parameterised by the new parameteriser. Other catchment elements are untouched.

Returns:

- **`HypercubeParameteriser`** ( `HypercubeParameteriser` ) – New parameteriser whose application is limited to the subcatchment.

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

### to_json_file

```
to_json_file(file_path: str) -> None
```

Save this parameteriser to a file with a JSON serialisation.

Parameters:

- **`file_path`** (`str`) – file path to save to

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

Collection of multiple ObjectiveScores, typically a capture of a from a population-based optimizer's iteration.

Note: **ALWAYS** use `get_best_score` to retrieve the 'best' score, as the order of scores in this collection is NOT guaranteed.

Methods:

- **`as_dataframe`** –
- **`get_best_score`** – Get the best ObjectiveScores in the collection based on a specified score.
- **`get_parameters_at_index`** – Get the parameteriser at a given index in the collection.
- **`get_score_at_index`** – Get the ObjectiveScores at a given index in the collection.
- **`sort_by_score`** – Sort the collection of ObjectiveScores based on a specified score.

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
get_best_score(score_name: str = '', convert_to_py: bool = False) -> Dict[str, Any] | ObjectiveScores
```

Get the best ObjectiveScores in the collection based on a specified score.

Parameters:

- **`score_name`** (`str`, default: `''` ) – The name of the score to evaluate for best performance. Defaults to "", which expects a single score per item (single objective optimisation).
- **`convert_to_py`** (`bool`, default: `False` ) – If True, returns a Python dictionary representation instead of an ObjectiveScores object. Defaults to False.

Returns:

- `Dict[str, Any] | ObjectiveScores` – Dict[str, Any] | ObjectiveScores: The best ObjectiveScores or its Python dictionary representation.

### get_parameters_at_index

```
get_parameters_at_index(index: int) -> HypercubeParameteriser
```

Get the parameteriser at a given index in the collection.

Note: Indexing is ONE-based. Also do NOT rely on the order of scores in this collection, as terminated optimisers may not guarantee any specific ordering. use `get_best_score()` to get the best one instead and retrieve its parameteriser.

Parameters:

- **`index`** (`int`) – one based index

Returns:

- **`HypercubeParameteriser`** ( `HypercubeParameteriser` ) – the parameteriser at the given index

### get_score_at_index

```
get_score_at_index(index: int) -> ObjectiveScores
```

Get the ObjectiveScores at a given index in the collection.

Note: Indexing is ONE-based. Also do NOT rely on the order of scores in this collection, as terminated optimisers may not guarantee any specific ordering. use `get_best_score()` to get the best one instead.

Parameters:

- **`index`** (`int`) – one based index

Returns:

- **`ObjectiveScores`** ( `ObjectiveScores` ) – the ObjectiveScores at the given index

### sort_by_score

```
sort_by_score(score_name: str = '') -> VectorObjectiveScores
```

Sort the collection of ObjectiveScores based on a specified score.

Parameters:

- **`score_name`** (`str`, default: `''` ) – The name of the score to evaluate for best performance. Defaults to "", which expects a single score per item (single objective optimisation).

Returns:

- **`VectorObjectiveScores`** ( `VectorObjectiveScores` ) – A new VectorObjectiveScores instance sorted by the specified score.

## wrap_cffi_native_handle

```
wrap_cffi_native_handle(obj: Any, type_id: str, release_native: Callable)
```
