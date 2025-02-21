## swift2

Tools for manipulating LakeOneD models and data and for running
SWIFT from Python.

**Modules:**

- [**classes**](#swift2.classes) –
- [**common**](#swift2.common) –
- [**const**](#swift2.const) –
- [**doc_helper**](#swift2.doc_helper) –
- [**helpers**](#swift2.helpers) –
- [**internal**](#swift2.internal) –
- [**model_definitions**](#swift2.model_definitions) –
- [**parameteriser**](#swift2.parameteriser) –
- [**play_record**](#swift2.play_record) –
- [**proto**](#swift2.proto) – Prototypes
- [**prototypes**](#swift2.prototypes) –
- [**simulation**](#swift2.simulation) –
- [**statistics**](#swift2.statistics) –
- [**system**](#swift2.system) –
- [**utils**](#swift2.utils) –
- [**vis**](#swift2.vis) –
- [**wrap**](#swift2.wrap) – CFFI based wrapper for the SWIFT2 native library

### swift2.classes

**Classes:**

- [**CandidateFactorySeed**](#swift2.classes.CandidateFactorySeed) –
- [**CompositeParameteriser**](#swift2.classes.CompositeParameteriser) – A parameteriser defined as the concatenation of several parameterisers
- [**ConstraintParameteriser**](#swift2.classes.ConstraintParameteriser) –
- [**EnsembleForecastSimulation**](#swift2.classes.EnsembleForecastSimulation) –
- [**EnsembleSimulation**](#swift2.classes.EnsembleSimulation) – A simulation designed to facilitate model runs over ensemble of inputs
- [**ErrisStagedCalibration**](#swift2.classes.ErrisStagedCalibration) –
- [**FilteringParameteriser**](#swift2.classes.FilteringParameteriser) –
- [**FunctionsParameteriser**](#swift2.classes.FunctionsParameteriser) –
- [**HypercubeParameteriser**](#swift2.classes.HypercubeParameteriser) –
- [**MaerrisStagedCalibration**](#swift2.classes.MaerrisStagedCalibration) –
- [**MemoryStates**](#swift2.classes.MemoryStates) –
- [**ObjectiveEvaluator**](#swift2.classes.ObjectiveEvaluator) – Objective Evaluator
- [**ObjectiveScores**](#swift2.classes.ObjectiveScores) –
- [**Optimiser**](#swift2.classes.Optimiser) –
- [**Parameteriser**](#swift2.classes.Parameteriser) – Wrapper around a native parameteriser.
- [**ScalingParameteriser**](#swift2.classes.ScalingParameteriser) –
- [**SceTerminationCondition**](#swift2.classes.SceTerminationCondition) –
- [**Simulation**](#swift2.classes.Simulation) – Wrapper around single dimension simulation objects
- [**SimulationMixin**](#swift2.classes.SimulationMixin) – A parent class for simulation objects. Most users are unlikely to explicitly use it.
- [**StateInitParameteriser**](#swift2.classes.StateInitParameteriser) –
- [**StateInitialiser**](#swift2.classes.StateInitialiser) –
- [**TransformParameteriser**](#swift2.classes.TransformParameteriser) –
- [**VectorObjectiveScores**](#swift2.classes.VectorObjectiveScores) –

**Functions:**

- [**wrap_cffi_native_handle**](#swift2.classes.wrap_cffi_native_handle) –

#### swift2.classes.CandidateFactorySeed

```python
CandidateFactorySeed(handle, release_native, type_id=None, prior_ref_count=0)
```

Bases: <code>[DeletableCffiNativeHandle](#refcount.interop.DeletableCffiNativeHandle)</code>

#### swift2.classes.CompositeParameteriser

```python
CompositeParameteriser(handle, release_native, type_id=None, prior_ref_count=0)
```

Bases: <code>[HypercubeParameteriser](#swift2.classes.HypercubeParameteriser)</code>

A parameteriser defined as the concatenation of several parameterisers

**Functions:**

- [**add_parameter_to_hypercube**](#swift2.classes.CompositeParameteriser.add_parameter_to_hypercube) – Add a parameter to a hypercube. Must be a type of object that is expandable, otherwise may raise an exception
- [**add_to_hypercube**](#swift2.classes.CompositeParameteriser.add_to_hypercube) – Add entries to a hypercube. Must be a type of object that is expandable, otherwise may raise an exception.
- [**append**](#swift2.classes.CompositeParameteriser.append) – Append a parameteriser to this composite parameteriser
- [**apply_sys_config**](#swift2.classes.CompositeParameteriser.apply_sys_config) – Apply a model configuration to a simulation
- [**as_dataframe**](#swift2.classes.CompositeParameteriser.as_dataframe) – Convert this hypercube parameteriser to a pandas data frame representation
- [**backtransform**](#swift2.classes.CompositeParameteriser.backtransform) – Get the parameteriser values in the untransformed space
- [**clone**](#swift2.classes.CompositeParameteriser.clone) –
- [**concatenate**](#swift2.classes.CompositeParameteriser.concatenate) – Concatenates some hypercubes to a single parameteriser
- [**create_parameter_sampler**](#swift2.classes.CompositeParameteriser.create_parameter_sampler) – Creates a sampler for this parameteriser
- [**empty_composite**](#swift2.classes.CompositeParameteriser.empty_composite) – Creates an empty parameteriser to be populated with other parameterisers
- [**filtered_parameters**](#swift2.classes.CompositeParameteriser.filtered_parameters) – Wrap a parameteriser in a filter that can hide some parameters
- [**from_dataframe**](#swift2.classes.CompositeParameteriser.from_dataframe) – Create a parameteriser
- [**hide_parameters**](#swift2.classes.CompositeParameteriser.hide_parameters) – Hide some parameters (from the outside e.g. optimisers) in a filter parameteriser
- [**make_state_init_parameteriser**](#swift2.classes.CompositeParameteriser.make_state_init_parameteriser) – Create a parameteriser used for model state initialisation
- [**num_free_parameters**](#swift2.classes.CompositeParameteriser.num_free_parameters) – Number of free parameters in this hypercube parameteriser
- [**score_for_objective**](#swift2.classes.CompositeParameteriser.score_for_objective) – Computes the value of an objective for this given set of parameters
- [**set_hypercube**](#swift2.classes.CompositeParameteriser.set_hypercube) – Set the properties of a hypercube parameteriser
- [**set_max_parameter_value**](#swift2.classes.CompositeParameteriser.set_max_parameter_value) – Sets the value(s) of the upper bound of one or more parameter(s)
- [**set_min_parameter_value**](#swift2.classes.CompositeParameteriser.set_min_parameter_value) – Sets the value(s) of the lower bound of one or more parameter(s)
- [**set_parameter_definition**](#swift2.classes.CompositeParameteriser.set_parameter_definition) – Sets the feasible range and value for a parameter
- [**set_parameter_value**](#swift2.classes.CompositeParameteriser.set_parameter_value) – Sets the value(s) of one or more parameter(s)
- [**show_parameters**](#swift2.classes.CompositeParameteriser.show_parameters) – Show some parameters (from the outside e.g. optimisers) in a filter parameteriser
- [**subcatchment_parameteriser**](#swift2.classes.CompositeParameteriser.subcatchment_parameteriser) – Create a parameteriser that gets applied to a subset of a whole catchment
- [**supports_thread_safe_cloning**](#swift2.classes.CompositeParameteriser.supports_thread_safe_cloning) – Is this parameteriser clonable as a deep copy, safe for multi-threading?
- [**wrap_transform**](#swift2.classes.CompositeParameteriser.wrap_transform) – Create a parameteriser for which parameter transformations can be defined.

##### swift2.classes.CompositeParameteriser.add_parameter_to_hypercube

```python
add_parameter_to_hypercube(name, value, min, max)
```

Add a parameter to a hypercube. Must be a type of object that is expandable, otherwise may raise an exception

##### swift2.classes.CompositeParameteriser.add_to_hypercube

```python
add_to_hypercube(specs)
```

Add entries to a hypercube. Must be a type of object that is expandable, otherwise may raise an exception.

**Parameters:**

- **specs** (<code>[DataFrame](#pandas.DataFrame)</code>) – An optional data frame description of the parameter set, with at least columns Name, Min, Max, Value.

##### swift2.classes.CompositeParameteriser.append

```python
append(p)
```

Append a parameteriser to this composite parameteriser

**Parameters:**

- **p** (<code>[HypercubeParameteriser](#swift2.classes.HypercubeParameteriser)</code>) – hypercube to append to this

##### swift2.classes.CompositeParameteriser.apply_sys_config

```python
apply_sys_config(simulation)
```

Apply a model configuration to a simulation

**Parameters:**

- **simulation** (<code>[Simulation](#swift2.classes.Simulation)</code>) – simulation

##### swift2.classes.CompositeParameteriser.as_dataframe

```python
as_dataframe()
```

Convert this hypercube parameteriser to a pandas data frame representation

**Returns:**

- <code>[DataFrame](#pandas.DataFrame)</code> – pd.DataFrame: pandas data frame

##### swift2.classes.CompositeParameteriser.backtransform

```python
backtransform()
```

Get the parameteriser values in the untransformed space

Get the parameteriser values in the untransformed space, i.e. remove any
transform added via \[`HypercubeParameteriser.wrap_transform`\][HypercubeParameteriser.wrap_transform].
This allows to transform back e.g. from a virtual parameter log_X
to the underlying model (or even virtual/meta) parameter X.

**Returns:**

- **HypercubeParameteriser** (<code>[HypercubeParameteriser](#swift2.classes.HypercubeParameteriser)</code>) – The parameters definitions without the transforms (if there are any)

**Examples:**

```pycon
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

##### swift2.classes.CompositeParameteriser.clone

```python
clone()
```

##### swift2.classes.CompositeParameteriser.concatenate

```python
concatenate(*args, strategy='')
```

Concatenates some hypercubes to a single parameteriser

**Parameters:**

- **strategy** (<code>[str](#str)</code>) – The strategy to contatenate. Defaults to "", equivalent to "composite", the only available. May have other options in the future.

**Returns:**

- **CompositeParameteriser** (<code>[CompositeParameteriser](#swift2.classes.CompositeParameteriser)</code>) – A concatenated parameteriser

##### swift2.classes.CompositeParameteriser.create_parameter_sampler

```python
create_parameter_sampler(seed=0, type='urs')
```

Creates a sampler for this parameteriser

**Parameters:**

- **seed** (<code>[int](#int)</code>) – a seed for the sampler. Defaults to 0.
- **type** (<code>[str](#str)</code>) – the type of sampler. Defaults to "urs". Only option supported as of 2023-01.

**Returns:**

- **CandidateFactorySeed** (<code>[CandidateFactorySeed](#swift2.classes.CandidateFactorySeed)</code>) – a sampler, aka candidate factory

##### swift2.classes.CompositeParameteriser.empty_composite

```python
empty_composite()
```

Creates an empty parameteriser to be populated with other parameterisers

**Returns:**

- **CompositeParameteriser** (<code>[CompositeParameteriser](#swift2.classes.CompositeParameteriser)</code>) – composite parameteriser

##### swift2.classes.CompositeParameteriser.filtered_parameters

```python
filtered_parameters()
```

Wrap a parameteriser in a filter that can hide some parameters

##### swift2.classes.CompositeParameteriser.from_dataframe

```python
from_dataframe(type='Generic subareas', definition=None)
```

Create a parameteriser

**Parameters:**

- **type** (<code>[str](#str)</code>) – A string identifying the type of parameteriser to use. Recognised types are (case insensitive) 'log-likelihood', 'generic', 'subareas', 'links', 'nodes' and 'muskingum'. Defaults to "Generic subareas".
- **specs** (<code>[DataFrame](#pandas.DataFrame)</code>) – An optional data frame description of the parameter set, with at least columns Name, Min, Max, Value. Defaults to None.

**Returns:**

- **HypercubeParameteriser** (<code>[HypercubeParameteriser](#swift2.classes.HypercubeParameteriser)</code>) – new parameteriser

**Examples:**

```pycon
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

##### swift2.classes.CompositeParameteriser.hide_parameters

```python
hide_parameters(patterns, regex=False, starts_with=False, strict=False)
```

Hide some parameters (from the outside e.g. optimisers) in a filter parameteriser

**Parameters:**

- **patterns** (<code>\[[type](#type)\]</code>) – character, one or more pattern to match and hide matching parameters. Match according to other parameters.
- **regex** (<code>[bool](#bool)</code>) – logical, defaults False, should the patterns be used as regular expressions.. Defaults to False.
- **starts_with** (<code>[bool](#bool)</code>) – logical, defaults False. Ignored if regex is True. Should the patterns be used as starting strings in the parameter names.. Defaults to False.
- **strict** (<code>[bool](#bool)</code>) – logical, default False. Used only if regex and starts_with are False. If True, raises an error if one of the "patterns" has no exact match in the parameters.. Defaults to False.

##### swift2.classes.CompositeParameteriser.make_state_init_parameteriser

```python
make_state_init_parameteriser()
```

Create a parameteriser used for model state initialisation

This allows to define tied parameters where, for instance, pval = a * modelStateVal.
A more concrete use case is to define an initial soil moisture store 'S0',
as a fraction of the model store capacity 'Smax'.
The model state to initialise is 'S'

<details class="note" open>
<summary>Note</summary>
See also [swift2.classes.ScalingParameteriser][] for typical joint usage.
</details>

**Returns:**

- **StateInitParameteriser** (<code>[StateInitParameteriser](#swift2.classes.StateInitParameteriser)</code>) – state initialisation parameteriser

**Examples:**

```pycon
>>> todo()
```

##### swift2.classes.CompositeParameteriser.num_free_parameters

```python
num_free_parameters()
```

Number of free parameters in this hypercube parameteriser

**Returns:**

- **int** (<code>[int](#int)</code>) – Number of free parameters

##### swift2.classes.CompositeParameteriser.score_for_objective

```python
score_for_objective(objective)
```

Computes the value of an objective for this given set of parameters

##### swift2.classes.CompositeParameteriser.set_hypercube

```python
set_hypercube(specs)
```

Set the properties of a hypercube parameteriser

**Parameters:**

- **specs** (<code>[DataFrame](#pandas.DataFrame)</code>) – An optional data frame description of the parameter set, with at least columns Name, Min, Max, Value.

##### swift2.classes.CompositeParameteriser.set_max_parameter_value

```python
set_max_parameter_value(variable_name, value)
```

Sets the value(s) of the upper bound of one or more parameter(s)

**Parameters:**

- **variable_name** (<code>[VecStr](#swift2.const.VecStr)</code>) – one or more parameter name(s)
- **value** (<code>[VecScalars](#swift2.const.VecScalars)</code>) – one or more parameter value(s)

##### swift2.classes.CompositeParameteriser.set_min_parameter_value

```python
set_min_parameter_value(variable_name, value)
```

Sets the value(s) of the lower bound of one or more parameter(s)

**Parameters:**

- **variable_name** (<code>[VecStr](#swift2.const.VecStr)</code>) – one or more parameter name(s)
- **value** (<code>[VecScalars](#swift2.const.VecScalars)</code>) – one or more parameter value(s)

##### swift2.classes.CompositeParameteriser.set_parameter_definition

```python
set_parameter_definition(variable_name, min, max, value)
```

Sets the feasible range and value for a parameter

**Parameters:**

- **variable_name** (<code>[str](#str)</code>) – parameter name
- **min** (<code>[float](#float)</code>) – min
- **max** (<code>[float](#float)</code>) – max
- **value** (<code>[float](#float)</code>) – value

##### swift2.classes.CompositeParameteriser.set_parameter_value

```python
set_parameter_value(variable_name, value)
```

Sets the value(s) of one or more parameter(s)

**Parameters:**

- **variable_name** (<code>[VecStr](#swift2.const.VecStr)</code>) – one or more parameter name(s)
- **value** (<code>[VecScalars](#swift2.const.VecScalars)</code>) – one or more parameter value(s)

##### swift2.classes.CompositeParameteriser.show_parameters

```python
show_parameters(patterns, regex=False, starts_with=False)
```

Show some parameters (from the outside e.g. optimisers) in a filter parameteriser

**Parameters:**

- **patterns** (<code>\[[type](#type)\]</code>) – character, one or more pattern to match and show matching parameters. Match according to other parameters
- **regex** (<code>[bool](#bool)</code>) – should the patterns be used as regular expressions. Defaults to False.
- **starts_with** (<code>[bool](#bool)</code>) – should the patterns be used as starting strings in the parameter names. Defaults to False.

##### swift2.classes.CompositeParameteriser.subcatchment_parameteriser

```python
subcatchment_parameteriser(subcatchment)
```

Create a parameteriser that gets applied to a subset of a whole catchment

**Parameters:**

- **subcatchment** (<code>[Simulation](#swift2.classes.Simulation)</code>) – the subcatchment, subset of a whole catchment, identifying which elements (subareas, nodes, links) will be parameterised by the new parameteriser. Other catchment elements are untouched.

**Returns:**

- **HypercubeParameteriser** – New parameteriser whose application is limited to the subcatchment.

**Examples:**

```pycon
>>> sub_cats = simulation.split_to_subcatchments(["node.node_7", "node.node_10"])
>>> sc = sub_cats["node.node_7"]
>>> p = sp.create_parameteriser('generic subarea')
>>> p.add_parameter_to_hypercube("x1", 32, 1, 6e3)
>>> sp = p.subcatchment_parameteriser(sc)
>>> sp.apply_sys_config(simulation)
```

##### swift2.classes.CompositeParameteriser.supports_thread_safe_cloning

```python
supports_thread_safe_cloning()
```

Is this parameteriser clonable as a deep copy, safe for multi-threading?

##### swift2.classes.CompositeParameteriser.wrap_transform

```python
wrap_transform()
```

Create a parameteriser for which parameter transformations can be defined.

This allows to define e.g. a virtual parameter log_X instead of calibrating on the parameter X.

**Returns:**

- **TransformParameteriser** (<code>[TransformParameteriser](#swift2.classes.TransformParameteriser)</code>) – A new parameteriser (TransformParameteriser) which has methods to define parameter transforms

#### swift2.classes.ConstraintParameteriser

```python
ConstraintParameteriser(handle, release_native, type_id=None, prior_ref_count=0)
```

Bases: <code>[HypercubeParameteriser](#swift2.classes.HypercubeParameteriser)</code>

**Functions:**

- [**add_parameter_to_hypercube**](#swift2.classes.ConstraintParameteriser.add_parameter_to_hypercube) – Add a parameter to a hypercube. Must be a type of object that is expandable, otherwise may raise an exception
- [**add_to_hypercube**](#swift2.classes.ConstraintParameteriser.add_to_hypercube) – Add entries to a hypercube. Must be a type of object that is expandable, otherwise may raise an exception.
- [**apply_sys_config**](#swift2.classes.ConstraintParameteriser.apply_sys_config) – Apply a model configuration to a simulation
- [**as_dataframe**](#swift2.classes.ConstraintParameteriser.as_dataframe) – Convert this hypercube parameteriser to a pandas data frame representation
- [**backtransform**](#swift2.classes.ConstraintParameteriser.backtransform) – Get the parameteriser values in the untransformed space
- [**clone**](#swift2.classes.ConstraintParameteriser.clone) –
- [**create_parameter_sampler**](#swift2.classes.ConstraintParameteriser.create_parameter_sampler) – Creates a sampler for this parameteriser
- [**filtered_parameters**](#swift2.classes.ConstraintParameteriser.filtered_parameters) – Wrap a parameteriser in a filter that can hide some parameters
- [**from_dataframe**](#swift2.classes.ConstraintParameteriser.from_dataframe) – Create a parameteriser
- [**hide_parameters**](#swift2.classes.ConstraintParameteriser.hide_parameters) – Hide some parameters (from the outside e.g. optimisers) in a filter parameteriser
- [**make_state_init_parameteriser**](#swift2.classes.ConstraintParameteriser.make_state_init_parameteriser) – Create a parameteriser used for model state initialisation
- [**num_free_parameters**](#swift2.classes.ConstraintParameteriser.num_free_parameters) – Number of free parameters in this hypercube parameteriser
- [**score_for_objective**](#swift2.classes.ConstraintParameteriser.score_for_objective) – Computes the value of an objective for this given set of parameters
- [**set_hypercube**](#swift2.classes.ConstraintParameteriser.set_hypercube) – Set the properties of a hypercube parameteriser
- [**set_max_parameter_value**](#swift2.classes.ConstraintParameteriser.set_max_parameter_value) – Sets the value(s) of the upper bound of one or more parameter(s)
- [**set_min_parameter_value**](#swift2.classes.ConstraintParameteriser.set_min_parameter_value) – Sets the value(s) of the lower bound of one or more parameter(s)
- [**set_parameter_definition**](#swift2.classes.ConstraintParameteriser.set_parameter_definition) – Sets the feasible range and value for a parameter
- [**set_parameter_value**](#swift2.classes.ConstraintParameteriser.set_parameter_value) – Sets the value(s) of one or more parameter(s)
- [**show_parameters**](#swift2.classes.ConstraintParameteriser.show_parameters) – Show some parameters (from the outside e.g. optimisers) in a filter parameteriser
- [**subcatchment_parameteriser**](#swift2.classes.ConstraintParameteriser.subcatchment_parameteriser) – Create a parameteriser that gets applied to a subset of a whole catchment
- [**supports_thread_safe_cloning**](#swift2.classes.ConstraintParameteriser.supports_thread_safe_cloning) – Is this parameteriser clonable as a deep copy, safe for multi-threading?
- [**wrap_transform**](#swift2.classes.ConstraintParameteriser.wrap_transform) – Create a parameteriser for which parameter transformations can be defined.

##### swift2.classes.ConstraintParameteriser.add_parameter_to_hypercube

```python
add_parameter_to_hypercube(name, value, min, max)
```

Add a parameter to a hypercube. Must be a type of object that is expandable, otherwise may raise an exception

##### swift2.classes.ConstraintParameteriser.add_to_hypercube

```python
add_to_hypercube(specs)
```

Add entries to a hypercube. Must be a type of object that is expandable, otherwise may raise an exception.

**Parameters:**

- **specs** (<code>[DataFrame](#pandas.DataFrame)</code>) – An optional data frame description of the parameter set, with at least columns Name, Min, Max, Value.

##### swift2.classes.ConstraintParameteriser.apply_sys_config

```python
apply_sys_config(simulation)
```

Apply a model configuration to a simulation

**Parameters:**

- **simulation** (<code>[Simulation](#swift2.classes.Simulation)</code>) – simulation

##### swift2.classes.ConstraintParameteriser.as_dataframe

```python
as_dataframe()
```

Convert this hypercube parameteriser to a pandas data frame representation

**Returns:**

- <code>[DataFrame](#pandas.DataFrame)</code> – pd.DataFrame: pandas data frame

##### swift2.classes.ConstraintParameteriser.backtransform

```python
backtransform()
```

Get the parameteriser values in the untransformed space

Get the parameteriser values in the untransformed space, i.e. remove any
transform added via \[`HypercubeParameteriser.wrap_transform`\][HypercubeParameteriser.wrap_transform].
This allows to transform back e.g. from a virtual parameter log_X
to the underlying model (or even virtual/meta) parameter X.

**Returns:**

- **HypercubeParameteriser** (<code>[HypercubeParameteriser](#swift2.classes.HypercubeParameteriser)</code>) – The parameters definitions without the transforms (if there are any)

**Examples:**

```pycon
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

##### swift2.classes.ConstraintParameteriser.clone

```python
clone()
```

##### swift2.classes.ConstraintParameteriser.create_parameter_sampler

```python
create_parameter_sampler(seed=0, type='urs')
```

Creates a sampler for this parameteriser

**Parameters:**

- **seed** (<code>[int](#int)</code>) – a seed for the sampler. Defaults to 0.
- **type** (<code>[str](#str)</code>) – the type of sampler. Defaults to "urs". Only option supported as of 2023-01.

**Returns:**

- **CandidateFactorySeed** (<code>[CandidateFactorySeed](#swift2.classes.CandidateFactorySeed)</code>) – a sampler, aka candidate factory

##### swift2.classes.ConstraintParameteriser.filtered_parameters

```python
filtered_parameters()
```

Wrap a parameteriser in a filter that can hide some parameters

##### swift2.classes.ConstraintParameteriser.from_dataframe

```python
from_dataframe(type='Generic subareas', definition=None)
```

Create a parameteriser

**Parameters:**

- **type** (<code>[str](#str)</code>) – A string identifying the type of parameteriser to use. Recognised types are (case insensitive) 'log-likelihood', 'generic', 'subareas', 'links', 'nodes' and 'muskingum'. Defaults to "Generic subareas".
- **specs** (<code>[DataFrame](#pandas.DataFrame)</code>) – An optional data frame description of the parameter set, with at least columns Name, Min, Max, Value. Defaults to None.

**Returns:**

- **HypercubeParameteriser** (<code>[HypercubeParameteriser](#swift2.classes.HypercubeParameteriser)</code>) – new parameteriser

**Examples:**

```pycon
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

##### swift2.classes.ConstraintParameteriser.hide_parameters

```python
hide_parameters(patterns, regex=False, starts_with=False, strict=False)
```

Hide some parameters (from the outside e.g. optimisers) in a filter parameteriser

**Parameters:**

- **patterns** (<code>\[[type](#type)\]</code>) – character, one or more pattern to match and hide matching parameters. Match according to other parameters.
- **regex** (<code>[bool](#bool)</code>) – logical, defaults False, should the patterns be used as regular expressions.. Defaults to False.
- **starts_with** (<code>[bool](#bool)</code>) – logical, defaults False. Ignored if regex is True. Should the patterns be used as starting strings in the parameter names.. Defaults to False.
- **strict** (<code>[bool](#bool)</code>) – logical, default False. Used only if regex and starts_with are False. If True, raises an error if one of the "patterns" has no exact match in the parameters.. Defaults to False.

##### swift2.classes.ConstraintParameteriser.make_state_init_parameteriser

```python
make_state_init_parameteriser()
```

Create a parameteriser used for model state initialisation

This allows to define tied parameters where, for instance, pval = a * modelStateVal.
A more concrete use case is to define an initial soil moisture store 'S0',
as a fraction of the model store capacity 'Smax'.
The model state to initialise is 'S'

<details class="note" open>
<summary>Note</summary>
See also [swift2.classes.ScalingParameteriser][] for typical joint usage.
</details>

**Returns:**

- **StateInitParameteriser** (<code>[StateInitParameteriser](#swift2.classes.StateInitParameteriser)</code>) – state initialisation parameteriser

**Examples:**

```pycon
>>> todo()
```

##### swift2.classes.ConstraintParameteriser.num_free_parameters

```python
num_free_parameters()
```

Number of free parameters in this hypercube parameteriser

**Returns:**

- **int** (<code>[int](#int)</code>) – Number of free parameters

##### swift2.classes.ConstraintParameteriser.score_for_objective

```python
score_for_objective(objective)
```

Computes the value of an objective for this given set of parameters

##### swift2.classes.ConstraintParameteriser.set_hypercube

```python
set_hypercube(specs)
```

Set the properties of a hypercube parameteriser

**Parameters:**

- **specs** (<code>[DataFrame](#pandas.DataFrame)</code>) – An optional data frame description of the parameter set, with at least columns Name, Min, Max, Value.

##### swift2.classes.ConstraintParameteriser.set_max_parameter_value

```python
set_max_parameter_value(variable_name, value)
```

Sets the value(s) of the upper bound of one or more parameter(s)

**Parameters:**

- **variable_name** (<code>[VecStr](#swift2.const.VecStr)</code>) – one or more parameter name(s)
- **value** (<code>[VecScalars](#swift2.const.VecScalars)</code>) – one or more parameter value(s)

##### swift2.classes.ConstraintParameteriser.set_min_parameter_value

```python
set_min_parameter_value(variable_name, value)
```

Sets the value(s) of the lower bound of one or more parameter(s)

**Parameters:**

- **variable_name** (<code>[VecStr](#swift2.const.VecStr)</code>) – one or more parameter name(s)
- **value** (<code>[VecScalars](#swift2.const.VecScalars)</code>) – one or more parameter value(s)

##### swift2.classes.ConstraintParameteriser.set_parameter_definition

```python
set_parameter_definition(variable_name, min, max, value)
```

Sets the feasible range and value for a parameter

**Parameters:**

- **variable_name** (<code>[str](#str)</code>) – parameter name
- **min** (<code>[float](#float)</code>) – min
- **max** (<code>[float](#float)</code>) – max
- **value** (<code>[float](#float)</code>) – value

##### swift2.classes.ConstraintParameteriser.set_parameter_value

```python
set_parameter_value(variable_name, value)
```

Sets the value(s) of one or more parameter(s)

**Parameters:**

- **variable_name** (<code>[VecStr](#swift2.const.VecStr)</code>) – one or more parameter name(s)
- **value** (<code>[VecScalars](#swift2.const.VecScalars)</code>) – one or more parameter value(s)

##### swift2.classes.ConstraintParameteriser.show_parameters

```python
show_parameters(patterns, regex=False, starts_with=False)
```

Show some parameters (from the outside e.g. optimisers) in a filter parameteriser

**Parameters:**

- **patterns** (<code>\[[type](#type)\]</code>) – character, one or more pattern to match and show matching parameters. Match according to other parameters
- **regex** (<code>[bool](#bool)</code>) – should the patterns be used as regular expressions. Defaults to False.
- **starts_with** (<code>[bool](#bool)</code>) – should the patterns be used as starting strings in the parameter names. Defaults to False.

##### swift2.classes.ConstraintParameteriser.subcatchment_parameteriser

```python
subcatchment_parameteriser(subcatchment)
```

Create a parameteriser that gets applied to a subset of a whole catchment

**Parameters:**

- **subcatchment** (<code>[Simulation](#swift2.classes.Simulation)</code>) – the subcatchment, subset of a whole catchment, identifying which elements (subareas, nodes, links) will be parameterised by the new parameteriser. Other catchment elements are untouched.

**Returns:**

- **HypercubeParameteriser** – New parameteriser whose application is limited to the subcatchment.

**Examples:**

```pycon
>>> sub_cats = simulation.split_to_subcatchments(["node.node_7", "node.node_10"])
>>> sc = sub_cats["node.node_7"]
>>> p = sp.create_parameteriser('generic subarea')
>>> p.add_parameter_to_hypercube("x1", 32, 1, 6e3)
>>> sp = p.subcatchment_parameteriser(sc)
>>> sp.apply_sys_config(simulation)
```

##### swift2.classes.ConstraintParameteriser.supports_thread_safe_cloning

```python
supports_thread_safe_cloning()
```

Is this parameteriser clonable as a deep copy, safe for multi-threading?

##### swift2.classes.ConstraintParameteriser.wrap_transform

```python
wrap_transform()
```

Create a parameteriser for which parameter transformations can be defined.

This allows to define e.g. a virtual parameter log_X instead of calibrating on the parameter X.

**Returns:**

- **TransformParameteriser** (<code>[TransformParameteriser](#swift2.classes.TransformParameteriser)</code>) – A new parameteriser (TransformParameteriser) which has methods to define parameter transforms

#### swift2.classes.EnsembleForecastSimulation

```python
EnsembleForecastSimulation(handle, release_native, type_id=None, prior_ref_count=0)
```

Bases: <code>[DeletableCffiNativeHandle](#refcount.interop.DeletableCffiNativeHandle)</code>, <code>[SimulationMixin](#swift2.classes.SimulationMixin)</code>

**Functions:**

- [**exec_simulation**](#swift2.classes.EnsembleForecastSimulation.exec_simulation) – Execute a simulation
- [**get_played_varnames**](#swift2.classes.EnsembleForecastSimulation.get_played_varnames) – Gets all the names of states fed an input time series
- [**get_recorded_ensemble_forecast**](#swift2.classes.EnsembleForecastSimulation.get_recorded_ensemble_forecast) –
- [**get_recorded_varnames**](#swift2.classes.EnsembleForecastSimulation.get_recorded_varnames) – Gets all the names of the recorded states
- [**get_simulation_span**](#swift2.classes.EnsembleForecastSimulation.get_simulation_span) –
- [**record_ensemble_forecast_state**](#swift2.classes.EnsembleForecastSimulation.record_ensemble_forecast_state) –
- [**record_state**](#swift2.classes.EnsembleForecastSimulation.record_state) – Record a time series of one of the state of the model

##### swift2.classes.EnsembleForecastSimulation.exec_simulation

```python
exec_simulation(reset_initial_states=True)
```

Execute a simulation

**Parameters:**

- **reset_initial_states** (<code>[bool](#bool)</code>) – logical, should the states of the model be reinitialized before the first time step.

##### swift2.classes.EnsembleForecastSimulation.get_played_varnames

```python
get_played_varnames()
```

Gets all the names of states fed an input time series

**Returns:**

- <code>[List](#typing.List)\[[str](#str)\]</code> – List\[str\]: The names of the state variables fed over the simulation with values from a time series

##### swift2.classes.EnsembleForecastSimulation.get_recorded_ensemble_forecast

```python
get_recorded_ensemble_forecast(var_id, start_time=None, end_time=None)
```

##### swift2.classes.EnsembleForecastSimulation.get_recorded_varnames

```python
get_recorded_varnames()
```

Gets all the names of the recorded states

**Returns:**

- <code>[List](#typing.List)\[[str](#str)\]</code> – List\[str\]: The names of the state variables being recorded into time series

##### swift2.classes.EnsembleForecastSimulation.get_simulation_span

```python
get_simulation_span()
```

##### swift2.classes.EnsembleForecastSimulation.record_ensemble_forecast_state

```python
record_ensemble_forecast_state(var_ids=CATCHMENT_FLOWRATE_VARID, recording_provider=None, data_ids=None)
```

##### swift2.classes.EnsembleForecastSimulation.record_state

```python
record_state(var_ids=CATCHMENT_FLOWRATE_VARID, recording_provider=None, data_ids=None)
```

Record a time series of one of the state of the model

**Parameters:**

- **var_ids** (<code>[VecStr](#swift2.const.VecStr)</code>) – identifier(s) of the output variable recorded to a time series, e.g. 'Catchment|StreamflowRate' or 'subcatchment.Subarea.runoff'. Defaults to CATCHMENT_FLOWRATE_VARID.
- **recording_provider** (<code>[TimeSeriesLibrary](#uchronia.classes.TimeSeriesLibrary)</code>) – _description_. Defaults to None.
- **data_ids** (<code>[VecStr](#swift2.const.VecStr)</code>) – _description_. Defaults to None.

**Raises:**

- <code>[ValueError](#ValueError)</code> – _description_

#### swift2.classes.EnsembleSimulation

```python
EnsembleSimulation(handle, release_native, type_id=None, prior_ref_count=0)
```

Bases: <code>[DeletableCffiNativeHandle](#refcount.interop.DeletableCffiNativeHandle)</code>

A simulation designed to facilitate model runs over ensemble of inputs

**Functions:**

- [**get_simulation_span**](#swift2.classes.EnsembleSimulation.get_simulation_span) – Gets the span of the simulation: start, end, time step
- [**record**](#swift2.classes.EnsembleSimulation.record) – Records a state variable of the simualtion
- [**record_ensemble_state**](#swift2.classes.EnsembleSimulation.record_ensemble_state) – Records one or more state values from an ensemble simulation
- [**setup**](#swift2.classes.EnsembleSimulation.setup) – Sets up this ensemble simulation

##### swift2.classes.EnsembleSimulation.get_simulation_span

```python
get_simulation_span()
```

Gets the span of the simulation: start, end, time step

**Returns:**

- <code>[Dict](#typing.Dict)\[[str](#str), [Any](#typing.Any)\]</code> – Dict\[str, Any\]: simulation span

##### swift2.classes.EnsembleSimulation.record

```python
record(variable_id)
```

Records a state variable of the simualtion

**Parameters:**

- **variable_id** (<code>[str](#str)</code>) – state variable identifier

##### swift2.classes.EnsembleSimulation.record_ensemble_state

```python
record_ensemble_state(var_ids=CATCHMENT_FLOWRATE_VARID, recording_provider=None, data_ids=None)
```

Records one or more state values from an ensemble simulation

**Parameters:**

- **var_ids** (<code>[VecStr](#swift2.const.VecStr)</code>) – Model variable identierfier(s). Defaults to CATCHMENT_FLOWRATE_VARID.
- **recording_provider** (<code>[Optional](#typing.Optional)\[[TimeSeriesLibrary](#uchronia.classes.TimeSeriesLibrary)\]</code>) – An optional time series library to record to. Defaults to None.
- **data_ids** (<code>[Optional](#typing.Optional)\[[VecStr](#swift2.const.VecStr)\]</code>) – Data identifier(s). Defaults to None.

##### swift2.classes.EnsembleSimulation.setup

```python
setup(forecast_start, ensemble_size, forecast_horizon_length)
```

Sets up this ensemble simulation

**Parameters:**

- **forecast_start** (<code>[datetime](#datetime.datetime)</code>) – Start date for the simulation
- **ensemble_size** (<code>[int](#int)</code>) – size of the ensemble
- **forecast_horizon_length** (<code>[int](#int)</code>) – length of the simulation in numbers of time steps.

#### swift2.classes.ErrisStagedCalibration

```python
ErrisStagedCalibration(handle, release_native, type_id=None, prior_ref_count=0)
```

Bases: <code>[DeletableCffiNativeHandle](#refcount.interop.DeletableCffiNativeHandle)</code>

**Functions:**

- [**extract_optimisation_log**](#swift2.classes.ErrisStagedCalibration.extract_optimisation_log) –

##### swift2.classes.ErrisStagedCalibration.extract_optimisation_log

```python
extract_optimisation_log(fitness_name='log.likelihood')
```

#### swift2.classes.FilteringParameteriser

```python
FilteringParameteriser(handle, release_native, type_id=None, prior_ref_count=0)
```

Bases: <code>[HypercubeParameteriser](#swift2.classes.HypercubeParameteriser)</code>

**Functions:**

- [**add_parameter_to_hypercube**](#swift2.classes.FilteringParameteriser.add_parameter_to_hypercube) – Add a parameter to a hypercube. Must be a type of object that is expandable, otherwise may raise an exception
- [**add_to_hypercube**](#swift2.classes.FilteringParameteriser.add_to_hypercube) – Add entries to a hypercube. Must be a type of object that is expandable, otherwise may raise an exception.
- [**apply_sys_config**](#swift2.classes.FilteringParameteriser.apply_sys_config) – Apply a model configuration to a simulation
- [**as_dataframe**](#swift2.classes.FilteringParameteriser.as_dataframe) – Convert this hypercube parameteriser to a pandas data frame representation
- [**backtransform**](#swift2.classes.FilteringParameteriser.backtransform) – Get the parameteriser values in the untransformed space
- [**clone**](#swift2.classes.FilteringParameteriser.clone) –
- [**create_parameter_sampler**](#swift2.classes.FilteringParameteriser.create_parameter_sampler) – Creates a sampler for this parameteriser
- [**filtered_parameters**](#swift2.classes.FilteringParameteriser.filtered_parameters) – Wrap a parameteriser in a filter that can hide some parameters
- [**from_dataframe**](#swift2.classes.FilteringParameteriser.from_dataframe) – Create a parameteriser
- [**hide_parameters**](#swift2.classes.FilteringParameteriser.hide_parameters) – Hide some parameters (from the outside e.g. optimisers) in a filter parameteriser
- [**make_state_init_parameteriser**](#swift2.classes.FilteringParameteriser.make_state_init_parameteriser) – Create a parameteriser used for model state initialisation
- [**num_free_parameters**](#swift2.classes.FilteringParameteriser.num_free_parameters) – Number of free parameters in this hypercube parameteriser
- [**score_for_objective**](#swift2.classes.FilteringParameteriser.score_for_objective) – Computes the value of an objective for this given set of parameters
- [**set_hypercube**](#swift2.classes.FilteringParameteriser.set_hypercube) – Set the properties of a hypercube parameteriser
- [**set_max_parameter_value**](#swift2.classes.FilteringParameteriser.set_max_parameter_value) – Sets the value(s) of the upper bound of one or more parameter(s)
- [**set_min_parameter_value**](#swift2.classes.FilteringParameteriser.set_min_parameter_value) – Sets the value(s) of the lower bound of one or more parameter(s)
- [**set_parameter_definition**](#swift2.classes.FilteringParameteriser.set_parameter_definition) – Sets the feasible range and value for a parameter
- [**set_parameter_value**](#swift2.classes.FilteringParameteriser.set_parameter_value) – Sets the value(s) of one or more parameter(s)
- [**show_parameters**](#swift2.classes.FilteringParameteriser.show_parameters) – Show some parameters (from the outside e.g. optimisers) in a filter parameteriser
- [**subcatchment_parameteriser**](#swift2.classes.FilteringParameteriser.subcatchment_parameteriser) – Create a parameteriser that gets applied to a subset of a whole catchment
- [**supports_thread_safe_cloning**](#swift2.classes.FilteringParameteriser.supports_thread_safe_cloning) – Is this parameteriser clonable as a deep copy, safe for multi-threading?
- [**wrap_transform**](#swift2.classes.FilteringParameteriser.wrap_transform) – Create a parameteriser for which parameter transformations can be defined.

##### swift2.classes.FilteringParameteriser.add_parameter_to_hypercube

```python
add_parameter_to_hypercube(name, value, min, max)
```

Add a parameter to a hypercube. Must be a type of object that is expandable, otherwise may raise an exception

##### swift2.classes.FilteringParameteriser.add_to_hypercube

```python
add_to_hypercube(specs)
```

Add entries to a hypercube. Must be a type of object that is expandable, otherwise may raise an exception.

**Parameters:**

- **specs** (<code>[DataFrame](#pandas.DataFrame)</code>) – An optional data frame description of the parameter set, with at least columns Name, Min, Max, Value.

##### swift2.classes.FilteringParameteriser.apply_sys_config

```python
apply_sys_config(simulation)
```

Apply a model configuration to a simulation

**Parameters:**

- **simulation** (<code>[Simulation](#swift2.classes.Simulation)</code>) – simulation

##### swift2.classes.FilteringParameteriser.as_dataframe

```python
as_dataframe()
```

Convert this hypercube parameteriser to a pandas data frame representation

**Returns:**

- <code>[DataFrame](#pandas.DataFrame)</code> – pd.DataFrame: pandas data frame

##### swift2.classes.FilteringParameteriser.backtransform

```python
backtransform()
```

Get the parameteriser values in the untransformed space

Get the parameteriser values in the untransformed space, i.e. remove any
transform added via \[`HypercubeParameteriser.wrap_transform`\][HypercubeParameteriser.wrap_transform].
This allows to transform back e.g. from a virtual parameter log_X
to the underlying model (or even virtual/meta) parameter X.

**Returns:**

- **HypercubeParameteriser** (<code>[HypercubeParameteriser](#swift2.classes.HypercubeParameteriser)</code>) – The parameters definitions without the transforms (if there are any)

**Examples:**

```pycon
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

##### swift2.classes.FilteringParameteriser.clone

```python
clone()
```

##### swift2.classes.FilteringParameteriser.create_parameter_sampler

```python
create_parameter_sampler(seed=0, type='urs')
```

Creates a sampler for this parameteriser

**Parameters:**

- **seed** (<code>[int](#int)</code>) – a seed for the sampler. Defaults to 0.
- **type** (<code>[str](#str)</code>) – the type of sampler. Defaults to "urs". Only option supported as of 2023-01.

**Returns:**

- **CandidateFactorySeed** (<code>[CandidateFactorySeed](#swift2.classes.CandidateFactorySeed)</code>) – a sampler, aka candidate factory

##### swift2.classes.FilteringParameteriser.filtered_parameters

```python
filtered_parameters()
```

Wrap a parameteriser in a filter that can hide some parameters

##### swift2.classes.FilteringParameteriser.from_dataframe

```python
from_dataframe(type='Generic subareas', definition=None)
```

Create a parameteriser

**Parameters:**

- **type** (<code>[str](#str)</code>) – A string identifying the type of parameteriser to use. Recognised types are (case insensitive) 'log-likelihood', 'generic', 'subareas', 'links', 'nodes' and 'muskingum'. Defaults to "Generic subareas".
- **specs** (<code>[DataFrame](#pandas.DataFrame)</code>) – An optional data frame description of the parameter set, with at least columns Name, Min, Max, Value. Defaults to None.

**Returns:**

- **HypercubeParameteriser** (<code>[HypercubeParameteriser](#swift2.classes.HypercubeParameteriser)</code>) – new parameteriser

**Examples:**

```pycon
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

##### swift2.classes.FilteringParameteriser.hide_parameters

```python
hide_parameters(patterns, regex=False, starts_with=False, strict=False)
```

Hide some parameters (from the outside e.g. optimisers) in a filter parameteriser

**Parameters:**

- **patterns** (<code>\[[type](#type)\]</code>) – character, one or more pattern to match and hide matching parameters. Match according to other parameters.
- **regex** (<code>[bool](#bool)</code>) – logical, defaults False, should the patterns be used as regular expressions.. Defaults to False.
- **starts_with** (<code>[bool](#bool)</code>) – logical, defaults False. Ignored if regex is True. Should the patterns be used as starting strings in the parameter names.. Defaults to False.
- **strict** (<code>[bool](#bool)</code>) – logical, default False. Used only if regex and starts_with are False. If True, raises an error if one of the "patterns" has no exact match in the parameters.. Defaults to False.

##### swift2.classes.FilteringParameteriser.make_state_init_parameteriser

```python
make_state_init_parameteriser()
```

Create a parameteriser used for model state initialisation

This allows to define tied parameters where, for instance, pval = a * modelStateVal.
A more concrete use case is to define an initial soil moisture store 'S0',
as a fraction of the model store capacity 'Smax'.
The model state to initialise is 'S'

<details class="note" open>
<summary>Note</summary>
See also [swift2.classes.ScalingParameteriser][] for typical joint usage.
</details>

**Returns:**

- **StateInitParameteriser** (<code>[StateInitParameteriser](#swift2.classes.StateInitParameteriser)</code>) – state initialisation parameteriser

**Examples:**

```pycon
>>> todo()
```

##### swift2.classes.FilteringParameteriser.num_free_parameters

```python
num_free_parameters()
```

Number of free parameters in this hypercube parameteriser

**Returns:**

- **int** (<code>[int](#int)</code>) – Number of free parameters

##### swift2.classes.FilteringParameteriser.score_for_objective

```python
score_for_objective(objective)
```

Computes the value of an objective for this given set of parameters

##### swift2.classes.FilteringParameteriser.set_hypercube

```python
set_hypercube(specs)
```

Set the properties of a hypercube parameteriser

**Parameters:**

- **specs** (<code>[DataFrame](#pandas.DataFrame)</code>) – An optional data frame description of the parameter set, with at least columns Name, Min, Max, Value.

##### swift2.classes.FilteringParameteriser.set_max_parameter_value

```python
set_max_parameter_value(variable_name, value)
```

Sets the value(s) of the upper bound of one or more parameter(s)

**Parameters:**

- **variable_name** (<code>[VecStr](#swift2.const.VecStr)</code>) – one or more parameter name(s)
- **value** (<code>[VecScalars](#swift2.const.VecScalars)</code>) – one or more parameter value(s)

##### swift2.classes.FilteringParameteriser.set_min_parameter_value

```python
set_min_parameter_value(variable_name, value)
```

Sets the value(s) of the lower bound of one or more parameter(s)

**Parameters:**

- **variable_name** (<code>[VecStr](#swift2.const.VecStr)</code>) – one or more parameter name(s)
- **value** (<code>[VecScalars](#swift2.const.VecScalars)</code>) – one or more parameter value(s)

##### swift2.classes.FilteringParameteriser.set_parameter_definition

```python
set_parameter_definition(variable_name, min, max, value)
```

Sets the feasible range and value for a parameter

**Parameters:**

- **variable_name** (<code>[str](#str)</code>) – parameter name
- **min** (<code>[float](#float)</code>) – min
- **max** (<code>[float](#float)</code>) – max
- **value** (<code>[float](#float)</code>) – value

##### swift2.classes.FilteringParameteriser.set_parameter_value

```python
set_parameter_value(variable_name, value)
```

Sets the value(s) of one or more parameter(s)

**Parameters:**

- **variable_name** (<code>[VecStr](#swift2.const.VecStr)</code>) – one or more parameter name(s)
- **value** (<code>[VecScalars](#swift2.const.VecScalars)</code>) – one or more parameter value(s)

##### swift2.classes.FilteringParameteriser.show_parameters

```python
show_parameters(patterns, regex=False, starts_with=False)
```

Show some parameters (from the outside e.g. optimisers) in a filter parameteriser

**Parameters:**

- **patterns** (<code>\[[type](#type)\]</code>) – character, one or more pattern to match and show matching parameters. Match according to other parameters
- **regex** (<code>[bool](#bool)</code>) – should the patterns be used as regular expressions. Defaults to False.
- **starts_with** (<code>[bool](#bool)</code>) – should the patterns be used as starting strings in the parameter names. Defaults to False.

##### swift2.classes.FilteringParameteriser.subcatchment_parameteriser

```python
subcatchment_parameteriser(subcatchment)
```

Create a parameteriser that gets applied to a subset of a whole catchment

**Parameters:**

- **subcatchment** (<code>[Simulation](#swift2.classes.Simulation)</code>) – the subcatchment, subset of a whole catchment, identifying which elements (subareas, nodes, links) will be parameterised by the new parameteriser. Other catchment elements are untouched.

**Returns:**

- **HypercubeParameteriser** – New parameteriser whose application is limited to the subcatchment.

**Examples:**

```pycon
>>> sub_cats = simulation.split_to_subcatchments(["node.node_7", "node.node_10"])
>>> sc = sub_cats["node.node_7"]
>>> p = sp.create_parameteriser('generic subarea')
>>> p.add_parameter_to_hypercube("x1", 32, 1, 6e3)
>>> sp = p.subcatchment_parameteriser(sc)
>>> sp.apply_sys_config(simulation)
```

##### swift2.classes.FilteringParameteriser.supports_thread_safe_cloning

```python
supports_thread_safe_cloning()
```

Is this parameteriser clonable as a deep copy, safe for multi-threading?

##### swift2.classes.FilteringParameteriser.wrap_transform

```python
wrap_transform()
```

Create a parameteriser for which parameter transformations can be defined.

This allows to define e.g. a virtual parameter log_X instead of calibrating on the parameter X.

**Returns:**

- **TransformParameteriser** (<code>[TransformParameteriser](#swift2.classes.TransformParameteriser)</code>) – A new parameteriser (TransformParameteriser) which has methods to define parameter transforms

#### swift2.classes.FunctionsParameteriser

```python
FunctionsParameteriser(handle, release_native, type_id=None, prior_ref_count=0)
```

Bases: <code>[HypercubeParameteriser](#swift2.classes.HypercubeParameteriser)</code>

**Functions:**

- [**add_parameter_to_hypercube**](#swift2.classes.FunctionsParameteriser.add_parameter_to_hypercube) – Add a parameter to a hypercube. Must be a type of object that is expandable, otherwise may raise an exception
- [**add_to_hypercube**](#swift2.classes.FunctionsParameteriser.add_to_hypercube) – Add entries to a hypercube. Must be a type of object that is expandable, otherwise may raise an exception.
- [**apply_sys_config**](#swift2.classes.FunctionsParameteriser.apply_sys_config) – Apply a model configuration to a simulation
- [**as_dataframe**](#swift2.classes.FunctionsParameteriser.as_dataframe) – Convert this hypercube parameteriser to a pandas data frame representation
- [**backtransform**](#swift2.classes.FunctionsParameteriser.backtransform) – Get the parameteriser values in the untransformed space
- [**clone**](#swift2.classes.FunctionsParameteriser.clone) –
- [**create_parameter_sampler**](#swift2.classes.FunctionsParameteriser.create_parameter_sampler) – Creates a sampler for this parameteriser
- [**filtered_parameters**](#swift2.classes.FunctionsParameteriser.filtered_parameters) – Wrap a parameteriser in a filter that can hide some parameters
- [**from_dataframe**](#swift2.classes.FunctionsParameteriser.from_dataframe) – Create a parameteriser
- [**hide_parameters**](#swift2.classes.FunctionsParameteriser.hide_parameters) – Hide some parameters (from the outside e.g. optimisers) in a filter parameteriser
- [**make_state_init_parameteriser**](#swift2.classes.FunctionsParameteriser.make_state_init_parameteriser) – Create a parameteriser used for model state initialisation
- [**num_free_parameters**](#swift2.classes.FunctionsParameteriser.num_free_parameters) – Number of free parameters in this hypercube parameteriser
- [**score_for_objective**](#swift2.classes.FunctionsParameteriser.score_for_objective) – Computes the value of an objective for this given set of parameters
- [**set_hypercube**](#swift2.classes.FunctionsParameteriser.set_hypercube) – Set the properties of a hypercube parameteriser
- [**set_max_parameter_value**](#swift2.classes.FunctionsParameteriser.set_max_parameter_value) – Sets the value(s) of the upper bound of one or more parameter(s)
- [**set_min_parameter_value**](#swift2.classes.FunctionsParameteriser.set_min_parameter_value) – Sets the value(s) of the lower bound of one or more parameter(s)
- [**set_parameter_definition**](#swift2.classes.FunctionsParameteriser.set_parameter_definition) – Sets the feasible range and value for a parameter
- [**set_parameter_value**](#swift2.classes.FunctionsParameteriser.set_parameter_value) – Sets the value(s) of one or more parameter(s)
- [**show_parameters**](#swift2.classes.FunctionsParameteriser.show_parameters) – Show some parameters (from the outside e.g. optimisers) in a filter parameteriser
- [**subcatchment_parameteriser**](#swift2.classes.FunctionsParameteriser.subcatchment_parameteriser) – Create a parameteriser that gets applied to a subset of a whole catchment
- [**supports_thread_safe_cloning**](#swift2.classes.FunctionsParameteriser.supports_thread_safe_cloning) – Is this parameteriser clonable as a deep copy, safe for multi-threading?
- [**wrap_transform**](#swift2.classes.FunctionsParameteriser.wrap_transform) – Create a parameteriser for which parameter transformations can be defined.

##### swift2.classes.FunctionsParameteriser.add_parameter_to_hypercube

```python
add_parameter_to_hypercube(name, value, min, max)
```

Add a parameter to a hypercube. Must be a type of object that is expandable, otherwise may raise an exception

##### swift2.classes.FunctionsParameteriser.add_to_hypercube

```python
add_to_hypercube(specs)
```

Add entries to a hypercube. Must be a type of object that is expandable, otherwise may raise an exception.

**Parameters:**

- **specs** (<code>[DataFrame](#pandas.DataFrame)</code>) – An optional data frame description of the parameter set, with at least columns Name, Min, Max, Value.

##### swift2.classes.FunctionsParameteriser.apply_sys_config

```python
apply_sys_config(simulation)
```

Apply a model configuration to a simulation

**Parameters:**

- **simulation** (<code>[Simulation](#swift2.classes.Simulation)</code>) – simulation

##### swift2.classes.FunctionsParameteriser.as_dataframe

```python
as_dataframe()
```

Convert this hypercube parameteriser to a pandas data frame representation

**Returns:**

- <code>[DataFrame](#pandas.DataFrame)</code> – pd.DataFrame: pandas data frame

##### swift2.classes.FunctionsParameteriser.backtransform

```python
backtransform()
```

Get the parameteriser values in the untransformed space

Get the parameteriser values in the untransformed space, i.e. remove any
transform added via \[`HypercubeParameteriser.wrap_transform`\][HypercubeParameteriser.wrap_transform].
This allows to transform back e.g. from a virtual parameter log_X
to the underlying model (or even virtual/meta) parameter X.

**Returns:**

- **HypercubeParameteriser** (<code>[HypercubeParameteriser](#swift2.classes.HypercubeParameteriser)</code>) – The parameters definitions without the transforms (if there are any)

**Examples:**

```pycon
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

##### swift2.classes.FunctionsParameteriser.clone

```python
clone()
```

##### swift2.classes.FunctionsParameteriser.create_parameter_sampler

```python
create_parameter_sampler(seed=0, type='urs')
```

Creates a sampler for this parameteriser

**Parameters:**

- **seed** (<code>[int](#int)</code>) – a seed for the sampler. Defaults to 0.
- **type** (<code>[str](#str)</code>) – the type of sampler. Defaults to "urs". Only option supported as of 2023-01.

**Returns:**

- **CandidateFactorySeed** (<code>[CandidateFactorySeed](#swift2.classes.CandidateFactorySeed)</code>) – a sampler, aka candidate factory

##### swift2.classes.FunctionsParameteriser.filtered_parameters

```python
filtered_parameters()
```

Wrap a parameteriser in a filter that can hide some parameters

##### swift2.classes.FunctionsParameteriser.from_dataframe

```python
from_dataframe(type='Generic subareas', definition=None)
```

Create a parameteriser

**Parameters:**

- **type** (<code>[str](#str)</code>) – A string identifying the type of parameteriser to use. Recognised types are (case insensitive) 'log-likelihood', 'generic', 'subareas', 'links', 'nodes' and 'muskingum'. Defaults to "Generic subareas".
- **specs** (<code>[DataFrame](#pandas.DataFrame)</code>) – An optional data frame description of the parameter set, with at least columns Name, Min, Max, Value. Defaults to None.

**Returns:**

- **HypercubeParameteriser** (<code>[HypercubeParameteriser](#swift2.classes.HypercubeParameteriser)</code>) – new parameteriser

**Examples:**

```pycon
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

##### swift2.classes.FunctionsParameteriser.hide_parameters

```python
hide_parameters(patterns, regex=False, starts_with=False, strict=False)
```

Hide some parameters (from the outside e.g. optimisers) in a filter parameteriser

**Parameters:**

- **patterns** (<code>\[[type](#type)\]</code>) – character, one or more pattern to match and hide matching parameters. Match according to other parameters.
- **regex** (<code>[bool](#bool)</code>) – logical, defaults False, should the patterns be used as regular expressions.. Defaults to False.
- **starts_with** (<code>[bool](#bool)</code>) – logical, defaults False. Ignored if regex is True. Should the patterns be used as starting strings in the parameter names.. Defaults to False.
- **strict** (<code>[bool](#bool)</code>) – logical, default False. Used only if regex and starts_with are False. If True, raises an error if one of the "patterns" has no exact match in the parameters.. Defaults to False.

##### swift2.classes.FunctionsParameteriser.make_state_init_parameteriser

```python
make_state_init_parameteriser()
```

Create a parameteriser used for model state initialisation

This allows to define tied parameters where, for instance, pval = a * modelStateVal.
A more concrete use case is to define an initial soil moisture store 'S0',
as a fraction of the model store capacity 'Smax'.
The model state to initialise is 'S'

<details class="note" open>
<summary>Note</summary>
See also [swift2.classes.ScalingParameteriser][] for typical joint usage.
</details>

**Returns:**

- **StateInitParameteriser** (<code>[StateInitParameteriser](#swift2.classes.StateInitParameteriser)</code>) – state initialisation parameteriser

**Examples:**

```pycon
>>> todo()
```

##### swift2.classes.FunctionsParameteriser.num_free_parameters

```python
num_free_parameters()
```

Number of free parameters in this hypercube parameteriser

**Returns:**

- **int** (<code>[int](#int)</code>) – Number of free parameters

##### swift2.classes.FunctionsParameteriser.score_for_objective

```python
score_for_objective(objective)
```

Computes the value of an objective for this given set of parameters

##### swift2.classes.FunctionsParameteriser.set_hypercube

```python
set_hypercube(specs)
```

Set the properties of a hypercube parameteriser

**Parameters:**

- **specs** (<code>[DataFrame](#pandas.DataFrame)</code>) – An optional data frame description of the parameter set, with at least columns Name, Min, Max, Value.

##### swift2.classes.FunctionsParameteriser.set_max_parameter_value

```python
set_max_parameter_value(variable_name, value)
```

Sets the value(s) of the upper bound of one or more parameter(s)

**Parameters:**

- **variable_name** (<code>[VecStr](#swift2.const.VecStr)</code>) – one or more parameter name(s)
- **value** (<code>[VecScalars](#swift2.const.VecScalars)</code>) – one or more parameter value(s)

##### swift2.classes.FunctionsParameteriser.set_min_parameter_value

```python
set_min_parameter_value(variable_name, value)
```

Sets the value(s) of the lower bound of one or more parameter(s)

**Parameters:**

- **variable_name** (<code>[VecStr](#swift2.const.VecStr)</code>) – one or more parameter name(s)
- **value** (<code>[VecScalars](#swift2.const.VecScalars)</code>) – one or more parameter value(s)

##### swift2.classes.FunctionsParameteriser.set_parameter_definition

```python
set_parameter_definition(variable_name, min, max, value)
```

Sets the feasible range and value for a parameter

**Parameters:**

- **variable_name** (<code>[str](#str)</code>) – parameter name
- **min** (<code>[float](#float)</code>) – min
- **max** (<code>[float](#float)</code>) – max
- **value** (<code>[float](#float)</code>) – value

##### swift2.classes.FunctionsParameteriser.set_parameter_value

```python
set_parameter_value(variable_name, value)
```

Sets the value(s) of one or more parameter(s)

**Parameters:**

- **variable_name** (<code>[VecStr](#swift2.const.VecStr)</code>) – one or more parameter name(s)
- **value** (<code>[VecScalars](#swift2.const.VecScalars)</code>) – one or more parameter value(s)

##### swift2.classes.FunctionsParameteriser.show_parameters

```python
show_parameters(patterns, regex=False, starts_with=False)
```

Show some parameters (from the outside e.g. optimisers) in a filter parameteriser

**Parameters:**

- **patterns** (<code>\[[type](#type)\]</code>) – character, one or more pattern to match and show matching parameters. Match according to other parameters
- **regex** (<code>[bool](#bool)</code>) – should the patterns be used as regular expressions. Defaults to False.
- **starts_with** (<code>[bool](#bool)</code>) – should the patterns be used as starting strings in the parameter names. Defaults to False.

##### swift2.classes.FunctionsParameteriser.subcatchment_parameteriser

```python
subcatchment_parameteriser(subcatchment)
```

Create a parameteriser that gets applied to a subset of a whole catchment

**Parameters:**

- **subcatchment** (<code>[Simulation](#swift2.classes.Simulation)</code>) – the subcatchment, subset of a whole catchment, identifying which elements (subareas, nodes, links) will be parameterised by the new parameteriser. Other catchment elements are untouched.

**Returns:**

- **HypercubeParameteriser** – New parameteriser whose application is limited to the subcatchment.

**Examples:**

```pycon
>>> sub_cats = simulation.split_to_subcatchments(["node.node_7", "node.node_10"])
>>> sc = sub_cats["node.node_7"]
>>> p = sp.create_parameteriser('generic subarea')
>>> p.add_parameter_to_hypercube("x1", 32, 1, 6e3)
>>> sp = p.subcatchment_parameteriser(sc)
>>> sp.apply_sys_config(simulation)
```

##### swift2.classes.FunctionsParameteriser.supports_thread_safe_cloning

```python
supports_thread_safe_cloning()
```

Is this parameteriser clonable as a deep copy, safe for multi-threading?

##### swift2.classes.FunctionsParameteriser.wrap_transform

```python
wrap_transform()
```

Create a parameteriser for which parameter transformations can be defined.

This allows to define e.g. a virtual parameter log_X instead of calibrating on the parameter X.

**Returns:**

- **TransformParameteriser** (<code>[TransformParameteriser](#swift2.classes.TransformParameteriser)</code>) – A new parameteriser (TransformParameteriser) which has methods to define parameter transforms

#### swift2.classes.HypercubeParameteriser

```python
HypercubeParameteriser(handle, release_native, type_id=None, prior_ref_count=0)
```

Bases: <code>[Parameteriser](#swift2.classes.Parameteriser)</code>

**Functions:**

- [**add_parameter_to_hypercube**](#swift2.classes.HypercubeParameteriser.add_parameter_to_hypercube) – Add a parameter to a hypercube. Must be a type of object that is expandable, otherwise may raise an exception
- [**add_to_hypercube**](#swift2.classes.HypercubeParameteriser.add_to_hypercube) – Add entries to a hypercube. Must be a type of object that is expandable, otherwise may raise an exception.
- [**apply_sys_config**](#swift2.classes.HypercubeParameteriser.apply_sys_config) – Apply a model configuration to a simulation
- [**as_dataframe**](#swift2.classes.HypercubeParameteriser.as_dataframe) – Convert this hypercube parameteriser to a pandas data frame representation
- [**backtransform**](#swift2.classes.HypercubeParameteriser.backtransform) – Get the parameteriser values in the untransformed space
- [**clone**](#swift2.classes.HypercubeParameteriser.clone) –
- [**create_parameter_sampler**](#swift2.classes.HypercubeParameteriser.create_parameter_sampler) – Creates a sampler for this parameteriser
- [**filtered_parameters**](#swift2.classes.HypercubeParameteriser.filtered_parameters) – Wrap a parameteriser in a filter that can hide some parameters
- [**from_dataframe**](#swift2.classes.HypercubeParameteriser.from_dataframe) – Create a parameteriser
- [**hide_parameters**](#swift2.classes.HypercubeParameteriser.hide_parameters) – Hide some parameters (from the outside e.g. optimisers) in a filter parameteriser
- [**make_state_init_parameteriser**](#swift2.classes.HypercubeParameteriser.make_state_init_parameteriser) – Create a parameteriser used for model state initialisation
- [**num_free_parameters**](#swift2.classes.HypercubeParameteriser.num_free_parameters) – Number of free parameters in this hypercube parameteriser
- [**score_for_objective**](#swift2.classes.HypercubeParameteriser.score_for_objective) – Computes the value of an objective for this given set of parameters
- [**set_hypercube**](#swift2.classes.HypercubeParameteriser.set_hypercube) – Set the properties of a hypercube parameteriser
- [**set_max_parameter_value**](#swift2.classes.HypercubeParameteriser.set_max_parameter_value) – Sets the value(s) of the upper bound of one or more parameter(s)
- [**set_min_parameter_value**](#swift2.classes.HypercubeParameteriser.set_min_parameter_value) – Sets the value(s) of the lower bound of one or more parameter(s)
- [**set_parameter_definition**](#swift2.classes.HypercubeParameteriser.set_parameter_definition) – Sets the feasible range and value for a parameter
- [**set_parameter_value**](#swift2.classes.HypercubeParameteriser.set_parameter_value) – Sets the value(s) of one or more parameter(s)
- [**show_parameters**](#swift2.classes.HypercubeParameteriser.show_parameters) – Show some parameters (from the outside e.g. optimisers) in a filter parameteriser
- [**subcatchment_parameteriser**](#swift2.classes.HypercubeParameteriser.subcatchment_parameteriser) – Create a parameteriser that gets applied to a subset of a whole catchment
- [**supports_thread_safe_cloning**](#swift2.classes.HypercubeParameteriser.supports_thread_safe_cloning) – Is this parameteriser clonable as a deep copy, safe for multi-threading?
- [**wrap_transform**](#swift2.classes.HypercubeParameteriser.wrap_transform) – Create a parameteriser for which parameter transformations can be defined.

##### swift2.classes.HypercubeParameteriser.add_parameter_to_hypercube

```python
add_parameter_to_hypercube(name, value, min, max)
```

Add a parameter to a hypercube. Must be a type of object that is expandable, otherwise may raise an exception

##### swift2.classes.HypercubeParameteriser.add_to_hypercube

```python
add_to_hypercube(specs)
```

Add entries to a hypercube. Must be a type of object that is expandable, otherwise may raise an exception.

**Parameters:**

- **specs** (<code>[DataFrame](#pandas.DataFrame)</code>) – An optional data frame description of the parameter set, with at least columns Name, Min, Max, Value.

##### swift2.classes.HypercubeParameteriser.apply_sys_config

```python
apply_sys_config(simulation)
```

Apply a model configuration to a simulation

**Parameters:**

- **simulation** (<code>[Simulation](#swift2.classes.Simulation)</code>) – simulation

##### swift2.classes.HypercubeParameteriser.as_dataframe

```python
as_dataframe()
```

Convert this hypercube parameteriser to a pandas data frame representation

**Returns:**

- <code>[DataFrame](#pandas.DataFrame)</code> – pd.DataFrame: pandas data frame

##### swift2.classes.HypercubeParameteriser.backtransform

```python
backtransform()
```

Get the parameteriser values in the untransformed space

Get the parameteriser values in the untransformed space, i.e. remove any
transform added via \[`HypercubeParameteriser.wrap_transform`\][HypercubeParameteriser.wrap_transform].
This allows to transform back e.g. from a virtual parameter log_X
to the underlying model (or even virtual/meta) parameter X.

**Returns:**

- **HypercubeParameteriser** (<code>[HypercubeParameteriser](#swift2.classes.HypercubeParameteriser)</code>) – The parameters definitions without the transforms (if there are any)

**Examples:**

```pycon
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

##### swift2.classes.HypercubeParameteriser.clone

```python
clone()
```

##### swift2.classes.HypercubeParameteriser.create_parameter_sampler

```python
create_parameter_sampler(seed=0, type='urs')
```

Creates a sampler for this parameteriser

**Parameters:**

- **seed** (<code>[int](#int)</code>) – a seed for the sampler. Defaults to 0.
- **type** (<code>[str](#str)</code>) – the type of sampler. Defaults to "urs". Only option supported as of 2023-01.

**Returns:**

- **CandidateFactorySeed** (<code>[CandidateFactorySeed](#swift2.classes.CandidateFactorySeed)</code>) – a sampler, aka candidate factory

##### swift2.classes.HypercubeParameteriser.filtered_parameters

```python
filtered_parameters()
```

Wrap a parameteriser in a filter that can hide some parameters

##### swift2.classes.HypercubeParameteriser.from_dataframe

```python
from_dataframe(type='Generic subareas', definition=None)
```

Create a parameteriser

**Parameters:**

- **type** (<code>[str](#str)</code>) – A string identifying the type of parameteriser to use. Recognised types are (case insensitive) 'log-likelihood', 'generic', 'subareas', 'links', 'nodes' and 'muskingum'. Defaults to "Generic subareas".
- **specs** (<code>[DataFrame](#pandas.DataFrame)</code>) – An optional data frame description of the parameter set, with at least columns Name, Min, Max, Value. Defaults to None.

**Returns:**

- **HypercubeParameteriser** (<code>[HypercubeParameteriser](#swift2.classes.HypercubeParameteriser)</code>) – new parameteriser

**Examples:**

```pycon
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

##### swift2.classes.HypercubeParameteriser.hide_parameters

```python
hide_parameters(patterns, regex=False, starts_with=False, strict=False)
```

Hide some parameters (from the outside e.g. optimisers) in a filter parameteriser

**Parameters:**

- **patterns** (<code>\[[type](#type)\]</code>) – character, one or more pattern to match and hide matching parameters. Match according to other parameters.
- **regex** (<code>[bool](#bool)</code>) – logical, defaults False, should the patterns be used as regular expressions.. Defaults to False.
- **starts_with** (<code>[bool](#bool)</code>) – logical, defaults False. Ignored if regex is True. Should the patterns be used as starting strings in the parameter names.. Defaults to False.
- **strict** (<code>[bool](#bool)</code>) – logical, default False. Used only if regex and starts_with are False. If True, raises an error if one of the "patterns" has no exact match in the parameters.. Defaults to False.

##### swift2.classes.HypercubeParameteriser.make_state_init_parameteriser

```python
make_state_init_parameteriser()
```

Create a parameteriser used for model state initialisation

This allows to define tied parameters where, for instance, pval = a * modelStateVal.
A more concrete use case is to define an initial soil moisture store 'S0',
as a fraction of the model store capacity 'Smax'.
The model state to initialise is 'S'

<details class="note" open>
<summary>Note</summary>
See also [swift2.classes.ScalingParameteriser][] for typical joint usage.
</details>

**Returns:**

- **StateInitParameteriser** (<code>[StateInitParameteriser](#swift2.classes.StateInitParameteriser)</code>) – state initialisation parameteriser

**Examples:**

```pycon
>>> todo()
```

##### swift2.classes.HypercubeParameteriser.num_free_parameters

```python
num_free_parameters()
```

Number of free parameters in this hypercube parameteriser

**Returns:**

- **int** (<code>[int](#int)</code>) – Number of free parameters

##### swift2.classes.HypercubeParameteriser.score_for_objective

```python
score_for_objective(objective)
```

Computes the value of an objective for this given set of parameters

##### swift2.classes.HypercubeParameteriser.set_hypercube

```python
set_hypercube(specs)
```

Set the properties of a hypercube parameteriser

**Parameters:**

- **specs** (<code>[DataFrame](#pandas.DataFrame)</code>) – An optional data frame description of the parameter set, with at least columns Name, Min, Max, Value.

##### swift2.classes.HypercubeParameteriser.set_max_parameter_value

```python
set_max_parameter_value(variable_name, value)
```

Sets the value(s) of the upper bound of one or more parameter(s)

**Parameters:**

- **variable_name** (<code>[VecStr](#swift2.const.VecStr)</code>) – one or more parameter name(s)
- **value** (<code>[VecScalars](#swift2.const.VecScalars)</code>) – one or more parameter value(s)

##### swift2.classes.HypercubeParameteriser.set_min_parameter_value

```python
set_min_parameter_value(variable_name, value)
```

Sets the value(s) of the lower bound of one or more parameter(s)

**Parameters:**

- **variable_name** (<code>[VecStr](#swift2.const.VecStr)</code>) – one or more parameter name(s)
- **value** (<code>[VecScalars](#swift2.const.VecScalars)</code>) – one or more parameter value(s)

##### swift2.classes.HypercubeParameteriser.set_parameter_definition

```python
set_parameter_definition(variable_name, min, max, value)
```

Sets the feasible range and value for a parameter

**Parameters:**

- **variable_name** (<code>[str](#str)</code>) – parameter name
- **min** (<code>[float](#float)</code>) – min
- **max** (<code>[float](#float)</code>) – max
- **value** (<code>[float](#float)</code>) – value

##### swift2.classes.HypercubeParameteriser.set_parameter_value

```python
set_parameter_value(variable_name, value)
```

Sets the value(s) of one or more parameter(s)

**Parameters:**

- **variable_name** (<code>[VecStr](#swift2.const.VecStr)</code>) – one or more parameter name(s)
- **value** (<code>[VecScalars](#swift2.const.VecScalars)</code>) – one or more parameter value(s)

##### swift2.classes.HypercubeParameteriser.show_parameters

```python
show_parameters(patterns, regex=False, starts_with=False)
```

Show some parameters (from the outside e.g. optimisers) in a filter parameteriser

**Parameters:**

- **patterns** (<code>\[[type](#type)\]</code>) – character, one or more pattern to match and show matching parameters. Match according to other parameters
- **regex** (<code>[bool](#bool)</code>) – should the patterns be used as regular expressions. Defaults to False.
- **starts_with** (<code>[bool](#bool)</code>) – should the patterns be used as starting strings in the parameter names. Defaults to False.

##### swift2.classes.HypercubeParameteriser.subcatchment_parameteriser

```python
subcatchment_parameteriser(subcatchment)
```

Create a parameteriser that gets applied to a subset of a whole catchment

**Parameters:**

- **subcatchment** (<code>[Simulation](#swift2.classes.Simulation)</code>) – the subcatchment, subset of a whole catchment, identifying which elements (subareas, nodes, links) will be parameterised by the new parameteriser. Other catchment elements are untouched.

**Returns:**

- **HypercubeParameteriser** – New parameteriser whose application is limited to the subcatchment.

**Examples:**

```pycon
>>> sub_cats = simulation.split_to_subcatchments(["node.node_7", "node.node_10"])
>>> sc = sub_cats["node.node_7"]
>>> p = sp.create_parameteriser('generic subarea')
>>> p.add_parameter_to_hypercube("x1", 32, 1, 6e3)
>>> sp = p.subcatchment_parameteriser(sc)
>>> sp.apply_sys_config(simulation)
```

##### swift2.classes.HypercubeParameteriser.supports_thread_safe_cloning

```python
supports_thread_safe_cloning()
```

Is this parameteriser clonable as a deep copy, safe for multi-threading?

##### swift2.classes.HypercubeParameteriser.wrap_transform

```python
wrap_transform()
```

Create a parameteriser for which parameter transformations can be defined.

This allows to define e.g. a virtual parameter log_X instead of calibrating on the parameter X.

**Returns:**

- **TransformParameteriser** (<code>[TransformParameteriser](#swift2.classes.TransformParameteriser)</code>) – A new parameteriser (TransformParameteriser) which has methods to define parameter transforms

#### swift2.classes.MaerrisStagedCalibration

```python
MaerrisStagedCalibration(handle, release_native, type_id=None, prior_ref_count=0)
```

Bases: <code>[DeletableCffiNativeHandle](#refcount.interop.DeletableCffiNativeHandle)</code>

**Functions:**

- [**extract_optimisation_log**](#swift2.classes.MaerrisStagedCalibration.extract_optimisation_log) –

##### swift2.classes.MaerrisStagedCalibration.extract_optimisation_log

```python
extract_optimisation_log(fitness_name='log.likelihood')
```

#### swift2.classes.MemoryStates

```python
MemoryStates(handle, release_native, type_id=None, prior_ref_count=0)
```

Bases: <code>[DeletableCffiNativeHandle](#refcount.interop.DeletableCffiNativeHandle)</code>

#### swift2.classes.ObjectiveEvaluator

```python
ObjectiveEvaluator(handle, release_native, type_id=None, prior_ref_count=0)
```

Bases: <code>[DeletableCffiNativeHandle](#refcount.interop.DeletableCffiNativeHandle)</code>

Objective Evaluator

**Functions:**

- [**create_composite_objective**](#swift2.classes.ObjectiveEvaluator.create_composite_objective) – Creates a composite objective, weighted average of several objectives
- [**create_sce_optim_swift**](#swift2.classes.ObjectiveEvaluator.create_sce_optim_swift) – Creates a shuffled complex optimiser for this objective
- [**get_score**](#swift2.classes.ObjectiveEvaluator.get_score) – Evaluate this objective for a given parameterisation
- [**get_scores**](#swift2.classes.ObjectiveEvaluator.get_scores) – Evaluate this objective for a given parameterisation

##### swift2.classes.ObjectiveEvaluator.create_composite_objective

```python
create_composite_objective(objectives, weights, names)
```

Creates a composite objective, weighted average of several objectives

**Parameters:**

- **objectives** (<code>Sequence["ObjectiveEvaluator"]</code>) – objective evaluators, for instance measures at several points in the catchment
- **weights** (<code>[Sequence](#typing.Sequence)\[[float](#float)\]</code>) – Weights to use to average the objectives. This may not add to one, but must not sum to zero
- **names** (<code>[Sequence](#typing.Sequence)\[[str](#str)\]</code>) – Names of individual objectives

**Returns:**

- **ObjectiveEvaluator** (<code>[ObjectiveEvaluator](#swift2.classes.ObjectiveEvaluator)</code>) – An objective evaluator that can be use by an optimiser

##### swift2.classes.ObjectiveEvaluator.create_sce_optim_swift

```python
create_sce_optim_swift(termination_criterion=None, sce_params=None, population_initialiser=None)
```

Creates a shuffled complex optimiser for this objective

**Parameters:**

- **termination_criterion** (<code>Optional["SceTerminationCondition"]</code>) – A termination criterion for the optimiser. Defaults to None, in which case an arbitrary "relative standard deviation" is set up.
- **sce_params** (<code>[Optional](#typing.Optional)\[[Dict](#typing.Dict)\[[str](#str), [float](#float)\]\]</code>) – hyperparameters controlling SCE. Defaults to None, in which case \[`swift2.parameteriser.get_default_sce_parameters`\][swift2.parameteriser.get_default_sce_parameters] is used.
- **population_initialiser** (<code>Optional["CandidateFactorySeed"]</code>) – A candidate factory to initialise the population of parameters the optimiser starts from, or a hypercube. In the latter case, uniform random sampling is used. Defaults to None, which leads to an error (for legacy reasons).

**Returns:**

- **Optimiser** (<code>[Optimiser](#swift2.classes.Optimiser)</code>) – SCE optimiser

##### swift2.classes.ObjectiveEvaluator.get_score

```python
get_score(p_set)
```

Evaluate this objective for a given parameterisation

**Parameters:**

- **p_set** (<code>[HypercubeParameteriser](#swift2.classes.HypercubeParameteriser)</code>) – parameteriser

**Returns:**

- <code>[Dict](#typing.Dict)\[[str](#str), [Any](#typing.Any)\]</code> – Dict\[str,Any\]: score(s), and a data frame representation of the input parameters.

##### swift2.classes.ObjectiveEvaluator.get_scores

```python
get_scores(p_set)
```

Evaluate this objective for a given parameterisation

**Parameters:**

- **p_set** (<code>[HypercubeParameteriser](#swift2.classes.HypercubeParameteriser)</code>) – parameteriser

**Returns:**

- <code>[Dict](#typing.Dict)\[[str](#str), [float](#float)\]</code> – Dict\[str,float\]: score(s)

#### swift2.classes.ObjectiveScores

```python
ObjectiveScores(handle, release_native, type_id=None, prior_ref_count=0)
```

Bases: <code>[DeletableCffiNativeHandle](#refcount.interop.DeletableCffiNativeHandle)</code>

**Functions:**

- [**apply_sys_config**](#swift2.classes.ObjectiveScores.apply_sys_config) –
- [**as_py_structure**](#swift2.classes.ObjectiveScores.as_py_structure) –

**Attributes:**

- [**num_scores**](#swift2.classes.ObjectiveScores.num_scores) (<code>[int](#int)</code>) –
- [**parameteriser**](#swift2.classes.ObjectiveScores.parameteriser) (<code>[HypercubeParameteriser](#swift2.classes.HypercubeParameteriser)</code>) –
- [**scores**](#swift2.classes.ObjectiveScores.scores) (<code>[Dict](#typing.Dict)\[[str](#str), [float](#float)\]</code>) –

##### swift2.classes.ObjectiveScores.apply_sys_config

```python
apply_sys_config(simulation)
```

##### swift2.classes.ObjectiveScores.as_py_structure

```python
as_py_structure()
```

##### swift2.classes.ObjectiveScores.num_scores

```python
num_scores: int
```

##### swift2.classes.ObjectiveScores.parameteriser

```python
parameteriser: HypercubeParameteriser
```

##### swift2.classes.ObjectiveScores.scores

```python
scores: Dict[str, float]
```

#### swift2.classes.Optimiser

```python
Optimiser(handle, release_native, type_id=None, prior_ref_count=0)
```

Bases: <code>[DeletableCffiNativeHandle](#refcount.interop.DeletableCffiNativeHandle)</code>

**Functions:**

- [**execute_optimisation**](#swift2.classes.Optimiser.execute_optimisation) –
- [**extract_optimisation_log**](#swift2.classes.Optimiser.extract_optimisation_log) –
- [**get_default_maximum_threads**](#swift2.classes.Optimiser.get_default_maximum_threads) –
- [**set_calibration_logger**](#swift2.classes.Optimiser.set_calibration_logger) –
- [**set_default_maximum_threads**](#swift2.classes.Optimiser.set_default_maximum_threads) –
- [**set_maximum_threads**](#swift2.classes.Optimiser.set_maximum_threads) –

##### swift2.classes.Optimiser.execute_optimisation

```python
execute_optimisation()
```

##### swift2.classes.Optimiser.extract_optimisation_log

```python
extract_optimisation_log(fitness_name='log.likelihood')
```

##### swift2.classes.Optimiser.get_default_maximum_threads

```python
get_default_maximum_threads()
```

##### swift2.classes.Optimiser.set_calibration_logger

```python
set_calibration_logger(type='')
```

##### swift2.classes.Optimiser.set_default_maximum_threads

```python
set_default_maximum_threads(n_threads)
```

##### swift2.classes.Optimiser.set_maximum_threads

```python
set_maximum_threads(n_threads=-1)
```

#### swift2.classes.Parameteriser

```python
Parameteriser(handle, release_native, type_id=None, prior_ref_count=0)
```

Bases: <code>[DeletableCffiNativeHandle](#refcount.interop.DeletableCffiNativeHandle)</code>

Wrapper around a native parameteriser.

<details class="note" open>
<summary>Note</summary>
This is a parent class for more common types such as 
[swift2.classes.HypercubeParameteriser][]
</details>

**Functions:**

- [**apply_sys_config**](#swift2.classes.Parameteriser.apply_sys_config) – Apply a model configuration to a simulation
- [**score_for_objective**](#swift2.classes.Parameteriser.score_for_objective) – Computes the value of an objective for this given set of parameters
- [**subcatchment_parameteriser**](#swift2.classes.Parameteriser.subcatchment_parameteriser) – Create a parameteriser that gets applied to a subset of a whole catchment
- [**supports_thread_safe_cloning**](#swift2.classes.Parameteriser.supports_thread_safe_cloning) – Is this parameteriser clonable as a deep copy, safe for multi-threading?

##### swift2.classes.Parameteriser.apply_sys_config

```python
apply_sys_config(simulation)
```

Apply a model configuration to a simulation

**Parameters:**

- **simulation** (<code>[Simulation](#swift2.classes.Simulation)</code>) – simulation

##### swift2.classes.Parameteriser.score_for_objective

```python
score_for_objective(objective)
```

Computes the value of an objective for this given set of parameters

##### swift2.classes.Parameteriser.subcatchment_parameteriser

```python
subcatchment_parameteriser(subcatchment)
```

Create a parameteriser that gets applied to a subset of a whole catchment

**Parameters:**

- **subcatchment** (<code>[Simulation](#swift2.classes.Simulation)</code>) – the subcatchment, subset of a whole catchment, identifying which elements (subareas, nodes, links) will be parameterised by the new parameteriser. Other catchment elements are untouched.

**Returns:**

- **HypercubeParameteriser** – New parameteriser whose application is limited to the subcatchment.

**Examples:**

```pycon
>>> sub_cats = simulation.split_to_subcatchments(["node.node_7", "node.node_10"])
>>> sc = sub_cats["node.node_7"]
>>> p = sp.create_parameteriser('generic subarea')
>>> p.add_parameter_to_hypercube("x1", 32, 1, 6e3)
>>> sp = p.subcatchment_parameteriser(sc)
>>> sp.apply_sys_config(simulation)
```

##### swift2.classes.Parameteriser.supports_thread_safe_cloning

```python
supports_thread_safe_cloning()
```

Is this parameteriser clonable as a deep copy, safe for multi-threading?

#### swift2.classes.ScalingParameteriser

```python
ScalingParameteriser(handle, release_native, type_id=None, prior_ref_count=0)
```

Bases: <code>[TransformParameteriser](#swift2.classes.TransformParameteriser)</code>

**Functions:**

- [**add_linear_scaled_parameter**](#swift2.classes.ScalingParameteriser.add_linear_scaled_parameter) –
- [**add_parameter_to_hypercube**](#swift2.classes.ScalingParameteriser.add_parameter_to_hypercube) – Add a parameter to a hypercube. Must be a type of object that is expandable, otherwise may raise an exception
- [**add_to_hypercube**](#swift2.classes.ScalingParameteriser.add_to_hypercube) – Add entries to a hypercube. Must be a type of object that is expandable, otherwise may raise an exception.
- [**add_transform**](#swift2.classes.ScalingParameteriser.add_transform) – Create a parameteriser for which parameter transformations can be defined
- [**apply_sys_config**](#swift2.classes.ScalingParameteriser.apply_sys_config) – Apply a model configuration to a simulation
- [**as_dataframe**](#swift2.classes.ScalingParameteriser.as_dataframe) – Convert this hypercube parameteriser to a pandas data frame representation
- [**backtransform**](#swift2.classes.ScalingParameteriser.backtransform) – Get the parameteriser values in the untransformed space
- [**clone**](#swift2.classes.ScalingParameteriser.clone) –
- [**create_parameter_sampler**](#swift2.classes.ScalingParameteriser.create_parameter_sampler) – Creates a sampler for this parameteriser
- [**filtered_parameters**](#swift2.classes.ScalingParameteriser.filtered_parameters) – Wrap a parameteriser in a filter that can hide some parameters
- [**from_dataframe**](#swift2.classes.ScalingParameteriser.from_dataframe) – Create a parameteriser
- [**hide_parameters**](#swift2.classes.ScalingParameteriser.hide_parameters) – Hide some parameters (from the outside e.g. optimisers) in a filter parameteriser
- [**linear_parameteriser**](#swift2.classes.ScalingParameteriser.linear_parameteriser) – Create a scaled linear parameteriser, tying by a linear transformation a (resp several) model state to a (resp several) parameter values
- [**linear_parameteriser_from**](#swift2.classes.ScalingParameteriser.linear_parameteriser_from) – Create a scaled linear parameteriser, tying by a linear transformation a (resp several) model state to a (resp several) parameter values
- [**make_state_init_parameteriser**](#swift2.classes.ScalingParameteriser.make_state_init_parameteriser) – Create a parameteriser used for model state initialisation
- [**num_free_parameters**](#swift2.classes.ScalingParameteriser.num_free_parameters) – Number of free parameters in this hypercube parameteriser
- [**score_for_objective**](#swift2.classes.ScalingParameteriser.score_for_objective) – Computes the value of an objective for this given set of parameters
- [**set_hypercube**](#swift2.classes.ScalingParameteriser.set_hypercube) – Set the properties of a hypercube parameteriser
- [**set_max_parameter_value**](#swift2.classes.ScalingParameteriser.set_max_parameter_value) – Sets the value(s) of the upper bound of one or more parameter(s)
- [**set_min_parameter_value**](#swift2.classes.ScalingParameteriser.set_min_parameter_value) – Sets the value(s) of the lower bound of one or more parameter(s)
- [**set_parameter_definition**](#swift2.classes.ScalingParameteriser.set_parameter_definition) – Sets the feasible range and value for a parameter
- [**set_parameter_value**](#swift2.classes.ScalingParameteriser.set_parameter_value) – Sets the value(s) of one or more parameter(s)
- [**show_parameters**](#swift2.classes.ScalingParameteriser.show_parameters) – Show some parameters (from the outside e.g. optimisers) in a filter parameteriser
- [**subcatchment_parameteriser**](#swift2.classes.ScalingParameteriser.subcatchment_parameteriser) – Create a parameteriser that gets applied to a subset of a whole catchment
- [**supports_thread_safe_cloning**](#swift2.classes.ScalingParameteriser.supports_thread_safe_cloning) – Is this parameteriser clonable as a deep copy, safe for multi-threading?
- [**wrap_transform**](#swift2.classes.ScalingParameteriser.wrap_transform) – Create a parameteriser for which parameter transformations can be defined.

##### swift2.classes.ScalingParameteriser.add_linear_scaled_parameter

```python
add_linear_scaled_parameter(param_name, state_name, scaling_var_name, min_p_val, max_p_val, value, intercept=0.0)
```

##### swift2.classes.ScalingParameteriser.add_parameter_to_hypercube

```python
add_parameter_to_hypercube(name, value, min, max)
```

Add a parameter to a hypercube. Must be a type of object that is expandable, otherwise may raise an exception

##### swift2.classes.ScalingParameteriser.add_to_hypercube

```python
add_to_hypercube(specs)
```

Add entries to a hypercube. Must be a type of object that is expandable, otherwise may raise an exception.

**Parameters:**

- **specs** (<code>[DataFrame](#pandas.DataFrame)</code>) – An optional data frame description of the parameter set, with at least columns Name, Min, Max, Value.

##### swift2.classes.ScalingParameteriser.add_transform

```python
add_transform(param_name, inner_param_name, transform_id, a=1.0, b=0.0)
```

Create a parameteriser for which parameter transformations can be defined

```
This allows to define e.g. a virtual parameter log_X instead of calibrating on the parameter X.
```

**Parameters:**

- **param_name** (<code>[str](#str)</code>) – the name of the meta-parameter. Note that it can be the same value as inner_param_name, but this is NOT recommended.
- **inner_param_name** (<code>[str](#str)</code>) – the name of the parameter being transformed
- **transform_id** (<code>[str](#str)</code>) – identifier for a known bijective univariate function
- **a** (<code>[float](#float)</code>) – parameter in Y = F(ax+b). Defaults to 1.0.
- **b** (<code>[float](#float)</code>) – parameter in Y = F(ax+b). Defaults to 0.0.

##### swift2.classes.ScalingParameteriser.apply_sys_config

```python
apply_sys_config(simulation)
```

Apply a model configuration to a simulation

**Parameters:**

- **simulation** (<code>[Simulation](#swift2.classes.Simulation)</code>) – simulation

##### swift2.classes.ScalingParameteriser.as_dataframe

```python
as_dataframe()
```

Convert this hypercube parameteriser to a pandas data frame representation

**Returns:**

- <code>[DataFrame](#pandas.DataFrame)</code> – pd.DataFrame: pandas data frame

##### swift2.classes.ScalingParameteriser.backtransform

```python
backtransform()
```

Get the parameteriser values in the untransformed space

Get the parameteriser values in the untransformed space, i.e. remove any
transform added via \[`HypercubeParameteriser.wrap_transform`\][HypercubeParameteriser.wrap_transform].
This allows to transform back e.g. from a virtual parameter log_X
to the underlying model (or even virtual/meta) parameter X.

**Returns:**

- **HypercubeParameteriser** (<code>[HypercubeParameteriser](#swift2.classes.HypercubeParameteriser)</code>) – The parameters definitions without the transforms (if there are any)

**Examples:**

```pycon
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

##### swift2.classes.ScalingParameteriser.clone

```python
clone()
```

##### swift2.classes.ScalingParameteriser.create_parameter_sampler

```python
create_parameter_sampler(seed=0, type='urs')
```

Creates a sampler for this parameteriser

**Parameters:**

- **seed** (<code>[int](#int)</code>) – a seed for the sampler. Defaults to 0.
- **type** (<code>[str](#str)</code>) – the type of sampler. Defaults to "urs". Only option supported as of 2023-01.

**Returns:**

- **CandidateFactorySeed** (<code>[CandidateFactorySeed](#swift2.classes.CandidateFactorySeed)</code>) – a sampler, aka candidate factory

##### swift2.classes.ScalingParameteriser.filtered_parameters

```python
filtered_parameters()
```

Wrap a parameteriser in a filter that can hide some parameters

##### swift2.classes.ScalingParameteriser.from_dataframe

```python
from_dataframe(type='Generic subareas', definition=None)
```

Create a parameteriser

**Parameters:**

- **type** (<code>[str](#str)</code>) – A string identifying the type of parameteriser to use. Recognised types are (case insensitive) 'log-likelihood', 'generic', 'subareas', 'links', 'nodes' and 'muskingum'. Defaults to "Generic subareas".
- **specs** (<code>[DataFrame](#pandas.DataFrame)</code>) – An optional data frame description of the parameter set, with at least columns Name, Min, Max, Value. Defaults to None.

**Returns:**

- **HypercubeParameteriser** (<code>[HypercubeParameteriser](#swift2.classes.HypercubeParameteriser)</code>) – new parameteriser

**Examples:**

```pycon
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

##### swift2.classes.ScalingParameteriser.hide_parameters

```python
hide_parameters(patterns, regex=False, starts_with=False, strict=False)
```

Hide some parameters (from the outside e.g. optimisers) in a filter parameteriser

**Parameters:**

- **patterns** (<code>\[[type](#type)\]</code>) – character, one or more pattern to match and hide matching parameters. Match according to other parameters.
- **regex** (<code>[bool](#bool)</code>) – logical, defaults False, should the patterns be used as regular expressions.. Defaults to False.
- **starts_with** (<code>[bool](#bool)</code>) – logical, defaults False. Ignored if regex is True. Should the patterns be used as starting strings in the parameter names.. Defaults to False.
- **strict** (<code>[bool](#bool)</code>) – logical, default False. Used only if regex and starts_with are False. If True, raises an error if one of the "patterns" has no exact match in the parameters.. Defaults to False.

##### swift2.classes.ScalingParameteriser.linear_parameteriser

```python
linear_parameteriser(param_name, state_name, scaling_var_name, min_p_val, max_p_val, value, selector_type='subareas', intercept=0.0)
```

Create a scaled linear parameteriser, tying by a linear transformation a (resp several) model state to a (resp several) parameter values

This allows to define tied parameters where pval = a * modelStateVal + intercept.
The intent in particular is to define virtual model parameters such as initial store value as a fraction of the maximum storage capacity.

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

**Returns:**

- **ScalingParameteriser** – new ScalingParameteriser

##### swift2.classes.ScalingParameteriser.linear_parameteriser_from

```python
linear_parameteriser_from(data_frame, selector_type='subareas')
```

Create a scaled linear parameteriser, tying by a linear transformation a (resp several) model state to a (resp several) parameter values
This allows to define tied parameters where pval = a * modelStateVal + intercept. The intent in particular is to define virtual model parameters such as initial store value as a fraction of the maximum storage capacity.

**Parameters:**

- **data_frame** (<code>[DataFrame](#pandas.DataFrame)</code>) – data frame with columns "param_name", "state_name", "scaling_var_name", "min_value", "max_value", "value", "intercept",
- **selector_type** (<code>[str](#str)</code>) – [description]. Defaults to "subareas".

**Returns:**

- **ScalingParameteriser** – ScalingParameteriser

##### swift2.classes.ScalingParameteriser.make_state_init_parameteriser

```python
make_state_init_parameteriser()
```

Create a parameteriser used for model state initialisation

This allows to define tied parameters where, for instance, pval = a * modelStateVal.
A more concrete use case is to define an initial soil moisture store 'S0',
as a fraction of the model store capacity 'Smax'.
The model state to initialise is 'S'

<details class="note" open>
<summary>Note</summary>
See also [swift2.classes.ScalingParameteriser][] for typical joint usage.
</details>

**Returns:**

- **StateInitParameteriser** (<code>[StateInitParameteriser](#swift2.classes.StateInitParameteriser)</code>) – state initialisation parameteriser

**Examples:**

```pycon
>>> todo()
```

##### swift2.classes.ScalingParameteriser.num_free_parameters

```python
num_free_parameters()
```

Number of free parameters in this hypercube parameteriser

**Returns:**

- **int** (<code>[int](#int)</code>) – Number of free parameters

##### swift2.classes.ScalingParameteriser.score_for_objective

```python
score_for_objective(objective)
```

Computes the value of an objective for this given set of parameters

##### swift2.classes.ScalingParameteriser.set_hypercube

```python
set_hypercube(specs)
```

Set the properties of a hypercube parameteriser

**Parameters:**

- **specs** (<code>[DataFrame](#pandas.DataFrame)</code>) – An optional data frame description of the parameter set, with at least columns Name, Min, Max, Value.

##### swift2.classes.ScalingParameteriser.set_max_parameter_value

```python
set_max_parameter_value(variable_name, value)
```

Sets the value(s) of the upper bound of one or more parameter(s)

**Parameters:**

- **variable_name** (<code>[VecStr](#swift2.const.VecStr)</code>) – one or more parameter name(s)
- **value** (<code>[VecScalars](#swift2.const.VecScalars)</code>) – one or more parameter value(s)

##### swift2.classes.ScalingParameteriser.set_min_parameter_value

```python
set_min_parameter_value(variable_name, value)
```

Sets the value(s) of the lower bound of one or more parameter(s)

**Parameters:**

- **variable_name** (<code>[VecStr](#swift2.const.VecStr)</code>) – one or more parameter name(s)
- **value** (<code>[VecScalars](#swift2.const.VecScalars)</code>) – one or more parameter value(s)

##### swift2.classes.ScalingParameteriser.set_parameter_definition

```python
set_parameter_definition(variable_name, min, max, value)
```

Sets the feasible range and value for a parameter

**Parameters:**

- **variable_name** (<code>[str](#str)</code>) – parameter name
- **min** (<code>[float](#float)</code>) – min
- **max** (<code>[float](#float)</code>) – max
- **value** (<code>[float](#float)</code>) – value

##### swift2.classes.ScalingParameteriser.set_parameter_value

```python
set_parameter_value(variable_name, value)
```

Sets the value(s) of one or more parameter(s)

**Parameters:**

- **variable_name** (<code>[VecStr](#swift2.const.VecStr)</code>) – one or more parameter name(s)
- **value** (<code>[VecScalars](#swift2.const.VecScalars)</code>) – one or more parameter value(s)

##### swift2.classes.ScalingParameteriser.show_parameters

```python
show_parameters(patterns, regex=False, starts_with=False)
```

Show some parameters (from the outside e.g. optimisers) in a filter parameteriser

**Parameters:**

- **patterns** (<code>\[[type](#type)\]</code>) – character, one or more pattern to match and show matching parameters. Match according to other parameters
- **regex** (<code>[bool](#bool)</code>) – should the patterns be used as regular expressions. Defaults to False.
- **starts_with** (<code>[bool](#bool)</code>) – should the patterns be used as starting strings in the parameter names. Defaults to False.

##### swift2.classes.ScalingParameteriser.subcatchment_parameteriser

```python
subcatchment_parameteriser(subcatchment)
```

Create a parameteriser that gets applied to a subset of a whole catchment

**Parameters:**

- **subcatchment** (<code>[Simulation](#swift2.classes.Simulation)</code>) – the subcatchment, subset of a whole catchment, identifying which elements (subareas, nodes, links) will be parameterised by the new parameteriser. Other catchment elements are untouched.

**Returns:**

- **HypercubeParameteriser** – New parameteriser whose application is limited to the subcatchment.

**Examples:**

```pycon
>>> sub_cats = simulation.split_to_subcatchments(["node.node_7", "node.node_10"])
>>> sc = sub_cats["node.node_7"]
>>> p = sp.create_parameteriser('generic subarea')
>>> p.add_parameter_to_hypercube("x1", 32, 1, 6e3)
>>> sp = p.subcatchment_parameteriser(sc)
>>> sp.apply_sys_config(simulation)
```

##### swift2.classes.ScalingParameteriser.supports_thread_safe_cloning

```python
supports_thread_safe_cloning()
```

Is this parameteriser clonable as a deep copy, safe for multi-threading?

##### swift2.classes.ScalingParameteriser.wrap_transform

```python
wrap_transform()
```

Create a parameteriser for which parameter transformations can be defined.

This allows to define e.g. a virtual parameter log_X instead of calibrating on the parameter X.

**Returns:**

- **TransformParameteriser** (<code>[TransformParameteriser](#swift2.classes.TransformParameteriser)</code>) – A new parameteriser (TransformParameteriser) which has methods to define parameter transforms

#### swift2.classes.SceTerminationCondition

```python
SceTerminationCondition(handle, release_native, type_id=None, prior_ref_count=0)
```

Bases: <code>[DeletableCffiNativeHandle](#refcount.interop.DeletableCffiNativeHandle)</code>

#### swift2.classes.Simulation

```python
Simulation(handle, release_native, type_id=None, prior_ref_count=0)
```

Bases: <code>[DeletableCffiNativeHandle](#refcount.interop.DeletableCffiNativeHandle)</code>, <code>[SimulationMixin](#swift2.classes.SimulationMixin)</code>

Wrapper around single dimension simulation objects

**Functions:**

- [**add_state_initialiser**](#swift2.classes.Simulation.add_state_initialiser) – Adds a state initialiser to any prior list of state initialisers
- [**apply_recording_function**](#swift2.classes.Simulation.apply_recording_function) – DRAFT Advanced/technical. Record states to a record provider using a callable function.
- [**check_simulation**](#swift2.classes.Simulation.check_simulation) – Checks whether a simulation is configured to a state where it is executable
- [**clone**](#swift2.classes.Simulation.clone) – Clone this simulation (deep copy)
- [**cookie_cut_dendritic_catchment**](#swift2.classes.Simulation.cookie_cut_dendritic_catchment) – cookie cut a dendritic catchment (without confluences)
- [**create_ensemble_forecast_simulation**](#swift2.classes.Simulation.create_ensemble_forecast_simulation) – Create an ensemble forecast simulation
- [**create_multisite_objective**](#swift2.classes.Simulation.create_multisite_objective) – Creates an objective that combines multiple statistics. Used for joined, "whole of catchment" calibration
- [**create_objective**](#swift2.classes.Simulation.create_objective) – Creates an objective calculator
- [**describe**](#swift2.classes.Simulation.describe) – Describe the catchment model structure using simple python representations
- [**ensemble_simulation**](#swift2.classes.Simulation.ensemble_simulation) – Create an ensemble simulation templated from this simulation
- [**erris_ensemble_simulation**](#swift2.classes.Simulation.erris_ensemble_simulation) – Creates an ensemble simulation templated on this simulation, with an ERRIS model on one of the network element
- [**exec_simulation**](#swift2.classes.Simulation.exec_simulation) – Execute a simulation
- [**from_json_file**](#swift2.classes.Simulation.from_json_file) – Create a model simulation from a file with a JSON serialisation.
- [**get_all_played**](#swift2.classes.Simulation.get_all_played) – Gets all the time series of models variables into which input time sereis is/are played
- [**get_all_recorded**](#swift2.classes.Simulation.get_all_recorded) – Gets all the time series of models variables recorded from
- [**get_catchment_structure**](#swift2.classes.Simulation.get_catchment_structure) – Gets the essential connective structure of a catchment
- [**get_link_ids**](#swift2.classes.Simulation.get_link_ids) – Gets all the identifiers of the links in the catchment
- [**get_link_names**](#swift2.classes.Simulation.get_link_names) – Gets all the names of the links in the catchment
- [**get_node_ids**](#swift2.classes.Simulation.get_node_ids) – Gets all the identifiers of the nodes in the catchment
- [**get_node_names**](#swift2.classes.Simulation.get_node_names) – Gets all the names of the nodes in the catchment
- [**get_played**](#swift2.classes.Simulation.get_played) – Retrieves one or more played (input) time series from a simulation
- [**get_played_varnames**](#swift2.classes.Simulation.get_played_varnames) – Gets all the names of model states fed an input time series
- [**get_recorded**](#swift2.classes.Simulation.get_recorded) – Retrieves a recorded time series from a simulation
- [**get_recorded_varnames**](#swift2.classes.Simulation.get_recorded_varnames) – Gets all the names of the recorded states
- [**get_simulation_span**](#swift2.classes.Simulation.get_simulation_span) – Gets the simulation span of this simulation
- [**get_state_value**](#swift2.classes.Simulation.get_state_value) – Gets the value(s) of a model state(s)
- [**get_subarea_ids**](#swift2.classes.Simulation.get_subarea_ids) – Gets all the identifiers of the subareas in the catchment
- [**get_subarea_names**](#swift2.classes.Simulation.get_subarea_names) – Gets all the names of the subareas in the catchment
- [**get_variable_ids**](#swift2.classes.Simulation.get_variable_ids) – Gets all the names of the variables of an element (link, node, subarea) within a catchment
- [**is_variable_id**](#swift2.classes.Simulation.is_variable_id) – Are one or more model state identifier(s) valid
- [**muskingum_param_constraints**](#swift2.classes.Simulation.muskingum_param_constraints) – Create a parameteriser with Muskingum-type constraints.
- [**play_input**](#swift2.classes.Simulation.play_input) – Sets one or more time series as input(s) to a simulation
- [**play_inputs**](#swift2.classes.Simulation.play_inputs) – Assign input time series from a time series library to a model simulation
- [**play_subarea_input**](#swift2.classes.Simulation.play_subarea_input) – Sets time series as input to a simulation
- [**prepare_dual_pass_forecasting**](#swift2.classes.Simulation.prepare_dual_pass_forecasting) – Create an ensemble simulation for forecasting with the Dual Pass error correction method
- [**prepare_erris_forecasting**](#swift2.classes.Simulation.prepare_erris_forecasting) – Create an ensemble simulation for forecasting with ERRIS
- [**record_singular_state**](#swift2.classes.Simulation.record_singular_state) – DRAFT Advanced/technical. Record states to a record provider.
- [**record_state**](#swift2.classes.Simulation.record_state) – Record a time series of one of the state of the model
- [**remove_state_initialisers**](#swift2.classes.Simulation.remove_state_initialisers) – Forces the removal of any state initialiser.
- [**reset_model_states**](#swift2.classes.Simulation.reset_model_states) – Reset the model states of a simulation, and apply one or more state initialers if the simulation is configured with any.
- [**set_error_correction_model**](#swift2.classes.Simulation.set_error_correction_model) – Add an error correction model to an element in a catchment
- [**set_reservoir_geometry**](#swift2.classes.Simulation.set_reservoir_geometry) – Sets the geometry of a reservoir
- [**set_reservoir_max_discharge**](#swift2.classes.Simulation.set_reservoir_max_discharge) – Sets a reservoir operating curve, maximum release for a given level
- [**set_reservoir_min_discharge**](#swift2.classes.Simulation.set_reservoir_min_discharge) – Sets a reservoir operating curve, minimum release for a given level
- [**set_reservoir_model**](#swift2.classes.Simulation.set_reservoir_model) – Sets a new reservoir model on an element
- [**set_simulation_span**](#swift2.classes.Simulation.set_simulation_span) – Sets the simulation span
- [**set_simulation_time_step**](#swift2.classes.Simulation.set_simulation_time_step) – Sets the time step of this simulation
- [**set_state_value**](#swift2.classes.Simulation.set_state_value) – Sets the value of a model state
- [**set_states**](#swift2.classes.Simulation.set_states) – Apply memory states to a simulation
- [**snapshot_state**](#swift2.classes.Simulation.snapshot_state) – Take a snapshot of the memory states of a simulation
- [**sort_by_execution_order**](#swift2.classes.Simulation.sort_by_execution_order) – Sort the specified element ids according to the execution order of the simulation
- [**split_to_subcatchments**](#swift2.classes.Simulation.split_to_subcatchments) – Split a catchment in subcatchments, given a list of node/link element identifiers
- [**subset_catchment**](#swift2.classes.Simulation.subset_catchment) – Subsets a catchment, keeping only a portion above or below a node, link or subarea.
- [**swap_model**](#swift2.classes.Simulation.swap_model) – Clone and change a simulation, using another model
- [**to_json_file**](#swift2.classes.Simulation.to_json_file) – Save a model simulation from a file with a JSON serialisation.
- [**use_state_initialises**](#swift2.classes.Simulation.use_state_initialises) – Sets the state initialiser to use for a simulation. This forces the removal of any prior state initialiser.

##### swift2.classes.Simulation.add_state_initialiser

```python
add_state_initialiser(state_initialiser)
```

Adds a state initialiser to any prior list of state initialisers

##### swift2.classes.Simulation.apply_recording_function

```python
apply_recording_function(recording_func, var_ids, recording_provider, data_ids)
```

DRAFT Advanced/technical. Record states to a record provider using a callable function.

Likely not for end users. This is used by methods such as
\[`EnsembleSimulation.record_ensemble_state`\][swift2.classes.EnsembleSimulation.record_ensemble_state].

##### swift2.classes.Simulation.check_simulation

```python
check_simulation()
```

Checks whether a simulation is configured to a state where it is executable

##### swift2.classes.Simulation.clone

```python
clone()
```

Clone this simulation (deep copy)

**Returns:**

- **Simulation** (<code>[Simulation](#swift2.classes.Simulation)</code>) – A new simulation object

##### swift2.classes.Simulation.cookie_cut_dendritic_catchment

```python
cookie_cut_dendritic_catchment(bottom_element_id, top_element_ids)
```

cookie cut a dendritic catchment (without confluences)

**Parameters:**

- **bottom_element_id** (<code>[str](#str)</code>) – identifier of the most downstream element to keep
- **top_element_ids** (<code>[str](#str)</code>) – identifier(s) of the most upstream element(s) to keep

**Returns:**

- **Simulation** – a subcatchment simulation, cookie cut from the base simulation. Deep clone of objects.

##### swift2.classes.Simulation.create_ensemble_forecast_simulation

```python
create_ensemble_forecast_simulation(data_library, start, end, input_map, lead_time, ensemble_size, n_time_steps_between_forecasts)
```

Create an ensemble forecast simulation

**Parameters:**

- **data_library** (<code>[Any](#typing.Any)</code>) – external pointer type ENSEMBLE_DATA_SET_PTR, or a Python class wrapper around it
- **start** (<code>[ConvertibleToTimestamp](#cinterop.timeseries.ConvertibleToTimestamp)</code>) – the start date of the simulation. The time zone will be forced to UTC.
- **end** (<code>[ConvertibleToTimestamp](#cinterop.timeseries.ConvertibleToTimestamp)</code>) – the end date of the simulation. The time zone will be forced to UTC.
- **input_map** (<code>[dict](#dict)</code>) – a named list were names are the data library data identifiers, and values are character vectors with model state identifiers.
- **lead_time** (<code>[int](#int)</code>) – integer, the length in time steps of the forecasts.
- **ensemble_size** (<code>[int](#int)</code>) – ensemble size
- **n_time_steps_between_forecasts** (<code>[int](#int)</code>) – nTimeStepsBetweenForecasts

**Returns:**

- <code>[EnsembleForecastSimulation](#swift2.classes.EnsembleForecastSimulation)</code> – An external pointer

##### swift2.classes.Simulation.create_multisite_objective

```python
create_multisite_objective(statspec, observations, weights)
```

Creates an objective that combines multiple statistics. Used for joined, "whole of catchment" calibration

**Parameters:**

- **statspec** (<code>[DataFrame](#pandas.DataFrame)</code>) – dataframe defining the objectives used. See function \[`multi_statistic_definition`\][swift2.statistics.multi_statistic_definition] to help build this dataframe.
- **observations** (<code>[Sequence](#typing.Sequence)\[[TimeSeriesLike](#cinterop.timeseries.TimeSeriesLike)\]</code>) – A list of (time series) observations to calculated the statistics. Must be of same length as the number of rows of statspec.
- **weights** (<code>[Dict](#typing.Dict)\[[str](#str), [float](#float)\]</code>) – numeric vector of weights to ponderate each objective.

**Returns:**

- **ObjectiveEvaluator** (<code>[ObjectiveEvaluator](#swift2.classes.ObjectiveEvaluator)</code>) – an objective evaluator

**Examples:**

```pycon
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

```pycon
>>> ms.record_state(mvids)
>>> ms.exec_simulation()
>>> 
>>> modFlows = ms.get_recorded()
>>> 
```

```pycon
>>> w = dict(zip(mvids, [1.0, 2.0]))
>>> w
{'node.n2.OutflowRate': 1.0, 'node.n4.OutflowRate': 2.0}
>>> span = ms.get_simulation_span()
>>> 
```

```pycon
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

```pycon
>>> dummy = sp.create_parameteriser()
>>> obj.get_scores(dummy)
{'node.n2.OutflowRate': -4.152338377267432, 'node.n4.OutflowRate': 0.8884789439301954}
>>> 
```

```pycon
>>> obj.get_score(dummy)
{'scores': {'MultisiteObjectives': 0.7917934964690136}, 'sysconfig': Empty DataFrame
Columns: [Name, Value, Min, Max]
Index: []}
>>>
```

##### swift2.classes.Simulation.create_objective

```python
create_objective(state_name, observation, statistic, start_date, end_date)
```

Creates an objective calculator

**Parameters:**

- **state_name** (<code>[str](#str)</code>) – The name identifying the model state variable to calibrate against the observation
- **observation** (<code>[TimeSeriesLike](#cinterop.timeseries.TimeSeriesLike)</code>) – an xts
- **statistic** (<code>[str](#str)</code>) – statistic identifier, e.g. "NSE"
- **start_date** (<code>[ConvertibleToTimestamp](#cinterop.timeseries.ConvertibleToTimestamp)</code>) – start date of the period to calculate statistics on
- **end_date** (<code>[ConvertibleToTimestamp](#cinterop.timeseries.ConvertibleToTimestamp)</code>) – end date of the period to calculate statistics on

**Returns:**

- **ObjectiveEvaluator** (<code>[ObjectiveEvaluator](#swift2.classes.ObjectiveEvaluator)</code>) – single objective evaluator

##### swift2.classes.Simulation.describe

```python
describe(verbosity=None)
```

Describe the catchment model structure using simple python representations

##### swift2.classes.Simulation.ensemble_simulation

```python
ensemble_simulation(ensemble_size)
```

Create an ensemble simulation templated from this simulation

**Parameters:**

- **ensemble_size** (<code>[int](#int)</code>) – The size of the ensemble dimension

**Returns:**

- **EnsembleSimulation** (<code>[EnsembleSimulation](#swift2.classes.EnsembleSimulation)</code>) – Ensemble simulation (ensemble simulation runner)

##### swift2.classes.Simulation.erris_ensemble_simulation

```python
erris_ensemble_simulation(warmup_start, warmup_end, observed_ts, error_model_element_id)
```

Creates an ensemble simulation templated on this simulation, with an ERRIS model on one of the network element

**Parameters:**

- **warmup_start** (<code>[ConvertibleToTimestamp](#cinterop.timeseries.ConvertibleToTimestamp)</code>) – start time stamp for the warmup period
- **warmup_end** (<code>[ConvertibleToTimestamp](#cinterop.timeseries.ConvertibleToTimestamp)</code>) – end time stamp for the warmup period
- **observed_ts** (<code>[TimeSeriesLike](#cinterop.timeseries.TimeSeriesLike)</code>) – Time series of observations to correct prediction against
- **error_model_element_id** (<code>[str](#str)</code>) – model element identifier where to set up an ERRIS correction model

**Returns:**

- **EnsembleSimulation** (<code>[EnsembleSimulation](#swift2.classes.EnsembleSimulation)</code>) – Ensemble simulation (ensemble simulation runner)

##### swift2.classes.Simulation.exec_simulation

```python
exec_simulation(reset_initial_states=True)
```

Execute a simulation

**Parameters:**

- **reset_initial_states** (<code>[bool](#bool)</code>) – logical, should the states of the model be reinitialized before the first time step.

##### swift2.classes.Simulation.from_json_file

```python
from_json_file(file_path)
```

Create a model simulation from a file with a JSON serialisation.

**Parameters:**

- **file_path** (<code>[str](#str)</code>) – valid file path.

**Returns:**

- **Simulation** (<code>[Simulation](#swift2.classes.Simulation)</code>) – a catchment simulation.

##### swift2.classes.Simulation.get_all_played

```python
get_all_played()
```

Gets all the time series of models variables into which input time sereis is/are played

##### swift2.classes.Simulation.get_all_recorded

```python
get_all_recorded()
```

Gets all the time series of models variables recorded from

##### swift2.classes.Simulation.get_catchment_structure

```python
get_catchment_structure()
```

Gets the essential connective structure of a catchment

**Parameters:**

- **simulation** (<code>[Simulation](#swift2.classes.Simulation)</code>) – base catchment simulation

**Returns:**

- <code>[Dict](#typing.Dict)\[[str](#str), [Any](#typing.Any)\]</code> – Dict\[str, Any\]: A nested dictionary describing the catchment connectivity of subareas, links, and nodes

**Examples:**

```pycon
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

##### swift2.classes.Simulation.get_link_ids

```python
get_link_ids()
```

Gets all the identifiers of the links in the catchment

##### swift2.classes.Simulation.get_link_names

```python
get_link_names()
```

Gets all the names of the links in the catchment

##### swift2.classes.Simulation.get_node_ids

```python
get_node_ids()
```

Gets all the identifiers of the nodes in the catchment

##### swift2.classes.Simulation.get_node_names

```python
get_node_names()
```

Gets all the names of the nodes in the catchment

##### swift2.classes.Simulation.get_played

```python
get_played(var_ids=None, start_time=None, end_time=None)
```

Retrieves one or more played (input) time series from a simulation

**Parameters:**

- **var_ids** (<code>optional str or sequence of str</code>) – name(s) of the model variable(s) into which a time series is played as input. e.g. 'Catchment.StreamflowRate'. If missing, a multivariate time series of all played states is returned; this may be a large amount of data.
- **start_time** (<code>datetime like</code>) – An optional parameter, the start of a period to subset the time series
- **end_time** (<code>datetime like</code>) – An optional parameter, the end of a period to subset the time series

**Returns:**

- <code>[DataArray](#xarray.DataArray)</code> – xr.DataArray: a time series, possibly multivariate.

##### swift2.classes.Simulation.get_played_varnames

```python
get_played_varnames()
```

Gets all the names of model states fed an input time series

##### swift2.classes.Simulation.get_recorded

```python
get_recorded(var_ids=None, start_time=None, end_time=None)
```

Retrieves a recorded time series from a simulation

**Parameters:**

- **var_ids** (<code>optional str or sequence of str</code>) – name(s) of the model variable(s) recorded to a time series. e.g. 'Catchment.StreamflowRate'. If missing, a multivariate time series of all played states is returned; this may be a large amount of data.
- **start_time** (<code>datetime like</code>) – An optional parameter, the start of a period to subset the time series
- **end_time** (<code>datetime like</code>) – An optional parameter, the end of a period to subset the time series

**Returns:**

- <code>[DataArray](#xarray.DataArray)</code> – xr.DataArray: a time series, possibly multivariate.

##### swift2.classes.Simulation.get_recorded_varnames

```python
get_recorded_varnames()
```

Gets all the names of the recorded states

**Returns:**

- <code>[List](#typing.List)\[[str](#str)\]</code> – List\[str\]: The names of the state variables being recorded into time series

##### swift2.classes.Simulation.get_simulation_span

```python
get_simulation_span()
```

Gets the simulation span of this simulation

**Returns:**

- <code>[Dict](#typing.Dict)\[[str](#str), [Any](#typing.Any)\]</code> – Dict\[str,Any\]: information on start, end, time step

##### swift2.classes.Simulation.get_state_value

```python
get_state_value(var_id)
```

Gets the value(s) of a model state(s)

**Parameters:**

- **var_id** (<code>[VecStr](#swift2.const.VecStr)</code>) – string or sequence of str, model variable state identifier(s)

**Returns:**

- <code>[Union](#typing.Union)\[[Dict](#typing.Dict)\[[str](#str), [float](#float)\], [float](#float)\]</code> – value(s) of the requested model states

##### swift2.classes.Simulation.get_subarea_ids

```python
get_subarea_ids()
```

Gets all the identifiers of the subareas in the catchment

##### swift2.classes.Simulation.get_subarea_names

```python
get_subarea_names()
```

Gets all the names of the subareas in the catchment

##### swift2.classes.Simulation.get_variable_ids

```python
get_variable_ids(element_id=None, full_id=True)
```

Gets all the names of the variables of an element (link, node, subarea) within a catchment

**Parameters:**

- **element_id** (<code>[Optional](#typing.Optional)\[[str](#str)\]</code>) – a character, identifier of the element within the catchment
- **full_id** (<code>[bool](#bool)</code>) – boolean, if TRUE return the full hierarchical identifier

##### swift2.classes.Simulation.is_variable_id

```python
is_variable_id(var_id)
```

Are one or more model state identifier(s) valid

**Parameters:**

- **var_id** (<code>[VecStr](#swift2.const.VecStr)</code>) – model identifier(s)

**Returns:**

- <code>[Union](#typing.Union)\[[Dict](#typing.Dict)\[[str](#str), [bool](#bool)\], [bool](#bool)\]</code> – Union\[Dict[str, bool], bool\]: whether the identifier(s) are valid. A dictionary is returned if the input is vectorised rather than scalar.

##### swift2.classes.Simulation.muskingum_param_constraints

```python
muskingum_param_constraints(inner_parameters, delta_t=1.0, param_name_k='K', param_name_x='X')
```

Create a parameteriser with Muskingum-type constraints.

Given an existing parameteriser, create a wrapper that adds constraints on two of its parameters.

**Parameters:**

- **inner_parameters** (<code>[HypercubeParameteriser](#swift2.classes.HypercubeParameteriser)</code>) – A SWIFT parameteriser object that contains two Muskingum-type attenuation and delay parameters.
- **delta_t** (<code>[int](#int)</code>) – the simulation time step in HOURS. Defaults to 1.
- **param_name_k** (<code>[str](#str)</code>) – the variable identifier to use for the delay parameter of the Muskingum routing. Defaults to "K".
- **param_name_x** (<code>[str](#str)</code>) – the variable identifier to use for the attenuation parameter of the Muskingum routing. Defaults to "X".

**Returns:**

- **ConstraintParameteriser** (<code>[ConstraintParameteriser](#swift2.classes.ConstraintParameteriser)</code>) – A parameteriser with constraints on the feasibility of the attenuation / delay parameters

**Examples:**

```pycon
>>> todo()
```

##### swift2.classes.Simulation.play_input

```python
play_input(input_ts, var_ids=None)
```

Sets one or more time series as input(s) to a simulation

**Parameters:**

- **input_ts** (<code>[TimeSeriesLike](#cinterop.timeseries.TimeSeriesLike)</code>) – univariate time series. If an xts time series column names must be valid model variable identifiers, unless explicitely provided via varIds
- **var_ids** (<code>optional str or sequence of str</code>) – optional character, the variable identifiers to use, overriding the column names of the inputTs. If not NULL, must be of length equal to the number of columns in inputTs

##### swift2.classes.Simulation.play_inputs

```python
play_inputs(data_library, model_var_id, data_id, resample='')
```

Assign input time series from a time series library to a model simulation

**Parameters:**

- **data_library** (<code>[TimeSeriesLibrary](#uchronia.classes.TimeSeriesLibrary)</code>) – external pointer type ENSEMBLE_DATA_SET_PTR, or a Python class wrapper around it
- **model_var_id** (<code>str or sequence of str</code>) – model state variable unique identifier(s)
- **data_id** (<code>str or sequence of str</code>) – identifier(s) for data in the data_library. If length is not the same as model_var_id, the elements of data_id are reused to match it
- **resample** (<code>str or sequence of str</code>) – identifier(s) for how the series is resampled (aggregated or disaggregated). If length is not the same as model_var_id, the elements of resample are reused to match it

##### swift2.classes.Simulation.play_subarea_input

```python
play_subarea_input(input, subarea_name, input_name)
```

Sets time series as input to a simulation

**Parameters:**

- **input** (<code>[TimeSeriesLike](#cinterop.timeseries.TimeSeriesLike)</code>) – univariate time series.
- **subarea_name** (<code>[str](#str)</code>) – a valid name of the subarea
- **input_name** (<code>[str](#str)</code>) – the name of the input variable to the model (i.e. 'P' for the precip of GR5H)

##### swift2.classes.Simulation.prepare_dual_pass_forecasting

```python
prepare_dual_pass_forecasting(observation, error_model_element_id, warmup_start, warmup_end, required_windows_percentage)
```

Create an ensemble simulation for forecasting with the Dual Pass error correction method

**Parameters:**

- **observation** (<code>[TimeSeriesLike](#cinterop.timeseries.TimeSeriesLike)</code>) – Time series of observations to correct prediction against
- **error_model_element_id** (<code>[str](#str)</code>) – model element identifier where to set up an ERRIS correction model
- **warmup_start** (<code>[ConvertibleToTimestamp](#cinterop.timeseries.ConvertibleToTimestamp)</code>) – start time stamp for the warmup period
- **warmup_end** (<code>[ConvertibleToTimestamp](#cinterop.timeseries.ConvertibleToTimestamp)</code>) – end time stamp for the warmup period
- **required_windows_percentage** (<code>[float](#float)</code>) – required_windows_percentage

**Returns:**

- **EnsembleSimulation** (<code>[EnsembleSimulation](#swift2.classes.EnsembleSimulation)</code>) – Ensemble simulation (ensemble simulation runner)

##### swift2.classes.Simulation.prepare_erris_forecasting

```python
prepare_erris_forecasting(observation, error_model_element_id, warmup_start, warmup_end)
```

Create an ensemble simulation for forecasting with ERRIS

**Parameters:**

- **observation** (<code>[TimeSeriesLike](#cinterop.timeseries.TimeSeriesLike)</code>) – Time series of observations to correct prediction against
- **error_model_element_id** (<code>[str](#str)</code>) – model element identifier where to set up an ERRIS correction model
- **warmup_start** (<code>[ConvertibleToTimestamp](#cinterop.timeseries.ConvertibleToTimestamp)</code>) – start time stamp for the warmup period
- **warmup_end** (<code>[ConvertibleToTimestamp](#cinterop.timeseries.ConvertibleToTimestamp)</code>) – end time stamp for the warmup period

**Returns:**

- **EnsembleSimulation** (<code>[EnsembleSimulation](#swift2.classes.EnsembleSimulation)</code>) – Ensemble simulation (ensemble simulation runner)

##### swift2.classes.Simulation.record_singular_state

```python
record_singular_state(var_ids=CATCHMENT_FLOWRATE_VARID, recording_provider=None, data_ids=None)
```

DRAFT Advanced/technical. Record states to a record provider.

Likely not for end users.

##### swift2.classes.Simulation.record_state

```python
record_state(var_ids=CATCHMENT_FLOWRATE_VARID, recording_provider=None, data_ids=None)
```

Record a time series of one of the state of the model

**Parameters:**

- **var_ids** (<code>[VecStr](#swift2.const.VecStr)</code>) – identifier(s) of the output variable recorded to a time series, e.g. 'Catchment|StreamflowRate' or 'subcatchment.Subarea.runoff'. Defaults to CATCHMENT_FLOWRATE_VARID.
- **recording_provider** (<code>[TimeSeriesLibrary](#uchronia.classes.TimeSeriesLibrary)</code>) – _description_. Defaults to None.
- **data_ids** (<code>[VecStr](#swift2.const.VecStr)</code>) – _description_. Defaults to None.

**Raises:**

- <code>[ValueError](#ValueError)</code> – _description_

##### swift2.classes.Simulation.remove_state_initialisers

```python
remove_state_initialisers()
```

Forces the removal of any state initialiser.

##### swift2.classes.Simulation.reset_model_states

```python
reset_model_states()
```

Reset the model states of a simulation, and apply one or more state initialers if the simulation is configured with any.

##### swift2.classes.Simulation.set_error_correction_model

```python
set_error_correction_model(model_id, element_id, length=1, seed=0)
```

Add an error correction model to an element in a catchment

**Parameters:**

- **model_id** (<code>[str](#str)</code>) – the identifier of the new model to use, e.g. 'ERRIS'
- **element_id** (<code>[str](#str)</code>) – the identifier of the catchment element (node, link, subcatchment) whose outflow rate is corrected.
- **length** (<code>[int](#int)</code>) – other parameters to pass to the creation of the error correction model. Currently length of the AR model only supported.
- **seed** (<code>[int](#int)</code>) – other parameters to pass to the creation of the error correction model. Currently length of the AR model only supported.

##### swift2.classes.Simulation.set_reservoir_geometry

```python
set_reservoir_geometry(element_id, level, storage, area)
```

Sets the geometry of a reservoir

**Parameters:**

- **element_id** (<code>[str](#str)</code>) – Element with a suitable reservoir supporting a geometry description
- **level** (<code>[ndarray](#numpy.ndarray)</code>) – array of water surface levels, in S.I. units (m) TO BE CONFIRMED
- **storage** (<code>[ndarray](#numpy.ndarray)</code>) – array of volume storages, in S.I. units (m3) TO BE CONFIRMED
- **area** (<code>[ndarray](#numpy.ndarray)</code>) – array of surfce areas, in S.I. units (m2) TO BE CONFIRMED

##### swift2.classes.Simulation.set_reservoir_max_discharge

```python
set_reservoir_max_discharge(element_id, level, discharge)
```

Sets a reservoir operating curve, maximum release for a given level

**Parameters:**

- **element_id** (<code>[str](#str)</code>) – Element with a suitable reservoir supporting a geometry description
- **level** (<code>[ndarray](#numpy.ndarray)</code>) – array of levels (m)
- **discharge** (<code>[ndarray](#numpy.ndarray)</code>) – array of maximum discharges (m3/s)

##### swift2.classes.Simulation.set_reservoir_min_discharge

```python
set_reservoir_min_discharge(element_id, level, discharge)
```

Sets a reservoir operating curve, minimum release for a given level

**Parameters:**

- **element_id** (<code>[str](#str)</code>) – Element with a suitable reservoir supporting a geometry description
- **level** (<code>[ndarray](#numpy.ndarray)</code>) – array of levels (m)
- **discharge** (<code>[ndarray](#numpy.ndarray)</code>) – array of minimum discharges (m3/s)

##### swift2.classes.Simulation.set_reservoir_model

```python
set_reservoir_model(new_model_id, element_id)
```

Sets a new reservoir model on an element

**Parameters:**

- **new_model_id** (<code>[str](#str)</code>) – Currently one of: "ControlledReleaseReservoir", "LevelVolumeAreaReservoir", "FarmDamReservoir";
- **element_id** (<code>[str](#str)</code>) – _description_

##### swift2.classes.Simulation.set_simulation_span

```python
set_simulation_span(start, end)
```

Sets the simulation span

**Parameters:**

- **start** (<code>[ConvertibleToTimestamp](#cinterop.timeseries.ConvertibleToTimestamp)</code>) – the start date of the simulation. The time zone will be forced to UTC.
- **end** (<code>[ConvertibleToTimestamp](#cinterop.timeseries.ConvertibleToTimestamp)</code>) – the end date of the simulation. The time zone will be forced to UTC.

##### swift2.classes.Simulation.set_simulation_time_step

```python
set_simulation_time_step(name)
```

Sets the time step of this simulation

**Parameters:**

- **name** (<code>[str](#str)</code>) – a time step identifier, currently 'daily' or 'hourly' are supported. The identifier is made lower case in the function.

##### swift2.classes.Simulation.set_state_value

```python
set_state_value(var_id, value=None)
```

Sets the value of a model state

**Parameters:**

- **var_id** (<code>[Any](#typing.Any)</code>) – character, model variable state identifier(s)
- **value** (<code>[Any](#typing.Any)</code>) – numeric value(s)

##### swift2.classes.Simulation.set_states

```python
set_states(states)
```

Apply memory states to a simulation

**Parameters:**

- **states** (<code>[MemoryStates](#swift2.classes.MemoryStates)</code>) – memory states

##### swift2.classes.Simulation.snapshot_state

```python
snapshot_state()
```

Take a snapshot of the memory states of a simulation

**Returns:**

- **MemoryStates** (<code>[MemoryStates](#swift2.classes.MemoryStates)</code>) – memory states, that can be stored and reapplied

##### swift2.classes.Simulation.sort_by_execution_order

```python
sort_by_execution_order(split_element_ids, sorting_option='')
```

Sort the specified element ids according to the execution order of the simulation

**Parameters:**

- **split_element_ids** (<code>[Sequence](#typing.Sequence)\[[str](#str)\]</code>) – a character vector with element identifiers such as 'node.n1', 'link.linkId_2'
- **sorting_option** (<code>[str](#str)</code>) – a character - for future options. Ignored for now.

**Returns:**

- <code>[List](#typing.List)\[[str](#str)\]</code> – List\[str\]: values in split_element_ids sorted by simulation execution order

##### swift2.classes.Simulation.split_to_subcatchments

```python
split_to_subcatchments(split_element_ids, include_upstream=None)
```

Split a catchment in subcatchments, given a list of node/link element identifiers

**Parameters:**

- **split_element_ids** (<code>[str](#str)</code>) – element identifiers such as 'node.n1', 'link.linkId_2'
- **include_upstream** (<code>[bool](#bool)</code>) – indicates whether for each element in split_element_ids it should be including in the upstream portion of the subcatchment. Defaults to None.

**Returns:**

- **OrderedDict** (<code>[OrderedDict](#typing.OrderedDict)\[[str](#str), [Simulation](#swift2.classes.Simulation)\]</code>) – list of subcatchments resulting from the split

**Examples:**

```pycon
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

##### swift2.classes.Simulation.subset_catchment

```python
subset_catchment(element_id, action='keep_above')
```

Subsets a catchment, keeping only a portion above or below a node, link or subarea.

**Parameters:**

- **element_id** (<code>[str](#str)</code>) – id of the element to cut at.
- **action** (<code>[str](#str)</code>) – how to cut; currently limited to 'keep_above'

**Returns:**

- **Simulation** – a subcatchment simulation, cookie cut from the base simulation. Deep clone of objects.

##### swift2.classes.Simulation.swap_model

```python
swap_model(model_id, what='runoff')
```

Clone and change a simulation, using another model

**Parameters:**

- **model_id** (<code>[str](#str)</code>) – the identifier of the new model to use, e.g. 'GR4J'
- **what** (<code>[str](#str)</code>) – character identifying the type of structure replaced: 'runoff', 'channel_routing'

**Returns:**

- **Simulation** (<code>[Simulation](#swift2.classes.Simulation)</code>) – A SWIFT simulation object, clone of the simulation but with a new model type in use.

##### swift2.classes.Simulation.to_json_file

```python
to_json_file(file_path)
```

Save a model simulation from a file with a JSON serialisation.

**Parameters:**

- **file_path** (<code>[str](#str)</code>) – file path to save to

##### swift2.classes.Simulation.use_state_initialises

```python
use_state_initialises(state_initialiser)
```

Sets the state initialiser to use for a simulation. This forces the removal of any prior state initialiser.

**Parameters:**

- **state_initialiser** (<code>[StateInitialiser](#swift2.classes.StateInitialiser)</code>) – the new state initialiser to use

#### swift2.classes.SimulationMixin

```python
SimulationMixin()
```

A parent class for simulation objects. Most users are unlikely to explicitly use it.

**Functions:**

- [**exec_simulation**](#swift2.classes.SimulationMixin.exec_simulation) – Execute a simulation
- [**get_played_varnames**](#swift2.classes.SimulationMixin.get_played_varnames) – Gets all the names of states fed an input time series
- [**get_recorded_varnames**](#swift2.classes.SimulationMixin.get_recorded_varnames) – Gets all the names of the recorded states
- [**record_state**](#swift2.classes.SimulationMixin.record_state) – Record a time series of one of the state of the model

##### swift2.classes.SimulationMixin.exec_simulation

```python
exec_simulation(reset_initial_states=True)
```

Execute a simulation

**Parameters:**

- **reset_initial_states** (<code>[bool](#bool)</code>) – logical, should the states of the model be reinitialized before the first time step.

##### swift2.classes.SimulationMixin.get_played_varnames

```python
get_played_varnames()
```

Gets all the names of states fed an input time series

**Returns:**

- <code>[List](#typing.List)\[[str](#str)\]</code> – List\[str\]: The names of the state variables fed over the simulation with values from a time series

##### swift2.classes.SimulationMixin.get_recorded_varnames

```python
get_recorded_varnames()
```

Gets all the names of the recorded states

**Returns:**

- <code>[List](#typing.List)\[[str](#str)\]</code> – List\[str\]: The names of the state variables being recorded into time series

##### swift2.classes.SimulationMixin.record_state

```python
record_state(var_ids=CATCHMENT_FLOWRATE_VARID, recording_provider=None, data_ids=None)
```

Record a time series of one of the state of the model

**Parameters:**

- **var_ids** (<code>[VecStr](#swift2.const.VecStr)</code>) – identifier(s) of the output variable recorded to a time series, e.g. 'Catchment|StreamflowRate' or 'subcatchment.Subarea.runoff'. Defaults to CATCHMENT_FLOWRATE_VARID.
- **recording_provider** (<code>[TimeSeriesLibrary](#uchronia.classes.TimeSeriesLibrary)</code>) – _description_. Defaults to None.
- **data_ids** (<code>[VecStr](#swift2.const.VecStr)</code>) – _description_. Defaults to None.

**Raises:**

- <code>[ValueError](#ValueError)</code> – _description_

#### swift2.classes.StateInitParameteriser

```python
StateInitParameteriser(handle, release_native, type_id=None, prior_ref_count=0)
```

Bases: <code>[HypercubeParameteriser](#swift2.classes.HypercubeParameteriser)</code>

**Functions:**

- [**add_parameter_to_hypercube**](#swift2.classes.StateInitParameteriser.add_parameter_to_hypercube) – Add a parameter to a hypercube. Must be a type of object that is expandable, otherwise may raise an exception
- [**add_to_hypercube**](#swift2.classes.StateInitParameteriser.add_to_hypercube) – Add entries to a hypercube. Must be a type of object that is expandable, otherwise may raise an exception.
- [**apply_sys_config**](#swift2.classes.StateInitParameteriser.apply_sys_config) – Apply a model configuration to a simulation
- [**as_dataframe**](#swift2.classes.StateInitParameteriser.as_dataframe) – Convert this hypercube parameteriser to a pandas data frame representation
- [**backtransform**](#swift2.classes.StateInitParameteriser.backtransform) – Get the parameteriser values in the untransformed space
- [**clone**](#swift2.classes.StateInitParameteriser.clone) –
- [**create_parameter_sampler**](#swift2.classes.StateInitParameteriser.create_parameter_sampler) – Creates a sampler for this parameteriser
- [**filtered_parameters**](#swift2.classes.StateInitParameteriser.filtered_parameters) – Wrap a parameteriser in a filter that can hide some parameters
- [**from_dataframe**](#swift2.classes.StateInitParameteriser.from_dataframe) – Create a parameteriser
- [**hide_parameters**](#swift2.classes.StateInitParameteriser.hide_parameters) – Hide some parameters (from the outside e.g. optimisers) in a filter parameteriser
- [**make_state_init_parameteriser**](#swift2.classes.StateInitParameteriser.make_state_init_parameteriser) – Create a parameteriser used for model state initialisation
- [**num_free_parameters**](#swift2.classes.StateInitParameteriser.num_free_parameters) – Number of free parameters in this hypercube parameteriser
- [**score_for_objective**](#swift2.classes.StateInitParameteriser.score_for_objective) – Computes the value of an objective for this given set of parameters
- [**set_hypercube**](#swift2.classes.StateInitParameteriser.set_hypercube) – Set the properties of a hypercube parameteriser
- [**set_max_parameter_value**](#swift2.classes.StateInitParameteriser.set_max_parameter_value) – Sets the value(s) of the upper bound of one or more parameter(s)
- [**set_min_parameter_value**](#swift2.classes.StateInitParameteriser.set_min_parameter_value) – Sets the value(s) of the lower bound of one or more parameter(s)
- [**set_parameter_definition**](#swift2.classes.StateInitParameteriser.set_parameter_definition) – Sets the feasible range and value for a parameter
- [**set_parameter_value**](#swift2.classes.StateInitParameteriser.set_parameter_value) – Sets the value(s) of one or more parameter(s)
- [**show_parameters**](#swift2.classes.StateInitParameteriser.show_parameters) – Show some parameters (from the outside e.g. optimisers) in a filter parameteriser
- [**subcatchment_parameteriser**](#swift2.classes.StateInitParameteriser.subcatchment_parameteriser) – Create a parameteriser that gets applied to a subset of a whole catchment
- [**supports_thread_safe_cloning**](#swift2.classes.StateInitParameteriser.supports_thread_safe_cloning) – Is this parameteriser clonable as a deep copy, safe for multi-threading?
- [**wrap_transform**](#swift2.classes.StateInitParameteriser.wrap_transform) – Create a parameteriser for which parameter transformations can be defined.

##### swift2.classes.StateInitParameteriser.add_parameter_to_hypercube

```python
add_parameter_to_hypercube(name, value, min, max)
```

Add a parameter to a hypercube. Must be a type of object that is expandable, otherwise may raise an exception

##### swift2.classes.StateInitParameteriser.add_to_hypercube

```python
add_to_hypercube(specs)
```

Add entries to a hypercube. Must be a type of object that is expandable, otherwise may raise an exception.

**Parameters:**

- **specs** (<code>[DataFrame](#pandas.DataFrame)</code>) – An optional data frame description of the parameter set, with at least columns Name, Min, Max, Value.

##### swift2.classes.StateInitParameteriser.apply_sys_config

```python
apply_sys_config(simulation)
```

Apply a model configuration to a simulation

**Parameters:**

- **simulation** (<code>[Simulation](#swift2.classes.Simulation)</code>) – simulation

##### swift2.classes.StateInitParameteriser.as_dataframe

```python
as_dataframe()
```

Convert this hypercube parameteriser to a pandas data frame representation

**Returns:**

- <code>[DataFrame](#pandas.DataFrame)</code> – pd.DataFrame: pandas data frame

##### swift2.classes.StateInitParameteriser.backtransform

```python
backtransform()
```

Get the parameteriser values in the untransformed space

Get the parameteriser values in the untransformed space, i.e. remove any
transform added via \[`HypercubeParameteriser.wrap_transform`\][HypercubeParameteriser.wrap_transform].
This allows to transform back e.g. from a virtual parameter log_X
to the underlying model (or even virtual/meta) parameter X.

**Returns:**

- **HypercubeParameteriser** (<code>[HypercubeParameteriser](#swift2.classes.HypercubeParameteriser)</code>) – The parameters definitions without the transforms (if there are any)

**Examples:**

```pycon
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

##### swift2.classes.StateInitParameteriser.clone

```python
clone()
```

##### swift2.classes.StateInitParameteriser.create_parameter_sampler

```python
create_parameter_sampler(seed=0, type='urs')
```

Creates a sampler for this parameteriser

**Parameters:**

- **seed** (<code>[int](#int)</code>) – a seed for the sampler. Defaults to 0.
- **type** (<code>[str](#str)</code>) – the type of sampler. Defaults to "urs". Only option supported as of 2023-01.

**Returns:**

- **CandidateFactorySeed** (<code>[CandidateFactorySeed](#swift2.classes.CandidateFactorySeed)</code>) – a sampler, aka candidate factory

##### swift2.classes.StateInitParameteriser.filtered_parameters

```python
filtered_parameters()
```

Wrap a parameteriser in a filter that can hide some parameters

##### swift2.classes.StateInitParameteriser.from_dataframe

```python
from_dataframe(type='Generic subareas', definition=None)
```

Create a parameteriser

**Parameters:**

- **type** (<code>[str](#str)</code>) – A string identifying the type of parameteriser to use. Recognised types are (case insensitive) 'log-likelihood', 'generic', 'subareas', 'links', 'nodes' and 'muskingum'. Defaults to "Generic subareas".
- **specs** (<code>[DataFrame](#pandas.DataFrame)</code>) – An optional data frame description of the parameter set, with at least columns Name, Min, Max, Value. Defaults to None.

**Returns:**

- **HypercubeParameteriser** (<code>[HypercubeParameteriser](#swift2.classes.HypercubeParameteriser)</code>) – new parameteriser

**Examples:**

```pycon
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

##### swift2.classes.StateInitParameteriser.hide_parameters

```python
hide_parameters(patterns, regex=False, starts_with=False, strict=False)
```

Hide some parameters (from the outside e.g. optimisers) in a filter parameteriser

**Parameters:**

- **patterns** (<code>\[[type](#type)\]</code>) – character, one or more pattern to match and hide matching parameters. Match according to other parameters.
- **regex** (<code>[bool](#bool)</code>) – logical, defaults False, should the patterns be used as regular expressions.. Defaults to False.
- **starts_with** (<code>[bool](#bool)</code>) – logical, defaults False. Ignored if regex is True. Should the patterns be used as starting strings in the parameter names.. Defaults to False.
- **strict** (<code>[bool](#bool)</code>) – logical, default False. Used only if regex and starts_with are False. If True, raises an error if one of the "patterns" has no exact match in the parameters.. Defaults to False.

##### swift2.classes.StateInitParameteriser.make_state_init_parameteriser

```python
make_state_init_parameteriser()
```

Create a parameteriser used for model state initialisation

This allows to define tied parameters where, for instance, pval = a * modelStateVal.
A more concrete use case is to define an initial soil moisture store 'S0',
as a fraction of the model store capacity 'Smax'.
The model state to initialise is 'S'

<details class="note" open>
<summary>Note</summary>
See also [swift2.classes.ScalingParameteriser][] for typical joint usage.
</details>

**Returns:**

- **StateInitParameteriser** (<code>[StateInitParameteriser](#swift2.classes.StateInitParameteriser)</code>) – state initialisation parameteriser

**Examples:**

```pycon
>>> todo()
```

##### swift2.classes.StateInitParameteriser.num_free_parameters

```python
num_free_parameters()
```

Number of free parameters in this hypercube parameteriser

**Returns:**

- **int** (<code>[int](#int)</code>) – Number of free parameters

##### swift2.classes.StateInitParameteriser.score_for_objective

```python
score_for_objective(objective)
```

Computes the value of an objective for this given set of parameters

##### swift2.classes.StateInitParameteriser.set_hypercube

```python
set_hypercube(specs)
```

Set the properties of a hypercube parameteriser

**Parameters:**

- **specs** (<code>[DataFrame](#pandas.DataFrame)</code>) – An optional data frame description of the parameter set, with at least columns Name, Min, Max, Value.

##### swift2.classes.StateInitParameteriser.set_max_parameter_value

```python
set_max_parameter_value(variable_name, value)
```

Sets the value(s) of the upper bound of one or more parameter(s)

**Parameters:**

- **variable_name** (<code>[VecStr](#swift2.const.VecStr)</code>) – one or more parameter name(s)
- **value** (<code>[VecScalars](#swift2.const.VecScalars)</code>) – one or more parameter value(s)

##### swift2.classes.StateInitParameteriser.set_min_parameter_value

```python
set_min_parameter_value(variable_name, value)
```

Sets the value(s) of the lower bound of one or more parameter(s)

**Parameters:**

- **variable_name** (<code>[VecStr](#swift2.const.VecStr)</code>) – one or more parameter name(s)
- **value** (<code>[VecScalars](#swift2.const.VecScalars)</code>) – one or more parameter value(s)

##### swift2.classes.StateInitParameteriser.set_parameter_definition

```python
set_parameter_definition(variable_name, min, max, value)
```

Sets the feasible range and value for a parameter

**Parameters:**

- **variable_name** (<code>[str](#str)</code>) – parameter name
- **min** (<code>[float](#float)</code>) – min
- **max** (<code>[float](#float)</code>) – max
- **value** (<code>[float](#float)</code>) – value

##### swift2.classes.StateInitParameteriser.set_parameter_value

```python
set_parameter_value(variable_name, value)
```

Sets the value(s) of one or more parameter(s)

**Parameters:**

- **variable_name** (<code>[VecStr](#swift2.const.VecStr)</code>) – one or more parameter name(s)
- **value** (<code>[VecScalars](#swift2.const.VecScalars)</code>) – one or more parameter value(s)

##### swift2.classes.StateInitParameteriser.show_parameters

```python
show_parameters(patterns, regex=False, starts_with=False)
```

Show some parameters (from the outside e.g. optimisers) in a filter parameteriser

**Parameters:**

- **patterns** (<code>\[[type](#type)\]</code>) – character, one or more pattern to match and show matching parameters. Match according to other parameters
- **regex** (<code>[bool](#bool)</code>) – should the patterns be used as regular expressions. Defaults to False.
- **starts_with** (<code>[bool](#bool)</code>) – should the patterns be used as starting strings in the parameter names. Defaults to False.

##### swift2.classes.StateInitParameteriser.subcatchment_parameteriser

```python
subcatchment_parameteriser(subcatchment)
```

Create a parameteriser that gets applied to a subset of a whole catchment

**Parameters:**

- **subcatchment** (<code>[Simulation](#swift2.classes.Simulation)</code>) – the subcatchment, subset of a whole catchment, identifying which elements (subareas, nodes, links) will be parameterised by the new parameteriser. Other catchment elements are untouched.

**Returns:**

- **HypercubeParameteriser** – New parameteriser whose application is limited to the subcatchment.

**Examples:**

```pycon
>>> sub_cats = simulation.split_to_subcatchments(["node.node_7", "node.node_10"])
>>> sc = sub_cats["node.node_7"]
>>> p = sp.create_parameteriser('generic subarea')
>>> p.add_parameter_to_hypercube("x1", 32, 1, 6e3)
>>> sp = p.subcatchment_parameteriser(sc)
>>> sp.apply_sys_config(simulation)
```

##### swift2.classes.StateInitParameteriser.supports_thread_safe_cloning

```python
supports_thread_safe_cloning()
```

Is this parameteriser clonable as a deep copy, safe for multi-threading?

##### swift2.classes.StateInitParameteriser.wrap_transform

```python
wrap_transform()
```

Create a parameteriser for which parameter transformations can be defined.

This allows to define e.g. a virtual parameter log_X instead of calibrating on the parameter X.

**Returns:**

- **TransformParameteriser** (<code>[TransformParameteriser](#swift2.classes.TransformParameteriser)</code>) – A new parameteriser (TransformParameteriser) which has methods to define parameter transforms

#### swift2.classes.StateInitialiser

```python
StateInitialiser(handle, release_native, type_id=None, prior_ref_count=0)
```

Bases: <code>[DeletableCffiNativeHandle](#refcount.interop.DeletableCffiNativeHandle)</code>

**Functions:**

- [**clone**](#swift2.classes.StateInitialiser.clone) –
- [**is_dictionary_like**](#swift2.classes.StateInitialiser.is_dictionary_like) –

##### swift2.classes.StateInitialiser.clone

```python
clone()
```

##### swift2.classes.StateInitialiser.is_dictionary_like

```python
is_dictionary_like()
```

#### swift2.classes.TransformParameteriser

```python
TransformParameteriser(handle, release_native, type_id=None, prior_ref_count=0)
```

Bases: <code>[HypercubeParameteriser](#swift2.classes.HypercubeParameteriser)</code>

**Functions:**

- [**add_parameter_to_hypercube**](#swift2.classes.TransformParameteriser.add_parameter_to_hypercube) – Add a parameter to a hypercube. Must be a type of object that is expandable, otherwise may raise an exception
- [**add_to_hypercube**](#swift2.classes.TransformParameteriser.add_to_hypercube) – Add entries to a hypercube. Must be a type of object that is expandable, otherwise may raise an exception.
- [**add_transform**](#swift2.classes.TransformParameteriser.add_transform) – Create a parameteriser for which parameter transformations can be defined
- [**apply_sys_config**](#swift2.classes.TransformParameteriser.apply_sys_config) – Apply a model configuration to a simulation
- [**as_dataframe**](#swift2.classes.TransformParameteriser.as_dataframe) – Convert this hypercube parameteriser to a pandas data frame representation
- [**backtransform**](#swift2.classes.TransformParameteriser.backtransform) – Get the parameteriser values in the untransformed space
- [**clone**](#swift2.classes.TransformParameteriser.clone) –
- [**create_parameter_sampler**](#swift2.classes.TransformParameteriser.create_parameter_sampler) – Creates a sampler for this parameteriser
- [**filtered_parameters**](#swift2.classes.TransformParameteriser.filtered_parameters) – Wrap a parameteriser in a filter that can hide some parameters
- [**from_dataframe**](#swift2.classes.TransformParameteriser.from_dataframe) – Create a parameteriser
- [**hide_parameters**](#swift2.classes.TransformParameteriser.hide_parameters) – Hide some parameters (from the outside e.g. optimisers) in a filter parameteriser
- [**make_state_init_parameteriser**](#swift2.classes.TransformParameteriser.make_state_init_parameteriser) – Create a parameteriser used for model state initialisation
- [**num_free_parameters**](#swift2.classes.TransformParameteriser.num_free_parameters) – Number of free parameters in this hypercube parameteriser
- [**score_for_objective**](#swift2.classes.TransformParameteriser.score_for_objective) – Computes the value of an objective for this given set of parameters
- [**set_hypercube**](#swift2.classes.TransformParameteriser.set_hypercube) – Set the properties of a hypercube parameteriser
- [**set_max_parameter_value**](#swift2.classes.TransformParameteriser.set_max_parameter_value) – Sets the value(s) of the upper bound of one or more parameter(s)
- [**set_min_parameter_value**](#swift2.classes.TransformParameteriser.set_min_parameter_value) – Sets the value(s) of the lower bound of one or more parameter(s)
- [**set_parameter_definition**](#swift2.classes.TransformParameteriser.set_parameter_definition) – Sets the feasible range and value for a parameter
- [**set_parameter_value**](#swift2.classes.TransformParameteriser.set_parameter_value) – Sets the value(s) of one or more parameter(s)
- [**show_parameters**](#swift2.classes.TransformParameteriser.show_parameters) – Show some parameters (from the outside e.g. optimisers) in a filter parameteriser
- [**subcatchment_parameteriser**](#swift2.classes.TransformParameteriser.subcatchment_parameteriser) – Create a parameteriser that gets applied to a subset of a whole catchment
- [**supports_thread_safe_cloning**](#swift2.classes.TransformParameteriser.supports_thread_safe_cloning) – Is this parameteriser clonable as a deep copy, safe for multi-threading?
- [**wrap_transform**](#swift2.classes.TransformParameteriser.wrap_transform) – Create a parameteriser for which parameter transformations can be defined.

##### swift2.classes.TransformParameteriser.add_parameter_to_hypercube

```python
add_parameter_to_hypercube(name, value, min, max)
```

Add a parameter to a hypercube. Must be a type of object that is expandable, otherwise may raise an exception

##### swift2.classes.TransformParameteriser.add_to_hypercube

```python
add_to_hypercube(specs)
```

Add entries to a hypercube. Must be a type of object that is expandable, otherwise may raise an exception.

**Parameters:**

- **specs** (<code>[DataFrame](#pandas.DataFrame)</code>) – An optional data frame description of the parameter set, with at least columns Name, Min, Max, Value.

##### swift2.classes.TransformParameteriser.add_transform

```python
add_transform(param_name, inner_param_name, transform_id, a=1.0, b=0.0)
```

Create a parameteriser for which parameter transformations can be defined

```
This allows to define e.g. a virtual parameter log_X instead of calibrating on the parameter X.
```

**Parameters:**

- **param_name** (<code>[str](#str)</code>) – the name of the meta-parameter. Note that it can be the same value as inner_param_name, but this is NOT recommended.
- **inner_param_name** (<code>[str](#str)</code>) – the name of the parameter being transformed
- **transform_id** (<code>[str](#str)</code>) – identifier for a known bijective univariate function
- **a** (<code>[float](#float)</code>) – parameter in Y = F(ax+b). Defaults to 1.0.
- **b** (<code>[float](#float)</code>) – parameter in Y = F(ax+b). Defaults to 0.0.

##### swift2.classes.TransformParameteriser.apply_sys_config

```python
apply_sys_config(simulation)
```

Apply a model configuration to a simulation

**Parameters:**

- **simulation** (<code>[Simulation](#swift2.classes.Simulation)</code>) – simulation

##### swift2.classes.TransformParameteriser.as_dataframe

```python
as_dataframe()
```

Convert this hypercube parameteriser to a pandas data frame representation

**Returns:**

- <code>[DataFrame](#pandas.DataFrame)</code> – pd.DataFrame: pandas data frame

##### swift2.classes.TransformParameteriser.backtransform

```python
backtransform()
```

Get the parameteriser values in the untransformed space

Get the parameteriser values in the untransformed space, i.e. remove any
transform added via \[`HypercubeParameteriser.wrap_transform`\][HypercubeParameteriser.wrap_transform].
This allows to transform back e.g. from a virtual parameter log_X
to the underlying model (or even virtual/meta) parameter X.

**Returns:**

- **HypercubeParameteriser** (<code>[HypercubeParameteriser](#swift2.classes.HypercubeParameteriser)</code>) – The parameters definitions without the transforms (if there are any)

**Examples:**

```pycon
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

##### swift2.classes.TransformParameteriser.clone

```python
clone()
```

##### swift2.classes.TransformParameteriser.create_parameter_sampler

```python
create_parameter_sampler(seed=0, type='urs')
```

Creates a sampler for this parameteriser

**Parameters:**

- **seed** (<code>[int](#int)</code>) – a seed for the sampler. Defaults to 0.
- **type** (<code>[str](#str)</code>) – the type of sampler. Defaults to "urs". Only option supported as of 2023-01.

**Returns:**

- **CandidateFactorySeed** (<code>[CandidateFactorySeed](#swift2.classes.CandidateFactorySeed)</code>) – a sampler, aka candidate factory

##### swift2.classes.TransformParameteriser.filtered_parameters

```python
filtered_parameters()
```

Wrap a parameteriser in a filter that can hide some parameters

##### swift2.classes.TransformParameteriser.from_dataframe

```python
from_dataframe(type='Generic subareas', definition=None)
```

Create a parameteriser

**Parameters:**

- **type** (<code>[str](#str)</code>) – A string identifying the type of parameteriser to use. Recognised types are (case insensitive) 'log-likelihood', 'generic', 'subareas', 'links', 'nodes' and 'muskingum'. Defaults to "Generic subareas".
- **specs** (<code>[DataFrame](#pandas.DataFrame)</code>) – An optional data frame description of the parameter set, with at least columns Name, Min, Max, Value. Defaults to None.

**Returns:**

- **HypercubeParameteriser** (<code>[HypercubeParameteriser](#swift2.classes.HypercubeParameteriser)</code>) – new parameteriser

**Examples:**

```pycon
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

##### swift2.classes.TransformParameteriser.hide_parameters

```python
hide_parameters(patterns, regex=False, starts_with=False, strict=False)
```

Hide some parameters (from the outside e.g. optimisers) in a filter parameteriser

**Parameters:**

- **patterns** (<code>\[[type](#type)\]</code>) – character, one or more pattern to match and hide matching parameters. Match according to other parameters.
- **regex** (<code>[bool](#bool)</code>) – logical, defaults False, should the patterns be used as regular expressions.. Defaults to False.
- **starts_with** (<code>[bool](#bool)</code>) – logical, defaults False. Ignored if regex is True. Should the patterns be used as starting strings in the parameter names.. Defaults to False.
- **strict** (<code>[bool](#bool)</code>) – logical, default False. Used only if regex and starts_with are False. If True, raises an error if one of the "patterns" has no exact match in the parameters.. Defaults to False.

##### swift2.classes.TransformParameteriser.make_state_init_parameteriser

```python
make_state_init_parameteriser()
```

Create a parameteriser used for model state initialisation

This allows to define tied parameters where, for instance, pval = a * modelStateVal.
A more concrete use case is to define an initial soil moisture store 'S0',
as a fraction of the model store capacity 'Smax'.
The model state to initialise is 'S'

<details class="note" open>
<summary>Note</summary>
See also [swift2.classes.ScalingParameteriser][] for typical joint usage.
</details>

**Returns:**

- **StateInitParameteriser** (<code>[StateInitParameteriser](#swift2.classes.StateInitParameteriser)</code>) – state initialisation parameteriser

**Examples:**

```pycon
>>> todo()
```

##### swift2.classes.TransformParameteriser.num_free_parameters

```python
num_free_parameters()
```

Number of free parameters in this hypercube parameteriser

**Returns:**

- **int** (<code>[int](#int)</code>) – Number of free parameters

##### swift2.classes.TransformParameteriser.score_for_objective

```python
score_for_objective(objective)
```

Computes the value of an objective for this given set of parameters

##### swift2.classes.TransformParameteriser.set_hypercube

```python
set_hypercube(specs)
```

Set the properties of a hypercube parameteriser

**Parameters:**

- **specs** (<code>[DataFrame](#pandas.DataFrame)</code>) – An optional data frame description of the parameter set, with at least columns Name, Min, Max, Value.

##### swift2.classes.TransformParameteriser.set_max_parameter_value

```python
set_max_parameter_value(variable_name, value)
```

Sets the value(s) of the upper bound of one or more parameter(s)

**Parameters:**

- **variable_name** (<code>[VecStr](#swift2.const.VecStr)</code>) – one or more parameter name(s)
- **value** (<code>[VecScalars](#swift2.const.VecScalars)</code>) – one or more parameter value(s)

##### swift2.classes.TransformParameteriser.set_min_parameter_value

```python
set_min_parameter_value(variable_name, value)
```

Sets the value(s) of the lower bound of one or more parameter(s)

**Parameters:**

- **variable_name** (<code>[VecStr](#swift2.const.VecStr)</code>) – one or more parameter name(s)
- **value** (<code>[VecScalars](#swift2.const.VecScalars)</code>) – one or more parameter value(s)

##### swift2.classes.TransformParameteriser.set_parameter_definition

```python
set_parameter_definition(variable_name, min, max, value)
```

Sets the feasible range and value for a parameter

**Parameters:**

- **variable_name** (<code>[str](#str)</code>) – parameter name
- **min** (<code>[float](#float)</code>) – min
- **max** (<code>[float](#float)</code>) – max
- **value** (<code>[float](#float)</code>) – value

##### swift2.classes.TransformParameteriser.set_parameter_value

```python
set_parameter_value(variable_name, value)
```

Sets the value(s) of one or more parameter(s)

**Parameters:**

- **variable_name** (<code>[VecStr](#swift2.const.VecStr)</code>) – one or more parameter name(s)
- **value** (<code>[VecScalars](#swift2.const.VecScalars)</code>) – one or more parameter value(s)

##### swift2.classes.TransformParameteriser.show_parameters

```python
show_parameters(patterns, regex=False, starts_with=False)
```

Show some parameters (from the outside e.g. optimisers) in a filter parameteriser

**Parameters:**

- **patterns** (<code>\[[type](#type)\]</code>) – character, one or more pattern to match and show matching parameters. Match according to other parameters
- **regex** (<code>[bool](#bool)</code>) – should the patterns be used as regular expressions. Defaults to False.
- **starts_with** (<code>[bool](#bool)</code>) – should the patterns be used as starting strings in the parameter names. Defaults to False.

##### swift2.classes.TransformParameteriser.subcatchment_parameteriser

```python
subcatchment_parameteriser(subcatchment)
```

Create a parameteriser that gets applied to a subset of a whole catchment

**Parameters:**

- **subcatchment** (<code>[Simulation](#swift2.classes.Simulation)</code>) – the subcatchment, subset of a whole catchment, identifying which elements (subareas, nodes, links) will be parameterised by the new parameteriser. Other catchment elements are untouched.

**Returns:**

- **HypercubeParameteriser** – New parameteriser whose application is limited to the subcatchment.

**Examples:**

```pycon
>>> sub_cats = simulation.split_to_subcatchments(["node.node_7", "node.node_10"])
>>> sc = sub_cats["node.node_7"]
>>> p = sp.create_parameteriser('generic subarea')
>>> p.add_parameter_to_hypercube("x1", 32, 1, 6e3)
>>> sp = p.subcatchment_parameteriser(sc)
>>> sp.apply_sys_config(simulation)
```

##### swift2.classes.TransformParameteriser.supports_thread_safe_cloning

```python
supports_thread_safe_cloning()
```

Is this parameteriser clonable as a deep copy, safe for multi-threading?

##### swift2.classes.TransformParameteriser.wrap_transform

```python
wrap_transform()
```

Create a parameteriser for which parameter transformations can be defined.

This allows to define e.g. a virtual parameter log_X instead of calibrating on the parameter X.

**Returns:**

- **TransformParameteriser** (<code>[TransformParameteriser](#swift2.classes.TransformParameteriser)</code>) – A new parameteriser (TransformParameteriser) which has methods to define parameter transforms

#### swift2.classes.VectorObjectiveScores

```python
VectorObjectiveScores(handle, release_native, type_id=None, prior_ref_count=0)
```

Bases: <code>[DeletableCffiNativeHandle](#refcount.interop.DeletableCffiNativeHandle)</code>

**Functions:**

- [**as_dataframe**](#swift2.classes.VectorObjectiveScores.as_dataframe) –
- [**get_best_score**](#swift2.classes.VectorObjectiveScores.get_best_score) –
- [**get_parameters_at_index**](#swift2.classes.VectorObjectiveScores.get_parameters_at_index) –
- [**get_score_at_index**](#swift2.classes.VectorObjectiveScores.get_score_at_index) –
- [**sort_by_score**](#swift2.classes.VectorObjectiveScores.sort_by_score) –

**Attributes:**

- [**size**](#swift2.classes.VectorObjectiveScores.size) (<code>[int](#int)</code>) –

##### swift2.classes.VectorObjectiveScores.as_dataframe

```python
as_dataframe()
```

##### swift2.classes.VectorObjectiveScores.get_best_score

```python
get_best_score(score_name='NSE', convert_to_py=False)
```

##### swift2.classes.VectorObjectiveScores.get_parameters_at_index

```python
get_parameters_at_index(index)
```

##### swift2.classes.VectorObjectiveScores.get_score_at_index

```python
get_score_at_index(index)
```

##### swift2.classes.VectorObjectiveScores.size

```python
size: int
```

##### swift2.classes.VectorObjectiveScores.sort_by_score

```python
sort_by_score(score_name='NSE')
```

#### swift2.classes.wrap_cffi_native_handle

```python
wrap_cffi_native_handle(obj, type_id, release_native)
```

### swift2.common

### swift2.const

**Attributes:**

- [**CATCHMENT_FLOWRATE_VARID**](#swift2.const.CATCHMENT_FLOWRATE_VARID) –
- [**NdSimulation**](#swift2.const.NdSimulation) (<code>[TypeAlias](#typing_extensions.TypeAlias)</code>) –
- [**RecordToSignature**](#swift2.const.RecordToSignature) (<code>[TypeAlias](#typing_extensions.TypeAlias)</code>) –

#### swift2.const.CATCHMENT_FLOWRATE_VARID

```python
CATCHMENT_FLOWRATE_VARID = 'Catchment.StreamflowRate'
```

#### swift2.const.NdSimulation

```python
NdSimulation: TypeAlias = Union[Simulation, EnsembleSimulation, EnsembleForecastSimulation]
```

#### swift2.const.RecordToSignature

```python
RecordToSignature: TypeAlias = Callable[[Any, VecStr, TimeSeriesLibrary, VecStr, int], None]
```

### swift2.doc_helper

**Modules:**

- [**swc**](#swift2.doc_helper.swc) –
- [**swg**](#swift2.doc_helper.swg) –

**Functions:**

- [**add_loglikelihood_params**](#swift2.doc_helper.add_loglikelihood_params) –
- [**add_mln_and_loglik**](#swift2.doc_helper.add_mln_and_loglik) –
- [**check_simulation**](#swift2.doc_helper.check_simulation) – Checks whether a simulation is configured to a state where it is executable
- [**configure_hourly_gr4j**](#swift2.doc_helper.configure_hourly_gr4j) – Configure a simulation with GR4J models for hourly time step modelling
- [**configure_test_simulation**](#swift2.doc_helper.configure_test_simulation) –
- [**create_catchment**](#swift2.doc_helper.create_catchment) – Create a SWIFT catchment with a specified hydrologic model
- [**create_catchment_model_from_structure**](#swift2.doc_helper.create_catchment_model_from_structure) –
- [**create_ensemble_forecast_simulation**](#swift2.doc_helper.create_ensemble_forecast_simulation) – Create an ensemble forecast simulation
- [**create_gr4jh_parameters**](#swift2.doc_helper.create_gr4jh_parameters) – Get a parameter set that configures GR4J for hourly operations
- [**create_subarea**](#swift2.doc_helper.create_subarea) – Create a SWIFT subarea with a specified hydrologic model
- [**create_subarea_simulation**](#swift2.doc_helper.create_subarea_simulation) – Creates a one sub-catchment simulation
- [**create_test_catchment_structure**](#swift2.doc_helper.create_test_catchment_structure) –
- [**default_pspec_nlm**](#swift2.doc_helper.default_pspec_nlm) –
- [**define_gr4j_scaled_parameter**](#swift2.doc_helper.define_gr4j_scaled_parameter) – define a scaled and transformed parameterizer for GR4J
- [**define_parameteriser_gr4j_muskingum**](#swift2.doc_helper.define_parameteriser_gr4j_muskingum) –
- [**describe**](#swift2.doc_helper.describe) –
- [**deserialise_sample_series**](#swift2.doc_helper.deserialise_sample_series) –
- [**exec_simulation**](#swift2.doc_helper.exec_simulation) – Execute a simulation
- [**get_catchment_dot_graph**](#swift2.doc_helper.get_catchment_dot_graph) – Gets a catchment representation in Graphviz DOT format
- [**get_free_params**](#swift2.doc_helper.get_free_params) – Get a default parameter set for models
- [**get_link_ids**](#swift2.doc_helper.get_link_ids) – Gets all the identifiers of the links in the catchment
- [**get_link_names**](#swift2.doc_helper.get_link_names) – Gets all the names of the links in the catchment
- [**get_node_ids**](#swift2.doc_helper.get_node_ids) – Gets all the identifiers of the nodes in the catchment
- [**get_node_names**](#swift2.doc_helper.get_node_names) – Gets all the names of the nodes in the catchment
- [**get_state_value**](#swift2.doc_helper.get_state_value) – Gets the value(s) of a model state(s)
- [**get_subarea_ids**](#swift2.doc_helper.get_subarea_ids) – Gets all the identifiers of the sub-areas in the catchment
- [**get_subarea_names**](#swift2.doc_helper.get_subarea_names) – Gets all the names of the sub-areas in the catchment
- [**get_variable_ids**](#swift2.doc_helper.get_variable_ids) – Gets all the names of the variables of an element within a catchment
- [**gr4j_scaled_parameteriser**](#swift2.doc_helper.gr4j_scaled_parameteriser) – Get a time step and area scaled parameterizer for the GR4 model structure
- [**inspect**](#swift2.doc_helper.inspect) – Inspect an element of a catchment model
- [**is_common_iterable**](#swift2.doc_helper.is_common_iterable) – True if an object is iterable but not a string (str)
- [**is_variable_id**](#swift2.doc_helper.is_variable_id) – Is a variable identifier valid for a simulation
- [**lag_and_route_parameteriser**](#swift2.doc_helper.lag_and_route_parameteriser) –
- [**paste0**](#swift2.doc_helper.paste0) – Port of R paste0 function
- [**play_subarea_input**](#swift2.doc_helper.play_subarea_input) – Sets time series as input to a simulation
- [**rep**](#swift2.doc_helper.rep) –
- [**reset_model_states**](#swift2.doc_helper.reset_model_states) – Reset the model states of a simulation, and apply one or more state initialers if the simulation is configured with any.
- [**sample_catchment_model**](#swift2.doc_helper.sample_catchment_model) – Deserialize a basic catchment structure from the package sample data
- [**sample_series**](#swift2.doc_helper.sample_series) – Deserialize information to a UTC time series
- [**sce_parameter**](#swift2.doc_helper.sce_parameter) – Create SCE parameters suited for a given number of parameters.
- [**set_error_correction_model**](#swift2.doc_helper.set_error_correction_model) – Add an error correction model to an element in a catchment
- [**set_loglik_param_keys**](#swift2.doc_helper.set_loglik_param_keys) – Specify the global parameter names to use in the log-likelihood calculation
- [**set_muskingum_routing_to_linear**](#swift2.doc_helper.set_muskingum_routing_to_linear) –
- [**set_sample_data**](#swift2.doc_helper.set_sample_data) – Sets sample input data into a model simulation
- [**set_simulation_span**](#swift2.doc_helper.set_simulation_span) – Sets simulation span
- [**set_simulation_time_step**](#swift2.doc_helper.set_simulation_time_step) – Sets the time step of a SWIFT simulation
- [**set_state_value**](#swift2.doc_helper.set_state_value) – Sets the value of a model state
- [**set_states**](#swift2.doc_helper.set_states) – Apply memory states to a simulation
- [**short_var_id**](#swift2.doc_helper.short_var_id) – Shorten long model variable identifiers to the short model variable name
- [**snapshot_state**](#swift2.doc_helper.snapshot_state) – Take a snapshot of the memory states of a simulation
- [**sort_by_execution_order**](#swift2.doc_helper.sort_by_execution_order) – Sort the specified element ids according to the execution order of the simulation
- [**swap_model**](#swift2.doc_helper.swap_model) – Clone and change a simulation, using another runoff model
- [**testdata_dir**](#swift2.doc_helper.testdata_dir) –

#### swift2.doc_helper.add_loglikelihood_params

```python
add_loglikelihood_params(parameteriser)
```

#### swift2.doc_helper.add_mln_and_loglik

```python
add_mln_and_loglik(parameteriser, simulation, p_spec_nlm, delta_t, param_name_k='Alpha', objfun=None)
```

#### swift2.doc_helper.check_simulation

```python
check_simulation(simulation)
```

Checks whether a simulation is configured to a state where it is executable

Checks whether a simulation is configured to a state where it is executable

**Parameters:**

- **simulation** (<code>[Simulation](#swift2.classes.Simulation)</code>) – A swift simulation object

#### swift2.doc_helper.configure_hourly_gr4j

```python
configure_hourly_gr4j(simulation)
```

Configure a simulation with GR4J models for hourly time step modelling

Configure a simulation with GR4J models for hourly time step modelling

**Parameters:**

- **simulation** (<code>[Simulation](#Simulation)</code>) – A swift simulation object

#### swift2.doc_helper.configure_test_simulation

```python
configure_test_simulation(simulation, data_id='MMH', simul_start='1990-01-01', simul_end='2005-12-31', tstep='daily', varname_rain='P', varname_pet='E', varname_data_rain='P', varname_data_pet='E')
```

#### swift2.doc_helper.create_catchment

```python
create_catchment(node_ids, node_names, link_ids, link_names, link_from_node, link_to_node, runoff_model_name='GR4J', areas_km2=None)
```

Create a SWIFT catchment with a specified hydrologic model

Create a SWIFT catchment with a specified hydrologic model.
This function is intended mostly for testing, not for usual modelling code.

**Parameters:**

- **node_ids** (<code>[Any](#typing.Any)</code>) – character, node unique identifiers
- **node_names** (<code>[Any](#typing.Any)</code>) – character, node display names
- **link_ids** (<code>[Any](#typing.Any)</code>) – character, links unique identifiers
- **link_names** (<code>[Any](#typing.Any)</code>) – character, links display names
- **link_from_node** (<code>[Any](#typing.Any)</code>) – character, identifier of the links' upstream node
- **link_to_node** (<code>[Any](#typing.Any)</code>) – character, identifier of the links' downstream node
- **runoff_model_name** (<code>[Any](#typing.Any)</code>) – A valid, known SWIFT model name (e.g. 'GR5H')
- **areas_km2** (<code>[Any](#typing.Any)</code>) – The areas in square kilometres

**Returns:**

- – A SWIFT simulation object (i.e. a model runner)

**Examples:**

TODO

#### swift2.doc_helper.create_catchment_model_from_structure

```python
create_catchment_model_from_structure(cat_structure)
```

#### swift2.doc_helper.create_ensemble_forecast_simulation

```python
create_ensemble_forecast_simulation(simulation, data_library, start, end, input_map, lead_time, ensemble_size, n_time_steps_between_forecasts)
```

Create an ensemble forecast simulation

Create an ensemble forecast simulation

**Parameters:**

- **simulation** (<code>[Simulation](#swift2.classes.Simulation)</code>) – A swift simulation object
- **data_library** (<code>[Any](#typing.Any)</code>) – external pointer type ENSEMBLE_DATA_SET_PTR, or a Python class wrapper around it
- **start** (<code>[Any](#typing.Any)</code>) – the start date of the simulation. The time zone will be forced to UTC.
- **end** (<code>[Any](#typing.Any)</code>) – the end date of the simulation. The time zone will be forced to UTC.
- **input_map** (<code>[Any](#typing.Any)</code>) – a named list were names are the data library data identifiers, and values are character vectors with model state identifiers.
- **lead_time** (<code>[Any](#typing.Any)</code>) – integer, the length in time steps of the forecasts.
- **ensemble_size** (<code>[Any](#typing.Any)</code>) – ensemble size
- **n_time_steps_between_forecasts** (<code>[Any](#typing.Any)</code>) – nTimeStepsBetweenForecasts

**Returns:**

- – An external pointer

#### swift2.doc_helper.create_gr4jh_parameters

```python
create_gr4jh_parameters()
```

Get a parameter set that configures GR4J for hourly operations

Get a parameter set that configures GR4J for hourly operations

**Returns:**

- **HyperCubeParameteriser** – a parameter set that can be applied to SWIFT systems with GR4J

#### swift2.doc_helper.create_subarea

```python
create_subarea(model_name, area_km2)
```

Create a SWIFT subarea with a specified hydrologic model

Create a SWIFT subarea with a specified hydrologic model

**Parameters:**

- **model_name** (<code>[Any](#typing.Any)</code>) – A valid, known SWIFT model name (e.g. 'GR5H')
- **area_km2** (<code>[Any](#typing.Any)</code>) – The area in square kilometres

**Returns:**

- – A SWIFT simulation object (i.e. a model runner)

#### swift2.doc_helper.create_subarea_simulation

```python
create_subarea_simulation(data_id='MMH', simul_start='1990-01-01', simul_end='2005-12-31', model_id='GR4J', tstep='daily', varname_rain='P', varname_pet='E')
```

Creates a one sub-catchment simulation

Creates a one sub-catchment simulation. This function is intended for creating sample simulations, not for use in production.

**Parameters:**

- **dataId** (<code>[Any](#typing.Any)</code>) – data identifier in swift_sample_data
- **simulStart** (<code>[Any](#typing.Any)</code>) – ISO string for the simulation start date time
- **simulEnd** (<code>[Any](#typing.Any)</code>) – ISO string for the simulation end date time
- **modelId** (<code>[Any](#typing.Any)</code>) – model identifier
- **tstep** (<code>[Any](#typing.Any)</code>) – character, 'daily' or 'hourly'
- **varNameRain** (<code>[Any](#typing.Any)</code>) – variable name to assign rainfall to
- **varNamePet** (<code>[Any](#typing.Any)</code>) – variable name to assign PET to

**Returns:**

- – A SWIFT simulation object, clone of the simulation but with a new model type in use.

#### swift2.doc_helper.create_test_catchment_structure

```python
create_test_catchment_structure(node_ids=None, link_ids=None, from_node=None, to_node=None, areas_km2=None, runoff_model='GR4J')
```

#### swift2.doc_helper.default_pspec_nlm

```python
default_pspec_nlm()
```

#### swift2.doc_helper.define_gr4j_scaled_parameter

```python
define_gr4j_scaled_parameter(ref_area=250, time_span=3600, pspec_gr4j=None)
```

define a scaled and transformed parameterizer for GR4J

define a scaled and transformed parameterizer for GR4J

**Parameters:**

- **ref_area** (<code>[float](#float)</code>) – the reference area in square kilometres
- **time_span** (<code>[int](#int)</code>) – the time span of the simulation intented for this model, in seconds
- **pspec_gr4j** (<code>[DataFrame](#pandas.DataFrame)</code>) – optional - data frame specifying the feasible parameter space for parameters x1 to x2 of GR4J

**Returns:**

- **TransformParameteriser** – a parameterizer for GR4J, combining time and area scaling and superimposed with log10 transforms for x1, x3, x4 and arc-sinh for x2

#### swift2.doc_helper.define_parameteriser_gr4j_muskingum

```python
define_parameteriser_gr4j_muskingum(ref_area=250, time_span=3600, p_spec_nlm=None, simulation=None, objfun=None, delta_t=1, param_name_k='K')
```

#### swift2.doc_helper.describe

```python
describe(simulation, verbosity=None)
```

#### swift2.doc_helper.deserialise_sample_series

```python
deserialise_sample_series(serialised)
```

#### swift2.doc_helper.exec_simulation

```python
exec_simulation(simulation, reset_initial_states=True)
```

Execute a simulation

Execute a simulation

**Parameters:**

- **simulation** (<code>[Simulation](#swift2.classes.Simulation)</code>) – A swift simulation object
- **reset_initial_states** (<code>[Any](#typing.Any)</code>) – logical, should the states of the model be reinitialized before the first time step.

#### swift2.doc_helper.get_catchment_dot_graph

```python
get_catchment_dot_graph(simulation)
```

Gets a catchment representation in Graphviz DOT format

Gets a catchment representation in Graphviz DOT format

**Parameters:**

- **simulation** (<code>[Simulation](#Simulation)</code>) – A swift simulation object

**Returns:**

- – a string in a notation usable by the DiagrammeR package.

**Examples:**

TODO

#### swift2.doc_helper.get_free_params

```python
get_free_params(model_id)
```

Get a default parameter set for models

Get a default parameter set for models, as a data frame

**Parameters:**

- **model_id** (<code>[Any](#swift2.simulation.Any)</code>) – an identifier for the model, e.g. 'GR5H'

**Returns:**

- – a data frame with Min, Max, Value, Name

#### swift2.doc_helper.get_link_ids

```python
get_link_ids(simulation)
```

Gets all the identifiers of the links in the catchment

Gets all the identifiers of the links in the catchment

**Parameters:**

- **simulation** (<code>[Simulation](#swift2.classes.Simulation)</code>) – A swift simulation object

**Returns:**

- – The identifiers of the links in the catchment

#### swift2.doc_helper.get_link_names

```python
get_link_names(simulation)
```

Gets all the names of the links in the catchment

Gets all the names of the links in the catchment

**Parameters:**

- **simulation** (<code>[Simulation](#swift2.classes.Simulation)</code>) – A swift simulation object

**Returns:**

- – The names of the links in the catchment

#### swift2.doc_helper.get_node_ids

```python
get_node_ids(simulation)
```

Gets all the identifiers of the nodes in the catchment

Gets all the identifiers of the nodes in the catchment

**Parameters:**

- **simulation** (<code>[Simulation](#swift2.classes.Simulation)</code>) – A swift simulation object

**Returns:**

- – The identifiers of the nodes in the catchment

#### swift2.doc_helper.get_node_names

```python
get_node_names(simulation)
```

Gets all the names of the nodes in the catchment

Gets all the names of the nodes in the catchment

**Parameters:**

- **simulation** (<code>[Simulation](#swift2.classes.Simulation)</code>) – A swift simulation object

**Returns:**

- – The names of the nodes in the catchment

#### swift2.doc_helper.get_state_value

```python
get_state_value(simulation, var_id)
```

Gets the value(s) of a model state(s)

**Parameters:**

- **simulation** (<code>[Simulation](#swift2.classes.Simulation)</code>) – A swift simulation object
- **var_id** (<code>[VecStr](#swift2.const.VecStr)</code>) – string or sequence of str, model variable state identifier(s)

**Returns:**

- – numeric vector, value(s) of the requested model states

#### swift2.doc_helper.get_subarea_ids

```python
get_subarea_ids(simulation)
```

Gets all the identifiers of the sub-areas in the catchment

Gets all the identifiers of the sub-areas in the catchment

**Parameters:**

- **simulation** (<code>[Simulation](#swift2.classes.Simulation)</code>) – A swift simulation object

**Returns:**

- – The identifiers of the sub-areas in the catchment

#### swift2.doc_helper.get_subarea_names

```python
get_subarea_names(simulation)
```

Gets all the names of the sub-areas in the catchment

Gets all the names of the sub-areas in the catchment

**Parameters:**

- **simulation** (<code>[Simulation](#swift2.classes.Simulation)</code>) – A swift simulation object

**Returns:**

- – The names of the sub-areas in the catchment

#### swift2.doc_helper.get_variable_ids

```python
get_variable_ids(simulation, element_id=None, full_id=True)
```

Gets all the names of the variables of an element within a catchment

Gets all the names of the variables of an element (link, node, subarea) within a catchment

**Parameters:**

- **simulation** (<code>[Simulation](#swift2.classes.Simulation)</code>) – A swift simulation object
- **element_id** (<code>[Any](#typing.Any)</code>) – a character, identifier of the element within the catchment
- **full_id** (<code>[Any](#typing.Any)</code>) – boolean, if TRUE return the full hierarchical identifier

**Returns:**

- – character vector, names (identifiers) of model states in the element

#### swift2.doc_helper.gr4j_scaled_parameteriser

```python
gr4j_scaled_parameteriser(reference_area=240, t_step_seconds=3600)
```

Get a time step and area scaled parameterizer for the GR4 model structure

Get a time step and area scaled parameterizer for the GR4 model structure

**Parameters:**

- **reference_area** (<code>[Any](#swift2.simulation.Any)</code>) – The reference area in km^2 for the parameter x4
- **t_step_seconds** (<code>[Any](#swift2.simulation.Any)</code>) – The simulation time step in seconds.

**Returns:**

- – A SWIFT catchment parameterizer for GR4 model structures

#### swift2.doc_helper.inspect

```python
inspect(simulation, element='link', id='1', full_names=False)
```

Inspect an element of a catchment model

Inspect the current state values of an element of a catchment model

**Parameters:**

- **simulation** (<code>[Simulation](#Simulation)</code>) – A swift simulation object
- **element** (<code>[Any](#swift2.simulation.Any)</code>) – type of top level element, within c('link','node','subarea')
- **id** (<code>[Any](#swift2.simulation.Any)</code>) – SWIFT simulation
- **full_names** (<code>[Any](#swift2.simulation.Any)</code>) – if TRUE returns the full names of state variable ids (e.g. link.link_1.OutlfowRate)

**Returns:**

- – named numeric vector, the current state values of the catchment model element

**Examples:**

TODO

#### swift2.doc_helper.is_common_iterable

```python
is_common_iterable(obj)
```

True if an object is iterable but not a string (str)

#### swift2.doc_helper.is_variable_id

```python
is_variable_id(simulation, var_id)
```

Is a variable identifier valid for a simulation

Is a variable identifier valid for a simulation

**Parameters:**

- **simulation** (<code>[Simulation](#swift2.classes.Simulation)</code>) – A swift simulation object
- **var_id** (<code>[Any](#typing.Any)</code>) – a character, identifier(s) of the variable(s)

**Returns:**

- – logical vector

#### swift2.doc_helper.lag_and_route_parameteriser

```python
lag_and_route_parameteriser()
```

#### swift2.doc_helper.paste0

```python
paste0(*lists, collapse=None)
```

Port of R paste0 function

#### swift2.doc_helper.play_subarea_input

```python
play_subarea_input(simulation, input, subarea_name, input_name)
```

Sets time series as input to a simulation

Sets time series as input to a simulation

**Parameters:**

- **simulation** (<code>[Simulation](#swift2.classes.Simulation)</code>) – A swift simulation object
- **input** (<code>[Any](#Any)</code>) – an xts time series.
- **subarea_name** (<code>[Any](#Any)</code>) – a valid name of the subarea
- **input_name** (<code>[Any](#Any)</code>) – the name of the input variable to the model (i.e. 'P' for the precip of GR5H)

#### swift2.doc_helper.rep

```python
rep(x, n)
```

#### swift2.doc_helper.reset_model_states

```python
reset_model_states(simulation)
```

Reset the model states of a simulation, and apply one or more state initialers if the simulation is configured with any.

**Parameters:**

- **simulation** (<code>[Simulation](#swift2.classes.Simulation)</code>) – simulation

#### swift2.doc_helper.sample_catchment_model

```python
sample_catchment_model(site_id='South_Esk', config_id='catchment')
```

Deserialize a basic catchment structure from the package sample data

Deserialize a basic catchment structure from the package sample data. This function is mostly for documentation purposes.

**Parameters:**

- **site_id** (<code>[Any](#swift2.simulation.Any)</code>) – a site identifier
- **config_id** (<code>[Any](#swift2.simulation.Any)</code>) – a variable identifier for a model structure valid for the given site_id

**Returns:**

- – a model simulation

#### swift2.doc_helper.sample_series

```python
sample_series(site_id='MMH', var_name='rain')
```

Deserialize information to a UTC time series

Deserialize information to a UTC time series. This function is overcoming some behaviors in saving/loading xts series to/from binary RData format. Usage is not intended for most users.

**Parameters:**

- **site_id** (<code>[Any](#swift2.simulation.Any)</code>) – a site identifier
- **var_name** (<code>[Any](#swift2.simulation.Any)</code>) – a variable identifier valid for the given site_id

**Returns:**

- – an xts time series with UTC time indexing

#### swift2.doc_helper.sce_parameter

```python
sce_parameter(nparams, nshuffle=40)
```

Create SCE parameters suited for a given number of parameters.

**Parameters:**

- **nparams** (<code>[int](#int)</code>) – number of free model parameters
- **nshuffle** (<code>[int](#int)</code>) – maximum number of shuffles to do, if no other termination criterion. Defaults to 40.

**Returns:**

- <code>[Dict](#swift2.simulation.Dict)\[[str](#str), [float](#float)\]</code> – Dict\[str,float\]: SCE hyperparameters

#### swift2.doc_helper.set_error_correction_model

```python
set_error_correction_model(simulation, model_id, element_id, length=1, seed=0)
```

Add an error correction model to an element in a catchment

Add an error correction model to an element in a catchment

**Parameters:**

- **simulation** (<code>[Simulation](#swift2.classes.Simulation)</code>) – A swift simulation object
- **model_id** (<code>[str](#str)</code>) – the identifier of the new model to use, e.g. 'ERRIS'
- **element_id** (<code>[str](#str)</code>) – the identifier of the catchment element (node, link, subcatchment) whose outflow rate is corrected.
- **length** (<code>[int](#int)</code>) – other parameters to pass to the creation of the error correction model. Currently length of the AR model only supported.
- **seed** (<code>[int](#int)</code>) – other parameters to pass to the creation of the error correction model. Currently length of the AR model only supported.

#### swift2.doc_helper.set_loglik_param_keys

```python
set_loglik_param_keys(a='a', b='b', m='m', s='s', maxobs='maxobs', ct='ct', censopt='CensOpt')
```

Specify the global parameter names to use in the log-likelihood calculation

Specify the global parameter names to use in the log-likelihood calculation. Consequence of prehistoric legacy.

**Parameters:**

- **a** (<code>[str](#str)</code>) – the name of the a parameter
- **b** (<code>[str](#str)</code>) – the name of the b parameter
- **m** (<code>[str](#str)</code>) – the name of the m parameter
- **s** (<code>[str](#str)</code>) – the name of the s parameter
- **maxobs** (<code>[str](#str)</code>) – the name of the maxobs parameter
- **ct** (<code>[str](#str)</code>) – the name of the ct parameter
- **censopt** (<code>[str](#str)</code>) – the name of the censopt parameter

**Examples:**

TODO

#### swift2.doc_helper.set_muskingum_routing_to_linear

```python
set_muskingum_routing_to_linear(simulation)
```

#### swift2.doc_helper.set_sample_data

```python
set_sample_data(model_sim, site_id='MMH', rain_data_var='rain', evap_data_var='evap', rain_model_var='P', evap_model_var='E', t_step='daily')
```

Sets sample input data into a model simulation

Sets input data from the included sample data into a model simulation

**Parameters:**

- **model_sim** (<code>[Any](#swift2.simulation.Any)</code>) – an S4 object 'ExternalObjRef' [package "cinterop"] with external pointer type "MODEL_SIMULATION_PTR"
- **site_id** (<code>[Any](#swift2.simulation.Any)</code>) – sample data site identifier
- **rain_data_var** (<code>[Any](#swift2.simulation.Any)</code>) – time series ID for the rainfall in the sample data
- **evap_data_var** (<code>[Any](#swift2.simulation.Any)</code>) – time series ID for the evaporation in the sample data
- **rain_model_var** (<code>[Any](#swift2.simulation.Any)</code>) – sub-area runoff model state identifier for the rainfall, e.g. 'P'
- **evap_model_var** (<code>[Any](#swift2.simulation.Any)</code>) – sub-area runoff model state identifier for the evaporation, e.g. 'E'
- **t_step** (<code>[Any](#swift2.simulation.Any)</code>) – identifier for the time step to set the simulation to.

#### swift2.doc_helper.set_simulation_span

```python
set_simulation_span(simulation, start, end)
```

Sets simulation span

Sets the simulation span

**Parameters:**

- **simulation** (<code>[Simulation](#swift2.classes.Simulation)</code>) – A swift simulation object
- **start** (<code>[Any](#typing.Any)</code>) – the start date of the simulation. The time zone will be forced to UTC.
- **end** (<code>[Any](#typing.Any)</code>) – the end date of the simulation. The time zone will be forced to UTC.

#### swift2.doc_helper.set_simulation_time_step

```python
set_simulation_time_step(simulation, name)
```

Sets the time step of a SWIFT simulation

Sets the time step of a SWIFT simulation

**Parameters:**

- **simulation** (<code>[Simulation](#swift2.classes.Simulation)</code>) – A swift simulation object
- **name** (<code>[Any](#typing.Any)</code>) – a time step identifier, currently 'daily' or 'hourly' are supported. The identifier is made lower case in the function.

#### swift2.doc_helper.set_state_value

```python
set_state_value(simulation, var_id, value)
```

Sets the value of a model state

Sets the value of a model state

**Parameters:**

- **simulation** (<code>[Simulation](#swift2.classes.Simulation)</code>) – A swift simulation object
- **var_id** (<code>([str](#str), [Sequence](#typing.Sequence)\[[str](#str)\])</code>) – character, model variable state identifier(s)
- **value** (<code>([float](#float), [int](#int), [bool](#bool), [Sequence](#typing.Sequence))</code>) – numeric value(s)

#### swift2.doc_helper.set_states

```python
set_states(simulation, states)
```

Apply memory states to a simulation

**Parameters:**

- **simulation** (<code>[Simulation](#swift2.classes.Simulation)</code>) – simulation
- **states** (<code>[MemoryStates](#swift2.classes.MemoryStates)</code>) – memory states

#### swift2.doc_helper.short_var_id

```python
short_var_id(var_ids)
```

Shorten long model variable identifiers to the short model variable name

Shorten long model variable identifiers to the short model variable name. This is useful for instance to prepare time series names for multi-plot displays.

**Parameters:**

- **var_ids** (<code>[Any](#swift2.simulation.Any)</code>) – character vector

**Returns:**

- <code>[VecStr](#VecStr)</code> – the short model variable identifiers

**Examples:**

```pycon
>>> short_var_id('elementtype|elementname|varid')
>>> short_var_id('elementtype.elementname.varid')
```

#### swift2.doc_helper.snapshot_state

```python
snapshot_state(simulation)
```

Take a snapshot of the memory states of a simulation

**Parameters:**

- **simulation** (<code>[Simulation](#swift2.classes.Simulation)</code>) – model simulation

**Returns:**

- **MemoryStates** (<code>[MemoryStates](#swift2.classes.MemoryStates)</code>) – memory states, that can be stored and reapplied

#### swift2.doc_helper.sort_by_execution_order

```python
sort_by_execution_order(simulation, split_element_ids, sorting_option='')
```

Sort the specified element ids according to the execution order of the simulation

Sort the specified element ids according to the execution order of the simulation

**Parameters:**

- **simulation** (<code>[Simulation](#swift2.classes.Simulation)</code>) – A swift simulation object
- **split_element_ids** (<code>[Any](#typing.Any)</code>) – a character vector with element identifiers such as 'node.n1', 'link.linkId_2'
- **sorting_option** (<code>[Any](#typing.Any)</code>) – a character - for future options. Ignored for now.

**Returns:**

- – values in split_element_ids sorted by simulation execution order

#### swift2.doc_helper.swap_model

```python
swap_model(simulation, model_id, what='runoff')
```

Clone and change a simulation, using another runoff model

Clone and change a simulation, using another runoff model

**Parameters:**

- **simulation** (<code>[Simulation](#swift2.classes.Simulation)</code>) – A swift simulation object
- **model_id** (<code>[Any](#typing.Any)</code>) – the identifier of the new model to use, e.g. 'GR4J'
- **what** (<code>[Any](#typing.Any)</code>) – character identifying the type of structure: 'runoff', 'channel_routing'

**Returns:**

- – A SWIFT simulation object, clone of the simulation but with a new model type in use.

#### swift2.doc_helper.swc

**Functions:**

- [**add_parameters_pkg**](#swift2.doc_helper.swc.add_parameters_pkg) –
- [**aggregate_parameterisers_pkg**](#swift2.doc_helper.swc.aggregate_parameterisers_pkg) –
- [**convert_optimisation_logger**](#swift2.doc_helper.swc.convert_optimisation_logger) –
- [**default_sce_parameters_pkg**](#swift2.doc_helper.swc.default_sce_parameters_pkg) –
- [**evaluate_score_wila_pkg**](#swift2.doc_helper.swc.evaluate_score_wila_pkg) –
- [**fitnesses_as_rpy_dict**](#swift2.doc_helper.swc.fitnesses_as_rpy_dict) –
- [**get_catchment_structure_pkg**](#swift2.doc_helper.swc.get_catchment_structure_pkg) –
- [**get_played_data**](#swift2.doc_helper.swc.get_played_data) –
- [**get_played_pkg**](#swift2.doc_helper.swc.get_played_pkg) –
- [**get_recorded_data**](#swift2.doc_helper.swc.get_recorded_data) –
- [**get_recorded_pkg**](#swift2.doc_helper.swc.get_recorded_pkg) –
- [**get_simulation_span_pkg**](#swift2.doc_helper.swc.get_simulation_span_pkg) –
- [**get_time_series_data_from_provider**](#swift2.doc_helper.swc.get_time_series_data_from_provider) –
- [**parameteriser_to_data_frame_pkg**](#swift2.doc_helper.swc.parameteriser_to_data_frame_pkg) –
- [**scores_as_rpy_dict**](#swift2.doc_helper.swc.scores_as_rpy_dict) –
- [**scores_as_rpy_dict_pkg**](#swift2.doc_helper.swc.scores_as_rpy_dict_pkg) –
- [**set_parameters_pkg**](#swift2.doc_helper.swc.set_parameters_pkg) –
- [**sort_simulation_elements_by_run_order_pkg**](#swift2.doc_helper.swc.sort_simulation_elements_by_run_order_pkg) –
- [**subset_model_pkg**](#swift2.doc_helper.swc.subset_model_pkg) –
- [**vec_scores_as_dataframe_pkg**](#swift2.doc_helper.swc.vec_scores_as_dataframe_pkg) –

##### swift2.doc_helper.swc.add_parameters_pkg

```python
add_parameters_pkg(parameteriser, parameter_specs)
```

##### swift2.doc_helper.swc.aggregate_parameterisers_pkg

```python
aggregate_parameterisers_pkg(strategy, parameterisers)
```

##### swift2.doc_helper.swc.convert_optimisation_logger

```python
convert_optimisation_logger(log_data, add_numbering=False)
```

##### swift2.doc_helper.swc.default_sce_parameters_pkg

```python
default_sce_parameters_pkg(n=4, nshuffle=40)
```

##### swift2.doc_helper.swc.evaluate_score_wila_pkg

```python
evaluate_score_wila_pkg(objectives, parameteriser)
```

##### swift2.doc_helper.swc.fitnesses_as_rpy_dict

```python
fitnesses_as_rpy_dict(scores)
```

##### swift2.doc_helper.swc.get_catchment_structure_pkg

```python
get_catchment_structure_pkg(simulation)
```

##### swift2.doc_helper.swc.get_played_data

```python
get_played_data(simulation, variable_identifier, mtsg)
```

##### swift2.doc_helper.swc.get_played_pkg

```python
get_played_pkg(simulation, variable_identifier)
```

##### swift2.doc_helper.swc.get_recorded_data

```python
get_recorded_data(simulation, variable_identifier, mtsg)
```

##### swift2.doc_helper.swc.get_recorded_pkg

```python
get_recorded_pkg(simulation, variable_identifier)
```

##### swift2.doc_helper.swc.get_simulation_span_pkg

```python
get_simulation_span_pkg(simulation)
```

##### swift2.doc_helper.swc.get_time_series_data_from_provider

```python
get_time_series_data_from_provider(provider, variable_identifier, mtsg)
```

##### swift2.doc_helper.swc.parameteriser_to_data_frame_pkg

```python
parameteriser_to_data_frame_pkg(parameteriser)
```

##### swift2.doc_helper.swc.scores_as_rpy_dict

```python
scores_as_rpy_dict(scores)
```

##### swift2.doc_helper.swc.scores_as_rpy_dict_pkg

```python
scores_as_rpy_dict_pkg(scores_wrapper)
```

##### swift2.doc_helper.swc.set_parameters_pkg

```python
set_parameters_pkg(parameteriser, parameter_specs)
```

##### swift2.doc_helper.swc.sort_simulation_elements_by_run_order_pkg

```python
sort_simulation_elements_by_run_order_pkg(simulation, elements_ids, ordering_option)
```

##### swift2.doc_helper.swc.subset_model_pkg

```python
subset_model_pkg(simulation, element_name, select_network_above_element, include_element_in_selection, invert_selection)
```

##### swift2.doc_helper.swc.vec_scores_as_dataframe_pkg

```python
vec_scores_as_dataframe_pkg(setOfScores)
```

#### swift2.doc_helper.swg

**Functions:**

- [**AddLinearScalingParameterizer_py**](#swift2.doc_helper.swg.AddLinearScalingParameterizer_py) – AddLinearScalingParameterizer_py
- [**AddParameterDefinition_py**](#swift2.doc_helper.swg.AddParameterDefinition_py) – AddParameterDefinition_py
- [**AddParameterTransform_py**](#swift2.doc_helper.swg.AddParameterTransform_py) – AddParameterTransform_py
- [**AddSingleObservationObjectiveEvaluator_py**](#swift2.doc_helper.swg.AddSingleObservationObjectiveEvaluator_py) – AddSingleObservationObjectiveEvaluator_py
- [**AddStateInitializerModelRunner_py**](#swift2.doc_helper.swg.AddStateInitializerModelRunner_py) – AddStateInitializerModelRunner_py
- [**AddToCompositeParameterizer_py**](#swift2.doc_helper.swg.AddToCompositeParameterizer_py) – AddToCompositeParameterizer_py
- [**AggregateParameterizers_py**](#swift2.doc_helper.swg.AggregateParameterizers_py) – AggregateParameterizers_py
- [**ApplyConfiguration_py**](#swift2.doc_helper.swg.ApplyConfiguration_py) – ApplyConfiguration_py
- [**ApplyMemoryStates_py**](#swift2.doc_helper.swg.ApplyMemoryStates_py) – ApplyMemoryStates_py
- [**CalibrateERRISStageFour_py**](#swift2.doc_helper.swg.CalibrateERRISStageFour_py) – CalibrateERRISStageFour_py
- [**CalibrateERRISStageOne_py**](#swift2.doc_helper.swg.CalibrateERRISStageOne_py) – CalibrateERRISStageOne_py
- [**CalibrateERRISStageThreeMS_py**](#swift2.doc_helper.swg.CalibrateERRISStageThreeMS_py) – CalibrateERRISStageThreeMS_py
- [**CalibrateERRISStageThree_py**](#swift2.doc_helper.swg.CalibrateERRISStageThree_py) – CalibrateERRISStageThree_py
- [**CalibrateERRISStageTwo_py**](#swift2.doc_helper.swg.CalibrateERRISStageTwo_py) – CalibrateERRISStageTwo_py
- [**CalibrateMAERRISStageFour_py**](#swift2.doc_helper.swg.CalibrateMAERRISStageFour_py) – CalibrateMAERRISStageFour_py
- [**CalibrateMAERRISStageOne_py**](#swift2.doc_helper.swg.CalibrateMAERRISStageOne_py) – CalibrateMAERRISStageOne_py
- [**CalibrateMAERRISStageThreeMS_py**](#swift2.doc_helper.swg.CalibrateMAERRISStageThreeMS_py) – CalibrateMAERRISStageThreeMS_py
- [**CalibrateMAERRISStageThree_py**](#swift2.doc_helper.swg.CalibrateMAERRISStageThree_py) – CalibrateMAERRISStageThree_py
- [**CalibrateMAERRISStageTwo_py**](#swift2.doc_helper.swg.CalibrateMAERRISStageTwo_py) – CalibrateMAERRISStageTwo_py
- [**CheckSimulationErrors_py**](#swift2.doc_helper.swg.CheckSimulationErrors_py) – CheckSimulationErrors_py
- [**ClearMemoryStates_py**](#swift2.doc_helper.swg.ClearMemoryStates_py) – ClearMemoryStates_py
- [**CloneHypercubeParameterizer_py**](#swift2.doc_helper.swg.CloneHypercubeParameterizer_py) – CloneHypercubeParameterizer_py
- [**CloneModel_py**](#swift2.doc_helper.swg.CloneModel_py) – CloneModel_py
- [**CloneObjectiveEvaluator_py**](#swift2.doc_helper.swg.CloneObjectiveEvaluator_py) – CloneObjectiveEvaluator_py
- [**CloneStateInitializer_py**](#swift2.doc_helper.swg.CloneStateInitializer_py) – CloneStateInitializer_py
- [**ConcatenateERRISStagesParameters_py**](#swift2.doc_helper.swg.ConcatenateERRISStagesParameters_py) – ConcatenateERRISStagesParameters_py
- [**ConcatenateMAERRISStagesParameters_py**](#swift2.doc_helper.swg.ConcatenateMAERRISStagesParameters_py) – ConcatenateMAERRISStagesParameters_py
- [**CreateCandidateFactorySeedWila_py**](#swift2.doc_helper.swg.CreateCandidateFactorySeedWila_py) – CreateCandidateFactorySeedWila_py
- [**CreateCatchment_py**](#swift2.doc_helper.swg.CreateCatchment_py) – CreateCatchment_py
- [**CreateCompositeObservationObjectiveEvaluator_py**](#swift2.doc_helper.swg.CreateCompositeObservationObjectiveEvaluator_py) – CreateCompositeObservationObjectiveEvaluator_py
- [**CreateCompositeParameterizer_py**](#swift2.doc_helper.swg.CreateCompositeParameterizer_py) – CreateCompositeParameterizer_py
- [**CreateERRISParameterEstimator_py**](#swift2.doc_helper.swg.CreateERRISParameterEstimator_py) – CreateERRISParameterEstimator_py
- [**CreateEmptyCompositeObjectiveEvaluator_py**](#swift2.doc_helper.swg.CreateEmptyCompositeObjectiveEvaluator_py) – CreateEmptyCompositeObjectiveEvaluator_py
- [**CreateEnsembleForecastSimulation_py**](#swift2.doc_helper.swg.CreateEnsembleForecastSimulation_py) – CreateEnsembleForecastSimulation_py
- [**CreateEnsembleModelRunner_py**](#swift2.doc_helper.swg.CreateEnsembleModelRunner_py) – CreateEnsembleModelRunner_py
- [**CreateFilteringParameterizer_py**](#swift2.doc_helper.swg.CreateFilteringParameterizer_py) – CreateFilteringParameterizer_py
- [**CreateFunctionsParameterizer_py**](#swift2.doc_helper.swg.CreateFunctionsParameterizer_py) – CreateFunctionsParameterizer_py
- [**CreateGr4ScaledParameterizer_py**](#swift2.doc_helper.swg.CreateGr4ScaledParameterizer_py) – CreateGr4ScaledParameterizer_py
- [**CreateHypercubeParameterizer_py**](#swift2.doc_helper.swg.CreateHypercubeParameterizer_py) – CreateHypercubeParameterizer_py
- [**CreateLinearFuncParameterizer_py**](#swift2.doc_helper.swg.CreateLinearFuncParameterizer_py) – CreateLinearFuncParameterizer_py
- [**CreateMAERRISParameterEstimator_py**](#swift2.doc_helper.swg.CreateMAERRISParameterEstimator_py) – CreateMAERRISParameterEstimator_py
- [**CreateMultisiteObjectiveEvaluator_py**](#swift2.doc_helper.swg.CreateMultisiteObjectiveEvaluator_py) – CreateMultisiteObjectiveEvaluator_py
- [**CreateMuskingumConstraint_py**](#swift2.doc_helper.swg.CreateMuskingumConstraint_py) – CreateMuskingumConstraint_py
- [**CreateNewFromNetworkInfo_py**](#swift2.doc_helper.swg.CreateNewFromNetworkInfo_py) – CreateNewFromNetworkInfo_py
- [**CreateOptimizerWila_py**](#swift2.doc_helper.swg.CreateOptimizerWila_py) – CreateOptimizerWila_py
- [**CreatePrefixingParameterizer_py**](#swift2.doc_helper.swg.CreatePrefixingParameterizer_py) – CreatePrefixingParameterizer_py
- [**CreateSceMarginalTerminationWila_py**](#swift2.doc_helper.swg.CreateSceMarginalTerminationWila_py) – CreateSceMarginalTerminationWila_py
- [**CreateSceMaxIterationTerminationWila_py**](#swift2.doc_helper.swg.CreateSceMaxIterationTerminationWila_py) – CreateSceMaxIterationTerminationWila_py
- [**CreateSceMaxRuntimeTerminationWila_py**](#swift2.doc_helper.swg.CreateSceMaxRuntimeTerminationWila_py) – CreateSceMaxRuntimeTerminationWila_py
- [**CreateSceTerminationWila_py**](#swift2.doc_helper.swg.CreateSceTerminationWila_py) – CreateSceTerminationWila_py
- [**CreateShuffledComplexEvolutionWila_py**](#swift2.doc_helper.swg.CreateShuffledComplexEvolutionWila_py) – CreateShuffledComplexEvolutionWila_py
- [**CreateSingleObservationObjectiveEvaluatorWila_py**](#swift2.doc_helper.swg.CreateSingleObservationObjectiveEvaluatorWila_py) – CreateSingleObservationObjectiveEvaluatorWila_py
- [**CreateSingleObservationObjectiveEvaluator_py**](#swift2.doc_helper.swg.CreateSingleObservationObjectiveEvaluator_py) – CreateSingleObservationObjectiveEvaluator_py
- [**CreateSqrtAreaRatioParameterizer_py**](#swift2.doc_helper.swg.CreateSqrtAreaRatioParameterizer_py) – CreateSqrtAreaRatioParameterizer_py
- [**CreateStateInitParameterizer_py**](#swift2.doc_helper.swg.CreateStateInitParameterizer_py) – CreateStateInitParameterizer_py
- [**CreateStateInitializer_py**](#swift2.doc_helper.swg.CreateStateInitializer_py) – CreateStateInitializer_py
- [**CreateSubarea_py**](#swift2.doc_helper.swg.CreateSubarea_py) – CreateSubarea_py
- [**CreateSubcatchmentHypercubeParameterizer_py**](#swift2.doc_helper.swg.CreateSubcatchmentHypercubeParameterizer_py) – CreateSubcatchmentHypercubeParameterizer_py
- [**CreateTargetScalingParameterizer_py**](#swift2.doc_helper.swg.CreateTargetScalingParameterizer_py) – CreateTargetScalingParameterizer_py
- [**CreateTestMemoryTrackedParameterizer_py**](#swift2.doc_helper.swg.CreateTestMemoryTrackedParameterizer_py) – CreateTestMemoryTrackedParameterizer_py
- [**CreateTestMemoryTrackedSimulation_py**](#swift2.doc_helper.swg.CreateTestMemoryTrackedSimulation_py) – CreateTestMemoryTrackedSimulation_py
- [**CreateTransformParameterizer_py**](#swift2.doc_helper.swg.CreateTransformParameterizer_py) – CreateTransformParameterizer_py
- [**DisposeCatchmentStructure_py**](#swift2.doc_helper.swg.DisposeCatchmentStructure_py) – DisposeCatchmentStructure_py
- [**DisposeNamedValuedVectorsSwift_py**](#swift2.doc_helper.swg.DisposeNamedValuedVectorsSwift_py) – DisposeNamedValuedVectorsSwift_py
- [**DisposeOptimizerLogDataWila_py**](#swift2.doc_helper.swg.DisposeOptimizerLogDataWila_py) – DisposeOptimizerLogDataWila_py
- [**DisposeSharedPointer_py**](#swift2.doc_helper.swg.DisposeSharedPointer_py) – DisposeSharedPointer_py
- [**DisposeStringStringMapSwift_py**](#swift2.doc_helper.swg.DisposeStringStringMapSwift_py) – DisposeStringStringMapSwift_py
- [**EstimateDualPassParameters_py**](#swift2.doc_helper.swg.EstimateDualPassParameters_py) – EstimateDualPassParameters_py
- [**EstimateERRISParameters_py**](#swift2.doc_helper.swg.EstimateERRISParameters_py) – EstimateERRISParameters_py
- [**EstimateMAERRISParameters_py**](#swift2.doc_helper.swg.EstimateMAERRISParameters_py) – EstimateMAERRISParameters_py
- [**EstimateTransformationParametersMS_py**](#swift2.doc_helper.swg.EstimateTransformationParametersMS_py) – EstimateTransformationParametersMS_py
- [**EstimateTransformationParameters_py**](#swift2.doc_helper.swg.EstimateTransformationParameters_py) – EstimateTransformationParameters_py
- [**EvaluateScoreForParametersInitState_py**](#swift2.doc_helper.swg.EvaluateScoreForParametersInitState_py) – EvaluateScoreForParametersInitState_py
- [**EvaluateScoreForParametersWilaInitState_py**](#swift2.doc_helper.swg.EvaluateScoreForParametersWilaInitState_py) – EvaluateScoreForParametersWilaInitState_py
- [**EvaluateScoreForParametersWila_py**](#swift2.doc_helper.swg.EvaluateScoreForParametersWila_py) – EvaluateScoreForParametersWila_py
- [**EvaluateScoreForParameters_py**](#swift2.doc_helper.swg.EvaluateScoreForParameters_py) – EvaluateScoreForParameters_py
- [**EvaluateScore_py**](#swift2.doc_helper.swg.EvaluateScore_py) – EvaluateScore_py
- [**EvaluateScoresForParametersWila_py**](#swift2.doc_helper.swg.EvaluateScoresForParametersWila_py) – EvaluateScoresForParametersWila_py
- [**ExecuteEnsembleForecastSimulation_py**](#swift2.doc_helper.swg.ExecuteEnsembleForecastSimulation_py) – ExecuteEnsembleForecastSimulation_py
- [**ExecuteOptimizerWila_py**](#swift2.doc_helper.swg.ExecuteOptimizerWila_py) – ExecuteOptimizerWila_py
- [**ExecuteSimulation_py**](#swift2.doc_helper.swg.ExecuteSimulation_py) – ExecuteSimulation_py
- [**GetCatchmentDOTGraph_py**](#swift2.doc_helper.swg.GetCatchmentDOTGraph_py) – GetCatchmentDOTGraph_py
- [**GetCatchmentStructure_py**](#swift2.doc_helper.swg.GetCatchmentStructure_py) – GetCatchmentStructure_py
- [**GetDefaultMaxThreadsWila_py**](#swift2.doc_helper.swg.GetDefaultMaxThreadsWila_py) – GetDefaultMaxThreadsWila_py
- [**GetERRISCalibrationLog_py**](#swift2.doc_helper.swg.GetERRISCalibrationLog_py) – GetERRISCalibrationLog_py
- [**GetElementVarIdentifier_py**](#swift2.doc_helper.swg.GetElementVarIdentifier_py) – GetElementVarIdentifier_py
- [**GetElementVarIdentifiers_py**](#swift2.doc_helper.swg.GetElementVarIdentifiers_py) – GetElementVarIdentifiers_py
- [**GetEnd_py**](#swift2.doc_helper.swg.GetEnd_py) – GetEnd_py
- [**GetEnsembleForecastEnsembleRecorded_py**](#swift2.doc_helper.swg.GetEnsembleForecastEnsembleRecorded_py) – GetEnsembleForecastEnsembleRecorded_py
- [**GetEnsembleForecastEnsembleSize_py**](#swift2.doc_helper.swg.GetEnsembleForecastEnsembleSize_py) – GetEnsembleForecastEnsembleSize_py
- [**GetEnsembleForecastLeadLength_py**](#swift2.doc_helper.swg.GetEnsembleForecastLeadLength_py) – GetEnsembleForecastLeadLength_py
- [**GetEnsembleForecastSingleRecorded_py**](#swift2.doc_helper.swg.GetEnsembleForecastSingleRecorded_py) – GetEnsembleForecastSingleRecorded_py
- [**GetFeasibleMuskingumBounds_py**](#swift2.doc_helper.swg.GetFeasibleMuskingumBounds_py) – GetFeasibleMuskingumBounds_py
- [**GetKnownParameterizationStrategies_py**](#swift2.doc_helper.swg.GetKnownParameterizationStrategies_py) – GetKnownParameterizationStrategies_py
- [**GetKnownParameterizationTargetSelectorTypes_py**](#swift2.doc_helper.swg.GetKnownParameterizationTargetSelectorTypes_py) – GetKnownParameterizationTargetSelectorTypes_py
- [**GetKnownParameterizerAggregationStrategies_py**](#swift2.doc_helper.swg.GetKnownParameterizerAggregationStrategies_py) – GetKnownParameterizerAggregationStrategies_py
- [**GetLastStdExceptionMessage_py**](#swift2.doc_helper.swg.GetLastStdExceptionMessage_py) – GetLastStdExceptionMessage_py
- [**GetLengthSetOfScores_py**](#swift2.doc_helper.swg.GetLengthSetOfScores_py) – GetLengthSetOfScores_py
- [**GetLinkIdentifier_py**](#swift2.doc_helper.swg.GetLinkIdentifier_py) – GetLinkIdentifier_py
- [**GetLinkIdentifiers_py**](#swift2.doc_helper.swg.GetLinkIdentifiers_py) – GetLinkIdentifiers_py
- [**GetLinkName_py**](#swift2.doc_helper.swg.GetLinkName_py) – GetLinkName_py
- [**GetLinkNames_py**](#swift2.doc_helper.swg.GetLinkNames_py) – GetLinkNames_py
- [**GetMAERRISCalibrationLog_py**](#swift2.doc_helper.swg.GetMAERRISCalibrationLog_py) – GetMAERRISCalibrationLog_py
- [**GetMemoryStates_py**](#swift2.doc_helper.swg.GetMemoryStates_py) – GetMemoryStates_py
- [**GetModelConfigurationSwift_py**](#swift2.doc_helper.swg.GetModelConfigurationSwift_py) – GetModelConfigurationSwift_py
- [**GetNameObjectiveEvaluator_py**](#swift2.doc_helper.swg.GetNameObjectiveEvaluator_py) – GetNameObjectiveEvaluator_py
- [**GetNodeIdentifier_py**](#swift2.doc_helper.swg.GetNodeIdentifier_py) – GetNodeIdentifier_py
- [**GetNodeIdentifiers_py**](#swift2.doc_helper.swg.GetNodeIdentifiers_py) – GetNodeIdentifiers_py
- [**GetNodeName_py**](#swift2.doc_helper.swg.GetNodeName_py) – GetNodeName_py
- [**GetNodeNames_py**](#swift2.doc_helper.swg.GetNodeNames_py) – GetNodeNames_py
- [**GetNumCatchments_py**](#swift2.doc_helper.swg.GetNumCatchments_py) – GetNumCatchments_py
- [**GetNumHyperCubesWila_py**](#swift2.doc_helper.swg.GetNumHyperCubesWila_py) – GetNumHyperCubesWila_py
- [**GetNumHyperCubes_py**](#swift2.doc_helper.swg.GetNumHyperCubes_py) – GetNumHyperCubes_py
- [**GetNumLinks_py**](#swift2.doc_helper.swg.GetNumLinks_py) – GetNumLinks_py
- [**GetNumMemTestCatchments_py**](#swift2.doc_helper.swg.GetNumMemTestCatchments_py) – GetNumMemTestCatchments_py
- [**GetNumMemTestModelRunners_py**](#swift2.doc_helper.swg.GetNumMemTestModelRunners_py) – GetNumMemTestModelRunners_py
- [**GetNumMemTestParameterizers_py**](#swift2.doc_helper.swg.GetNumMemTestParameterizers_py) – GetNumMemTestParameterizers_py
- [**GetNumModelRunners_py**](#swift2.doc_helper.swg.GetNumModelRunners_py) – GetNumModelRunners_py
- [**GetNumNodes_py**](#swift2.doc_helper.swg.GetNumNodes_py) – GetNumNodes_py
- [**GetNumParameters_py**](#swift2.doc_helper.swg.GetNumParameters_py) – GetNumParameters_py
- [**GetNumPlayedVariables_py**](#swift2.doc_helper.swg.GetNumPlayedVariables_py) – GetNumPlayedVariables_py
- [**GetNumRainfallRunoff_py**](#swift2.doc_helper.swg.GetNumRainfallRunoff_py) – GetNumRainfallRunoff_py
- [**GetNumRecordedVariables_py**](#swift2.doc_helper.swg.GetNumRecordedVariables_py) – GetNumRecordedVariables_py
- [**GetNumRunoffModelIdentifiers_py**](#swift2.doc_helper.swg.GetNumRunoffModelIdentifiers_py) – GetNumRunoffModelIdentifiers_py
- [**GetNumRunoffModelVarIdentifiers_py**](#swift2.doc_helper.swg.GetNumRunoffModelVarIdentifiers_py) – GetNumRunoffModelVarIdentifiers_py
- [**GetNumScoresWila_py**](#swift2.doc_helper.swg.GetNumScoresWila_py) – GetNumScoresWila_py
- [**GetNumStateInitializers_py**](#swift2.doc_helper.swg.GetNumStateInitializers_py) – GetNumStateInitializers_py
- [**GetNumStepsForTimeSpan_py**](#swift2.doc_helper.swg.GetNumStepsForTimeSpan_py) – GetNumStepsForTimeSpan_py
- [**GetNumSteps_py**](#swift2.doc_helper.swg.GetNumSteps_py) – GetNumSteps_py
- [**GetNumSubareas_py**](#swift2.doc_helper.swg.GetNumSubareas_py) – GetNumSubareas_py
- [**GetNumVarIdentifiers_py**](#swift2.doc_helper.swg.GetNumVarIdentifiers_py) – GetNumVarIdentifiers_py
- [**GetOptimizerLogDataWilaDims_py**](#swift2.doc_helper.swg.GetOptimizerLogDataWilaDims_py) – GetOptimizerLogDataWilaDims_py
- [**GetOptimizerLogDataWilaNumericDataNames_py**](#swift2.doc_helper.swg.GetOptimizerLogDataWilaNumericDataNames_py) – GetOptimizerLogDataWilaNumericDataNames_py
- [**GetOptimizerLogDataWilaNumericData_py**](#swift2.doc_helper.swg.GetOptimizerLogDataWilaNumericData_py) – GetOptimizerLogDataWilaNumericData_py
- [**GetOptimizerLogDataWilaStringDataNames_py**](#swift2.doc_helper.swg.GetOptimizerLogDataWilaStringDataNames_py) – GetOptimizerLogDataWilaStringDataNames_py
- [**GetOptimizerLogDataWilaStringData_py**](#swift2.doc_helper.swg.GetOptimizerLogDataWilaStringData_py) – GetOptimizerLogDataWilaStringData_py
- [**GetOptimizerLogDataWila_py**](#swift2.doc_helper.swg.GetOptimizerLogDataWila_py) – GetOptimizerLogDataWila_py
- [**GetParameterMaxValue_py**](#swift2.doc_helper.swg.GetParameterMaxValue_py) – GetParameterMaxValue_py
- [**GetParameterMinValue_py**](#swift2.doc_helper.swg.GetParameterMinValue_py) – GetParameterMinValue_py
- [**GetParameterName_py**](#swift2.doc_helper.swg.GetParameterName_py) – GetParameterName_py
- [**GetParameterValue_py**](#swift2.doc_helper.swg.GetParameterValue_py) – GetParameterValue_py
- [**GetPlayedTimeSeriesLength_py**](#swift2.doc_helper.swg.GetPlayedTimeSeriesLength_py) – GetPlayedTimeSeriesLength_py
- [**GetPlayedTsGeometry_py**](#swift2.doc_helper.swg.GetPlayedTsGeometry_py) – GetPlayedTsGeometry_py
- [**GetPlayedVariableName_py**](#swift2.doc_helper.swg.GetPlayedVariableName_py) – GetPlayedVariableName_py
- [**GetPlayedVariableNames_py**](#swift2.doc_helper.swg.GetPlayedVariableNames_py) – GetPlayedVariableNames_py
- [**GetPlayed_py**](#swift2.doc_helper.swg.GetPlayed_py) – GetPlayed_py
- [**GetRecordedEnsembleForecastTimeSeries_py**](#swift2.doc_helper.swg.GetRecordedEnsembleForecastTimeSeries_py) – GetRecordedEnsembleForecastTimeSeries_py
- [**GetRecordedTsGeometry_py**](#swift2.doc_helper.swg.GetRecordedTsGeometry_py) – GetRecordedTsGeometry_py
- [**GetRecordedVariableName_py**](#swift2.doc_helper.swg.GetRecordedVariableName_py) – GetRecordedVariableName_py
- [**GetRecordedVariableNames_py**](#swift2.doc_helper.swg.GetRecordedVariableNames_py) – GetRecordedVariableNames_py
- [**GetRecorded_py**](#swift2.doc_helper.swg.GetRecorded_py) – GetRecorded_py
- [**GetRunoffModelIdentifier_py**](#swift2.doc_helper.swg.GetRunoffModelIdentifier_py) – GetRunoffModelIdentifier_py
- [**GetRunoffModelIdentifiers_py**](#swift2.doc_helper.swg.GetRunoffModelIdentifiers_py) – GetRunoffModelIdentifiers_py
- [**GetRunoffModelVarIdentifier_py**](#swift2.doc_helper.swg.GetRunoffModelVarIdentifier_py) – GetRunoffModelVarIdentifier_py
- [**GetRunoffModelVarIdentifiers_py**](#swift2.doc_helper.swg.GetRunoffModelVarIdentifiers_py) – GetRunoffModelVarIdentifiers_py
- [**GetScoreNameWila_py**](#swift2.doc_helper.swg.GetScoreNameWila_py) – GetScoreNameWila_py
- [**GetScoreWila_py**](#swift2.doc_helper.swg.GetScoreWila_py) – GetScoreWila_py
- [**GetScoresAtIndex_py**](#swift2.doc_helper.swg.GetScoresAtIndex_py) – GetScoresAtIndex_py
- [**GetStart_py**](#swift2.doc_helper.swg.GetStart_py) – GetStart_py
- [**GetSubareaIdentifier_py**](#swift2.doc_helper.swg.GetSubareaIdentifier_py) – GetSubareaIdentifier_py
- [**GetSubareaIdentifiers_py**](#swift2.doc_helper.swg.GetSubareaIdentifiers_py) – GetSubareaIdentifiers_py
- [**GetSubareaName_py**](#swift2.doc_helper.swg.GetSubareaName_py) – GetSubareaName_py
- [**GetSubareaNames_py**](#swift2.doc_helper.swg.GetSubareaNames_py) – GetSubareaNames_py
- [**GetSystemConfigurationWila_py**](#swift2.doc_helper.swg.GetSystemConfigurationWila_py) – GetSystemConfigurationWila_py
- [**GetTimeStepName_py**](#swift2.doc_helper.swg.GetTimeStepName_py) – GetTimeStepName_py
- [**GetValueStateInitializer_py**](#swift2.doc_helper.swg.GetValueStateInitializer_py) – GetValueStateInitializer_py
- [**GetVariableBool_py**](#swift2.doc_helper.swg.GetVariableBool_py) – GetVariableBool_py
- [**GetVariableInt_py**](#swift2.doc_helper.swg.GetVariableInt_py) – GetVariableInt_py
- [**GetVariable_py**](#swift2.doc_helper.swg.GetVariable_py) – GetVariable_py
- [**HideParameters_py**](#swift2.doc_helper.swg.HideParameters_py) – HideParameters_py
- [**HomotheticTransform_py**](#swift2.doc_helper.swg.HomotheticTransform_py) – HomotheticTransform_py
- [**IsDictionaryStateInitializer_py**](#swift2.doc_helper.swg.IsDictionaryStateInitializer_py) – IsDictionaryStateInitializer_py
- [**IsValidVariableIdentifier_py**](#swift2.doc_helper.swg.IsValidVariableIdentifier_py) – IsValidVariableIdentifier_py
- [**IsWithinBounds_py**](#swift2.doc_helper.swg.IsWithinBounds_py) – IsWithinBounds_py
- [**LoadMemoryStatesFromFile_py**](#swift2.doc_helper.swg.LoadMemoryStatesFromFile_py) – LoadMemoryStatesFromFile_py
- [**LoadModelSimulationFromJson_py**](#swift2.doc_helper.swg.LoadModelSimulationFromJson_py) – LoadModelSimulationFromJson_py
- [**LoadParameterizer_py**](#swift2.doc_helper.swg.LoadParameterizer_py) – LoadParameterizer_py
- [**LoadVersionOneControlFile_py**](#swift2.doc_helper.swg.LoadVersionOneControlFile_py) – LoadVersionOneControlFile_py
- [**LoadVersionOneTimeSeriesFile_py**](#swift2.doc_helper.swg.LoadVersionOneTimeSeriesFile_py) – LoadVersionOneTimeSeriesFile_py
- [**MemoryStatesFromString_py**](#swift2.doc_helper.swg.MemoryStatesFromString_py) – MemoryStatesFromString_py
- [**ObjectiveEvaluatorIsMaximizable_py**](#swift2.doc_helper.swg.ObjectiveEvaluatorIsMaximizable_py) – ObjectiveEvaluatorIsMaximizable_py
- [**PlayDatasetEnsembleForecastInput_py**](#swift2.doc_helper.swg.PlayDatasetEnsembleForecastInput_py) – PlayDatasetEnsembleForecastInput_py
- [**PlayDatasetInputs_py**](#swift2.doc_helper.swg.PlayDatasetInputs_py) – PlayDatasetInputs_py
- [**PlayDatasetSingleInput_py**](#swift2.doc_helper.swg.PlayDatasetSingleInput_py) – PlayDatasetSingleInput_py
- [**PlayEnsembleForecastTimeSeries_py**](#swift2.doc_helper.swg.PlayEnsembleForecastTimeSeries_py) – PlayEnsembleForecastTimeSeries_py
- [**Play_py**](#swift2.doc_helper.swg.Play_py) – Play_py
- [**PrepareDualPassForecasting_py**](#swift2.doc_helper.swg.PrepareDualPassForecasting_py) – PrepareDualPassForecasting_py
- [**PrepareERRISForecasting_py**](#swift2.doc_helper.swg.PrepareERRISForecasting_py) – PrepareERRISForecasting_py
- [**PrepareEnsembleModelRunner_py**](#swift2.doc_helper.swg.PrepareEnsembleModelRunner_py) – PrepareEnsembleModelRunner_py
- [**RecordEnsembleForecastTimeSeries_py**](#swift2.doc_helper.swg.RecordEnsembleForecastTimeSeries_py) – RecordEnsembleForecastTimeSeries_py
- [**RecordEnsembleForecastToRecorder_py**](#swift2.doc_helper.swg.RecordEnsembleForecastToRecorder_py) – RecordEnsembleForecastToRecorder_py
- [**RecordEnsembleModelRunner_py**](#swift2.doc_helper.swg.RecordEnsembleModelRunner_py) – RecordEnsembleModelRunner_py
- [**Record_py**](#swift2.doc_helper.swg.Record_py) – Record_py
- [**RegisterAdditionalSwiftDataHandling_py**](#swift2.doc_helper.swg.RegisterAdditionalSwiftDataHandling_py) – RegisterAdditionalSwiftDataHandling_py
- [**RegisterExceptionCallbackSwift_py**](#swift2.doc_helper.swg.RegisterExceptionCallbackSwift_py) – RegisterExceptionCallbackSwift_py
- [**RegisterExceptionCallback_py**](#swift2.doc_helper.swg.RegisterExceptionCallback_py) – RegisterExceptionCallback_py
- [**RemoveERRISExclusionPeriod_py**](#swift2.doc_helper.swg.RemoveERRISExclusionPeriod_py) – RemoveERRISExclusionPeriod_py
- [**RemoveERRISWarmupPeriod_py**](#swift2.doc_helper.swg.RemoveERRISWarmupPeriod_py) – RemoveERRISWarmupPeriod_py
- [**RemoveMAERRISExclusionPeriod_py**](#swift2.doc_helper.swg.RemoveMAERRISExclusionPeriod_py) – RemoveMAERRISExclusionPeriod_py
- [**RemoveMAERRISWarmupPeriod_py**](#swift2.doc_helper.swg.RemoveMAERRISWarmupPeriod_py) – RemoveMAERRISWarmupPeriod_py
- [**RemoveModel_py**](#swift2.doc_helper.swg.RemoveModel_py) – RemoveModel_py
- [**RemovePlayedTimeSeries_py**](#swift2.doc_helper.swg.RemovePlayedTimeSeries_py) – RemovePlayedTimeSeries_py
- [**RemoveRecorder_py**](#swift2.doc_helper.swg.RemoveRecorder_py) – RemoveRecorder_py
- [**RemoveStateInitializerModelRunner_py**](#swift2.doc_helper.swg.RemoveStateInitializerModelRunner_py) – RemoveStateInitializerModelRunner_py
- [**RemoveStorageDischargeRelationship_py**](#swift2.doc_helper.swg.RemoveStorageDischargeRelationship_py) – RemoveStorageDischargeRelationship_py
- [**ResetModelStates_py**](#swift2.doc_helper.swg.ResetModelStates_py) – ResetModelStates_py
- [**SaveMemoryStatesToFile_py**](#swift2.doc_helper.swg.SaveMemoryStatesToFile_py) – SaveMemoryStatesToFile_py
- [**SaveModelSimulationToJson_py**](#swift2.doc_helper.swg.SaveModelSimulationToJson_py) – SaveModelSimulationToJson_py
- [**SaveParameterizer_py**](#swift2.doc_helper.swg.SaveParameterizer_py) – SaveParameterizer_py
- [**SetChannelRoutingModel_py**](#swift2.doc_helper.swg.SetChannelRoutingModel_py) – SetChannelRoutingModel_py
- [**SetDefaultMaxThreadsWila_py**](#swift2.doc_helper.swg.SetDefaultMaxThreadsWila_py) – SetDefaultMaxThreadsWila_py
- [**SetDefaultParameters_py**](#swift2.doc_helper.swg.SetDefaultParameters_py) – SetDefaultParameters_py
- [**SetERRISCensOptions_py**](#swift2.doc_helper.swg.SetERRISCensOptions_py) – SetERRISCensOptions_py
- [**SetERRISErrorCorrectionParameterSpace_py**](#swift2.doc_helper.swg.SetERRISErrorCorrectionParameterSpace_py) – SetERRISErrorCorrectionParameterSpace_py
- [**SetERRISEstimationPeriod_py**](#swift2.doc_helper.swg.SetERRISEstimationPeriod_py) – SetERRISEstimationPeriod_py
- [**SetERRISExclusionPeriod_py**](#swift2.doc_helper.swg.SetERRISExclusionPeriod_py) – SetERRISExclusionPeriod_py
- [**SetERRISHydrologicParameterSpace_py**](#swift2.doc_helper.swg.SetERRISHydrologicParameterSpace_py) – SetERRISHydrologicParameterSpace_py
- [**SetERRISMaxObservation_py**](#swift2.doc_helper.swg.SetERRISMaxObservation_py) – SetERRISMaxObservation_py
- [**SetERRISVerboseCalibration_py**](#swift2.doc_helper.swg.SetERRISVerboseCalibration_py) – SetERRISVerboseCalibration_py
- [**SetERRISWarmupPeriod_py**](#swift2.doc_helper.swg.SetERRISWarmupPeriod_py) – SetERRISWarmupPeriod_py
- [**SetErrorCorrectionModel_py**](#swift2.doc_helper.swg.SetErrorCorrectionModel_py) – SetErrorCorrectionModel_py
- [**SetLogLikelihoodMixtureVariableNames_py**](#swift2.doc_helper.swg.SetLogLikelihoodMixtureVariableNames_py) – SetLogLikelihoodMixtureVariableNames_py
- [**SetLogLikelihoodVariableNames_py**](#swift2.doc_helper.swg.SetLogLikelihoodVariableNames_py) – SetLogLikelihoodVariableNames_py
- [**SetLogLikelihoodXVariableNames_py**](#swift2.doc_helper.swg.SetLogLikelihoodXVariableNames_py) – SetLogLikelihoodXVariableNames_py
- [**SetMAERRISCensOptions_py**](#swift2.doc_helper.swg.SetMAERRISCensOptions_py) – SetMAERRISCensOptions_py
- [**SetMAERRISErrorCorrectionParameterSpace_py**](#swift2.doc_helper.swg.SetMAERRISErrorCorrectionParameterSpace_py) – SetMAERRISErrorCorrectionParameterSpace_py
- [**SetMAERRISEstimationPeriod_py**](#swift2.doc_helper.swg.SetMAERRISEstimationPeriod_py) – SetMAERRISEstimationPeriod_py
- [**SetMAERRISExclusionPeriod_py**](#swift2.doc_helper.swg.SetMAERRISExclusionPeriod_py) – SetMAERRISExclusionPeriod_py
- [**SetMAERRISHydrologicParameterSpace_py**](#swift2.doc_helper.swg.SetMAERRISHydrologicParameterSpace_py) – SetMAERRISHydrologicParameterSpace_py
- [**SetMAERRISMaxObservation_py**](#swift2.doc_helper.swg.SetMAERRISMaxObservation_py) – SetMAERRISMaxObservation_py
- [**SetMAERRISRestrictionOn_py**](#swift2.doc_helper.swg.SetMAERRISRestrictionOn_py) – SetMAERRISRestrictionOn_py
- [**SetMAERRISS2Window_py**](#swift2.doc_helper.swg.SetMAERRISS2Window_py) – SetMAERRISS2Window_py
- [**SetMAERRISVerboseCalibration_py**](#swift2.doc_helper.swg.SetMAERRISVerboseCalibration_py) – SetMAERRISVerboseCalibration_py
- [**SetMAERRISWarmupPeriod_py**](#swift2.doc_helper.swg.SetMAERRISWarmupPeriod_py) – SetMAERRISWarmupPeriod_py
- [**SetMaxParameterValue_py**](#swift2.doc_helper.swg.SetMaxParameterValue_py) – SetMaxParameterValue_py
- [**SetMaxThreadsOptimizerWila_py**](#swift2.doc_helper.swg.SetMaxThreadsOptimizerWila_py) – SetMaxThreadsOptimizerWila_py
- [**SetMemoryStates_py**](#swift2.doc_helper.swg.SetMemoryStates_py) – SetMemoryStates_py
- [**SetMinParameterValue_py**](#swift2.doc_helper.swg.SetMinParameterValue_py) – SetMinParameterValue_py
- [**SetOptimizerLoggerWila_py**](#swift2.doc_helper.swg.SetOptimizerLoggerWila_py) – SetOptimizerLoggerWila_py
- [**SetParameterDefinition_py**](#swift2.doc_helper.swg.SetParameterDefinition_py) – SetParameterDefinition_py
- [**SetParameterValue_py**](#swift2.doc_helper.swg.SetParameterValue_py) – SetParameterValue_py
- [**SetReservoirGeometry_py**](#swift2.doc_helper.swg.SetReservoirGeometry_py) – SetReservoirGeometry_py
- [**SetReservoirMaxDischarge_py**](#swift2.doc_helper.swg.SetReservoirMaxDischarge_py) – SetReservoirMaxDischarge_py
- [**SetReservoirMinDischarge_py**](#swift2.doc_helper.swg.SetReservoirMinDischarge_py) – SetReservoirMinDischarge_py
- [**SetReservoirModel_py**](#swift2.doc_helper.swg.SetReservoirModel_py) – SetReservoirModel_py
- [**SetReservoirOpsReleaseCurve_py**](#swift2.doc_helper.swg.SetReservoirOpsReleaseCurve_py) – SetReservoirOpsReleaseCurve_py
- [**SetRunoffPostProcessingModel_py**](#swift2.doc_helper.swg.SetRunoffPostProcessingModel_py) – SetRunoffPostProcessingModel_py
- [**SetSeedForModel_py**](#swift2.doc_helper.swg.SetSeedForModel_py) – SetSeedForModel_py
- [**SetSpan_py**](#swift2.doc_helper.swg.SetSpan_py) – SetSpan_py
- [**SetSubareaInputsPreprocessorModel_py**](#swift2.doc_helper.swg.SetSubareaInputsPreprocessorModel_py) – SetSubareaInputsPreprocessorModel_py
- [**SetTimeStep_py**](#swift2.doc_helper.swg.SetTimeStep_py) – SetTimeStep_py
- [**SetValueStateInitializer_py**](#swift2.doc_helper.swg.SetValueStateInitializer_py) – SetValueStateInitializer_py
- [**SetVariableBool_py**](#swift2.doc_helper.swg.SetVariableBool_py) – SetVariableBool_py
- [**SetVariableInt_py**](#swift2.doc_helper.swg.SetVariableInt_py) – SetVariableInt_py
- [**SetVariable_py**](#swift2.doc_helper.swg.SetVariable_py) – SetVariable_py
- [**SetupEnsembleModelRunner_py**](#swift2.doc_helper.swg.SetupEnsembleModelRunner_py) – SetupEnsembleModelRunner_py
- [**ShowParameters_py**](#swift2.doc_helper.swg.ShowParameters_py) – ShowParameters_py
- [**SnapshotMemoryStates_py**](#swift2.doc_helper.swg.SnapshotMemoryStates_py) – SnapshotMemoryStates_py
- [**SortSetOfScoresBy_py**](#swift2.doc_helper.swg.SortSetOfScoresBy_py) – SortSetOfScoresBy_py
- [**SortSimulationElementsByRunOrder_py**](#swift2.doc_helper.swg.SortSimulationElementsByRunOrder_py) – SortSimulationElementsByRunOrder_py
- [**SubsetModel_py**](#swift2.doc_helper.swg.SubsetModel_py) – SubsetModel_py
- [**SupportsThreadSafeCloning_py**](#swift2.doc_helper.swg.SupportsThreadSafeCloning_py) – SupportsThreadSafeCloning_py
- [**SwapRunoffModel_py**](#swift2.doc_helper.swg.SwapRunoffModel_py) – SwapRunoffModel_py
- [**TagParameterizer_py**](#swift2.doc_helper.swg.TagParameterizer_py) – TagParameterizer_py
- [**UntransformHypercubeParameterizer_py**](#swift2.doc_helper.swg.UntransformHypercubeParameterizer_py) – UntransformHypercubeParameterizer_py
- [**UnwrapObjectiveEvaluatorWila_py**](#swift2.doc_helper.swg.UnwrapObjectiveEvaluatorWila_py) – UnwrapObjectiveEvaluatorWila_py
- [**UseStateInitializerModelRunner_py**](#swift2.doc_helper.swg.UseStateInitializerModelRunner_py) – UseStateInitializerModelRunner_py
- [**VariableIsBool_py**](#swift2.doc_helper.swg.VariableIsBool_py) – VariableIsBool_py
- [**VariableIsDouble_py**](#swift2.doc_helper.swg.VariableIsDouble_py) – VariableIsDouble_py
- [**VariableIsInt_py**](#swift2.doc_helper.swg.VariableIsInt_py) – VariableIsInt_py
- [**WireSubareaInputsPreprocessorModel_py**](#swift2.doc_helper.swg.WireSubareaInputsPreprocessorModel_py) – WireSubareaInputsPreprocessorModel_py
- [**WrapObjectiveEvaluatorWila_py**](#swift2.doc_helper.swg.WrapObjectiveEvaluatorWila_py) – WrapObjectiveEvaluatorWila_py
- [**char_array_to_py**](#swift2.doc_helper.swg.char_array_to_py) –
- [**charp_array_to_py**](#swift2.doc_helper.swg.charp_array_to_py) –
- [**custom_wrap_cffi_native_handle**](#swift2.doc_helper.swg.custom_wrap_cffi_native_handle) – Create a wrapper around a cffi pointer (if this is one),
- [**dispose_shared_pointer_py**](#swift2.doc_helper.swg.dispose_shared_pointer_py) –
- [**named_values_to_py**](#swift2.doc_helper.swg.named_values_to_py) –
- [**opaque_ts_as_xarray_time_series**](#swift2.doc_helper.swg.opaque_ts_as_xarray_time_series) –
- [**py_time_series_dimensions_description**](#swift2.doc_helper.swg.py_time_series_dimensions_description) –
- [**set_wrap_cffi_native_handle**](#swift2.doc_helper.swg.set_wrap_cffi_native_handle) –
- [**toSceParametersNative**](#swift2.doc_helper.swg.toSceParametersNative) –

##### swift2.doc_helper.swg.AddLinearScalingParameterizer_py

```python
AddLinearScalingParameterizer_py(scalingParameterizer, paramName, stateName, scalingVarName, constant, min, max, value)
```

AddLinearScalingParameterizer_py

AddLinearScalingParameterizer_py: generated wrapper function for API function AddLinearScalingParameterizer

**Parameters:**

- **scalingParameterizer** (<code>[ScalingParameteriser](#swift2.classes.ScalingParameteriser)</code>) – scalingParameterizer
- **paramName** (<code>[str](#str)</code>) – paramName
- **stateName** (<code>[str](#str)</code>) – stateName
- **scalingVarName** (<code>[str](#str)</code>) – scalingVarName
- **constant** (<code>[float](#float)</code>) – constant
- **min** (<code>[float](#float)</code>) – min
- **max** (<code>[float](#float)</code>) – max
- **value** (<code>[float](#float)</code>) – value

##### swift2.doc_helper.swg.AddParameterDefinition_py

```python
AddParameterDefinition_py(hypercubeParameterizer, variableName, min, max, value)
```

AddParameterDefinition_py

AddParameterDefinition_py: generated wrapper function for API function AddParameterDefinition

**Parameters:**

- **hypercubeParameterizer** (<code>[HypercubeParameteriser](#swift2.classes.HypercubeParameteriser)</code>) – hypercubeParameterizer
- **variableName** (<code>[str](#str)</code>) – variableName
- **min** (<code>[float](#float)</code>) – min
- **max** (<code>[float](#float)</code>) – max
- **value** (<code>[float](#float)</code>) – value

##### swift2.doc_helper.swg.AddParameterTransform_py

```python
AddParameterTransform_py(transformParameterizer, paramName, innerParamName, transformId, a, b)
```

AddParameterTransform_py

AddParameterTransform_py: generated wrapper function for API function AddParameterTransform

**Parameters:**

- **transformParameterizer** (<code>[TransformParameteriser](#swift2.classes.TransformParameteriser)</code>) – transformParameterizer
- **paramName** (<code>[str](#str)</code>) – paramName
- **innerParamName** (<code>[str](#str)</code>) – innerParamName
- **transformId** (<code>[str](#str)</code>) – transformId
- **a** (<code>[float](#float)</code>) – a
- **b** (<code>[float](#float)</code>) – b

##### swift2.doc_helper.swg.AddSingleObservationObjectiveEvaluator_py

```python
AddSingleObservationObjectiveEvaluator_py(compositeObjective, singleObjective, weight, name)
```

AddSingleObservationObjectiveEvaluator_py

AddSingleObservationObjectiveEvaluator_py: generated wrapper function for API function AddSingleObservationObjectiveEvaluator

**Parameters:**

- **compositeObjective** (<code>[DeletableCffiNativeHandle](#refcount.interop.DeletableCffiNativeHandle)</code>) – compositeObjective
- **singleObjective** (<code>[DeletableCffiNativeHandle](#refcount.interop.DeletableCffiNativeHandle)</code>) – singleObjective
- **weight** (<code>[float](#float)</code>) – weight
- **name** (<code>[str](#str)</code>) – name

##### swift2.doc_helper.swg.AddStateInitializerModelRunner_py

```python
AddStateInitializerModelRunner_py(modelSimulation, stateInit)
```

AddStateInitializerModelRunner_py

AddStateInitializerModelRunner_py: generated wrapper function for API function AddStateInitializerModelRunner

**Parameters:**

- **modelSimulation** (<code>[Simulation](#swift2.classes.Simulation)</code>) – modelSimulation
- **stateInit** (<code>[StateInitialiser](#swift2.classes.StateInitialiser)</code>) – stateInit

##### swift2.doc_helper.swg.AddToCompositeParameterizer_py

```python
AddToCompositeParameterizer_py(compositeParameterizer, parameterizer)
```

AddToCompositeParameterizer_py

AddToCompositeParameterizer_py: generated wrapper function for API function AddToCompositeParameterizer

**Parameters:**

- **compositeParameterizer** (<code>[CompositeParameteriser](#swift2.classes.CompositeParameteriser)</code>) – compositeParameterizer
- **parameterizer** (<code>[HypercubeParameteriser](#swift2.classes.HypercubeParameteriser)</code>) – parameterizer

##### swift2.doc_helper.swg.AggregateParameterizers_py

```python
AggregateParameterizers_py(strategy, parameterizers, numParameterizers)
```

AggregateParameterizers_py

AggregateParameterizers_py: generated wrapper function for API function AggregateParameterizers

**Parameters:**

- **strategy** (<code>[str](#str)</code>) – strategy
- **parameterizers** (<code>[Any](#typing.Any)</code>) – parameterizers
- **numParameterizers** (<code>[int](#int)</code>) – numParameterizers

**Returns:**

- <code>[CompositeParameteriser](#swift2.classes.CompositeParameteriser)</code> – returned result

##### swift2.doc_helper.swg.ApplyConfiguration_py

```python
ApplyConfiguration_py(parameterizer, simulation)
```

ApplyConfiguration_py

ApplyConfiguration_py: generated wrapper function for API function ApplyConfiguration

**Parameters:**

- **parameterizer** (<code>[Any](#typing.Any)</code>) – parameterizer
- **simulation** (<code>[Simulation](#swift2.classes.Simulation)</code>) – simulation

##### swift2.doc_helper.swg.ApplyMemoryStates_py

```python
ApplyMemoryStates_py(simulation, memoryStates)
```

ApplyMemoryStates_py

ApplyMemoryStates_py: generated wrapper function for API function ApplyMemoryStates

**Parameters:**

- **simulation** (<code>[Simulation](#swift2.classes.Simulation)</code>) – simulation
- **memoryStates** (<code>[MemoryStates](#swift2.classes.MemoryStates)</code>) – memoryStates

##### swift2.doc_helper.swg.CalibrateERRISStageFour_py

```python
CalibrateERRISStageFour_py(calibObject, previousStage, useRising)
```

CalibrateERRISStageFour_py

CalibrateERRISStageFour_py: generated wrapper function for API function CalibrateERRISStageFour

**Parameters:**

- **calibObject** (<code>[ErrisStagedCalibration](#swift2.classes.ErrisStagedCalibration)</code>) – calibObject
- **previousStage** (<code>[HypercubeParameteriser](#swift2.classes.HypercubeParameteriser)</code>) – previousStage
- **useRising** (<code>[bool](#bool)</code>) – useRising

**Returns:**

- <code>[HypercubeParameteriser](#swift2.classes.HypercubeParameteriser)</code> – returned result

##### swift2.doc_helper.swg.CalibrateERRISStageOne_py

```python
CalibrateERRISStageOne_py(calibObject)
```

CalibrateERRISStageOne_py

CalibrateERRISStageOne_py: generated wrapper function for API function CalibrateERRISStageOne

**Parameters:**

- **calibObject** (<code>[ErrisStagedCalibration](#swift2.classes.ErrisStagedCalibration)</code>) – calibObject

**Returns:**

- <code>[HypercubeParameteriser](#swift2.classes.HypercubeParameteriser)</code> – returned result

##### swift2.doc_helper.swg.CalibrateERRISStageThreeMS_py

```python
CalibrateERRISStageThreeMS_py(calibObject, previousStage)
```

CalibrateERRISStageThreeMS_py

CalibrateERRISStageThreeMS_py: generated wrapper function for API function CalibrateERRISStageThreeMS

**Parameters:**

- **calibObject** (<code>[ErrisStagedCalibration](#swift2.classes.ErrisStagedCalibration)</code>) – calibObject
- **previousStage** (<code>[HypercubeParameteriser](#swift2.classes.HypercubeParameteriser)</code>) – previousStage

**Returns:**

- <code>[HypercubeParameteriser](#swift2.classes.HypercubeParameteriser)</code> – returned result

##### swift2.doc_helper.swg.CalibrateERRISStageThree_py

```python
CalibrateERRISStageThree_py(calibObject, previousStage)
```

CalibrateERRISStageThree_py

CalibrateERRISStageThree_py: generated wrapper function for API function CalibrateERRISStageThree

**Parameters:**

- **calibObject** (<code>[ErrisStagedCalibration](#swift2.classes.ErrisStagedCalibration)</code>) – calibObject
- **previousStage** (<code>[HypercubeParameteriser](#swift2.classes.HypercubeParameteriser)</code>) – previousStage

**Returns:**

- <code>[HypercubeParameteriser](#swift2.classes.HypercubeParameteriser)</code> – returned result

##### swift2.doc_helper.swg.CalibrateERRISStageTwo_py

```python
CalibrateERRISStageTwo_py(calibObject, previousStage)
```

CalibrateERRISStageTwo_py

CalibrateERRISStageTwo_py: generated wrapper function for API function CalibrateERRISStageTwo

**Parameters:**

- **calibObject** (<code>[ErrisStagedCalibration](#swift2.classes.ErrisStagedCalibration)</code>) – calibObject
- **previousStage** (<code>[HypercubeParameteriser](#swift2.classes.HypercubeParameteriser)</code>) – previousStage

**Returns:**

- <code>[HypercubeParameteriser](#swift2.classes.HypercubeParameteriser)</code> – returned result

##### swift2.doc_helper.swg.CalibrateMAERRISStageFour_py

```python
CalibrateMAERRISStageFour_py(calibObject, previousStage, useRising)
```

CalibrateMAERRISStageFour_py

CalibrateMAERRISStageFour_py: generated wrapper function for API function CalibrateMAERRISStageFour

**Parameters:**

- **calibObject** (<code>[MaerrisStagedCalibration](#swift2.classes.MaerrisStagedCalibration)</code>) – calibObject
- **previousStage** (<code>[HypercubeParameteriser](#swift2.classes.HypercubeParameteriser)</code>) – previousStage
- **useRising** (<code>[bool](#bool)</code>) – useRising

**Returns:**

- <code>[HypercubeParameteriser](#swift2.classes.HypercubeParameteriser)</code> – returned result

##### swift2.doc_helper.swg.CalibrateMAERRISStageOne_py

```python
CalibrateMAERRISStageOne_py(calibObject)
```

CalibrateMAERRISStageOne_py

CalibrateMAERRISStageOne_py: generated wrapper function for API function CalibrateMAERRISStageOne

**Parameters:**

- **calibObject** (<code>[MaerrisStagedCalibration](#swift2.classes.MaerrisStagedCalibration)</code>) – calibObject

**Returns:**

- <code>[HypercubeParameteriser](#swift2.classes.HypercubeParameteriser)</code> – returned result

##### swift2.doc_helper.swg.CalibrateMAERRISStageThreeMS_py

```python
CalibrateMAERRISStageThreeMS_py(calibObject, previousStage)
```

CalibrateMAERRISStageThreeMS_py

CalibrateMAERRISStageThreeMS_py: generated wrapper function for API function CalibrateMAERRISStageThreeMS

**Parameters:**

- **calibObject** (<code>[MaerrisStagedCalibration](#swift2.classes.MaerrisStagedCalibration)</code>) – calibObject
- **previousStage** (<code>[HypercubeParameteriser](#swift2.classes.HypercubeParameteriser)</code>) – previousStage

**Returns:**

- <code>[HypercubeParameteriser](#swift2.classes.HypercubeParameteriser)</code> – returned result

##### swift2.doc_helper.swg.CalibrateMAERRISStageThree_py

```python
CalibrateMAERRISStageThree_py(calibObject, previousStage)
```

CalibrateMAERRISStageThree_py

CalibrateMAERRISStageThree_py: generated wrapper function for API function CalibrateMAERRISStageThree

**Parameters:**

- **calibObject** (<code>[MaerrisStagedCalibration](#swift2.classes.MaerrisStagedCalibration)</code>) – calibObject
- **previousStage** (<code>[HypercubeParameteriser](#swift2.classes.HypercubeParameteriser)</code>) – previousStage

**Returns:**

- <code>[HypercubeParameteriser](#swift2.classes.HypercubeParameteriser)</code> – returned result

##### swift2.doc_helper.swg.CalibrateMAERRISStageTwo_py

```python
CalibrateMAERRISStageTwo_py(calibObject, previousStage)
```

CalibrateMAERRISStageTwo_py

CalibrateMAERRISStageTwo_py: generated wrapper function for API function CalibrateMAERRISStageTwo

**Parameters:**

- **calibObject** (<code>[MaerrisStagedCalibration](#swift2.classes.MaerrisStagedCalibration)</code>) – calibObject
- **previousStage** (<code>[HypercubeParameteriser](#swift2.classes.HypercubeParameteriser)</code>) – previousStage

**Returns:**

- <code>[HypercubeParameteriser](#swift2.classes.HypercubeParameteriser)</code> – returned result

##### swift2.doc_helper.swg.CheckSimulationErrors_py

```python
CheckSimulationErrors_py(simulation)
```

CheckSimulationErrors_py

CheckSimulationErrors_py: generated wrapper function for API function CheckSimulationErrors

##### swift2.doc_helper.swg.ClearMemoryStates_py

```python
ClearMemoryStates_py(simulation)
```

ClearMemoryStates_py

ClearMemoryStates_py: generated wrapper function for API function ClearMemoryStates

**Parameters:**

- **simulation** (<code>[Simulation](#swift2.classes.Simulation)</code>) – simulation

##### swift2.doc_helper.swg.CloneHypercubeParameterizer_py

```python
CloneHypercubeParameterizer_py(hypercubeParameterizer)
```

CloneHypercubeParameterizer_py

CloneHypercubeParameterizer_py: generated wrapper function for API function CloneHypercubeParameterizer

**Parameters:**

- **hypercubeParameterizer** (<code>[HypercubeParameteriser](#swift2.classes.HypercubeParameteriser)</code>) – hypercubeParameterizer

**Returns:**

- <code>[HypercubeParameteriser](#swift2.classes.HypercubeParameteriser)</code> – returned result

##### swift2.doc_helper.swg.CloneModel_py

```python
CloneModel_py(simulation)
```

CloneModel_py

CloneModel_py: generated wrapper function for API function CloneModel

**Parameters:**

- **simulation** (<code>[Simulation](#swift2.classes.Simulation)</code>) – simulation

**Returns:**

- <code>[Simulation](#swift2.classes.Simulation)</code> – returned result

##### swift2.doc_helper.swg.CloneObjectiveEvaluator_py

```python
CloneObjectiveEvaluator_py(objectiveEvaluator, simulation)
```

CloneObjectiveEvaluator_py

CloneObjectiveEvaluator_py: generated wrapper function for API function CloneObjectiveEvaluator

**Parameters:**

- **objectiveEvaluator** (<code>[DeletableCffiNativeHandle](#refcount.interop.DeletableCffiNativeHandle)</code>) – objectiveEvaluator
- **simulation** (<code>[Simulation](#swift2.classes.Simulation)</code>) – simulation

**Returns:**

- <code>[DeletableCffiNativeHandle](#refcount.interop.DeletableCffiNativeHandle)</code> – returned result

##### swift2.doc_helper.swg.CloneStateInitializer_py

```python
CloneStateInitializer_py(stateInitializer)
```

CloneStateInitializer_py

CloneStateInitializer_py: generated wrapper function for API function CloneStateInitializer

**Parameters:**

- **stateInitializer** (<code>[StateInitialiser](#swift2.classes.StateInitialiser)</code>) – stateInitializer

**Returns:**

- <code>[StateInitialiser](#swift2.classes.StateInitialiser)</code> – returned result

##### swift2.doc_helper.swg.ConcatenateERRISStagesParameters_py

```python
ConcatenateERRISStagesParameters_py(calibObject, hydroParams, stage1_result, stage2_result, stage3_result, stage4a_result, stage4b_result, toLongParameterName)
```

ConcatenateERRISStagesParameters_py

ConcatenateERRISStagesParameters_py: generated wrapper function for API function ConcatenateERRISStagesParameters

**Parameters:**

- **calibObject** (<code>[ErrisStagedCalibration](#swift2.classes.ErrisStagedCalibration)</code>) – calibObject
- **hydroParams** (<code>[HypercubeParameteriser](#swift2.classes.HypercubeParameteriser)</code>) – hydroParams
- **stage1_result** (<code>[HypercubeParameteriser](#swift2.classes.HypercubeParameteriser)</code>) – stage1_result
- **stage2_result** (<code>[HypercubeParameteriser](#swift2.classes.HypercubeParameteriser)</code>) – stage2_result
- **stage3_result** (<code>[HypercubeParameteriser](#swift2.classes.HypercubeParameteriser)</code>) – stage3_result
- **stage4a_result** (<code>[HypercubeParameteriser](#swift2.classes.HypercubeParameteriser)</code>) – stage4a_result
- **stage4b_result** (<code>[HypercubeParameteriser](#swift2.classes.HypercubeParameteriser)</code>) – stage4b_result
- **toLongParameterName** (<code>[bool](#bool)</code>) – toLongParameterName

**Returns:**

- <code>[HypercubeParameteriser](#swift2.classes.HypercubeParameteriser)</code> – returned result

##### swift2.doc_helper.swg.ConcatenateMAERRISStagesParameters_py

```python
ConcatenateMAERRISStagesParameters_py(calibObject, hydroParams, stage1_result, stage2_result, stage3_result, stage4a_result, stage4b_result, toLongParameterName)
```

ConcatenateMAERRISStagesParameters_py

ConcatenateMAERRISStagesParameters_py: generated wrapper function for API function ConcatenateMAERRISStagesParameters

**Parameters:**

- **calibObject** (<code>[MaerrisStagedCalibration](#swift2.classes.MaerrisStagedCalibration)</code>) – calibObject
- **hydroParams** (<code>[HypercubeParameteriser](#swift2.classes.HypercubeParameteriser)</code>) – hydroParams
- **stage1_result** (<code>[HypercubeParameteriser](#swift2.classes.HypercubeParameteriser)</code>) – stage1_result
- **stage2_result** (<code>[HypercubeParameteriser](#swift2.classes.HypercubeParameteriser)</code>) – stage2_result
- **stage3_result** (<code>[HypercubeParameteriser](#swift2.classes.HypercubeParameteriser)</code>) – stage3_result
- **stage4a_result** (<code>[HypercubeParameteriser](#swift2.classes.HypercubeParameteriser)</code>) – stage4a_result
- **stage4b_result** (<code>[HypercubeParameteriser](#swift2.classes.HypercubeParameteriser)</code>) – stage4b_result
- **toLongParameterName** (<code>[bool](#bool)</code>) – toLongParameterName

**Returns:**

- <code>[HypercubeParameteriser](#swift2.classes.HypercubeParameteriser)</code> – returned result

##### swift2.doc_helper.swg.CreateCandidateFactorySeedWila_py

```python
CreateCandidateFactorySeedWila_py(hypercubeParameterizer, type, seed)
```

CreateCandidateFactorySeedWila_py

CreateCandidateFactorySeedWila_py: generated wrapper function for API function CreateCandidateFactorySeedWila

**Parameters:**

- **hypercubeParameterizer** (<code>[HypercubeParameteriser](#swift2.classes.HypercubeParameteriser)</code>) – hypercubeParameterizer
- **type** (<code>[str](#str)</code>) – type
- **seed** (<code>[int](#int)</code>) – seed

**Returns:**

- <code>[CandidateFactorySeed](#swift2.classes.CandidateFactorySeed)</code> – returned result

##### swift2.doc_helper.swg.CreateCatchment_py

```python
CreateCatchment_py(numNodes, nodeIds, nodeNames, numLinks, linkIds, linkNames, linkFromNode, linkToNode, runoffModelName, areasKm2)
```

CreateCatchment_py

CreateCatchment_py: generated wrapper function for API function CreateCatchment

**Parameters:**

- **numNodes** (<code>[int](#int)</code>) – numNodes
- **nodeIds** (<code>[List](#typing.List)\[[str](#str)\]</code>) – nodeIds
- **nodeNames** (<code>[List](#typing.List)\[[str](#str)\]</code>) – nodeNames
- **numLinks** (<code>[int](#int)</code>) – numLinks
- **linkIds** (<code>[List](#typing.List)\[[str](#str)\]</code>) – linkIds
- **linkNames** (<code>[List](#typing.List)\[[str](#str)\]</code>) – linkNames
- **linkFromNode** (<code>[List](#typing.List)\[[str](#str)\]</code>) – linkFromNode
- **linkToNode** (<code>[List](#typing.List)\[[str](#str)\]</code>) – linkToNode
- **runoffModelName** (<code>[str](#str)</code>) – runoffModelName
- **areasKm2** (<code>[ndarray](#numpy.ndarray)</code>) – areasKm2

**Returns:**

- <code>[Simulation](#swift2.classes.Simulation)</code> – returned result

##### swift2.doc_helper.swg.CreateCompositeObservationObjectiveEvaluator_py

```python
CreateCompositeObservationObjectiveEvaluator_py(simulation, obsVarId, observations, obsGeom, yamlStatIdString)
```

CreateCompositeObservationObjectiveEvaluator_py

CreateCompositeObservationObjectiveEvaluator_py: generated wrapper function for API function CreateCompositeObservationObjectiveEvaluator

**Parameters:**

- **simulation** (<code>[Simulation](#swift2.classes.Simulation)</code>) – simulation
- **obsVarId** (<code>[str](#str)</code>) – obsVarId
- **observations** (<code>[ndarray](#numpy.ndarray)</code>) – observations
- **obsGeom** (<code>[TimeSeriesGeometryNative](#cinterop.cffi.marshal.TimeSeriesGeometryNative)</code>) – obsGeom
- **yamlStatIdString** (<code>[str](#str)</code>) – yamlStatIdString

**Returns:**

- <code>[DeletableCffiNativeHandle](#refcount.interop.DeletableCffiNativeHandle)</code> – returned result

##### swift2.doc_helper.swg.CreateCompositeParameterizer_py

```python
CreateCompositeParameterizer_py()
```

CreateCompositeParameterizer_py

CreateCompositeParameterizer_py: generated wrapper function for API function CreateCompositeParameterizer

Args:

**Returns:**

- <code>[CompositeParameteriser](#swift2.classes.CompositeParameteriser)</code> – returned result

##### swift2.doc_helper.swg.CreateERRISParameterEstimator_py

```python
CreateERRISParameterEstimator_py(mr, obsValues, obsGeom, errorModelElementId, estimationStart, estimationEnd, censThr, censOpt, terminationCondition, restrictionOn, weightedLeastSquare)
```

CreateERRISParameterEstimator_py

CreateERRISParameterEstimator_py: generated wrapper function for API function CreateERRISParameterEstimator

**Parameters:**

- **mr** (<code>[Simulation](#swift2.classes.Simulation)</code>) – mr
- **obsValues** (<code>[ndarray](#numpy.ndarray)</code>) – obsValues
- **obsGeom** (<code>[TimeSeriesGeometryNative](#cinterop.cffi.marshal.TimeSeriesGeometryNative)</code>) – obsGeom
- **errorModelElementId** (<code>[str](#str)</code>) – errorModelElementId
- **estimationStart** (<code>[datetime](#datetime.datetime)</code>) – estimationStart
- **estimationEnd** (<code>[datetime](#datetime.datetime)</code>) – estimationEnd
- **censThr** (<code>[float](#float)</code>) – censThr
- **censOpt** (<code>[float](#float)</code>) – censOpt
- **terminationCondition** (<code>[SceTerminationCondition](#swift2.classes.SceTerminationCondition)</code>) – terminationCondition
- **restrictionOn** (<code>[bool](#bool)</code>) – restrictionOn
- **weightedLeastSquare** (<code>[bool](#bool)</code>) – weightedLeastSquare

**Returns:**

- <code>[ErrisStagedCalibration](#swift2.classes.ErrisStagedCalibration)</code> – returned result

##### swift2.doc_helper.swg.CreateEmptyCompositeObjectiveEvaluator_py

```python
CreateEmptyCompositeObjectiveEvaluator_py()
```

CreateEmptyCompositeObjectiveEvaluator_py

CreateEmptyCompositeObjectiveEvaluator_py: generated wrapper function for API function CreateEmptyCompositeObjectiveEvaluator

Args:

**Returns:**

- <code>[DeletableCffiNativeHandle](#refcount.interop.DeletableCffiNativeHandle)</code> – returned result

##### swift2.doc_helper.swg.CreateEnsembleForecastSimulation_py

```python
CreateEnsembleForecastSimulation_py(simulation, start, leadTime, ensembleSize, simulationLength, nTimeStepsBetweenForecasts)
```

CreateEnsembleForecastSimulation_py

CreateEnsembleForecastSimulation_py: generated wrapper function for API function CreateEnsembleForecastSimulation

**Parameters:**

- **simulation** (<code>[Simulation](#swift2.classes.Simulation)</code>) – simulation
- **start** (<code>[datetime](#datetime.datetime)</code>) – start
- **leadTime** (<code>[int](#int)</code>) – leadTime
- **ensembleSize** (<code>[int](#int)</code>) – ensembleSize
- **simulationLength** (<code>[int](#int)</code>) – simulationLength
- **nTimeStepsBetweenForecasts** (<code>[int](#int)</code>) – nTimeStepsBetweenForecasts

**Returns:**

- <code>[EnsembleForecastSimulation](#swift2.classes.EnsembleForecastSimulation)</code> – returned result

##### swift2.doc_helper.swg.CreateEnsembleModelRunner_py

```python
CreateEnsembleModelRunner_py(simulation, ensembleSize)
```

CreateEnsembleModelRunner_py

CreateEnsembleModelRunner_py: generated wrapper function for API function CreateEnsembleModelRunner

**Parameters:**

- **simulation** (<code>[Simulation](#swift2.classes.Simulation)</code>) – simulation
- **ensembleSize** (<code>[int](#int)</code>) – ensembleSize

**Returns:**

- <code>[EnsembleSimulation](#swift2.classes.EnsembleSimulation)</code> – returned result

##### swift2.doc_helper.swg.CreateFilteringParameterizer_py

```python
CreateFilteringParameterizer_py(p)
```

CreateFilteringParameterizer_py

CreateFilteringParameterizer_py: generated wrapper function for API function CreateFilteringParameterizer

**Parameters:**

- **p** (<code>[HypercubeParameteriser](#swift2.classes.HypercubeParameteriser)</code>) – p

**Returns:**

- <code>[FilteringParameteriser](#swift2.classes.FilteringParameteriser)</code> – returned result

##### swift2.doc_helper.swg.CreateFunctionsParameterizer_py

```python
CreateFunctionsParameterizer_py(modelParameters, functionsParameters)
```

CreateFunctionsParameterizer_py

CreateFunctionsParameterizer_py: generated wrapper function for API function CreateFunctionsParameterizer

**Parameters:**

- **modelParameters** (<code>[HypercubeParameteriser](#swift2.classes.HypercubeParameteriser)</code>) – modelParameters
- **functionsParameters** (<code>[HypercubeParameteriser](#swift2.classes.HypercubeParameteriser)</code>) – functionsParameters

**Returns:**

- <code>[FunctionsParameteriser](#swift2.classes.FunctionsParameteriser)</code> – returned result

##### swift2.doc_helper.swg.CreateGr4ScaledParameterizer_py

```python
CreateGr4ScaledParameterizer_py(referenceAreaKm2, tStepSeconds)
```

CreateGr4ScaledParameterizer_py

CreateGr4ScaledParameterizer_py: generated wrapper function for API function CreateGr4ScaledParameterizer

**Parameters:**

- **referenceAreaKm2** (<code>[float](#float)</code>) – referenceAreaKm2
- **tStepSeconds** (<code>[int](#int)</code>) – tStepSeconds

**Returns:**

- <code>[CompositeParameteriser](#swift2.classes.CompositeParameteriser)</code> – returned result

##### swift2.doc_helper.swg.CreateHypercubeParameterizer_py

```python
CreateHypercubeParameterizer_py(strategy)
```

CreateHypercubeParameterizer_py

CreateHypercubeParameterizer_py: generated wrapper function for API function CreateHypercubeParameterizer

**Parameters:**

- **strategy** (<code>[str](#str)</code>) – strategy

**Returns:**

- <code>[HypercubeParameteriser](#swift2.classes.HypercubeParameteriser)</code> – returned result

##### swift2.doc_helper.swg.CreateLinearFuncParameterizer_py

```python
CreateLinearFuncParameterizer_py(paramName, innerParamName, observedState, constant, min, max, value, selectorType)
```

CreateLinearFuncParameterizer_py

CreateLinearFuncParameterizer_py: generated wrapper function for API function CreateLinearFuncParameterizer

**Parameters:**

- **paramName** (<code>[str](#str)</code>) – paramName
- **innerParamName** (<code>[str](#str)</code>) – innerParamName
- **observedState** (<code>[str](#str)</code>) – observedState
- **constant** (<code>[float](#float)</code>) – constant
- **min** (<code>[float](#float)</code>) – min
- **max** (<code>[float](#float)</code>) – max
- **value** (<code>[float](#float)</code>) – value
- **selectorType** (<code>[str](#str)</code>) – selectorType

**Returns:**

- <code>[ScalingParameteriser](#swift2.classes.ScalingParameteriser)</code> – returned result

##### swift2.doc_helper.swg.CreateMAERRISParameterEstimator_py

```python
CreateMAERRISParameterEstimator_py(mr, obsValues, obsGeom, errorModelElementId, estimationStart, estimationEnd, s2Window, censThr, censOpt, terminationCondition, restrictionOn)
```

CreateMAERRISParameterEstimator_py

CreateMAERRISParameterEstimator_py: generated wrapper function for API function CreateMAERRISParameterEstimator

**Parameters:**

- **mr** (<code>[Simulation](#swift2.classes.Simulation)</code>) – mr
- **obsValues** (<code>[ndarray](#numpy.ndarray)</code>) – obsValues
- **obsGeom** (<code>[TimeSeriesGeometryNative](#cinterop.cffi.marshal.TimeSeriesGeometryNative)</code>) – obsGeom
- **errorModelElementId** (<code>[str](#str)</code>) – errorModelElementId
- **estimationStart** (<code>[datetime](#datetime.datetime)</code>) – estimationStart
- **estimationEnd** (<code>[datetime](#datetime.datetime)</code>) – estimationEnd
- **s2Window** (<code>[float](#float)</code>) – s2Window
- **censThr** (<code>[float](#float)</code>) – censThr
- **censOpt** (<code>[float](#float)</code>) – censOpt
- **terminationCondition** (<code>[SceTerminationCondition](#swift2.classes.SceTerminationCondition)</code>) – terminationCondition
- **restrictionOn** (<code>[bool](#bool)</code>) – restrictionOn

**Returns:**

- <code>[MaerrisStagedCalibration](#swift2.classes.MaerrisStagedCalibration)</code> – returned result

##### swift2.doc_helper.swg.CreateMultisiteObjectiveEvaluator_py

```python
CreateMultisiteObjectiveEvaluator_py(simulation, defn, weights)
```

CreateMultisiteObjectiveEvaluator_py

CreateMultisiteObjectiveEvaluator_py: generated wrapper function for API function CreateMultisiteObjectiveEvaluator

**Parameters:**

- **simulation** (<code>[Simulation](#swift2.classes.Simulation)</code>) – simulation
- **defn** (<code>[Any](#typing.Any)</code>) – defn
- **weights** (<code>[Dict](#typing.Dict)\[[str](#str), [float](#float)\]</code>) – weights

**Returns:**

- <code>[DeletableCffiNativeHandle](#refcount.interop.DeletableCffiNativeHandle)</code> – returned result

##### swift2.doc_helper.swg.CreateMuskingumConstraint_py

```python
CreateMuskingumConstraint_py(hypercubeParameterizer, deltaTHours, paramNameK, paramNameX, simulation)
```

CreateMuskingumConstraint_py

CreateMuskingumConstraint_py: generated wrapper function for API function CreateMuskingumConstraint

**Parameters:**

- **hypercubeParameterizer** (<code>[HypercubeParameteriser](#swift2.classes.HypercubeParameteriser)</code>) – hypercubeParameterizer
- **deltaTHours** (<code>[float](#float)</code>) – deltaTHours
- **paramNameK** (<code>[str](#str)</code>) – paramNameK
- **paramNameX** (<code>[str](#str)</code>) – paramNameX
- **simulation** (<code>[Simulation](#swift2.classes.Simulation)</code>) – simulation

**Returns:**

- <code>[ConstraintParameteriser](#swift2.classes.ConstraintParameteriser)</code> – returned result

##### swift2.doc_helper.swg.CreateNewFromNetworkInfo_py

```python
CreateNewFromNetworkInfo_py(nodes, numNodes, links, numLinks)
```

CreateNewFromNetworkInfo_py

CreateNewFromNetworkInfo_py: generated wrapper function for API function CreateNewFromNetworkInfo

**Parameters:**

- **nodes** (<code>[Any](#typing.Any)</code>) – nodes
- **numNodes** (<code>[int](#int)</code>) – numNodes
- **links** (<code>[Any](#typing.Any)</code>) – links
- **numLinks** (<code>[int](#int)</code>) – numLinks

**Returns:**

- <code>[Simulation](#swift2.classes.Simulation)</code> – returned result

##### swift2.doc_helper.swg.CreateOptimizerWila_py

```python
CreateOptimizerWila_py(objective, parameterizer, parameters)
```

CreateOptimizerWila_py

CreateOptimizerWila_py: generated wrapper function for API function CreateOptimizerWila

**Parameters:**

- **objective** (<code>[ObjectiveEvaluator](#swift2.classes.ObjectiveEvaluator)</code>) – objective
- **parameterizer** (<code>[HypercubeParameteriser](#swift2.classes.HypercubeParameteriser)</code>) – parameterizer
- **parameters** (<code>[Dict](#typing.Dict)\[[str](#str), [str](#str)\]</code>) – parameters

**Returns:**

- <code>[Optimiser](#swift2.classes.Optimiser)</code> – returned result

##### swift2.doc_helper.swg.CreatePrefixingParameterizer_py

```python
CreatePrefixingParameterizer_py(p, prefix)
```

CreatePrefixingParameterizer_py

CreatePrefixingParameterizer_py: generated wrapper function for API function CreatePrefixingParameterizer

**Parameters:**

- **p** (<code>[HypercubeParameteriser](#swift2.classes.HypercubeParameteriser)</code>) – p
- **prefix** (<code>[str](#str)</code>) – prefix

**Returns:**

- <code>[HypercubeParameteriser](#swift2.classes.HypercubeParameteriser)</code> – returned result

##### swift2.doc_helper.swg.CreateSceMarginalTerminationWila_py

```python
CreateSceMarginalTerminationWila_py(tolerance, cutoffNoImprovement, maxHours)
```

CreateSceMarginalTerminationWila_py

CreateSceMarginalTerminationWila_py: generated wrapper function for API function CreateSceMarginalTerminationWila

**Parameters:**

- **tolerance** (<code>[float](#float)</code>) – tolerance
- **cutoffNoImprovement** (<code>[int](#int)</code>) – cutoffNoImprovement
- **maxHours** (<code>[float](#float)</code>) – maxHours

**Returns:**

- <code>[SceTerminationCondition](#swift2.classes.SceTerminationCondition)</code> – returned result

##### swift2.doc_helper.swg.CreateSceMaxIterationTerminationWila_py

```python
CreateSceMaxIterationTerminationWila_py(maxIterations)
```

CreateSceMaxIterationTerminationWila_py

CreateSceMaxIterationTerminationWila_py: generated wrapper function for API function CreateSceMaxIterationTerminationWila

**Parameters:**

- **maxIterations** (<code>[int](#int)</code>) – maxIterations

**Returns:**

- <code>[SceTerminationCondition](#swift2.classes.SceTerminationCondition)</code> – returned result

##### swift2.doc_helper.swg.CreateSceMaxRuntimeTerminationWila_py

```python
CreateSceMaxRuntimeTerminationWila_py(maxHours)
```

CreateSceMaxRuntimeTerminationWila_py

CreateSceMaxRuntimeTerminationWila_py: generated wrapper function for API function CreateSceMaxRuntimeTerminationWila

**Parameters:**

- **maxHours** (<code>[float](#float)</code>) – maxHours

**Returns:**

- <code>[SceTerminationCondition](#swift2.classes.SceTerminationCondition)</code> – returned result

##### swift2.doc_helper.swg.CreateSceTerminationWila_py

```python
CreateSceTerminationWila_py(type, arguments, numArguments)
```

CreateSceTerminationWila_py

CreateSceTerminationWila_py: generated wrapper function for API function CreateSceTerminationWila

**Parameters:**

- **type** (<code>[str](#str)</code>) – type
- **arguments** (<code>[List](#typing.List)\[[str](#str)\]</code>) – arguments
- **numArguments** (<code>[int](#int)</code>) – numArguments

**Returns:**

- <code>[SceTerminationCondition](#swift2.classes.SceTerminationCondition)</code> – returned result

##### swift2.doc_helper.swg.CreateShuffledComplexEvolutionWila_py

```python
CreateShuffledComplexEvolutionWila_py(objective, terminationCriterion, SCEpars, populationInitializer)
```

CreateShuffledComplexEvolutionWila_py

CreateShuffledComplexEvolutionWila_py: generated wrapper function for API function CreateShuffledComplexEvolutionWila

**Parameters:**

- **objective** (<code>[ObjectiveEvaluator](#swift2.classes.ObjectiveEvaluator)</code>) – objective
- **terminationCriterion** (<code>[SceTerminationCondition](#swift2.classes.SceTerminationCondition)</code>) – terminationCriterion
- **SCEpars** (<code>[Dict](#typing.Dict)\[[str](#str), [float](#float)\]</code>) – SCEpars
- **populationInitializer** (<code>[CandidateFactorySeed](#swift2.classes.CandidateFactorySeed)</code>) – populationInitializer

**Returns:**

- <code>[Optimiser](#swift2.classes.Optimiser)</code> – returned result

##### swift2.doc_helper.swg.CreateSingleObservationObjectiveEvaluatorWila_py

```python
CreateSingleObservationObjectiveEvaluatorWila_py(simulation, obsVarId, observations, obsGeom, statisticId)
```

CreateSingleObservationObjectiveEvaluatorWila_py

CreateSingleObservationObjectiveEvaluatorWila_py: generated wrapper function for API function CreateSingleObservationObjectiveEvaluatorWila

**Parameters:**

- **simulation** (<code>[Simulation](#swift2.classes.Simulation)</code>) – simulation
- **obsVarId** (<code>[str](#str)</code>) – obsVarId
- **observations** (<code>[ndarray](#numpy.ndarray)</code>) – observations
- **obsGeom** (<code>[TimeSeriesGeometryNative](#cinterop.cffi.marshal.TimeSeriesGeometryNative)</code>) – obsGeom
- **statisticId** (<code>[str](#str)</code>) – statisticId

**Returns:**

- <code>[ObjectiveEvaluator](#swift2.classes.ObjectiveEvaluator)</code> – returned result

##### swift2.doc_helper.swg.CreateSingleObservationObjectiveEvaluator_py

```python
CreateSingleObservationObjectiveEvaluator_py(simulation, obsVarId, observations, obsGeom, statisticId)
```

CreateSingleObservationObjectiveEvaluator_py

CreateSingleObservationObjectiveEvaluator_py: generated wrapper function for API function CreateSingleObservationObjectiveEvaluator

**Parameters:**

- **simulation** (<code>[Simulation](#swift2.classes.Simulation)</code>) – simulation
- **obsVarId** (<code>[str](#str)</code>) – obsVarId
- **observations** (<code>[ndarray](#numpy.ndarray)</code>) – observations
- **obsGeom** (<code>[TimeSeriesGeometryNative](#cinterop.cffi.marshal.TimeSeriesGeometryNative)</code>) – obsGeom
- **statisticId** (<code>[str](#str)</code>) – statisticId

**Returns:**

- <code>[DeletableCffiNativeHandle](#refcount.interop.DeletableCffiNativeHandle)</code> – returned result

##### swift2.doc_helper.swg.CreateSqrtAreaRatioParameterizer_py

```python
CreateSqrtAreaRatioParameterizer_py(referenceAreaKm2, paramName, innerParamName, min, max, value)
```

CreateSqrtAreaRatioParameterizer_py

CreateSqrtAreaRatioParameterizer_py: generated wrapper function for API function CreateSqrtAreaRatioParameterizer

**Parameters:**

- **referenceAreaKm2** (<code>[float](#float)</code>) – referenceAreaKm2
- **paramName** (<code>[str](#str)</code>) – paramName
- **innerParamName** (<code>[str](#str)</code>) – innerParamName
- **min** (<code>[float](#float)</code>) – min
- **max** (<code>[float](#float)</code>) – max
- **value** (<code>[float](#float)</code>) – value

**Returns:**

- <code>[DeletableCffiNativeHandle](#refcount.interop.DeletableCffiNativeHandle)</code> – returned result

##### swift2.doc_helper.swg.CreateStateInitParameterizer_py

```python
CreateStateInitParameterizer_py(hypercubeParameterizer)
```

CreateStateInitParameterizer_py

CreateStateInitParameterizer_py: generated wrapper function for API function CreateStateInitParameterizer

**Parameters:**

- **hypercubeParameterizer** (<code>[HypercubeParameteriser](#swift2.classes.HypercubeParameteriser)</code>) – hypercubeParameterizer

**Returns:**

- <code>[StateInitParameteriser](#swift2.classes.StateInitParameteriser)</code> – returned result

##### swift2.doc_helper.swg.CreateStateInitializer_py

```python
CreateStateInitializer_py(type)
```

CreateStateInitializer_py

CreateStateInitializer_py: generated wrapper function for API function CreateStateInitializer

**Parameters:**

- **type** (<code>[str](#str)</code>) – type

**Returns:**

- <code>[StateInitialiser](#swift2.classes.StateInitialiser)</code> – returned result

##### swift2.doc_helper.swg.CreateSubarea_py

```python
CreateSubarea_py(modelId, areaKm2)
```

CreateSubarea_py

CreateSubarea_py: generated wrapper function for API function CreateSubarea

**Parameters:**

- **modelId** (<code>[str](#str)</code>) – modelId
- **areaKm2** (<code>[float](#float)</code>) – areaKm2

**Returns:**

- <code>[Simulation](#swift2.classes.Simulation)</code> – returned result

##### swift2.doc_helper.swg.CreateSubcatchmentHypercubeParameterizer_py

```python
CreateSubcatchmentHypercubeParameterizer_py(parameterizer, subcatchment)
```

CreateSubcatchmentHypercubeParameterizer_py

CreateSubcatchmentHypercubeParameterizer_py: generated wrapper function for API function CreateSubcatchmentHypercubeParameterizer

**Parameters:**

- **parameterizer** (<code>[HypercubeParameteriser](#swift2.classes.HypercubeParameteriser)</code>) – parameterizer
- **subcatchment** (<code>[Simulation](#swift2.classes.Simulation)</code>) – subcatchment

**Returns:**

- <code>[HypercubeParameteriser](#swift2.classes.HypercubeParameteriser)</code> – returned result

##### swift2.doc_helper.swg.CreateTargetScalingParameterizer_py

```python
CreateTargetScalingParameterizer_py(selectorType)
```

CreateTargetScalingParameterizer_py

CreateTargetScalingParameterizer_py: generated wrapper function for API function CreateTargetScalingParameterizer

**Parameters:**

- **selectorType** (<code>[str](#str)</code>) – selectorType

**Returns:**

- <code>[ScalingParameteriser](#swift2.classes.ScalingParameteriser)</code> – returned result

##### swift2.doc_helper.swg.CreateTestMemoryTrackedParameterizer_py

```python
CreateTestMemoryTrackedParameterizer_py()
```

CreateTestMemoryTrackedParameterizer_py

CreateTestMemoryTrackedParameterizer_py: generated wrapper function for API function CreateTestMemoryTrackedParameterizer

Args:

**Returns:**

- <code>[HypercubeParameteriser](#swift2.classes.HypercubeParameteriser)</code> – returned result

##### swift2.doc_helper.swg.CreateTestMemoryTrackedSimulation_py

```python
CreateTestMemoryTrackedSimulation_py()
```

CreateTestMemoryTrackedSimulation_py

CreateTestMemoryTrackedSimulation_py: generated wrapper function for API function CreateTestMemoryTrackedSimulation

Args:

**Returns:**

- <code>[Simulation](#swift2.classes.Simulation)</code> – returned result

##### swift2.doc_helper.swg.CreateTransformParameterizer_py

```python
CreateTransformParameterizer_py(hypercubeParameterizer)
```

CreateTransformParameterizer_py

CreateTransformParameterizer_py: generated wrapper function for API function CreateTransformParameterizer

**Parameters:**

- **hypercubeParameterizer** (<code>[HypercubeParameteriser](#swift2.classes.HypercubeParameteriser)</code>) – hypercubeParameterizer

**Returns:**

- <code>[TransformParameteriser](#swift2.classes.TransformParameteriser)</code> – returned result

##### swift2.doc_helper.swg.DisposeCatchmentStructure_py

```python
DisposeCatchmentStructure_py(structure)
```

DisposeCatchmentStructure_py

DisposeCatchmentStructure_py: generated wrapper function for API function DisposeCatchmentStructure

**Parameters:**

- **structure** (<code>[DeletableCffiNativeHandle](#refcount.interop.DeletableCffiNativeHandle)</code>) – structure

##### swift2.doc_helper.swg.DisposeNamedValuedVectorsSwift_py

```python
DisposeNamedValuedVectorsSwift_py(v)
```

DisposeNamedValuedVectorsSwift_py

DisposeNamedValuedVectorsSwift_py: generated wrapper function for API function DisposeNamedValuedVectorsSwift

**Parameters:**

- **v** (<code>[Dict](#typing.Dict)\[[str](#str), [float](#float)\]</code>) – v

##### swift2.doc_helper.swg.DisposeOptimizerLogDataWila_py

```python
DisposeOptimizerLogDataWila_py(logData)
```

DisposeOptimizerLogDataWila_py

DisposeOptimizerLogDataWila_py: generated wrapper function for API function DisposeOptimizerLogDataWila

**Parameters:**

- **logData** (<code>[DeletableCffiNativeHandle](#refcount.interop.DeletableCffiNativeHandle)</code>) – logData

##### swift2.doc_helper.swg.DisposeSharedPointer_py

```python
DisposeSharedPointer_py(ptr)
```

DisposeSharedPointer_py

DisposeSharedPointer_py: generated wrapper function for API function DisposeSharedPointer

**Parameters:**

- **ptr** (<code>[Any](#typing.Any)</code>) – ptr

##### swift2.doc_helper.swg.DisposeStringStringMapSwift_py

```python
DisposeStringStringMapSwift_py(v)
```

DisposeStringStringMapSwift_py

DisposeStringStringMapSwift_py: generated wrapper function for API function DisposeStringStringMapSwift

**Parameters:**

- **v** (<code>[Dict](#typing.Dict)\[[str](#str), [str](#str)\]</code>) – v

##### swift2.doc_helper.swg.EstimateDualPassParameters_py

```python
EstimateDualPassParameters_py(simulation, obsValues, obsGeom, errorModelElementId, warmupStart, warmupEnd, warmup, estimationStart, estimationEnd, windowL, windowDecayL, windowDecayS, useLongPass, objFuncDescYaml, exclusionStart, exclusionEnd, exclusion, terminationCondition)
```

EstimateDualPassParameters_py

EstimateDualPassParameters_py: generated wrapper function for API function EstimateDualPassParameters

**Parameters:**

- **simulation** (<code>[Simulation](#swift2.classes.Simulation)</code>) – simulation
- **obsValues** (<code>[ndarray](#numpy.ndarray)</code>) – obsValues
- **obsGeom** (<code>[TimeSeriesGeometryNative](#cinterop.cffi.marshal.TimeSeriesGeometryNative)</code>) – obsGeom
- **errorModelElementId** (<code>[str](#str)</code>) – errorModelElementId
- **warmupStart** (<code>[datetime](#datetime.datetime)</code>) – warmupStart
- **warmupEnd** (<code>[datetime](#datetime.datetime)</code>) – warmupEnd
- **warmup** (<code>[bool](#bool)</code>) – warmup
- **estimationStart** (<code>[datetime](#datetime.datetime)</code>) – estimationStart
- **estimationEnd** (<code>[datetime](#datetime.datetime)</code>) – estimationEnd
- **windowL** (<code>[int](#int)</code>) – windowL
- **windowDecayL** (<code>[int](#int)</code>) – windowDecayL
- **windowDecayS** (<code>[int](#int)</code>) – windowDecayS
- **useLongPass** (<code>[bool](#bool)</code>) – useLongPass
- **objFuncDescYaml** (<code>[str](#str)</code>) – objFuncDescYaml
- **exclusionStart** (<code>[datetime](#datetime.datetime)</code>) – exclusionStart
- **exclusionEnd** (<code>[datetime](#datetime.datetime)</code>) – exclusionEnd
- **exclusion** (<code>[bool](#bool)</code>) – exclusion
- **terminationCondition** (<code>[SceTerminationCondition](#swift2.classes.SceTerminationCondition)</code>) – terminationCondition

**Returns:**

- <code>[HypercubeParameteriser](#swift2.classes.HypercubeParameteriser)</code> – returned result

##### swift2.doc_helper.swg.EstimateERRISParameters_py

```python
EstimateERRISParameters_py(simulation, obsValues, obsGeom, errorModelElementId, warmupStart, warmupEnd, warmup, estimationStart, estimationEnd, censThr, censOpt, exclusionStart, exclusionEnd, exclusion, terminationCondition, errisParams, hydroParams, restrictionOn, weightedLeastSquare)
```

EstimateERRISParameters_py

EstimateERRISParameters_py: generated wrapper function for API function EstimateERRISParameters

**Parameters:**

- **simulation** (<code>[Simulation](#swift2.classes.Simulation)</code>) – simulation
- **obsValues** (<code>[ndarray](#numpy.ndarray)</code>) – obsValues
- **obsGeom** (<code>[TimeSeriesGeometryNative](#cinterop.cffi.marshal.TimeSeriesGeometryNative)</code>) – obsGeom
- **errorModelElementId** (<code>[str](#str)</code>) – errorModelElementId
- **warmupStart** (<code>[datetime](#datetime.datetime)</code>) – warmupStart
- **warmupEnd** (<code>[datetime](#datetime.datetime)</code>) – warmupEnd
- **warmup** (<code>[bool](#bool)</code>) – warmup
- **estimationStart** (<code>[datetime](#datetime.datetime)</code>) – estimationStart
- **estimationEnd** (<code>[datetime](#datetime.datetime)</code>) – estimationEnd
- **censThr** (<code>[float](#float)</code>) – censThr
- **censOpt** (<code>[float](#float)</code>) – censOpt
- **exclusionStart** (<code>[datetime](#datetime.datetime)</code>) – exclusionStart
- **exclusionEnd** (<code>[datetime](#datetime.datetime)</code>) – exclusionEnd
- **exclusion** (<code>[bool](#bool)</code>) – exclusion
- **terminationCondition** (<code>[SceTerminationCondition](#swift2.classes.SceTerminationCondition)</code>) – terminationCondition
- **errisParams** (<code>[HypercubeParameteriser](#swift2.classes.HypercubeParameteriser)</code>) – errisParams
- **hydroParams** (<code>[HypercubeParameteriser](#swift2.classes.HypercubeParameteriser)</code>) – hydroParams
- **restrictionOn** (<code>[bool](#bool)</code>) – restrictionOn
- **weightedLeastSquare** (<code>[bool](#bool)</code>) – weightedLeastSquare

**Returns:**

- <code>[HypercubeParameteriser](#swift2.classes.HypercubeParameteriser)</code> – returned result

##### swift2.doc_helper.swg.EstimateMAERRISParameters_py

```python
EstimateMAERRISParameters_py(simulation, obsValues, obsGeom, errorModelElementId, warmupStart, warmupEnd, warmup, estimationStart, estimationEnd, s2Window, censThr, censOpt, exclusionStart, exclusionEnd, exclusion, terminationCondition, maerrisParams, hydroParams, restrictionOn)
```

EstimateMAERRISParameters_py

EstimateMAERRISParameters_py: generated wrapper function for API function EstimateMAERRISParameters

**Parameters:**

- **simulation** (<code>[Simulation](#swift2.classes.Simulation)</code>) – simulation
- **obsValues** (<code>[ndarray](#numpy.ndarray)</code>) – obsValues
- **obsGeom** (<code>[TimeSeriesGeometryNative](#cinterop.cffi.marshal.TimeSeriesGeometryNative)</code>) – obsGeom
- **errorModelElementId** (<code>[str](#str)</code>) – errorModelElementId
- **warmupStart** (<code>[datetime](#datetime.datetime)</code>) – warmupStart
- **warmupEnd** (<code>[datetime](#datetime.datetime)</code>) – warmupEnd
- **warmup** (<code>[bool](#bool)</code>) – warmup
- **estimationStart** (<code>[datetime](#datetime.datetime)</code>) – estimationStart
- **estimationEnd** (<code>[datetime](#datetime.datetime)</code>) – estimationEnd
- **s2Window** (<code>[float](#float)</code>) – s2Window
- **censThr** (<code>[float](#float)</code>) – censThr
- **censOpt** (<code>[float](#float)</code>) – censOpt
- **exclusionStart** (<code>[datetime](#datetime.datetime)</code>) – exclusionStart
- **exclusionEnd** (<code>[datetime](#datetime.datetime)</code>) – exclusionEnd
- **exclusion** (<code>[bool](#bool)</code>) – exclusion
- **terminationCondition** (<code>[SceTerminationCondition](#swift2.classes.SceTerminationCondition)</code>) – terminationCondition
- **maerrisParams** (<code>[HypercubeParameteriser](#swift2.classes.HypercubeParameteriser)</code>) – maerrisParams
- **hydroParams** (<code>[HypercubeParameteriser](#swift2.classes.HypercubeParameteriser)</code>) – hydroParams
- **restrictionOn** (<code>[bool](#bool)</code>) – restrictionOn

**Returns:**

- <code>[HypercubeParameteriser](#swift2.classes.HypercubeParameteriser)</code> – returned result

##### swift2.doc_helper.swg.EstimateTransformationParametersMS_py

```python
EstimateTransformationParametersMS_py(obsValues, obsGeom, estimationStart, estimationEnd, exclusionStart, exclusionEnd, exclusion, terminationCondition, Params)
```

EstimateTransformationParametersMS_py

EstimateTransformationParametersMS_py: generated wrapper function for API function EstimateTransformationParametersMS

**Parameters:**

- **obsValues** (<code>[ndarray](#numpy.ndarray)</code>) – obsValues
- **obsGeom** (<code>[TimeSeriesGeometryNative](#cinterop.cffi.marshal.TimeSeriesGeometryNative)</code>) – obsGeom
- **estimationStart** (<code>[datetime](#datetime.datetime)</code>) – estimationStart
- **estimationEnd** (<code>[datetime](#datetime.datetime)</code>) – estimationEnd
- **exclusionStart** (<code>[datetime](#datetime.datetime)</code>) – exclusionStart
- **exclusionEnd** (<code>[datetime](#datetime.datetime)</code>) – exclusionEnd
- **exclusion** (<code>[bool](#bool)</code>) – exclusion
- **terminationCondition** (<code>[SceTerminationCondition](#swift2.classes.SceTerminationCondition)</code>) – terminationCondition
- **Params** (<code>[HypercubeParameteriser](#swift2.classes.HypercubeParameteriser)</code>) – Params

**Returns:**

- <code>[HypercubeParameteriser](#swift2.classes.HypercubeParameteriser)</code> – returned result

##### swift2.doc_helper.swg.EstimateTransformationParameters_py

```python
EstimateTransformationParameters_py(obsValues, obsGeom, estimationStart, estimationEnd, censThr, censOpt, exclusionStart, exclusionEnd, exclusion, terminationCondition)
```

EstimateTransformationParameters_py

EstimateTransformationParameters_py: generated wrapper function for API function EstimateTransformationParameters

**Parameters:**

- **obsValues** (<code>[ndarray](#numpy.ndarray)</code>) – obsValues
- **obsGeom** (<code>[TimeSeriesGeometryNative](#cinterop.cffi.marshal.TimeSeriesGeometryNative)</code>) – obsGeom
- **estimationStart** (<code>[datetime](#datetime.datetime)</code>) – estimationStart
- **estimationEnd** (<code>[datetime](#datetime.datetime)</code>) – estimationEnd
- **censThr** (<code>[float](#float)</code>) – censThr
- **censOpt** (<code>[float](#float)</code>) – censOpt
- **exclusionStart** (<code>[datetime](#datetime.datetime)</code>) – exclusionStart
- **exclusionEnd** (<code>[datetime](#datetime.datetime)</code>) – exclusionEnd
- **exclusion** (<code>[bool](#bool)</code>) – exclusion
- **terminationCondition** (<code>[SceTerminationCondition](#swift2.classes.SceTerminationCondition)</code>) – terminationCondition

**Returns:**

- <code>[HypercubeParameteriser](#swift2.classes.HypercubeParameteriser)</code> – returned result

##### swift2.doc_helper.swg.EvaluateScoreForParametersInitState_py

```python
EvaluateScoreForParametersInitState_py(objectiveEvaluator, parameterizer)
```

EvaluateScoreForParametersInitState_py

EvaluateScoreForParametersInitState_py: generated wrapper function for API function EvaluateScoreForParametersInitState

**Parameters:**

- **objectiveEvaluator** (<code>[DeletableCffiNativeHandle](#refcount.interop.DeletableCffiNativeHandle)</code>) – objectiveEvaluator
- **parameterizer** (<code>[Any](#typing.Any)</code>) – parameterizer

**Returns:**

- <code>[float](#float)</code> – returned result

##### swift2.doc_helper.swg.EvaluateScoreForParametersWilaInitState_py

```python
EvaluateScoreForParametersWilaInitState_py(objectiveEvaluator, hypercubeParameterizer)
```

EvaluateScoreForParametersWilaInitState_py

EvaluateScoreForParametersWilaInitState_py: generated wrapper function for API function EvaluateScoreForParametersWilaInitState

**Parameters:**

- **objectiveEvaluator** (<code>[ObjectiveEvaluator](#swift2.classes.ObjectiveEvaluator)</code>) – objectiveEvaluator
- **hypercubeParameterizer** (<code>[HypercubeParameteriser](#swift2.classes.HypercubeParameteriser)</code>) – hypercubeParameterizer

**Returns:**

- <code>[ObjectiveScores](#swift2.classes.ObjectiveScores)</code> – returned result

##### swift2.doc_helper.swg.EvaluateScoreForParametersWila_py

```python
EvaluateScoreForParametersWila_py(objectiveEvaluator, hypercubeParameterizer)
```

EvaluateScoreForParametersWila_py

EvaluateScoreForParametersWila_py: generated wrapper function for API function EvaluateScoreForParametersWila

**Parameters:**

- **objectiveEvaluator** (<code>[ObjectiveEvaluator](#swift2.classes.ObjectiveEvaluator)</code>) – objectiveEvaluator
- **hypercubeParameterizer** (<code>[HypercubeParameteriser](#swift2.classes.HypercubeParameteriser)</code>) – hypercubeParameterizer

**Returns:**

- <code>[ObjectiveScores](#swift2.classes.ObjectiveScores)</code> – returned result

##### swift2.doc_helper.swg.EvaluateScoreForParameters_py

```python
EvaluateScoreForParameters_py(objectiveEvaluator, parameterizer)
```

EvaluateScoreForParameters_py

EvaluateScoreForParameters_py: generated wrapper function for API function EvaluateScoreForParameters

**Parameters:**

- **objectiveEvaluator** (<code>[DeletableCffiNativeHandle](#refcount.interop.DeletableCffiNativeHandle)</code>) – objectiveEvaluator
- **parameterizer** (<code>[Any](#typing.Any)</code>) – parameterizer

**Returns:**

- <code>[float](#float)</code> – returned result

##### swift2.doc_helper.swg.EvaluateScore_py

```python
EvaluateScore_py(objectiveEvaluator)
```

EvaluateScore_py

EvaluateScore_py: generated wrapper function for API function EvaluateScore

**Parameters:**

- **objectiveEvaluator** (<code>[DeletableCffiNativeHandle](#refcount.interop.DeletableCffiNativeHandle)</code>) – objectiveEvaluator

**Returns:**

- <code>[float](#float)</code> – returned result

##### swift2.doc_helper.swg.EvaluateScoresForParametersWila_py

```python
EvaluateScoresForParametersWila_py(objectiveEvaluator, parameterizer)
```

EvaluateScoresForParametersWila_py

EvaluateScoresForParametersWila_py: generated wrapper function for API function EvaluateScoresForParametersWila

**Parameters:**

- **objectiveEvaluator** (<code>[ObjectiveEvaluator](#swift2.classes.ObjectiveEvaluator)</code>) – objectiveEvaluator
- **parameterizer** (<code>[HypercubeParameteriser](#swift2.classes.HypercubeParameteriser)</code>) – parameterizer

**Returns:**

- <code>[Dict](#typing.Dict)\[[str](#str), [float](#float)\]</code> – returned result

##### swift2.doc_helper.swg.ExecuteEnsembleForecastSimulation_py

```python
ExecuteEnsembleForecastSimulation_py(efSimulation)
```

ExecuteEnsembleForecastSimulation_py

ExecuteEnsembleForecastSimulation_py: generated wrapper function for API function ExecuteEnsembleForecastSimulation

**Parameters:**

- **efSimulation** (<code>[EnsembleForecastSimulation](#swift2.classes.EnsembleForecastSimulation)</code>) – efSimulation

##### swift2.doc_helper.swg.ExecuteOptimizerWila_py

```python
ExecuteOptimizerWila_py(optimizer)
```

ExecuteOptimizerWila_py

ExecuteOptimizerWila_py: generated wrapper function for API function ExecuteOptimizerWila

**Parameters:**

- **optimizer** (<code>[Optimiser](#swift2.classes.Optimiser)</code>) – optimizer

**Returns:**

- <code>[VectorObjectiveScores](#swift2.classes.VectorObjectiveScores)</code> – returned result

##### swift2.doc_helper.swg.ExecuteSimulation_py

```python
ExecuteSimulation_py(simulation, resetInitialStates)
```

ExecuteSimulation_py

ExecuteSimulation_py: generated wrapper function for API function ExecuteSimulation

**Parameters:**

- **simulation** (<code>[Simulation](#swift2.classes.Simulation)</code>) – simulation
- **resetInitialStates** (<code>[bool](#bool)</code>) – resetInitialStates

##### swift2.doc_helper.swg.GetCatchmentDOTGraph_py

```python
GetCatchmentDOTGraph_py(simulation)
```

GetCatchmentDOTGraph_py

GetCatchmentDOTGraph_py: generated wrapper function for API function GetCatchmentDOTGraph

**Parameters:**

- **simulation** (<code>[Simulation](#swift2.classes.Simulation)</code>) – simulation

**Returns:**

- <code>[str](#str)</code> – returned result

##### swift2.doc_helper.swg.GetCatchmentStructure_py

```python
GetCatchmentStructure_py(simulation)
```

GetCatchmentStructure_py

GetCatchmentStructure_py: generated wrapper function for API function GetCatchmentStructure

**Parameters:**

- **simulation** (<code>[Simulation](#swift2.classes.Simulation)</code>) – simulation

**Returns:**

- <code>[DeletableCffiNativeHandle](#refcount.interop.DeletableCffiNativeHandle)</code> – returned result

##### swift2.doc_helper.swg.GetDefaultMaxThreadsWila_py

```python
GetDefaultMaxThreadsWila_py()
```

GetDefaultMaxThreadsWila_py

GetDefaultMaxThreadsWila_py: generated wrapper function for API function GetDefaultMaxThreadsWila

Args:

**Returns:**

- <code>[int](#int)</code> – returned result

##### swift2.doc_helper.swg.GetERRISCalibrationLog_py

```python
GetERRISCalibrationLog_py(calibObject)
```

GetERRISCalibrationLog_py

GetERRISCalibrationLog_py: generated wrapper function for API function GetERRISCalibrationLog

**Parameters:**

- **calibObject** (<code>[ErrisStagedCalibration](#swift2.classes.ErrisStagedCalibration)</code>) – calibObject

**Returns:**

- <code>[DeletableCffiNativeHandle](#refcount.interop.DeletableCffiNativeHandle)</code> – returned result

##### swift2.doc_helper.swg.GetElementVarIdentifier_py

```python
GetElementVarIdentifier_py(simulation, elementId, index)
```

GetElementVarIdentifier_py

GetElementVarIdentifier_py: generated wrapper function for API function GetElementVarIdentifier

**Parameters:**

- **simulation** (<code>[Simulation](#swift2.classes.Simulation)</code>) – simulation
- **elementId** (<code>[str](#str)</code>) – elementId
- **index** (<code>[int](#int)</code>) – index

**Returns:**

- <code>[str](#str)</code> – returned result

##### swift2.doc_helper.swg.GetElementVarIdentifiers_py

```python
GetElementVarIdentifiers_py(simulation, elementId)
```

GetElementVarIdentifiers_py

GetElementVarIdentifiers_py: generated wrapper function for API function GetElementVarIdentifiers

##### swift2.doc_helper.swg.GetEnd_py

```python
GetEnd_py(simulation, end)
```

GetEnd_py

GetEnd_py: generated wrapper function for API function GetEnd

**Parameters:**

- **simulation** (<code>[Any](#typing.Any)</code>) – simulation
- **end** (<code>[Any](#typing.Any)</code>) – end

##### swift2.doc_helper.swg.GetEnsembleForecastEnsembleRecorded_py

```python
GetEnsembleForecastEnsembleRecorded_py(efSimulation, variableIdentifier, leadTimeIndex, values)
```

GetEnsembleForecastEnsembleRecorded_py

GetEnsembleForecastEnsembleRecorded_py: generated wrapper function for API function GetEnsembleForecastEnsembleRecorded

**Parameters:**

- **efSimulation** (<code>[EnsembleForecastSimulation](#swift2.classes.EnsembleForecastSimulation)</code>) – efSimulation
- **variableIdentifier** (<code>[str](#str)</code>) – variableIdentifier
- **leadTimeIndex** (<code>[int](#int)</code>) – leadTimeIndex
- **values** (<code>[ndarray](#numpy.ndarray)</code>) – values

##### swift2.doc_helper.swg.GetEnsembleForecastEnsembleSize_py

```python
GetEnsembleForecastEnsembleSize_py(efSimulation)
```

GetEnsembleForecastEnsembleSize_py

GetEnsembleForecastEnsembleSize_py: generated wrapper function for API function GetEnsembleForecastEnsembleSize

**Parameters:**

- **efSimulation** (<code>[EnsembleForecastSimulation](#swift2.classes.EnsembleForecastSimulation)</code>) – efSimulation

**Returns:**

- <code>[int](#int)</code> – returned result

##### swift2.doc_helper.swg.GetEnsembleForecastLeadLength_py

```python
GetEnsembleForecastLeadLength_py(efSimulation)
```

GetEnsembleForecastLeadLength_py

GetEnsembleForecastLeadLength_py: generated wrapper function for API function GetEnsembleForecastLeadLength

**Parameters:**

- **efSimulation** (<code>[EnsembleForecastSimulation](#swift2.classes.EnsembleForecastSimulation)</code>) – efSimulation

**Returns:**

- <code>[int](#int)</code> – returned result

##### swift2.doc_helper.swg.GetEnsembleForecastSingleRecorded_py

```python
GetEnsembleForecastSingleRecorded_py(efSimulation, variableIdentifier, leadTimeIndex, ensembleIndex, values)
```

GetEnsembleForecastSingleRecorded_py

GetEnsembleForecastSingleRecorded_py: generated wrapper function for API function GetEnsembleForecastSingleRecorded

**Parameters:**

- **efSimulation** (<code>[EnsembleForecastSimulation](#swift2.classes.EnsembleForecastSimulation)</code>) – efSimulation
- **variableIdentifier** (<code>[str](#str)</code>) – variableIdentifier
- **leadTimeIndex** (<code>[int](#int)</code>) – leadTimeIndex
- **ensembleIndex** (<code>[int](#int)</code>) – ensembleIndex
- **values** (<code>[ndarray](#numpy.ndarray)</code>) – values

##### swift2.doc_helper.swg.GetFeasibleMuskingumBounds_py

```python
GetFeasibleMuskingumBounds_py(simulation, deltaTHours)
```

GetFeasibleMuskingumBounds_py

GetFeasibleMuskingumBounds_py: generated wrapper function for API function GetFeasibleMuskingumBounds

**Parameters:**

- **simulation** (<code>[Simulation](#swift2.classes.Simulation)</code>) – simulation
- **deltaTHours** (<code>[float](#float)</code>) – deltaTHours

**Returns:**

- <code>[Dict](#typing.Dict)\[[str](#str), [float](#float)\]</code> – returned result

##### swift2.doc_helper.swg.GetKnownParameterizationStrategies_py

```python
GetKnownParameterizationStrategies_py()
```

GetKnownParameterizationStrategies_py

GetKnownParameterizationStrategies_py: generated wrapper function for API function GetKnownParameterizationStrategies

##### swift2.doc_helper.swg.GetKnownParameterizationTargetSelectorTypes_py

```python
GetKnownParameterizationTargetSelectorTypes_py()
```

GetKnownParameterizationTargetSelectorTypes_py

GetKnownParameterizationTargetSelectorTypes_py: generated wrapper function for API function GetKnownParameterizationTargetSelectorTypes

##### swift2.doc_helper.swg.GetKnownParameterizerAggregationStrategies_py

```python
GetKnownParameterizerAggregationStrategies_py()
```

GetKnownParameterizerAggregationStrategies_py

GetKnownParameterizerAggregationStrategies_py: generated wrapper function for API function GetKnownParameterizerAggregationStrategies

##### swift2.doc_helper.swg.GetLastStdExceptionMessage_py

```python
GetLastStdExceptionMessage_py()
```

GetLastStdExceptionMessage_py

GetLastStdExceptionMessage_py: generated wrapper function for API function GetLastStdExceptionMessage

Args:

**Returns:**

- <code>[str](#str)</code> – returned result

##### swift2.doc_helper.swg.GetLengthSetOfScores_py

```python
GetLengthSetOfScores_py(vectorScores)
```

GetLengthSetOfScores_py

GetLengthSetOfScores_py: generated wrapper function for API function GetLengthSetOfScores

**Parameters:**

- **vectorScores** (<code>[VectorObjectiveScores](#swift2.classes.VectorObjectiveScores)</code>) – vectorScores

**Returns:**

- <code>[int](#int)</code> – returned result

##### swift2.doc_helper.swg.GetLinkIdentifier_py

```python
GetLinkIdentifier_py(simulation, index)
```

GetLinkIdentifier_py

GetLinkIdentifier_py: generated wrapper function for API function GetLinkIdentifier

**Parameters:**

- **simulation** (<code>[Simulation](#swift2.classes.Simulation)</code>) – simulation
- **index** (<code>[int](#int)</code>) – index

**Returns:**

- <code>[str](#str)</code> – returned result

##### swift2.doc_helper.swg.GetLinkIdentifiers_py

```python
GetLinkIdentifiers_py(simulation)
```

GetLinkIdentifiers_py

GetLinkIdentifiers_py: generated wrapper function for API function GetLinkIdentifiers

##### swift2.doc_helper.swg.GetLinkName_py

```python
GetLinkName_py(simulation, index)
```

GetLinkName_py

GetLinkName_py: generated wrapper function for API function GetLinkName

**Parameters:**

- **simulation** (<code>[Simulation](#swift2.classes.Simulation)</code>) – simulation
- **index** (<code>[int](#int)</code>) – index

**Returns:**

- <code>[str](#str)</code> – returned result

##### swift2.doc_helper.swg.GetLinkNames_py

```python
GetLinkNames_py(simulation)
```

GetLinkNames_py

GetLinkNames_py: generated wrapper function for API function GetLinkNames

##### swift2.doc_helper.swg.GetMAERRISCalibrationLog_py

```python
GetMAERRISCalibrationLog_py(calibObject)
```

GetMAERRISCalibrationLog_py

GetMAERRISCalibrationLog_py: generated wrapper function for API function GetMAERRISCalibrationLog

**Parameters:**

- **calibObject** (<code>[MaerrisStagedCalibration](#swift2.classes.MaerrisStagedCalibration)</code>) – calibObject

**Returns:**

- <code>[DeletableCffiNativeHandle](#refcount.interop.DeletableCffiNativeHandle)</code> – returned result

##### swift2.doc_helper.swg.GetMemoryStates_py

```python
GetMemoryStates_py(memoryStates)
```

GetMemoryStates_py

GetMemoryStates_py: generated wrapper function for API function GetMemoryStates

**Parameters:**

- **memoryStates** (<code>[MemoryStates](#swift2.classes.MemoryStates)</code>) – memoryStates

**Returns:**

- <code>[str](#str)</code> – returned result

##### swift2.doc_helper.swg.GetModelConfigurationSwift_py

```python
GetModelConfigurationSwift_py(simulation, elementIdentifier)
```

GetModelConfigurationSwift_py

GetModelConfigurationSwift_py: generated wrapper function for API function GetModelConfigurationSwift

**Parameters:**

- **simulation** (<code>[Simulation](#swift2.classes.Simulation)</code>) – simulation
- **elementIdentifier** (<code>[str](#str)</code>) – elementIdentifier

**Returns:**

- <code>[Dict](#typing.Dict)\[[str](#str), [str](#str)\]</code> – returned result

##### swift2.doc_helper.swg.GetNameObjectiveEvaluator_py

```python
GetNameObjectiveEvaluator_py(objectiveEvaluator)
```

GetNameObjectiveEvaluator_py

GetNameObjectiveEvaluator_py: generated wrapper function for API function GetNameObjectiveEvaluator

**Parameters:**

- **objectiveEvaluator** (<code>[DeletableCffiNativeHandle](#refcount.interop.DeletableCffiNativeHandle)</code>) – objectiveEvaluator

**Returns:**

- <code>[str](#str)</code> – returned result

##### swift2.doc_helper.swg.GetNodeIdentifier_py

```python
GetNodeIdentifier_py(simulation, index)
```

GetNodeIdentifier_py

GetNodeIdentifier_py: generated wrapper function for API function GetNodeIdentifier

**Parameters:**

- **simulation** (<code>[Simulation](#swift2.classes.Simulation)</code>) – simulation
- **index** (<code>[int](#int)</code>) – index

**Returns:**

- <code>[str](#str)</code> – returned result

##### swift2.doc_helper.swg.GetNodeIdentifiers_py

```python
GetNodeIdentifiers_py(simulation)
```

GetNodeIdentifiers_py

GetNodeIdentifiers_py: generated wrapper function for API function GetNodeIdentifiers

##### swift2.doc_helper.swg.GetNodeName_py

```python
GetNodeName_py(simulation, index)
```

GetNodeName_py

GetNodeName_py: generated wrapper function for API function GetNodeName

**Parameters:**

- **simulation** (<code>[Simulation](#swift2.classes.Simulation)</code>) – simulation
- **index** (<code>[int](#int)</code>) – index

**Returns:**

- <code>[str](#str)</code> – returned result

##### swift2.doc_helper.swg.GetNodeNames_py

```python
GetNodeNames_py(simulation)
```

GetNodeNames_py

GetNodeNames_py: generated wrapper function for API function GetNodeNames

##### swift2.doc_helper.swg.GetNumCatchments_py

```python
GetNumCatchments_py()
```

GetNumCatchments_py

GetNumCatchments_py: generated wrapper function for API function GetNumCatchments

Args:

**Returns:**

- <code>[int](#int)</code> – returned result

##### swift2.doc_helper.swg.GetNumHyperCubesWila_py

```python
GetNumHyperCubesWila_py()
```

GetNumHyperCubesWila_py

GetNumHyperCubesWila_py: generated wrapper function for API function GetNumHyperCubesWila

Args:

**Returns:**

- <code>[int](#int)</code> – returned result

##### swift2.doc_helper.swg.GetNumHyperCubes_py

```python
GetNumHyperCubes_py()
```

GetNumHyperCubes_py

GetNumHyperCubes_py: generated wrapper function for API function GetNumHyperCubes

Args:

**Returns:**

- <code>[int](#int)</code> – returned result

##### swift2.doc_helper.swg.GetNumLinks_py

```python
GetNumLinks_py(simulation)
```

GetNumLinks_py

GetNumLinks_py: generated wrapper function for API function GetNumLinks

**Parameters:**

- **simulation** (<code>[Simulation](#swift2.classes.Simulation)</code>) – simulation

**Returns:**

- <code>[int](#int)</code> – returned result

##### swift2.doc_helper.swg.GetNumMemTestCatchments_py

```python
GetNumMemTestCatchments_py()
```

GetNumMemTestCatchments_py

GetNumMemTestCatchments_py: generated wrapper function for API function GetNumMemTestCatchments

Args:

**Returns:**

- <code>[int](#int)</code> – returned result

##### swift2.doc_helper.swg.GetNumMemTestModelRunners_py

```python
GetNumMemTestModelRunners_py()
```

GetNumMemTestModelRunners_py

GetNumMemTestModelRunners_py: generated wrapper function for API function GetNumMemTestModelRunners

Args:

**Returns:**

- <code>[int](#int)</code> – returned result

##### swift2.doc_helper.swg.GetNumMemTestParameterizers_py

```python
GetNumMemTestParameterizers_py()
```

GetNumMemTestParameterizers_py

GetNumMemTestParameterizers_py: generated wrapper function for API function GetNumMemTestParameterizers

Args:

**Returns:**

- <code>[int](#int)</code> – returned result

##### swift2.doc_helper.swg.GetNumModelRunners_py

```python
GetNumModelRunners_py()
```

GetNumModelRunners_py

GetNumModelRunners_py: generated wrapper function for API function GetNumModelRunners

Args:

**Returns:**

- <code>[int](#int)</code> – returned result

##### swift2.doc_helper.swg.GetNumNodes_py

```python
GetNumNodes_py(simulation)
```

GetNumNodes_py

GetNumNodes_py: generated wrapper function for API function GetNumNodes

**Parameters:**

- **simulation** (<code>[Simulation](#swift2.classes.Simulation)</code>) – simulation

**Returns:**

- <code>[int](#int)</code> – returned result

##### swift2.doc_helper.swg.GetNumParameters_py

```python
GetNumParameters_py(hypercubeParameterizer)
```

GetNumParameters_py

GetNumParameters_py: generated wrapper function for API function GetNumParameters

**Parameters:**

- **hypercubeParameterizer** (<code>[HypercubeParameteriser](#swift2.classes.HypercubeParameteriser)</code>) – hypercubeParameterizer

**Returns:**

- <code>[int](#int)</code> – returned result

##### swift2.doc_helper.swg.GetNumPlayedVariables_py

```python
GetNumPlayedVariables_py(simulation)
```

GetNumPlayedVariables_py

GetNumPlayedVariables_py: generated wrapper function for API function GetNumPlayedVariables

**Parameters:**

- **simulation** (<code>[Simulation](#swift2.classes.Simulation)</code>) – simulation

**Returns:**

- <code>[int](#int)</code> – returned result

##### swift2.doc_helper.swg.GetNumRainfallRunoff_py

```python
GetNumRainfallRunoff_py()
```

GetNumRainfallRunoff_py

GetNumRainfallRunoff_py: generated wrapper function for API function GetNumRainfallRunoff

Args:

**Returns:**

- <code>[int](#int)</code> – returned result

##### swift2.doc_helper.swg.GetNumRecordedVariables_py

```python
GetNumRecordedVariables_py(simulation)
```

GetNumRecordedVariables_py

GetNumRecordedVariables_py: generated wrapper function for API function GetNumRecordedVariables

**Parameters:**

- **simulation** (<code>[Simulation](#swift2.classes.Simulation)</code>) – simulation

**Returns:**

- <code>[int](#int)</code> – returned result

##### swift2.doc_helper.swg.GetNumRunoffModelIdentifiers_py

```python
GetNumRunoffModelIdentifiers_py()
```

GetNumRunoffModelIdentifiers_py

GetNumRunoffModelIdentifiers_py: generated wrapper function for API function GetNumRunoffModelIdentifiers

Args:

**Returns:**

- <code>[int](#int)</code> – returned result

##### swift2.doc_helper.swg.GetNumRunoffModelVarIdentifiers_py

```python
GetNumRunoffModelVarIdentifiers_py(modelId)
```

GetNumRunoffModelVarIdentifiers_py

GetNumRunoffModelVarIdentifiers_py: generated wrapper function for API function GetNumRunoffModelVarIdentifiers

**Parameters:**

- **modelId** (<code>[str](#str)</code>) – modelId

**Returns:**

- <code>[int](#int)</code> – returned result

##### swift2.doc_helper.swg.GetNumScoresWila_py

```python
GetNumScoresWila_py(scores)
```

GetNumScoresWila_py

GetNumScoresWila_py: generated wrapper function for API function GetNumScoresWila

**Parameters:**

- **scores** (<code>[ObjectiveScores](#swift2.classes.ObjectiveScores)</code>) – scores

**Returns:**

- <code>[int](#int)</code> – returned result

##### swift2.doc_helper.swg.GetNumStateInitializers_py

```python
GetNumStateInitializers_py()
```

GetNumStateInitializers_py

GetNumStateInitializers_py: generated wrapper function for API function GetNumStateInitializers

Args:

**Returns:**

- <code>[int](#int)</code> – returned result

##### swift2.doc_helper.swg.GetNumStepsForTimeSpan_py

```python
GetNumStepsForTimeSpan_py(modelSimulation, start, end)
```

GetNumStepsForTimeSpan_py

GetNumStepsForTimeSpan_py: generated wrapper function for API function GetNumStepsForTimeSpan

**Parameters:**

- **modelSimulation** (<code>[Simulation](#swift2.classes.Simulation)</code>) – modelSimulation
- **start** (<code>[datetime](#datetime.datetime)</code>) – start
- **end** (<code>[datetime](#datetime.datetime)</code>) – end

**Returns:**

- <code>[int](#int)</code> – returned result

##### swift2.doc_helper.swg.GetNumSteps_py

```python
GetNumSteps_py(simulation)
```

GetNumSteps_py

GetNumSteps_py: generated wrapper function for API function GetNumSteps

**Parameters:**

- **simulation** (<code>[Simulation](#swift2.classes.Simulation)</code>) – simulation

**Returns:**

- <code>[int](#int)</code> – returned result

##### swift2.doc_helper.swg.GetNumSubareas_py

```python
GetNumSubareas_py(simulation)
```

GetNumSubareas_py

GetNumSubareas_py: generated wrapper function for API function GetNumSubareas

**Parameters:**

- **simulation** (<code>[Simulation](#swift2.classes.Simulation)</code>) – simulation

**Returns:**

- <code>[int](#int)</code> – returned result

##### swift2.doc_helper.swg.GetNumVarIdentifiers_py

```python
GetNumVarIdentifiers_py(simulation, elementId)
```

GetNumVarIdentifiers_py

GetNumVarIdentifiers_py: generated wrapper function for API function GetNumVarIdentifiers

**Parameters:**

- **simulation** (<code>[Simulation](#swift2.classes.Simulation)</code>) – simulation
- **elementId** (<code>[str](#str)</code>) – elementId

**Returns:**

- <code>[int](#int)</code> – returned result

##### swift2.doc_helper.swg.GetOptimizerLogDataWilaDims_py

```python
GetOptimizerLogDataWilaDims_py(logData, logLength, stringDataCount, numericDataCount)
```

GetOptimizerLogDataWilaDims_py

GetOptimizerLogDataWilaDims_py: generated wrapper function for API function GetOptimizerLogDataWilaDims

**Parameters:**

- **logData** (<code>[DeletableCffiNativeHandle](#refcount.interop.DeletableCffiNativeHandle)</code>) – logData
- **logLength** (<code>[ndarray](#numpy.ndarray)</code>) – logLength
- **stringDataCount** (<code>[ndarray](#numpy.ndarray)</code>) – stringDataCount
- **numericDataCount** (<code>[ndarray](#numpy.ndarray)</code>) – numericDataCount

##### swift2.doc_helper.swg.GetOptimizerLogDataWilaNumericDataNames_py

```python
GetOptimizerLogDataWilaNumericDataNames_py(logData, numericDataIndex)
```

GetOptimizerLogDataWilaNumericDataNames_py

GetOptimizerLogDataWilaNumericDataNames_py: generated wrapper function for API function GetOptimizerLogDataWilaNumericDataNames

**Parameters:**

- **logData** (<code>[DeletableCffiNativeHandle](#refcount.interop.DeletableCffiNativeHandle)</code>) – logData
- **numericDataIndex** (<code>[int](#int)</code>) – numericDataIndex

**Returns:**

- <code>[str](#str)</code> – returned result

##### swift2.doc_helper.swg.GetOptimizerLogDataWilaNumericData_py

```python
GetOptimizerLogDataWilaNumericData_py(logData, numericDataIndex, data)
```

GetOptimizerLogDataWilaNumericData_py

GetOptimizerLogDataWilaNumericData_py: generated wrapper function for API function GetOptimizerLogDataWilaNumericData

**Parameters:**

- **logData** (<code>[DeletableCffiNativeHandle](#refcount.interop.DeletableCffiNativeHandle)</code>) – logData
- **numericDataIndex** (<code>[int](#int)</code>) – numericDataIndex
- **data** (<code>[ndarray](#numpy.ndarray)</code>) – data

##### swift2.doc_helper.swg.GetOptimizerLogDataWilaStringDataNames_py

```python
GetOptimizerLogDataWilaStringDataNames_py(logData, stringDataIndex)
```

GetOptimizerLogDataWilaStringDataNames_py

GetOptimizerLogDataWilaStringDataNames_py: generated wrapper function for API function GetOptimizerLogDataWilaStringDataNames

**Parameters:**

- **logData** (<code>[DeletableCffiNativeHandle](#refcount.interop.DeletableCffiNativeHandle)</code>) – logData
- **stringDataIndex** (<code>[int](#int)</code>) – stringDataIndex

**Returns:**

- <code>[str](#str)</code> – returned result

##### swift2.doc_helper.swg.GetOptimizerLogDataWilaStringData_py

```python
GetOptimizerLogDataWilaStringData_py(logData)
```

GetOptimizerLogDataWilaStringData_py

GetOptimizerLogDataWilaStringData_py: generated wrapper function for API function GetOptimizerLogDataWilaStringData

##### swift2.doc_helper.swg.GetOptimizerLogDataWila_py

```python
GetOptimizerLogDataWila_py(optimizer)
```

GetOptimizerLogDataWila_py

GetOptimizerLogDataWila_py: generated wrapper function for API function GetOptimizerLogDataWila

**Parameters:**

- **optimizer** (<code>[Optimiser](#swift2.classes.Optimiser)</code>) – optimizer

**Returns:**

- <code>[DeletableCffiNativeHandle](#refcount.interop.DeletableCffiNativeHandle)</code> – returned result

##### swift2.doc_helper.swg.GetParameterMaxValue_py

```python
GetParameterMaxValue_py(hypercubeParameterizer, variableName)
```

GetParameterMaxValue_py

GetParameterMaxValue_py: generated wrapper function for API function GetParameterMaxValue

**Parameters:**

- **hypercubeParameterizer** (<code>[HypercubeParameteriser](#swift2.classes.HypercubeParameteriser)</code>) – hypercubeParameterizer
- **variableName** (<code>[str](#str)</code>) – variableName

**Returns:**

- <code>[float](#float)</code> – returned result

##### swift2.doc_helper.swg.GetParameterMinValue_py

```python
GetParameterMinValue_py(hypercubeParameterizer, variableName)
```

GetParameterMinValue_py

GetParameterMinValue_py: generated wrapper function for API function GetParameterMinValue

**Parameters:**

- **hypercubeParameterizer** (<code>[HypercubeParameteriser](#swift2.classes.HypercubeParameteriser)</code>) – hypercubeParameterizer
- **variableName** (<code>[str](#str)</code>) – variableName

**Returns:**

- <code>[float](#float)</code> – returned result

##### swift2.doc_helper.swg.GetParameterName_py

```python
GetParameterName_py(hypercubeParameterizer, index)
```

GetParameterName_py

GetParameterName_py: generated wrapper function for API function GetParameterName

**Parameters:**

- **hypercubeParameterizer** (<code>[HypercubeParameteriser](#swift2.classes.HypercubeParameteriser)</code>) – hypercubeParameterizer
- **index** (<code>[int](#int)</code>) – index

**Returns:**

- <code>[str](#str)</code> – returned result

##### swift2.doc_helper.swg.GetParameterValue_py

```python
GetParameterValue_py(hypercubeParameterizer, variableName)
```

GetParameterValue_py

GetParameterValue_py: generated wrapper function for API function GetParameterValue

**Parameters:**

- **hypercubeParameterizer** (<code>[HypercubeParameteriser](#swift2.classes.HypercubeParameteriser)</code>) – hypercubeParameterizer
- **variableName** (<code>[str](#str)</code>) – variableName

**Returns:**

- <code>[float](#float)</code> – returned result

##### swift2.doc_helper.swg.GetPlayedTimeSeriesLength_py

```python
GetPlayedTimeSeriesLength_py(simulation, variableIdentifier)
```

GetPlayedTimeSeriesLength_py

GetPlayedTimeSeriesLength_py: generated wrapper function for API function GetPlayedTimeSeriesLength

**Parameters:**

- **simulation** (<code>[Simulation](#swift2.classes.Simulation)</code>) – simulation
- **variableIdentifier** (<code>[str](#str)</code>) – variableIdentifier

**Returns:**

- <code>[int](#int)</code> – returned result

##### swift2.doc_helper.swg.GetPlayedTsGeometry_py

```python
GetPlayedTsGeometry_py(simulation, variableIdentifier, geom)
```

GetPlayedTsGeometry_py

GetPlayedTsGeometry_py: generated wrapper function for API function GetPlayedTsGeometry

**Parameters:**

- **simulation** (<code>[Simulation](#swift2.classes.Simulation)</code>) – simulation
- **variableIdentifier** (<code>[str](#str)</code>) – variableIdentifier
- **geom** (<code>[TimeSeriesGeometryNative](#cinterop.cffi.marshal.TimeSeriesGeometryNative)</code>) – geom

##### swift2.doc_helper.swg.GetPlayedVariableName_py

```python
GetPlayedVariableName_py(simulation, index)
```

GetPlayedVariableName_py

GetPlayedVariableName_py: generated wrapper function for API function GetPlayedVariableName

**Parameters:**

- **simulation** (<code>[Simulation](#swift2.classes.Simulation)</code>) – simulation
- **index** (<code>[int](#int)</code>) – index

**Returns:**

- <code>[str](#str)</code> – returned result

##### swift2.doc_helper.swg.GetPlayedVariableNames_py

```python
GetPlayedVariableNames_py(simulation)
```

GetPlayedVariableNames_py

GetPlayedVariableNames_py: generated wrapper function for API function GetPlayedVariableNames

##### swift2.doc_helper.swg.GetPlayed_py

```python
GetPlayed_py(simulation, variableIdentifier, values, arrayLength)
```

GetPlayed_py

GetPlayed_py: generated wrapper function for API function GetPlayed

**Parameters:**

- **simulation** (<code>[Simulation](#swift2.classes.Simulation)</code>) – simulation
- **variableIdentifier** (<code>[str](#str)</code>) – variableIdentifier
- **values** (<code>[ndarray](#numpy.ndarray)</code>) – values
- **arrayLength** (<code>[int](#int)</code>) – arrayLength

##### swift2.doc_helper.swg.GetRecordedEnsembleForecastTimeSeries_py

```python
GetRecordedEnsembleForecastTimeSeries_py(efSimulation, variableIdentifier)
```

GetRecordedEnsembleForecastTimeSeries_py

GetRecordedEnsembleForecastTimeSeries_py: generated wrapper function for API function GetRecordedEnsembleForecastTimeSeries

**Parameters:**

- **efSimulation** (<code>[EnsembleForecastSimulation](#swift2.classes.EnsembleForecastSimulation)</code>) – efSimulation
- **variableIdentifier** (<code>[str](#str)</code>) – variableIdentifier

**Returns:**

- <code>[EnsembleForecastTimeSeries](#uchronia.classes.EnsembleForecastTimeSeries)</code> – returned result

##### swift2.doc_helper.swg.GetRecordedTsGeometry_py

```python
GetRecordedTsGeometry_py(simulation, variableIdentifier, geom)
```

GetRecordedTsGeometry_py

GetRecordedTsGeometry_py: generated wrapper function for API function GetRecordedTsGeometry

**Parameters:**

- **simulation** (<code>[Simulation](#swift2.classes.Simulation)</code>) – simulation
- **variableIdentifier** (<code>[str](#str)</code>) – variableIdentifier
- **geom** (<code>[TimeSeriesGeometryNative](#cinterop.cffi.marshal.TimeSeriesGeometryNative)</code>) – geom

##### swift2.doc_helper.swg.GetRecordedVariableName_py

```python
GetRecordedVariableName_py(simulation, index)
```

GetRecordedVariableName_py

GetRecordedVariableName_py: generated wrapper function for API function GetRecordedVariableName

**Parameters:**

- **simulation** (<code>[Simulation](#swift2.classes.Simulation)</code>) – simulation
- **index** (<code>[int](#int)</code>) – index

**Returns:**

- <code>[str](#str)</code> – returned result

##### swift2.doc_helper.swg.GetRecordedVariableNames_py

```python
GetRecordedVariableNames_py(simulation)
```

GetRecordedVariableNames_py

GetRecordedVariableNames_py: generated wrapper function for API function GetRecordedVariableNames

##### swift2.doc_helper.swg.GetRecorded_py

```python
GetRecorded_py(simulation, variableIdentifier, values, arrayLength)
```

GetRecorded_py

GetRecorded_py: generated wrapper function for API function GetRecorded

**Parameters:**

- **simulation** (<code>[Simulation](#swift2.classes.Simulation)</code>) – simulation
- **variableIdentifier** (<code>[str](#str)</code>) – variableIdentifier
- **values** (<code>[ndarray](#numpy.ndarray)</code>) – values
- **arrayLength** (<code>[int](#int)</code>) – arrayLength

##### swift2.doc_helper.swg.GetRunoffModelIdentifier_py

```python
GetRunoffModelIdentifier_py(index)
```

GetRunoffModelIdentifier_py

GetRunoffModelIdentifier_py: generated wrapper function for API function GetRunoffModelIdentifier

**Parameters:**

- **index** (<code>[int](#int)</code>) – index

**Returns:**

- <code>[str](#str)</code> – returned result

##### swift2.doc_helper.swg.GetRunoffModelIdentifiers_py

```python
GetRunoffModelIdentifiers_py()
```

GetRunoffModelIdentifiers_py

GetRunoffModelIdentifiers_py: generated wrapper function for API function GetRunoffModelIdentifiers

##### swift2.doc_helper.swg.GetRunoffModelVarIdentifier_py

```python
GetRunoffModelVarIdentifier_py(modelId, index)
```

GetRunoffModelVarIdentifier_py

GetRunoffModelVarIdentifier_py: generated wrapper function for API function GetRunoffModelVarIdentifier

**Parameters:**

- **modelId** (<code>[str](#str)</code>) – modelId
- **index** (<code>[int](#int)</code>) – index

**Returns:**

- <code>[str](#str)</code> – returned result

##### swift2.doc_helper.swg.GetRunoffModelVarIdentifiers_py

```python
GetRunoffModelVarIdentifiers_py(modelId)
```

GetRunoffModelVarIdentifiers_py

GetRunoffModelVarIdentifiers_py: generated wrapper function for API function GetRunoffModelVarIdentifiers

##### swift2.doc_helper.swg.GetScoreNameWila_py

```python
GetScoreNameWila_py(scores, index)
```

GetScoreNameWila_py

GetScoreNameWila_py: generated wrapper function for API function GetScoreNameWila

**Parameters:**

- **scores** (<code>[ObjectiveScores](#swift2.classes.ObjectiveScores)</code>) – scores
- **index** (<code>[int](#int)</code>) – index

**Returns:**

- <code>[str](#str)</code> – returned result

##### swift2.doc_helper.swg.GetScoreWila_py

```python
GetScoreWila_py(scores, index)
```

GetScoreWila_py

GetScoreWila_py: generated wrapper function for API function GetScoreWila

**Parameters:**

- **scores** (<code>[ObjectiveScores](#swift2.classes.ObjectiveScores)</code>) – scores
- **index** (<code>[int](#int)</code>) – index

**Returns:**

- <code>[float](#float)</code> – returned result

##### swift2.doc_helper.swg.GetScoresAtIndex_py

```python
GetScoresAtIndex_py(vectorScores, index)
```

GetScoresAtIndex_py

GetScoresAtIndex_py: generated wrapper function for API function GetScoresAtIndex

**Parameters:**

- **vectorScores** (<code>[VectorObjectiveScores](#swift2.classes.VectorObjectiveScores)</code>) – vectorScores
- **index** (<code>[int](#int)</code>) – index

**Returns:**

- <code>[ObjectiveScores](#swift2.classes.ObjectiveScores)</code> – returned result

##### swift2.doc_helper.swg.GetStart_py

```python
GetStart_py(simulation, start)
```

GetStart_py

GetStart_py: generated wrapper function for API function GetStart

**Parameters:**

- **simulation** (<code>[Any](#typing.Any)</code>) – simulation
- **start** (<code>[Any](#typing.Any)</code>) – start

##### swift2.doc_helper.swg.GetSubareaIdentifier_py

```python
GetSubareaIdentifier_py(simulation, index)
```

GetSubareaIdentifier_py

GetSubareaIdentifier_py: generated wrapper function for API function GetSubareaIdentifier

**Parameters:**

- **simulation** (<code>[Simulation](#swift2.classes.Simulation)</code>) – simulation
- **index** (<code>[int](#int)</code>) – index

**Returns:**

- <code>[str](#str)</code> – returned result

##### swift2.doc_helper.swg.GetSubareaIdentifiers_py

```python
GetSubareaIdentifiers_py(simulation)
```

GetSubareaIdentifiers_py

GetSubareaIdentifiers_py: generated wrapper function for API function GetSubareaIdentifiers

##### swift2.doc_helper.swg.GetSubareaName_py

```python
GetSubareaName_py(simulation, index)
```

GetSubareaName_py

GetSubareaName_py: generated wrapper function for API function GetSubareaName

**Parameters:**

- **simulation** (<code>[Simulation](#swift2.classes.Simulation)</code>) – simulation
- **index** (<code>[int](#int)</code>) – index

**Returns:**

- <code>[str](#str)</code> – returned result

##### swift2.doc_helper.swg.GetSubareaNames_py

```python
GetSubareaNames_py(simulation)
```

GetSubareaNames_py

GetSubareaNames_py: generated wrapper function for API function GetSubareaNames

##### swift2.doc_helper.swg.GetSystemConfigurationWila_py

```python
GetSystemConfigurationWila_py(scores)
```

GetSystemConfigurationWila_py

GetSystemConfigurationWila_py: generated wrapper function for API function GetSystemConfigurationWila

**Parameters:**

- **scores** (<code>[ObjectiveScores](#swift2.classes.ObjectiveScores)</code>) – scores

**Returns:**

- <code>[HypercubeParameteriser](#swift2.classes.HypercubeParameteriser)</code> – returned result

##### swift2.doc_helper.swg.GetTimeStepName_py

```python
GetTimeStepName_py(simulation)
```

GetTimeStepName_py

GetTimeStepName_py: generated wrapper function for API function GetTimeStepName

**Parameters:**

- **simulation** (<code>[Any](#typing.Any)</code>) – simulation

**Returns:**

- <code>[str](#str)</code> – returned result

##### swift2.doc_helper.swg.GetValueStateInitializer_py

```python
GetValueStateInitializer_py(stateInitializer, identifier)
```

GetValueStateInitializer_py

GetValueStateInitializer_py: generated wrapper function for API function GetValueStateInitializer

**Parameters:**

- **stateInitializer** (<code>[StateInitialiser](#swift2.classes.StateInitialiser)</code>) – stateInitializer
- **identifier** (<code>[str](#str)</code>) – identifier

**Returns:**

- <code>[float](#float)</code> – returned result

##### swift2.doc_helper.swg.GetVariableBool_py

```python
GetVariableBool_py(simulation, variableIdentifier)
```

GetVariableBool_py

GetVariableBool_py: generated wrapper function for API function GetVariableBool

**Parameters:**

- **simulation** (<code>[Simulation](#swift2.classes.Simulation)</code>) – simulation
- **variableIdentifier** (<code>[str](#str)</code>) – variableIdentifier

**Returns:**

- <code>[bool](#bool)</code> – returned result

##### swift2.doc_helper.swg.GetVariableInt_py

```python
GetVariableInt_py(simulation, variableIdentifier)
```

GetVariableInt_py

GetVariableInt_py: generated wrapper function for API function GetVariableInt

**Parameters:**

- **simulation** (<code>[Simulation](#swift2.classes.Simulation)</code>) – simulation
- **variableIdentifier** (<code>[str](#str)</code>) – variableIdentifier

**Returns:**

- <code>[int](#int)</code> – returned result

##### swift2.doc_helper.swg.GetVariable_py

```python
GetVariable_py(simulation, variableIdentifier)
```

GetVariable_py

GetVariable_py: generated wrapper function for API function GetVariable

**Parameters:**

- **simulation** (<code>[Simulation](#swift2.classes.Simulation)</code>) – simulation
- **variableIdentifier** (<code>[str](#str)</code>) – variableIdentifier

**Returns:**

- <code>[float](#float)</code> – returned result

##### swift2.doc_helper.swg.HideParameters_py

```python
HideParameters_py(p, pnames, regex, startsWith, strict)
```

HideParameters_py

HideParameters_py: generated wrapper function for API function HideParameters

**Parameters:**

- **p** (<code>[HypercubeParameteriser](#swift2.classes.HypercubeParameteriser)</code>) – p
- **pnames** (<code>[List](#typing.List)</code>) – pnames
- **regex** (<code>[bool](#bool)</code>) – regex
- **startsWith** (<code>[bool](#bool)</code>) – startsWith
- **strict** (<code>[bool](#bool)</code>) – strict

##### swift2.doc_helper.swg.HomotheticTransform_py

```python
HomotheticTransform_py(centre, point, factor)
```

HomotheticTransform_py

HomotheticTransform_py: generated wrapper function for API function HomotheticTransform

**Parameters:**

- **centre** (<code>[HypercubeParameteriser](#swift2.classes.HypercubeParameteriser)</code>) – centre
- **point** (<code>[HypercubeParameteriser](#swift2.classes.HypercubeParameteriser)</code>) – point
- **factor** (<code>[float](#float)</code>) – factor

**Returns:**

- <code>[HypercubeParameteriser](#swift2.classes.HypercubeParameteriser)</code> – returned result

##### swift2.doc_helper.swg.IsDictionaryStateInitializer_py

```python
IsDictionaryStateInitializer_py(stateInitializer)
```

IsDictionaryStateInitializer_py

IsDictionaryStateInitializer_py: generated wrapper function for API function IsDictionaryStateInitializer

**Parameters:**

- **stateInitializer** (<code>[StateInitialiser](#swift2.classes.StateInitialiser)</code>) – stateInitializer

**Returns:**

- <code>[bool](#bool)</code> – returned result

##### swift2.doc_helper.swg.IsValidVariableIdentifier_py

```python
IsValidVariableIdentifier_py(simulation, varId)
```

IsValidVariableIdentifier_py

IsValidVariableIdentifier_py: generated wrapper function for API function IsValidVariableIdentifier

**Parameters:**

- **simulation** (<code>[Simulation](#swift2.classes.Simulation)</code>) – simulation
- **varId** (<code>[str](#str)</code>) – varId

**Returns:**

- <code>[bool](#bool)</code> – returned result

##### swift2.doc_helper.swg.IsWithinBounds_py

```python
IsWithinBounds_py(hypercubeParameterizer)
```

IsWithinBounds_py

IsWithinBounds_py: generated wrapper function for API function IsWithinBounds

**Parameters:**

- **hypercubeParameterizer** (<code>[HypercubeParameteriser](#swift2.classes.HypercubeParameteriser)</code>) – hypercubeParameterizer

**Returns:**

- <code>[bool](#bool)</code> – returned result

##### swift2.doc_helper.swg.LoadMemoryStatesFromFile_py

```python
LoadMemoryStatesFromFile_py(filePath, format)
```

LoadMemoryStatesFromFile_py

LoadMemoryStatesFromFile_py: generated wrapper function for API function LoadMemoryStatesFromFile

**Parameters:**

- **filePath** (<code>[str](#str)</code>) – filePath
- **format** (<code>[str](#str)</code>) – format

**Returns:**

- <code>[MemoryStates](#swift2.classes.MemoryStates)</code> – returned result

##### swift2.doc_helper.swg.LoadModelSimulationFromJson_py

```python
LoadModelSimulationFromJson_py(jsonFilePath)
```

LoadModelSimulationFromJson_py

LoadModelSimulationFromJson_py: generated wrapper function for API function LoadModelSimulationFromJson

**Parameters:**

- **jsonFilePath** (<code>[str](#str)</code>) – jsonFilePath

**Returns:**

- <code>[Simulation](#swift2.classes.Simulation)</code> – returned result

##### swift2.doc_helper.swg.LoadParameterizer_py

```python
LoadParameterizer_py(filepath)
```

LoadParameterizer_py

LoadParameterizer_py: generated wrapper function for API function LoadParameterizer

**Parameters:**

- **filepath** (<code>[str](#str)</code>) – filepath

**Returns:**

- <code>[HypercubeParameteriser](#swift2.classes.HypercubeParameteriser)</code> – returned result

##### swift2.doc_helper.swg.LoadVersionOneControlFile_py

```python
LoadVersionOneControlFile_py(controlFileName, rootDataDir)
```

LoadVersionOneControlFile_py

LoadVersionOneControlFile_py: generated wrapper function for API function LoadVersionOneControlFile

**Parameters:**

- **controlFileName** (<code>[str](#str)</code>) – controlFileName
- **rootDataDir** (<code>[str](#str)</code>) – rootDataDir

**Returns:**

- <code>[Simulation](#swift2.classes.Simulation)</code> – returned result

##### swift2.doc_helper.swg.LoadVersionOneTimeSeriesFile_py

```python
LoadVersionOneTimeSeriesFile_py(fileName)
```

LoadVersionOneTimeSeriesFile_py

LoadVersionOneTimeSeriesFile_py: generated wrapper function for API function LoadVersionOneTimeSeriesFile

**Parameters:**

- **fileName** (<code>[str](#str)</code>) – fileName

**Returns:**

- <code>[TimeSeriesProvider](#uchronia.classes.TimeSeriesProvider)</code> – returned result

##### swift2.doc_helper.swg.MemoryStatesFromString_py

```python
MemoryStatesFromString_py(jsonString)
```

MemoryStatesFromString_py

MemoryStatesFromString_py: generated wrapper function for API function MemoryStatesFromString

**Parameters:**

- **jsonString** (<code>[str](#str)</code>) – jsonString

**Returns:**

- <code>[MemoryStates](#swift2.classes.MemoryStates)</code> – returned result

##### swift2.doc_helper.swg.ObjectiveEvaluatorIsMaximizable_py

```python
ObjectiveEvaluatorIsMaximizable_py(objectiveEvaluator)
```

ObjectiveEvaluatorIsMaximizable_py

ObjectiveEvaluatorIsMaximizable_py: generated wrapper function for API function ObjectiveEvaluatorIsMaximizable

**Parameters:**

- **objectiveEvaluator** (<code>[DeletableCffiNativeHandle](#refcount.interop.DeletableCffiNativeHandle)</code>) – objectiveEvaluator

**Returns:**

- <code>[bool](#bool)</code> – returned result

##### swift2.doc_helper.swg.PlayDatasetEnsembleForecastInput_py

```python
PlayDatasetEnsembleForecastInput_py(efSimulation, dataLibrary, identifiers, dataId, size)
```

PlayDatasetEnsembleForecastInput_py

PlayDatasetEnsembleForecastInput_py: generated wrapper function for API function PlayDatasetEnsembleForecastInput

**Parameters:**

- **efSimulation** (<code>[EnsembleForecastSimulation](#swift2.classes.EnsembleForecastSimulation)</code>) – efSimulation
- **dataLibrary** (<code>[TimeSeriesLibrary](#uchronia.classes.TimeSeriesLibrary)</code>) – dataLibrary
- **identifiers** (<code>[List](#typing.List)\[[str](#str)\]</code>) – identifiers
- **dataId** (<code>[List](#typing.List)\[[str](#str)\]</code>) – dataId
- **size** (<code>[int](#int)</code>) – size

##### swift2.doc_helper.swg.PlayDatasetInputs_py

```python
PlayDatasetInputs_py(simulation, dataLibrary, identifiers, dataId, resampleMethod, size)
```

PlayDatasetInputs_py

PlayDatasetInputs_py: generated wrapper function for API function PlayDatasetInputs

**Parameters:**

- **simulation** (<code>[Simulation](#swift2.classes.Simulation)</code>) – simulation
- **dataLibrary** (<code>[TimeSeriesLibrary](#uchronia.classes.TimeSeriesLibrary)</code>) – dataLibrary
- **identifiers** (<code>[List](#typing.List)\[[str](#str)\]</code>) – identifiers
- **dataId** (<code>[List](#typing.List)\[[str](#str)\]</code>) – dataId
- **resampleMethod** (<code>[List](#typing.List)\[[str](#str)\]</code>) – resampleMethod
- **size** (<code>[int](#int)</code>) – size

##### swift2.doc_helper.swg.PlayDatasetSingleInput_py

```python
PlayDatasetSingleInput_py(efSimulation, dataLibrary, identifiers, dataId, size)
```

PlayDatasetSingleInput_py

PlayDatasetSingleInput_py: generated wrapper function for API function PlayDatasetSingleInput

**Parameters:**

- **efSimulation** (<code>[EnsembleForecastSimulation](#swift2.classes.EnsembleForecastSimulation)</code>) – efSimulation
- **dataLibrary** (<code>[TimeSeriesLibrary](#uchronia.classes.TimeSeriesLibrary)</code>) – dataLibrary
- **identifiers** (<code>[List](#typing.List)\[[str](#str)\]</code>) – identifiers
- **dataId** (<code>[List](#typing.List)\[[str](#str)\]</code>) – dataId
- **size** (<code>[int](#int)</code>) – size

##### swift2.doc_helper.swg.PlayEnsembleForecastTimeSeries_py

```python
PlayEnsembleForecastTimeSeries_py(efSimulation, series, variableIdentifier)
```

PlayEnsembleForecastTimeSeries_py

PlayEnsembleForecastTimeSeries_py: generated wrapper function for API function PlayEnsembleForecastTimeSeries

**Parameters:**

- **efSimulation** (<code>[EnsembleForecastSimulation](#swift2.classes.EnsembleForecastSimulation)</code>) – efSimulation
- **series** (<code>[EnsembleForecastTimeSeries](#uchronia.classes.EnsembleForecastTimeSeries)</code>) – series
- **variableIdentifier** (<code>[str](#str)</code>) – variableIdentifier

##### swift2.doc_helper.swg.Play_py

```python
Play_py(simulation, variableIdentifier, values, geom)
```

Play_py

Play_py: generated wrapper function for API function Play

**Parameters:**

- **simulation** (<code>[Simulation](#swift2.classes.Simulation)</code>) – simulation
- **variableIdentifier** (<code>[str](#str)</code>) – variableIdentifier
- **values** (<code>[ndarray](#numpy.ndarray)</code>) – values
- **geom** (<code>[TimeSeriesGeometryNative](#cinterop.cffi.marshal.TimeSeriesGeometryNative)</code>) – geom

##### swift2.doc_helper.swg.PrepareDualPassForecasting_py

```python
PrepareDualPassForecasting_py(mr, obsValues, obsGeom, errorModelElementId, warmupStart, warmupEnd, requiredWindowPercentage)
```

PrepareDualPassForecasting_py

PrepareDualPassForecasting_py: generated wrapper function for API function PrepareDualPassForecasting

**Parameters:**

- **mr** (<code>[Simulation](#swift2.classes.Simulation)</code>) – mr
- **obsValues** (<code>[ndarray](#numpy.ndarray)</code>) – obsValues
- **obsGeom** (<code>[TimeSeriesGeometryNative](#cinterop.cffi.marshal.TimeSeriesGeometryNative)</code>) – obsGeom
- **errorModelElementId** (<code>[str](#str)</code>) – errorModelElementId
- **warmupStart** (<code>[datetime](#datetime.datetime)</code>) – warmupStart
- **warmupEnd** (<code>[datetime](#datetime.datetime)</code>) – warmupEnd
- **requiredWindowPercentage** (<code>[float](#float)</code>) – requiredWindowPercentage

**Returns:**

- <code>[EnsembleSimulation](#swift2.classes.EnsembleSimulation)</code> – returned result

##### swift2.doc_helper.swg.PrepareERRISForecasting_py

```python
PrepareERRISForecasting_py(mr, obsValues, obsGeom, errorModelElementId, warmupStart, warmupEnd)
```

PrepareERRISForecasting_py

PrepareERRISForecasting_py: generated wrapper function for API function PrepareERRISForecasting

**Parameters:**

- **mr** (<code>[Simulation](#swift2.classes.Simulation)</code>) – mr
- **obsValues** (<code>[ndarray](#numpy.ndarray)</code>) – obsValues
- **obsGeom** (<code>[TimeSeriesGeometryNative](#cinterop.cffi.marshal.TimeSeriesGeometryNative)</code>) – obsGeom
- **errorModelElementId** (<code>[str](#str)</code>) – errorModelElementId
- **warmupStart** (<code>[datetime](#datetime.datetime)</code>) – warmupStart
- **warmupEnd** (<code>[datetime](#datetime.datetime)</code>) – warmupEnd

**Returns:**

- <code>[EnsembleSimulation](#swift2.classes.EnsembleSimulation)</code> – returned result

##### swift2.doc_helper.swg.PrepareEnsembleModelRunner_py

```python
PrepareEnsembleModelRunner_py(simulation, warmupStart, warmupEnd, obsTsValues, obsTsGeom, errorModelElementId)
```

PrepareEnsembleModelRunner_py

PrepareEnsembleModelRunner_py: generated wrapper function for API function PrepareEnsembleModelRunner

**Parameters:**

- **simulation** (<code>[Simulation](#swift2.classes.Simulation)</code>) – simulation
- **warmupStart** (<code>[datetime](#datetime.datetime)</code>) – warmupStart
- **warmupEnd** (<code>[datetime](#datetime.datetime)</code>) – warmupEnd
- **obsTsValues** (<code>[ndarray](#numpy.ndarray)</code>) – obsTsValues
- **obsTsGeom** (<code>[TimeSeriesGeometryNative](#cinterop.cffi.marshal.TimeSeriesGeometryNative)</code>) – obsTsGeom
- **errorModelElementId** (<code>[str](#str)</code>) – errorModelElementId

**Returns:**

- <code>[EnsembleSimulation](#swift2.classes.EnsembleSimulation)</code> – returned result

##### swift2.doc_helper.swg.RecordEnsembleForecastTimeSeries_py

```python
RecordEnsembleForecastTimeSeries_py(efSimulation, variableIdentifier)
```

RecordEnsembleForecastTimeSeries_py

RecordEnsembleForecastTimeSeries_py: generated wrapper function for API function RecordEnsembleForecastTimeSeries

**Parameters:**

- **efSimulation** (<code>[EnsembleForecastSimulation](#swift2.classes.EnsembleForecastSimulation)</code>) – efSimulation
- **variableIdentifier** (<code>[str](#str)</code>) – variableIdentifier

##### swift2.doc_helper.swg.RecordEnsembleForecastToRecorder_py

```python
RecordEnsembleForecastToRecorder_py(efSimulation, variableIdentifiers, dataLibrary, dataIdentifiers, size)
```

RecordEnsembleForecastToRecorder_py

RecordEnsembleForecastToRecorder_py: generated wrapper function for API function RecordEnsembleForecastToRecorder

**Parameters:**

- **efSimulation** (<code>[EnsembleForecastSimulation](#swift2.classes.EnsembleForecastSimulation)</code>) – efSimulation
- **variableIdentifiers** (<code>[List](#typing.List)\[[str](#str)\]</code>) – variableIdentifiers
- **dataLibrary** (<code>[TimeSeriesLibrary](#uchronia.classes.TimeSeriesLibrary)</code>) – dataLibrary
- **dataIdentifiers** (<code>[List](#typing.List)\[[str](#str)\]</code>) – dataIdentifiers
- **size** (<code>[int](#int)</code>) – size

##### swift2.doc_helper.swg.RecordEnsembleModelRunner_py

```python
RecordEnsembleModelRunner_py(emr, variableIdentifier)
```

RecordEnsembleModelRunner_py

RecordEnsembleModelRunner_py: generated wrapper function for API function RecordEnsembleModelRunner

**Parameters:**

- **emr** (<code>[EnsembleSimulation](#swift2.classes.EnsembleSimulation)</code>) – emr
- **variableIdentifier** (<code>[str](#str)</code>) – variableIdentifier

##### swift2.doc_helper.swg.Record_py

```python
Record_py(simulation, variableIdentifier)
```

Record_py

Record_py: generated wrapper function for API function Record

**Parameters:**

- **simulation** (<code>[Simulation](#swift2.classes.Simulation)</code>) – simulation
- **variableIdentifier** (<code>[str](#str)</code>) – variableIdentifier

##### swift2.doc_helper.swg.RegisterAdditionalSwiftDataHandling_py

```python
RegisterAdditionalSwiftDataHandling_py(type)
```

RegisterAdditionalSwiftDataHandling_py

RegisterAdditionalSwiftDataHandling_py: generated wrapper function for API function RegisterAdditionalSwiftDataHandling

**Parameters:**

- **type** (<code>[str](#str)</code>) – type

**Returns:**

- <code>[bool](#bool)</code> – returned result

##### swift2.doc_helper.swg.RegisterExceptionCallbackSwift_py

```python
RegisterExceptionCallbackSwift_py(callback)
```

RegisterExceptionCallbackSwift_py

RegisterExceptionCallbackSwift_py: generated wrapper function for API function RegisterExceptionCallbackSwift

**Parameters:**

- **callback** (<code>[Any](#typing.Any)</code>) – callback

##### swift2.doc_helper.swg.RegisterExceptionCallback_py

```python
RegisterExceptionCallback_py(callback)
```

RegisterExceptionCallback_py

RegisterExceptionCallback_py: generated wrapper function for API function RegisterExceptionCallback

**Parameters:**

- **callback** (<code>[Any](#typing.Any)</code>) – callback

##### swift2.doc_helper.swg.RemoveERRISExclusionPeriod_py

```python
RemoveERRISExclusionPeriod_py(calibObject)
```

RemoveERRISExclusionPeriod_py

RemoveERRISExclusionPeriod_py: generated wrapper function for API function RemoveERRISExclusionPeriod

**Parameters:**

- **calibObject** (<code>[ErrisStagedCalibration](#swift2.classes.ErrisStagedCalibration)</code>) – calibObject

##### swift2.doc_helper.swg.RemoveERRISWarmupPeriod_py

```python
RemoveERRISWarmupPeriod_py(calibObject)
```

RemoveERRISWarmupPeriod_py

RemoveERRISWarmupPeriod_py: generated wrapper function for API function RemoveERRISWarmupPeriod

**Parameters:**

- **calibObject** (<code>[ErrisStagedCalibration](#swift2.classes.ErrisStagedCalibration)</code>) – calibObject

##### swift2.doc_helper.swg.RemoveMAERRISExclusionPeriod_py

```python
RemoveMAERRISExclusionPeriod_py(calibObject)
```

RemoveMAERRISExclusionPeriod_py

RemoveMAERRISExclusionPeriod_py: generated wrapper function for API function RemoveMAERRISExclusionPeriod

**Parameters:**

- **calibObject** (<code>[MaerrisStagedCalibration](#swift2.classes.MaerrisStagedCalibration)</code>) – calibObject

##### swift2.doc_helper.swg.RemoveMAERRISWarmupPeriod_py

```python
RemoveMAERRISWarmupPeriod_py(calibObject)
```

RemoveMAERRISWarmupPeriod_py

RemoveMAERRISWarmupPeriod_py: generated wrapper function for API function RemoveMAERRISWarmupPeriod

**Parameters:**

- **calibObject** (<code>[MaerrisStagedCalibration](#swift2.classes.MaerrisStagedCalibration)</code>) – calibObject

##### swift2.doc_helper.swg.RemoveModel_py

```python
RemoveModel_py(simulation, fullModelId)
```

RemoveModel_py

RemoveModel_py: generated wrapper function for API function RemoveModel

**Parameters:**

- **simulation** (<code>[Simulation](#swift2.classes.Simulation)</code>) – simulation
- **fullModelId** (<code>[str](#str)</code>) – fullModelId

##### swift2.doc_helper.swg.RemovePlayedTimeSeries_py

```python
RemovePlayedTimeSeries_py(modelInstance, variableIdentifier)
```

RemovePlayedTimeSeries_py

RemovePlayedTimeSeries_py: generated wrapper function for API function RemovePlayedTimeSeries

**Parameters:**

- **modelInstance** (<code>[Simulation](#swift2.classes.Simulation)</code>) – modelInstance
- **variableIdentifier** (<code>[str](#str)</code>) – variableIdentifier

##### swift2.doc_helper.swg.RemoveRecorder_py

```python
RemoveRecorder_py(modelInstance, variableIdentifier)
```

RemoveRecorder_py

RemoveRecorder_py: generated wrapper function for API function RemoveRecorder

**Parameters:**

- **modelInstance** (<code>[Simulation](#swift2.classes.Simulation)</code>) – modelInstance
- **variableIdentifier** (<code>[str](#str)</code>) – variableIdentifier

##### swift2.doc_helper.swg.RemoveStateInitializerModelRunner_py

```python
RemoveStateInitializerModelRunner_py(modelSimulation)
```

RemoveStateInitializerModelRunner_py

RemoveStateInitializerModelRunner_py: generated wrapper function for API function RemoveStateInitializerModelRunner

**Parameters:**

- **modelSimulation** (<code>[Simulation](#swift2.classes.Simulation)</code>) – modelSimulation

##### swift2.doc_helper.swg.RemoveStorageDischargeRelationship_py

```python
RemoveStorageDischargeRelationship_py(simulation, elementId, relationshipType)
```

RemoveStorageDischargeRelationship_py

RemoveStorageDischargeRelationship_py: generated wrapper function for API function RemoveStorageDischargeRelationship

**Parameters:**

- **simulation** (<code>[Simulation](#swift2.classes.Simulation)</code>) – simulation
- **elementId** (<code>[str](#str)</code>) – elementId
- **relationshipType** (<code>[str](#str)</code>) – relationshipType

##### swift2.doc_helper.swg.ResetModelStates_py

```python
ResetModelStates_py(simulation)
```

ResetModelStates_py

ResetModelStates_py: generated wrapper function for API function ResetModelStates

**Parameters:**

- **simulation** (<code>[Simulation](#swift2.classes.Simulation)</code>) – simulation

##### swift2.doc_helper.swg.SaveMemoryStatesToFile_py

```python
SaveMemoryStatesToFile_py(memoryStates, filePath, format)
```

SaveMemoryStatesToFile_py

SaveMemoryStatesToFile_py: generated wrapper function for API function SaveMemoryStatesToFile

**Parameters:**

- **memoryStates** (<code>[MemoryStates](#swift2.classes.MemoryStates)</code>) – memoryStates
- **filePath** (<code>[str](#str)</code>) – filePath
- **format** (<code>[str](#str)</code>) – format

##### swift2.doc_helper.swg.SaveModelSimulationToJson_py

```python
SaveModelSimulationToJson_py(simulation, jsonFilePath)
```

SaveModelSimulationToJson_py

SaveModelSimulationToJson_py: generated wrapper function for API function SaveModelSimulationToJson

**Parameters:**

- **simulation** (<code>[Simulation](#swift2.classes.Simulation)</code>) – simulation
- **jsonFilePath** (<code>[str](#str)</code>) – jsonFilePath

##### swift2.doc_helper.swg.SaveParameterizer_py

```python
SaveParameterizer_py(parameterizer, filepath)
```

SaveParameterizer_py

SaveParameterizer_py: generated wrapper function for API function SaveParameterizer

**Parameters:**

- **parameterizer** (<code>[HypercubeParameteriser](#swift2.classes.HypercubeParameteriser)</code>) – parameterizer
- **filepath** (<code>[str](#str)</code>) – filepath

##### swift2.doc_helper.swg.SetChannelRoutingModel_py

```python
SetChannelRoutingModel_py(simulation, newModelId)
```

SetChannelRoutingModel_py

SetChannelRoutingModel_py: generated wrapper function for API function SetChannelRoutingModel

**Parameters:**

- **simulation** (<code>[Simulation](#swift2.classes.Simulation)</code>) – simulation
- **newModelId** (<code>[str](#str)</code>) – newModelId

##### swift2.doc_helper.swg.SetDefaultMaxThreadsWila_py

```python
SetDefaultMaxThreadsWila_py(nThreads)
```

SetDefaultMaxThreadsWila_py

SetDefaultMaxThreadsWila_py: generated wrapper function for API function SetDefaultMaxThreadsWila

**Parameters:**

- **nThreads** (<code>[int](#int)</code>) – nThreads

##### swift2.doc_helper.swg.SetDefaultParameters_py

```python
SetDefaultParameters_py(hypercubeParameterizer, modelId)
```

SetDefaultParameters_py

SetDefaultParameters_py: generated wrapper function for API function SetDefaultParameters

**Parameters:**

- **hypercubeParameterizer** (<code>[HypercubeParameteriser](#swift2.classes.HypercubeParameteriser)</code>) – hypercubeParameterizer
- **modelId** (<code>[str](#str)</code>) – modelId

##### swift2.doc_helper.swg.SetERRISCensOptions_py

```python
SetERRISCensOptions_py(calibObject, censOpt)
```

SetERRISCensOptions_py

SetERRISCensOptions_py: generated wrapper function for API function SetERRISCensOptions

**Parameters:**

- **calibObject** (<code>[ErrisStagedCalibration](#swift2.classes.ErrisStagedCalibration)</code>) – calibObject
- **censOpt** (<code>[float](#float)</code>) – censOpt

##### swift2.doc_helper.swg.SetERRISErrorCorrectionParameterSpace_py

```python
SetERRISErrorCorrectionParameterSpace_py(calibObject, errisParams)
```

SetERRISErrorCorrectionParameterSpace_py

SetERRISErrorCorrectionParameterSpace_py: generated wrapper function for API function SetERRISErrorCorrectionParameterSpace

**Parameters:**

- **calibObject** (<code>[ErrisStagedCalibration](#swift2.classes.ErrisStagedCalibration)</code>) – calibObject
- **errisParams** (<code>[HypercubeParameteriser](#swift2.classes.HypercubeParameteriser)</code>) – errisParams

##### swift2.doc_helper.swg.SetERRISEstimationPeriod_py

```python
SetERRISEstimationPeriod_py(calibObject, estimationStart, estimationEnd)
```

SetERRISEstimationPeriod_py

SetERRISEstimationPeriod_py: generated wrapper function for API function SetERRISEstimationPeriod

**Parameters:**

- **calibObject** (<code>[ErrisStagedCalibration](#swift2.classes.ErrisStagedCalibration)</code>) – calibObject
- **estimationStart** (<code>[datetime](#datetime.datetime)</code>) – estimationStart
- **estimationEnd** (<code>[datetime](#datetime.datetime)</code>) – estimationEnd

##### swift2.doc_helper.swg.SetERRISExclusionPeriod_py

```python
SetERRISExclusionPeriod_py(calibObject, exclusionStart, exclusionEnd)
```

SetERRISExclusionPeriod_py

SetERRISExclusionPeriod_py: generated wrapper function for API function SetERRISExclusionPeriod

**Parameters:**

- **calibObject** (<code>[ErrisStagedCalibration](#swift2.classes.ErrisStagedCalibration)</code>) – calibObject
- **exclusionStart** (<code>[datetime](#datetime.datetime)</code>) – exclusionStart
- **exclusionEnd** (<code>[datetime](#datetime.datetime)</code>) – exclusionEnd

##### swift2.doc_helper.swg.SetERRISHydrologicParameterSpace_py

```python
SetERRISHydrologicParameterSpace_py(calibObject, hydroParams)
```

SetERRISHydrologicParameterSpace_py

SetERRISHydrologicParameterSpace_py: generated wrapper function for API function SetERRISHydrologicParameterSpace

**Parameters:**

- **calibObject** (<code>[ErrisStagedCalibration](#swift2.classes.ErrisStagedCalibration)</code>) – calibObject
- **hydroParams** (<code>[HypercubeParameteriser](#swift2.classes.HypercubeParameteriser)</code>) – hydroParams

##### swift2.doc_helper.swg.SetERRISMaxObservation_py

```python
SetERRISMaxObservation_py(calibObject, maxObs)
```

SetERRISMaxObservation_py

SetERRISMaxObservation_py: generated wrapper function for API function SetERRISMaxObservation

**Parameters:**

- **calibObject** (<code>[ErrisStagedCalibration](#swift2.classes.ErrisStagedCalibration)</code>) – calibObject
- **maxObs** (<code>[float](#float)</code>) – maxObs

##### swift2.doc_helper.swg.SetERRISVerboseCalibration_py

```python
SetERRISVerboseCalibration_py(calibObject, verboseCalibrationLog)
```

SetERRISVerboseCalibration_py

SetERRISVerboseCalibration_py: generated wrapper function for API function SetERRISVerboseCalibration

**Parameters:**

- **calibObject** (<code>[ErrisStagedCalibration](#swift2.classes.ErrisStagedCalibration)</code>) – calibObject
- **verboseCalibrationLog** (<code>[bool](#bool)</code>) – verboseCalibrationLog

##### swift2.doc_helper.swg.SetERRISWarmupPeriod_py

```python
SetERRISWarmupPeriod_py(calibObject, warmupStart, warmupEnd)
```

SetERRISWarmupPeriod_py

SetERRISWarmupPeriod_py: generated wrapper function for API function SetERRISWarmupPeriod

**Parameters:**

- **calibObject** (<code>[ErrisStagedCalibration](#swift2.classes.ErrisStagedCalibration)</code>) – calibObject
- **warmupStart** (<code>[datetime](#datetime.datetime)</code>) – warmupStart
- **warmupEnd** (<code>[datetime](#datetime.datetime)</code>) – warmupEnd

##### swift2.doc_helper.swg.SetErrorCorrectionModel_py

```python
SetErrorCorrectionModel_py(simulation, newModelId, elementId, length, seed)
```

SetErrorCorrectionModel_py

SetErrorCorrectionModel_py: generated wrapper function for API function SetErrorCorrectionModel

**Parameters:**

- **simulation** (<code>[Simulation](#swift2.classes.Simulation)</code>) – simulation
- **newModelId** (<code>[str](#str)</code>) – newModelId
- **elementId** (<code>[str](#str)</code>) – elementId
- **length** (<code>[int](#int)</code>) – length
- **seed** (<code>[int](#int)</code>) – seed

##### swift2.doc_helper.swg.SetLogLikelihoodMixtureVariableNames_py

```python
SetLogLikelihoodMixtureVariableNames_py(a, b, m, s1, s2, w, maxobs, ct, censopt)
```

SetLogLikelihoodMixtureVariableNames_py

SetLogLikelihoodMixtureVariableNames_py: generated wrapper function for API function SetLogLikelihoodMixtureVariableNames

**Parameters:**

- **a** (<code>[str](#str)</code>) – a
- **b** (<code>[str](#str)</code>) – b
- **m** (<code>[str](#str)</code>) – m
- **s1** (<code>[str](#str)</code>) – s1
- **s2** (<code>[str](#str)</code>) – s2
- **w** (<code>[str](#str)</code>) – w
- **maxobs** (<code>[str](#str)</code>) – maxobs
- **ct** (<code>[str](#str)</code>) – ct
- **censopt** (<code>[str](#str)</code>) – censopt

##### swift2.doc_helper.swg.SetLogLikelihoodVariableNames_py

```python
SetLogLikelihoodVariableNames_py(a, b, m, s, maxobs, ct, censopt)
```

SetLogLikelihoodVariableNames_py

SetLogLikelihoodVariableNames_py: generated wrapper function for API function SetLogLikelihoodVariableNames

**Parameters:**

- **a** (<code>[str](#str)</code>) – a
- **b** (<code>[str](#str)</code>) – b
- **m** (<code>[str](#str)</code>) – m
- **s** (<code>[str](#str)</code>) – s
- **maxobs** (<code>[str](#str)</code>) – maxobs
- **ct** (<code>[str](#str)</code>) – ct
- **censopt** (<code>[str](#str)</code>) – censopt

##### swift2.doc_helper.swg.SetLogLikelihoodXVariableNames_py

```python
SetLogLikelihoodXVariableNames_py(a, b, m, s1, s2, w, maxobs, ct, censopt)
```

SetLogLikelihoodXVariableNames_py

SetLogLikelihoodXVariableNames_py: generated wrapper function for API function SetLogLikelihoodXVariableNames

**Parameters:**

- **a** (<code>[str](#str)</code>) – a
- **b** (<code>[str](#str)</code>) – b
- **m** (<code>[str](#str)</code>) – m
- **s1** (<code>[str](#str)</code>) – s1
- **s2** (<code>[str](#str)</code>) – s2
- **w** (<code>[str](#str)</code>) – w
- **maxobs** (<code>[str](#str)</code>) – maxobs
- **ct** (<code>[str](#str)</code>) – ct
- **censopt** (<code>[str](#str)</code>) – censopt

##### swift2.doc_helper.swg.SetMAERRISCensOptions_py

```python
SetMAERRISCensOptions_py(calibObject, censOpt)
```

SetMAERRISCensOptions_py

SetMAERRISCensOptions_py: generated wrapper function for API function SetMAERRISCensOptions

**Parameters:**

- **calibObject** (<code>[MaerrisStagedCalibration](#swift2.classes.MaerrisStagedCalibration)</code>) – calibObject
- **censOpt** (<code>[float](#float)</code>) – censOpt

##### swift2.doc_helper.swg.SetMAERRISErrorCorrectionParameterSpace_py

```python
SetMAERRISErrorCorrectionParameterSpace_py(calibObject, maerrisParams)
```

SetMAERRISErrorCorrectionParameterSpace_py

SetMAERRISErrorCorrectionParameterSpace_py: generated wrapper function for API function SetMAERRISErrorCorrectionParameterSpace

**Parameters:**

- **calibObject** (<code>[MaerrisStagedCalibration](#swift2.classes.MaerrisStagedCalibration)</code>) – calibObject
- **maerrisParams** (<code>[HypercubeParameteriser](#swift2.classes.HypercubeParameteriser)</code>) – maerrisParams

##### swift2.doc_helper.swg.SetMAERRISEstimationPeriod_py

```python
SetMAERRISEstimationPeriod_py(calibObject, estimationStart, estimationEnd)
```

SetMAERRISEstimationPeriod_py

SetMAERRISEstimationPeriod_py: generated wrapper function for API function SetMAERRISEstimationPeriod

**Parameters:**

- **calibObject** (<code>[MaerrisStagedCalibration](#swift2.classes.MaerrisStagedCalibration)</code>) – calibObject
- **estimationStart** (<code>[datetime](#datetime.datetime)</code>) – estimationStart
- **estimationEnd** (<code>[datetime](#datetime.datetime)</code>) – estimationEnd

##### swift2.doc_helper.swg.SetMAERRISExclusionPeriod_py

```python
SetMAERRISExclusionPeriod_py(calibObject, exclusionStart, exclusionEnd)
```

SetMAERRISExclusionPeriod_py

SetMAERRISExclusionPeriod_py: generated wrapper function for API function SetMAERRISExclusionPeriod

**Parameters:**

- **calibObject** (<code>[MaerrisStagedCalibration](#swift2.classes.MaerrisStagedCalibration)</code>) – calibObject
- **exclusionStart** (<code>[datetime](#datetime.datetime)</code>) – exclusionStart
- **exclusionEnd** (<code>[datetime](#datetime.datetime)</code>) – exclusionEnd

##### swift2.doc_helper.swg.SetMAERRISHydrologicParameterSpace_py

```python
SetMAERRISHydrologicParameterSpace_py(calibObject, hydroParams)
```

SetMAERRISHydrologicParameterSpace_py

SetMAERRISHydrologicParameterSpace_py: generated wrapper function for API function SetMAERRISHydrologicParameterSpace

**Parameters:**

- **calibObject** (<code>[MaerrisStagedCalibration](#swift2.classes.MaerrisStagedCalibration)</code>) – calibObject
- **hydroParams** (<code>[HypercubeParameteriser](#swift2.classes.HypercubeParameteriser)</code>) – hydroParams

##### swift2.doc_helper.swg.SetMAERRISMaxObservation_py

```python
SetMAERRISMaxObservation_py(calibObject, maxObs)
```

SetMAERRISMaxObservation_py

SetMAERRISMaxObservation_py: generated wrapper function for API function SetMAERRISMaxObservation

**Parameters:**

- **calibObject** (<code>[MaerrisStagedCalibration](#swift2.classes.MaerrisStagedCalibration)</code>) – calibObject
- **maxObs** (<code>[float](#float)</code>) – maxObs

##### swift2.doc_helper.swg.SetMAERRISRestrictionOn_py

```python
SetMAERRISRestrictionOn_py(calibObject, restrictionOn)
```

SetMAERRISRestrictionOn_py

SetMAERRISRestrictionOn_py: generated wrapper function for API function SetMAERRISRestrictionOn

**Parameters:**

- **calibObject** (<code>[MaerrisStagedCalibration](#swift2.classes.MaerrisStagedCalibration)</code>) – calibObject
- **restrictionOn** (<code>[bool](#bool)</code>) – restrictionOn

##### swift2.doc_helper.swg.SetMAERRISS2Window_py

```python
SetMAERRISS2Window_py(calibObject, s2Window)
```

SetMAERRISS2Window_py

SetMAERRISS2Window_py: generated wrapper function for API function SetMAERRISS2Window

**Parameters:**

- **calibObject** (<code>[MaerrisStagedCalibration](#swift2.classes.MaerrisStagedCalibration)</code>) – calibObject
- **s2Window** (<code>[float](#float)</code>) – s2Window

##### swift2.doc_helper.swg.SetMAERRISVerboseCalibration_py

```python
SetMAERRISVerboseCalibration_py(calibObject, verboseCalibrationLog)
```

SetMAERRISVerboseCalibration_py

SetMAERRISVerboseCalibration_py: generated wrapper function for API function SetMAERRISVerboseCalibration

**Parameters:**

- **calibObject** (<code>[MaerrisStagedCalibration](#swift2.classes.MaerrisStagedCalibration)</code>) – calibObject
- **verboseCalibrationLog** (<code>[bool](#bool)</code>) – verboseCalibrationLog

##### swift2.doc_helper.swg.SetMAERRISWarmupPeriod_py

```python
SetMAERRISWarmupPeriod_py(calibObject, warmupStart, warmupEnd)
```

SetMAERRISWarmupPeriod_py

SetMAERRISWarmupPeriod_py: generated wrapper function for API function SetMAERRISWarmupPeriod

**Parameters:**

- **calibObject** (<code>[MaerrisStagedCalibration](#swift2.classes.MaerrisStagedCalibration)</code>) – calibObject
- **warmupStart** (<code>[datetime](#datetime.datetime)</code>) – warmupStart
- **warmupEnd** (<code>[datetime](#datetime.datetime)</code>) – warmupEnd

##### swift2.doc_helper.swg.SetMaxParameterValue_py

```python
SetMaxParameterValue_py(hypercubeParameterizer, variableName, value)
```

SetMaxParameterValue_py

SetMaxParameterValue_py: generated wrapper function for API function SetMaxParameterValue

**Parameters:**

- **hypercubeParameterizer** (<code>[HypercubeParameteriser](#swift2.classes.HypercubeParameteriser)</code>) – hypercubeParameterizer
- **variableName** (<code>[str](#str)</code>) – variableName
- **value** (<code>[float](#float)</code>) – value

##### swift2.doc_helper.swg.SetMaxThreadsOptimizerWila_py

```python
SetMaxThreadsOptimizerWila_py(optimizer, nThreads)
```

SetMaxThreadsOptimizerWila_py

SetMaxThreadsOptimizerWila_py: generated wrapper function for API function SetMaxThreadsOptimizerWila

**Parameters:**

- **optimizer** (<code>[Optimiser](#swift2.classes.Optimiser)</code>) – optimizer
- **nThreads** (<code>[int](#int)</code>) – nThreads

##### swift2.doc_helper.swg.SetMemoryStates_py

```python
SetMemoryStates_py(simulation, memoryStates)
```

SetMemoryStates_py

SetMemoryStates_py: generated wrapper function for API function SetMemoryStates

**Parameters:**

- **simulation** (<code>[Simulation](#swift2.classes.Simulation)</code>) – simulation
- **memoryStates** (<code>[MemoryStates](#swift2.classes.MemoryStates)</code>) – memoryStates

##### swift2.doc_helper.swg.SetMinParameterValue_py

```python
SetMinParameterValue_py(hypercubeParameterizer, variableName, value)
```

SetMinParameterValue_py

SetMinParameterValue_py: generated wrapper function for API function SetMinParameterValue

**Parameters:**

- **hypercubeParameterizer** (<code>[HypercubeParameteriser](#swift2.classes.HypercubeParameteriser)</code>) – hypercubeParameterizer
- **variableName** (<code>[str](#str)</code>) – variableName
- **value** (<code>[float](#float)</code>) – value

##### swift2.doc_helper.swg.SetOptimizerLoggerWila_py

```python
SetOptimizerLoggerWila_py(optimizer, type)
```

SetOptimizerLoggerWila_py

SetOptimizerLoggerWila_py: generated wrapper function for API function SetOptimizerLoggerWila

**Parameters:**

- **optimizer** (<code>[Optimiser](#swift2.classes.Optimiser)</code>) – optimizer
- **type** (<code>[str](#str)</code>) – type

##### swift2.doc_helper.swg.SetParameterDefinition_py

```python
SetParameterDefinition_py(hypercubeParameterizer, variableName, min, max, value)
```

SetParameterDefinition_py

SetParameterDefinition_py: generated wrapper function for API function SetParameterDefinition

**Parameters:**

- **hypercubeParameterizer** (<code>[HypercubeParameteriser](#swift2.classes.HypercubeParameteriser)</code>) – hypercubeParameterizer
- **variableName** (<code>[str](#str)</code>) – variableName
- **min** (<code>[float](#float)</code>) – min
- **max** (<code>[float](#float)</code>) – max
- **value** (<code>[float](#float)</code>) – value

##### swift2.doc_helper.swg.SetParameterValue_py

```python
SetParameterValue_py(hypercubeParameterizer, variableName, value)
```

SetParameterValue_py

SetParameterValue_py: generated wrapper function for API function SetParameterValue

**Parameters:**

- **hypercubeParameterizer** (<code>[HypercubeParameteriser](#swift2.classes.HypercubeParameteriser)</code>) – hypercubeParameterizer
- **variableName** (<code>[str](#str)</code>) – variableName
- **value** (<code>[float](#float)</code>) – value

##### swift2.doc_helper.swg.SetReservoirGeometry_py

```python
SetReservoirGeometry_py(simulation, elementId, numEntries, level, storage, area)
```

SetReservoirGeometry_py

SetReservoirGeometry_py: generated wrapper function for API function SetReservoirGeometry

**Parameters:**

- **simulation** (<code>[Simulation](#swift2.classes.Simulation)</code>) – simulation
- **elementId** (<code>[str](#str)</code>) – elementId
- **numEntries** (<code>[int](#int)</code>) – numEntries
- **level** (<code>[ndarray](#numpy.ndarray)</code>) – level
- **storage** (<code>[ndarray](#numpy.ndarray)</code>) – storage
- **area** (<code>[ndarray](#numpy.ndarray)</code>) – area

##### swift2.doc_helper.swg.SetReservoirMaxDischarge_py

```python
SetReservoirMaxDischarge_py(simulation, elementId, numEntries, level, discharge)
```

SetReservoirMaxDischarge_py

SetReservoirMaxDischarge_py: generated wrapper function for API function SetReservoirMaxDischarge

**Parameters:**

- **simulation** (<code>[Simulation](#swift2.classes.Simulation)</code>) – simulation
- **elementId** (<code>[str](#str)</code>) – elementId
- **numEntries** (<code>[int](#int)</code>) – numEntries
- **level** (<code>[ndarray](#numpy.ndarray)</code>) – level
- **discharge** (<code>[ndarray](#numpy.ndarray)</code>) – discharge

##### swift2.doc_helper.swg.SetReservoirMinDischarge_py

```python
SetReservoirMinDischarge_py(simulation, elementId, numEntries, level, discharge)
```

SetReservoirMinDischarge_py

SetReservoirMinDischarge_py: generated wrapper function for API function SetReservoirMinDischarge

**Parameters:**

- **simulation** (<code>[Simulation](#swift2.classes.Simulation)</code>) – simulation
- **elementId** (<code>[str](#str)</code>) – elementId
- **numEntries** (<code>[int](#int)</code>) – numEntries
- **level** (<code>[ndarray](#numpy.ndarray)</code>) – level
- **discharge** (<code>[ndarray](#numpy.ndarray)</code>) – discharge

##### swift2.doc_helper.swg.SetReservoirModel_py

```python
SetReservoirModel_py(simulation, newModelId, elementId)
```

SetReservoirModel_py

SetReservoirModel_py: generated wrapper function for API function SetReservoirModel

**Parameters:**

- **simulation** (<code>[Simulation](#swift2.classes.Simulation)</code>) – simulation
- **newModelId** (<code>[str](#str)</code>) – newModelId
- **elementId** (<code>[str](#str)</code>) – elementId

##### swift2.doc_helper.swg.SetReservoirOpsReleaseCurve_py

```python
SetReservoirOpsReleaseCurve_py(simulation, elementId, numEntries, level, discharge)
```

SetReservoirOpsReleaseCurve_py

SetReservoirOpsReleaseCurve_py: generated wrapper function for API function SetReservoirOpsReleaseCurve

**Parameters:**

- **simulation** (<code>[Simulation](#swift2.classes.Simulation)</code>) – simulation
- **elementId** (<code>[str](#str)</code>) – elementId
- **numEntries** (<code>[int](#int)</code>) – numEntries
- **level** (<code>[ndarray](#numpy.ndarray)</code>) – level
- **discharge** (<code>[ndarray](#numpy.ndarray)</code>) – discharge

##### swift2.doc_helper.swg.SetRunoffPostProcessingModel_py

```python
SetRunoffPostProcessingModel_py(src, newModelId, elementId)
```

SetRunoffPostProcessingModel_py

SetRunoffPostProcessingModel_py: generated wrapper function for API function SetRunoffPostProcessingModel

**Parameters:**

- **src** (<code>[Simulation](#swift2.classes.Simulation)</code>) – src
- **newModelId** (<code>[str](#str)</code>) – newModelId
- **elementId** (<code>[str](#str)</code>) – elementId

##### swift2.doc_helper.swg.SetSeedForModel_py

```python
SetSeedForModel_py(simulation, modelObjectIdentifier, seed)
```

SetSeedForModel_py

SetSeedForModel_py: generated wrapper function for API function SetSeedForModel

**Parameters:**

- **simulation** (<code>[Simulation](#swift2.classes.Simulation)</code>) – simulation
- **modelObjectIdentifier** (<code>[str](#str)</code>) – modelObjectIdentifier
- **seed** (<code>[int](#int)</code>) – seed

##### swift2.doc_helper.swg.SetSpan_py

```python
SetSpan_py(simulation, start, end)
```

SetSpan_py

SetSpan_py: generated wrapper function for API function SetSpan

**Parameters:**

- **simulation** (<code>[Any](#typing.Any)</code>) – simulation
- **start** (<code>[datetime](#datetime.datetime)</code>) – start
- **end** (<code>[datetime](#datetime.datetime)</code>) – end

##### swift2.doc_helper.swg.SetSubareaInputsPreprocessorModel_py

```python
SetSubareaInputsPreprocessorModel_py(simulation, newModelId, subAreaId)
```

SetSubareaInputsPreprocessorModel_py

SetSubareaInputsPreprocessorModel_py: generated wrapper function for API function SetSubareaInputsPreprocessorModel

**Parameters:**

- **simulation** (<code>[Simulation](#swift2.classes.Simulation)</code>) – simulation
- **newModelId** (<code>[str](#str)</code>) – newModelId
- **subAreaId** (<code>[str](#str)</code>) – subAreaId

##### swift2.doc_helper.swg.SetTimeStep_py

```python
SetTimeStep_py(simulation, timeStepName)
```

SetTimeStep_py

SetTimeStep_py: generated wrapper function for API function SetTimeStep

**Parameters:**

- **simulation** (<code>[Any](#typing.Any)</code>) – simulation
- **timeStepName** (<code>[str](#str)</code>) – timeStepName

##### swift2.doc_helper.swg.SetValueStateInitializer_py

```python
SetValueStateInitializer_py(stateInitializer, identifier, value)
```

SetValueStateInitializer_py

SetValueStateInitializer_py: generated wrapper function for API function SetValueStateInitializer

**Parameters:**

- **stateInitializer** (<code>[StateInitialiser](#swift2.classes.StateInitialiser)</code>) – stateInitializer
- **identifier** (<code>[str](#str)</code>) – identifier
- **value** (<code>[float](#float)</code>) – value

##### swift2.doc_helper.swg.SetVariableBool_py

```python
SetVariableBool_py(simulation, variableIdentifier, value)
```

SetVariableBool_py

SetVariableBool_py: generated wrapper function for API function SetVariableBool

**Parameters:**

- **simulation** (<code>[Simulation](#swift2.classes.Simulation)</code>) – simulation
- **variableIdentifier** (<code>[str](#str)</code>) – variableIdentifier
- **value** (<code>[bool](#bool)</code>) – value

##### swift2.doc_helper.swg.SetVariableInt_py

```python
SetVariableInt_py(simulation, variableIdentifier, value)
```

SetVariableInt_py

SetVariableInt_py: generated wrapper function for API function SetVariableInt

**Parameters:**

- **simulation** (<code>[Simulation](#swift2.classes.Simulation)</code>) – simulation
- **variableIdentifier** (<code>[str](#str)</code>) – variableIdentifier
- **value** (<code>[int](#int)</code>) – value

##### swift2.doc_helper.swg.SetVariable_py

```python
SetVariable_py(simulation, variableIdentifier, value)
```

SetVariable_py

SetVariable_py: generated wrapper function for API function SetVariable

**Parameters:**

- **simulation** (<code>[Simulation](#swift2.classes.Simulation)</code>) – simulation
- **variableIdentifier** (<code>[str](#str)</code>) – variableIdentifier
- **value** (<code>[float](#float)</code>) – value

##### swift2.doc_helper.swg.SetupEnsembleModelRunner_py

```python
SetupEnsembleModelRunner_py(emr, forecastStart, ensembleSize, forecastHorizonLength)
```

SetupEnsembleModelRunner_py

SetupEnsembleModelRunner_py: generated wrapper function for API function SetupEnsembleModelRunner

**Parameters:**

- **emr** (<code>[EnsembleSimulation](#swift2.classes.EnsembleSimulation)</code>) – emr
- **forecastStart** (<code>[datetime](#datetime.datetime)</code>) – forecastStart
- **ensembleSize** (<code>[int](#int)</code>) – ensembleSize
- **forecastHorizonLength** (<code>[int](#int)</code>) – forecastHorizonLength

##### swift2.doc_helper.swg.ShowParameters_py

```python
ShowParameters_py(p, pnames, regex, startsWith)
```

ShowParameters_py

ShowParameters_py: generated wrapper function for API function ShowParameters

**Parameters:**

- **p** (<code>[HypercubeParameteriser](#swift2.classes.HypercubeParameteriser)</code>) – p
- **pnames** (<code>[List](#typing.List)</code>) – pnames
- **regex** (<code>[bool](#bool)</code>) – regex
- **startsWith** (<code>[bool](#bool)</code>) – startsWith

##### swift2.doc_helper.swg.SnapshotMemoryStates_py

```python
SnapshotMemoryStates_py(simulation)
```

SnapshotMemoryStates_py

SnapshotMemoryStates_py: generated wrapper function for API function SnapshotMemoryStates

**Parameters:**

- **simulation** (<code>[Simulation](#swift2.classes.Simulation)</code>) – simulation

**Returns:**

- <code>[MemoryStates](#swift2.classes.MemoryStates)</code> – returned result

##### swift2.doc_helper.swg.SortSetOfScoresBy_py

```python
SortSetOfScoresBy_py(vectorScores, scoreName)
```

SortSetOfScoresBy_py

SortSetOfScoresBy_py: generated wrapper function for API function SortSetOfScoresBy

**Parameters:**

- **vectorScores** (<code>[VectorObjectiveScores](#swift2.classes.VectorObjectiveScores)</code>) – vectorScores
- **scoreName** (<code>[str](#str)</code>) – scoreName

**Returns:**

- <code>[VectorObjectiveScores](#swift2.classes.VectorObjectiveScores)</code> – returned result

##### swift2.doc_helper.swg.SortSimulationElementsByRunOrder_py

```python
SortSimulationElementsByRunOrder_py(simulation, elementIds, numElements, orderingMethod)
```

SortSimulationElementsByRunOrder_py

SortSimulationElementsByRunOrder_py: generated wrapper function for API function SortSimulationElementsByRunOrder

##### swift2.doc_helper.swg.SubsetModel_py

```python
SubsetModel_py(simulation, elementName, selectNetworkAboveElement, includeElementInSelection, invertSelection, terminationElements, terminationElementsLength)
```

SubsetModel_py

SubsetModel_py: generated wrapper function for API function SubsetModel

**Parameters:**

- **simulation** (<code>[Simulation](#swift2.classes.Simulation)</code>) – simulation
- **elementName** (<code>[str](#str)</code>) – elementName
- **selectNetworkAboveElement** (<code>[bool](#bool)</code>) – selectNetworkAboveElement
- **includeElementInSelection** (<code>[bool](#bool)</code>) – includeElementInSelection
- **invertSelection** (<code>[bool](#bool)</code>) – invertSelection
- **terminationElements** (<code>[List](#typing.List)\[[str](#str)\]</code>) – terminationElements
- **terminationElementsLength** (<code>[int](#int)</code>) – terminationElementsLength

**Returns:**

- <code>[Simulation](#swift2.classes.Simulation)</code> – returned result

##### swift2.doc_helper.swg.SupportsThreadSafeCloning_py

```python
SupportsThreadSafeCloning_py(parameterizer)
```

SupportsThreadSafeCloning_py

SupportsThreadSafeCloning_py: generated wrapper function for API function SupportsThreadSafeCloning

**Parameters:**

- **parameterizer** (<code>[Any](#typing.Any)</code>) – parameterizer

**Returns:**

- <code>[bool](#bool)</code> – returned result

##### swift2.doc_helper.swg.SwapRunoffModel_py

```python
SwapRunoffModel_py(simulation, newModelId)
```

SwapRunoffModel_py

SwapRunoffModel_py: generated wrapper function for API function SwapRunoffModel

**Parameters:**

- **simulation** (<code>[Simulation](#swift2.classes.Simulation)</code>) – simulation
- **newModelId** (<code>[str](#str)</code>) – newModelId

**Returns:**

- <code>[Simulation](#swift2.classes.Simulation)</code> – returned result

##### swift2.doc_helper.swg.TagParameterizer_py

```python
TagParameterizer_py(p, tag)
```

TagParameterizer_py

TagParameterizer_py: generated wrapper function for API function TagParameterizer

**Parameters:**

- **p** (<code>[HypercubeParameteriser](#swift2.classes.HypercubeParameteriser)</code>) – p
- **tag** (<code>[str](#str)</code>) – tag

##### swift2.doc_helper.swg.UntransformHypercubeParameterizer_py

```python
UntransformHypercubeParameterizer_py(hypercubeParameterizer)
```

UntransformHypercubeParameterizer_py

UntransformHypercubeParameterizer_py: generated wrapper function for API function UntransformHypercubeParameterizer

**Parameters:**

- **hypercubeParameterizer** (<code>[HypercubeParameteriser](#swift2.classes.HypercubeParameteriser)</code>) – hypercubeParameterizer

**Returns:**

- <code>[HypercubeParameteriser](#swift2.classes.HypercubeParameteriser)</code> – returned result

##### swift2.doc_helper.swg.UnwrapObjectiveEvaluatorWila_py

```python
UnwrapObjectiveEvaluatorWila_py(objective)
```

UnwrapObjectiveEvaluatorWila_py

UnwrapObjectiveEvaluatorWila_py: generated wrapper function for API function UnwrapObjectiveEvaluatorWila

**Parameters:**

- **objective** (<code>[ObjectiveEvaluator](#swift2.classes.ObjectiveEvaluator)</code>) – objective

**Returns:**

- <code>[DeletableCffiNativeHandle](#refcount.interop.DeletableCffiNativeHandle)</code> – returned result

##### swift2.doc_helper.swg.UseStateInitializerModelRunner_py

```python
UseStateInitializerModelRunner_py(simulation, stateInitializer)
```

UseStateInitializerModelRunner_py

UseStateInitializerModelRunner_py: generated wrapper function for API function UseStateInitializerModelRunner

**Parameters:**

- **simulation** (<code>[Simulation](#swift2.classes.Simulation)</code>) – simulation
- **stateInitializer** (<code>[StateInitialiser](#swift2.classes.StateInitialiser)</code>) – stateInitializer

##### swift2.doc_helper.swg.VariableIsBool_py

```python
VariableIsBool_py(simulation, variableIdentifier)
```

VariableIsBool_py

VariableIsBool_py: generated wrapper function for API function VariableIsBool

**Parameters:**

- **simulation** (<code>[Simulation](#swift2.classes.Simulation)</code>) – simulation
- **variableIdentifier** (<code>[str](#str)</code>) – variableIdentifier

**Returns:**

- <code>[bool](#bool)</code> – returned result

##### swift2.doc_helper.swg.VariableIsDouble_py

```python
VariableIsDouble_py(simulation, variableIdentifier)
```

VariableIsDouble_py

VariableIsDouble_py: generated wrapper function for API function VariableIsDouble

**Parameters:**

- **simulation** (<code>[Simulation](#swift2.classes.Simulation)</code>) – simulation
- **variableIdentifier** (<code>[str](#str)</code>) – variableIdentifier

**Returns:**

- <code>[bool](#bool)</code> – returned result

##### swift2.doc_helper.swg.VariableIsInt_py

```python
VariableIsInt_py(simulation, variableIdentifier)
```

VariableIsInt_py

VariableIsInt_py: generated wrapper function for API function VariableIsInt

**Parameters:**

- **simulation** (<code>[Simulation](#swift2.classes.Simulation)</code>) – simulation
- **variableIdentifier** (<code>[str](#str)</code>) – variableIdentifier

**Returns:**

- <code>[bool](#bool)</code> – returned result

##### swift2.doc_helper.swg.WireSubareaInputsPreprocessorModel_py

```python
WireSubareaInputsPreprocessorModel_py(simulation, fromOutput, toInput, subAreaId)
```

WireSubareaInputsPreprocessorModel_py

WireSubareaInputsPreprocessorModel_py: generated wrapper function for API function WireSubareaInputsPreprocessorModel

**Parameters:**

- **simulation** (<code>[Simulation](#swift2.classes.Simulation)</code>) – simulation
- **fromOutput** (<code>[str](#str)</code>) – fromOutput
- **toInput** (<code>[str](#str)</code>) – toInput
- **subAreaId** (<code>[str](#str)</code>) – subAreaId

##### swift2.doc_helper.swg.WrapObjectiveEvaluatorWila_py

```python
WrapObjectiveEvaluatorWila_py(objective, clone)
```

WrapObjectiveEvaluatorWila_py

WrapObjectiveEvaluatorWila_py: generated wrapper function for API function WrapObjectiveEvaluatorWila

**Parameters:**

- **objective** (<code>[DeletableCffiNativeHandle](#refcount.interop.DeletableCffiNativeHandle)</code>) – objective
- **clone** (<code>[bool](#bool)</code>) – clone

**Returns:**

- <code>[ObjectiveEvaluator](#swift2.classes.ObjectiveEvaluator)</code> – returned result

##### swift2.doc_helper.swg.char_array_to_py

```python
char_array_to_py(values, dispose=True)
```

##### swift2.doc_helper.swg.charp_array_to_py

```python
charp_array_to_py(values, size, dispose=True)
```

##### swift2.doc_helper.swg.custom_wrap_cffi_native_handle

```python
custom_wrap_cffi_native_handle(obj, type_id='', release_native=None)
```

Create a wrapper around a cffi pointer (if this is one),
with the suitable native release function call specific to this external pointer.

##### swift2.doc_helper.swg.dispose_shared_pointer_py

```python
dispose_shared_pointer_py(ptr)
```

##### swift2.doc_helper.swg.named_values_to_py

```python
named_values_to_py(values, dispose=True)
```

##### swift2.doc_helper.swg.opaque_ts_as_xarray_time_series

```python
opaque_ts_as_xarray_time_series(ptr, dispose=True)
```

##### swift2.doc_helper.swg.py_time_series_dimensions_description

```python
py_time_series_dimensions_description(ptr, dispose=True)
```

##### swift2.doc_helper.swg.set_wrap_cffi_native_handle

```python
set_wrap_cffi_native_handle(wrapper_function)
```

##### swift2.doc_helper.swg.toSceParametersNative

```python
toSceParametersNative(x)
```

#### swift2.doc_helper.testdata_dir

```python
testdata_dir()
```

### swift2.helpers

**Functions:**

- [**lag_and_route_linear_storage_type**](#swift2.helpers.lag_and_route_linear_storage_type) –
- [**parameteriser_lag_and_route**](#swift2.helpers.parameteriser_lag_and_route) –
- [**set_reach_lengths_lag_n_route**](#swift2.helpers.set_reach_lengths_lag_n_route) –

#### swift2.helpers.lag_and_route_linear_storage_type

```python
lag_and_route_linear_storage_type(simulation)
```

#### swift2.helpers.parameteriser_lag_and_route

```python
parameteriser_lag_and_route()
```

#### swift2.helpers.set_reach_lengths_lag_n_route

```python
set_reach_lengths_lag_n_route(simulation)
```

### swift2.internal

**Functions:**

- [**arg_error_swift_type**](#swift2.internal.arg_error_swift_type) –
- [**check_ensemble_forecast_simulation**](#swift2.internal.check_ensemble_forecast_simulation) –
- [**check_ensemble_forecast_time_series**](#swift2.internal.check_ensemble_forecast_time_series) –
- [**check_ensemble_simulation**](#swift2.internal.check_ensemble_simulation) –
- [**check_singular_simulation**](#swift2.internal.check_singular_simulation) –
- [**chk_date_time**](#swift2.internal.chk_date_time) –
- [**get_ts_window**](#swift2.internal.get_ts_window) –
- [**internal_get_played_tts**](#swift2.internal.internal_get_played_tts) –
- [**internal_get_recorded_tts**](#swift2.internal.internal_get_recorded_tts) –
- [**is_ensemble_forecast_simulation**](#swift2.internal.is_ensemble_forecast_simulation) –
- [**is_ensemble_forecast_time_series**](#swift2.internal.is_ensemble_forecast_time_series) –
- [**is_ensemble_simulation**](#swift2.internal.is_ensemble_simulation) –
- [**is_singular_simulation**](#swift2.internal.is_singular_simulation) –
- [**is_swift_ref**](#swift2.internal.is_swift_ref) –
- [**simplify_time_series**](#swift2.internal.simplify_time_series) – simplify a 1D time series object to a representation suitable for portable serialisation.
- [**to_interop_univariate_series**](#swift2.internal.to_interop_univariate_series) – Convert an univariate python time series to a representation suitable for interoperability with a C API

**Attributes:**

- [**TS_INTEROP_GEOM_KEY**](#swift2.internal.TS_INTEROP_GEOM_KEY) –
- [**TS_INTEROP_VALUES_KEY**](#swift2.internal.TS_INTEROP_VALUES_KEY) –

#### swift2.internal.TS_INTEROP_GEOM_KEY

```python
TS_INTEROP_GEOM_KEY = 'tsgeom'
```

#### swift2.internal.TS_INTEROP_VALUES_KEY

```python
TS_INTEROP_VALUES_KEY = 'tsvalues'
```

#### swift2.internal.arg_error_swift_type

```python
arg_error_swift_type(x, expected_type_id)
```

#### swift2.internal.check_ensemble_forecast_simulation

```python
check_ensemble_forecast_simulation(s)
```

#### swift2.internal.check_ensemble_forecast_time_series

```python
check_ensemble_forecast_time_series(s)
```

#### swift2.internal.check_ensemble_simulation

```python
check_ensemble_simulation(s)
```

#### swift2.internal.check_singular_simulation

```python
check_singular_simulation(s)
```

#### swift2.internal.chk_date_time

```python
chk_date_time(series, dt, xr_func)
```

#### swift2.internal.get_ts_window

```python
get_ts_window(series, start_time, end_time)
```

#### swift2.internal.internal_get_played_tts

```python
internal_get_played_tts(simulation, var_ids)
```

#### swift2.internal.internal_get_recorded_tts

```python
internal_get_recorded_tts(simulation, var_ids)
```

#### swift2.internal.is_ensemble_forecast_simulation

```python
is_ensemble_forecast_simulation(s)
```

#### swift2.internal.is_ensemble_forecast_time_series

```python
is_ensemble_forecast_time_series(s)
```

#### swift2.internal.is_ensemble_simulation

```python
is_ensemble_simulation(s)
```

#### swift2.internal.is_singular_simulation

```python
is_singular_simulation(s)
```

#### swift2.internal.is_swift_ref

```python
is_swift_ref(x, type)
```

#### swift2.internal.simplify_time_series

```python
simplify_time_series(input_ts)
```

simplify a 1D time series object to a representation suitable for portable serialisation.

**Parameters:**

- **input_ts** (<code>[TimeSeriesLike](#cinterop.timeseries.TimeSeriesLike)</code>) – time series

**Returns:**

- <code>[Dict](#typing.Dict)\[[str](#str), [Any](#typing.Any)\]</code> – Dict\[str,Any\]: dictionary with keys "tsgeom" for the time series geometry, and "tsvalues" for its values.

#### swift2.internal.to_interop_univariate_series

```python
to_interop_univariate_series(ts, from_date=None, to_date=None)
```

Convert an univariate python time series to a representation suitable for interoperability with a C API

**Parameters:**

- **ts** (<code>[TimeSeriesLike](#cinterop.timeseries.TimeSeriesLike)</code>) – Python native time series
- **from_date** (<code>[ConvertibleToTimestamp](#cinterop.timeseries.ConvertibleToTimestamp)</code>) – start timestamp of the time series to subset to. Defaults to None.
- **to_date** (<code>[ConvertibleToTimestamp](#cinterop.timeseries.ConvertibleToTimestamp)</code>) – end timestamp of the time series to subset to. Defaults to None.

**Returns:**

- <code>[Tuple](#typing.Tuple)\[[ndarray](#numpy.ndarray), [TimeSeriesGeometryNative](#cinterop.cffi.marshal.TimeSeriesGeometryNative)\]</code> – Tuple\[np.ndarray, TimeSeriesGeometryNative\]: univeriate data and time series geometry for interop.

### swift2.model_definitions

**Functions:**

- [**cookie_cut_dendritic_catchment**](#swift2.model_definitions.cookie_cut_dendritic_catchment) – cookie cut a dendritic catchment (without confluences)
- [**get_catchment_structure**](#swift2.model_definitions.get_catchment_structure) – Gets the essential connective structure of a catchment
- [**model_from_json_file**](#swift2.model_definitions.model_from_json_file) – Create a model simulation from a file with a JSON serialisation.
- [**model_to_json_file**](#swift2.model_definitions.model_to_json_file) – Save a model simulation from a file with a JSON serialisation.
- [**split_to_subcatchments**](#swift2.model_definitions.split_to_subcatchments) – Split a catchment in subcatchments, given a list of node/link element identifiers
- [**subset_catchment**](#swift2.model_definitions.subset_catchment) – Subsets a catchment, keeping only a portion above or below a node, link or subarea.

#### swift2.model_definitions.cookie_cut_dendritic_catchment

```python
cookie_cut_dendritic_catchment(simulation, bottom_element_id, top_element_ids)
```

cookie cut a dendritic catchment (without confluences)

**Parameters:**

- **simulation** (<code>[Simulation](#swift2.classes.Simulation)</code>) – base catchment simulation
- **bottom_element_id** (<code>[str](#str)</code>) – identifier of the most downstream element to keep
- **top_element_ids** (<code>[str](#str)</code>) – identifier(s) of the most upstream element(s) to keep

**Returns:**

- **Simulation** (<code>[Simulation](#swift2.classes.Simulation)</code>) – a subcatchment simulation, cookie cut from the base simulation. Deep clone of objects.

#### swift2.model_definitions.get_catchment_structure

```python
get_catchment_structure(simulation)
```

Gets the essential connective structure of a catchment

**Parameters:**

- **simulation** (<code>[Simulation](#swift2.classes.Simulation)</code>) – base catchment simulation

**Returns:**

- <code>[Dict](#typing.Dict)</code> – \[type\]: [description]

**Examples:**

```pycon
>>> _, simulation = sdh.create_test_catchment_structure()
>>> smd.get_catchment_structure(simulation)
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

#### swift2.model_definitions.model_from_json_file

```python
model_from_json_file(file_path)
```

Create a model simulation from a file with a JSON serialisation.

**Parameters:**

- **file_path** (<code>[str](#str)</code>) – valid file path.

**Returns:**

- **Simulation** (<code>[Simulation](#swift2.classes.Simulation)</code>) – a catchment simulation.

#### swift2.model_definitions.model_to_json_file

```python
model_to_json_file(simulation, file_path)
```

Save a model simulation from a file with a JSON serialisation.

**Parameters:**

- **simulation** (<code>[Simulation](#swift2.classes.Simulation)</code>) – Catchment simulation
- **file_path** (<code>[str](#str)</code>) – file path to save to

#### swift2.model_definitions.split_to_subcatchments

```python
split_to_subcatchments(simulation, split_element_ids, include_upstream=None)
```

Split a catchment in subcatchments, given a list of node/link element identifiers

**Parameters:**

- **simulation** (<code>[Simulation](#swift2.classes.Simulation)</code>) – base catchment simulation
- **split_element_ids** (<code>[str](#str)</code>) – element identifiers such as 'node.n1', 'link.linkId_2'
- **include_upstream** (<code>[bool](#bool)</code>) – indicates whether for each element in split_element_ids it should be including in the upstream portion of the subcatchment. Defaults to None.

**Returns:**

- **OrderedDict** (<code>[OrderedDict](#typing.OrderedDict)\[[str](#str), [Simulation](#swift2.classes.Simulation)\]</code>) – list of subcatchments resulting from the split

**Examples:**

```pycon
>>> _, simulation = sdh.create_test_catchment_structure()
>>> e_ids = ['node.n2', 'node.n4']
>>> sub_sims = smd.split_to_subcatchments(simulation, e_ids)
>>>
>>> for k in sub_sims:
...     print(k)
...     print(sub_sims[k].get_node_ids())
...     print(sub_sims[k].get_node_names())
...
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

#### swift2.model_definitions.subset_catchment

```python
subset_catchment(simulation, element_id, action='keep_above')
```

Subsets a catchment, keeping only a portion above or below a node, link or subarea.

**Parameters:**

- **simulation** (<code>[Simulation](#swift2.classes.Simulation)</code>) – an S4 object 'ExternalObjRef' [package "cinterop"] with external pointer type "MODEL_SIMULATION_PTR"
- **element_id** (<code>[str](#str)</code>) – id of the element to cut at.
- **action** (<code>[str](#str)</code>) – how to cut; currently limited to 'keep_above'

**Returns:**

- **Simulation** (<code>[Simulation](#swift2.classes.Simulation)</code>) – a subcatchment simulation, cookie cut from the base simulation. Deep clone of objects.

### swift2.parameteriser

**Classes:**

- [**MhData**](#swift2.parameteriser.MhData) – Data log from metaheuristic calibration processes

**Functions:**

- [**add_to_hypercube**](#swift2.parameteriser.add_to_hypercube) – Add entries to a hypercube
- [**add_transform**](#swift2.parameteriser.add_transform) – Create a parameteriser for which parameter transformations can be defined
- [**apply_sys_config**](#swift2.parameteriser.apply_sys_config) – Apply a model configuration to a simulation
- [**as_py_structure**](#swift2.parameteriser.as_py_structure) – Try to convert an external pointer to a native python representation
- [**backtransform**](#swift2.parameteriser.backtransform) – Get the parameteriser values in the untransformed space
- [**bound_values**](#swift2.parameteriser.bound_values) –
- [**bound_values_df**](#swift2.parameteriser.bound_values_df) – min/max bound a column in a data frame
- [**concatenate_parameterisers**](#swift2.parameteriser.concatenate_parameterisers) – Concatenate hypercubes to a single parameteriser
- [**create_multisite_obj_parameteriser**](#swift2.parameteriser.create_multisite_obj_parameteriser) – Builds a parameteriser usable with a multisite multiobjective calculator.
- [**create_muskingum_param_constraints**](#swift2.parameteriser.create_muskingum_param_constraints) – Create a parameteriser with Muskingum-type constraints. Given an existing parameteriser, create a wrapper that adds constraints on two of its parameters.
- [**create_parameter_sampler**](#swift2.parameteriser.create_parameter_sampler) – Args:
- [**create_parameteriser**](#swift2.parameteriser.create_parameteriser) – Create a SWIFT parameteriser
- [**create_sce_optim_swift**](#swift2.parameteriser.create_sce_optim_swift) – Build an SCE optimiser for a SWIFT model
- [**create_sce_termination_wila**](#swift2.parameteriser.create_sce_termination_wila) – Create a type of termination criteria suitable for the SCE algorithm.
- [**evaluate_score_for_parameters**](#swift2.parameteriser.evaluate_score_for_parameters) – Computes the value of an objective for a given set of parameters
- [**example_parameteriser**](#swift2.parameteriser.example_parameteriser) – Get examples of typical parameterisers
- [**execute_optimisation**](#swift2.parameteriser.execute_optimisation) – Launch an optimization task, as defined by the object passed as an argument
- [**extract_optimisation_log**](#swift2.parameteriser.extract_optimisation_log) –
- [**feasible_muskingum_bounds**](#swift2.parameteriser.feasible_muskingum_bounds) – [summary]
- [**filtered_parameters**](#swift2.parameteriser.filtered_parameters) – Wrap a parameteriser in a filter that can hide some parameters
- [**get_best_score**](#swift2.parameteriser.get_best_score) – Gets the best score in a population for a given objective
- [**get_default_sce_parameters**](#swift2.parameteriser.get_default_sce_parameters) – [summary]
- [**get_logger_content**](#swift2.parameteriser.get_logger_content) – Gets logger content on an optimiser, recorded detail of the optimisation process for post-optimisation analysis.
- [**get_marginal_termination**](#swift2.parameteriser.get_marginal_termination) – Create an termination criterion based on the rate of marginal fitness improvement
- [**get_max_iteration_termination**](#swift2.parameteriser.get_max_iteration_termination) – Create an termination criterion based on the number of objective evaluations
- [**get_max_runtime_termination**](#swift2.parameteriser.get_max_runtime_termination) – Create an termination criterion based on the wall clock runtime
- [**get_score_at_index**](#swift2.parameteriser.get_score_at_index) – Get an objective scores in a vector thereof
- [**hide_parameters**](#swift2.parameteriser.hide_parameters) – Hide some parameters (from the outside e.g. optimisers) in a filter parameteriser
- [**is_hypercube**](#swift2.parameteriser.is_hypercube) – Is the object a native parameteriser that can be cast as a hypercube?
- [**is_sampler_seeding**](#swift2.parameteriser.is_sampler_seeding) – Is the argument a native object that is a seeded candidate parameteriser factory
- [**is_score**](#swift2.parameteriser.is_score) – OBJECTIVE_SCORES_WILA_PTR
- [**is_set_of_scores**](#swift2.parameteriser.is_set_of_scores) – VEC_OBJECTIVE_SCORES_PTR
- [**linear_parameteriser**](#swift2.parameteriser.linear_parameteriser) – Create a scaled linear parameteriser, tying by a linear transformation a (resp several) model state to a (resp several) parameter values
- [**linear_parameteriser_from**](#swift2.parameteriser.linear_parameteriser_from) – Create a scaled linear parameteriser, tying by a linear transformation a (resp several) model state to a (resp several) parameter values
- [**listify**](#swift2.parameteriser.listify) –
- [**make_state_init_parameteriser**](#swift2.parameteriser.make_state_init_parameteriser) – [summary]
- [**mk_optim_log**](#swift2.parameteriser.mk_optim_log) –
- [**num_free_parameters**](#swift2.parameteriser.num_free_parameters) –
- [**parameteriser_as_dataframe**](#swift2.parameteriser.parameteriser_as_dataframe) – Convert an external object hypercube parameteriser to a pandas data frame
- [**parameteriser_for_score**](#swift2.parameteriser.parameteriser_for_score) – Gets the parameteriser for a score
- [**parameters_for**](#swift2.parameteriser.parameters_for) –
- [**scores_as_dataframe**](#swift2.parameteriser.scores_as_dataframe) – Convert objective scores to a pandas data frame representation
- [**set_calibration_logger**](#swift2.parameteriser.set_calibration_logger) – Sets logging on an optimiser, so as to record a detail of the optimisation process for post-optimisation analysis.
- [**set_hypercube**](#swift2.parameteriser.set_hypercube) – Set the properties of a hypercube parameteriser
- [**set_max_parameter_value**](#swift2.parameteriser.set_max_parameter_value) – Sets the maximum value of a model parameter value
- [**set_min_parameter_value**](#swift2.parameteriser.set_min_parameter_value) – Sets the minimum value of a model parameter value
- [**set_parameter_value**](#swift2.parameteriser.set_parameter_value) – Sets the value of a model parameter value
- [**show_parameters**](#swift2.parameteriser.show_parameters) – Show some parameters (from the outside e.g. optimisers) in a filter parameteriser
- [**sort_by_score**](#swift2.parameteriser.sort_by_score) – Sort objective scores according to one of the objective values
- [**subcatchment_parameteriser**](#swift2.parameteriser.subcatchment_parameteriser) – Create a parameteriser that gets applied to a subset of a whole catchment
- [**wrap_transform**](#swift2.parameteriser.wrap_transform) – Create a parameteriser for which parameter transformations can be defined.

**Attributes:**

- [**INTERCEPT_COL**](#swift2.parameteriser.INTERCEPT_COL) –
- [**MAX_VALUE_COL**](#swift2.parameteriser.MAX_VALUE_COL) –
- [**MIN_VALUE_COL**](#swift2.parameteriser.MIN_VALUE_COL) –
- [**PARAM_NAME_COL**](#swift2.parameteriser.PARAM_NAME_COL) –
- [**SCALING_VAR_NAME_COL**](#swift2.parameteriser.SCALING_VAR_NAME_COL) –
- [**STATE_NAME_COL**](#swift2.parameteriser.STATE_NAME_COL) –
- [**VALUE_COL**](#swift2.parameteriser.VALUE_COL) –

#### swift2.parameteriser.INTERCEPT_COL

```python
INTERCEPT_COL = 'intercept'
```

#### swift2.parameteriser.MAX_VALUE_COL

```python
MAX_VALUE_COL = 'max_value'
```

#### swift2.parameteriser.MIN_VALUE_COL

```python
MIN_VALUE_COL = 'min_value'
```

#### swift2.parameteriser.MhData

```python
MhData(data, fitness='NSE', messages='Message', categories='Category')
```

Data log from metaheuristic calibration processes

**Functions:**

- [**bound_fitness**](#swift2.parameteriser.MhData.bound_fitness) – Return a copy of the log data with the fitness measure bound by min/max limits
- [**rename_columns**](#swift2.parameteriser.MhData.rename_columns) – Rename the columns of the data log according to a mapping.
- [**subset_by_message**](#swift2.parameteriser.MhData.subset_by_message) – Subset the log by filtering the 'Message' column by a regexp pattern
- [**subset_by_pattern**](#swift2.parameteriser.MhData.subset_by_pattern) – Subset the log by filtering an attribute by a regexp pattern

**Attributes:**

- [**data**](#swift2.parameteriser.MhData.data) – The inner data of this data log

##### swift2.parameteriser.MhData.bound_fitness

```python
bound_fitness(obj_lims=None)
```

Return a copy of the log data with the fitness measure bound by min/max limits

**Parameters:**

- **obj_lims** (<code>[Sequence](#typing.Sequence)\[[float](#float)\]</code>) – min/max limits, length 2. Defaults to None.

**Returns:**

- <code>[DataFrame](#pandas.DataFrame)</code> – pd.DataFrame: log data with bound fitness

##### swift2.parameteriser.MhData.data

```python
data
```

The inner data of this data log

##### swift2.parameteriser.MhData.rename_columns

```python
rename_columns(colnames_map)
```

Rename the columns of the data log according to a mapping.

This is handy for instance to change fully qualified parameter names
such as 'subarea.Wolf_Creek.x1' to just 'x1' to produce more legible plots.

**Parameters:**

- **colnames_map** (<code>[Dict](#typing.Dict)\[[str](#str), [str](#str)\]</code>) – mapping

##### swift2.parameteriser.MhData.subset_by_message

```python
subset_by_message(pattern='Initial.*|Reflec.*|Contrac.*|Add.*')
```

Subset the log by filtering the 'Message' column by a regexp pattern

**Parameters:**

- **pattern** (<code>[str](#str)</code>) – regexp pattern, filter definition

**Returns:**

- **Any** (<code>[MhData](#swift2.parameteriser.MhData)</code>) – New MhData object with subset data

##### swift2.parameteriser.MhData.subset_by_pattern

```python
subset_by_pattern(colname, pattern)
```

Subset the log by filtering an attribute by a regexp pattern

**Parameters:**

- **colname** (<code>[str](#str)</code>) – column name to filter on
- **pattern** (<code>[str](#str)</code>) – regexp pattern, filter definition

**Returns:**

- **Any** (<code>[MhData](#swift2.parameteriser.MhData)</code>) – New MhData object with subset data

#### swift2.parameteriser.PARAM_NAME_COL

```python
PARAM_NAME_COL = 'param_name'
```

#### swift2.parameteriser.SCALING_VAR_NAME_COL

```python
SCALING_VAR_NAME_COL = 'scaling_var_name'
```

#### swift2.parameteriser.STATE_NAME_COL

```python
STATE_NAME_COL = 'state_name'
```

#### swift2.parameteriser.VALUE_COL

```python
VALUE_COL = 'value'
```

#### swift2.parameteriser.add_to_hypercube

```python
add_to_hypercube(parameteriser, specs)
```

Add entries to a hypercube

**Parameters:**

- **parameteriser** (<code>[HypercubeParameteriser](#swift2.classes.HypercubeParameteriser)</code>) – A HypercubeParameteriser wrapper, or a type inheriting from it
- **specs** (<code>[DataFrame](#pandas.DataFrame)</code>) – An optional data frame description of the parameter set, with at least columns Name, Min, Max, Value.

#### swift2.parameteriser.add_transform

```python
add_transform(parameteriser, param_name, inner_param_name, transform_id, a=1.0, b=0.0)
```

Create a parameteriser for which parameter transformations can be defined

```
This allows to define e.g. a virtual parameter log_X instead of calibrating on the parameter X.
```

**Parameters:**

- **parameteriser** (<code>[TransformParameteriser](#swift2.classes.TransformParameteriser)</code>) – A TransformParameteriser wrapper, or a type inheriting from it
- **param_name** (<code>[str](#str)</code>) – the name of the meta-parameter. Note that it can be the same value as inner_param_name, but this is NOT recommended.
- **inner_param_name** (<code>[str](#str)</code>) – the name of the parameter being transformed
- **transform_id** (<code>[str](#str)</code>) – identifier for a known bijective univariate function
- **a** (<code>[float](#float)</code>) – parameter in Y = F(ax+b). Defaults to 1.0.
- **b** (<code>[float](#float)</code>) – parameter in Y = F(ax+b). Defaults to 0.0.

#### swift2.parameteriser.apply_sys_config

```python
apply_sys_config(parameteriser, simulation)
```

Apply a model configuration to a simulation

**Parameters:**

- **parameteriser** (<code>[HypercubeParameteriser](#swift2.classes.HypercubeParameteriser)</code>) – A HypercubeParameteriser wrapper, or a type inheriting from it
- **simulation** (<code>[Simulation](#swift2.classes.Simulation)</code>) – simulation

#### swift2.parameteriser.as_py_structure

```python
as_py_structure(x)
```

Try to convert an external pointer to a native python representation

**Parameters:**

- **x** (<code>[Any](#typing.Any)</code>) – object, presumably wrapper around an Xptr, to convert to a 'pure' python representation

**Returns:**

- – \[type\]: [description]

#### swift2.parameteriser.backtransform

```python
backtransform(parameteriser)
```

Get the parameteriser values in the untransformed space

Get the parameteriser values in the untransformed space, i.e. remove any transform added via wrapTransform.
This allows to transform back e.g. from a virtual parameter log_X to the underlying model (or even virtual/meta) parameter X.

**Parameters:**

- **parameteriser** (<code>[HypercubeParameteriser](#swift2.classes.HypercubeParameteriser)</code>) – A HypercubeParameteriser wrapper, or a type inheriting from it

**Returns:**

- – \[HypercubeParameteriser\]: The parameters definitions without the transforms (if there are any)

#### swift2.parameteriser.bound_values

```python
bound_values(x, lim=None)
```

#### swift2.parameteriser.bound_values_df

```python
bound_values_df(x, colname, lim=None)
```

min/max bound a column in a data frame

**Parameters:**

- **x** (<code>\[[type](#type)\]</code>) – a data frame
- **colname** (<code>\[[type](#type)\]</code>) – a character vector, name of the column to bound
- **lim** (<code>\[[type](#type)\]</code>) – a num vector of the min/max limits to apply, for instance c(0, 1). Defaults to None.

**Returns:**

- – \[type\]: [description]

#### swift2.parameteriser.concatenate_parameterisers

```python
concatenate_parameterisers(*args, strategy='')
```

Concatenate hypercubes to a single parameteriser

**Parameters:**

- **strategy** (<code>[str](#str)</code>) – The strategy to contatenate. Defaults to "", equivalent to "composite", the only available. May have other options in the future.

**Returns:**

- **CompositeParameteriser** (<code>[CompositeParameteriser](#swift2.classes.CompositeParameteriser)</code>) – A concatenated parameteriser

#### swift2.parameteriser.create_multisite_obj_parameteriser

```python
create_multisite_obj_parameteriser(func_parameterisers, func_identifiers, prefixes=None, mix_func_parameteriser=None, hydro_parameteriser=None)
```

Builds a parameteriser usable with a multisite multiobjective calculator.

**Parameters:**

- **func_parameterisers** (<code>\[[type](#type)\]</code>) – list of external pointers, parameterisers for each function of a multiobjective calculation.
- **func_identifiers** (<code>\[[type](#type)\]</code>) – character, identifiers for each of the objectives defined in an multisite objective definition.
- **prefixes** (<code>\[[type](#type)\]</code>) – Optional prefixes to use to disambiguate short parameter names used in each function of a multiobjective calculator.. Defaults to None.
- **mix_func_parameteriser** (<code>\[[type](#type)\]</code>) – parameteriser, default None. (FUTURE) Optional parameteriser used in mixing the multiple objectives.. Defaults to None.
- **hydro_parameteriser** (<code>\[[type](#type)\]</code>) – parameteriser, default None. Optional parameteriser applied to the simulation model.. Defaults to None.

**Returns:**

- – \[FunctionsParameteriser\]: [description]

#### swift2.parameteriser.create_muskingum_param_constraints

```python
create_muskingum_param_constraints(inner_parameters, delta_t=1, param_name_k='K', param_name_x='X', simulation=None)
```

Create a parameteriser with Muskingum-type constraints. Given an existing parameteriser, create a wrapper that adds constraints on two of its parameters.

**Parameters:**

- **inner_parameters** (<code>\[[HypercubeParameteriser](#swift2.classes.HypercubeParameteriser)\]</code>) – A SWIFT parameteriser object.
- **delta_t** (<code>[int](#int)</code>) – the simulation time step in HOURS. Defaults to 1.
- **param_name_k** (<code>[str](#str)</code>) – the variable identifier to use for the delay parameter of the Muskingum routing. Defaults to "K".
- **param_name_x** (<code>[str](#str)</code>) – the variable identifier to use for the attenuation parameter of the Muskingum routing. Defaults to "X".
- **simulation** (<code>\[[Simulation](#swift2.classes.Simulation)\]</code>) – the model simulation from which link properties are inspected to define constraints. The links' parameters must already be set.. Defaults to None.

**Raises:**

- <code>[ValueError](#ValueError)</code> – [description]

**Returns:**

- – \[ConstraintParameteriser\]: [description]

#### swift2.parameteriser.create_parameter_sampler

```python
create_parameter_sampler(seed, parameteriser, type)
```

**Parameters:**

- **seed** (<code>\[[type](#type)\]</code>) – seed integer, the seed to use for the sampler
- **parameteriser** (<code>[HypercubeParameteriser](#swift2.classes.HypercubeParameteriser)</code>) – A HypercubeParameteriser wrapper, or a type inheriting from it
- **type** (<code>[str](#str)</code>) – identifying a method such as 'urs' for uniform random sampling.

**Returns:**

- – \[type\]: [description]

#### swift2.parameteriser.create_parameteriser

```python
create_parameteriser(type='Generic subareas', specs=None)
```

Create a SWIFT parameteriser

**Parameters:**

- **type** (<code>[str](#str)</code>) – A string identifying the (likely SWIFT-specific) type of parameteriser to use. Recognised types are (case insensitive) 'log-likelihood', 'generic', 'subareas', 'links', 'nodes' and 'muskingum'. Defaults to "Generic subareas".
- **specs** (<code>[DataFrame](#pandas.DataFrame)</code>) – An optional data frame description of the parameter set, with at least columns Name, Min, Max, Value. Defaults to None.

**Returns:**

- – \[HypercubeParameteriser\]: new parameteriser

#### swift2.parameteriser.create_sce_optim_swift

```python
create_sce_optim_swift(objective, termination_criterion, sce_params, population_initialiser)
```

Build an SCE optimiser for a SWIFT model

**Parameters:**

- **objective** (<code>[ObjectiveEvaluator](#ObjectiveEvaluator)</code>) – an objective calculator
- **termination_criterion** (<code>[SceTerminationCondition](#swift2.classes.SceTerminationCondition)</code>) – An object that can be passed to SCE for testing the completion of the algorithm.
- **sce_params** (<code>[dict](#dict)</code>) – optional; parameters controlling the behavior of the SCE optimisers.
- **population_initialiser** (<code>[CandidateFactorySeed](#CandidateFactorySeed)</code>) – an S4 object 'ExternalObjRef' [package "cinterop"] with external pointer type HYPERCUBE_PTR or coercible to it, or a type of object that can seed a sampler i.e. coercible to a type CANDIDATE_FACTORY_SEED_WILA_PTR. If the argument is a hypercube, a uniform random sampler is created.

**Returns:**

- – \[Optimiser\]: [description]

#### swift2.parameteriser.create_sce_termination_wila

```python
create_sce_termination_wila(type, arguments)
```

Create a type of termination criteria suitable for the SCE algorithm.

**Parameters:**

- **type** (<code>[str](#str)</code>) – A type of termination criterion; currently at least "relative standard deviation" and "maximum evaluations" are valid options
- **arguments** (<code>[Sequence](#typing.Sequence)\[[str](#str)\]</code>) – Arguments, in string forms even for numeric values, options for the selected type.

**Returns:**

- **SceTerminationCondition** (<code>[SceTerminationCondition](#swift2.classes.SceTerminationCondition)</code>) – [description]

#### swift2.parameteriser.evaluate_score_for_parameters

```python
evaluate_score_for_parameters(objective, parameteriser)
```

Computes the value of an objective for a given set of parameters

**Parameters:**

- **objective** (<code>\[[type](#type)\]</code>) – an objective calculator
- **parameteriser** (<code>[HypercubeParameteriser](#swift2.classes.HypercubeParameteriser)</code>) – A HypercubeParameteriser wrapper, or a type inheriting from it

**Returns:**

- – \[type\]: [description]

#### swift2.parameteriser.example_parameteriser

```python
example_parameteriser(type, strict=False)
```

Get examples of typical parameterisers

**Parameters:**

- **type** (<code>[str](#str)</code>) – identifier for a type of parameteriser including 'log-likelihood'
- **strict** (<code>[bool](#bool)</code>) – If True an error is raised if the type is not found, otherwise a dummy empty parameteriser is returned.. Defaults to False.

**Returns:**

- – \[HypercubeParameteriser\]: [description]

#### swift2.parameteriser.execute_optimisation

```python
execute_optimisation(optimiser)
```

Launch an optimization task, as defined by the object passed as an argument

**Parameters:**

- **optimiser** (<code>[Optimiser](#Optimiser)</code>) – the instance of the optimiser that has been created for the optimisation task about to be launched.

**Returns:**

- – \[VectorObjectiveScores\]: [description]

#### swift2.parameteriser.extract_optimisation_log

```python
extract_optimisation_log(estimator, fitness_name='log.likelihood')
```

#### swift2.parameteriser.feasible_muskingum_bounds

```python
feasible_muskingum_bounds(simulation, delta_t_hours=1)
```

[summary]

**Parameters:**

- **simulation** (<code>[Simulation](#swift2.classes.Simulation)</code>) – [description]
- **delta_t_hours** (<code>[int](#int)</code>) – [description]. Defaults to 1.

**Returns:**

- – \[type\]: [description]

#### swift2.parameteriser.filtered_parameters

```python
filtered_parameters(parameteriser)
```

Wrap a parameteriser in a filter that can hide some parameters

**Parameters:**

- **parameteriser** (<code>[HypercubeParameteriser](#swift2.classes.HypercubeParameteriser)</code>) – A HypercubeParameteriser wrapper, or a type inheriting from it. A deep copy of the input is taken.

**Returns:**

- – \[FilteringParameteriser\]: [description]

#### swift2.parameteriser.get_best_score

```python
get_best_score(scores_population, score_name='NSE', convert_to_py=False)
```

Gets the best score in a population for a given objective

**Parameters:**

- **scores_population** (<code>\[[type](#type)\]</code>) – an S4 object 'ExternalObjRef' [package "cinterop"] with external pointer type VEC_OBJECTIVE_SCORES_PTR
- **score_name** (<code>[str](#str)</code>) – name of the objective to use for sorting. Defaults to "NSE".
- **convert_to_py** (<code>[bool](#bool)</code>) – should the returned score be converted to an R representation. Default False. Defaults to False.

**Returns:**

- – \[ObjectiveScores or Dict\]: [description]

#### swift2.parameteriser.get_default_sce_parameters

```python
get_default_sce_parameters()
```

[summary]

**Returns:**

- – \[type\]: [description]

#### swift2.parameteriser.get_logger_content

```python
get_logger_content(optimiser, add_numbering=False)
```

Gets logger content on an optimiser, recorded detail of the optimisation process for post-optimisation analysis.

**Parameters:**

- **optimiser** (<code>\[[type](#type)\]</code>) – the instance of the optimiser that has been created for the optimisation task about to be launched.
- **add_numbering** (<code>[bool](#bool)</code>) – Add an explicit column for numbering the lines of the log. Defaults to False.

**Returns:**

- <code>[DataFrame](#pandas.DataFrame)</code> – pd.DataFrame: The data log of the optimiser

#### swift2.parameteriser.get_marginal_termination

```python
get_marginal_termination(tolerance=1e-06, cutoff_no_improvement=10, max_hours=0.05)
```

Create an termination criterion based on the rate of marginal fitness improvement

**Parameters:**

- **tolerance** (<code>\[[type](#type)\]</code>) – the increment in the objective below which the improvement is considered negligible. Defaults to 1e-06.
- **cutoff_no_improvement** (<code>[int](#int)</code>) – the maximum number of successive times the algorithm fails to improve the objective function.. Defaults to 10.
- **max_hours** (<code>[float](#float)</code>) – the maximum wall time runtime for the optimisation. Defaults to 0.05.

**Returns:**

- – \[SceTerminationCondition\]: [description]

#### swift2.parameteriser.get_max_iteration_termination

```python
get_max_iteration_termination(max_iterations=1000)
```

Create an termination criterion based on the number of objective evaluations

**Parameters:**

- **max_iterations** (<code>[int](#int)</code>) – number of iterations, which, if less than total count of optim objective evaluations, defines optim termination.. Defaults to 1000.

**Returns:**

- – \[SceTerminationCondition\]: [description]

#### swift2.parameteriser.get_max_runtime_termination

```python
get_max_runtime_termination(max_hours=0.05)
```

Create an termination criterion based on the wall clock runtime

**Parameters:**

- **max_hours** (<code>[float](#float)</code>) – the maximum wall time runtime in hours for the optimisation. Defaults to 0.05.

**Returns:**

- – \[SceTerminationCondition\]: [description]

#### swift2.parameteriser.get_score_at_index

```python
get_score_at_index(scores_population, index)
```

Get an objective scores in a vector thereof

**Parameters:**

- **scores_population** (<code>\[[type](#type)\]</code>) – an S4 object 'ExternalObjRef' [package "cinterop"] with external pointer type VEC_OBJECTIVE_SCORES_PTR
- **index** (<code>[int](#int)</code>) – one-based index in the population

**Returns:**

- – \[ObjectiveScores\]: [description]

#### swift2.parameteriser.hide_parameters

```python
hide_parameters(parameteriser, patterns, regex=False, starts_with=False, strict=False)
```

Hide some parameters (from the outside e.g. optimisers) in a filter parameteriser

**Parameters:**

- **parameteriser** (<code>[HypercubeParameteriser](#swift2.classes.HypercubeParameteriser)</code>) – A HypercubeParameteriser wrapper, or a type inheriting from it
- **patterns** (<code>\[[type](#type)\]</code>) – character, one or more pattern to match and hide matching parameters. Match according to other parameters.
- **regex** (<code>[bool](#bool)</code>) – logical, defaults False, should the patterns be used as regular expressions.. Defaults to False.
- **starts_with** (<code>[bool](#bool)</code>) – logical, defaults False. Ignored if regex is True. Should the patterns be used as starting strings in the parameter names.. Defaults to False.
- **strict** (<code>[bool](#bool)</code>) – logical, default False. Used only if regex and starts_with are False. If True, raises an error if one of the "patterns" has no exact match in the parameters.. Defaults to False.

#### swift2.parameteriser.is_hypercube

```python
is_hypercube(p_set)
```

Is the object a native parameteriser that can be cast as a hypercube?

**Parameters:**

- **p_set** (<code>[CffiNativeHandle](#refcount.interop.CffiNativeHandle)</code>) – [description]

**Returns:**

- – \[type\]: [description]

#### swift2.parameteriser.is_sampler_seeding

```python
is_sampler_seeding(obj)
```

Is the argument a native object that is a seeded candidate parameteriser factory

**Parameters:**

- **obj** (<code>[CffiNativeHandle](#refcount.interop.CffiNativeHandle)</code>) – [description]

**Returns:**

- – \[type\]: [description]

#### swift2.parameteriser.is_score

```python
is_score(x)
```

OBJECTIVE_SCORES_WILA_PTR

**Parameters:**

- **x** (<code>\[[type](#type)\]</code>) – [description]

**Returns:**

- – \[type\]: [description]

#### swift2.parameteriser.is_set_of_scores

```python
is_set_of_scores(x)
```

VEC_OBJECTIVE_SCORES_PTR

**Parameters:**

- **x** (<code>\[[type](#type)\]</code>) – [description]

**Returns:**

- – \[type\]: [description]

#### swift2.parameteriser.linear_parameteriser

```python
linear_parameteriser(param_name, state_name, scaling_var_name, min_p_val, max_p_val, value, selector_type='subareas', intercept=0.0)
```

Create a scaled linear parameteriser, tying by a linear transformation a (resp several) model state to a (resp several) parameter values

This allows to define tied parameters where pval = a * modelStateVal + intercept.
The intent in particular is to define virtual model parameters such as initial store value as a fraction of the maximum storage capacity.

Args:

```
param_name (VecStr): the name of the meta-parameter. Note that it can be the same value as inner_param_name without interference, though this may be confusing a choice.
state_name (VecStr): the name of the model state to modify, based on the value of the meta-parameter and the state found in 'scalingVarName'
scaling_var_name (VecStr): the name of the parameter for each subarea model, to which to apply the area scaled value.
min_p_val (VecNum): minimum value allowed for the meta-parameter
max_p_val (VecNum): minimum value allowed for the meta-parameter
value (VecNum): value for the meta parameter.
selector_type (str, optional): an identifier to define to which catchment element(s) the parameteriser will be applied. Defaults to "subareas".
intercept (VecNum, optional): intercepts in the linear relationship(s). Defaults to 0.0.
```

**Returns:**

- – \[ScalingParameteriser\]: new ScalingParameteriser

#### swift2.parameteriser.linear_parameteriser_from

```python
linear_parameteriser_from(data_frame, selector_type='subareas')
```

Create a scaled linear parameteriser, tying by a linear transformation a (resp several) model state to a (resp several) parameter values

This allows to define tied parameters where pval = a * modelStateVal + intercept.
The intent in particular is to define virtual model parameters such as initial store value as a fraction of the maximum storage capacity.
Args:
data_frame (pd.DataFrame): data frame with columns "param_name", "state_name", "scaling_var_name", "min_value", "max_value", "value", "intercept",
selector_type (str, optional): [description]. Defaults to "subareas".

**Returns:**

- – \[ScalingParameteriser\]: ScalingParameteriser

#### swift2.parameteriser.listify

```python
listify(*args)
```

#### swift2.parameteriser.make_state_init_parameteriser

```python
make_state_init_parameteriser(parameteriser)
```

[summary]

**Parameters:**

- **parameteriser** (<code>[HypercubeParameteriser](#swift2.classes.HypercubeParameteriser)</code>) – A HypercubeParameteriser wrapper, or a type inheriting from it

**Returns:**

- – \[StateInitParameteriser\]: new state initialisation parameteriser

#### swift2.parameteriser.mk_optim_log

```python
mk_optim_log(log_dataframe, fitness='NSE', messages='Message', categories='Category')
```

#### swift2.parameteriser.num_free_parameters

```python
num_free_parameters(parameteriser)
```

#### swift2.parameteriser.parameteriser_as_dataframe

```python
parameteriser_as_dataframe(parameteriser)
```

Convert an external object hypercube parameteriser to a pandas data frame

**Parameters:**

- **parameteriser** (<code>[HypercubeParameteriser](#swift2.classes.HypercubeParameteriser)</code>) – A HypercubeParameteriser wrapper, or a type inheriting from it

**Returns:**

- – \[type\]: [a data frame]

#### swift2.parameteriser.parameteriser_for_score

```python
parameteriser_for_score(score)
```

Gets the parameteriser for a score

**Parameters:**

- **score** (<code>\[[type](#type)\]</code>) – [description]

**Returns:**

- – \[HypercubeParameteriser\]: [description]

#### swift2.parameteriser.parameters_for

```python
parameters_for(model_id, as_pandas_df=False)
```

#### swift2.parameteriser.scores_as_dataframe

```python
scores_as_dataframe(scores_population)
```

Convert objective scores to a pandas data frame representation

**Parameters:**

- **scores_population** (<code>\[[type](#type)\]</code>) – [description]

**Returns:**

- – \[type\]: [description]

#### swift2.parameteriser.set_calibration_logger

```python
set_calibration_logger(optimiser, type='')
```

Sets logging on an optimiser, so as to record a detail of the optimisation process for post-optimisation analysis.

**Parameters:**

- **optimiser** (<code>\[[type](#type)\]</code>) – [description]
- **type** (<code>[str](#str)</code>) – [description]. Defaults to "".

**Returns:**

- – \[type\]: [description]

#### swift2.parameteriser.set_hypercube

```python
set_hypercube(parameteriser, specs)
```

Set the properties of a hypercube parameteriser

**Parameters:**

- **parameteriser** (<code>[HypercubeParameteriser](#swift2.classes.HypercubeParameteriser)</code>) – A HypercubeParameteriser wrapper, or a type inheriting from it
- **specs** (<code>[DataFrame](#pandas.DataFrame)</code>) – An optional data frame description of the parameter set, with at least columns Name, Min, Max, Value.

#### swift2.parameteriser.set_max_parameter_value

```python
set_max_parameter_value(parameteriser, variable_name, value)
```

Sets the maximum value of a model parameter value

**Parameters:**

- **parameteriser** (<code>[HypercubeParameteriser](#swift2.classes.HypercubeParameteriser)</code>) – A HypercubeParameteriser wrapper, or a type inheriting from it
- **variable_name** (<code>str or iterable of str</code>) – model variable state identifier(s)
- **value** (<code>numeric or iterable of numeric</code>) – value(s)

#### swift2.parameteriser.set_min_parameter_value

```python
set_min_parameter_value(parameteriser, variable_name, value)
```

Sets the minimum value of a model parameter value

**Parameters:**

- **parameteriser** (<code>[HypercubeParameteriser](#swift2.classes.HypercubeParameteriser)</code>) – A HypercubeParameteriser wrapper, or a type inheriting from it
- **variable_name** (<code>str or iterable of str</code>) – model variable state identifier(s)
- **value** (<code>numeric or iterable of numeric</code>) – value(s)

#### swift2.parameteriser.set_parameter_value

```python
set_parameter_value(parameteriser, variable_name, value)
```

Sets the value of a model parameter value

**Parameters:**

- **parameteriser** (<code>[HypercubeParameteriser](#swift2.classes.HypercubeParameteriser)</code>) – A HypercubeParameteriser wrapper, or a type inheriting from it
- **variable_name** (<code>str or iterable of str</code>) – model variable state identifier(s)
- **value** (<code>numeric or iterable of numeric</code>) – value(s)

#### swift2.parameteriser.show_parameters

```python
show_parameters(parameteriser, patterns, regex=False, starts_with=False)
```

Show some parameters (from the outside e.g. optimisers) in a filter parameteriser

**Parameters:**

- **parameteriser** (<code>[HypercubeParameteriser](#swift2.classes.HypercubeParameteriser)</code>) – A HypercubeParameteriser wrapper, or a type inheriting from it
- **patterns** (<code>\[[type](#type)\]</code>) – character, one or more pattern to match and show matching parameters. Match according to other parameters
- **regex** (<code>[bool](#bool)</code>) – should the patterns be used as regular expressions. Defaults to False.
- **starts_with** (<code>[bool](#bool)</code>) – should the patterns be used as starting strings in the parameter names. Defaults to False.

#### swift2.parameteriser.sort_by_score

```python
sort_by_score(scores_population, score_name='NSE')
```

Sort objective scores according to one of the objective values

**Parameters:**

- **scores_population** (<code>\[[type](#type)\]</code>) – an S4 object 'ExternalObjRef' [package "cinterop"] with external pointer type VEC_OBJECTIVE_SCORES_PTR
- **score_name** (<code>[str](#str)</code>) – name of the objective to use for sorting. Defaults to "NSE".

**Returns:**

- **VectorObjectiveScores** – an S4 object 'ExternalObjRef' [package "cinterop"] with external pointer type VEC_OBJECTIVE_SCORES_PTR

#### swift2.parameteriser.subcatchment_parameteriser

```python
subcatchment_parameteriser(parameteriser, subcatchment)
```

Create a parameteriser that gets applied to a subset of a whole catchment

**Parameters:**

- **parameteriser** (<code>[HypercubeParameteriser](#swift2.classes.HypercubeParameteriser)</code>) – A HypercubeParameteriser wrapper, or a type inheriting from it
- **subcatchment** (<code>[Simulation](#swift2.classes.Simulation)</code>) – the subcatchment, subset of a whole catchment, identifying which elements (subareas, nodes, links) will be parameterised by the new parameteriser. Other catchment elements are untouched.

**Returns:**

- – \[HypercubeParameteriser\]: New parameteriser whose application is limited to the subcatchment.

**Examples:**

```pycon
>>> sub_cats = simulation.split_to_subcatchments(["node.node_7", "node.node_10"])
>>> sc = sub_cats["node.node_7"]
>>> p = sp.create_parameteriser('generic subarea')
>>> p.add_parameter_to_hypercube("x1", 32, 1, 6e3)
>>> sp = p.subcatchment_parameteriser(sc)
>>> sp.apply_sys_config(simulation)
```

#### swift2.parameteriser.wrap_transform

```python
wrap_transform(parameteriser)
```

Create a parameteriser for which parameter transformations can be defined.

This allows to define e.g. a virtual parameter log_X instead of calibrating on the parameter X.

**Parameters:**

- **parameteriser** (<code>[HypercubeParameteriser](#swift2.classes.HypercubeParameteriser)</code>) – A HypercubeParameteriser wrapper, or a type inheriting from it

**Returns:**

- **TransformParameteriser** – A new parameteriser (TransformParameteriser) which has methods to define parameter transforms

### swift2.play_record

**Functions:**

- [**apply_recording_function**](#swift2.play_record.apply_recording_function) –
- [**get_all_played**](#swift2.play_record.get_all_played) –
- [**get_all_recorded**](#swift2.play_record.get_all_recorded) –
- [**get_played**](#swift2.play_record.get_played) – Retrieves a played time series from a simulation
- [**get_played_varnames**](#swift2.play_record.get_played_varnames) – Gets all the names of states fed an input time series
- [**get_recorded**](#swift2.play_record.get_recorded) – Retrieves a recorded time series from a simulation
- [**get_recorded_ensemble_forecast**](#swift2.play_record.get_recorded_ensemble_forecast) – Retrieves a recorded time series from a simulation
- [**get_recorded_varnames**](#swift2.play_record.get_recorded_varnames) – Gets all the names of the recorded states
- [**play_ensemble_forecast_input**](#swift2.play_record.play_ensemble_forecast_input) – Sets time series as input to a simulation
- [**play_input**](#swift2.play_record.play_input) – Sets time series as input to a simulation
- [**play_inputs**](#swift2.play_record.play_inputs) – Assign input time series from a time series library to a model simulation
- [**play_singular_simulation**](#swift2.play_record.play_singular_simulation) –
- [**play_subarea_input**](#swift2.play_record.play_subarea_input) – Sets time series as input to a simulation
- [**record_ensemble_forecast_state**](#swift2.play_record.record_ensemble_forecast_state) –
- [**record_ensemble_state**](#swift2.play_record.record_ensemble_state) –
- [**record_singular_state**](#swift2.play_record.record_singular_state) –
- [**record_state**](#swift2.play_record.record_state) – Record a time series of one of the state of the model

#### swift2.play_record.apply_recording_function

```python
apply_recording_function(simulation, recording_func, var_ids, recording_provider, data_ids)
```

#### swift2.play_record.get_all_played

```python
get_all_played(simulation)
```

#### swift2.play_record.get_all_recorded

```python
get_all_recorded(simulation)
```

#### swift2.play_record.get_played

```python
get_played(simulation, var_ids=None, start_time=None, end_time=None)
```

Retrieves a played time series from a simulation

Retrieves a played time series from a simulation.

**Parameters:**

- **simulation** (<code>[Simulation](#swift2.classes.Simulation)</code>) – A swift simulation object
- **var_ids** (<code>[Any](#Any)</code>) – name of the output variable played to a time series. 'Catchment|StreamflowRate'. If missing, a multivariate time series of all played states is returned; this may be a large amount of data.
- **start_time** (<code>[Any](#Any)</code>) – An optional parameter, the start of a period to subset the time series
- **end_time** (<code>[Any](#Any)</code>) – An optional parameter, the end of a period to subset the time series

**Returns:**

- – an xts time series, possibly multivariate.

#### swift2.play_record.get_played_varnames

```python
get_played_varnames(simulation)
```

Gets all the names of states fed an input time series

Gets all the names of states fed an input time series

**Parameters:**

- **simulation** (<code>[Simulation](#swift2.classes.Simulation)</code>) – A swift simulation object

**Returns:**

- – The names of the state variables fed over the simulation with values from a time series

#### swift2.play_record.get_recorded

```python
get_recorded(simulation, var_ids=None, start_time=None, end_time=None)
```

Retrieves a recorded time series from a simulation

Retrieves a recorded time series from a simulation.

**Parameters:**

- **simulation** (<code>[Simulation](#swift2.classes.Simulation)</code>) – A swift simulation object
- **var_ids** (<code>[Any](#Any)</code>) – name of the output variable recorded to a time series. 'Catchment|StreamflowRate'. If missing, a multivariate time series of all recorded states is returned; this may be a large amount of data.
- **start_time** (<code>[Any](#Any)</code>) – An optional parameter, the start of a period to subset the time series
- **end_time** (<code>[Any](#Any)</code>) – An optional parameter, the end of a period to subset the time series

**Returns:**

- – an xts time series, possibly multivariate.

#### swift2.play_record.get_recorded_ensemble_forecast

```python
get_recorded_ensemble_forecast(simulation, var_id, start_time=None, end_time=None)
```

Retrieves a recorded time series from a simulation

Retrieves a recorded time series from a simulation.

**Parameters:**

- **simulation** (<code>[Simulation](#swift2.classes.Simulation)</code>) – A swift simulation object
- **var_ids** (<code>[Any](#Any)</code>) – name of the output variable recorded to a time series. 'Catchment|StreamflowRate'. If missing, a multivariate time series of all recorded states is returned; this may be a large amount of data.
- **start_time** (<code>[Any](#Any)</code>) – NOT USED YET An optional parameter, the start of a period to subset the time series
- **end_time** (<code>[Any](#Any)</code>) – NOT USED YET An optional parameter, the end of a period to subset the time series

**Returns:**

- – an xts time series, possibly multivariate.

#### swift2.play_record.get_recorded_varnames

```python
get_recorded_varnames(simulation)
```

Gets all the names of the recorded states

Gets all the names of the recorded states

**Parameters:**

- **simulation** (<code>[Simulation](#swift2.classes.Simulation)</code>) – A swift simulation object

**Returns:**

- – The names of the state variables being recorded into time series

#### swift2.play_record.play_ensemble_forecast_input

```python
play_ensemble_forecast_input(simulation, input_ts, var_id)
```

Sets time series as input to a simulation

Sets time series as input to a simulation

**Parameters:**

- **simulation** (<code>[Any](#Any)</code>) – an S4 object 'ExternalObjRef' [package "cinterop"] with external pointer type "ENSEMBLE_FORECAST_SIMULATION_PTR"
- **input_ts** (<code>[Any](#Any)</code>) – an S4 object 'ExternalObjRef' [package "cinterop"] with external pointer type "ENSEMBLE_FORECAST_TIME_SERIES_PTR"
- **var_id** (<code>[Any](#Any)</code>) – character of length one, the variable identifier to use

#### swift2.play_record.play_input

```python
play_input(simulation, input_ts, var_ids=None)
```

Sets time series as input to a simulation

Sets time series as input to a simulation

**Parameters:**

- **simulation** (<code>[Simulation](#swift2.classes.Simulation)</code>) – A swift simulation object
- **input_ts** (<code>[Any](#Any)</code>) – an xts time series, or an S4 object 'ExternalObjRef' [package "cinterop"] with external pointer type "ENSEMBLE_FORECAST_TIME_SERIES_PTR". if an xts time series column names must be valid model variable identifiers, unless explicitely provided via varIds
- **var_ids** (<code>[Any](#Any)</code>) – optional character, the variable identifiers to use, overriding the column names of the inputTs. If not NULL, must be of length equal to the number of columns in inputTs

#### swift2.play_record.play_inputs

```python
play_inputs(simulation, data_library, model_var_id, data_id, resample='')
```

Assign input time series from a time series library to a model simulation

**Parameters:**

- **simulation** (<code>[Simulation](#swift2.classes.Simulation)</code>) – A swift simulation object
- **data_library** (<code>[TimeSeriesLibrary](#uchronia.classes.TimeSeriesLibrary)</code>) – external pointer type ENSEMBLE_DATA_SET_PTR, or a Python class wrapper around it
- **model_var_id** (<code>str or sequence of str</code>) – model state variable unique identifier(s)
- **data_id** (<code>str or sequence of str</code>) – identifier(s) for data in the data_library. If length is not the same as model_var_id, the elements of data_id are reused to match it
- **resample** (<code>str or sequence of str</code>) – identifier(s) for how the series is resampled (aggregated or disaggregated). If length is not the same as model_var_id, the elements of resample are reused to match it

#### swift2.play_record.play_singular_simulation

```python
play_singular_simulation(simulation, input_ts, var_ids)
```

#### swift2.play_record.play_subarea_input

```python
play_subarea_input(simulation, input, subarea_name, input_name)
```

Sets time series as input to a simulation

Sets time series as input to a simulation

**Parameters:**

- **simulation** (<code>[Simulation](#swift2.classes.Simulation)</code>) – A swift simulation object
- **input** (<code>[Any](#Any)</code>) – an xts time series.
- **subarea_name** (<code>[Any](#Any)</code>) – a valid name of the subarea
- **input_name** (<code>[Any](#Any)</code>) – the name of the input variable to the model (i.e. 'P' for the precip of GR5H)

#### swift2.play_record.record_ensemble_forecast_state

```python
record_ensemble_forecast_state(simulation, var_ids=CATCHMENT_FLOWRATE_VARID, recording_provider=None, data_ids=None)
```

#### swift2.play_record.record_ensemble_state

```python
record_ensemble_state(simulation, var_ids=CATCHMENT_FLOWRATE_VARID, recording_provider=None, data_ids=None)
```

#### swift2.play_record.record_singular_state

```python
record_singular_state(simulation, var_ids=CATCHMENT_FLOWRATE_VARID, recording_provider=None, data_ids=None)
```

#### swift2.play_record.record_state

```python
record_state(simulation, var_ids=CATCHMENT_FLOWRATE_VARID, recording_provider=None, data_ids=None)
```

Record a time series of one of the state of the model

Record a time series of one of the state of the model

**Parameters:**

- **simulation** (<code>[Any](#Any)</code>) – an S4 object 'ExternalObjRef' [package "cinterop"] with external pointer type "MODEL_SIMULATION_PTR", "ENSEMBLE_SIMULATION_PTR" or "ENSEMBLE_FORECAST_SIMULATION_PTR"
- **var_ids** (<code>[VecStr](#swift2.const.VecStr)</code>) – identifier(s) of the output variable recorded to a time series, e.g. 'Catchment|StreamflowRate' or 'subcatchment.Subarea.runoff'. Defaults to CATCHMENT_FLOWRATE_VARID.
- **recording_provider** (<code>[TimeSeriesLibrary](#uchronia.classes.TimeSeriesLibrary)</code>) – _description_. Defaults to None.
- **data_ids** (<code>[VecStr](#swift2.const.VecStr)</code>) – _description_. Defaults to None.

**Raises:**

- <code>[ValueError](#ValueError)</code> – _description_

### swift2.proto

Prototypes

**Classes:**

- [**PbmCalibration**](#swift2.proto.PbmCalibration) –
- [**PbmCalibrationBuilder**](#swift2.proto.PbmCalibrationBuilder) –
- [**PbmModelFactory**](#swift2.proto.PbmModelFactory) –

**Functions:**

- [**parameters_for**](#swift2.proto.parameters_for) –
- [**scatter_plot**](#swift2.proto.scatter_plot) –
- [**ts_plot**](#swift2.proto.ts_plot) –

**Attributes:**

- [**MODELLED_SERIES_COLNAME**](#swift2.proto.MODELLED_SERIES_COLNAME) –
- [**OBSERVED_SERIES_COLNAME**](#swift2.proto.OBSERVED_SERIES_COLNAME) –

#### swift2.proto.MODELLED_SERIES_COLNAME

```python
MODELLED_SERIES_COLNAME = 'Modelled'
```

#### swift2.proto.OBSERVED_SERIES_COLNAME

```python
OBSERVED_SERIES_COLNAME = 'Observed'
```

#### swift2.proto.PbmCalibration

```python
PbmCalibration(station_id, model_id, simulation, data_repo)
```

**Functions:**

- [**best_modelled_runoff**](#swift2.proto.PbmCalibration.best_modelled_runoff) –
- [**best_runoff_series**](#swift2.proto.PbmCalibration.best_runoff_series) –
- [**calibrate**](#swift2.proto.PbmCalibration.calibrate) –
- [**extract_optimisation_log**](#swift2.proto.PbmCalibration.extract_optimisation_log) –
- [**get_geom_ops**](#swift2.proto.PbmCalibration.get_geom_ops) –
- [**max_walltime_seconds**](#swift2.proto.PbmCalibration.max_walltime_seconds) –
- [**save_to**](#swift2.proto.PbmCalibration.save_to) –
- [**scatter_plot_calib**](#swift2.proto.PbmCalibration.scatter_plot_calib) –
- [**scatter_plot_valid**](#swift2.proto.PbmCalibration.scatter_plot_valid) –
- [**set_metrics**](#swift2.proto.PbmCalibration.set_metrics) –
- [**validate**](#swift2.proto.PbmCalibration.validate) –

**Attributes:**

- [**calib_end**](#swift2.proto.PbmCalibration.calib_end) –
- [**calib_start**](#swift2.proto.PbmCalibration.calib_start) –
- [**data_repo**](#swift2.proto.PbmCalibration.data_repo) –
- [**model_id**](#swift2.proto.PbmCalibration.model_id) –
- [**objective_id**](#swift2.proto.PbmCalibration.objective_id) –
- [**opt_log**](#swift2.proto.PbmCalibration.opt_log) –
- [**optimiser**](#swift2.proto.PbmCalibration.optimiser) –
- [**parameter_template**](#swift2.proto.PbmCalibration.parameter_template) –
- [**run_start**](#swift2.proto.PbmCalibration.run_start) –
- [**runoff_id**](#swift2.proto.PbmCalibration.runoff_id) –
- [**runoff_ts**](#swift2.proto.PbmCalibration.runoff_ts) –
- [**s_calib**](#swift2.proto.PbmCalibration.s_calib) –
- [**s_valid**](#swift2.proto.PbmCalibration.s_valid) –
- [**station_id**](#swift2.proto.PbmCalibration.station_id) –
- [**valid_end**](#swift2.proto.PbmCalibration.valid_end) –
- [**valid_start**](#swift2.proto.PbmCalibration.valid_start) –

##### swift2.proto.PbmCalibration.best_modelled_runoff

```python
best_modelled_runoff()
```

##### swift2.proto.PbmCalibration.best_runoff_series

```python
best_runoff_series()
```

##### swift2.proto.PbmCalibration.calib_end

```python
calib_end = pd.Timestamp('1995-12-01')
```

##### swift2.proto.PbmCalibration.calib_start

```python
calib_start = pd.Timestamp('1952-01-01')
```

##### swift2.proto.PbmCalibration.calibrate

```python
calibrate()
```

##### swift2.proto.PbmCalibration.data_repo

```python
data_repo = data_repo
```

##### swift2.proto.PbmCalibration.extract_optimisation_log

```python
extract_optimisation_log()
```

##### swift2.proto.PbmCalibration.get_geom_ops

```python
get_geom_ops()
```

##### swift2.proto.PbmCalibration.max_walltime_seconds

```python
max_walltime_seconds(sec)
```

##### swift2.proto.PbmCalibration.model_id

```python
model_id = model_id
```

##### swift2.proto.PbmCalibration.objective_id

```python
objective_id = 'NSE'
```

##### swift2.proto.PbmCalibration.opt_log

```python
opt_log = None
```

##### swift2.proto.PbmCalibration.optimiser

```python
optimiser = None
```

##### swift2.proto.PbmCalibration.parameter_template

```python
parameter_template = parameters_for(self.model_id)
```

##### swift2.proto.PbmCalibration.run_start

```python
run_start = pd.Timestamp('1950-01-01')
```

##### swift2.proto.PbmCalibration.runoff_id

```python
runoff_id = 'subarea.Subarea.runoff'
```

##### swift2.proto.PbmCalibration.runoff_ts

```python
runoff_ts = self.data_repo.monthly_data(self.station_id, 'runoff', cf_time=True)
```

##### swift2.proto.PbmCalibration.s_calib

```python
s_calib = slice(self.calib_start, self.calib_end)
```

##### swift2.proto.PbmCalibration.s_valid

```python
s_valid = slice(self.valid_start, self.valid_end)
```

##### swift2.proto.PbmCalibration.save_to

```python
save_to(root_path=None)
```

##### swift2.proto.PbmCalibration.scatter_plot_calib

```python
scatter_plot_calib()
```

##### swift2.proto.PbmCalibration.scatter_plot_valid

```python
scatter_plot_valid()
```

##### swift2.proto.PbmCalibration.set_metrics

```python
set_metrics(metrics)
```

##### swift2.proto.PbmCalibration.station_id

```python
station_id = station_id
```

##### swift2.proto.PbmCalibration.valid_end

```python
valid_end = pd.Timestamp('2014-12-01')
```

##### swift2.proto.PbmCalibration.valid_start

```python
valid_start = pd.Timestamp('1996-01-01')
```

##### swift2.proto.PbmCalibration.validate

```python
validate()
```

#### swift2.proto.PbmCalibrationBuilder

```python
PbmCalibrationBuilder(model_factory)
```

**Functions:**

- [**build_calibration**](#swift2.proto.PbmCalibrationBuilder.build_calibration) –
- [**max_walltime_seconds**](#swift2.proto.PbmCalibrationBuilder.max_walltime_seconds) –
- [**set_sampling_periods**](#swift2.proto.PbmCalibrationBuilder.set_sampling_periods) –

**Attributes:**

- [**convergence_criterion**](#swift2.proto.PbmCalibrationBuilder.convergence_criterion) –
- [**model_factory**](#swift2.proto.PbmCalibrationBuilder.model_factory) –
- [**objective_id**](#swift2.proto.PbmCalibrationBuilder.objective_id) –

##### swift2.proto.PbmCalibrationBuilder.build_calibration

```python
build_calibration(station_id, model_id)
```

##### swift2.proto.PbmCalibrationBuilder.convergence_criterion

```python
convergence_criterion = 0.002
```

##### swift2.proto.PbmCalibrationBuilder.max_walltime_seconds

```python
max_walltime_seconds(sec)
```

##### swift2.proto.PbmCalibrationBuilder.model_factory

```python
model_factory = model_factory
```

##### swift2.proto.PbmCalibrationBuilder.objective_id

```python
objective_id = 'NSE'
```

##### swift2.proto.PbmCalibrationBuilder.set_sampling_periods

```python
set_sampling_periods(run_start='1950-01-01', calib_start='1952-01-01', calib_end='1995-12-01', valid_start='1996-01-01', valid_end='2014-12-01')
```

#### swift2.proto.PbmModelFactory

```python
PbmModelFactory(data_repo)
```

**Functions:**

- [**new_monthly_lumped_model**](#swift2.proto.PbmModelFactory.new_monthly_lumped_model) –

**Attributes:**

- [**data_repo**](#swift2.proto.PbmModelFactory.data_repo) –

##### swift2.proto.PbmModelFactory.data_repo

```python
data_repo = data_repo
```

##### swift2.proto.PbmModelFactory.new_monthly_lumped_model

```python
new_monthly_lumped_model(station_id, model_id, rain_varid='P', evap_varid='E')
```

#### swift2.proto.parameters_for

```python
parameters_for(model_id)
```

#### swift2.proto.scatter_plot

```python
scatter_plot(obs_runoff_ts, mod_runoff_ts, title)
```

#### swift2.proto.ts_plot

```python
ts_plot(x, title, y_units)
```

### swift2.prototypes

**Functions:**

- [**clone**](#swift2.prototypes.clone) –
- [**create_erris_parameter_estimator**](#swift2.prototypes.create_erris_parameter_estimator) –
- [**estimate_erris_parameters**](#swift2.prototypes.estimate_erris_parameters) –
- [**estimate_transformation_parameters**](#swift2.prototypes.estimate_transformation_parameters) – Estimate the transformation parameters for a log-likelihood for a series of observations

#### swift2.prototypes.clone

```python
clone(external_ptr)
```

#### swift2.prototypes.create_erris_parameter_estimator

```python
create_erris_parameter_estimator(simulation, observed_ts, error_model_element_id, estimation_start, estimation_end, cens_thr, cens_opt, termination_condition=None, restriction_on=True, weighted_least_square=False)
```

#### swift2.prototypes.estimate_erris_parameters

```python
estimate_erris_parameters(simulation, observed_ts, error_model_element_id, warmup_start, warmup_end, warmup, estimation_start, estimation_end, cens_thr, cens_opt, exclusion_start, exclusion_end, exclusion, termination_condition, hydro_params=None, erris_params=None, restriction_on=True, weighted_least_square=False)
```

#### swift2.prototypes.estimate_transformation_parameters

```python
estimate_transformation_parameters(calib_obs, estimation_start, estimation_end, censor_threshold, exclusion, exclusion_start, exclusion_end, termination_condition=None)
```

Estimate the transformation parameters for a log-likelihood for a series of observations

**Parameters:**

- **calib_obs** (<code>[TimeSeriesLike](#cinterop.cffi.marshal.TimeSeriesLike)</code>) – An timeseries of observed data
- **estimation_start** (<code>[datetime](#datetime.datetime)</code>) – Start of estimation period
- **estimation_end** (<code>[datetime](#datetime.datetime)</code>) – End of estimation period
- **censor_threshold** (<code>[float](#float)</code>) – The value below which observations are treated a censored data (Default=0.0)
- **exclusion** (<code>[bool](#bool)</code>) – Start of period exclued from estimation
- **exclusion_start** (<code>[datetime](#datetime.datetime)</code>) – End of period exclued from estimation
- **exclusion_end** (<code>[datetime](#datetime.datetime)</code>) – Use the exclusion period (bool)
- **termination_condition** (<code>[SceTerminationCondition](#swift2.classes.SceTerminationCondition)</code>) – A SWIFT termination condition used by the optimisation. Default max runtime of ~3 minutes if None.

**Returns:**

- **HypercubeParameteriser** (<code>[HypercubeParameteriser](#swift2.classes.HypercubeParameteriser)</code>) – transformation parameters

### swift2.simulation

**Functions:**

- [**check_simulation**](#swift2.simulation.check_simulation) – Checks whether a simulation is configured to a state where it is executable
- [**create_catchment**](#swift2.simulation.create_catchment) – Create a SWIFT catchment with a specified hydrologic model
- [**create_ensemble_forecast_simulation**](#swift2.simulation.create_ensemble_forecast_simulation) – Create an ensemble forecast simulation
- [**create_subarea**](#swift2.simulation.create_subarea) – Create a SWIFT subarea with a specified hydrologic model
- [**create_subarea_simulation**](#swift2.simulation.create_subarea_simulation) – Creates a one sub-catchment simulation
- [**describe**](#swift2.simulation.describe) –
- [**exec_simulation**](#swift2.simulation.exec_simulation) – Execute a simulation
- [**get_link_ids**](#swift2.simulation.get_link_ids) – Gets all the identifiers of the links in the catchment
- [**get_link_names**](#swift2.simulation.get_link_names) – Gets all the names of the links in the catchment
- [**get_node_ids**](#swift2.simulation.get_node_ids) – Gets all the identifiers of the nodes in the catchment
- [**get_node_names**](#swift2.simulation.get_node_names) – Gets all the names of the nodes in the catchment
- [**get_state_value**](#swift2.simulation.get_state_value) – Gets the value(s) of a model state(s)
- [**get_subarea_ids**](#swift2.simulation.get_subarea_ids) – Gets all the identifiers of the sub-areas in the catchment
- [**get_subarea_names**](#swift2.simulation.get_subarea_names) – Gets all the names of the sub-areas in the catchment
- [**get_variable_ids**](#swift2.simulation.get_variable_ids) – Gets all the names of the variables of an element within a catchment
- [**is_variable_id**](#swift2.simulation.is_variable_id) – Is a variable identifier valid for a simulation
- [**reset_model_states**](#swift2.simulation.reset_model_states) – Reset the model states of a simulation, and apply one or more state initialers if the simulation is configured with any.
- [**set_error_correction_model**](#swift2.simulation.set_error_correction_model) – Add an error correction model to an element in a catchment
- [**set_simulation_span**](#swift2.simulation.set_simulation_span) – Sets simulation span
- [**set_simulation_time_step**](#swift2.simulation.set_simulation_time_step) – Sets the time step of a SWIFT simulation
- [**set_state_value**](#swift2.simulation.set_state_value) – Sets the value of a model state
- [**set_states**](#swift2.simulation.set_states) – Apply memory states to a simulation
- [**snapshot_state**](#swift2.simulation.snapshot_state) – Take a snapshot of the memory states of a simulation
- [**sort_by_execution_order**](#swift2.simulation.sort_by_execution_order) – Sort the specified element ids according to the execution order of the simulation
- [**swap_model**](#swift2.simulation.swap_model) – Clone and change a simulation, using another runoff model

#### swift2.simulation.check_simulation

```python
check_simulation(simulation)
```

Checks whether a simulation is configured to a state where it is executable

Checks whether a simulation is configured to a state where it is executable

**Parameters:**

- **simulation** (<code>[Simulation](#swift2.classes.Simulation)</code>) – A swift simulation object

#### swift2.simulation.create_catchment

```python
create_catchment(node_ids, node_names, link_ids, link_names, link_from_node, link_to_node, runoff_model_name='GR4J', areas_km2=None)
```

Create a SWIFT catchment with a specified hydrologic model

Create a SWIFT catchment with a specified hydrologic model.
This function is intended mostly for testing, not for usual modelling code.

**Parameters:**

- **node_ids** (<code>[Any](#typing.Any)</code>) – character, node unique identifiers
- **node_names** (<code>[Any](#typing.Any)</code>) – character, node display names
- **link_ids** (<code>[Any](#typing.Any)</code>) – character, links unique identifiers
- **link_names** (<code>[Any](#typing.Any)</code>) – character, links display names
- **link_from_node** (<code>[Any](#typing.Any)</code>) – character, identifier of the links' upstream node
- **link_to_node** (<code>[Any](#typing.Any)</code>) – character, identifier of the links' downstream node
- **runoff_model_name** (<code>[Any](#typing.Any)</code>) – A valid, known SWIFT model name (e.g. 'GR5H')
- **areas_km2** (<code>[Any](#typing.Any)</code>) – The areas in square kilometres

**Returns:**

- – A SWIFT simulation object (i.e. a model runner)

**Examples:**

TODO

#### swift2.simulation.create_ensemble_forecast_simulation

```python
create_ensemble_forecast_simulation(simulation, data_library, start, end, input_map, lead_time, ensemble_size, n_time_steps_between_forecasts)
```

Create an ensemble forecast simulation

Create an ensemble forecast simulation

**Parameters:**

- **simulation** (<code>[Simulation](#swift2.classes.Simulation)</code>) – A swift simulation object
- **data_library** (<code>[Any](#typing.Any)</code>) – external pointer type ENSEMBLE_DATA_SET_PTR, or a Python class wrapper around it
- **start** (<code>[Any](#typing.Any)</code>) – the start date of the simulation. The time zone will be forced to UTC.
- **end** (<code>[Any](#typing.Any)</code>) – the end date of the simulation. The time zone will be forced to UTC.
- **input_map** (<code>[Any](#typing.Any)</code>) – a named list were names are the data library data identifiers, and values are character vectors with model state identifiers.
- **lead_time** (<code>[Any](#typing.Any)</code>) – integer, the length in time steps of the forecasts.
- **ensemble_size** (<code>[Any](#typing.Any)</code>) – ensemble size
- **n_time_steps_between_forecasts** (<code>[Any](#typing.Any)</code>) – nTimeStepsBetweenForecasts

**Returns:**

- – An external pointer

#### swift2.simulation.create_subarea

```python
create_subarea(model_name, area_km2)
```

Create a SWIFT subarea with a specified hydrologic model

Create a SWIFT subarea with a specified hydrologic model

**Parameters:**

- **model_name** (<code>[Any](#typing.Any)</code>) – A valid, known SWIFT model name (e.g. 'GR5H')
- **area_km2** (<code>[Any](#typing.Any)</code>) – The area in square kilometres

**Returns:**

- – A SWIFT simulation object (i.e. a model runner)

#### swift2.simulation.create_subarea_simulation

```python
create_subarea_simulation(data_id='MMH', simul_start='1990-01-01', simul_end='2005-12-31', model_id='GR4J', tstep='daily', varname_rain='P', varname_pet='E')
```

Creates a one sub-catchment simulation

Creates a one sub-catchment simulation. This function is intended for creating sample simulations, not for use in production.

**Parameters:**

- **dataId** (<code>[Any](#typing.Any)</code>) – data identifier in swift_sample_data
- **simulStart** (<code>[Any](#typing.Any)</code>) – ISO string for the simulation start date time
- **simulEnd** (<code>[Any](#typing.Any)</code>) – ISO string for the simulation end date time
- **modelId** (<code>[Any](#typing.Any)</code>) – model identifier
- **tstep** (<code>[Any](#typing.Any)</code>) – character, 'daily' or 'hourly'
- **varNameRain** (<code>[Any](#typing.Any)</code>) – variable name to assign rainfall to
- **varNamePet** (<code>[Any](#typing.Any)</code>) – variable name to assign PET to

**Returns:**

- – A SWIFT simulation object, clone of the simulation but with a new model type in use.

#### swift2.simulation.describe

```python
describe(simulation, verbosity=None)
```

#### swift2.simulation.exec_simulation

```python
exec_simulation(simulation, reset_initial_states=True)
```

Execute a simulation

Execute a simulation

**Parameters:**

- **simulation** (<code>[Simulation](#swift2.classes.Simulation)</code>) – A swift simulation object
- **reset_initial_states** (<code>[Any](#typing.Any)</code>) – logical, should the states of the model be reinitialized before the first time step.

#### swift2.simulation.get_link_ids

```python
get_link_ids(simulation)
```

Gets all the identifiers of the links in the catchment

Gets all the identifiers of the links in the catchment

**Parameters:**

- **simulation** (<code>[Simulation](#swift2.classes.Simulation)</code>) – A swift simulation object

**Returns:**

- – The identifiers of the links in the catchment

#### swift2.simulation.get_link_names

```python
get_link_names(simulation)
```

Gets all the names of the links in the catchment

Gets all the names of the links in the catchment

**Parameters:**

- **simulation** (<code>[Simulation](#swift2.classes.Simulation)</code>) – A swift simulation object

**Returns:**

- – The names of the links in the catchment

#### swift2.simulation.get_node_ids

```python
get_node_ids(simulation)
```

Gets all the identifiers of the nodes in the catchment

Gets all the identifiers of the nodes in the catchment

**Parameters:**

- **simulation** (<code>[Simulation](#swift2.classes.Simulation)</code>) – A swift simulation object

**Returns:**

- – The identifiers of the nodes in the catchment

#### swift2.simulation.get_node_names

```python
get_node_names(simulation)
```

Gets all the names of the nodes in the catchment

Gets all the names of the nodes in the catchment

**Parameters:**

- **simulation** (<code>[Simulation](#swift2.classes.Simulation)</code>) – A swift simulation object

**Returns:**

- – The names of the nodes in the catchment

#### swift2.simulation.get_state_value

```python
get_state_value(simulation, var_id)
```

Gets the value(s) of a model state(s)

**Parameters:**

- **simulation** (<code>[Simulation](#swift2.classes.Simulation)</code>) – A swift simulation object
- **var_id** (<code>[VecStr](#swift2.const.VecStr)</code>) – string or sequence of str, model variable state identifier(s)

**Returns:**

- – numeric vector, value(s) of the requested model states

#### swift2.simulation.get_subarea_ids

```python
get_subarea_ids(simulation)
```

Gets all the identifiers of the sub-areas in the catchment

Gets all the identifiers of the sub-areas in the catchment

**Parameters:**

- **simulation** (<code>[Simulation](#swift2.classes.Simulation)</code>) – A swift simulation object

**Returns:**

- – The identifiers of the sub-areas in the catchment

#### swift2.simulation.get_subarea_names

```python
get_subarea_names(simulation)
```

Gets all the names of the sub-areas in the catchment

Gets all the names of the sub-areas in the catchment

**Parameters:**

- **simulation** (<code>[Simulation](#swift2.classes.Simulation)</code>) – A swift simulation object

**Returns:**

- – The names of the sub-areas in the catchment

#### swift2.simulation.get_variable_ids

```python
get_variable_ids(simulation, element_id=None, full_id=True)
```

Gets all the names of the variables of an element within a catchment

Gets all the names of the variables of an element (link, node, subarea) within a catchment

**Parameters:**

- **simulation** (<code>[Simulation](#swift2.classes.Simulation)</code>) – A swift simulation object
- **element_id** (<code>[Any](#typing.Any)</code>) – a character, identifier of the element within the catchment
- **full_id** (<code>[Any](#typing.Any)</code>) – boolean, if TRUE return the full hierarchical identifier

**Returns:**

- – character vector, names (identifiers) of model states in the element

#### swift2.simulation.is_variable_id

```python
is_variable_id(simulation, var_id)
```

Is a variable identifier valid for a simulation

Is a variable identifier valid for a simulation

**Parameters:**

- **simulation** (<code>[Simulation](#swift2.classes.Simulation)</code>) – A swift simulation object
- **var_id** (<code>[Any](#typing.Any)</code>) – a character, identifier(s) of the variable(s)

**Returns:**

- – logical vector

#### swift2.simulation.reset_model_states

```python
reset_model_states(simulation)
```

Reset the model states of a simulation, and apply one or more state initialers if the simulation is configured with any.

**Parameters:**

- **simulation** (<code>[Simulation](#swift2.classes.Simulation)</code>) – simulation

#### swift2.simulation.set_error_correction_model

```python
set_error_correction_model(simulation, model_id, element_id, length=1, seed=0)
```

Add an error correction model to an element in a catchment

Add an error correction model to an element in a catchment

**Parameters:**

- **simulation** (<code>[Simulation](#swift2.classes.Simulation)</code>) – A swift simulation object
- **model_id** (<code>[str](#str)</code>) – the identifier of the new model to use, e.g. 'ERRIS'
- **element_id** (<code>[str](#str)</code>) – the identifier of the catchment element (node, link, subcatchment) whose outflow rate is corrected.
- **length** (<code>[int](#int)</code>) – other parameters to pass to the creation of the error correction model. Currently length of the AR model only supported.
- **seed** (<code>[int](#int)</code>) – other parameters to pass to the creation of the error correction model. Currently length of the AR model only supported.

#### swift2.simulation.set_simulation_span

```python
set_simulation_span(simulation, start, end)
```

Sets simulation span

Sets the simulation span

**Parameters:**

- **simulation** (<code>[Simulation](#swift2.classes.Simulation)</code>) – A swift simulation object
- **start** (<code>[Any](#typing.Any)</code>) – the start date of the simulation. The time zone will be forced to UTC.
- **end** (<code>[Any](#typing.Any)</code>) – the end date of the simulation. The time zone will be forced to UTC.

#### swift2.simulation.set_simulation_time_step

```python
set_simulation_time_step(simulation, name)
```

Sets the time step of a SWIFT simulation

Sets the time step of a SWIFT simulation

**Parameters:**

- **simulation** (<code>[Simulation](#swift2.classes.Simulation)</code>) – A swift simulation object
- **name** (<code>[Any](#typing.Any)</code>) – a time step identifier, currently 'daily' or 'hourly' are supported. The identifier is made lower case in the function.

#### swift2.simulation.set_state_value

```python
set_state_value(simulation, var_id, value)
```

Sets the value of a model state

Sets the value of a model state

**Parameters:**

- **simulation** (<code>[Simulation](#swift2.classes.Simulation)</code>) – A swift simulation object
- **var_id** (<code>([str](#str), [Sequence](#typing.Sequence)\[[str](#str)\])</code>) – character, model variable state identifier(s)
- **value** (<code>([float](#float), [int](#int), [bool](#bool), [Sequence](#typing.Sequence))</code>) – numeric value(s)

#### swift2.simulation.set_states

```python
set_states(simulation, states)
```

Apply memory states to a simulation

**Parameters:**

- **simulation** (<code>[Simulation](#swift2.classes.Simulation)</code>) – simulation
- **states** (<code>[MemoryStates](#swift2.classes.MemoryStates)</code>) – memory states

#### swift2.simulation.snapshot_state

```python
snapshot_state(simulation)
```

Take a snapshot of the memory states of a simulation

**Parameters:**

- **simulation** (<code>[Simulation](#swift2.classes.Simulation)</code>) – model simulation

**Returns:**

- **MemoryStates** (<code>[MemoryStates](#swift2.classes.MemoryStates)</code>) – memory states, that can be stored and reapplied

#### swift2.simulation.sort_by_execution_order

```python
sort_by_execution_order(simulation, split_element_ids, sorting_option='')
```

Sort the specified element ids according to the execution order of the simulation

Sort the specified element ids according to the execution order of the simulation

**Parameters:**

- **simulation** (<code>[Simulation](#swift2.classes.Simulation)</code>) – A swift simulation object
- **split_element_ids** (<code>[Any](#typing.Any)</code>) – a character vector with element identifiers such as 'node.n1', 'link.linkId_2'
- **sorting_option** (<code>[Any](#typing.Any)</code>) – a character - for future options. Ignored for now.

**Returns:**

- – values in split_element_ids sorted by simulation execution order

#### swift2.simulation.swap_model

```python
swap_model(simulation, model_id, what='runoff')
```

Clone and change a simulation, using another runoff model

Clone and change a simulation, using another runoff model

**Parameters:**

- **simulation** (<code>[Simulation](#swift2.classes.Simulation)</code>) – A swift simulation object
- **model_id** (<code>[Any](#typing.Any)</code>) – the identifier of the new model to use, e.g. 'GR4J'
- **what** (<code>[Any](#typing.Any)</code>) – character identifying the type of structure: 'runoff', 'channel_routing'

**Returns:**

- – A SWIFT simulation object, clone of the simulation but with a new model type in use.

### swift2.statistics

**Functions:**

- [**createCompositeObjective**](#swift2.statistics.createCompositeObjective) – Creates a composite objective calculator
- [**create_composite_objective**](#swift2.statistics.create_composite_objective) –
- [**create_multisite_objective**](#swift2.statistics.create_multisite_objective) – Creates an objective that combines multiple statistics
- [**create_objective**](#swift2.statistics.create_objective) – Creates an objective calculator
- [**get_score**](#swift2.statistics.get_score) – Evaluate an objective for a given parameterisation
- [**multi_statistic_definition**](#swift2.statistics.multi_statistic_definition) – Collate information for use in multisite multiobjective definition

#### swift2.statistics.createCompositeObjective

```python
createCompositeObjective(simulation, state_name, observation, yamlstring_statistic, start_date, end_date)
```

Creates a composite objective calculator

Creates a composite objective calculator

**Parameters:**

- **simulation** (<code>[Simulation](#swift2.classes.Simulation)</code>) – A SWIFT simulation object (i.e. a model runner)
- **state_name** (<code>[Any](#typing.Any)</code>) – The name identifying the model state variable to calibrate against the observation
- **observation** (<code>[Any](#typing.Any)</code>) – an xts
- **yamlstring_statistic** (<code>[Any](#typing.Any)</code>) – a yaml string representing objective functions and weights eg...
- **start_date** (<code>[Any](#typing.Any)</code>) – start date of the period to calculate statistics on
- **end_date** (<code>[Any](#typing.Any)</code>) – end date of the period to calculate statistics on

**Returns:**

- – objective evaluator

#### swift2.statistics.create_composite_objective

```python
create_composite_objective(objectives, weights, names)
```

#### swift2.statistics.create_multisite_objective

```python
create_multisite_objective(simulation, statspec, observations, weights)
```

Creates an objective that combines multiple statistics

Creates an objective that combines multiple statistics. Used for joined, "whole of catchment" calibration

**Parameters:**

- **simulation** (<code>[Simulation](#swift2.classes.Simulation)</code>) – A SWIFT simulation object (i.e. a model runner)
- **statspec** (<code>[DataFrame](#pandas.DataFrame)</code>) – dataframe defining the objectives used. See function \[`multi_statistic_definition`\][swift2.statistics.multi_statistic_definition] to help build this dataframe.
- **observations** (<code>[Sequence](#typing.Sequence)\[[TimeSeriesLike](#cinterop.timeseries.TimeSeriesLike)\]</code>) – A list of (time series) observations to calculated the statistics. Must be of same length as the number of rows of statspec.
- **weights** (<code>[Dict](#typing.Dict)\[[str](#str), [float](#float)\]</code>) – numeric vector of weights to ponderate each objective.
- **Examples** –

> > > todo()

#### swift2.statistics.create_objective

```python
create_objective(simulation, state_name, observation, statistic, start_date, end_date)
```

Creates an objective calculator

**Parameters:**

- **simulation** (<code>[Simulation](#swift2.classes.Simulation)</code>) – A SWIFT simulation object (i.e. a model runner)
- **state_name** (<code>[Any](#typing.Any)</code>) – The name identifying the model state variable to calibrate against the observation
- **observation** (<code>[TimeSeriesLike](#cinterop.timeseries.TimeSeriesLike)</code>) – an xts
- **statistic** (<code>[str](#str)</code>) – statistic identifier, e.g. "NSE"
- **start_date** (<code>[ConvertibleToTimestamp](#cinterop.timeseries.ConvertibleToTimestamp)</code>) – start date of the period to calculate statistics on
- **end_date** (<code>[ConvertibleToTimestamp](#cinterop.timeseries.ConvertibleToTimestamp)</code>) – end date of the period to calculate statistics on

#### swift2.statistics.get_score

```python
get_score(objective_evaluator, p_set)
```

Evaluate an objective for a given parameterisation

**Parameters:**

- **objective_evaluator** (<code>[ObjectiveEvaluator](#swift2.classes.ObjectiveEvaluator)</code>) – objective evaluator
- **p_set** (<code>[HypercubeParameteriser](#swift2.classes.HypercubeParameteriser)</code>) – parameteriser

**Returns:**

- <code>[Dict](#typing.Dict)\[[str](#str), [Any](#typing.Any)\]</code> – Dict\[str,Any\]: score(s), and a data frame representation of the input parameters.

#### swift2.statistics.multi_statistic_definition

```python
multi_statistic_definition(model_var_ids, statistic_ids, objective_ids, objective_names, starts, ends)
```

Collate information for use in multisite multiobjective definition

Collate information for use in multisite multiobjective definition

**Parameters:**

- **model_var_ids** (<code>[Any](#typing.Any)</code>) – character vector, model state identifiers where statistics are calculated
- **statistic_ids** (<code>[Any](#typing.Any)</code>) – character vector, identifiers for bivariate statistics (e.g. nse, lognse, et.)
- **objective_ids** (<code>[Any](#typing.Any)</code>) – character vector, identifiers for the objectives. Can be the same as modelVarIds.
- **objective_names** (<code>[Any](#typing.Any)</code>) – character vector, display names for the objectives. Can be the same as modelVarIds.
- **starts** (<code>[Any](#typing.Any)</code>) – POSIXct vector of start dates for statistics
- **ends** (<code>[Any](#typing.Any)</code>) – POSIXct vector of end dates for statistics

### swift2.system

**Functions:**

- [**get_last_swift_error**](#swift2.system.get_last_swift_error) – Retrieve the message for the last known error in SWIFT
- [**runoff_model_ids**](#swift2.system.runoff_model_ids) – Gets all the names of known runoff models
- [**runoff_model_var_ids**](#swift2.system.runoff_model_var_ids) – Gets all the names of the variables a runoff model exposes
- [**set_default_max_parallelism_threads**](#swift2.system.set_default_max_parallelism_threads) – Sets the level of thread parallelism to use by default for new objects such as optimisers. May be overwritten for each instance afterwards.
- [**set_maximum_threads**](#swift2.system.set_maximum_threads) – Sets the maximum level of parallelism of an optimizer

#### swift2.system.get_last_swift_error

```python
get_last_swift_error()
```

Retrieve the message for the last known error in SWIFT

Retrieve the message for the last known error in SWIFT. Error means here that an exception was thrown by the core
SWIFT library. The SWIFT C API intercepts these messages to make them available to users for diagnosis.

**Returns:**

- – A character, the message for the last known error in SWIFT.

#### swift2.system.runoff_model_ids

```python
runoff_model_ids()
```

Gets all the names of known runoff models

Gets all the names of known runoff models

**Returns:**

- – character vector, names (identifiers) of runoff models

#### swift2.system.runoff_model_var_ids

```python
runoff_model_var_ids(model_id)
```

Gets all the names of the variables a runoff model exposes

Gets all the names of the variables a runoff model exposes for dynamic query.

**Parameters:**

- **model_id** (<code>[Any](#Any)</code>) – character; A recognized model identifier

**Returns:**

- – a character vector, the known model variable that can be set/gotten

#### swift2.system.set_default_max_parallelism_threads

```python
set_default_max_parallelism_threads(n_threads=-1)
```

Sets the level of thread parallelism to use by default for new objects such as optimisers. May be overwritten for each instance afterwards.

**Parameters:**

- **n_threads** (<code>[int](#int)</code>) – number of threads. Positive, or -1 to mean "as many as available"

#### swift2.system.set_maximum_threads

```python
set_maximum_threads(optimiser, n_threads=-1)
```

Sets the maximum level of parallelism of an optimizer

Sets the maximum level of threading of an optimizer. NOTE: this also modifies a global default for further optimizers,
which is a hack for ERRIS, acceptable but still likely to change in the future.
It is VERY important to use this function prior to running calibrations on some systems such as clusters,
as the default hardware detection may not be appropriate if the cluster node is not dedicated.

**Parameters:**

- **optimizer** (<code>[Any](#Any)</code>) – an S4 object 'ExternalObjRef' [package "cinterop"] with external pointer type "OPTIMIZER_PTR"
- **n_threads** (<code>[Any](#Any)</code>) – integer, maximum number of threads allowed. If -1, the system defaults to using all but one of the CPU cores detected on the hardware.

### swift2.utils

**Functions:**

- [**as_xarray_series**](#swift2.utils.as_xarray_series) –
- [**c**](#swift2.utils.c) – Emulate the R c (concatenate) function, somewhat.
- [**is_common_iterable**](#swift2.utils.is_common_iterable) – True if an object is iterable but not a string (str)
- [**mk_full_data_id**](#swift2.utils.mk_full_data_id) – Create swift IDs (dot separated hierarchical naming scheme)
- [**parameter_df**](#swift2.utils.parameter_df) –
- [**parameters_df**](#swift2.utils.parameters_df) –
- [**paste**](#swift2.utils.paste) – Port of R paste function
- [**paste0**](#swift2.utils.paste0) – Port of R paste0 function
- [**paste_2**](#swift2.utils.paste_2) – Port of R vectorised paste, for 2 elements
- [**paste_list_scalar**](#swift2.utils.paste_list_scalar) –
- [**paste_lists**](#swift2.utils.paste_lists) –
- [**paste_scalar_list**](#swift2.utils.paste_scalar_list) –
- [**paste_scalar_scalar**](#swift2.utils.paste_scalar_scalar) –
- [**reduce_concat**](#swift2.utils.reduce_concat) –
- [**rep**](#swift2.utils.rep) –
- [**sort_by**](#swift2.utils.sort_by) – Sort one vector according to the known reordering of another
- [**vpaste**](#swift2.utils.vpaste) – vectorised paste for 2 elements; Port of R paste0 in spirit

#### swift2.utils.as_xarray_series

```python
as_xarray_series(x)
```

#### swift2.utils.c

```python
c(*args)
```

Emulate the R c (concatenate) function, somewhat.

**Returns:**

- <code>[ndarray](#numpy.ndarray)</code> – np.ndarray: [description]

#### swift2.utils.is_common_iterable

```python
is_common_iterable(obj)
```

True if an object is iterable but not a string (str)

#### swift2.utils.mk_full_data_id

```python
mk_full_data_id(*args)
```

Create swift IDs (dot separated hierarchical naming scheme)

Create swift IDs (dot separated hierarchical naming scheme). Note that the behavior is different than 'paste' for empty characters.

**Parameters:**

- **args** (<code>[Any](#typing.Any)</code>) – one or more character vectors.

**Examples:**

TODO

#### swift2.utils.parameter_df

```python
parameter_df(name, value, min, max)
```

#### swift2.utils.parameters_df

```python
parameters_df(names, values, minima, maxima)
```

#### swift2.utils.paste

```python
paste(*lists, sep=' ', collapse=None)
```

Port of R paste function

#### swift2.utils.paste0

```python
paste0(*lists, collapse=None)
```

Port of R paste0 function

#### swift2.utils.paste_2

```python
paste_2(x, y, sep=' ')
```

Port of R vectorised paste, for 2 elements

#### swift2.utils.paste_list_scalar

```python
paste_list_scalar(x, y, sep=' ')
```

#### swift2.utils.paste_lists

```python
paste_lists(x, y, sep=' ')
```

#### swift2.utils.paste_scalar_list

```python
paste_scalar_list(x, y, sep=' ')
```

#### swift2.utils.paste_scalar_scalar

```python
paste_scalar_scalar(x, y, sep=' ')
```

#### swift2.utils.reduce_concat

```python
reduce_concat(z, sep='')
```

#### swift2.utils.rep

```python
rep(x, n)
```

#### swift2.utils.sort_by

```python
sort_by(x, unsorted_reference, sorted_reference)
```

Sort one vector according to the known reordering of another

**Parameters:**

- **x** (<code>[Any](#typing.Any)</code>) – values to sort
- **unsorted_reference** (<code>[Any](#typing.Any)</code>) – unique 'keys' corresponding to each element in x
- **sorted_reference** (<code>[Any](#typing.Any)</code>) – set of 'keys', identical as a set to unsorted_reference, but sorted

**Returns:**

- – the values in x reordered such that the same reordering of unsorted_reference matches sorted_reference

**Examples:**

TODO

#### swift2.utils.vpaste

```python
vpaste(root, vars)
```

vectorised paste for 2 elements; Port of R paste0 in spirit

**Parameters:**

- **root** (<code>[VecScalars](#swift2.const.VecScalars)</code>) – left hand side(s) of the paste
- **vars** (<code>[VecScalars](#swift2.const.VecScalars)</code>) – right hand side(s) of the paste

**Returns:**

- <code>[Union](#typing.Union)\[[str](#str), [Sequence](#typing.Sequence)\[[str](#str)\]\]</code> – Union\[str,Sequence[str]\]: pasted scalars

### swift2.vis

**Classes:**

- [**OptimisationPlots**](#swift2.vis.OptimisationPlots) –

**Functions:**

- [**plot_series**](#swift2.vis.plot_series) –
- [**plot_two_series**](#swift2.vis.plot_two_series) –

#### swift2.vis.OptimisationPlots

```python
OptimisationPlots(optim_geom)
```

**Functions:**

- [**parameter_evolution**](#swift2.vis.OptimisationPlots.parameter_evolution) –
- [**shuffles**](#swift2.vis.OptimisationPlots.shuffles) – Facetted bi-parameter scatter plots of the value of a parameter along the optimisation process

##### swift2.vis.OptimisationPlots.parameter_evolution

```python
parameter_evolution(param_name, obj_lims=None, title='Evolution of parameter values', xlab='Logged point', ylab=None, **kwargs)
```

##### swift2.vis.OptimisationPlots.shuffles

```python
shuffles(x, y, obj_lims=None)
```

Facetted bi-parameter scatter plots of the value of a parameter along the optimisation process

Plot the value of a parameter along the optimisation process.
The color scale is the objective score. Useful to check the behavior of the optimisation process.

**Parameters:**

- **x** (<code>[str](#str)</code>) – the exact name of one of the model parameters
- **y** (<code>[str](#str)</code>) – the exact name of a second model parameter
- **obj_lims** (<code>[Sequence](#typing.Sequence)\[[float](#float)\]</code>) – min/max limits to plot the fitness, for example min 0 for NSE. Defaults to None.

**Returns:**

- <code>[Any](#typing.Any)</code> – sns.FacetGrid: FacetGrid object

#### swift2.vis.plot_series

```python
plot_series(a, start_time=None, end_time=None, name=None, xlab='time', ylab=None, title=None, **kwargs)
```

#### swift2.vis.plot_two_series

```python
plot_two_series(a, b, start_time=None, end_time=None, names=None, xlab='time', ylab=None, title=None, **kwargs)
```

### swift2.wrap

CFFI based wrapper for the SWIFT2 native library

**Modules:**

- [**ffi_interop**](#swift2.wrap.ffi_interop) – Wrapper around SWIFT2 C API functions using CFFI.
- [**swift_wrap_custom**](#swift2.wrap.swift_wrap_custom) –
- [**swift_wrap_generated**](#swift2.wrap.swift_wrap_generated) –

#### swift2.wrap.ffi_interop

Wrapper around SWIFT2 C API functions using CFFI.

**Classes:**

- [**SwiftError**](#swift2.wrap.ffi_interop.SwiftError) – Exception when calling a swift function.

**Functions:**

- [**cc**](#swift2.wrap.ffi_interop.cc) –
- [**check_exceptions**](#swift2.wrap.ffi_interop.check_exceptions) – Returns a wrapper that raises a Python exception if a swift exception
- [**debug_dt_ser**](#swift2.wrap.ffi_interop.debug_dt_ser) –
- [**debug_msd**](#swift2.wrap.ffi_interop.debug_msd) –
- [**debug_stat_ser**](#swift2.wrap.ffi_interop.debug_stat_ser) –
- [**swift_dispose_multi_time_series_data**](#swift2.wrap.ffi_interop.swift_dispose_multi_time_series_data) – :param ptr data: Pointer to a MultiTimeSeriesData.
- [**to_multi_statistic_definition**](#swift2.wrap.ffi_interop.to_multi_statistic_definition) –
- [**unwrap**](#swift2.wrap.ffi_interop.unwrap) –

**Attributes:**

- [**RCPP_STAT_LENGTH_NAME**](#swift2.wrap.ffi_interop.RCPP_STAT_LENGTH_NAME) –
- [**RCPP_STAT_OBJ_ID_NAME**](#swift2.wrap.ffi_interop.RCPP_STAT_OBJ_ID_NAME) –
- [**RCPP_STAT_OBJ_NAME_NAME**](#swift2.wrap.ffi_interop.RCPP_STAT_OBJ_NAME_NAME) –
- [**RCPP_STAT_OBSERVATIONS_NAME**](#swift2.wrap.ffi_interop.RCPP_STAT_OBSERVATIONS_NAME) –
- [**RCPP_STAT_SPEC_NAME**](#swift2.wrap.ffi_interop.RCPP_STAT_SPEC_NAME) –
- [**RCPP_STAT_STAT_ID_NAME**](#swift2.wrap.ffi_interop.RCPP_STAT_STAT_ID_NAME) –
- [**RCPP_STAT_VAR_ID_NAME**](#swift2.wrap.ffi_interop.RCPP_STAT_VAR_ID_NAME) –
- [**RCPP_TS_END_NAME**](#swift2.wrap.ffi_interop.RCPP_TS_END_NAME) –
- [**RCPP_TS_START_NAME**](#swift2.wrap.ffi_interop.RCPP_TS_START_NAME) –
- [**cdefs_dir**](#swift2.wrap.ffi_interop.cdefs_dir) –
- [**here**](#swift2.wrap.ffi_interop.here) –
- [**long_fname**](#swift2.wrap.ffi_interop.long_fname) –
- [**marshal**](#swift2.wrap.ffi_interop.marshal) –
- [**short_fname**](#swift2.wrap.ffi_interop.short_fname) –
- [**swift_ffi**](#swift2.wrap.ffi_interop.swift_ffi) –
- [**swift_pkg_dir**](#swift2.wrap.ffi_interop.swift_pkg_dir) –
- [**swift_so**](#swift2.wrap.ffi_interop.swift_so) –

##### swift2.wrap.ffi_interop.RCPP_STAT_LENGTH_NAME

```python
RCPP_STAT_LENGTH_NAME = 'Length'
```

##### swift2.wrap.ffi_interop.RCPP_STAT_OBJ_ID_NAME

```python
RCPP_STAT_OBJ_ID_NAME = 'ObjectiveId'
```

##### swift2.wrap.ffi_interop.RCPP_STAT_OBJ_NAME_NAME

```python
RCPP_STAT_OBJ_NAME_NAME = 'ObjectiveName'
```

##### swift2.wrap.ffi_interop.RCPP_STAT_OBSERVATIONS_NAME

```python
RCPP_STAT_OBSERVATIONS_NAME = 'Observations'
```

##### swift2.wrap.ffi_interop.RCPP_STAT_SPEC_NAME

```python
RCPP_STAT_SPEC_NAME = 'Statistics'
```

##### swift2.wrap.ffi_interop.RCPP_STAT_STAT_ID_NAME

```python
RCPP_STAT_STAT_ID_NAME = 'StatisticId'
```

##### swift2.wrap.ffi_interop.RCPP_STAT_VAR_ID_NAME

```python
RCPP_STAT_VAR_ID_NAME = 'ModelVarId'
```

##### swift2.wrap.ffi_interop.RCPP_TS_END_NAME

```python
RCPP_TS_END_NAME = 'End'
```

##### swift2.wrap.ffi_interop.RCPP_TS_START_NAME

```python
RCPP_TS_START_NAME = 'Start'
```

##### swift2.wrap.ffi_interop.SwiftError

```python
SwiftError(message)
```

Bases: <code>[Exception](#Exception)</code>

Exception when calling a swift function.

##### swift2.wrap.ffi_interop.cc

```python
cc(x)
```

##### swift2.wrap.ffi_interop.cdefs_dir

```python
cdefs_dir = os.path.join(swift_pkg_dir, 'data')
```

##### swift2.wrap.ffi_interop.check_exceptions

```python
check_exceptions(func)
```

Returns a wrapper that raises a Python exception if a swift exception
occured.

##### swift2.wrap.ffi_interop.debug_dt_ser

```python
debug_dt_ser(d)
```

##### swift2.wrap.ffi_interop.debug_msd

```python
debug_msd(msd)
```

##### swift2.wrap.ffi_interop.debug_stat_ser

```python
debug_stat_ser(s)
```

##### swift2.wrap.ffi_interop.here

```python
here = os.path.abspath(os.path.dirname(__file__))
```

##### swift2.wrap.ffi_interop.long_fname

```python
long_fname = short_fname
```

##### swift2.wrap.ffi_interop.marshal

```python
marshal = CffiMarshal(swift_ffi)
```

##### swift2.wrap.ffi_interop.short_fname

```python
short_fname = library_short_filename('swift')
```

##### swift2.wrap.ffi_interop.swift_dispose_multi_time_series_data

```python
swift_dispose_multi_time_series_data(data)
```

:param ptr data: Pointer to a MultiTimeSeriesData.

##### swift2.wrap.ffi_interop.swift_ffi

```python
swift_ffi = FFI()
```

##### swift2.wrap.ffi_interop.swift_pkg_dir

```python
swift_pkg_dir = os.path.join(here, '..')
```

##### swift2.wrap.ffi_interop.swift_so

```python
swift_so = swift_ffi.dlopen(long_fname, swift_ffi.RTLD_LAZY)
```

##### swift2.wrap.ffi_interop.to_multi_statistic_definition

```python
to_multi_statistic_definition(rTsInfo)
```

##### swift2.wrap.ffi_interop.unwrap

```python
unwrap(x)
```

#### swift2.wrap.swift_wrap_custom

**Functions:**

- [**add_parameters_pkg**](#swift2.wrap.swift_wrap_custom.add_parameters_pkg) –
- [**aggregate_parameterisers_pkg**](#swift2.wrap.swift_wrap_custom.aggregate_parameterisers_pkg) –
- [**convert_optimisation_logger**](#swift2.wrap.swift_wrap_custom.convert_optimisation_logger) –
- [**default_sce_parameters_pkg**](#swift2.wrap.swift_wrap_custom.default_sce_parameters_pkg) –
- [**evaluate_score_wila_pkg**](#swift2.wrap.swift_wrap_custom.evaluate_score_wila_pkg) –
- [**fitnesses_as_rpy_dict**](#swift2.wrap.swift_wrap_custom.fitnesses_as_rpy_dict) –
- [**get_catchment_structure_pkg**](#swift2.wrap.swift_wrap_custom.get_catchment_structure_pkg) –
- [**get_played_data**](#swift2.wrap.swift_wrap_custom.get_played_data) –
- [**get_played_pkg**](#swift2.wrap.swift_wrap_custom.get_played_pkg) –
- [**get_recorded_data**](#swift2.wrap.swift_wrap_custom.get_recorded_data) –
- [**get_recorded_pkg**](#swift2.wrap.swift_wrap_custom.get_recorded_pkg) –
- [**get_simulation_span_pkg**](#swift2.wrap.swift_wrap_custom.get_simulation_span_pkg) –
- [**get_time_series_data_from_provider**](#swift2.wrap.swift_wrap_custom.get_time_series_data_from_provider) –
- [**parameteriser_to_data_frame_pkg**](#swift2.wrap.swift_wrap_custom.parameteriser_to_data_frame_pkg) –
- [**scores_as_rpy_dict**](#swift2.wrap.swift_wrap_custom.scores_as_rpy_dict) –
- [**scores_as_rpy_dict_pkg**](#swift2.wrap.swift_wrap_custom.scores_as_rpy_dict_pkg) –
- [**set_parameters_pkg**](#swift2.wrap.swift_wrap_custom.set_parameters_pkg) –
- [**sort_simulation_elements_by_run_order_pkg**](#swift2.wrap.swift_wrap_custom.sort_simulation_elements_by_run_order_pkg) –
- [**subset_model_pkg**](#swift2.wrap.swift_wrap_custom.subset_model_pkg) –
- [**vec_scores_as_dataframe_pkg**](#swift2.wrap.swift_wrap_custom.vec_scores_as_dataframe_pkg) –

##### swift2.wrap.swift_wrap_custom.add_parameters_pkg

```python
add_parameters_pkg(parameteriser, parameter_specs)
```

##### swift2.wrap.swift_wrap_custom.aggregate_parameterisers_pkg

```python
aggregate_parameterisers_pkg(strategy, parameterisers)
```

##### swift2.wrap.swift_wrap_custom.convert_optimisation_logger

```python
convert_optimisation_logger(log_data, add_numbering=False)
```

##### swift2.wrap.swift_wrap_custom.default_sce_parameters_pkg

```python
default_sce_parameters_pkg(n=4, nshuffle=40)
```

##### swift2.wrap.swift_wrap_custom.evaluate_score_wila_pkg

```python
evaluate_score_wila_pkg(objectives, parameteriser)
```

##### swift2.wrap.swift_wrap_custom.fitnesses_as_rpy_dict

```python
fitnesses_as_rpy_dict(scores)
```

##### swift2.wrap.swift_wrap_custom.get_catchment_structure_pkg

```python
get_catchment_structure_pkg(simulation)
```

##### swift2.wrap.swift_wrap_custom.get_played_data

```python
get_played_data(simulation, variable_identifier, mtsg)
```

##### swift2.wrap.swift_wrap_custom.get_played_pkg

```python
get_played_pkg(simulation, variable_identifier)
```

##### swift2.wrap.swift_wrap_custom.get_recorded_data

```python
get_recorded_data(simulation, variable_identifier, mtsg)
```

##### swift2.wrap.swift_wrap_custom.get_recorded_pkg

```python
get_recorded_pkg(simulation, variable_identifier)
```

##### swift2.wrap.swift_wrap_custom.get_simulation_span_pkg

```python
get_simulation_span_pkg(simulation)
```

##### swift2.wrap.swift_wrap_custom.get_time_series_data_from_provider

```python
get_time_series_data_from_provider(provider, variable_identifier, mtsg)
```

##### swift2.wrap.swift_wrap_custom.parameteriser_to_data_frame_pkg

```python
parameteriser_to_data_frame_pkg(parameteriser)
```

##### swift2.wrap.swift_wrap_custom.scores_as_rpy_dict

```python
scores_as_rpy_dict(scores)
```

##### swift2.wrap.swift_wrap_custom.scores_as_rpy_dict_pkg

```python
scores_as_rpy_dict_pkg(scores_wrapper)
```

##### swift2.wrap.swift_wrap_custom.set_parameters_pkg

```python
set_parameters_pkg(parameteriser, parameter_specs)
```

##### swift2.wrap.swift_wrap_custom.sort_simulation_elements_by_run_order_pkg

```python
sort_simulation_elements_by_run_order_pkg(simulation, elements_ids, ordering_option)
```

##### swift2.wrap.swift_wrap_custom.subset_model_pkg

```python
subset_model_pkg(simulation, element_name, select_network_above_element, include_element_in_selection, invert_selection)
```

##### swift2.wrap.swift_wrap_custom.vec_scores_as_dataframe_pkg

```python
vec_scores_as_dataframe_pkg(setOfScores)
```

#### swift2.wrap.swift_wrap_generated

**Functions:**

- [**AddLinearScalingParameterizer_py**](#swift2.wrap.swift_wrap_generated.AddLinearScalingParameterizer_py) – AddLinearScalingParameterizer_py
- [**AddParameterDefinition_py**](#swift2.wrap.swift_wrap_generated.AddParameterDefinition_py) – AddParameterDefinition_py
- [**AddParameterTransform_py**](#swift2.wrap.swift_wrap_generated.AddParameterTransform_py) – AddParameterTransform_py
- [**AddSingleObservationObjectiveEvaluator_py**](#swift2.wrap.swift_wrap_generated.AddSingleObservationObjectiveEvaluator_py) – AddSingleObservationObjectiveEvaluator_py
- [**AddStateInitializerModelRunner_py**](#swift2.wrap.swift_wrap_generated.AddStateInitializerModelRunner_py) – AddStateInitializerModelRunner_py
- [**AddToCompositeParameterizer_py**](#swift2.wrap.swift_wrap_generated.AddToCompositeParameterizer_py) – AddToCompositeParameterizer_py
- [**AggregateParameterizers_py**](#swift2.wrap.swift_wrap_generated.AggregateParameterizers_py) – AggregateParameterizers_py
- [**ApplyConfiguration_py**](#swift2.wrap.swift_wrap_generated.ApplyConfiguration_py) – ApplyConfiguration_py
- [**ApplyMemoryStates_py**](#swift2.wrap.swift_wrap_generated.ApplyMemoryStates_py) – ApplyMemoryStates_py
- [**CalibrateERRISStageFour_py**](#swift2.wrap.swift_wrap_generated.CalibrateERRISStageFour_py) – CalibrateERRISStageFour_py
- [**CalibrateERRISStageOne_py**](#swift2.wrap.swift_wrap_generated.CalibrateERRISStageOne_py) – CalibrateERRISStageOne_py
- [**CalibrateERRISStageThreeMS_py**](#swift2.wrap.swift_wrap_generated.CalibrateERRISStageThreeMS_py) – CalibrateERRISStageThreeMS_py
- [**CalibrateERRISStageThree_py**](#swift2.wrap.swift_wrap_generated.CalibrateERRISStageThree_py) – CalibrateERRISStageThree_py
- [**CalibrateERRISStageTwo_py**](#swift2.wrap.swift_wrap_generated.CalibrateERRISStageTwo_py) – CalibrateERRISStageTwo_py
- [**CalibrateMAERRISStageFour_py**](#swift2.wrap.swift_wrap_generated.CalibrateMAERRISStageFour_py) – CalibrateMAERRISStageFour_py
- [**CalibrateMAERRISStageOne_py**](#swift2.wrap.swift_wrap_generated.CalibrateMAERRISStageOne_py) – CalibrateMAERRISStageOne_py
- [**CalibrateMAERRISStageThreeMS_py**](#swift2.wrap.swift_wrap_generated.CalibrateMAERRISStageThreeMS_py) – CalibrateMAERRISStageThreeMS_py
- [**CalibrateMAERRISStageThree_py**](#swift2.wrap.swift_wrap_generated.CalibrateMAERRISStageThree_py) – CalibrateMAERRISStageThree_py
- [**CalibrateMAERRISStageTwo_py**](#swift2.wrap.swift_wrap_generated.CalibrateMAERRISStageTwo_py) – CalibrateMAERRISStageTwo_py
- [**CheckSimulationErrors_py**](#swift2.wrap.swift_wrap_generated.CheckSimulationErrors_py) – CheckSimulationErrors_py
- [**ClearMemoryStates_py**](#swift2.wrap.swift_wrap_generated.ClearMemoryStates_py) – ClearMemoryStates_py
- [**CloneHypercubeParameterizer_py**](#swift2.wrap.swift_wrap_generated.CloneHypercubeParameterizer_py) – CloneHypercubeParameterizer_py
- [**CloneModel_py**](#swift2.wrap.swift_wrap_generated.CloneModel_py) – CloneModel_py
- [**CloneObjectiveEvaluator_py**](#swift2.wrap.swift_wrap_generated.CloneObjectiveEvaluator_py) – CloneObjectiveEvaluator_py
- [**CloneStateInitializer_py**](#swift2.wrap.swift_wrap_generated.CloneStateInitializer_py) – CloneStateInitializer_py
- [**ConcatenateERRISStagesParameters_py**](#swift2.wrap.swift_wrap_generated.ConcatenateERRISStagesParameters_py) – ConcatenateERRISStagesParameters_py
- [**ConcatenateMAERRISStagesParameters_py**](#swift2.wrap.swift_wrap_generated.ConcatenateMAERRISStagesParameters_py) – ConcatenateMAERRISStagesParameters_py
- [**CreateCandidateFactorySeedWila_py**](#swift2.wrap.swift_wrap_generated.CreateCandidateFactorySeedWila_py) – CreateCandidateFactorySeedWila_py
- [**CreateCatchment_py**](#swift2.wrap.swift_wrap_generated.CreateCatchment_py) – CreateCatchment_py
- [**CreateCompositeObservationObjectiveEvaluator_py**](#swift2.wrap.swift_wrap_generated.CreateCompositeObservationObjectiveEvaluator_py) – CreateCompositeObservationObjectiveEvaluator_py
- [**CreateCompositeParameterizer_py**](#swift2.wrap.swift_wrap_generated.CreateCompositeParameterizer_py) – CreateCompositeParameterizer_py
- [**CreateERRISParameterEstimator_py**](#swift2.wrap.swift_wrap_generated.CreateERRISParameterEstimator_py) – CreateERRISParameterEstimator_py
- [**CreateEmptyCompositeObjectiveEvaluator_py**](#swift2.wrap.swift_wrap_generated.CreateEmptyCompositeObjectiveEvaluator_py) – CreateEmptyCompositeObjectiveEvaluator_py
- [**CreateEnsembleForecastSimulation_py**](#swift2.wrap.swift_wrap_generated.CreateEnsembleForecastSimulation_py) – CreateEnsembleForecastSimulation_py
- [**CreateEnsembleModelRunner_py**](#swift2.wrap.swift_wrap_generated.CreateEnsembleModelRunner_py) – CreateEnsembleModelRunner_py
- [**CreateFilteringParameterizer_py**](#swift2.wrap.swift_wrap_generated.CreateFilteringParameterizer_py) – CreateFilteringParameterizer_py
- [**CreateFunctionsParameterizer_py**](#swift2.wrap.swift_wrap_generated.CreateFunctionsParameterizer_py) – CreateFunctionsParameterizer_py
- [**CreateGr4ScaledParameterizer_py**](#swift2.wrap.swift_wrap_generated.CreateGr4ScaledParameterizer_py) – CreateGr4ScaledParameterizer_py
- [**CreateHypercubeParameterizer_py**](#swift2.wrap.swift_wrap_generated.CreateHypercubeParameterizer_py) – CreateHypercubeParameterizer_py
- [**CreateLinearFuncParameterizer_py**](#swift2.wrap.swift_wrap_generated.CreateLinearFuncParameterizer_py) – CreateLinearFuncParameterizer_py
- [**CreateMAERRISParameterEstimator_py**](#swift2.wrap.swift_wrap_generated.CreateMAERRISParameterEstimator_py) – CreateMAERRISParameterEstimator_py
- [**CreateMultisiteObjectiveEvaluator_py**](#swift2.wrap.swift_wrap_generated.CreateMultisiteObjectiveEvaluator_py) – CreateMultisiteObjectiveEvaluator_py
- [**CreateMuskingumConstraint_py**](#swift2.wrap.swift_wrap_generated.CreateMuskingumConstraint_py) – CreateMuskingumConstraint_py
- [**CreateNewFromNetworkInfo_py**](#swift2.wrap.swift_wrap_generated.CreateNewFromNetworkInfo_py) – CreateNewFromNetworkInfo_py
- [**CreateOptimizerWila_py**](#swift2.wrap.swift_wrap_generated.CreateOptimizerWila_py) – CreateOptimizerWila_py
- [**CreatePrefixingParameterizer_py**](#swift2.wrap.swift_wrap_generated.CreatePrefixingParameterizer_py) – CreatePrefixingParameterizer_py
- [**CreateSceMarginalTerminationWila_py**](#swift2.wrap.swift_wrap_generated.CreateSceMarginalTerminationWila_py) – CreateSceMarginalTerminationWila_py
- [**CreateSceMaxIterationTerminationWila_py**](#swift2.wrap.swift_wrap_generated.CreateSceMaxIterationTerminationWila_py) – CreateSceMaxIterationTerminationWila_py
- [**CreateSceMaxRuntimeTerminationWila_py**](#swift2.wrap.swift_wrap_generated.CreateSceMaxRuntimeTerminationWila_py) – CreateSceMaxRuntimeTerminationWila_py
- [**CreateSceTerminationWila_py**](#swift2.wrap.swift_wrap_generated.CreateSceTerminationWila_py) – CreateSceTerminationWila_py
- [**CreateShuffledComplexEvolutionWila_py**](#swift2.wrap.swift_wrap_generated.CreateShuffledComplexEvolutionWila_py) – CreateShuffledComplexEvolutionWila_py
- [**CreateSingleObservationObjectiveEvaluatorWila_py**](#swift2.wrap.swift_wrap_generated.CreateSingleObservationObjectiveEvaluatorWila_py) – CreateSingleObservationObjectiveEvaluatorWila_py
- [**CreateSingleObservationObjectiveEvaluator_py**](#swift2.wrap.swift_wrap_generated.CreateSingleObservationObjectiveEvaluator_py) – CreateSingleObservationObjectiveEvaluator_py
- [**CreateSqrtAreaRatioParameterizer_py**](#swift2.wrap.swift_wrap_generated.CreateSqrtAreaRatioParameterizer_py) – CreateSqrtAreaRatioParameterizer_py
- [**CreateStateInitParameterizer_py**](#swift2.wrap.swift_wrap_generated.CreateStateInitParameterizer_py) – CreateStateInitParameterizer_py
- [**CreateStateInitializer_py**](#swift2.wrap.swift_wrap_generated.CreateStateInitializer_py) – CreateStateInitializer_py
- [**CreateSubarea_py**](#swift2.wrap.swift_wrap_generated.CreateSubarea_py) – CreateSubarea_py
- [**CreateSubcatchmentHypercubeParameterizer_py**](#swift2.wrap.swift_wrap_generated.CreateSubcatchmentHypercubeParameterizer_py) – CreateSubcatchmentHypercubeParameterizer_py
- [**CreateTargetScalingParameterizer_py**](#swift2.wrap.swift_wrap_generated.CreateTargetScalingParameterizer_py) – CreateTargetScalingParameterizer_py
- [**CreateTestMemoryTrackedParameterizer_py**](#swift2.wrap.swift_wrap_generated.CreateTestMemoryTrackedParameterizer_py) – CreateTestMemoryTrackedParameterizer_py
- [**CreateTestMemoryTrackedSimulation_py**](#swift2.wrap.swift_wrap_generated.CreateTestMemoryTrackedSimulation_py) – CreateTestMemoryTrackedSimulation_py
- [**CreateTransformParameterizer_py**](#swift2.wrap.swift_wrap_generated.CreateTransformParameterizer_py) – CreateTransformParameterizer_py
- [**DisposeCatchmentStructure_py**](#swift2.wrap.swift_wrap_generated.DisposeCatchmentStructure_py) – DisposeCatchmentStructure_py
- [**DisposeNamedValuedVectorsSwift_py**](#swift2.wrap.swift_wrap_generated.DisposeNamedValuedVectorsSwift_py) – DisposeNamedValuedVectorsSwift_py
- [**DisposeOptimizerLogDataWila_py**](#swift2.wrap.swift_wrap_generated.DisposeOptimizerLogDataWila_py) – DisposeOptimizerLogDataWila_py
- [**DisposeSharedPointer_py**](#swift2.wrap.swift_wrap_generated.DisposeSharedPointer_py) – DisposeSharedPointer_py
- [**DisposeStringStringMapSwift_py**](#swift2.wrap.swift_wrap_generated.DisposeStringStringMapSwift_py) – DisposeStringStringMapSwift_py
- [**EstimateDualPassParameters_py**](#swift2.wrap.swift_wrap_generated.EstimateDualPassParameters_py) – EstimateDualPassParameters_py
- [**EstimateERRISParameters_py**](#swift2.wrap.swift_wrap_generated.EstimateERRISParameters_py) – EstimateERRISParameters_py
- [**EstimateMAERRISParameters_py**](#swift2.wrap.swift_wrap_generated.EstimateMAERRISParameters_py) – EstimateMAERRISParameters_py
- [**EstimateTransformationParametersMS_py**](#swift2.wrap.swift_wrap_generated.EstimateTransformationParametersMS_py) – EstimateTransformationParametersMS_py
- [**EstimateTransformationParameters_py**](#swift2.wrap.swift_wrap_generated.EstimateTransformationParameters_py) – EstimateTransformationParameters_py
- [**EvaluateScoreForParametersInitState_py**](#swift2.wrap.swift_wrap_generated.EvaluateScoreForParametersInitState_py) – EvaluateScoreForParametersInitState_py
- [**EvaluateScoreForParametersWilaInitState_py**](#swift2.wrap.swift_wrap_generated.EvaluateScoreForParametersWilaInitState_py) – EvaluateScoreForParametersWilaInitState_py
- [**EvaluateScoreForParametersWila_py**](#swift2.wrap.swift_wrap_generated.EvaluateScoreForParametersWila_py) – EvaluateScoreForParametersWila_py
- [**EvaluateScoreForParameters_py**](#swift2.wrap.swift_wrap_generated.EvaluateScoreForParameters_py) – EvaluateScoreForParameters_py
- [**EvaluateScore_py**](#swift2.wrap.swift_wrap_generated.EvaluateScore_py) – EvaluateScore_py
- [**EvaluateScoresForParametersWila_py**](#swift2.wrap.swift_wrap_generated.EvaluateScoresForParametersWila_py) – EvaluateScoresForParametersWila_py
- [**ExecuteEnsembleForecastSimulation_py**](#swift2.wrap.swift_wrap_generated.ExecuteEnsembleForecastSimulation_py) – ExecuteEnsembleForecastSimulation_py
- [**ExecuteOptimizerWila_py**](#swift2.wrap.swift_wrap_generated.ExecuteOptimizerWila_py) – ExecuteOptimizerWila_py
- [**ExecuteSimulation_py**](#swift2.wrap.swift_wrap_generated.ExecuteSimulation_py) – ExecuteSimulation_py
- [**GetCatchmentDOTGraph_py**](#swift2.wrap.swift_wrap_generated.GetCatchmentDOTGraph_py) – GetCatchmentDOTGraph_py
- [**GetCatchmentStructure_py**](#swift2.wrap.swift_wrap_generated.GetCatchmentStructure_py) – GetCatchmentStructure_py
- [**GetDefaultMaxThreadsWila_py**](#swift2.wrap.swift_wrap_generated.GetDefaultMaxThreadsWila_py) – GetDefaultMaxThreadsWila_py
- [**GetERRISCalibrationLog_py**](#swift2.wrap.swift_wrap_generated.GetERRISCalibrationLog_py) – GetERRISCalibrationLog_py
- [**GetElementVarIdentifier_py**](#swift2.wrap.swift_wrap_generated.GetElementVarIdentifier_py) – GetElementVarIdentifier_py
- [**GetElementVarIdentifiers_py**](#swift2.wrap.swift_wrap_generated.GetElementVarIdentifiers_py) – GetElementVarIdentifiers_py
- [**GetEnd_py**](#swift2.wrap.swift_wrap_generated.GetEnd_py) – GetEnd_py
- [**GetEnsembleForecastEnsembleRecorded_py**](#swift2.wrap.swift_wrap_generated.GetEnsembleForecastEnsembleRecorded_py) – GetEnsembleForecastEnsembleRecorded_py
- [**GetEnsembleForecastEnsembleSize_py**](#swift2.wrap.swift_wrap_generated.GetEnsembleForecastEnsembleSize_py) – GetEnsembleForecastEnsembleSize_py
- [**GetEnsembleForecastLeadLength_py**](#swift2.wrap.swift_wrap_generated.GetEnsembleForecastLeadLength_py) – GetEnsembleForecastLeadLength_py
- [**GetEnsembleForecastSingleRecorded_py**](#swift2.wrap.swift_wrap_generated.GetEnsembleForecastSingleRecorded_py) – GetEnsembleForecastSingleRecorded_py
- [**GetFeasibleMuskingumBounds_py**](#swift2.wrap.swift_wrap_generated.GetFeasibleMuskingumBounds_py) – GetFeasibleMuskingumBounds_py
- [**GetKnownParameterizationStrategies_py**](#swift2.wrap.swift_wrap_generated.GetKnownParameterizationStrategies_py) – GetKnownParameterizationStrategies_py
- [**GetKnownParameterizationTargetSelectorTypes_py**](#swift2.wrap.swift_wrap_generated.GetKnownParameterizationTargetSelectorTypes_py) – GetKnownParameterizationTargetSelectorTypes_py
- [**GetKnownParameterizerAggregationStrategies_py**](#swift2.wrap.swift_wrap_generated.GetKnownParameterizerAggregationStrategies_py) – GetKnownParameterizerAggregationStrategies_py
- [**GetLastStdExceptionMessage_py**](#swift2.wrap.swift_wrap_generated.GetLastStdExceptionMessage_py) – GetLastStdExceptionMessage_py
- [**GetLengthSetOfScores_py**](#swift2.wrap.swift_wrap_generated.GetLengthSetOfScores_py) – GetLengthSetOfScores_py
- [**GetLinkIdentifier_py**](#swift2.wrap.swift_wrap_generated.GetLinkIdentifier_py) – GetLinkIdentifier_py
- [**GetLinkIdentifiers_py**](#swift2.wrap.swift_wrap_generated.GetLinkIdentifiers_py) – GetLinkIdentifiers_py
- [**GetLinkName_py**](#swift2.wrap.swift_wrap_generated.GetLinkName_py) – GetLinkName_py
- [**GetLinkNames_py**](#swift2.wrap.swift_wrap_generated.GetLinkNames_py) – GetLinkNames_py
- [**GetMAERRISCalibrationLog_py**](#swift2.wrap.swift_wrap_generated.GetMAERRISCalibrationLog_py) – GetMAERRISCalibrationLog_py
- [**GetMemoryStates_py**](#swift2.wrap.swift_wrap_generated.GetMemoryStates_py) – GetMemoryStates_py
- [**GetModelConfigurationSwift_py**](#swift2.wrap.swift_wrap_generated.GetModelConfigurationSwift_py) – GetModelConfigurationSwift_py
- [**GetNameObjectiveEvaluator_py**](#swift2.wrap.swift_wrap_generated.GetNameObjectiveEvaluator_py) – GetNameObjectiveEvaluator_py
- [**GetNodeIdentifier_py**](#swift2.wrap.swift_wrap_generated.GetNodeIdentifier_py) – GetNodeIdentifier_py
- [**GetNodeIdentifiers_py**](#swift2.wrap.swift_wrap_generated.GetNodeIdentifiers_py) – GetNodeIdentifiers_py
- [**GetNodeName_py**](#swift2.wrap.swift_wrap_generated.GetNodeName_py) – GetNodeName_py
- [**GetNodeNames_py**](#swift2.wrap.swift_wrap_generated.GetNodeNames_py) – GetNodeNames_py
- [**GetNumCatchments_py**](#swift2.wrap.swift_wrap_generated.GetNumCatchments_py) – GetNumCatchments_py
- [**GetNumHyperCubesWila_py**](#swift2.wrap.swift_wrap_generated.GetNumHyperCubesWila_py) – GetNumHyperCubesWila_py
- [**GetNumHyperCubes_py**](#swift2.wrap.swift_wrap_generated.GetNumHyperCubes_py) – GetNumHyperCubes_py
- [**GetNumLinks_py**](#swift2.wrap.swift_wrap_generated.GetNumLinks_py) – GetNumLinks_py
- [**GetNumMemTestCatchments_py**](#swift2.wrap.swift_wrap_generated.GetNumMemTestCatchments_py) – GetNumMemTestCatchments_py
- [**GetNumMemTestModelRunners_py**](#swift2.wrap.swift_wrap_generated.GetNumMemTestModelRunners_py) – GetNumMemTestModelRunners_py
- [**GetNumMemTestParameterizers_py**](#swift2.wrap.swift_wrap_generated.GetNumMemTestParameterizers_py) – GetNumMemTestParameterizers_py
- [**GetNumModelRunners_py**](#swift2.wrap.swift_wrap_generated.GetNumModelRunners_py) – GetNumModelRunners_py
- [**GetNumNodes_py**](#swift2.wrap.swift_wrap_generated.GetNumNodes_py) – GetNumNodes_py
- [**GetNumParameters_py**](#swift2.wrap.swift_wrap_generated.GetNumParameters_py) – GetNumParameters_py
- [**GetNumPlayedVariables_py**](#swift2.wrap.swift_wrap_generated.GetNumPlayedVariables_py) – GetNumPlayedVariables_py
- [**GetNumRainfallRunoff_py**](#swift2.wrap.swift_wrap_generated.GetNumRainfallRunoff_py) – GetNumRainfallRunoff_py
- [**GetNumRecordedVariables_py**](#swift2.wrap.swift_wrap_generated.GetNumRecordedVariables_py) – GetNumRecordedVariables_py
- [**GetNumRunoffModelIdentifiers_py**](#swift2.wrap.swift_wrap_generated.GetNumRunoffModelIdentifiers_py) – GetNumRunoffModelIdentifiers_py
- [**GetNumRunoffModelVarIdentifiers_py**](#swift2.wrap.swift_wrap_generated.GetNumRunoffModelVarIdentifiers_py) – GetNumRunoffModelVarIdentifiers_py
- [**GetNumScoresWila_py**](#swift2.wrap.swift_wrap_generated.GetNumScoresWila_py) – GetNumScoresWila_py
- [**GetNumStateInitializers_py**](#swift2.wrap.swift_wrap_generated.GetNumStateInitializers_py) – GetNumStateInitializers_py
- [**GetNumStepsForTimeSpan_py**](#swift2.wrap.swift_wrap_generated.GetNumStepsForTimeSpan_py) – GetNumStepsForTimeSpan_py
- [**GetNumSteps_py**](#swift2.wrap.swift_wrap_generated.GetNumSteps_py) – GetNumSteps_py
- [**GetNumSubareas_py**](#swift2.wrap.swift_wrap_generated.GetNumSubareas_py) – GetNumSubareas_py
- [**GetNumVarIdentifiers_py**](#swift2.wrap.swift_wrap_generated.GetNumVarIdentifiers_py) – GetNumVarIdentifiers_py
- [**GetOptimizerLogDataWilaDims_py**](#swift2.wrap.swift_wrap_generated.GetOptimizerLogDataWilaDims_py) – GetOptimizerLogDataWilaDims_py
- [**GetOptimizerLogDataWilaNumericDataNames_py**](#swift2.wrap.swift_wrap_generated.GetOptimizerLogDataWilaNumericDataNames_py) – GetOptimizerLogDataWilaNumericDataNames_py
- [**GetOptimizerLogDataWilaNumericData_py**](#swift2.wrap.swift_wrap_generated.GetOptimizerLogDataWilaNumericData_py) – GetOptimizerLogDataWilaNumericData_py
- [**GetOptimizerLogDataWilaStringDataNames_py**](#swift2.wrap.swift_wrap_generated.GetOptimizerLogDataWilaStringDataNames_py) – GetOptimizerLogDataWilaStringDataNames_py
- [**GetOptimizerLogDataWilaStringData_py**](#swift2.wrap.swift_wrap_generated.GetOptimizerLogDataWilaStringData_py) – GetOptimizerLogDataWilaStringData_py
- [**GetOptimizerLogDataWila_py**](#swift2.wrap.swift_wrap_generated.GetOptimizerLogDataWila_py) – GetOptimizerLogDataWila_py
- [**GetParameterMaxValue_py**](#swift2.wrap.swift_wrap_generated.GetParameterMaxValue_py) – GetParameterMaxValue_py
- [**GetParameterMinValue_py**](#swift2.wrap.swift_wrap_generated.GetParameterMinValue_py) – GetParameterMinValue_py
- [**GetParameterName_py**](#swift2.wrap.swift_wrap_generated.GetParameterName_py) – GetParameterName_py
- [**GetParameterValue_py**](#swift2.wrap.swift_wrap_generated.GetParameterValue_py) – GetParameterValue_py
- [**GetPlayedTimeSeriesLength_py**](#swift2.wrap.swift_wrap_generated.GetPlayedTimeSeriesLength_py) – GetPlayedTimeSeriesLength_py
- [**GetPlayedTsGeometry_py**](#swift2.wrap.swift_wrap_generated.GetPlayedTsGeometry_py) – GetPlayedTsGeometry_py
- [**GetPlayedVariableName_py**](#swift2.wrap.swift_wrap_generated.GetPlayedVariableName_py) – GetPlayedVariableName_py
- [**GetPlayedVariableNames_py**](#swift2.wrap.swift_wrap_generated.GetPlayedVariableNames_py) – GetPlayedVariableNames_py
- [**GetPlayed_py**](#swift2.wrap.swift_wrap_generated.GetPlayed_py) – GetPlayed_py
- [**GetRecordedEnsembleForecastTimeSeries_py**](#swift2.wrap.swift_wrap_generated.GetRecordedEnsembleForecastTimeSeries_py) – GetRecordedEnsembleForecastTimeSeries_py
- [**GetRecordedTsGeometry_py**](#swift2.wrap.swift_wrap_generated.GetRecordedTsGeometry_py) – GetRecordedTsGeometry_py
- [**GetRecordedVariableName_py**](#swift2.wrap.swift_wrap_generated.GetRecordedVariableName_py) – GetRecordedVariableName_py
- [**GetRecordedVariableNames_py**](#swift2.wrap.swift_wrap_generated.GetRecordedVariableNames_py) – GetRecordedVariableNames_py
- [**GetRecorded_py**](#swift2.wrap.swift_wrap_generated.GetRecorded_py) – GetRecorded_py
- [**GetRunoffModelIdentifier_py**](#swift2.wrap.swift_wrap_generated.GetRunoffModelIdentifier_py) – GetRunoffModelIdentifier_py
- [**GetRunoffModelIdentifiers_py**](#swift2.wrap.swift_wrap_generated.GetRunoffModelIdentifiers_py) – GetRunoffModelIdentifiers_py
- [**GetRunoffModelVarIdentifier_py**](#swift2.wrap.swift_wrap_generated.GetRunoffModelVarIdentifier_py) – GetRunoffModelVarIdentifier_py
- [**GetRunoffModelVarIdentifiers_py**](#swift2.wrap.swift_wrap_generated.GetRunoffModelVarIdentifiers_py) – GetRunoffModelVarIdentifiers_py
- [**GetScoreNameWila_py**](#swift2.wrap.swift_wrap_generated.GetScoreNameWila_py) – GetScoreNameWila_py
- [**GetScoreWila_py**](#swift2.wrap.swift_wrap_generated.GetScoreWila_py) – GetScoreWila_py
- [**GetScoresAtIndex_py**](#swift2.wrap.swift_wrap_generated.GetScoresAtIndex_py) – GetScoresAtIndex_py
- [**GetStart_py**](#swift2.wrap.swift_wrap_generated.GetStart_py) – GetStart_py
- [**GetSubareaIdentifier_py**](#swift2.wrap.swift_wrap_generated.GetSubareaIdentifier_py) – GetSubareaIdentifier_py
- [**GetSubareaIdentifiers_py**](#swift2.wrap.swift_wrap_generated.GetSubareaIdentifiers_py) – GetSubareaIdentifiers_py
- [**GetSubareaName_py**](#swift2.wrap.swift_wrap_generated.GetSubareaName_py) – GetSubareaName_py
- [**GetSubareaNames_py**](#swift2.wrap.swift_wrap_generated.GetSubareaNames_py) – GetSubareaNames_py
- [**GetSystemConfigurationWila_py**](#swift2.wrap.swift_wrap_generated.GetSystemConfigurationWila_py) – GetSystemConfigurationWila_py
- [**GetTimeStepName_py**](#swift2.wrap.swift_wrap_generated.GetTimeStepName_py) – GetTimeStepName_py
- [**GetValueStateInitializer_py**](#swift2.wrap.swift_wrap_generated.GetValueStateInitializer_py) – GetValueStateInitializer_py
- [**GetVariableBool_py**](#swift2.wrap.swift_wrap_generated.GetVariableBool_py) – GetVariableBool_py
- [**GetVariableInt_py**](#swift2.wrap.swift_wrap_generated.GetVariableInt_py) – GetVariableInt_py
- [**GetVariable_py**](#swift2.wrap.swift_wrap_generated.GetVariable_py) – GetVariable_py
- [**HideParameters_py**](#swift2.wrap.swift_wrap_generated.HideParameters_py) – HideParameters_py
- [**HomotheticTransform_py**](#swift2.wrap.swift_wrap_generated.HomotheticTransform_py) – HomotheticTransform_py
- [**IsDictionaryStateInitializer_py**](#swift2.wrap.swift_wrap_generated.IsDictionaryStateInitializer_py) – IsDictionaryStateInitializer_py
- [**IsValidVariableIdentifier_py**](#swift2.wrap.swift_wrap_generated.IsValidVariableIdentifier_py) – IsValidVariableIdentifier_py
- [**IsWithinBounds_py**](#swift2.wrap.swift_wrap_generated.IsWithinBounds_py) – IsWithinBounds_py
- [**LoadMemoryStatesFromFile_py**](#swift2.wrap.swift_wrap_generated.LoadMemoryStatesFromFile_py) – LoadMemoryStatesFromFile_py
- [**LoadModelSimulationFromJson_py**](#swift2.wrap.swift_wrap_generated.LoadModelSimulationFromJson_py) – LoadModelSimulationFromJson_py
- [**LoadParameterizer_py**](#swift2.wrap.swift_wrap_generated.LoadParameterizer_py) – LoadParameterizer_py
- [**LoadVersionOneControlFile_py**](#swift2.wrap.swift_wrap_generated.LoadVersionOneControlFile_py) – LoadVersionOneControlFile_py
- [**LoadVersionOneTimeSeriesFile_py**](#swift2.wrap.swift_wrap_generated.LoadVersionOneTimeSeriesFile_py) – LoadVersionOneTimeSeriesFile_py
- [**MemoryStatesFromString_py**](#swift2.wrap.swift_wrap_generated.MemoryStatesFromString_py) – MemoryStatesFromString_py
- [**ObjectiveEvaluatorIsMaximizable_py**](#swift2.wrap.swift_wrap_generated.ObjectiveEvaluatorIsMaximizable_py) – ObjectiveEvaluatorIsMaximizable_py
- [**PlayDatasetEnsembleForecastInput_py**](#swift2.wrap.swift_wrap_generated.PlayDatasetEnsembleForecastInput_py) – PlayDatasetEnsembleForecastInput_py
- [**PlayDatasetInputs_py**](#swift2.wrap.swift_wrap_generated.PlayDatasetInputs_py) – PlayDatasetInputs_py
- [**PlayDatasetSingleInput_py**](#swift2.wrap.swift_wrap_generated.PlayDatasetSingleInput_py) – PlayDatasetSingleInput_py
- [**PlayEnsembleForecastTimeSeries_py**](#swift2.wrap.swift_wrap_generated.PlayEnsembleForecastTimeSeries_py) – PlayEnsembleForecastTimeSeries_py
- [**Play_py**](#swift2.wrap.swift_wrap_generated.Play_py) – Play_py
- [**PrepareDualPassForecasting_py**](#swift2.wrap.swift_wrap_generated.PrepareDualPassForecasting_py) – PrepareDualPassForecasting_py
- [**PrepareERRISForecasting_py**](#swift2.wrap.swift_wrap_generated.PrepareERRISForecasting_py) – PrepareERRISForecasting_py
- [**PrepareEnsembleModelRunner_py**](#swift2.wrap.swift_wrap_generated.PrepareEnsembleModelRunner_py) – PrepareEnsembleModelRunner_py
- [**RecordEnsembleForecastTimeSeries_py**](#swift2.wrap.swift_wrap_generated.RecordEnsembleForecastTimeSeries_py) – RecordEnsembleForecastTimeSeries_py
- [**RecordEnsembleForecastToRecorder_py**](#swift2.wrap.swift_wrap_generated.RecordEnsembleForecastToRecorder_py) – RecordEnsembleForecastToRecorder_py
- [**RecordEnsembleModelRunner_py**](#swift2.wrap.swift_wrap_generated.RecordEnsembleModelRunner_py) – RecordEnsembleModelRunner_py
- [**Record_py**](#swift2.wrap.swift_wrap_generated.Record_py) – Record_py
- [**RegisterAdditionalSwiftDataHandling_py**](#swift2.wrap.swift_wrap_generated.RegisterAdditionalSwiftDataHandling_py) – RegisterAdditionalSwiftDataHandling_py
- [**RegisterExceptionCallbackSwift_py**](#swift2.wrap.swift_wrap_generated.RegisterExceptionCallbackSwift_py) – RegisterExceptionCallbackSwift_py
- [**RegisterExceptionCallback_py**](#swift2.wrap.swift_wrap_generated.RegisterExceptionCallback_py) – RegisterExceptionCallback_py
- [**RemoveERRISExclusionPeriod_py**](#swift2.wrap.swift_wrap_generated.RemoveERRISExclusionPeriod_py) – RemoveERRISExclusionPeriod_py
- [**RemoveERRISWarmupPeriod_py**](#swift2.wrap.swift_wrap_generated.RemoveERRISWarmupPeriod_py) – RemoveERRISWarmupPeriod_py
- [**RemoveMAERRISExclusionPeriod_py**](#swift2.wrap.swift_wrap_generated.RemoveMAERRISExclusionPeriod_py) – RemoveMAERRISExclusionPeriod_py
- [**RemoveMAERRISWarmupPeriod_py**](#swift2.wrap.swift_wrap_generated.RemoveMAERRISWarmupPeriod_py) – RemoveMAERRISWarmupPeriod_py
- [**RemoveModel_py**](#swift2.wrap.swift_wrap_generated.RemoveModel_py) – RemoveModel_py
- [**RemovePlayedTimeSeries_py**](#swift2.wrap.swift_wrap_generated.RemovePlayedTimeSeries_py) – RemovePlayedTimeSeries_py
- [**RemoveRecorder_py**](#swift2.wrap.swift_wrap_generated.RemoveRecorder_py) – RemoveRecorder_py
- [**RemoveStateInitializerModelRunner_py**](#swift2.wrap.swift_wrap_generated.RemoveStateInitializerModelRunner_py) – RemoveStateInitializerModelRunner_py
- [**RemoveStorageDischargeRelationship_py**](#swift2.wrap.swift_wrap_generated.RemoveStorageDischargeRelationship_py) – RemoveStorageDischargeRelationship_py
- [**ResetModelStates_py**](#swift2.wrap.swift_wrap_generated.ResetModelStates_py) – ResetModelStates_py
- [**SaveMemoryStatesToFile_py**](#swift2.wrap.swift_wrap_generated.SaveMemoryStatesToFile_py) – SaveMemoryStatesToFile_py
- [**SaveModelSimulationToJson_py**](#swift2.wrap.swift_wrap_generated.SaveModelSimulationToJson_py) – SaveModelSimulationToJson_py
- [**SaveParameterizer_py**](#swift2.wrap.swift_wrap_generated.SaveParameterizer_py) – SaveParameterizer_py
- [**SetChannelRoutingModel_py**](#swift2.wrap.swift_wrap_generated.SetChannelRoutingModel_py) – SetChannelRoutingModel_py
- [**SetDefaultMaxThreadsWila_py**](#swift2.wrap.swift_wrap_generated.SetDefaultMaxThreadsWila_py) – SetDefaultMaxThreadsWila_py
- [**SetDefaultParameters_py**](#swift2.wrap.swift_wrap_generated.SetDefaultParameters_py) – SetDefaultParameters_py
- [**SetERRISCensOptions_py**](#swift2.wrap.swift_wrap_generated.SetERRISCensOptions_py) – SetERRISCensOptions_py
- [**SetERRISErrorCorrectionParameterSpace_py**](#swift2.wrap.swift_wrap_generated.SetERRISErrorCorrectionParameterSpace_py) – SetERRISErrorCorrectionParameterSpace_py
- [**SetERRISEstimationPeriod_py**](#swift2.wrap.swift_wrap_generated.SetERRISEstimationPeriod_py) – SetERRISEstimationPeriod_py
- [**SetERRISExclusionPeriod_py**](#swift2.wrap.swift_wrap_generated.SetERRISExclusionPeriod_py) – SetERRISExclusionPeriod_py
- [**SetERRISHydrologicParameterSpace_py**](#swift2.wrap.swift_wrap_generated.SetERRISHydrologicParameterSpace_py) – SetERRISHydrologicParameterSpace_py
- [**SetERRISMaxObservation_py**](#swift2.wrap.swift_wrap_generated.SetERRISMaxObservation_py) – SetERRISMaxObservation_py
- [**SetERRISVerboseCalibration_py**](#swift2.wrap.swift_wrap_generated.SetERRISVerboseCalibration_py) – SetERRISVerboseCalibration_py
- [**SetERRISWarmupPeriod_py**](#swift2.wrap.swift_wrap_generated.SetERRISWarmupPeriod_py) – SetERRISWarmupPeriod_py
- [**SetErrorCorrectionModel_py**](#swift2.wrap.swift_wrap_generated.SetErrorCorrectionModel_py) – SetErrorCorrectionModel_py
- [**SetLogLikelihoodMixtureVariableNames_py**](#swift2.wrap.swift_wrap_generated.SetLogLikelihoodMixtureVariableNames_py) – SetLogLikelihoodMixtureVariableNames_py
- [**SetLogLikelihoodVariableNames_py**](#swift2.wrap.swift_wrap_generated.SetLogLikelihoodVariableNames_py) – SetLogLikelihoodVariableNames_py
- [**SetLogLikelihoodXVariableNames_py**](#swift2.wrap.swift_wrap_generated.SetLogLikelihoodXVariableNames_py) – SetLogLikelihoodXVariableNames_py
- [**SetMAERRISCensOptions_py**](#swift2.wrap.swift_wrap_generated.SetMAERRISCensOptions_py) – SetMAERRISCensOptions_py
- [**SetMAERRISErrorCorrectionParameterSpace_py**](#swift2.wrap.swift_wrap_generated.SetMAERRISErrorCorrectionParameterSpace_py) – SetMAERRISErrorCorrectionParameterSpace_py
- [**SetMAERRISEstimationPeriod_py**](#swift2.wrap.swift_wrap_generated.SetMAERRISEstimationPeriod_py) – SetMAERRISEstimationPeriod_py
- [**SetMAERRISExclusionPeriod_py**](#swift2.wrap.swift_wrap_generated.SetMAERRISExclusionPeriod_py) – SetMAERRISExclusionPeriod_py
- [**SetMAERRISHydrologicParameterSpace_py**](#swift2.wrap.swift_wrap_generated.SetMAERRISHydrologicParameterSpace_py) – SetMAERRISHydrologicParameterSpace_py
- [**SetMAERRISMaxObservation_py**](#swift2.wrap.swift_wrap_generated.SetMAERRISMaxObservation_py) – SetMAERRISMaxObservation_py
- [**SetMAERRISRestrictionOn_py**](#swift2.wrap.swift_wrap_generated.SetMAERRISRestrictionOn_py) – SetMAERRISRestrictionOn_py
- [**SetMAERRISS2Window_py**](#swift2.wrap.swift_wrap_generated.SetMAERRISS2Window_py) – SetMAERRISS2Window_py
- [**SetMAERRISVerboseCalibration_py**](#swift2.wrap.swift_wrap_generated.SetMAERRISVerboseCalibration_py) – SetMAERRISVerboseCalibration_py
- [**SetMAERRISWarmupPeriod_py**](#swift2.wrap.swift_wrap_generated.SetMAERRISWarmupPeriod_py) – SetMAERRISWarmupPeriod_py
- [**SetMaxParameterValue_py**](#swift2.wrap.swift_wrap_generated.SetMaxParameterValue_py) – SetMaxParameterValue_py
- [**SetMaxThreadsOptimizerWila_py**](#swift2.wrap.swift_wrap_generated.SetMaxThreadsOptimizerWila_py) – SetMaxThreadsOptimizerWila_py
- [**SetMemoryStates_py**](#swift2.wrap.swift_wrap_generated.SetMemoryStates_py) – SetMemoryStates_py
- [**SetMinParameterValue_py**](#swift2.wrap.swift_wrap_generated.SetMinParameterValue_py) – SetMinParameterValue_py
- [**SetOptimizerLoggerWila_py**](#swift2.wrap.swift_wrap_generated.SetOptimizerLoggerWila_py) – SetOptimizerLoggerWila_py
- [**SetParameterDefinition_py**](#swift2.wrap.swift_wrap_generated.SetParameterDefinition_py) – SetParameterDefinition_py
- [**SetParameterValue_py**](#swift2.wrap.swift_wrap_generated.SetParameterValue_py) – SetParameterValue_py
- [**SetReservoirGeometry_py**](#swift2.wrap.swift_wrap_generated.SetReservoirGeometry_py) – SetReservoirGeometry_py
- [**SetReservoirMaxDischarge_py**](#swift2.wrap.swift_wrap_generated.SetReservoirMaxDischarge_py) – SetReservoirMaxDischarge_py
- [**SetReservoirMinDischarge_py**](#swift2.wrap.swift_wrap_generated.SetReservoirMinDischarge_py) – SetReservoirMinDischarge_py
- [**SetReservoirModel_py**](#swift2.wrap.swift_wrap_generated.SetReservoirModel_py) – SetReservoirModel_py
- [**SetReservoirOpsReleaseCurve_py**](#swift2.wrap.swift_wrap_generated.SetReservoirOpsReleaseCurve_py) – SetReservoirOpsReleaseCurve_py
- [**SetRunoffPostProcessingModel_py**](#swift2.wrap.swift_wrap_generated.SetRunoffPostProcessingModel_py) – SetRunoffPostProcessingModel_py
- [**SetSeedForModel_py**](#swift2.wrap.swift_wrap_generated.SetSeedForModel_py) – SetSeedForModel_py
- [**SetSpan_py**](#swift2.wrap.swift_wrap_generated.SetSpan_py) – SetSpan_py
- [**SetSubareaInputsPreprocessorModel_py**](#swift2.wrap.swift_wrap_generated.SetSubareaInputsPreprocessorModel_py) – SetSubareaInputsPreprocessorModel_py
- [**SetTimeStep_py**](#swift2.wrap.swift_wrap_generated.SetTimeStep_py) – SetTimeStep_py
- [**SetValueStateInitializer_py**](#swift2.wrap.swift_wrap_generated.SetValueStateInitializer_py) – SetValueStateInitializer_py
- [**SetVariableBool_py**](#swift2.wrap.swift_wrap_generated.SetVariableBool_py) – SetVariableBool_py
- [**SetVariableInt_py**](#swift2.wrap.swift_wrap_generated.SetVariableInt_py) – SetVariableInt_py
- [**SetVariable_py**](#swift2.wrap.swift_wrap_generated.SetVariable_py) – SetVariable_py
- [**SetupEnsembleModelRunner_py**](#swift2.wrap.swift_wrap_generated.SetupEnsembleModelRunner_py) – SetupEnsembleModelRunner_py
- [**ShowParameters_py**](#swift2.wrap.swift_wrap_generated.ShowParameters_py) – ShowParameters_py
- [**SnapshotMemoryStates_py**](#swift2.wrap.swift_wrap_generated.SnapshotMemoryStates_py) – SnapshotMemoryStates_py
- [**SortSetOfScoresBy_py**](#swift2.wrap.swift_wrap_generated.SortSetOfScoresBy_py) – SortSetOfScoresBy_py
- [**SortSimulationElementsByRunOrder_py**](#swift2.wrap.swift_wrap_generated.SortSimulationElementsByRunOrder_py) – SortSimulationElementsByRunOrder_py
- [**SubsetModel_py**](#swift2.wrap.swift_wrap_generated.SubsetModel_py) – SubsetModel_py
- [**SupportsThreadSafeCloning_py**](#swift2.wrap.swift_wrap_generated.SupportsThreadSafeCloning_py) – SupportsThreadSafeCloning_py
- [**SwapRunoffModel_py**](#swift2.wrap.swift_wrap_generated.SwapRunoffModel_py) – SwapRunoffModel_py
- [**TagParameterizer_py**](#swift2.wrap.swift_wrap_generated.TagParameterizer_py) – TagParameterizer_py
- [**UntransformHypercubeParameterizer_py**](#swift2.wrap.swift_wrap_generated.UntransformHypercubeParameterizer_py) – UntransformHypercubeParameterizer_py
- [**UnwrapObjectiveEvaluatorWila_py**](#swift2.wrap.swift_wrap_generated.UnwrapObjectiveEvaluatorWila_py) – UnwrapObjectiveEvaluatorWila_py
- [**UseStateInitializerModelRunner_py**](#swift2.wrap.swift_wrap_generated.UseStateInitializerModelRunner_py) – UseStateInitializerModelRunner_py
- [**VariableIsBool_py**](#swift2.wrap.swift_wrap_generated.VariableIsBool_py) – VariableIsBool_py
- [**VariableIsDouble_py**](#swift2.wrap.swift_wrap_generated.VariableIsDouble_py) – VariableIsDouble_py
- [**VariableIsInt_py**](#swift2.wrap.swift_wrap_generated.VariableIsInt_py) – VariableIsInt_py
- [**WireSubareaInputsPreprocessorModel_py**](#swift2.wrap.swift_wrap_generated.WireSubareaInputsPreprocessorModel_py) – WireSubareaInputsPreprocessorModel_py
- [**WrapObjectiveEvaluatorWila_py**](#swift2.wrap.swift_wrap_generated.WrapObjectiveEvaluatorWila_py) – WrapObjectiveEvaluatorWila_py
- [**char_array_to_py**](#swift2.wrap.swift_wrap_generated.char_array_to_py) –
- [**charp_array_to_py**](#swift2.wrap.swift_wrap_generated.charp_array_to_py) –
- [**custom_wrap_cffi_native_handle**](#swift2.wrap.swift_wrap_generated.custom_wrap_cffi_native_handle) – Create a wrapper around a cffi pointer (if this is one),
- [**dispose_shared_pointer_py**](#swift2.wrap.swift_wrap_generated.dispose_shared_pointer_py) –
- [**named_values_to_py**](#swift2.wrap.swift_wrap_generated.named_values_to_py) –
- [**opaque_ts_as_xarray_time_series**](#swift2.wrap.swift_wrap_generated.opaque_ts_as_xarray_time_series) –
- [**py_time_series_dimensions_description**](#swift2.wrap.swift_wrap_generated.py_time_series_dimensions_description) –
- [**set_wrap_cffi_native_handle**](#swift2.wrap.swift_wrap_generated.set_wrap_cffi_native_handle) –
- [**toSceParametersNative**](#swift2.wrap.swift_wrap_generated.toSceParametersNative) –

##### swift2.wrap.swift_wrap_generated.AddLinearScalingParameterizer_py

```python
AddLinearScalingParameterizer_py(scalingParameterizer, paramName, stateName, scalingVarName, constant, min, max, value)
```

AddLinearScalingParameterizer_py

AddLinearScalingParameterizer_py: generated wrapper function for API function AddLinearScalingParameterizer

**Parameters:**

- **scalingParameterizer** (<code>[ScalingParameteriser](#swift2.classes.ScalingParameteriser)</code>) – scalingParameterizer
- **paramName** (<code>[str](#str)</code>) – paramName
- **stateName** (<code>[str](#str)</code>) – stateName
- **scalingVarName** (<code>[str](#str)</code>) – scalingVarName
- **constant** (<code>[float](#float)</code>) – constant
- **min** (<code>[float](#float)</code>) – min
- **max** (<code>[float](#float)</code>) – max
- **value** (<code>[float](#float)</code>) – value

##### swift2.wrap.swift_wrap_generated.AddParameterDefinition_py

```python
AddParameterDefinition_py(hypercubeParameterizer, variableName, min, max, value)
```

AddParameterDefinition_py

AddParameterDefinition_py: generated wrapper function for API function AddParameterDefinition

**Parameters:**

- **hypercubeParameterizer** (<code>[HypercubeParameteriser](#swift2.classes.HypercubeParameteriser)</code>) – hypercubeParameterizer
- **variableName** (<code>[str](#str)</code>) – variableName
- **min** (<code>[float](#float)</code>) – min
- **max** (<code>[float](#float)</code>) – max
- **value** (<code>[float](#float)</code>) – value

##### swift2.wrap.swift_wrap_generated.AddParameterTransform_py

```python
AddParameterTransform_py(transformParameterizer, paramName, innerParamName, transformId, a, b)
```

AddParameterTransform_py

AddParameterTransform_py: generated wrapper function for API function AddParameterTransform

**Parameters:**

- **transformParameterizer** (<code>[TransformParameteriser](#swift2.classes.TransformParameteriser)</code>) – transformParameterizer
- **paramName** (<code>[str](#str)</code>) – paramName
- **innerParamName** (<code>[str](#str)</code>) – innerParamName
- **transformId** (<code>[str](#str)</code>) – transformId
- **a** (<code>[float](#float)</code>) – a
- **b** (<code>[float](#float)</code>) – b

##### swift2.wrap.swift_wrap_generated.AddSingleObservationObjectiveEvaluator_py

```python
AddSingleObservationObjectiveEvaluator_py(compositeObjective, singleObjective, weight, name)
```

AddSingleObservationObjectiveEvaluator_py

AddSingleObservationObjectiveEvaluator_py: generated wrapper function for API function AddSingleObservationObjectiveEvaluator

**Parameters:**

- **compositeObjective** (<code>[DeletableCffiNativeHandle](#refcount.interop.DeletableCffiNativeHandle)</code>) – compositeObjective
- **singleObjective** (<code>[DeletableCffiNativeHandle](#refcount.interop.DeletableCffiNativeHandle)</code>) – singleObjective
- **weight** (<code>[float](#float)</code>) – weight
- **name** (<code>[str](#str)</code>) – name

##### swift2.wrap.swift_wrap_generated.AddStateInitializerModelRunner_py

```python
AddStateInitializerModelRunner_py(modelSimulation, stateInit)
```

AddStateInitializerModelRunner_py

AddStateInitializerModelRunner_py: generated wrapper function for API function AddStateInitializerModelRunner

**Parameters:**

- **modelSimulation** (<code>[Simulation](#swift2.classes.Simulation)</code>) – modelSimulation
- **stateInit** (<code>[StateInitialiser](#swift2.classes.StateInitialiser)</code>) – stateInit

##### swift2.wrap.swift_wrap_generated.AddToCompositeParameterizer_py

```python
AddToCompositeParameterizer_py(compositeParameterizer, parameterizer)
```

AddToCompositeParameterizer_py

AddToCompositeParameterizer_py: generated wrapper function for API function AddToCompositeParameterizer

**Parameters:**

- **compositeParameterizer** (<code>[CompositeParameteriser](#swift2.classes.CompositeParameteriser)</code>) – compositeParameterizer
- **parameterizer** (<code>[HypercubeParameteriser](#swift2.classes.HypercubeParameteriser)</code>) – parameterizer

##### swift2.wrap.swift_wrap_generated.AggregateParameterizers_py

```python
AggregateParameterizers_py(strategy, parameterizers, numParameterizers)
```

AggregateParameterizers_py

AggregateParameterizers_py: generated wrapper function for API function AggregateParameterizers

**Parameters:**

- **strategy** (<code>[str](#str)</code>) – strategy
- **parameterizers** (<code>[Any](#typing.Any)</code>) – parameterizers
- **numParameterizers** (<code>[int](#int)</code>) – numParameterizers

**Returns:**

- <code>[CompositeParameteriser](#swift2.classes.CompositeParameteriser)</code> – returned result

##### swift2.wrap.swift_wrap_generated.ApplyConfiguration_py

```python
ApplyConfiguration_py(parameterizer, simulation)
```

ApplyConfiguration_py

ApplyConfiguration_py: generated wrapper function for API function ApplyConfiguration

**Parameters:**

- **parameterizer** (<code>[Any](#typing.Any)</code>) – parameterizer
- **simulation** (<code>[Simulation](#swift2.classes.Simulation)</code>) – simulation

##### swift2.wrap.swift_wrap_generated.ApplyMemoryStates_py

```python
ApplyMemoryStates_py(simulation, memoryStates)
```

ApplyMemoryStates_py

ApplyMemoryStates_py: generated wrapper function for API function ApplyMemoryStates

**Parameters:**

- **simulation** (<code>[Simulation](#swift2.classes.Simulation)</code>) – simulation
- **memoryStates** (<code>[MemoryStates](#swift2.classes.MemoryStates)</code>) – memoryStates

##### swift2.wrap.swift_wrap_generated.CalibrateERRISStageFour_py

```python
CalibrateERRISStageFour_py(calibObject, previousStage, useRising)
```

CalibrateERRISStageFour_py

CalibrateERRISStageFour_py: generated wrapper function for API function CalibrateERRISStageFour

**Parameters:**

- **calibObject** (<code>[ErrisStagedCalibration](#swift2.classes.ErrisStagedCalibration)</code>) – calibObject
- **previousStage** (<code>[HypercubeParameteriser](#swift2.classes.HypercubeParameteriser)</code>) – previousStage
- **useRising** (<code>[bool](#bool)</code>) – useRising

**Returns:**

- <code>[HypercubeParameteriser](#swift2.classes.HypercubeParameteriser)</code> – returned result

##### swift2.wrap.swift_wrap_generated.CalibrateERRISStageOne_py

```python
CalibrateERRISStageOne_py(calibObject)
```

CalibrateERRISStageOne_py

CalibrateERRISStageOne_py: generated wrapper function for API function CalibrateERRISStageOne

**Parameters:**

- **calibObject** (<code>[ErrisStagedCalibration](#swift2.classes.ErrisStagedCalibration)</code>) – calibObject

**Returns:**

- <code>[HypercubeParameteriser](#swift2.classes.HypercubeParameteriser)</code> – returned result

##### swift2.wrap.swift_wrap_generated.CalibrateERRISStageThreeMS_py

```python
CalibrateERRISStageThreeMS_py(calibObject, previousStage)
```

CalibrateERRISStageThreeMS_py

CalibrateERRISStageThreeMS_py: generated wrapper function for API function CalibrateERRISStageThreeMS

**Parameters:**

- **calibObject** (<code>[ErrisStagedCalibration](#swift2.classes.ErrisStagedCalibration)</code>) – calibObject
- **previousStage** (<code>[HypercubeParameteriser](#swift2.classes.HypercubeParameteriser)</code>) – previousStage

**Returns:**

- <code>[HypercubeParameteriser](#swift2.classes.HypercubeParameteriser)</code> – returned result

##### swift2.wrap.swift_wrap_generated.CalibrateERRISStageThree_py

```python
CalibrateERRISStageThree_py(calibObject, previousStage)
```

CalibrateERRISStageThree_py

CalibrateERRISStageThree_py: generated wrapper function for API function CalibrateERRISStageThree

**Parameters:**

- **calibObject** (<code>[ErrisStagedCalibration](#swift2.classes.ErrisStagedCalibration)</code>) – calibObject
- **previousStage** (<code>[HypercubeParameteriser](#swift2.classes.HypercubeParameteriser)</code>) – previousStage

**Returns:**

- <code>[HypercubeParameteriser](#swift2.classes.HypercubeParameteriser)</code> – returned result

##### swift2.wrap.swift_wrap_generated.CalibrateERRISStageTwo_py

```python
CalibrateERRISStageTwo_py(calibObject, previousStage)
```

CalibrateERRISStageTwo_py

CalibrateERRISStageTwo_py: generated wrapper function for API function CalibrateERRISStageTwo

**Parameters:**

- **calibObject** (<code>[ErrisStagedCalibration](#swift2.classes.ErrisStagedCalibration)</code>) – calibObject
- **previousStage** (<code>[HypercubeParameteriser](#swift2.classes.HypercubeParameteriser)</code>) – previousStage

**Returns:**

- <code>[HypercubeParameteriser](#swift2.classes.HypercubeParameteriser)</code> – returned result

##### swift2.wrap.swift_wrap_generated.CalibrateMAERRISStageFour_py

```python
CalibrateMAERRISStageFour_py(calibObject, previousStage, useRising)
```

CalibrateMAERRISStageFour_py

CalibrateMAERRISStageFour_py: generated wrapper function for API function CalibrateMAERRISStageFour

**Parameters:**

- **calibObject** (<code>[MaerrisStagedCalibration](#swift2.classes.MaerrisStagedCalibration)</code>) – calibObject
- **previousStage** (<code>[HypercubeParameteriser](#swift2.classes.HypercubeParameteriser)</code>) – previousStage
- **useRising** (<code>[bool](#bool)</code>) – useRising

**Returns:**

- <code>[HypercubeParameteriser](#swift2.classes.HypercubeParameteriser)</code> – returned result

##### swift2.wrap.swift_wrap_generated.CalibrateMAERRISStageOne_py

```python
CalibrateMAERRISStageOne_py(calibObject)
```

CalibrateMAERRISStageOne_py

CalibrateMAERRISStageOne_py: generated wrapper function for API function CalibrateMAERRISStageOne

**Parameters:**

- **calibObject** (<code>[MaerrisStagedCalibration](#swift2.classes.MaerrisStagedCalibration)</code>) – calibObject

**Returns:**

- <code>[HypercubeParameteriser](#swift2.classes.HypercubeParameteriser)</code> – returned result

##### swift2.wrap.swift_wrap_generated.CalibrateMAERRISStageThreeMS_py

```python
CalibrateMAERRISStageThreeMS_py(calibObject, previousStage)
```

CalibrateMAERRISStageThreeMS_py

CalibrateMAERRISStageThreeMS_py: generated wrapper function for API function CalibrateMAERRISStageThreeMS

**Parameters:**

- **calibObject** (<code>[MaerrisStagedCalibration](#swift2.classes.MaerrisStagedCalibration)</code>) – calibObject
- **previousStage** (<code>[HypercubeParameteriser](#swift2.classes.HypercubeParameteriser)</code>) – previousStage

**Returns:**

- <code>[HypercubeParameteriser](#swift2.classes.HypercubeParameteriser)</code> – returned result

##### swift2.wrap.swift_wrap_generated.CalibrateMAERRISStageThree_py

```python
CalibrateMAERRISStageThree_py(calibObject, previousStage)
```

CalibrateMAERRISStageThree_py

CalibrateMAERRISStageThree_py: generated wrapper function for API function CalibrateMAERRISStageThree

**Parameters:**

- **calibObject** (<code>[MaerrisStagedCalibration](#swift2.classes.MaerrisStagedCalibration)</code>) – calibObject
- **previousStage** (<code>[HypercubeParameteriser](#swift2.classes.HypercubeParameteriser)</code>) – previousStage

**Returns:**

- <code>[HypercubeParameteriser](#swift2.classes.HypercubeParameteriser)</code> – returned result

##### swift2.wrap.swift_wrap_generated.CalibrateMAERRISStageTwo_py

```python
CalibrateMAERRISStageTwo_py(calibObject, previousStage)
```

CalibrateMAERRISStageTwo_py

CalibrateMAERRISStageTwo_py: generated wrapper function for API function CalibrateMAERRISStageTwo

**Parameters:**

- **calibObject** (<code>[MaerrisStagedCalibration](#swift2.classes.MaerrisStagedCalibration)</code>) – calibObject
- **previousStage** (<code>[HypercubeParameteriser](#swift2.classes.HypercubeParameteriser)</code>) – previousStage

**Returns:**

- <code>[HypercubeParameteriser](#swift2.classes.HypercubeParameteriser)</code> – returned result

##### swift2.wrap.swift_wrap_generated.CheckSimulationErrors_py

```python
CheckSimulationErrors_py(simulation)
```

CheckSimulationErrors_py

CheckSimulationErrors_py: generated wrapper function for API function CheckSimulationErrors

##### swift2.wrap.swift_wrap_generated.ClearMemoryStates_py

```python
ClearMemoryStates_py(simulation)
```

ClearMemoryStates_py

ClearMemoryStates_py: generated wrapper function for API function ClearMemoryStates

**Parameters:**

- **simulation** (<code>[Simulation](#swift2.classes.Simulation)</code>) – simulation

##### swift2.wrap.swift_wrap_generated.CloneHypercubeParameterizer_py

```python
CloneHypercubeParameterizer_py(hypercubeParameterizer)
```

CloneHypercubeParameterizer_py

CloneHypercubeParameterizer_py: generated wrapper function for API function CloneHypercubeParameterizer

**Parameters:**

- **hypercubeParameterizer** (<code>[HypercubeParameteriser](#swift2.classes.HypercubeParameteriser)</code>) – hypercubeParameterizer

**Returns:**

- <code>[HypercubeParameteriser](#swift2.classes.HypercubeParameteriser)</code> – returned result

##### swift2.wrap.swift_wrap_generated.CloneModel_py

```python
CloneModel_py(simulation)
```

CloneModel_py

CloneModel_py: generated wrapper function for API function CloneModel

**Parameters:**

- **simulation** (<code>[Simulation](#swift2.classes.Simulation)</code>) – simulation

**Returns:**

- <code>[Simulation](#swift2.classes.Simulation)</code> – returned result

##### swift2.wrap.swift_wrap_generated.CloneObjectiveEvaluator_py

```python
CloneObjectiveEvaluator_py(objectiveEvaluator, simulation)
```

CloneObjectiveEvaluator_py

CloneObjectiveEvaluator_py: generated wrapper function for API function CloneObjectiveEvaluator

**Parameters:**

- **objectiveEvaluator** (<code>[DeletableCffiNativeHandle](#refcount.interop.DeletableCffiNativeHandle)</code>) – objectiveEvaluator
- **simulation** (<code>[Simulation](#swift2.classes.Simulation)</code>) – simulation

**Returns:**

- <code>[DeletableCffiNativeHandle](#refcount.interop.DeletableCffiNativeHandle)</code> – returned result

##### swift2.wrap.swift_wrap_generated.CloneStateInitializer_py

```python
CloneStateInitializer_py(stateInitializer)
```

CloneStateInitializer_py

CloneStateInitializer_py: generated wrapper function for API function CloneStateInitializer

**Parameters:**

- **stateInitializer** (<code>[StateInitialiser](#swift2.classes.StateInitialiser)</code>) – stateInitializer

**Returns:**

- <code>[StateInitialiser](#swift2.classes.StateInitialiser)</code> – returned result

##### swift2.wrap.swift_wrap_generated.ConcatenateERRISStagesParameters_py

```python
ConcatenateERRISStagesParameters_py(calibObject, hydroParams, stage1_result, stage2_result, stage3_result, stage4a_result, stage4b_result, toLongParameterName)
```

ConcatenateERRISStagesParameters_py

ConcatenateERRISStagesParameters_py: generated wrapper function for API function ConcatenateERRISStagesParameters

**Parameters:**

- **calibObject** (<code>[ErrisStagedCalibration](#swift2.classes.ErrisStagedCalibration)</code>) – calibObject
- **hydroParams** (<code>[HypercubeParameteriser](#swift2.classes.HypercubeParameteriser)</code>) – hydroParams
- **stage1_result** (<code>[HypercubeParameteriser](#swift2.classes.HypercubeParameteriser)</code>) – stage1_result
- **stage2_result** (<code>[HypercubeParameteriser](#swift2.classes.HypercubeParameteriser)</code>) – stage2_result
- **stage3_result** (<code>[HypercubeParameteriser](#swift2.classes.HypercubeParameteriser)</code>) – stage3_result
- **stage4a_result** (<code>[HypercubeParameteriser](#swift2.classes.HypercubeParameteriser)</code>) – stage4a_result
- **stage4b_result** (<code>[HypercubeParameteriser](#swift2.classes.HypercubeParameteriser)</code>) – stage4b_result
- **toLongParameterName** (<code>[bool](#bool)</code>) – toLongParameterName

**Returns:**

- <code>[HypercubeParameteriser](#swift2.classes.HypercubeParameteriser)</code> – returned result

##### swift2.wrap.swift_wrap_generated.ConcatenateMAERRISStagesParameters_py

```python
ConcatenateMAERRISStagesParameters_py(calibObject, hydroParams, stage1_result, stage2_result, stage3_result, stage4a_result, stage4b_result, toLongParameterName)
```

ConcatenateMAERRISStagesParameters_py

ConcatenateMAERRISStagesParameters_py: generated wrapper function for API function ConcatenateMAERRISStagesParameters

**Parameters:**

- **calibObject** (<code>[MaerrisStagedCalibration](#swift2.classes.MaerrisStagedCalibration)</code>) – calibObject
- **hydroParams** (<code>[HypercubeParameteriser](#swift2.classes.HypercubeParameteriser)</code>) – hydroParams
- **stage1_result** (<code>[HypercubeParameteriser](#swift2.classes.HypercubeParameteriser)</code>) – stage1_result
- **stage2_result** (<code>[HypercubeParameteriser](#swift2.classes.HypercubeParameteriser)</code>) – stage2_result
- **stage3_result** (<code>[HypercubeParameteriser](#swift2.classes.HypercubeParameteriser)</code>) – stage3_result
- **stage4a_result** (<code>[HypercubeParameteriser](#swift2.classes.HypercubeParameteriser)</code>) – stage4a_result
- **stage4b_result** (<code>[HypercubeParameteriser](#swift2.classes.HypercubeParameteriser)</code>) – stage4b_result
- **toLongParameterName** (<code>[bool](#bool)</code>) – toLongParameterName

**Returns:**

- <code>[HypercubeParameteriser](#swift2.classes.HypercubeParameteriser)</code> – returned result

##### swift2.wrap.swift_wrap_generated.CreateCandidateFactorySeedWila_py

```python
CreateCandidateFactorySeedWila_py(hypercubeParameterizer, type, seed)
```

CreateCandidateFactorySeedWila_py

CreateCandidateFactorySeedWila_py: generated wrapper function for API function CreateCandidateFactorySeedWila

**Parameters:**

- **hypercubeParameterizer** (<code>[HypercubeParameteriser](#swift2.classes.HypercubeParameteriser)</code>) – hypercubeParameterizer
- **type** (<code>[str](#str)</code>) – type
- **seed** (<code>[int](#int)</code>) – seed

**Returns:**

- <code>[CandidateFactorySeed](#swift2.classes.CandidateFactorySeed)</code> – returned result

##### swift2.wrap.swift_wrap_generated.CreateCatchment_py

```python
CreateCatchment_py(numNodes, nodeIds, nodeNames, numLinks, linkIds, linkNames, linkFromNode, linkToNode, runoffModelName, areasKm2)
```

CreateCatchment_py

CreateCatchment_py: generated wrapper function for API function CreateCatchment

**Parameters:**

- **numNodes** (<code>[int](#int)</code>) – numNodes
- **nodeIds** (<code>[List](#typing.List)\[[str](#str)\]</code>) – nodeIds
- **nodeNames** (<code>[List](#typing.List)\[[str](#str)\]</code>) – nodeNames
- **numLinks** (<code>[int](#int)</code>) – numLinks
- **linkIds** (<code>[List](#typing.List)\[[str](#str)\]</code>) – linkIds
- **linkNames** (<code>[List](#typing.List)\[[str](#str)\]</code>) – linkNames
- **linkFromNode** (<code>[List](#typing.List)\[[str](#str)\]</code>) – linkFromNode
- **linkToNode** (<code>[List](#typing.List)\[[str](#str)\]</code>) – linkToNode
- **runoffModelName** (<code>[str](#str)</code>) – runoffModelName
- **areasKm2** (<code>[ndarray](#numpy.ndarray)</code>) – areasKm2

**Returns:**

- <code>[Simulation](#swift2.classes.Simulation)</code> – returned result

##### swift2.wrap.swift_wrap_generated.CreateCompositeObservationObjectiveEvaluator_py

```python
CreateCompositeObservationObjectiveEvaluator_py(simulation, obsVarId, observations, obsGeom, yamlStatIdString)
```

CreateCompositeObservationObjectiveEvaluator_py

CreateCompositeObservationObjectiveEvaluator_py: generated wrapper function for API function CreateCompositeObservationObjectiveEvaluator

**Parameters:**

- **simulation** (<code>[Simulation](#swift2.classes.Simulation)</code>) – simulation
- **obsVarId** (<code>[str](#str)</code>) – obsVarId
- **observations** (<code>[ndarray](#numpy.ndarray)</code>) – observations
- **obsGeom** (<code>[TimeSeriesGeometryNative](#cinterop.cffi.marshal.TimeSeriesGeometryNative)</code>) – obsGeom
- **yamlStatIdString** (<code>[str](#str)</code>) – yamlStatIdString

**Returns:**

- <code>[DeletableCffiNativeHandle](#refcount.interop.DeletableCffiNativeHandle)</code> – returned result

##### swift2.wrap.swift_wrap_generated.CreateCompositeParameterizer_py

```python
CreateCompositeParameterizer_py()
```

CreateCompositeParameterizer_py

CreateCompositeParameterizer_py: generated wrapper function for API function CreateCompositeParameterizer

Args:

**Returns:**

- <code>[CompositeParameteriser](#swift2.classes.CompositeParameteriser)</code> – returned result

##### swift2.wrap.swift_wrap_generated.CreateERRISParameterEstimator_py

```python
CreateERRISParameterEstimator_py(mr, obsValues, obsGeom, errorModelElementId, estimationStart, estimationEnd, censThr, censOpt, terminationCondition, restrictionOn, weightedLeastSquare)
```

CreateERRISParameterEstimator_py

CreateERRISParameterEstimator_py: generated wrapper function for API function CreateERRISParameterEstimator

**Parameters:**

- **mr** (<code>[Simulation](#swift2.classes.Simulation)</code>) – mr
- **obsValues** (<code>[ndarray](#numpy.ndarray)</code>) – obsValues
- **obsGeom** (<code>[TimeSeriesGeometryNative](#cinterop.cffi.marshal.TimeSeriesGeometryNative)</code>) – obsGeom
- **errorModelElementId** (<code>[str](#str)</code>) – errorModelElementId
- **estimationStart** (<code>[datetime](#datetime.datetime)</code>) – estimationStart
- **estimationEnd** (<code>[datetime](#datetime.datetime)</code>) – estimationEnd
- **censThr** (<code>[float](#float)</code>) – censThr
- **censOpt** (<code>[float](#float)</code>) – censOpt
- **terminationCondition** (<code>[SceTerminationCondition](#swift2.classes.SceTerminationCondition)</code>) – terminationCondition
- **restrictionOn** (<code>[bool](#bool)</code>) – restrictionOn
- **weightedLeastSquare** (<code>[bool](#bool)</code>) – weightedLeastSquare

**Returns:**

- <code>[ErrisStagedCalibration](#swift2.classes.ErrisStagedCalibration)</code> – returned result

##### swift2.wrap.swift_wrap_generated.CreateEmptyCompositeObjectiveEvaluator_py

```python
CreateEmptyCompositeObjectiveEvaluator_py()
```

CreateEmptyCompositeObjectiveEvaluator_py

CreateEmptyCompositeObjectiveEvaluator_py: generated wrapper function for API function CreateEmptyCompositeObjectiveEvaluator

Args:

**Returns:**

- <code>[DeletableCffiNativeHandle](#refcount.interop.DeletableCffiNativeHandle)</code> – returned result

##### swift2.wrap.swift_wrap_generated.CreateEnsembleForecastSimulation_py

```python
CreateEnsembleForecastSimulation_py(simulation, start, leadTime, ensembleSize, simulationLength, nTimeStepsBetweenForecasts)
```

CreateEnsembleForecastSimulation_py

CreateEnsembleForecastSimulation_py: generated wrapper function for API function CreateEnsembleForecastSimulation

**Parameters:**

- **simulation** (<code>[Simulation](#swift2.classes.Simulation)</code>) – simulation
- **start** (<code>[datetime](#datetime.datetime)</code>) – start
- **leadTime** (<code>[int](#int)</code>) – leadTime
- **ensembleSize** (<code>[int](#int)</code>) – ensembleSize
- **simulationLength** (<code>[int](#int)</code>) – simulationLength
- **nTimeStepsBetweenForecasts** (<code>[int](#int)</code>) – nTimeStepsBetweenForecasts

**Returns:**

- <code>[EnsembleForecastSimulation](#swift2.classes.EnsembleForecastSimulation)</code> – returned result

##### swift2.wrap.swift_wrap_generated.CreateEnsembleModelRunner_py

```python
CreateEnsembleModelRunner_py(simulation, ensembleSize)
```

CreateEnsembleModelRunner_py

CreateEnsembleModelRunner_py: generated wrapper function for API function CreateEnsembleModelRunner

**Parameters:**

- **simulation** (<code>[Simulation](#swift2.classes.Simulation)</code>) – simulation
- **ensembleSize** (<code>[int](#int)</code>) – ensembleSize

**Returns:**

- <code>[EnsembleSimulation](#swift2.classes.EnsembleSimulation)</code> – returned result

##### swift2.wrap.swift_wrap_generated.CreateFilteringParameterizer_py

```python
CreateFilteringParameterizer_py(p)
```

CreateFilteringParameterizer_py

CreateFilteringParameterizer_py: generated wrapper function for API function CreateFilteringParameterizer

**Parameters:**

- **p** (<code>[HypercubeParameteriser](#swift2.classes.HypercubeParameteriser)</code>) – p

**Returns:**

- <code>[FilteringParameteriser](#swift2.classes.FilteringParameteriser)</code> – returned result

##### swift2.wrap.swift_wrap_generated.CreateFunctionsParameterizer_py

```python
CreateFunctionsParameterizer_py(modelParameters, functionsParameters)
```

CreateFunctionsParameterizer_py

CreateFunctionsParameterizer_py: generated wrapper function for API function CreateFunctionsParameterizer

**Parameters:**

- **modelParameters** (<code>[HypercubeParameteriser](#swift2.classes.HypercubeParameteriser)</code>) – modelParameters
- **functionsParameters** (<code>[HypercubeParameteriser](#swift2.classes.HypercubeParameteriser)</code>) – functionsParameters

**Returns:**

- <code>[FunctionsParameteriser](#swift2.classes.FunctionsParameteriser)</code> – returned result

##### swift2.wrap.swift_wrap_generated.CreateGr4ScaledParameterizer_py

```python
CreateGr4ScaledParameterizer_py(referenceAreaKm2, tStepSeconds)
```

CreateGr4ScaledParameterizer_py

CreateGr4ScaledParameterizer_py: generated wrapper function for API function CreateGr4ScaledParameterizer

**Parameters:**

- **referenceAreaKm2** (<code>[float](#float)</code>) – referenceAreaKm2
- **tStepSeconds** (<code>[int](#int)</code>) – tStepSeconds

**Returns:**

- <code>[CompositeParameteriser](#swift2.classes.CompositeParameteriser)</code> – returned result

##### swift2.wrap.swift_wrap_generated.CreateHypercubeParameterizer_py

```python
CreateHypercubeParameterizer_py(strategy)
```

CreateHypercubeParameterizer_py

CreateHypercubeParameterizer_py: generated wrapper function for API function CreateHypercubeParameterizer

**Parameters:**

- **strategy** (<code>[str](#str)</code>) – strategy

**Returns:**

- <code>[HypercubeParameteriser](#swift2.classes.HypercubeParameteriser)</code> – returned result

##### swift2.wrap.swift_wrap_generated.CreateLinearFuncParameterizer_py

```python
CreateLinearFuncParameterizer_py(paramName, innerParamName, observedState, constant, min, max, value, selectorType)
```

CreateLinearFuncParameterizer_py

CreateLinearFuncParameterizer_py: generated wrapper function for API function CreateLinearFuncParameterizer

**Parameters:**

- **paramName** (<code>[str](#str)</code>) – paramName
- **innerParamName** (<code>[str](#str)</code>) – innerParamName
- **observedState** (<code>[str](#str)</code>) – observedState
- **constant** (<code>[float](#float)</code>) – constant
- **min** (<code>[float](#float)</code>) – min
- **max** (<code>[float](#float)</code>) – max
- **value** (<code>[float](#float)</code>) – value
- **selectorType** (<code>[str](#str)</code>) – selectorType

**Returns:**

- <code>[ScalingParameteriser](#swift2.classes.ScalingParameteriser)</code> – returned result

##### swift2.wrap.swift_wrap_generated.CreateMAERRISParameterEstimator_py

```python
CreateMAERRISParameterEstimator_py(mr, obsValues, obsGeom, errorModelElementId, estimationStart, estimationEnd, s2Window, censThr, censOpt, terminationCondition, restrictionOn)
```

CreateMAERRISParameterEstimator_py

CreateMAERRISParameterEstimator_py: generated wrapper function for API function CreateMAERRISParameterEstimator

**Parameters:**

- **mr** (<code>[Simulation](#swift2.classes.Simulation)</code>) – mr
- **obsValues** (<code>[ndarray](#numpy.ndarray)</code>) – obsValues
- **obsGeom** (<code>[TimeSeriesGeometryNative](#cinterop.cffi.marshal.TimeSeriesGeometryNative)</code>) – obsGeom
- **errorModelElementId** (<code>[str](#str)</code>) – errorModelElementId
- **estimationStart** (<code>[datetime](#datetime.datetime)</code>) – estimationStart
- **estimationEnd** (<code>[datetime](#datetime.datetime)</code>) – estimationEnd
- **s2Window** (<code>[float](#float)</code>) – s2Window
- **censThr** (<code>[float](#float)</code>) – censThr
- **censOpt** (<code>[float](#float)</code>) – censOpt
- **terminationCondition** (<code>[SceTerminationCondition](#swift2.classes.SceTerminationCondition)</code>) – terminationCondition
- **restrictionOn** (<code>[bool](#bool)</code>) – restrictionOn

**Returns:**

- <code>[MaerrisStagedCalibration](#swift2.classes.MaerrisStagedCalibration)</code> – returned result

##### swift2.wrap.swift_wrap_generated.CreateMultisiteObjectiveEvaluator_py

```python
CreateMultisiteObjectiveEvaluator_py(simulation, defn, weights)
```

CreateMultisiteObjectiveEvaluator_py

CreateMultisiteObjectiveEvaluator_py: generated wrapper function for API function CreateMultisiteObjectiveEvaluator

**Parameters:**

- **simulation** (<code>[Simulation](#swift2.classes.Simulation)</code>) – simulation
- **defn** (<code>[Any](#typing.Any)</code>) – defn
- **weights** (<code>[Dict](#typing.Dict)\[[str](#str), [float](#float)\]</code>) – weights

**Returns:**

- <code>[DeletableCffiNativeHandle](#refcount.interop.DeletableCffiNativeHandle)</code> – returned result

##### swift2.wrap.swift_wrap_generated.CreateMuskingumConstraint_py

```python
CreateMuskingumConstraint_py(hypercubeParameterizer, deltaTHours, paramNameK, paramNameX, simulation)
```

CreateMuskingumConstraint_py

CreateMuskingumConstraint_py: generated wrapper function for API function CreateMuskingumConstraint

**Parameters:**

- **hypercubeParameterizer** (<code>[HypercubeParameteriser](#swift2.classes.HypercubeParameteriser)</code>) – hypercubeParameterizer
- **deltaTHours** (<code>[float](#float)</code>) – deltaTHours
- **paramNameK** (<code>[str](#str)</code>) – paramNameK
- **paramNameX** (<code>[str](#str)</code>) – paramNameX
- **simulation** (<code>[Simulation](#swift2.classes.Simulation)</code>) – simulation

**Returns:**

- <code>[ConstraintParameteriser](#swift2.classes.ConstraintParameteriser)</code> – returned result

##### swift2.wrap.swift_wrap_generated.CreateNewFromNetworkInfo_py

```python
CreateNewFromNetworkInfo_py(nodes, numNodes, links, numLinks)
```

CreateNewFromNetworkInfo_py

CreateNewFromNetworkInfo_py: generated wrapper function for API function CreateNewFromNetworkInfo

**Parameters:**

- **nodes** (<code>[Any](#typing.Any)</code>) – nodes
- **numNodes** (<code>[int](#int)</code>) – numNodes
- **links** (<code>[Any](#typing.Any)</code>) – links
- **numLinks** (<code>[int](#int)</code>) – numLinks

**Returns:**

- <code>[Simulation](#swift2.classes.Simulation)</code> – returned result

##### swift2.wrap.swift_wrap_generated.CreateOptimizerWila_py

```python
CreateOptimizerWila_py(objective, parameterizer, parameters)
```

CreateOptimizerWila_py

CreateOptimizerWila_py: generated wrapper function for API function CreateOptimizerWila

**Parameters:**

- **objective** (<code>[ObjectiveEvaluator](#swift2.classes.ObjectiveEvaluator)</code>) – objective
- **parameterizer** (<code>[HypercubeParameteriser](#swift2.classes.HypercubeParameteriser)</code>) – parameterizer
- **parameters** (<code>[Dict](#typing.Dict)\[[str](#str), [str](#str)\]</code>) – parameters

**Returns:**

- <code>[Optimiser](#swift2.classes.Optimiser)</code> – returned result

##### swift2.wrap.swift_wrap_generated.CreatePrefixingParameterizer_py

```python
CreatePrefixingParameterizer_py(p, prefix)
```

CreatePrefixingParameterizer_py

CreatePrefixingParameterizer_py: generated wrapper function for API function CreatePrefixingParameterizer

**Parameters:**

- **p** (<code>[HypercubeParameteriser](#swift2.classes.HypercubeParameteriser)</code>) – p
- **prefix** (<code>[str](#str)</code>) – prefix

**Returns:**

- <code>[HypercubeParameteriser](#swift2.classes.HypercubeParameteriser)</code> – returned result

##### swift2.wrap.swift_wrap_generated.CreateSceMarginalTerminationWila_py

```python
CreateSceMarginalTerminationWila_py(tolerance, cutoffNoImprovement, maxHours)
```

CreateSceMarginalTerminationWila_py

CreateSceMarginalTerminationWila_py: generated wrapper function for API function CreateSceMarginalTerminationWila

**Parameters:**

- **tolerance** (<code>[float](#float)</code>) – tolerance
- **cutoffNoImprovement** (<code>[int](#int)</code>) – cutoffNoImprovement
- **maxHours** (<code>[float](#float)</code>) – maxHours

**Returns:**

- <code>[SceTerminationCondition](#swift2.classes.SceTerminationCondition)</code> – returned result

##### swift2.wrap.swift_wrap_generated.CreateSceMaxIterationTerminationWila_py

```python
CreateSceMaxIterationTerminationWila_py(maxIterations)
```

CreateSceMaxIterationTerminationWila_py

CreateSceMaxIterationTerminationWila_py: generated wrapper function for API function CreateSceMaxIterationTerminationWila

**Parameters:**

- **maxIterations** (<code>[int](#int)</code>) – maxIterations

**Returns:**

- <code>[SceTerminationCondition](#swift2.classes.SceTerminationCondition)</code> – returned result

##### swift2.wrap.swift_wrap_generated.CreateSceMaxRuntimeTerminationWila_py

```python
CreateSceMaxRuntimeTerminationWila_py(maxHours)
```

CreateSceMaxRuntimeTerminationWila_py

CreateSceMaxRuntimeTerminationWila_py: generated wrapper function for API function CreateSceMaxRuntimeTerminationWila

**Parameters:**

- **maxHours** (<code>[float](#float)</code>) – maxHours

**Returns:**

- <code>[SceTerminationCondition](#swift2.classes.SceTerminationCondition)</code> – returned result

##### swift2.wrap.swift_wrap_generated.CreateSceTerminationWila_py

```python
CreateSceTerminationWila_py(type, arguments, numArguments)
```

CreateSceTerminationWila_py

CreateSceTerminationWila_py: generated wrapper function for API function CreateSceTerminationWila

**Parameters:**

- **type** (<code>[str](#str)</code>) – type
- **arguments** (<code>[List](#typing.List)\[[str](#str)\]</code>) – arguments
- **numArguments** (<code>[int](#int)</code>) – numArguments

**Returns:**

- <code>[SceTerminationCondition](#swift2.classes.SceTerminationCondition)</code> – returned result

##### swift2.wrap.swift_wrap_generated.CreateShuffledComplexEvolutionWila_py

```python
CreateShuffledComplexEvolutionWila_py(objective, terminationCriterion, SCEpars, populationInitializer)
```

CreateShuffledComplexEvolutionWila_py

CreateShuffledComplexEvolutionWila_py: generated wrapper function for API function CreateShuffledComplexEvolutionWila

**Parameters:**

- **objective** (<code>[ObjectiveEvaluator](#swift2.classes.ObjectiveEvaluator)</code>) – objective
- **terminationCriterion** (<code>[SceTerminationCondition](#swift2.classes.SceTerminationCondition)</code>) – terminationCriterion
- **SCEpars** (<code>[Dict](#typing.Dict)\[[str](#str), [float](#float)\]</code>) – SCEpars
- **populationInitializer** (<code>[CandidateFactorySeed](#swift2.classes.CandidateFactorySeed)</code>) – populationInitializer

**Returns:**

- <code>[Optimiser](#swift2.classes.Optimiser)</code> – returned result

##### swift2.wrap.swift_wrap_generated.CreateSingleObservationObjectiveEvaluatorWila_py

```python
CreateSingleObservationObjectiveEvaluatorWila_py(simulation, obsVarId, observations, obsGeom, statisticId)
```

CreateSingleObservationObjectiveEvaluatorWila_py

CreateSingleObservationObjectiveEvaluatorWila_py: generated wrapper function for API function CreateSingleObservationObjectiveEvaluatorWila

**Parameters:**

- **simulation** (<code>[Simulation](#swift2.classes.Simulation)</code>) – simulation
- **obsVarId** (<code>[str](#str)</code>) – obsVarId
- **observations** (<code>[ndarray](#numpy.ndarray)</code>) – observations
- **obsGeom** (<code>[TimeSeriesGeometryNative](#cinterop.cffi.marshal.TimeSeriesGeometryNative)</code>) – obsGeom
- **statisticId** (<code>[str](#str)</code>) – statisticId

**Returns:**

- <code>[ObjectiveEvaluator](#swift2.classes.ObjectiveEvaluator)</code> – returned result

##### swift2.wrap.swift_wrap_generated.CreateSingleObservationObjectiveEvaluator_py

```python
CreateSingleObservationObjectiveEvaluator_py(simulation, obsVarId, observations, obsGeom, statisticId)
```

CreateSingleObservationObjectiveEvaluator_py

CreateSingleObservationObjectiveEvaluator_py: generated wrapper function for API function CreateSingleObservationObjectiveEvaluator

**Parameters:**

- **simulation** (<code>[Simulation](#swift2.classes.Simulation)</code>) – simulation
- **obsVarId** (<code>[str](#str)</code>) – obsVarId
- **observations** (<code>[ndarray](#numpy.ndarray)</code>) – observations
- **obsGeom** (<code>[TimeSeriesGeometryNative](#cinterop.cffi.marshal.TimeSeriesGeometryNative)</code>) – obsGeom
- **statisticId** (<code>[str](#str)</code>) – statisticId

**Returns:**

- <code>[DeletableCffiNativeHandle](#refcount.interop.DeletableCffiNativeHandle)</code> – returned result

##### swift2.wrap.swift_wrap_generated.CreateSqrtAreaRatioParameterizer_py

```python
CreateSqrtAreaRatioParameterizer_py(referenceAreaKm2, paramName, innerParamName, min, max, value)
```

CreateSqrtAreaRatioParameterizer_py

CreateSqrtAreaRatioParameterizer_py: generated wrapper function for API function CreateSqrtAreaRatioParameterizer

**Parameters:**

- **referenceAreaKm2** (<code>[float](#float)</code>) – referenceAreaKm2
- **paramName** (<code>[str](#str)</code>) – paramName
- **innerParamName** (<code>[str](#str)</code>) – innerParamName
- **min** (<code>[float](#float)</code>) – min
- **max** (<code>[float](#float)</code>) – max
- **value** (<code>[float](#float)</code>) – value

**Returns:**

- <code>[DeletableCffiNativeHandle](#refcount.interop.DeletableCffiNativeHandle)</code> – returned result

##### swift2.wrap.swift_wrap_generated.CreateStateInitParameterizer_py

```python
CreateStateInitParameterizer_py(hypercubeParameterizer)
```

CreateStateInitParameterizer_py

CreateStateInitParameterizer_py: generated wrapper function for API function CreateStateInitParameterizer

**Parameters:**

- **hypercubeParameterizer** (<code>[HypercubeParameteriser](#swift2.classes.HypercubeParameteriser)</code>) – hypercubeParameterizer

**Returns:**

- <code>[StateInitParameteriser](#swift2.classes.StateInitParameteriser)</code> – returned result

##### swift2.wrap.swift_wrap_generated.CreateStateInitializer_py

```python
CreateStateInitializer_py(type)
```

CreateStateInitializer_py

CreateStateInitializer_py: generated wrapper function for API function CreateStateInitializer

**Parameters:**

- **type** (<code>[str](#str)</code>) – type

**Returns:**

- <code>[StateInitialiser](#swift2.classes.StateInitialiser)</code> – returned result

##### swift2.wrap.swift_wrap_generated.CreateSubarea_py

```python
CreateSubarea_py(modelId, areaKm2)
```

CreateSubarea_py

CreateSubarea_py: generated wrapper function for API function CreateSubarea

**Parameters:**

- **modelId** (<code>[str](#str)</code>) – modelId
- **areaKm2** (<code>[float](#float)</code>) – areaKm2

**Returns:**

- <code>[Simulation](#swift2.classes.Simulation)</code> – returned result

##### swift2.wrap.swift_wrap_generated.CreateSubcatchmentHypercubeParameterizer_py

```python
CreateSubcatchmentHypercubeParameterizer_py(parameterizer, subcatchment)
```

CreateSubcatchmentHypercubeParameterizer_py

CreateSubcatchmentHypercubeParameterizer_py: generated wrapper function for API function CreateSubcatchmentHypercubeParameterizer

**Parameters:**

- **parameterizer** (<code>[HypercubeParameteriser](#swift2.classes.HypercubeParameteriser)</code>) – parameterizer
- **subcatchment** (<code>[Simulation](#swift2.classes.Simulation)</code>) – subcatchment

**Returns:**

- <code>[HypercubeParameteriser](#swift2.classes.HypercubeParameteriser)</code> – returned result

##### swift2.wrap.swift_wrap_generated.CreateTargetScalingParameterizer_py

```python
CreateTargetScalingParameterizer_py(selectorType)
```

CreateTargetScalingParameterizer_py

CreateTargetScalingParameterizer_py: generated wrapper function for API function CreateTargetScalingParameterizer

**Parameters:**

- **selectorType** (<code>[str](#str)</code>) – selectorType

**Returns:**

- <code>[ScalingParameteriser](#swift2.classes.ScalingParameteriser)</code> – returned result

##### swift2.wrap.swift_wrap_generated.CreateTestMemoryTrackedParameterizer_py

```python
CreateTestMemoryTrackedParameterizer_py()
```

CreateTestMemoryTrackedParameterizer_py

CreateTestMemoryTrackedParameterizer_py: generated wrapper function for API function CreateTestMemoryTrackedParameterizer

Args:

**Returns:**

- <code>[HypercubeParameteriser](#swift2.classes.HypercubeParameteriser)</code> – returned result

##### swift2.wrap.swift_wrap_generated.CreateTestMemoryTrackedSimulation_py

```python
CreateTestMemoryTrackedSimulation_py()
```

CreateTestMemoryTrackedSimulation_py

CreateTestMemoryTrackedSimulation_py: generated wrapper function for API function CreateTestMemoryTrackedSimulation

Args:

**Returns:**

- <code>[Simulation](#swift2.classes.Simulation)</code> – returned result

##### swift2.wrap.swift_wrap_generated.CreateTransformParameterizer_py

```python
CreateTransformParameterizer_py(hypercubeParameterizer)
```

CreateTransformParameterizer_py

CreateTransformParameterizer_py: generated wrapper function for API function CreateTransformParameterizer

**Parameters:**

- **hypercubeParameterizer** (<code>[HypercubeParameteriser](#swift2.classes.HypercubeParameteriser)</code>) – hypercubeParameterizer

**Returns:**

- <code>[TransformParameteriser](#swift2.classes.TransformParameteriser)</code> – returned result

##### swift2.wrap.swift_wrap_generated.DisposeCatchmentStructure_py

```python
DisposeCatchmentStructure_py(structure)
```

DisposeCatchmentStructure_py

DisposeCatchmentStructure_py: generated wrapper function for API function DisposeCatchmentStructure

**Parameters:**

- **structure** (<code>[DeletableCffiNativeHandle](#refcount.interop.DeletableCffiNativeHandle)</code>) – structure

##### swift2.wrap.swift_wrap_generated.DisposeNamedValuedVectorsSwift_py

```python
DisposeNamedValuedVectorsSwift_py(v)
```

DisposeNamedValuedVectorsSwift_py

DisposeNamedValuedVectorsSwift_py: generated wrapper function for API function DisposeNamedValuedVectorsSwift

**Parameters:**

- **v** (<code>[Dict](#typing.Dict)\[[str](#str), [float](#float)\]</code>) – v

##### swift2.wrap.swift_wrap_generated.DisposeOptimizerLogDataWila_py

```python
DisposeOptimizerLogDataWila_py(logData)
```

DisposeOptimizerLogDataWila_py

DisposeOptimizerLogDataWila_py: generated wrapper function for API function DisposeOptimizerLogDataWila

**Parameters:**

- **logData** (<code>[DeletableCffiNativeHandle](#refcount.interop.DeletableCffiNativeHandle)</code>) – logData

##### swift2.wrap.swift_wrap_generated.DisposeSharedPointer_py

```python
DisposeSharedPointer_py(ptr)
```

DisposeSharedPointer_py

DisposeSharedPointer_py: generated wrapper function for API function DisposeSharedPointer

**Parameters:**

- **ptr** (<code>[Any](#typing.Any)</code>) – ptr

##### swift2.wrap.swift_wrap_generated.DisposeStringStringMapSwift_py

```python
DisposeStringStringMapSwift_py(v)
```

DisposeStringStringMapSwift_py

DisposeStringStringMapSwift_py: generated wrapper function for API function DisposeStringStringMapSwift

**Parameters:**

- **v** (<code>[Dict](#typing.Dict)\[[str](#str), [str](#str)\]</code>) – v

##### swift2.wrap.swift_wrap_generated.EstimateDualPassParameters_py

```python
EstimateDualPassParameters_py(simulation, obsValues, obsGeom, errorModelElementId, warmupStart, warmupEnd, warmup, estimationStart, estimationEnd, windowL, windowDecayL, windowDecayS, useLongPass, objFuncDescYaml, exclusionStart, exclusionEnd, exclusion, terminationCondition)
```

EstimateDualPassParameters_py

EstimateDualPassParameters_py: generated wrapper function for API function EstimateDualPassParameters

**Parameters:**

- **simulation** (<code>[Simulation](#swift2.classes.Simulation)</code>) – simulation
- **obsValues** (<code>[ndarray](#numpy.ndarray)</code>) – obsValues
- **obsGeom** (<code>[TimeSeriesGeometryNative](#cinterop.cffi.marshal.TimeSeriesGeometryNative)</code>) – obsGeom
- **errorModelElementId** (<code>[str](#str)</code>) – errorModelElementId
- **warmupStart** (<code>[datetime](#datetime.datetime)</code>) – warmupStart
- **warmupEnd** (<code>[datetime](#datetime.datetime)</code>) – warmupEnd
- **warmup** (<code>[bool](#bool)</code>) – warmup
- **estimationStart** (<code>[datetime](#datetime.datetime)</code>) – estimationStart
- **estimationEnd** (<code>[datetime](#datetime.datetime)</code>) – estimationEnd
- **windowL** (<code>[int](#int)</code>) – windowL
- **windowDecayL** (<code>[int](#int)</code>) – windowDecayL
- **windowDecayS** (<code>[int](#int)</code>) – windowDecayS
- **useLongPass** (<code>[bool](#bool)</code>) – useLongPass
- **objFuncDescYaml** (<code>[str](#str)</code>) – objFuncDescYaml
- **exclusionStart** (<code>[datetime](#datetime.datetime)</code>) – exclusionStart
- **exclusionEnd** (<code>[datetime](#datetime.datetime)</code>) – exclusionEnd
- **exclusion** (<code>[bool](#bool)</code>) – exclusion
- **terminationCondition** (<code>[SceTerminationCondition](#swift2.classes.SceTerminationCondition)</code>) – terminationCondition

**Returns:**

- <code>[HypercubeParameteriser](#swift2.classes.HypercubeParameteriser)</code> – returned result

##### swift2.wrap.swift_wrap_generated.EstimateERRISParameters_py

```python
EstimateERRISParameters_py(simulation, obsValues, obsGeom, errorModelElementId, warmupStart, warmupEnd, warmup, estimationStart, estimationEnd, censThr, censOpt, exclusionStart, exclusionEnd, exclusion, terminationCondition, errisParams, hydroParams, restrictionOn, weightedLeastSquare)
```

EstimateERRISParameters_py

EstimateERRISParameters_py: generated wrapper function for API function EstimateERRISParameters

**Parameters:**

- **simulation** (<code>[Simulation](#swift2.classes.Simulation)</code>) – simulation
- **obsValues** (<code>[ndarray](#numpy.ndarray)</code>) – obsValues
- **obsGeom** (<code>[TimeSeriesGeometryNative](#cinterop.cffi.marshal.TimeSeriesGeometryNative)</code>) – obsGeom
- **errorModelElementId** (<code>[str](#str)</code>) – errorModelElementId
- **warmupStart** (<code>[datetime](#datetime.datetime)</code>) – warmupStart
- **warmupEnd** (<code>[datetime](#datetime.datetime)</code>) – warmupEnd
- **warmup** (<code>[bool](#bool)</code>) – warmup
- **estimationStart** (<code>[datetime](#datetime.datetime)</code>) – estimationStart
- **estimationEnd** (<code>[datetime](#datetime.datetime)</code>) – estimationEnd
- **censThr** (<code>[float](#float)</code>) – censThr
- **censOpt** (<code>[float](#float)</code>) – censOpt
- **exclusionStart** (<code>[datetime](#datetime.datetime)</code>) – exclusionStart
- **exclusionEnd** (<code>[datetime](#datetime.datetime)</code>) – exclusionEnd
- **exclusion** (<code>[bool](#bool)</code>) – exclusion
- **terminationCondition** (<code>[SceTerminationCondition](#swift2.classes.SceTerminationCondition)</code>) – terminationCondition
- **errisParams** (<code>[HypercubeParameteriser](#swift2.classes.HypercubeParameteriser)</code>) – errisParams
- **hydroParams** (<code>[HypercubeParameteriser](#swift2.classes.HypercubeParameteriser)</code>) – hydroParams
- **restrictionOn** (<code>[bool](#bool)</code>) – restrictionOn
- **weightedLeastSquare** (<code>[bool](#bool)</code>) – weightedLeastSquare

**Returns:**

- <code>[HypercubeParameteriser](#swift2.classes.HypercubeParameteriser)</code> – returned result

##### swift2.wrap.swift_wrap_generated.EstimateMAERRISParameters_py

```python
EstimateMAERRISParameters_py(simulation, obsValues, obsGeom, errorModelElementId, warmupStart, warmupEnd, warmup, estimationStart, estimationEnd, s2Window, censThr, censOpt, exclusionStart, exclusionEnd, exclusion, terminationCondition, maerrisParams, hydroParams, restrictionOn)
```

EstimateMAERRISParameters_py

EstimateMAERRISParameters_py: generated wrapper function for API function EstimateMAERRISParameters

**Parameters:**

- **simulation** (<code>[Simulation](#swift2.classes.Simulation)</code>) – simulation
- **obsValues** (<code>[ndarray](#numpy.ndarray)</code>) – obsValues
- **obsGeom** (<code>[TimeSeriesGeometryNative](#cinterop.cffi.marshal.TimeSeriesGeometryNative)</code>) – obsGeom
- **errorModelElementId** (<code>[str](#str)</code>) – errorModelElementId
- **warmupStart** (<code>[datetime](#datetime.datetime)</code>) – warmupStart
- **warmupEnd** (<code>[datetime](#datetime.datetime)</code>) – warmupEnd
- **warmup** (<code>[bool](#bool)</code>) – warmup
- **estimationStart** (<code>[datetime](#datetime.datetime)</code>) – estimationStart
- **estimationEnd** (<code>[datetime](#datetime.datetime)</code>) – estimationEnd
- **s2Window** (<code>[float](#float)</code>) – s2Window
- **censThr** (<code>[float](#float)</code>) – censThr
- **censOpt** (<code>[float](#float)</code>) – censOpt
- **exclusionStart** (<code>[datetime](#datetime.datetime)</code>) – exclusionStart
- **exclusionEnd** (<code>[datetime](#datetime.datetime)</code>) – exclusionEnd
- **exclusion** (<code>[bool](#bool)</code>) – exclusion
- **terminationCondition** (<code>[SceTerminationCondition](#swift2.classes.SceTerminationCondition)</code>) – terminationCondition
- **maerrisParams** (<code>[HypercubeParameteriser](#swift2.classes.HypercubeParameteriser)</code>) – maerrisParams
- **hydroParams** (<code>[HypercubeParameteriser](#swift2.classes.HypercubeParameteriser)</code>) – hydroParams
- **restrictionOn** (<code>[bool](#bool)</code>) – restrictionOn

**Returns:**

- <code>[HypercubeParameteriser](#swift2.classes.HypercubeParameteriser)</code> – returned result

##### swift2.wrap.swift_wrap_generated.EstimateTransformationParametersMS_py

```python
EstimateTransformationParametersMS_py(obsValues, obsGeom, estimationStart, estimationEnd, exclusionStart, exclusionEnd, exclusion, terminationCondition, Params)
```

EstimateTransformationParametersMS_py

EstimateTransformationParametersMS_py: generated wrapper function for API function EstimateTransformationParametersMS

**Parameters:**

- **obsValues** (<code>[ndarray](#numpy.ndarray)</code>) – obsValues
- **obsGeom** (<code>[TimeSeriesGeometryNative](#cinterop.cffi.marshal.TimeSeriesGeometryNative)</code>) – obsGeom
- **estimationStart** (<code>[datetime](#datetime.datetime)</code>) – estimationStart
- **estimationEnd** (<code>[datetime](#datetime.datetime)</code>) – estimationEnd
- **exclusionStart** (<code>[datetime](#datetime.datetime)</code>) – exclusionStart
- **exclusionEnd** (<code>[datetime](#datetime.datetime)</code>) – exclusionEnd
- **exclusion** (<code>[bool](#bool)</code>) – exclusion
- **terminationCondition** (<code>[SceTerminationCondition](#swift2.classes.SceTerminationCondition)</code>) – terminationCondition
- **Params** (<code>[HypercubeParameteriser](#swift2.classes.HypercubeParameteriser)</code>) – Params

**Returns:**

- <code>[HypercubeParameteriser](#swift2.classes.HypercubeParameteriser)</code> – returned result

##### swift2.wrap.swift_wrap_generated.EstimateTransformationParameters_py

```python
EstimateTransformationParameters_py(obsValues, obsGeom, estimationStart, estimationEnd, censThr, censOpt, exclusionStart, exclusionEnd, exclusion, terminationCondition)
```

EstimateTransformationParameters_py

EstimateTransformationParameters_py: generated wrapper function for API function EstimateTransformationParameters

**Parameters:**

- **obsValues** (<code>[ndarray](#numpy.ndarray)</code>) – obsValues
- **obsGeom** (<code>[TimeSeriesGeometryNative](#cinterop.cffi.marshal.TimeSeriesGeometryNative)</code>) – obsGeom
- **estimationStart** (<code>[datetime](#datetime.datetime)</code>) – estimationStart
- **estimationEnd** (<code>[datetime](#datetime.datetime)</code>) – estimationEnd
- **censThr** (<code>[float](#float)</code>) – censThr
- **censOpt** (<code>[float](#float)</code>) – censOpt
- **exclusionStart** (<code>[datetime](#datetime.datetime)</code>) – exclusionStart
- **exclusionEnd** (<code>[datetime](#datetime.datetime)</code>) – exclusionEnd
- **exclusion** (<code>[bool](#bool)</code>) – exclusion
- **terminationCondition** (<code>[SceTerminationCondition](#swift2.classes.SceTerminationCondition)</code>) – terminationCondition

**Returns:**

- <code>[HypercubeParameteriser](#swift2.classes.HypercubeParameteriser)</code> – returned result

##### swift2.wrap.swift_wrap_generated.EvaluateScoreForParametersInitState_py

```python
EvaluateScoreForParametersInitState_py(objectiveEvaluator, parameterizer)
```

EvaluateScoreForParametersInitState_py

EvaluateScoreForParametersInitState_py: generated wrapper function for API function EvaluateScoreForParametersInitState

**Parameters:**

- **objectiveEvaluator** (<code>[DeletableCffiNativeHandle](#refcount.interop.DeletableCffiNativeHandle)</code>) – objectiveEvaluator
- **parameterizer** (<code>[Any](#typing.Any)</code>) – parameterizer

**Returns:**

- <code>[float](#float)</code> – returned result

##### swift2.wrap.swift_wrap_generated.EvaluateScoreForParametersWilaInitState_py

```python
EvaluateScoreForParametersWilaInitState_py(objectiveEvaluator, hypercubeParameterizer)
```

EvaluateScoreForParametersWilaInitState_py

EvaluateScoreForParametersWilaInitState_py: generated wrapper function for API function EvaluateScoreForParametersWilaInitState

**Parameters:**

- **objectiveEvaluator** (<code>[ObjectiveEvaluator](#swift2.classes.ObjectiveEvaluator)</code>) – objectiveEvaluator
- **hypercubeParameterizer** (<code>[HypercubeParameteriser](#swift2.classes.HypercubeParameteriser)</code>) – hypercubeParameterizer

**Returns:**

- <code>[ObjectiveScores](#swift2.classes.ObjectiveScores)</code> – returned result

##### swift2.wrap.swift_wrap_generated.EvaluateScoreForParametersWila_py

```python
EvaluateScoreForParametersWila_py(objectiveEvaluator, hypercubeParameterizer)
```

EvaluateScoreForParametersWila_py

EvaluateScoreForParametersWila_py: generated wrapper function for API function EvaluateScoreForParametersWila

**Parameters:**

- **objectiveEvaluator** (<code>[ObjectiveEvaluator](#swift2.classes.ObjectiveEvaluator)</code>) – objectiveEvaluator
- **hypercubeParameterizer** (<code>[HypercubeParameteriser](#swift2.classes.HypercubeParameteriser)</code>) – hypercubeParameterizer

**Returns:**

- <code>[ObjectiveScores](#swift2.classes.ObjectiveScores)</code> – returned result

##### swift2.wrap.swift_wrap_generated.EvaluateScoreForParameters_py

```python
EvaluateScoreForParameters_py(objectiveEvaluator, parameterizer)
```

EvaluateScoreForParameters_py

EvaluateScoreForParameters_py: generated wrapper function for API function EvaluateScoreForParameters

**Parameters:**

- **objectiveEvaluator** (<code>[DeletableCffiNativeHandle](#refcount.interop.DeletableCffiNativeHandle)</code>) – objectiveEvaluator
- **parameterizer** (<code>[Any](#typing.Any)</code>) – parameterizer

**Returns:**

- <code>[float](#float)</code> – returned result

##### swift2.wrap.swift_wrap_generated.EvaluateScore_py

```python
EvaluateScore_py(objectiveEvaluator)
```

EvaluateScore_py

EvaluateScore_py: generated wrapper function for API function EvaluateScore

**Parameters:**

- **objectiveEvaluator** (<code>[DeletableCffiNativeHandle](#refcount.interop.DeletableCffiNativeHandle)</code>) – objectiveEvaluator

**Returns:**

- <code>[float](#float)</code> – returned result

##### swift2.wrap.swift_wrap_generated.EvaluateScoresForParametersWila_py

```python
EvaluateScoresForParametersWila_py(objectiveEvaluator, parameterizer)
```

EvaluateScoresForParametersWila_py

EvaluateScoresForParametersWila_py: generated wrapper function for API function EvaluateScoresForParametersWila

**Parameters:**

- **objectiveEvaluator** (<code>[ObjectiveEvaluator](#swift2.classes.ObjectiveEvaluator)</code>) – objectiveEvaluator
- **parameterizer** (<code>[HypercubeParameteriser](#swift2.classes.HypercubeParameteriser)</code>) – parameterizer

**Returns:**

- <code>[Dict](#typing.Dict)\[[str](#str), [float](#float)\]</code> – returned result

##### swift2.wrap.swift_wrap_generated.ExecuteEnsembleForecastSimulation_py

```python
ExecuteEnsembleForecastSimulation_py(efSimulation)
```

ExecuteEnsembleForecastSimulation_py

ExecuteEnsembleForecastSimulation_py: generated wrapper function for API function ExecuteEnsembleForecastSimulation

**Parameters:**

- **efSimulation** (<code>[EnsembleForecastSimulation](#swift2.classes.EnsembleForecastSimulation)</code>) – efSimulation

##### swift2.wrap.swift_wrap_generated.ExecuteOptimizerWila_py

```python
ExecuteOptimizerWila_py(optimizer)
```

ExecuteOptimizerWila_py

ExecuteOptimizerWila_py: generated wrapper function for API function ExecuteOptimizerWila

**Parameters:**

- **optimizer** (<code>[Optimiser](#swift2.classes.Optimiser)</code>) – optimizer

**Returns:**

- <code>[VectorObjectiveScores](#swift2.classes.VectorObjectiveScores)</code> – returned result

##### swift2.wrap.swift_wrap_generated.ExecuteSimulation_py

```python
ExecuteSimulation_py(simulation, resetInitialStates)
```

ExecuteSimulation_py

ExecuteSimulation_py: generated wrapper function for API function ExecuteSimulation

**Parameters:**

- **simulation** (<code>[Simulation](#swift2.classes.Simulation)</code>) – simulation
- **resetInitialStates** (<code>[bool](#bool)</code>) – resetInitialStates

##### swift2.wrap.swift_wrap_generated.GetCatchmentDOTGraph_py

```python
GetCatchmentDOTGraph_py(simulation)
```

GetCatchmentDOTGraph_py

GetCatchmentDOTGraph_py: generated wrapper function for API function GetCatchmentDOTGraph

**Parameters:**

- **simulation** (<code>[Simulation](#swift2.classes.Simulation)</code>) – simulation

**Returns:**

- <code>[str](#str)</code> – returned result

##### swift2.wrap.swift_wrap_generated.GetCatchmentStructure_py

```python
GetCatchmentStructure_py(simulation)
```

GetCatchmentStructure_py

GetCatchmentStructure_py: generated wrapper function for API function GetCatchmentStructure

**Parameters:**

- **simulation** (<code>[Simulation](#swift2.classes.Simulation)</code>) – simulation

**Returns:**

- <code>[DeletableCffiNativeHandle](#refcount.interop.DeletableCffiNativeHandle)</code> – returned result

##### swift2.wrap.swift_wrap_generated.GetDefaultMaxThreadsWila_py

```python
GetDefaultMaxThreadsWila_py()
```

GetDefaultMaxThreadsWila_py

GetDefaultMaxThreadsWila_py: generated wrapper function for API function GetDefaultMaxThreadsWila

Args:

**Returns:**

- <code>[int](#int)</code> – returned result

##### swift2.wrap.swift_wrap_generated.GetERRISCalibrationLog_py

```python
GetERRISCalibrationLog_py(calibObject)
```

GetERRISCalibrationLog_py

GetERRISCalibrationLog_py: generated wrapper function for API function GetERRISCalibrationLog

**Parameters:**

- **calibObject** (<code>[ErrisStagedCalibration](#swift2.classes.ErrisStagedCalibration)</code>) – calibObject

**Returns:**

- <code>[DeletableCffiNativeHandle](#refcount.interop.DeletableCffiNativeHandle)</code> – returned result

##### swift2.wrap.swift_wrap_generated.GetElementVarIdentifier_py

```python
GetElementVarIdentifier_py(simulation, elementId, index)
```

GetElementVarIdentifier_py

GetElementVarIdentifier_py: generated wrapper function for API function GetElementVarIdentifier

**Parameters:**

- **simulation** (<code>[Simulation](#swift2.classes.Simulation)</code>) – simulation
- **elementId** (<code>[str](#str)</code>) – elementId
- **index** (<code>[int](#int)</code>) – index

**Returns:**

- <code>[str](#str)</code> – returned result

##### swift2.wrap.swift_wrap_generated.GetElementVarIdentifiers_py

```python
GetElementVarIdentifiers_py(simulation, elementId)
```

GetElementVarIdentifiers_py

GetElementVarIdentifiers_py: generated wrapper function for API function GetElementVarIdentifiers

##### swift2.wrap.swift_wrap_generated.GetEnd_py

```python
GetEnd_py(simulation, end)
```

GetEnd_py

GetEnd_py: generated wrapper function for API function GetEnd

**Parameters:**

- **simulation** (<code>[Any](#typing.Any)</code>) – simulation
- **end** (<code>[Any](#typing.Any)</code>) – end

##### swift2.wrap.swift_wrap_generated.GetEnsembleForecastEnsembleRecorded_py

```python
GetEnsembleForecastEnsembleRecorded_py(efSimulation, variableIdentifier, leadTimeIndex, values)
```

GetEnsembleForecastEnsembleRecorded_py

GetEnsembleForecastEnsembleRecorded_py: generated wrapper function for API function GetEnsembleForecastEnsembleRecorded

**Parameters:**

- **efSimulation** (<code>[EnsembleForecastSimulation](#swift2.classes.EnsembleForecastSimulation)</code>) – efSimulation
- **variableIdentifier** (<code>[str](#str)</code>) – variableIdentifier
- **leadTimeIndex** (<code>[int](#int)</code>) – leadTimeIndex
- **values** (<code>[ndarray](#numpy.ndarray)</code>) – values

##### swift2.wrap.swift_wrap_generated.GetEnsembleForecastEnsembleSize_py

```python
GetEnsembleForecastEnsembleSize_py(efSimulation)
```

GetEnsembleForecastEnsembleSize_py

GetEnsembleForecastEnsembleSize_py: generated wrapper function for API function GetEnsembleForecastEnsembleSize

**Parameters:**

- **efSimulation** (<code>[EnsembleForecastSimulation](#swift2.classes.EnsembleForecastSimulation)</code>) – efSimulation

**Returns:**

- <code>[int](#int)</code> – returned result

##### swift2.wrap.swift_wrap_generated.GetEnsembleForecastLeadLength_py

```python
GetEnsembleForecastLeadLength_py(efSimulation)
```

GetEnsembleForecastLeadLength_py

GetEnsembleForecastLeadLength_py: generated wrapper function for API function GetEnsembleForecastLeadLength

**Parameters:**

- **efSimulation** (<code>[EnsembleForecastSimulation](#swift2.classes.EnsembleForecastSimulation)</code>) – efSimulation

**Returns:**

- <code>[int](#int)</code> – returned result

##### swift2.wrap.swift_wrap_generated.GetEnsembleForecastSingleRecorded_py

```python
GetEnsembleForecastSingleRecorded_py(efSimulation, variableIdentifier, leadTimeIndex, ensembleIndex, values)
```

GetEnsembleForecastSingleRecorded_py

GetEnsembleForecastSingleRecorded_py: generated wrapper function for API function GetEnsembleForecastSingleRecorded

**Parameters:**

- **efSimulation** (<code>[EnsembleForecastSimulation](#swift2.classes.EnsembleForecastSimulation)</code>) – efSimulation
- **variableIdentifier** (<code>[str](#str)</code>) – variableIdentifier
- **leadTimeIndex** (<code>[int](#int)</code>) – leadTimeIndex
- **ensembleIndex** (<code>[int](#int)</code>) – ensembleIndex
- **values** (<code>[ndarray](#numpy.ndarray)</code>) – values

##### swift2.wrap.swift_wrap_generated.GetFeasibleMuskingumBounds_py

```python
GetFeasibleMuskingumBounds_py(simulation, deltaTHours)
```

GetFeasibleMuskingumBounds_py

GetFeasibleMuskingumBounds_py: generated wrapper function for API function GetFeasibleMuskingumBounds

**Parameters:**

- **simulation** (<code>[Simulation](#swift2.classes.Simulation)</code>) – simulation
- **deltaTHours** (<code>[float](#float)</code>) – deltaTHours

**Returns:**

- <code>[Dict](#typing.Dict)\[[str](#str), [float](#float)\]</code> – returned result

##### swift2.wrap.swift_wrap_generated.GetKnownParameterizationStrategies_py

```python
GetKnownParameterizationStrategies_py()
```

GetKnownParameterizationStrategies_py

GetKnownParameterizationStrategies_py: generated wrapper function for API function GetKnownParameterizationStrategies

##### swift2.wrap.swift_wrap_generated.GetKnownParameterizationTargetSelectorTypes_py

```python
GetKnownParameterizationTargetSelectorTypes_py()
```

GetKnownParameterizationTargetSelectorTypes_py

GetKnownParameterizationTargetSelectorTypes_py: generated wrapper function for API function GetKnownParameterizationTargetSelectorTypes

##### swift2.wrap.swift_wrap_generated.GetKnownParameterizerAggregationStrategies_py

```python
GetKnownParameterizerAggregationStrategies_py()
```

GetKnownParameterizerAggregationStrategies_py

GetKnownParameterizerAggregationStrategies_py: generated wrapper function for API function GetKnownParameterizerAggregationStrategies

##### swift2.wrap.swift_wrap_generated.GetLastStdExceptionMessage_py

```python
GetLastStdExceptionMessage_py()
```

GetLastStdExceptionMessage_py

GetLastStdExceptionMessage_py: generated wrapper function for API function GetLastStdExceptionMessage

Args:

**Returns:**

- <code>[str](#str)</code> – returned result

##### swift2.wrap.swift_wrap_generated.GetLengthSetOfScores_py

```python
GetLengthSetOfScores_py(vectorScores)
```

GetLengthSetOfScores_py

GetLengthSetOfScores_py: generated wrapper function for API function GetLengthSetOfScores

**Parameters:**

- **vectorScores** (<code>[VectorObjectiveScores](#swift2.classes.VectorObjectiveScores)</code>) – vectorScores

**Returns:**

- <code>[int](#int)</code> – returned result

##### swift2.wrap.swift_wrap_generated.GetLinkIdentifier_py

```python
GetLinkIdentifier_py(simulation, index)
```

GetLinkIdentifier_py

GetLinkIdentifier_py: generated wrapper function for API function GetLinkIdentifier

**Parameters:**

- **simulation** (<code>[Simulation](#swift2.classes.Simulation)</code>) – simulation
- **index** (<code>[int](#int)</code>) – index

**Returns:**

- <code>[str](#str)</code> – returned result

##### swift2.wrap.swift_wrap_generated.GetLinkIdentifiers_py

```python
GetLinkIdentifiers_py(simulation)
```

GetLinkIdentifiers_py

GetLinkIdentifiers_py: generated wrapper function for API function GetLinkIdentifiers

##### swift2.wrap.swift_wrap_generated.GetLinkName_py

```python
GetLinkName_py(simulation, index)
```

GetLinkName_py

GetLinkName_py: generated wrapper function for API function GetLinkName

**Parameters:**

- **simulation** (<code>[Simulation](#swift2.classes.Simulation)</code>) – simulation
- **index** (<code>[int](#int)</code>) – index

**Returns:**

- <code>[str](#str)</code> – returned result

##### swift2.wrap.swift_wrap_generated.GetLinkNames_py

```python
GetLinkNames_py(simulation)
```

GetLinkNames_py

GetLinkNames_py: generated wrapper function for API function GetLinkNames

##### swift2.wrap.swift_wrap_generated.GetMAERRISCalibrationLog_py

```python
GetMAERRISCalibrationLog_py(calibObject)
```

GetMAERRISCalibrationLog_py

GetMAERRISCalibrationLog_py: generated wrapper function for API function GetMAERRISCalibrationLog

**Parameters:**

- **calibObject** (<code>[MaerrisStagedCalibration](#swift2.classes.MaerrisStagedCalibration)</code>) – calibObject

**Returns:**

- <code>[DeletableCffiNativeHandle](#refcount.interop.DeletableCffiNativeHandle)</code> – returned result

##### swift2.wrap.swift_wrap_generated.GetMemoryStates_py

```python
GetMemoryStates_py(memoryStates)
```

GetMemoryStates_py

GetMemoryStates_py: generated wrapper function for API function GetMemoryStates

**Parameters:**

- **memoryStates** (<code>[MemoryStates](#swift2.classes.MemoryStates)</code>) – memoryStates

**Returns:**

- <code>[str](#str)</code> – returned result

##### swift2.wrap.swift_wrap_generated.GetModelConfigurationSwift_py

```python
GetModelConfigurationSwift_py(simulation, elementIdentifier)
```

GetModelConfigurationSwift_py

GetModelConfigurationSwift_py: generated wrapper function for API function GetModelConfigurationSwift

**Parameters:**

- **simulation** (<code>[Simulation](#swift2.classes.Simulation)</code>) – simulation
- **elementIdentifier** (<code>[str](#str)</code>) – elementIdentifier

**Returns:**

- <code>[Dict](#typing.Dict)\[[str](#str), [str](#str)\]</code> – returned result

##### swift2.wrap.swift_wrap_generated.GetNameObjectiveEvaluator_py

```python
GetNameObjectiveEvaluator_py(objectiveEvaluator)
```

GetNameObjectiveEvaluator_py

GetNameObjectiveEvaluator_py: generated wrapper function for API function GetNameObjectiveEvaluator

**Parameters:**

- **objectiveEvaluator** (<code>[DeletableCffiNativeHandle](#refcount.interop.DeletableCffiNativeHandle)</code>) – objectiveEvaluator

**Returns:**

- <code>[str](#str)</code> – returned result

##### swift2.wrap.swift_wrap_generated.GetNodeIdentifier_py

```python
GetNodeIdentifier_py(simulation, index)
```

GetNodeIdentifier_py

GetNodeIdentifier_py: generated wrapper function for API function GetNodeIdentifier

**Parameters:**

- **simulation** (<code>[Simulation](#swift2.classes.Simulation)</code>) – simulation
- **index** (<code>[int](#int)</code>) – index

**Returns:**

- <code>[str](#str)</code> – returned result

##### swift2.wrap.swift_wrap_generated.GetNodeIdentifiers_py

```python
GetNodeIdentifiers_py(simulation)
```

GetNodeIdentifiers_py

GetNodeIdentifiers_py: generated wrapper function for API function GetNodeIdentifiers

##### swift2.wrap.swift_wrap_generated.GetNodeName_py

```python
GetNodeName_py(simulation, index)
```

GetNodeName_py

GetNodeName_py: generated wrapper function for API function GetNodeName

**Parameters:**

- **simulation** (<code>[Simulation](#swift2.classes.Simulation)</code>) – simulation
- **index** (<code>[int](#int)</code>) – index

**Returns:**

- <code>[str](#str)</code> – returned result

##### swift2.wrap.swift_wrap_generated.GetNodeNames_py

```python
GetNodeNames_py(simulation)
```

GetNodeNames_py

GetNodeNames_py: generated wrapper function for API function GetNodeNames

##### swift2.wrap.swift_wrap_generated.GetNumCatchments_py

```python
GetNumCatchments_py()
```

GetNumCatchments_py

GetNumCatchments_py: generated wrapper function for API function GetNumCatchments

Args:

**Returns:**

- <code>[int](#int)</code> – returned result

##### swift2.wrap.swift_wrap_generated.GetNumHyperCubesWila_py

```python
GetNumHyperCubesWila_py()
```

GetNumHyperCubesWila_py

GetNumHyperCubesWila_py: generated wrapper function for API function GetNumHyperCubesWila

Args:

**Returns:**

- <code>[int](#int)</code> – returned result

##### swift2.wrap.swift_wrap_generated.GetNumHyperCubes_py

```python
GetNumHyperCubes_py()
```

GetNumHyperCubes_py

GetNumHyperCubes_py: generated wrapper function for API function GetNumHyperCubes

Args:

**Returns:**

- <code>[int](#int)</code> – returned result

##### swift2.wrap.swift_wrap_generated.GetNumLinks_py

```python
GetNumLinks_py(simulation)
```

GetNumLinks_py

GetNumLinks_py: generated wrapper function for API function GetNumLinks

**Parameters:**

- **simulation** (<code>[Simulation](#swift2.classes.Simulation)</code>) – simulation

**Returns:**

- <code>[int](#int)</code> – returned result

##### swift2.wrap.swift_wrap_generated.GetNumMemTestCatchments_py

```python
GetNumMemTestCatchments_py()
```

GetNumMemTestCatchments_py

GetNumMemTestCatchments_py: generated wrapper function for API function GetNumMemTestCatchments

Args:

**Returns:**

- <code>[int](#int)</code> – returned result

##### swift2.wrap.swift_wrap_generated.GetNumMemTestModelRunners_py

```python
GetNumMemTestModelRunners_py()
```

GetNumMemTestModelRunners_py

GetNumMemTestModelRunners_py: generated wrapper function for API function GetNumMemTestModelRunners

Args:

**Returns:**

- <code>[int](#int)</code> – returned result

##### swift2.wrap.swift_wrap_generated.GetNumMemTestParameterizers_py

```python
GetNumMemTestParameterizers_py()
```

GetNumMemTestParameterizers_py

GetNumMemTestParameterizers_py: generated wrapper function for API function GetNumMemTestParameterizers

Args:

**Returns:**

- <code>[int](#int)</code> – returned result

##### swift2.wrap.swift_wrap_generated.GetNumModelRunners_py

```python
GetNumModelRunners_py()
```

GetNumModelRunners_py

GetNumModelRunners_py: generated wrapper function for API function GetNumModelRunners

Args:

**Returns:**

- <code>[int](#int)</code> – returned result

##### swift2.wrap.swift_wrap_generated.GetNumNodes_py

```python
GetNumNodes_py(simulation)
```

GetNumNodes_py

GetNumNodes_py: generated wrapper function for API function GetNumNodes

**Parameters:**

- **simulation** (<code>[Simulation](#swift2.classes.Simulation)</code>) – simulation

**Returns:**

- <code>[int](#int)</code> – returned result

##### swift2.wrap.swift_wrap_generated.GetNumParameters_py

```python
GetNumParameters_py(hypercubeParameterizer)
```

GetNumParameters_py

GetNumParameters_py: generated wrapper function for API function GetNumParameters

**Parameters:**

- **hypercubeParameterizer** (<code>[HypercubeParameteriser](#swift2.classes.HypercubeParameteriser)</code>) – hypercubeParameterizer

**Returns:**

- <code>[int](#int)</code> – returned result

##### swift2.wrap.swift_wrap_generated.GetNumPlayedVariables_py

```python
GetNumPlayedVariables_py(simulation)
```

GetNumPlayedVariables_py

GetNumPlayedVariables_py: generated wrapper function for API function GetNumPlayedVariables

**Parameters:**

- **simulation** (<code>[Simulation](#swift2.classes.Simulation)</code>) – simulation

**Returns:**

- <code>[int](#int)</code> – returned result

##### swift2.wrap.swift_wrap_generated.GetNumRainfallRunoff_py

```python
GetNumRainfallRunoff_py()
```

GetNumRainfallRunoff_py

GetNumRainfallRunoff_py: generated wrapper function for API function GetNumRainfallRunoff

Args:

**Returns:**

- <code>[int](#int)</code> – returned result

##### swift2.wrap.swift_wrap_generated.GetNumRecordedVariables_py

```python
GetNumRecordedVariables_py(simulation)
```

GetNumRecordedVariables_py

GetNumRecordedVariables_py: generated wrapper function for API function GetNumRecordedVariables

**Parameters:**

- **simulation** (<code>[Simulation](#swift2.classes.Simulation)</code>) – simulation

**Returns:**

- <code>[int](#int)</code> – returned result

##### swift2.wrap.swift_wrap_generated.GetNumRunoffModelIdentifiers_py

```python
GetNumRunoffModelIdentifiers_py()
```

GetNumRunoffModelIdentifiers_py

GetNumRunoffModelIdentifiers_py: generated wrapper function for API function GetNumRunoffModelIdentifiers

Args:

**Returns:**

- <code>[int](#int)</code> – returned result

##### swift2.wrap.swift_wrap_generated.GetNumRunoffModelVarIdentifiers_py

```python
GetNumRunoffModelVarIdentifiers_py(modelId)
```

GetNumRunoffModelVarIdentifiers_py

GetNumRunoffModelVarIdentifiers_py: generated wrapper function for API function GetNumRunoffModelVarIdentifiers

**Parameters:**

- **modelId** (<code>[str](#str)</code>) – modelId

**Returns:**

- <code>[int](#int)</code> – returned result

##### swift2.wrap.swift_wrap_generated.GetNumScoresWila_py

```python
GetNumScoresWila_py(scores)
```

GetNumScoresWila_py

GetNumScoresWila_py: generated wrapper function for API function GetNumScoresWila

**Parameters:**

- **scores** (<code>[ObjectiveScores](#swift2.classes.ObjectiveScores)</code>) – scores

**Returns:**

- <code>[int](#int)</code> – returned result

##### swift2.wrap.swift_wrap_generated.GetNumStateInitializers_py

```python
GetNumStateInitializers_py()
```

GetNumStateInitializers_py

GetNumStateInitializers_py: generated wrapper function for API function GetNumStateInitializers

Args:

**Returns:**

- <code>[int](#int)</code> – returned result

##### swift2.wrap.swift_wrap_generated.GetNumStepsForTimeSpan_py

```python
GetNumStepsForTimeSpan_py(modelSimulation, start, end)
```

GetNumStepsForTimeSpan_py

GetNumStepsForTimeSpan_py: generated wrapper function for API function GetNumStepsForTimeSpan

**Parameters:**

- **modelSimulation** (<code>[Simulation](#swift2.classes.Simulation)</code>) – modelSimulation
- **start** (<code>[datetime](#datetime.datetime)</code>) – start
- **end** (<code>[datetime](#datetime.datetime)</code>) – end

**Returns:**

- <code>[int](#int)</code> – returned result

##### swift2.wrap.swift_wrap_generated.GetNumSteps_py

```python
GetNumSteps_py(simulation)
```

GetNumSteps_py

GetNumSteps_py: generated wrapper function for API function GetNumSteps

**Parameters:**

- **simulation** (<code>[Simulation](#swift2.classes.Simulation)</code>) – simulation

**Returns:**

- <code>[int](#int)</code> – returned result

##### swift2.wrap.swift_wrap_generated.GetNumSubareas_py

```python
GetNumSubareas_py(simulation)
```

GetNumSubareas_py

GetNumSubareas_py: generated wrapper function for API function GetNumSubareas

**Parameters:**

- **simulation** (<code>[Simulation](#swift2.classes.Simulation)</code>) – simulation

**Returns:**

- <code>[int](#int)</code> – returned result

##### swift2.wrap.swift_wrap_generated.GetNumVarIdentifiers_py

```python
GetNumVarIdentifiers_py(simulation, elementId)
```

GetNumVarIdentifiers_py

GetNumVarIdentifiers_py: generated wrapper function for API function GetNumVarIdentifiers

**Parameters:**

- **simulation** (<code>[Simulation](#swift2.classes.Simulation)</code>) – simulation
- **elementId** (<code>[str](#str)</code>) – elementId

**Returns:**

- <code>[int](#int)</code> – returned result

##### swift2.wrap.swift_wrap_generated.GetOptimizerLogDataWilaDims_py

```python
GetOptimizerLogDataWilaDims_py(logData, logLength, stringDataCount, numericDataCount)
```

GetOptimizerLogDataWilaDims_py

GetOptimizerLogDataWilaDims_py: generated wrapper function for API function GetOptimizerLogDataWilaDims

**Parameters:**

- **logData** (<code>[DeletableCffiNativeHandle](#refcount.interop.DeletableCffiNativeHandle)</code>) – logData
- **logLength** (<code>[ndarray](#numpy.ndarray)</code>) – logLength
- **stringDataCount** (<code>[ndarray](#numpy.ndarray)</code>) – stringDataCount
- **numericDataCount** (<code>[ndarray](#numpy.ndarray)</code>) – numericDataCount

##### swift2.wrap.swift_wrap_generated.GetOptimizerLogDataWilaNumericDataNames_py

```python
GetOptimizerLogDataWilaNumericDataNames_py(logData, numericDataIndex)
```

GetOptimizerLogDataWilaNumericDataNames_py

GetOptimizerLogDataWilaNumericDataNames_py: generated wrapper function for API function GetOptimizerLogDataWilaNumericDataNames

**Parameters:**

- **logData** (<code>[DeletableCffiNativeHandle](#refcount.interop.DeletableCffiNativeHandle)</code>) – logData
- **numericDataIndex** (<code>[int](#int)</code>) – numericDataIndex

**Returns:**

- <code>[str](#str)</code> – returned result

##### swift2.wrap.swift_wrap_generated.GetOptimizerLogDataWilaNumericData_py

```python
GetOptimizerLogDataWilaNumericData_py(logData, numericDataIndex, data)
```

GetOptimizerLogDataWilaNumericData_py

GetOptimizerLogDataWilaNumericData_py: generated wrapper function for API function GetOptimizerLogDataWilaNumericData

**Parameters:**

- **logData** (<code>[DeletableCffiNativeHandle](#refcount.interop.DeletableCffiNativeHandle)</code>) – logData
- **numericDataIndex** (<code>[int](#int)</code>) – numericDataIndex
- **data** (<code>[ndarray](#numpy.ndarray)</code>) – data

##### swift2.wrap.swift_wrap_generated.GetOptimizerLogDataWilaStringDataNames_py

```python
GetOptimizerLogDataWilaStringDataNames_py(logData, stringDataIndex)
```

GetOptimizerLogDataWilaStringDataNames_py

GetOptimizerLogDataWilaStringDataNames_py: generated wrapper function for API function GetOptimizerLogDataWilaStringDataNames

**Parameters:**

- **logData** (<code>[DeletableCffiNativeHandle](#refcount.interop.DeletableCffiNativeHandle)</code>) – logData
- **stringDataIndex** (<code>[int](#int)</code>) – stringDataIndex

**Returns:**

- <code>[str](#str)</code> – returned result

##### swift2.wrap.swift_wrap_generated.GetOptimizerLogDataWilaStringData_py

```python
GetOptimizerLogDataWilaStringData_py(logData)
```

GetOptimizerLogDataWilaStringData_py

GetOptimizerLogDataWilaStringData_py: generated wrapper function for API function GetOptimizerLogDataWilaStringData

##### swift2.wrap.swift_wrap_generated.GetOptimizerLogDataWila_py

```python
GetOptimizerLogDataWila_py(optimizer)
```

GetOptimizerLogDataWila_py

GetOptimizerLogDataWila_py: generated wrapper function for API function GetOptimizerLogDataWila

**Parameters:**

- **optimizer** (<code>[Optimiser](#swift2.classes.Optimiser)</code>) – optimizer

**Returns:**

- <code>[DeletableCffiNativeHandle](#refcount.interop.DeletableCffiNativeHandle)</code> – returned result

##### swift2.wrap.swift_wrap_generated.GetParameterMaxValue_py

```python
GetParameterMaxValue_py(hypercubeParameterizer, variableName)
```

GetParameterMaxValue_py

GetParameterMaxValue_py: generated wrapper function for API function GetParameterMaxValue

**Parameters:**

- **hypercubeParameterizer** (<code>[HypercubeParameteriser](#swift2.classes.HypercubeParameteriser)</code>) – hypercubeParameterizer
- **variableName** (<code>[str](#str)</code>) – variableName

**Returns:**

- <code>[float](#float)</code> – returned result

##### swift2.wrap.swift_wrap_generated.GetParameterMinValue_py

```python
GetParameterMinValue_py(hypercubeParameterizer, variableName)
```

GetParameterMinValue_py

GetParameterMinValue_py: generated wrapper function for API function GetParameterMinValue

**Parameters:**

- **hypercubeParameterizer** (<code>[HypercubeParameteriser](#swift2.classes.HypercubeParameteriser)</code>) – hypercubeParameterizer
- **variableName** (<code>[str](#str)</code>) – variableName

**Returns:**

- <code>[float](#float)</code> – returned result

##### swift2.wrap.swift_wrap_generated.GetParameterName_py

```python
GetParameterName_py(hypercubeParameterizer, index)
```

GetParameterName_py

GetParameterName_py: generated wrapper function for API function GetParameterName

**Parameters:**

- **hypercubeParameterizer** (<code>[HypercubeParameteriser](#swift2.classes.HypercubeParameteriser)</code>) – hypercubeParameterizer
- **index** (<code>[int](#int)</code>) – index

**Returns:**

- <code>[str](#str)</code> – returned result

##### swift2.wrap.swift_wrap_generated.GetParameterValue_py

```python
GetParameterValue_py(hypercubeParameterizer, variableName)
```

GetParameterValue_py

GetParameterValue_py: generated wrapper function for API function GetParameterValue

**Parameters:**

- **hypercubeParameterizer** (<code>[HypercubeParameteriser](#swift2.classes.HypercubeParameteriser)</code>) – hypercubeParameterizer
- **variableName** (<code>[str](#str)</code>) – variableName

**Returns:**

- <code>[float](#float)</code> – returned result

##### swift2.wrap.swift_wrap_generated.GetPlayedTimeSeriesLength_py

```python
GetPlayedTimeSeriesLength_py(simulation, variableIdentifier)
```

GetPlayedTimeSeriesLength_py

GetPlayedTimeSeriesLength_py: generated wrapper function for API function GetPlayedTimeSeriesLength

**Parameters:**

- **simulation** (<code>[Simulation](#swift2.classes.Simulation)</code>) – simulation
- **variableIdentifier** (<code>[str](#str)</code>) – variableIdentifier

**Returns:**

- <code>[int](#int)</code> – returned result

##### swift2.wrap.swift_wrap_generated.GetPlayedTsGeometry_py

```python
GetPlayedTsGeometry_py(simulation, variableIdentifier, geom)
```

GetPlayedTsGeometry_py

GetPlayedTsGeometry_py: generated wrapper function for API function GetPlayedTsGeometry

**Parameters:**

- **simulation** (<code>[Simulation](#swift2.classes.Simulation)</code>) – simulation
- **variableIdentifier** (<code>[str](#str)</code>) – variableIdentifier
- **geom** (<code>[TimeSeriesGeometryNative](#cinterop.cffi.marshal.TimeSeriesGeometryNative)</code>) – geom

##### swift2.wrap.swift_wrap_generated.GetPlayedVariableName_py

```python
GetPlayedVariableName_py(simulation, index)
```

GetPlayedVariableName_py

GetPlayedVariableName_py: generated wrapper function for API function GetPlayedVariableName

**Parameters:**

- **simulation** (<code>[Simulation](#swift2.classes.Simulation)</code>) – simulation
- **index** (<code>[int](#int)</code>) – index

**Returns:**

- <code>[str](#str)</code> – returned result

##### swift2.wrap.swift_wrap_generated.GetPlayedVariableNames_py

```python
GetPlayedVariableNames_py(simulation)
```

GetPlayedVariableNames_py

GetPlayedVariableNames_py: generated wrapper function for API function GetPlayedVariableNames

##### swift2.wrap.swift_wrap_generated.GetPlayed_py

```python
GetPlayed_py(simulation, variableIdentifier, values, arrayLength)
```

GetPlayed_py

GetPlayed_py: generated wrapper function for API function GetPlayed

**Parameters:**

- **simulation** (<code>[Simulation](#swift2.classes.Simulation)</code>) – simulation
- **variableIdentifier** (<code>[str](#str)</code>) – variableIdentifier
- **values** (<code>[ndarray](#numpy.ndarray)</code>) – values
- **arrayLength** (<code>[int](#int)</code>) – arrayLength

##### swift2.wrap.swift_wrap_generated.GetRecordedEnsembleForecastTimeSeries_py

```python
GetRecordedEnsembleForecastTimeSeries_py(efSimulation, variableIdentifier)
```

GetRecordedEnsembleForecastTimeSeries_py

GetRecordedEnsembleForecastTimeSeries_py: generated wrapper function for API function GetRecordedEnsembleForecastTimeSeries

**Parameters:**

- **efSimulation** (<code>[EnsembleForecastSimulation](#swift2.classes.EnsembleForecastSimulation)</code>) – efSimulation
- **variableIdentifier** (<code>[str](#str)</code>) – variableIdentifier

**Returns:**

- <code>[EnsembleForecastTimeSeries](#uchronia.classes.EnsembleForecastTimeSeries)</code> – returned result

##### swift2.wrap.swift_wrap_generated.GetRecordedTsGeometry_py

```python
GetRecordedTsGeometry_py(simulation, variableIdentifier, geom)
```

GetRecordedTsGeometry_py

GetRecordedTsGeometry_py: generated wrapper function for API function GetRecordedTsGeometry

**Parameters:**

- **simulation** (<code>[Simulation](#swift2.classes.Simulation)</code>) – simulation
- **variableIdentifier** (<code>[str](#str)</code>) – variableIdentifier
- **geom** (<code>[TimeSeriesGeometryNative](#cinterop.cffi.marshal.TimeSeriesGeometryNative)</code>) – geom

##### swift2.wrap.swift_wrap_generated.GetRecordedVariableName_py

```python
GetRecordedVariableName_py(simulation, index)
```

GetRecordedVariableName_py

GetRecordedVariableName_py: generated wrapper function for API function GetRecordedVariableName

**Parameters:**

- **simulation** (<code>[Simulation](#swift2.classes.Simulation)</code>) – simulation
- **index** (<code>[int](#int)</code>) – index

**Returns:**

- <code>[str](#str)</code> – returned result

##### swift2.wrap.swift_wrap_generated.GetRecordedVariableNames_py

```python
GetRecordedVariableNames_py(simulation)
```

GetRecordedVariableNames_py

GetRecordedVariableNames_py: generated wrapper function for API function GetRecordedVariableNames

##### swift2.wrap.swift_wrap_generated.GetRecorded_py

```python
GetRecorded_py(simulation, variableIdentifier, values, arrayLength)
```

GetRecorded_py

GetRecorded_py: generated wrapper function for API function GetRecorded

**Parameters:**

- **simulation** (<code>[Simulation](#swift2.classes.Simulation)</code>) – simulation
- **variableIdentifier** (<code>[str](#str)</code>) – variableIdentifier
- **values** (<code>[ndarray](#numpy.ndarray)</code>) – values
- **arrayLength** (<code>[int](#int)</code>) – arrayLength

##### swift2.wrap.swift_wrap_generated.GetRunoffModelIdentifier_py

```python
GetRunoffModelIdentifier_py(index)
```

GetRunoffModelIdentifier_py

GetRunoffModelIdentifier_py: generated wrapper function for API function GetRunoffModelIdentifier

**Parameters:**

- **index** (<code>[int](#int)</code>) – index

**Returns:**

- <code>[str](#str)</code> – returned result

##### swift2.wrap.swift_wrap_generated.GetRunoffModelIdentifiers_py

```python
GetRunoffModelIdentifiers_py()
```

GetRunoffModelIdentifiers_py

GetRunoffModelIdentifiers_py: generated wrapper function for API function GetRunoffModelIdentifiers

##### swift2.wrap.swift_wrap_generated.GetRunoffModelVarIdentifier_py

```python
GetRunoffModelVarIdentifier_py(modelId, index)
```

GetRunoffModelVarIdentifier_py

GetRunoffModelVarIdentifier_py: generated wrapper function for API function GetRunoffModelVarIdentifier

**Parameters:**

- **modelId** (<code>[str](#str)</code>) – modelId
- **index** (<code>[int](#int)</code>) – index

**Returns:**

- <code>[str](#str)</code> – returned result

##### swift2.wrap.swift_wrap_generated.GetRunoffModelVarIdentifiers_py

```python
GetRunoffModelVarIdentifiers_py(modelId)
```

GetRunoffModelVarIdentifiers_py

GetRunoffModelVarIdentifiers_py: generated wrapper function for API function GetRunoffModelVarIdentifiers

##### swift2.wrap.swift_wrap_generated.GetScoreNameWila_py

```python
GetScoreNameWila_py(scores, index)
```

GetScoreNameWila_py

GetScoreNameWila_py: generated wrapper function for API function GetScoreNameWila

**Parameters:**

- **scores** (<code>[ObjectiveScores](#swift2.classes.ObjectiveScores)</code>) – scores
- **index** (<code>[int](#int)</code>) – index

**Returns:**

- <code>[str](#str)</code> – returned result

##### swift2.wrap.swift_wrap_generated.GetScoreWila_py

```python
GetScoreWila_py(scores, index)
```

GetScoreWila_py

GetScoreWila_py: generated wrapper function for API function GetScoreWila

**Parameters:**

- **scores** (<code>[ObjectiveScores](#swift2.classes.ObjectiveScores)</code>) – scores
- **index** (<code>[int](#int)</code>) – index

**Returns:**

- <code>[float](#float)</code> – returned result

##### swift2.wrap.swift_wrap_generated.GetScoresAtIndex_py

```python
GetScoresAtIndex_py(vectorScores, index)
```

GetScoresAtIndex_py

GetScoresAtIndex_py: generated wrapper function for API function GetScoresAtIndex

**Parameters:**

- **vectorScores** (<code>[VectorObjectiveScores](#swift2.classes.VectorObjectiveScores)</code>) – vectorScores
- **index** (<code>[int](#int)</code>) – index

**Returns:**

- <code>[ObjectiveScores](#swift2.classes.ObjectiveScores)</code> – returned result

##### swift2.wrap.swift_wrap_generated.GetStart_py

```python
GetStart_py(simulation, start)
```

GetStart_py

GetStart_py: generated wrapper function for API function GetStart

**Parameters:**

- **simulation** (<code>[Any](#typing.Any)</code>) – simulation
- **start** (<code>[Any](#typing.Any)</code>) – start

##### swift2.wrap.swift_wrap_generated.GetSubareaIdentifier_py

```python
GetSubareaIdentifier_py(simulation, index)
```

GetSubareaIdentifier_py

GetSubareaIdentifier_py: generated wrapper function for API function GetSubareaIdentifier

**Parameters:**

- **simulation** (<code>[Simulation](#swift2.classes.Simulation)</code>) – simulation
- **index** (<code>[int](#int)</code>) – index

**Returns:**

- <code>[str](#str)</code> – returned result

##### swift2.wrap.swift_wrap_generated.GetSubareaIdentifiers_py

```python
GetSubareaIdentifiers_py(simulation)
```

GetSubareaIdentifiers_py

GetSubareaIdentifiers_py: generated wrapper function for API function GetSubareaIdentifiers

##### swift2.wrap.swift_wrap_generated.GetSubareaName_py

```python
GetSubareaName_py(simulation, index)
```

GetSubareaName_py

GetSubareaName_py: generated wrapper function for API function GetSubareaName

**Parameters:**

- **simulation** (<code>[Simulation](#swift2.classes.Simulation)</code>) – simulation
- **index** (<code>[int](#int)</code>) – index

**Returns:**

- <code>[str](#str)</code> – returned result

##### swift2.wrap.swift_wrap_generated.GetSubareaNames_py

```python
GetSubareaNames_py(simulation)
```

GetSubareaNames_py

GetSubareaNames_py: generated wrapper function for API function GetSubareaNames

##### swift2.wrap.swift_wrap_generated.GetSystemConfigurationWila_py

```python
GetSystemConfigurationWila_py(scores)
```

GetSystemConfigurationWila_py

GetSystemConfigurationWila_py: generated wrapper function for API function GetSystemConfigurationWila

**Parameters:**

- **scores** (<code>[ObjectiveScores](#swift2.classes.ObjectiveScores)</code>) – scores

**Returns:**

- <code>[HypercubeParameteriser](#swift2.classes.HypercubeParameteriser)</code> – returned result

##### swift2.wrap.swift_wrap_generated.GetTimeStepName_py

```python
GetTimeStepName_py(simulation)
```

GetTimeStepName_py

GetTimeStepName_py: generated wrapper function for API function GetTimeStepName

**Parameters:**

- **simulation** (<code>[Any](#typing.Any)</code>) – simulation

**Returns:**

- <code>[str](#str)</code> – returned result

##### swift2.wrap.swift_wrap_generated.GetValueStateInitializer_py

```python
GetValueStateInitializer_py(stateInitializer, identifier)
```

GetValueStateInitializer_py

GetValueStateInitializer_py: generated wrapper function for API function GetValueStateInitializer

**Parameters:**

- **stateInitializer** (<code>[StateInitialiser](#swift2.classes.StateInitialiser)</code>) – stateInitializer
- **identifier** (<code>[str](#str)</code>) – identifier

**Returns:**

- <code>[float](#float)</code> – returned result

##### swift2.wrap.swift_wrap_generated.GetVariableBool_py

```python
GetVariableBool_py(simulation, variableIdentifier)
```

GetVariableBool_py

GetVariableBool_py: generated wrapper function for API function GetVariableBool

**Parameters:**

- **simulation** (<code>[Simulation](#swift2.classes.Simulation)</code>) – simulation
- **variableIdentifier** (<code>[str](#str)</code>) – variableIdentifier

**Returns:**

- <code>[bool](#bool)</code> – returned result

##### swift2.wrap.swift_wrap_generated.GetVariableInt_py

```python
GetVariableInt_py(simulation, variableIdentifier)
```

GetVariableInt_py

GetVariableInt_py: generated wrapper function for API function GetVariableInt

**Parameters:**

- **simulation** (<code>[Simulation](#swift2.classes.Simulation)</code>) – simulation
- **variableIdentifier** (<code>[str](#str)</code>) – variableIdentifier

**Returns:**

- <code>[int](#int)</code> – returned result

##### swift2.wrap.swift_wrap_generated.GetVariable_py

```python
GetVariable_py(simulation, variableIdentifier)
```

GetVariable_py

GetVariable_py: generated wrapper function for API function GetVariable

**Parameters:**

- **simulation** (<code>[Simulation](#swift2.classes.Simulation)</code>) – simulation
- **variableIdentifier** (<code>[str](#str)</code>) – variableIdentifier

**Returns:**

- <code>[float](#float)</code> – returned result

##### swift2.wrap.swift_wrap_generated.HideParameters_py

```python
HideParameters_py(p, pnames, regex, startsWith, strict)
```

HideParameters_py

HideParameters_py: generated wrapper function for API function HideParameters

**Parameters:**

- **p** (<code>[HypercubeParameteriser](#swift2.classes.HypercubeParameteriser)</code>) – p
- **pnames** (<code>[List](#typing.List)</code>) – pnames
- **regex** (<code>[bool](#bool)</code>) – regex
- **startsWith** (<code>[bool](#bool)</code>) – startsWith
- **strict** (<code>[bool](#bool)</code>) – strict

##### swift2.wrap.swift_wrap_generated.HomotheticTransform_py

```python
HomotheticTransform_py(centre, point, factor)
```

HomotheticTransform_py

HomotheticTransform_py: generated wrapper function for API function HomotheticTransform

**Parameters:**

- **centre** (<code>[HypercubeParameteriser](#swift2.classes.HypercubeParameteriser)</code>) – centre
- **point** (<code>[HypercubeParameteriser](#swift2.classes.HypercubeParameteriser)</code>) – point
- **factor** (<code>[float](#float)</code>) – factor

**Returns:**

- <code>[HypercubeParameteriser](#swift2.classes.HypercubeParameteriser)</code> – returned result

##### swift2.wrap.swift_wrap_generated.IsDictionaryStateInitializer_py

```python
IsDictionaryStateInitializer_py(stateInitializer)
```

IsDictionaryStateInitializer_py

IsDictionaryStateInitializer_py: generated wrapper function for API function IsDictionaryStateInitializer

**Parameters:**

- **stateInitializer** (<code>[StateInitialiser](#swift2.classes.StateInitialiser)</code>) – stateInitializer

**Returns:**

- <code>[bool](#bool)</code> – returned result

##### swift2.wrap.swift_wrap_generated.IsValidVariableIdentifier_py

```python
IsValidVariableIdentifier_py(simulation, varId)
```

IsValidVariableIdentifier_py

IsValidVariableIdentifier_py: generated wrapper function for API function IsValidVariableIdentifier

**Parameters:**

- **simulation** (<code>[Simulation](#swift2.classes.Simulation)</code>) – simulation
- **varId** (<code>[str](#str)</code>) – varId

**Returns:**

- <code>[bool](#bool)</code> – returned result

##### swift2.wrap.swift_wrap_generated.IsWithinBounds_py

```python
IsWithinBounds_py(hypercubeParameterizer)
```

IsWithinBounds_py

IsWithinBounds_py: generated wrapper function for API function IsWithinBounds

**Parameters:**

- **hypercubeParameterizer** (<code>[HypercubeParameteriser](#swift2.classes.HypercubeParameteriser)</code>) – hypercubeParameterizer

**Returns:**

- <code>[bool](#bool)</code> – returned result

##### swift2.wrap.swift_wrap_generated.LoadMemoryStatesFromFile_py

```python
LoadMemoryStatesFromFile_py(filePath, format)
```

LoadMemoryStatesFromFile_py

LoadMemoryStatesFromFile_py: generated wrapper function for API function LoadMemoryStatesFromFile

**Parameters:**

- **filePath** (<code>[str](#str)</code>) – filePath
- **format** (<code>[str](#str)</code>) – format

**Returns:**

- <code>[MemoryStates](#swift2.classes.MemoryStates)</code> – returned result

##### swift2.wrap.swift_wrap_generated.LoadModelSimulationFromJson_py

```python
LoadModelSimulationFromJson_py(jsonFilePath)
```

LoadModelSimulationFromJson_py

LoadModelSimulationFromJson_py: generated wrapper function for API function LoadModelSimulationFromJson

**Parameters:**

- **jsonFilePath** (<code>[str](#str)</code>) – jsonFilePath

**Returns:**

- <code>[Simulation](#swift2.classes.Simulation)</code> – returned result

##### swift2.wrap.swift_wrap_generated.LoadParameterizer_py

```python
LoadParameterizer_py(filepath)
```

LoadParameterizer_py

LoadParameterizer_py: generated wrapper function for API function LoadParameterizer

**Parameters:**

- **filepath** (<code>[str](#str)</code>) – filepath

**Returns:**

- <code>[HypercubeParameteriser](#swift2.classes.HypercubeParameteriser)</code> – returned result

##### swift2.wrap.swift_wrap_generated.LoadVersionOneControlFile_py

```python
LoadVersionOneControlFile_py(controlFileName, rootDataDir)
```

LoadVersionOneControlFile_py

LoadVersionOneControlFile_py: generated wrapper function for API function LoadVersionOneControlFile

**Parameters:**

- **controlFileName** (<code>[str](#str)</code>) – controlFileName
- **rootDataDir** (<code>[str](#str)</code>) – rootDataDir

**Returns:**

- <code>[Simulation](#swift2.classes.Simulation)</code> – returned result

##### swift2.wrap.swift_wrap_generated.LoadVersionOneTimeSeriesFile_py

```python
LoadVersionOneTimeSeriesFile_py(fileName)
```

LoadVersionOneTimeSeriesFile_py

LoadVersionOneTimeSeriesFile_py: generated wrapper function for API function LoadVersionOneTimeSeriesFile

**Parameters:**

- **fileName** (<code>[str](#str)</code>) – fileName

**Returns:**

- <code>[TimeSeriesProvider](#uchronia.classes.TimeSeriesProvider)</code> – returned result

##### swift2.wrap.swift_wrap_generated.MemoryStatesFromString_py

```python
MemoryStatesFromString_py(jsonString)
```

MemoryStatesFromString_py

MemoryStatesFromString_py: generated wrapper function for API function MemoryStatesFromString

**Parameters:**

- **jsonString** (<code>[str](#str)</code>) – jsonString

**Returns:**

- <code>[MemoryStates](#swift2.classes.MemoryStates)</code> – returned result

##### swift2.wrap.swift_wrap_generated.ObjectiveEvaluatorIsMaximizable_py

```python
ObjectiveEvaluatorIsMaximizable_py(objectiveEvaluator)
```

ObjectiveEvaluatorIsMaximizable_py

ObjectiveEvaluatorIsMaximizable_py: generated wrapper function for API function ObjectiveEvaluatorIsMaximizable

**Parameters:**

- **objectiveEvaluator** (<code>[DeletableCffiNativeHandle](#refcount.interop.DeletableCffiNativeHandle)</code>) – objectiveEvaluator

**Returns:**

- <code>[bool](#bool)</code> – returned result

##### swift2.wrap.swift_wrap_generated.PlayDatasetEnsembleForecastInput_py

```python
PlayDatasetEnsembleForecastInput_py(efSimulation, dataLibrary, identifiers, dataId, size)
```

PlayDatasetEnsembleForecastInput_py

PlayDatasetEnsembleForecastInput_py: generated wrapper function for API function PlayDatasetEnsembleForecastInput

**Parameters:**

- **efSimulation** (<code>[EnsembleForecastSimulation](#swift2.classes.EnsembleForecastSimulation)</code>) – efSimulation
- **dataLibrary** (<code>[TimeSeriesLibrary](#uchronia.classes.TimeSeriesLibrary)</code>) – dataLibrary
- **identifiers** (<code>[List](#typing.List)\[[str](#str)\]</code>) – identifiers
- **dataId** (<code>[List](#typing.List)\[[str](#str)\]</code>) – dataId
- **size** (<code>[int](#int)</code>) – size

##### swift2.wrap.swift_wrap_generated.PlayDatasetInputs_py

```python
PlayDatasetInputs_py(simulation, dataLibrary, identifiers, dataId, resampleMethod, size)
```

PlayDatasetInputs_py

PlayDatasetInputs_py: generated wrapper function for API function PlayDatasetInputs

**Parameters:**

- **simulation** (<code>[Simulation](#swift2.classes.Simulation)</code>) – simulation
- **dataLibrary** (<code>[TimeSeriesLibrary](#uchronia.classes.TimeSeriesLibrary)</code>) – dataLibrary
- **identifiers** (<code>[List](#typing.List)\[[str](#str)\]</code>) – identifiers
- **dataId** (<code>[List](#typing.List)\[[str](#str)\]</code>) – dataId
- **resampleMethod** (<code>[List](#typing.List)\[[str](#str)\]</code>) – resampleMethod
- **size** (<code>[int](#int)</code>) – size

##### swift2.wrap.swift_wrap_generated.PlayDatasetSingleInput_py

```python
PlayDatasetSingleInput_py(efSimulation, dataLibrary, identifiers, dataId, size)
```

PlayDatasetSingleInput_py

PlayDatasetSingleInput_py: generated wrapper function for API function PlayDatasetSingleInput

**Parameters:**

- **efSimulation** (<code>[EnsembleForecastSimulation](#swift2.classes.EnsembleForecastSimulation)</code>) – efSimulation
- **dataLibrary** (<code>[TimeSeriesLibrary](#uchronia.classes.TimeSeriesLibrary)</code>) – dataLibrary
- **identifiers** (<code>[List](#typing.List)\[[str](#str)\]</code>) – identifiers
- **dataId** (<code>[List](#typing.List)\[[str](#str)\]</code>) – dataId
- **size** (<code>[int](#int)</code>) – size

##### swift2.wrap.swift_wrap_generated.PlayEnsembleForecastTimeSeries_py

```python
PlayEnsembleForecastTimeSeries_py(efSimulation, series, variableIdentifier)
```

PlayEnsembleForecastTimeSeries_py

PlayEnsembleForecastTimeSeries_py: generated wrapper function for API function PlayEnsembleForecastTimeSeries

**Parameters:**

- **efSimulation** (<code>[EnsembleForecastSimulation](#swift2.classes.EnsembleForecastSimulation)</code>) – efSimulation
- **series** (<code>[EnsembleForecastTimeSeries](#uchronia.classes.EnsembleForecastTimeSeries)</code>) – series
- **variableIdentifier** (<code>[str](#str)</code>) – variableIdentifier

##### swift2.wrap.swift_wrap_generated.Play_py

```python
Play_py(simulation, variableIdentifier, values, geom)
```

Play_py

Play_py: generated wrapper function for API function Play

**Parameters:**

- **simulation** (<code>[Simulation](#swift2.classes.Simulation)</code>) – simulation
- **variableIdentifier** (<code>[str](#str)</code>) – variableIdentifier
- **values** (<code>[ndarray](#numpy.ndarray)</code>) – values
- **geom** (<code>[TimeSeriesGeometryNative](#cinterop.cffi.marshal.TimeSeriesGeometryNative)</code>) – geom

##### swift2.wrap.swift_wrap_generated.PrepareDualPassForecasting_py

```python
PrepareDualPassForecasting_py(mr, obsValues, obsGeom, errorModelElementId, warmupStart, warmupEnd, requiredWindowPercentage)
```

PrepareDualPassForecasting_py

PrepareDualPassForecasting_py: generated wrapper function for API function PrepareDualPassForecasting

**Parameters:**

- **mr** (<code>[Simulation](#swift2.classes.Simulation)</code>) – mr
- **obsValues** (<code>[ndarray](#numpy.ndarray)</code>) – obsValues
- **obsGeom** (<code>[TimeSeriesGeometryNative](#cinterop.cffi.marshal.TimeSeriesGeometryNative)</code>) – obsGeom
- **errorModelElementId** (<code>[str](#str)</code>) – errorModelElementId
- **warmupStart** (<code>[datetime](#datetime.datetime)</code>) – warmupStart
- **warmupEnd** (<code>[datetime](#datetime.datetime)</code>) – warmupEnd
- **requiredWindowPercentage** (<code>[float](#float)</code>) – requiredWindowPercentage

**Returns:**

- <code>[EnsembleSimulation](#swift2.classes.EnsembleSimulation)</code> – returned result

##### swift2.wrap.swift_wrap_generated.PrepareERRISForecasting_py

```python
PrepareERRISForecasting_py(mr, obsValues, obsGeom, errorModelElementId, warmupStart, warmupEnd)
```

PrepareERRISForecasting_py

PrepareERRISForecasting_py: generated wrapper function for API function PrepareERRISForecasting

**Parameters:**

- **mr** (<code>[Simulation](#swift2.classes.Simulation)</code>) – mr
- **obsValues** (<code>[ndarray](#numpy.ndarray)</code>) – obsValues
- **obsGeom** (<code>[TimeSeriesGeometryNative](#cinterop.cffi.marshal.TimeSeriesGeometryNative)</code>) – obsGeom
- **errorModelElementId** (<code>[str](#str)</code>) – errorModelElementId
- **warmupStart** (<code>[datetime](#datetime.datetime)</code>) – warmupStart
- **warmupEnd** (<code>[datetime](#datetime.datetime)</code>) – warmupEnd

**Returns:**

- <code>[EnsembleSimulation](#swift2.classes.EnsembleSimulation)</code> – returned result

##### swift2.wrap.swift_wrap_generated.PrepareEnsembleModelRunner_py

```python
PrepareEnsembleModelRunner_py(simulation, warmupStart, warmupEnd, obsTsValues, obsTsGeom, errorModelElementId)
```

PrepareEnsembleModelRunner_py

PrepareEnsembleModelRunner_py: generated wrapper function for API function PrepareEnsembleModelRunner

**Parameters:**

- **simulation** (<code>[Simulation](#swift2.classes.Simulation)</code>) – simulation
- **warmupStart** (<code>[datetime](#datetime.datetime)</code>) – warmupStart
- **warmupEnd** (<code>[datetime](#datetime.datetime)</code>) – warmupEnd
- **obsTsValues** (<code>[ndarray](#numpy.ndarray)</code>) – obsTsValues
- **obsTsGeom** (<code>[TimeSeriesGeometryNative](#cinterop.cffi.marshal.TimeSeriesGeometryNative)</code>) – obsTsGeom
- **errorModelElementId** (<code>[str](#str)</code>) – errorModelElementId

**Returns:**

- <code>[EnsembleSimulation](#swift2.classes.EnsembleSimulation)</code> – returned result

##### swift2.wrap.swift_wrap_generated.RecordEnsembleForecastTimeSeries_py

```python
RecordEnsembleForecastTimeSeries_py(efSimulation, variableIdentifier)
```

RecordEnsembleForecastTimeSeries_py

RecordEnsembleForecastTimeSeries_py: generated wrapper function for API function RecordEnsembleForecastTimeSeries

**Parameters:**

- **efSimulation** (<code>[EnsembleForecastSimulation](#swift2.classes.EnsembleForecastSimulation)</code>) – efSimulation
- **variableIdentifier** (<code>[str](#str)</code>) – variableIdentifier

##### swift2.wrap.swift_wrap_generated.RecordEnsembleForecastToRecorder_py

```python
RecordEnsembleForecastToRecorder_py(efSimulation, variableIdentifiers, dataLibrary, dataIdentifiers, size)
```

RecordEnsembleForecastToRecorder_py

RecordEnsembleForecastToRecorder_py: generated wrapper function for API function RecordEnsembleForecastToRecorder

**Parameters:**

- **efSimulation** (<code>[EnsembleForecastSimulation](#swift2.classes.EnsembleForecastSimulation)</code>) – efSimulation
- **variableIdentifiers** (<code>[List](#typing.List)\[[str](#str)\]</code>) – variableIdentifiers
- **dataLibrary** (<code>[TimeSeriesLibrary](#uchronia.classes.TimeSeriesLibrary)</code>) – dataLibrary
- **dataIdentifiers** (<code>[List](#typing.List)\[[str](#str)\]</code>) – dataIdentifiers
- **size** (<code>[int](#int)</code>) – size

##### swift2.wrap.swift_wrap_generated.RecordEnsembleModelRunner_py

```python
RecordEnsembleModelRunner_py(emr, variableIdentifier)
```

RecordEnsembleModelRunner_py

RecordEnsembleModelRunner_py: generated wrapper function for API function RecordEnsembleModelRunner

**Parameters:**

- **emr** (<code>[EnsembleSimulation](#swift2.classes.EnsembleSimulation)</code>) – emr
- **variableIdentifier** (<code>[str](#str)</code>) – variableIdentifier

##### swift2.wrap.swift_wrap_generated.Record_py

```python
Record_py(simulation, variableIdentifier)
```

Record_py

Record_py: generated wrapper function for API function Record

**Parameters:**

- **simulation** (<code>[Simulation](#swift2.classes.Simulation)</code>) – simulation
- **variableIdentifier** (<code>[str](#str)</code>) – variableIdentifier

##### swift2.wrap.swift_wrap_generated.RegisterAdditionalSwiftDataHandling_py

```python
RegisterAdditionalSwiftDataHandling_py(type)
```

RegisterAdditionalSwiftDataHandling_py

RegisterAdditionalSwiftDataHandling_py: generated wrapper function for API function RegisterAdditionalSwiftDataHandling

**Parameters:**

- **type** (<code>[str](#str)</code>) – type

**Returns:**

- <code>[bool](#bool)</code> – returned result

##### swift2.wrap.swift_wrap_generated.RegisterExceptionCallbackSwift_py

```python
RegisterExceptionCallbackSwift_py(callback)
```

RegisterExceptionCallbackSwift_py

RegisterExceptionCallbackSwift_py: generated wrapper function for API function RegisterExceptionCallbackSwift

**Parameters:**

- **callback** (<code>[Any](#typing.Any)</code>) – callback

##### swift2.wrap.swift_wrap_generated.RegisterExceptionCallback_py

```python
RegisterExceptionCallback_py(callback)
```

RegisterExceptionCallback_py

RegisterExceptionCallback_py: generated wrapper function for API function RegisterExceptionCallback

**Parameters:**

- **callback** (<code>[Any](#typing.Any)</code>) – callback

##### swift2.wrap.swift_wrap_generated.RemoveERRISExclusionPeriod_py

```python
RemoveERRISExclusionPeriod_py(calibObject)
```

RemoveERRISExclusionPeriod_py

RemoveERRISExclusionPeriod_py: generated wrapper function for API function RemoveERRISExclusionPeriod

**Parameters:**

- **calibObject** (<code>[ErrisStagedCalibration](#swift2.classes.ErrisStagedCalibration)</code>) – calibObject

##### swift2.wrap.swift_wrap_generated.RemoveERRISWarmupPeriod_py

```python
RemoveERRISWarmupPeriod_py(calibObject)
```

RemoveERRISWarmupPeriod_py

RemoveERRISWarmupPeriod_py: generated wrapper function for API function RemoveERRISWarmupPeriod

**Parameters:**

- **calibObject** (<code>[ErrisStagedCalibration](#swift2.classes.ErrisStagedCalibration)</code>) – calibObject

##### swift2.wrap.swift_wrap_generated.RemoveMAERRISExclusionPeriod_py

```python
RemoveMAERRISExclusionPeriod_py(calibObject)
```

RemoveMAERRISExclusionPeriod_py

RemoveMAERRISExclusionPeriod_py: generated wrapper function for API function RemoveMAERRISExclusionPeriod

**Parameters:**

- **calibObject** (<code>[MaerrisStagedCalibration](#swift2.classes.MaerrisStagedCalibration)</code>) – calibObject

##### swift2.wrap.swift_wrap_generated.RemoveMAERRISWarmupPeriod_py

```python
RemoveMAERRISWarmupPeriod_py(calibObject)
```

RemoveMAERRISWarmupPeriod_py

RemoveMAERRISWarmupPeriod_py: generated wrapper function for API function RemoveMAERRISWarmupPeriod

**Parameters:**

- **calibObject** (<code>[MaerrisStagedCalibration](#swift2.classes.MaerrisStagedCalibration)</code>) – calibObject

##### swift2.wrap.swift_wrap_generated.RemoveModel_py

```python
RemoveModel_py(simulation, fullModelId)
```

RemoveModel_py

RemoveModel_py: generated wrapper function for API function RemoveModel

**Parameters:**

- **simulation** (<code>[Simulation](#swift2.classes.Simulation)</code>) – simulation
- **fullModelId** (<code>[str](#str)</code>) – fullModelId

##### swift2.wrap.swift_wrap_generated.RemovePlayedTimeSeries_py

```python
RemovePlayedTimeSeries_py(modelInstance, variableIdentifier)
```

RemovePlayedTimeSeries_py

RemovePlayedTimeSeries_py: generated wrapper function for API function RemovePlayedTimeSeries

**Parameters:**

- **modelInstance** (<code>[Simulation](#swift2.classes.Simulation)</code>) – modelInstance
- **variableIdentifier** (<code>[str](#str)</code>) – variableIdentifier

##### swift2.wrap.swift_wrap_generated.RemoveRecorder_py

```python
RemoveRecorder_py(modelInstance, variableIdentifier)
```

RemoveRecorder_py

RemoveRecorder_py: generated wrapper function for API function RemoveRecorder

**Parameters:**

- **modelInstance** (<code>[Simulation](#swift2.classes.Simulation)</code>) – modelInstance
- **variableIdentifier** (<code>[str](#str)</code>) – variableIdentifier

##### swift2.wrap.swift_wrap_generated.RemoveStateInitializerModelRunner_py

```python
RemoveStateInitializerModelRunner_py(modelSimulation)
```

RemoveStateInitializerModelRunner_py

RemoveStateInitializerModelRunner_py: generated wrapper function for API function RemoveStateInitializerModelRunner

**Parameters:**

- **modelSimulation** (<code>[Simulation](#swift2.classes.Simulation)</code>) – modelSimulation

##### swift2.wrap.swift_wrap_generated.RemoveStorageDischargeRelationship_py

```python
RemoveStorageDischargeRelationship_py(simulation, elementId, relationshipType)
```

RemoveStorageDischargeRelationship_py

RemoveStorageDischargeRelationship_py: generated wrapper function for API function RemoveStorageDischargeRelationship

**Parameters:**

- **simulation** (<code>[Simulation](#swift2.classes.Simulation)</code>) – simulation
- **elementId** (<code>[str](#str)</code>) – elementId
- **relationshipType** (<code>[str](#str)</code>) – relationshipType

##### swift2.wrap.swift_wrap_generated.ResetModelStates_py

```python
ResetModelStates_py(simulation)
```

ResetModelStates_py

ResetModelStates_py: generated wrapper function for API function ResetModelStates

**Parameters:**

- **simulation** (<code>[Simulation](#swift2.classes.Simulation)</code>) – simulation

##### swift2.wrap.swift_wrap_generated.SaveMemoryStatesToFile_py

```python
SaveMemoryStatesToFile_py(memoryStates, filePath, format)
```

SaveMemoryStatesToFile_py

SaveMemoryStatesToFile_py: generated wrapper function for API function SaveMemoryStatesToFile

**Parameters:**

- **memoryStates** (<code>[MemoryStates](#swift2.classes.MemoryStates)</code>) – memoryStates
- **filePath** (<code>[str](#str)</code>) – filePath
- **format** (<code>[str](#str)</code>) – format

##### swift2.wrap.swift_wrap_generated.SaveModelSimulationToJson_py

```python
SaveModelSimulationToJson_py(simulation, jsonFilePath)
```

SaveModelSimulationToJson_py

SaveModelSimulationToJson_py: generated wrapper function for API function SaveModelSimulationToJson

**Parameters:**

- **simulation** (<code>[Simulation](#swift2.classes.Simulation)</code>) – simulation
- **jsonFilePath** (<code>[str](#str)</code>) – jsonFilePath

##### swift2.wrap.swift_wrap_generated.SaveParameterizer_py

```python
SaveParameterizer_py(parameterizer, filepath)
```

SaveParameterizer_py

SaveParameterizer_py: generated wrapper function for API function SaveParameterizer

**Parameters:**

- **parameterizer** (<code>[HypercubeParameteriser](#swift2.classes.HypercubeParameteriser)</code>) – parameterizer
- **filepath** (<code>[str](#str)</code>) – filepath

##### swift2.wrap.swift_wrap_generated.SetChannelRoutingModel_py

```python
SetChannelRoutingModel_py(simulation, newModelId)
```

SetChannelRoutingModel_py

SetChannelRoutingModel_py: generated wrapper function for API function SetChannelRoutingModel

**Parameters:**

- **simulation** (<code>[Simulation](#swift2.classes.Simulation)</code>) – simulation
- **newModelId** (<code>[str](#str)</code>) – newModelId

##### swift2.wrap.swift_wrap_generated.SetDefaultMaxThreadsWila_py

```python
SetDefaultMaxThreadsWila_py(nThreads)
```

SetDefaultMaxThreadsWila_py

SetDefaultMaxThreadsWila_py: generated wrapper function for API function SetDefaultMaxThreadsWila

**Parameters:**

- **nThreads** (<code>[int](#int)</code>) – nThreads

##### swift2.wrap.swift_wrap_generated.SetDefaultParameters_py

```python
SetDefaultParameters_py(hypercubeParameterizer, modelId)
```

SetDefaultParameters_py

SetDefaultParameters_py: generated wrapper function for API function SetDefaultParameters

**Parameters:**

- **hypercubeParameterizer** (<code>[HypercubeParameteriser](#swift2.classes.HypercubeParameteriser)</code>) – hypercubeParameterizer
- **modelId** (<code>[str](#str)</code>) – modelId

##### swift2.wrap.swift_wrap_generated.SetERRISCensOptions_py

```python
SetERRISCensOptions_py(calibObject, censOpt)
```

SetERRISCensOptions_py

SetERRISCensOptions_py: generated wrapper function for API function SetERRISCensOptions

**Parameters:**

- **calibObject** (<code>[ErrisStagedCalibration](#swift2.classes.ErrisStagedCalibration)</code>) – calibObject
- **censOpt** (<code>[float](#float)</code>) – censOpt

##### swift2.wrap.swift_wrap_generated.SetERRISErrorCorrectionParameterSpace_py

```python
SetERRISErrorCorrectionParameterSpace_py(calibObject, errisParams)
```

SetERRISErrorCorrectionParameterSpace_py

SetERRISErrorCorrectionParameterSpace_py: generated wrapper function for API function SetERRISErrorCorrectionParameterSpace

**Parameters:**

- **calibObject** (<code>[ErrisStagedCalibration](#swift2.classes.ErrisStagedCalibration)</code>) – calibObject
- **errisParams** (<code>[HypercubeParameteriser](#swift2.classes.HypercubeParameteriser)</code>) – errisParams

##### swift2.wrap.swift_wrap_generated.SetERRISEstimationPeriod_py

```python
SetERRISEstimationPeriod_py(calibObject, estimationStart, estimationEnd)
```

SetERRISEstimationPeriod_py

SetERRISEstimationPeriod_py: generated wrapper function for API function SetERRISEstimationPeriod

**Parameters:**

- **calibObject** (<code>[ErrisStagedCalibration](#swift2.classes.ErrisStagedCalibration)</code>) – calibObject
- **estimationStart** (<code>[datetime](#datetime.datetime)</code>) – estimationStart
- **estimationEnd** (<code>[datetime](#datetime.datetime)</code>) – estimationEnd

##### swift2.wrap.swift_wrap_generated.SetERRISExclusionPeriod_py

```python
SetERRISExclusionPeriod_py(calibObject, exclusionStart, exclusionEnd)
```

SetERRISExclusionPeriod_py

SetERRISExclusionPeriod_py: generated wrapper function for API function SetERRISExclusionPeriod

**Parameters:**

- **calibObject** (<code>[ErrisStagedCalibration](#swift2.classes.ErrisStagedCalibration)</code>) – calibObject
- **exclusionStart** (<code>[datetime](#datetime.datetime)</code>) – exclusionStart
- **exclusionEnd** (<code>[datetime](#datetime.datetime)</code>) – exclusionEnd

##### swift2.wrap.swift_wrap_generated.SetERRISHydrologicParameterSpace_py

```python
SetERRISHydrologicParameterSpace_py(calibObject, hydroParams)
```

SetERRISHydrologicParameterSpace_py

SetERRISHydrologicParameterSpace_py: generated wrapper function for API function SetERRISHydrologicParameterSpace

**Parameters:**

- **calibObject** (<code>[ErrisStagedCalibration](#swift2.classes.ErrisStagedCalibration)</code>) – calibObject
- **hydroParams** (<code>[HypercubeParameteriser](#swift2.classes.HypercubeParameteriser)</code>) – hydroParams

##### swift2.wrap.swift_wrap_generated.SetERRISMaxObservation_py

```python
SetERRISMaxObservation_py(calibObject, maxObs)
```

SetERRISMaxObservation_py

SetERRISMaxObservation_py: generated wrapper function for API function SetERRISMaxObservation

**Parameters:**

- **calibObject** (<code>[ErrisStagedCalibration](#swift2.classes.ErrisStagedCalibration)</code>) – calibObject
- **maxObs** (<code>[float](#float)</code>) – maxObs

##### swift2.wrap.swift_wrap_generated.SetERRISVerboseCalibration_py

```python
SetERRISVerboseCalibration_py(calibObject, verboseCalibrationLog)
```

SetERRISVerboseCalibration_py

SetERRISVerboseCalibration_py: generated wrapper function for API function SetERRISVerboseCalibration

**Parameters:**

- **calibObject** (<code>[ErrisStagedCalibration](#swift2.classes.ErrisStagedCalibration)</code>) – calibObject
- **verboseCalibrationLog** (<code>[bool](#bool)</code>) – verboseCalibrationLog

##### swift2.wrap.swift_wrap_generated.SetERRISWarmupPeriod_py

```python
SetERRISWarmupPeriod_py(calibObject, warmupStart, warmupEnd)
```

SetERRISWarmupPeriod_py

SetERRISWarmupPeriod_py: generated wrapper function for API function SetERRISWarmupPeriod

**Parameters:**

- **calibObject** (<code>[ErrisStagedCalibration](#swift2.classes.ErrisStagedCalibration)</code>) – calibObject
- **warmupStart** (<code>[datetime](#datetime.datetime)</code>) – warmupStart
- **warmupEnd** (<code>[datetime](#datetime.datetime)</code>) – warmupEnd

##### swift2.wrap.swift_wrap_generated.SetErrorCorrectionModel_py

```python
SetErrorCorrectionModel_py(simulation, newModelId, elementId, length, seed)
```

SetErrorCorrectionModel_py

SetErrorCorrectionModel_py: generated wrapper function for API function SetErrorCorrectionModel

**Parameters:**

- **simulation** (<code>[Simulation](#swift2.classes.Simulation)</code>) – simulation
- **newModelId** (<code>[str](#str)</code>) – newModelId
- **elementId** (<code>[str](#str)</code>) – elementId
- **length** (<code>[int](#int)</code>) – length
- **seed** (<code>[int](#int)</code>) – seed

##### swift2.wrap.swift_wrap_generated.SetLogLikelihoodMixtureVariableNames_py

```python
SetLogLikelihoodMixtureVariableNames_py(a, b, m, s1, s2, w, maxobs, ct, censopt)
```

SetLogLikelihoodMixtureVariableNames_py

SetLogLikelihoodMixtureVariableNames_py: generated wrapper function for API function SetLogLikelihoodMixtureVariableNames

**Parameters:**

- **a** (<code>[str](#str)</code>) – a
- **b** (<code>[str](#str)</code>) – b
- **m** (<code>[str](#str)</code>) – m
- **s1** (<code>[str](#str)</code>) – s1
- **s2** (<code>[str](#str)</code>) – s2
- **w** (<code>[str](#str)</code>) – w
- **maxobs** (<code>[str](#str)</code>) – maxobs
- **ct** (<code>[str](#str)</code>) – ct
- **censopt** (<code>[str](#str)</code>) – censopt

##### swift2.wrap.swift_wrap_generated.SetLogLikelihoodVariableNames_py

```python
SetLogLikelihoodVariableNames_py(a, b, m, s, maxobs, ct, censopt)
```

SetLogLikelihoodVariableNames_py

SetLogLikelihoodVariableNames_py: generated wrapper function for API function SetLogLikelihoodVariableNames

**Parameters:**

- **a** (<code>[str](#str)</code>) – a
- **b** (<code>[str](#str)</code>) – b
- **m** (<code>[str](#str)</code>) – m
- **s** (<code>[str](#str)</code>) – s
- **maxobs** (<code>[str](#str)</code>) – maxobs
- **ct** (<code>[str](#str)</code>) – ct
- **censopt** (<code>[str](#str)</code>) – censopt

##### swift2.wrap.swift_wrap_generated.SetLogLikelihoodXVariableNames_py

```python
SetLogLikelihoodXVariableNames_py(a, b, m, s1, s2, w, maxobs, ct, censopt)
```

SetLogLikelihoodXVariableNames_py

SetLogLikelihoodXVariableNames_py: generated wrapper function for API function SetLogLikelihoodXVariableNames

**Parameters:**

- **a** (<code>[str](#str)</code>) – a
- **b** (<code>[str](#str)</code>) – b
- **m** (<code>[str](#str)</code>) – m
- **s1** (<code>[str](#str)</code>) – s1
- **s2** (<code>[str](#str)</code>) – s2
- **w** (<code>[str](#str)</code>) – w
- **maxobs** (<code>[str](#str)</code>) – maxobs
- **ct** (<code>[str](#str)</code>) – ct
- **censopt** (<code>[str](#str)</code>) – censopt

##### swift2.wrap.swift_wrap_generated.SetMAERRISCensOptions_py

```python
SetMAERRISCensOptions_py(calibObject, censOpt)
```

SetMAERRISCensOptions_py

SetMAERRISCensOptions_py: generated wrapper function for API function SetMAERRISCensOptions

**Parameters:**

- **calibObject** (<code>[MaerrisStagedCalibration](#swift2.classes.MaerrisStagedCalibration)</code>) – calibObject
- **censOpt** (<code>[float](#float)</code>) – censOpt

##### swift2.wrap.swift_wrap_generated.SetMAERRISErrorCorrectionParameterSpace_py

```python
SetMAERRISErrorCorrectionParameterSpace_py(calibObject, maerrisParams)
```

SetMAERRISErrorCorrectionParameterSpace_py

SetMAERRISErrorCorrectionParameterSpace_py: generated wrapper function for API function SetMAERRISErrorCorrectionParameterSpace

**Parameters:**

- **calibObject** (<code>[MaerrisStagedCalibration](#swift2.classes.MaerrisStagedCalibration)</code>) – calibObject
- **maerrisParams** (<code>[HypercubeParameteriser](#swift2.classes.HypercubeParameteriser)</code>) – maerrisParams

##### swift2.wrap.swift_wrap_generated.SetMAERRISEstimationPeriod_py

```python
SetMAERRISEstimationPeriod_py(calibObject, estimationStart, estimationEnd)
```

SetMAERRISEstimationPeriod_py

SetMAERRISEstimationPeriod_py: generated wrapper function for API function SetMAERRISEstimationPeriod

**Parameters:**

- **calibObject** (<code>[MaerrisStagedCalibration](#swift2.classes.MaerrisStagedCalibration)</code>) – calibObject
- **estimationStart** (<code>[datetime](#datetime.datetime)</code>) – estimationStart
- **estimationEnd** (<code>[datetime](#datetime.datetime)</code>) – estimationEnd

##### swift2.wrap.swift_wrap_generated.SetMAERRISExclusionPeriod_py

```python
SetMAERRISExclusionPeriod_py(calibObject, exclusionStart, exclusionEnd)
```

SetMAERRISExclusionPeriod_py

SetMAERRISExclusionPeriod_py: generated wrapper function for API function SetMAERRISExclusionPeriod

**Parameters:**

- **calibObject** (<code>[MaerrisStagedCalibration](#swift2.classes.MaerrisStagedCalibration)</code>) – calibObject
- **exclusionStart** (<code>[datetime](#datetime.datetime)</code>) – exclusionStart
- **exclusionEnd** (<code>[datetime](#datetime.datetime)</code>) – exclusionEnd

##### swift2.wrap.swift_wrap_generated.SetMAERRISHydrologicParameterSpace_py

```python
SetMAERRISHydrologicParameterSpace_py(calibObject, hydroParams)
```

SetMAERRISHydrologicParameterSpace_py

SetMAERRISHydrologicParameterSpace_py: generated wrapper function for API function SetMAERRISHydrologicParameterSpace

**Parameters:**

- **calibObject** (<code>[MaerrisStagedCalibration](#swift2.classes.MaerrisStagedCalibration)</code>) – calibObject
- **hydroParams** (<code>[HypercubeParameteriser](#swift2.classes.HypercubeParameteriser)</code>) – hydroParams

##### swift2.wrap.swift_wrap_generated.SetMAERRISMaxObservation_py

```python
SetMAERRISMaxObservation_py(calibObject, maxObs)
```

SetMAERRISMaxObservation_py

SetMAERRISMaxObservation_py: generated wrapper function for API function SetMAERRISMaxObservation

**Parameters:**

- **calibObject** (<code>[MaerrisStagedCalibration](#swift2.classes.MaerrisStagedCalibration)</code>) – calibObject
- **maxObs** (<code>[float](#float)</code>) – maxObs

##### swift2.wrap.swift_wrap_generated.SetMAERRISRestrictionOn_py

```python
SetMAERRISRestrictionOn_py(calibObject, restrictionOn)
```

SetMAERRISRestrictionOn_py

SetMAERRISRestrictionOn_py: generated wrapper function for API function SetMAERRISRestrictionOn

**Parameters:**

- **calibObject** (<code>[MaerrisStagedCalibration](#swift2.classes.MaerrisStagedCalibration)</code>) – calibObject
- **restrictionOn** (<code>[bool](#bool)</code>) – restrictionOn

##### swift2.wrap.swift_wrap_generated.SetMAERRISS2Window_py

```python
SetMAERRISS2Window_py(calibObject, s2Window)
```

SetMAERRISS2Window_py

SetMAERRISS2Window_py: generated wrapper function for API function SetMAERRISS2Window

**Parameters:**

- **calibObject** (<code>[MaerrisStagedCalibration](#swift2.classes.MaerrisStagedCalibration)</code>) – calibObject
- **s2Window** (<code>[float](#float)</code>) – s2Window

##### swift2.wrap.swift_wrap_generated.SetMAERRISVerboseCalibration_py

```python
SetMAERRISVerboseCalibration_py(calibObject, verboseCalibrationLog)
```

SetMAERRISVerboseCalibration_py

SetMAERRISVerboseCalibration_py: generated wrapper function for API function SetMAERRISVerboseCalibration

**Parameters:**

- **calibObject** (<code>[MaerrisStagedCalibration](#swift2.classes.MaerrisStagedCalibration)</code>) – calibObject
- **verboseCalibrationLog** (<code>[bool](#bool)</code>) – verboseCalibrationLog

##### swift2.wrap.swift_wrap_generated.SetMAERRISWarmupPeriod_py

```python
SetMAERRISWarmupPeriod_py(calibObject, warmupStart, warmupEnd)
```

SetMAERRISWarmupPeriod_py

SetMAERRISWarmupPeriod_py: generated wrapper function for API function SetMAERRISWarmupPeriod

**Parameters:**

- **calibObject** (<code>[MaerrisStagedCalibration](#swift2.classes.MaerrisStagedCalibration)</code>) – calibObject
- **warmupStart** (<code>[datetime](#datetime.datetime)</code>) – warmupStart
- **warmupEnd** (<code>[datetime](#datetime.datetime)</code>) – warmupEnd

##### swift2.wrap.swift_wrap_generated.SetMaxParameterValue_py

```python
SetMaxParameterValue_py(hypercubeParameterizer, variableName, value)
```

SetMaxParameterValue_py

SetMaxParameterValue_py: generated wrapper function for API function SetMaxParameterValue

**Parameters:**

- **hypercubeParameterizer** (<code>[HypercubeParameteriser](#swift2.classes.HypercubeParameteriser)</code>) – hypercubeParameterizer
- **variableName** (<code>[str](#str)</code>) – variableName
- **value** (<code>[float](#float)</code>) – value

##### swift2.wrap.swift_wrap_generated.SetMaxThreadsOptimizerWila_py

```python
SetMaxThreadsOptimizerWila_py(optimizer, nThreads)
```

SetMaxThreadsOptimizerWila_py

SetMaxThreadsOptimizerWila_py: generated wrapper function for API function SetMaxThreadsOptimizerWila

**Parameters:**

- **optimizer** (<code>[Optimiser](#swift2.classes.Optimiser)</code>) – optimizer
- **nThreads** (<code>[int](#int)</code>) – nThreads

##### swift2.wrap.swift_wrap_generated.SetMemoryStates_py

```python
SetMemoryStates_py(simulation, memoryStates)
```

SetMemoryStates_py

SetMemoryStates_py: generated wrapper function for API function SetMemoryStates

**Parameters:**

- **simulation** (<code>[Simulation](#swift2.classes.Simulation)</code>) – simulation
- **memoryStates** (<code>[MemoryStates](#swift2.classes.MemoryStates)</code>) – memoryStates

##### swift2.wrap.swift_wrap_generated.SetMinParameterValue_py

```python
SetMinParameterValue_py(hypercubeParameterizer, variableName, value)
```

SetMinParameterValue_py

SetMinParameterValue_py: generated wrapper function for API function SetMinParameterValue

**Parameters:**

- **hypercubeParameterizer** (<code>[HypercubeParameteriser](#swift2.classes.HypercubeParameteriser)</code>) – hypercubeParameterizer
- **variableName** (<code>[str](#str)</code>) – variableName
- **value** (<code>[float](#float)</code>) – value

##### swift2.wrap.swift_wrap_generated.SetOptimizerLoggerWila_py

```python
SetOptimizerLoggerWila_py(optimizer, type)
```

SetOptimizerLoggerWila_py

SetOptimizerLoggerWila_py: generated wrapper function for API function SetOptimizerLoggerWila

**Parameters:**

- **optimizer** (<code>[Optimiser](#swift2.classes.Optimiser)</code>) – optimizer
- **type** (<code>[str](#str)</code>) – type

##### swift2.wrap.swift_wrap_generated.SetParameterDefinition_py

```python
SetParameterDefinition_py(hypercubeParameterizer, variableName, min, max, value)
```

SetParameterDefinition_py

SetParameterDefinition_py: generated wrapper function for API function SetParameterDefinition

**Parameters:**

- **hypercubeParameterizer** (<code>[HypercubeParameteriser](#swift2.classes.HypercubeParameteriser)</code>) – hypercubeParameterizer
- **variableName** (<code>[str](#str)</code>) – variableName
- **min** (<code>[float](#float)</code>) – min
- **max** (<code>[float](#float)</code>) – max
- **value** (<code>[float](#float)</code>) – value

##### swift2.wrap.swift_wrap_generated.SetParameterValue_py

```python
SetParameterValue_py(hypercubeParameterizer, variableName, value)
```

SetParameterValue_py

SetParameterValue_py: generated wrapper function for API function SetParameterValue

**Parameters:**

- **hypercubeParameterizer** (<code>[HypercubeParameteriser](#swift2.classes.HypercubeParameteriser)</code>) – hypercubeParameterizer
- **variableName** (<code>[str](#str)</code>) – variableName
- **value** (<code>[float](#float)</code>) – value

##### swift2.wrap.swift_wrap_generated.SetReservoirGeometry_py

```python
SetReservoirGeometry_py(simulation, elementId, numEntries, level, storage, area)
```

SetReservoirGeometry_py

SetReservoirGeometry_py: generated wrapper function for API function SetReservoirGeometry

**Parameters:**

- **simulation** (<code>[Simulation](#swift2.classes.Simulation)</code>) – simulation
- **elementId** (<code>[str](#str)</code>) – elementId
- **numEntries** (<code>[int](#int)</code>) – numEntries
- **level** (<code>[ndarray](#numpy.ndarray)</code>) – level
- **storage** (<code>[ndarray](#numpy.ndarray)</code>) – storage
- **area** (<code>[ndarray](#numpy.ndarray)</code>) – area

##### swift2.wrap.swift_wrap_generated.SetReservoirMaxDischarge_py

```python
SetReservoirMaxDischarge_py(simulation, elementId, numEntries, level, discharge)
```

SetReservoirMaxDischarge_py

SetReservoirMaxDischarge_py: generated wrapper function for API function SetReservoirMaxDischarge

**Parameters:**

- **simulation** (<code>[Simulation](#swift2.classes.Simulation)</code>) – simulation
- **elementId** (<code>[str](#str)</code>) – elementId
- **numEntries** (<code>[int](#int)</code>) – numEntries
- **level** (<code>[ndarray](#numpy.ndarray)</code>) – level
- **discharge** (<code>[ndarray](#numpy.ndarray)</code>) – discharge

##### swift2.wrap.swift_wrap_generated.SetReservoirMinDischarge_py

```python
SetReservoirMinDischarge_py(simulation, elementId, numEntries, level, discharge)
```

SetReservoirMinDischarge_py

SetReservoirMinDischarge_py: generated wrapper function for API function SetReservoirMinDischarge

**Parameters:**

- **simulation** (<code>[Simulation](#swift2.classes.Simulation)</code>) – simulation
- **elementId** (<code>[str](#str)</code>) – elementId
- **numEntries** (<code>[int](#int)</code>) – numEntries
- **level** (<code>[ndarray](#numpy.ndarray)</code>) – level
- **discharge** (<code>[ndarray](#numpy.ndarray)</code>) – discharge

##### swift2.wrap.swift_wrap_generated.SetReservoirModel_py

```python
SetReservoirModel_py(simulation, newModelId, elementId)
```

SetReservoirModel_py

SetReservoirModel_py: generated wrapper function for API function SetReservoirModel

**Parameters:**

- **simulation** (<code>[Simulation](#swift2.classes.Simulation)</code>) – simulation
- **newModelId** (<code>[str](#str)</code>) – newModelId
- **elementId** (<code>[str](#str)</code>) – elementId

##### swift2.wrap.swift_wrap_generated.SetReservoirOpsReleaseCurve_py

```python
SetReservoirOpsReleaseCurve_py(simulation, elementId, numEntries, level, discharge)
```

SetReservoirOpsReleaseCurve_py

SetReservoirOpsReleaseCurve_py: generated wrapper function for API function SetReservoirOpsReleaseCurve

**Parameters:**

- **simulation** (<code>[Simulation](#swift2.classes.Simulation)</code>) – simulation
- **elementId** (<code>[str](#str)</code>) – elementId
- **numEntries** (<code>[int](#int)</code>) – numEntries
- **level** (<code>[ndarray](#numpy.ndarray)</code>) – level
- **discharge** (<code>[ndarray](#numpy.ndarray)</code>) – discharge

##### swift2.wrap.swift_wrap_generated.SetRunoffPostProcessingModel_py

```python
SetRunoffPostProcessingModel_py(src, newModelId, elementId)
```

SetRunoffPostProcessingModel_py

SetRunoffPostProcessingModel_py: generated wrapper function for API function SetRunoffPostProcessingModel

**Parameters:**

- **src** (<code>[Simulation](#swift2.classes.Simulation)</code>) – src
- **newModelId** (<code>[str](#str)</code>) – newModelId
- **elementId** (<code>[str](#str)</code>) – elementId

##### swift2.wrap.swift_wrap_generated.SetSeedForModel_py

```python
SetSeedForModel_py(simulation, modelObjectIdentifier, seed)
```

SetSeedForModel_py

SetSeedForModel_py: generated wrapper function for API function SetSeedForModel

**Parameters:**

- **simulation** (<code>[Simulation](#swift2.classes.Simulation)</code>) – simulation
- **modelObjectIdentifier** (<code>[str](#str)</code>) – modelObjectIdentifier
- **seed** (<code>[int](#int)</code>) – seed

##### swift2.wrap.swift_wrap_generated.SetSpan_py

```python
SetSpan_py(simulation, start, end)
```

SetSpan_py

SetSpan_py: generated wrapper function for API function SetSpan

**Parameters:**

- **simulation** (<code>[Any](#typing.Any)</code>) – simulation
- **start** (<code>[datetime](#datetime.datetime)</code>) – start
- **end** (<code>[datetime](#datetime.datetime)</code>) – end

##### swift2.wrap.swift_wrap_generated.SetSubareaInputsPreprocessorModel_py

```python
SetSubareaInputsPreprocessorModel_py(simulation, newModelId, subAreaId)
```

SetSubareaInputsPreprocessorModel_py

SetSubareaInputsPreprocessorModel_py: generated wrapper function for API function SetSubareaInputsPreprocessorModel

**Parameters:**

- **simulation** (<code>[Simulation](#swift2.classes.Simulation)</code>) – simulation
- **newModelId** (<code>[str](#str)</code>) – newModelId
- **subAreaId** (<code>[str](#str)</code>) – subAreaId

##### swift2.wrap.swift_wrap_generated.SetTimeStep_py

```python
SetTimeStep_py(simulation, timeStepName)
```

SetTimeStep_py

SetTimeStep_py: generated wrapper function for API function SetTimeStep

**Parameters:**

- **simulation** (<code>[Any](#typing.Any)</code>) – simulation
- **timeStepName** (<code>[str](#str)</code>) – timeStepName

##### swift2.wrap.swift_wrap_generated.SetValueStateInitializer_py

```python
SetValueStateInitializer_py(stateInitializer, identifier, value)
```

SetValueStateInitializer_py

SetValueStateInitializer_py: generated wrapper function for API function SetValueStateInitializer

**Parameters:**

- **stateInitializer** (<code>[StateInitialiser](#swift2.classes.StateInitialiser)</code>) – stateInitializer
- **identifier** (<code>[str](#str)</code>) – identifier
- **value** (<code>[float](#float)</code>) – value

##### swift2.wrap.swift_wrap_generated.SetVariableBool_py

```python
SetVariableBool_py(simulation, variableIdentifier, value)
```

SetVariableBool_py

SetVariableBool_py: generated wrapper function for API function SetVariableBool

**Parameters:**

- **simulation** (<code>[Simulation](#swift2.classes.Simulation)</code>) – simulation
- **variableIdentifier** (<code>[str](#str)</code>) – variableIdentifier
- **value** (<code>[bool](#bool)</code>) – value

##### swift2.wrap.swift_wrap_generated.SetVariableInt_py

```python
SetVariableInt_py(simulation, variableIdentifier, value)
```

SetVariableInt_py

SetVariableInt_py: generated wrapper function for API function SetVariableInt

**Parameters:**

- **simulation** (<code>[Simulation](#swift2.classes.Simulation)</code>) – simulation
- **variableIdentifier** (<code>[str](#str)</code>) – variableIdentifier
- **value** (<code>[int](#int)</code>) – value

##### swift2.wrap.swift_wrap_generated.SetVariable_py

```python
SetVariable_py(simulation, variableIdentifier, value)
```

SetVariable_py

SetVariable_py: generated wrapper function for API function SetVariable

**Parameters:**

- **simulation** (<code>[Simulation](#swift2.classes.Simulation)</code>) – simulation
- **variableIdentifier** (<code>[str](#str)</code>) – variableIdentifier
- **value** (<code>[float](#float)</code>) – value

##### swift2.wrap.swift_wrap_generated.SetupEnsembleModelRunner_py

```python
SetupEnsembleModelRunner_py(emr, forecastStart, ensembleSize, forecastHorizonLength)
```

SetupEnsembleModelRunner_py

SetupEnsembleModelRunner_py: generated wrapper function for API function SetupEnsembleModelRunner

**Parameters:**

- **emr** (<code>[EnsembleSimulation](#swift2.classes.EnsembleSimulation)</code>) – emr
- **forecastStart** (<code>[datetime](#datetime.datetime)</code>) – forecastStart
- **ensembleSize** (<code>[int](#int)</code>) – ensembleSize
- **forecastHorizonLength** (<code>[int](#int)</code>) – forecastHorizonLength

##### swift2.wrap.swift_wrap_generated.ShowParameters_py

```python
ShowParameters_py(p, pnames, regex, startsWith)
```

ShowParameters_py

ShowParameters_py: generated wrapper function for API function ShowParameters

**Parameters:**

- **p** (<code>[HypercubeParameteriser](#swift2.classes.HypercubeParameteriser)</code>) – p
- **pnames** (<code>[List](#typing.List)</code>) – pnames
- **regex** (<code>[bool](#bool)</code>) – regex
- **startsWith** (<code>[bool](#bool)</code>) – startsWith

##### swift2.wrap.swift_wrap_generated.SnapshotMemoryStates_py

```python
SnapshotMemoryStates_py(simulation)
```

SnapshotMemoryStates_py

SnapshotMemoryStates_py: generated wrapper function for API function SnapshotMemoryStates

**Parameters:**

- **simulation** (<code>[Simulation](#swift2.classes.Simulation)</code>) – simulation

**Returns:**

- <code>[MemoryStates](#swift2.classes.MemoryStates)</code> – returned result

##### swift2.wrap.swift_wrap_generated.SortSetOfScoresBy_py

```python
SortSetOfScoresBy_py(vectorScores, scoreName)
```

SortSetOfScoresBy_py

SortSetOfScoresBy_py: generated wrapper function for API function SortSetOfScoresBy

**Parameters:**

- **vectorScores** (<code>[VectorObjectiveScores](#swift2.classes.VectorObjectiveScores)</code>) – vectorScores
- **scoreName** (<code>[str](#str)</code>) – scoreName

**Returns:**

- <code>[VectorObjectiveScores](#swift2.classes.VectorObjectiveScores)</code> – returned result

##### swift2.wrap.swift_wrap_generated.SortSimulationElementsByRunOrder_py

```python
SortSimulationElementsByRunOrder_py(simulation, elementIds, numElements, orderingMethod)
```

SortSimulationElementsByRunOrder_py

SortSimulationElementsByRunOrder_py: generated wrapper function for API function SortSimulationElementsByRunOrder

##### swift2.wrap.swift_wrap_generated.SubsetModel_py

```python
SubsetModel_py(simulation, elementName, selectNetworkAboveElement, includeElementInSelection, invertSelection, terminationElements, terminationElementsLength)
```

SubsetModel_py

SubsetModel_py: generated wrapper function for API function SubsetModel

**Parameters:**

- **simulation** (<code>[Simulation](#swift2.classes.Simulation)</code>) – simulation
- **elementName** (<code>[str](#str)</code>) – elementName
- **selectNetworkAboveElement** (<code>[bool](#bool)</code>) – selectNetworkAboveElement
- **includeElementInSelection** (<code>[bool](#bool)</code>) – includeElementInSelection
- **invertSelection** (<code>[bool](#bool)</code>) – invertSelection
- **terminationElements** (<code>[List](#typing.List)\[[str](#str)\]</code>) – terminationElements
- **terminationElementsLength** (<code>[int](#int)</code>) – terminationElementsLength

**Returns:**

- <code>[Simulation](#swift2.classes.Simulation)</code> – returned result

##### swift2.wrap.swift_wrap_generated.SupportsThreadSafeCloning_py

```python
SupportsThreadSafeCloning_py(parameterizer)
```

SupportsThreadSafeCloning_py

SupportsThreadSafeCloning_py: generated wrapper function for API function SupportsThreadSafeCloning

**Parameters:**

- **parameterizer** (<code>[Any](#typing.Any)</code>) – parameterizer

**Returns:**

- <code>[bool](#bool)</code> – returned result

##### swift2.wrap.swift_wrap_generated.SwapRunoffModel_py

```python
SwapRunoffModel_py(simulation, newModelId)
```

SwapRunoffModel_py

SwapRunoffModel_py: generated wrapper function for API function SwapRunoffModel

**Parameters:**

- **simulation** (<code>[Simulation](#swift2.classes.Simulation)</code>) – simulation
- **newModelId** (<code>[str](#str)</code>) – newModelId

**Returns:**

- <code>[Simulation](#swift2.classes.Simulation)</code> – returned result

##### swift2.wrap.swift_wrap_generated.TagParameterizer_py

```python
TagParameterizer_py(p, tag)
```

TagParameterizer_py

TagParameterizer_py: generated wrapper function for API function TagParameterizer

**Parameters:**

- **p** (<code>[HypercubeParameteriser](#swift2.classes.HypercubeParameteriser)</code>) – p
- **tag** (<code>[str](#str)</code>) – tag

##### swift2.wrap.swift_wrap_generated.UntransformHypercubeParameterizer_py

```python
UntransformHypercubeParameterizer_py(hypercubeParameterizer)
```

UntransformHypercubeParameterizer_py

UntransformHypercubeParameterizer_py: generated wrapper function for API function UntransformHypercubeParameterizer

**Parameters:**

- **hypercubeParameterizer** (<code>[HypercubeParameteriser](#swift2.classes.HypercubeParameteriser)</code>) – hypercubeParameterizer

**Returns:**

- <code>[HypercubeParameteriser](#swift2.classes.HypercubeParameteriser)</code> – returned result

##### swift2.wrap.swift_wrap_generated.UnwrapObjectiveEvaluatorWila_py

```python
UnwrapObjectiveEvaluatorWila_py(objective)
```

UnwrapObjectiveEvaluatorWila_py

UnwrapObjectiveEvaluatorWila_py: generated wrapper function for API function UnwrapObjectiveEvaluatorWila

**Parameters:**

- **objective** (<code>[ObjectiveEvaluator](#swift2.classes.ObjectiveEvaluator)</code>) – objective

**Returns:**

- <code>[DeletableCffiNativeHandle](#refcount.interop.DeletableCffiNativeHandle)</code> – returned result

##### swift2.wrap.swift_wrap_generated.UseStateInitializerModelRunner_py

```python
UseStateInitializerModelRunner_py(simulation, stateInitializer)
```

UseStateInitializerModelRunner_py

UseStateInitializerModelRunner_py: generated wrapper function for API function UseStateInitializerModelRunner

**Parameters:**

- **simulation** (<code>[Simulation](#swift2.classes.Simulation)</code>) – simulation
- **stateInitializer** (<code>[StateInitialiser](#swift2.classes.StateInitialiser)</code>) – stateInitializer

##### swift2.wrap.swift_wrap_generated.VariableIsBool_py

```python
VariableIsBool_py(simulation, variableIdentifier)
```

VariableIsBool_py

VariableIsBool_py: generated wrapper function for API function VariableIsBool

**Parameters:**

- **simulation** (<code>[Simulation](#swift2.classes.Simulation)</code>) – simulation
- **variableIdentifier** (<code>[str](#str)</code>) – variableIdentifier

**Returns:**

- <code>[bool](#bool)</code> – returned result

##### swift2.wrap.swift_wrap_generated.VariableIsDouble_py

```python
VariableIsDouble_py(simulation, variableIdentifier)
```

VariableIsDouble_py

VariableIsDouble_py: generated wrapper function for API function VariableIsDouble

**Parameters:**

- **simulation** (<code>[Simulation](#swift2.classes.Simulation)</code>) – simulation
- **variableIdentifier** (<code>[str](#str)</code>) – variableIdentifier

**Returns:**

- <code>[bool](#bool)</code> – returned result

##### swift2.wrap.swift_wrap_generated.VariableIsInt_py

```python
VariableIsInt_py(simulation, variableIdentifier)
```

VariableIsInt_py

VariableIsInt_py: generated wrapper function for API function VariableIsInt

**Parameters:**

- **simulation** (<code>[Simulation](#swift2.classes.Simulation)</code>) – simulation
- **variableIdentifier** (<code>[str](#str)</code>) – variableIdentifier

**Returns:**

- <code>[bool](#bool)</code> – returned result

##### swift2.wrap.swift_wrap_generated.WireSubareaInputsPreprocessorModel_py

```python
WireSubareaInputsPreprocessorModel_py(simulation, fromOutput, toInput, subAreaId)
```

WireSubareaInputsPreprocessorModel_py

WireSubareaInputsPreprocessorModel_py: generated wrapper function for API function WireSubareaInputsPreprocessorModel

**Parameters:**

- **simulation** (<code>[Simulation](#swift2.classes.Simulation)</code>) – simulation
- **fromOutput** (<code>[str](#str)</code>) – fromOutput
- **toInput** (<code>[str](#str)</code>) – toInput
- **subAreaId** (<code>[str](#str)</code>) – subAreaId

##### swift2.wrap.swift_wrap_generated.WrapObjectiveEvaluatorWila_py

```python
WrapObjectiveEvaluatorWila_py(objective, clone)
```

WrapObjectiveEvaluatorWila_py

WrapObjectiveEvaluatorWila_py: generated wrapper function for API function WrapObjectiveEvaluatorWila

**Parameters:**

- **objective** (<code>[DeletableCffiNativeHandle](#refcount.interop.DeletableCffiNativeHandle)</code>) – objective
- **clone** (<code>[bool](#bool)</code>) – clone

**Returns:**

- <code>[ObjectiveEvaluator](#swift2.classes.ObjectiveEvaluator)</code> – returned result

##### swift2.wrap.swift_wrap_generated.char_array_to_py

```python
char_array_to_py(values, dispose=True)
```

##### swift2.wrap.swift_wrap_generated.charp_array_to_py

```python
charp_array_to_py(values, size, dispose=True)
```

##### swift2.wrap.swift_wrap_generated.custom_wrap_cffi_native_handle

```python
custom_wrap_cffi_native_handle(obj, type_id='', release_native=None)
```

Create a wrapper around a cffi pointer (if this is one),
with the suitable native release function call specific to this external pointer.

##### swift2.wrap.swift_wrap_generated.dispose_shared_pointer_py

```python
dispose_shared_pointer_py(ptr)
```

##### swift2.wrap.swift_wrap_generated.named_values_to_py

```python
named_values_to_py(values, dispose=True)
```

##### swift2.wrap.swift_wrap_generated.opaque_ts_as_xarray_time_series

```python
opaque_ts_as_xarray_time_series(ptr, dispose=True)
```

##### swift2.wrap.swift_wrap_generated.py_time_series_dimensions_description

```python
py_time_series_dimensions_description(ptr, dispose=True)
```

##### swift2.wrap.swift_wrap_generated.set_wrap_cffi_native_handle

```python
set_wrap_cffi_native_handle(wrapper_function)
```

##### swift2.wrap.swift_wrap_generated.toSceParametersNative

```python
toSceParametersNative(x)
```
