# Module doc_helper

# doc_helper

Modules:

- **`swc`** –
- **`swg`** –

Functions:

- **`add_loglikelihood_params`** –
- **`add_mln_and_loglik`** –
- **`check_simulation`** – Checks whether a simulation is configured to a state where it is executable
- **`configure_daily_gr4j`** – Configure a simulation with GR4J models for daily time step modelling
- **`configure_hourly_gr4j`** – Configure a simulation with GR4J models for hourly time step modelling
- **`configure_test_simulation`** –
- **`create_catchment`** – Create a SWIFT catchment with a specified hydrologic model
- **`create_catchment_model_from_structure`** –
- **`create_ensemble_forecast_simulation`** – Create an ensemble forecast simulation
- **`create_gr4jh_parameters`** – Get a parameter set that configures GR4J for hourly or daily operations
- **`create_subarea`** – Create a SWIFT subarea with a specified hydrologic model
- **`create_subarea_simulation`** – Creates a one sub-catchment simulation
- **`create_test_catchment_structure`** –
- **`default_pspec_nlm`** –
- **`define_gr4j_scaled_parameter`** – define a scaled and transformed parameterizer for GR4J
- **`define_parameteriser_gr4j_muskingum`** –
- **`describe`** –
- **`deserialise_sample_series`** –
- **`exec_simulation`** – Execute a simulation
- **`get_catchment_dot_graph`** – Gets a catchment representation in Graphviz DOT format
- **`get_free_params`** – Get a default parameter set for models
- **`get_link_ids`** – Gets all the identifiers of the links in the catchment
- **`get_link_names`** – Gets all the names of the links in the catchment
- **`get_node_ids`** – Gets all the identifiers of the nodes in the catchment
- **`get_node_names`** – Gets all the names of the nodes in the catchment
- **`get_state_value`** – Gets the value(s) of a model state(s)
- **`get_state_value_bool`** –
- **`get_state_value_int`** –
- **`get_subarea_ids`** – Gets all the identifiers of the sub-areas in the catchment
- **`get_subarea_names`** – Gets all the names of the sub-areas in the catchment
- **`get_variable_ids`** – Gets all the names of the variables of an element within a catchment
- **`gr4j_scaled_parameteriser`** – Get a time step and area scaled parameterizer for the GR4 model structure
- **`inspect`** – Inspect an element of a catchment model
- **`is_common_iterable`** – True if an object is iterable but not a string (str)
- **`is_variable_id`** – Is a variable identifier valid for a simulation
- **`lag_and_route_parameteriser`** –
- **`paste0`** – Port of R paste0 function
- **`pkg_versions_info`** –
- **`play_subarea_input`** – Sets time series as input to a simulation
- **`rep`** –
- **`reset_model_states`** – Reset the model states of a simulation, and apply one or more state initialers if the simulation is configured with any.
- **`sample_catchment_model`** – Deserialize a basic catchment structure from the package sample data
- **`sample_series`** – Deserialize information to a UTC time series
- **`sce_parameter`** – Create SCE parameters suited for a given number of parameters.
- **`set_error_correction_model`** – Add an error correction model to an element in a catchment
- **`set_loglik_param_keys`** – Specify the global parameter names to use in the log-likelihood calculation
- **`set_muskingum_routing_to_linear`** –
- **`set_sample_data`** – Sets sample input data into a model simulation
- **`set_simulation_span`** – Sets simulation span
- **`set_simulation_time_step`** – Sets the time step of a SWIFT simulation
- **`set_state_value`** – Sets the value(s) of one or more model state variables.
- **`set_state_value_bool`** –
- **`set_state_value_int`** –
- **`set_states`** – Apply memory states to a simulation
- **`short_var_id`** – Shorten long model variable identifiers to the short model variable name
- **`snapshot_state`** – Take a snapshot of the memory states of a simulation
- **`sort_by_execution_order`** – Sort the specified element ids according to the execution order of the simulation
- **`swap_model`** – Clone and change a simulation, using another runoff model
- **`testdata_dir`** –

## add_loglikelihood_params

```
add_loglikelihood_params(parameteriser)
```

## add_mln_and_loglik

```
add_mln_and_loglik(parameteriser, simulation, p_spec_nlm, delta_t, param_name_k='Alpha', objfun=None)
```

## check_simulation

```
check_simulation(simulation) -> Dict
```

Checks whether a simulation is configured to a state where it is executable

Checks whether a simulation is configured to a state where it is executable

Parameters:

- **`simulation`** (`Simulation`) – A swift simulation object

## configure_daily_gr4j

```
configure_daily_gr4j(simulation)
```

Configure a simulation with GR4J models for daily time step modelling

Configure a simulation with GR4J models for daily time step modelling

Parameters:

- **`simulation`** (`Simulation`) – A swift simulation object

## configure_hourly_gr4j

```
configure_hourly_gr4j(simulation)
```

Configure a simulation with GR4J models for hourly time step modelling

Configure a simulation with GR4J models for hourly time step modelling

Parameters:

- **`simulation`** (`Simulation`) – A swift simulation object

## configure_test_simulation

```
configure_test_simulation(simulation: Simulation, data_id='MMH', simul_start='1990-01-01', simul_end='2005-12-31', tstep='daily', varname_rain='P', varname_pet='E', varname_data_rain='P', varname_data_pet='E')
```

## create_catchment

```
create_catchment(node_ids: List, node_names: List, link_ids: List, link_names: List, link_from_node: List, link_to_node: List, runoff_model_name: str = 'GR4J', areas_km2: List[float] = None) -> Simulation
```

Create a SWIFT catchment with a specified hydrologic model

Create a SWIFT catchment with a specified hydrologic model. This function is intended mostly for testing, not for usual modelling code.

Parameters:

- **`node_ids`** (`Any`) – character, node unique identifiers
- **`node_names`** (`Any`) – character, node display names
- **`link_ids`** (`Any`) – character, links unique identifiers
- **`link_names`** (`Any`) – character, links display names
- **`link_from_node`** (`Any`) – character, identifier of the links' upstream node
- **`link_to_node`** (`Any`) – character, identifier of the links' downstream node
- **`runoff_model_name`** (`Any`, default: `'GR4J'` ) – A valid, known SWIFT model name (e.g. 'GR5H')
- **`areas_km2`** (`Any`, default: `None` ) – The areas in square kilometres

Returns:

- **`Simulation`** ( `Simulation` ) – A SWIFT simulation object (i.e. a model runner)

Examples:

TODO

## create_catchment_model_from_structure

```
create_catchment_model_from_structure(cat_structure: Dict[str, List])
```

## create_ensemble_forecast_simulation

```
create_ensemble_forecast_simulation(simulation: Simulation, data_library: Any, start: ConvertibleToTimestamp, end: ConvertibleToTimestamp, input_map: Dict[str, List[str]], lead_time: int, ensemble_size: int, n_time_steps_between_forecasts: int = 1) -> EnsembleForecastSimulation
```

Create an ensemble forecast simulation

Create an ensemble forecast simulation

Parameters:

- **`simulation`** (`Simulation`) – A swift simulation object
- **`data_library`** (`Any`) – external pointer type ENSEMBLE_DATA_SET_PTR, or a Python class wrapper around it
- **`start`** (`Any`) – the start date of the simulation. Time zone aware timestamps are not supported..
- **`end`** (`Any`) – the end date of the simulation. Time zone aware timestamps are not supported..
- **`input_map`** (`Any`) – a named list were names are the data library data identifiers, and values are character vectors with model state identifiers.
- **`lead_time`** (`Any`) – integer, the length in time steps of the forecasts.
- **`ensemble_size`** (`Any`) – ensemble size
- **`n_time_steps_between_forecasts`** (`Any`, default: `1` ) – nTimeStepsBetweenForecasts

Returns:

- **`EnsembleForecastSimulation`** ( `EnsembleForecastSimulation` ) – A SWIFT ensemble forecast simulation object

## create_gr4jh_parameters

```
create_gr4jh_parameters(hourly: bool = True) -> HypercubeParameteriser
```

Get a parameter set that configures GR4J for hourly or daily operations

Derived from the initial Fortran implementation in SWIFTv1 * UHExponent = 2.5 is the default value for daily time step. Set to 1.25 for hourly time step * PercFactor = 9.0 / 4.0 for daily, 4.0 for hourly time step.

Returns:

- **`HypercubeParameteriser`** ( `HypercubeParameteriser` ) – a parameter set that can be applied to SWIFT systems with GR4J

## create_subarea

```
create_subarea(model_name: str, area_km2: float) -> Simulation
```

Create a SWIFT subarea with a specified hydrologic model

Create a SWIFT subarea with a specified hydrologic model

Parameters:

- **`model_name`** (`str`) – A valid, known SWIFT model name (e.g. 'GR5H')
- **`area_km2`** (`float`) – The area in square kilometres

Returns:

- **`Simulation`** ( `Simulation` ) – A SWIFT simulation object (i.e. a model runner)

## create_subarea_simulation

```
create_subarea_simulation(data_id: str = 'MMH', simul_start: str = '1990-01-01', simul_end: str = '2005-12-31', model_id: str = 'GR4J', tstep: str = 'daily', varname_rain: str = 'P', varname_pet: str = 'E', data_rain_id: str = 'rain', data_evap_id: str = 'evap') -> Simulation
```

Creates a one sub-catchment simulation

Creates a one sub-catchment simulation. This function is intended for creating sample simulations, not for use in production.

Parameters:

- **`data_id`** (`str`, default: `'MMH'` ) – data identifier in swift_sample_data
- **`simul_start`** (`str`, default: `'1990-01-01'` ) – ISO string for the simulation start date time
- **`simul_end`** (`str`, default: `'2005-12-31'` ) – ISO string for the simulation end date time
- **`model_id`** (`str`, default: `'GR4J'` ) – model identifier
- **`tstep`** (`str`, default: `'daily'` ) – character, 'daily' or 'hourly'
- **`varname_rain`** (`str`, default: `'P'` ) – variable name to assign rainfall to
- **`varname_pet`** (`str`, default: `'E'` ) – variable name to assign PET to
- **`data_rain_id`** (`str`, default: `'rain'` ) – key to use to retrieve the rainfall series from the sample data
- **`data_evap_id`** (`str`, default: `'evap'` ) – key to use to retrieve the evaporation series from the sample data

Returns:

- **`Simulation`** ( `Simulation` ) – A SWIFT simulation object (i.e. a model runner)

## create_test_catchment_structure

```
create_test_catchment_structure(node_ids=None, link_ids=None, from_node=None, to_node=None, areas_km2=None, runoff_model='GR4J')
```

## default_pspec_nlm

```
default_pspec_nlm()
```

## define_gr4j_scaled_parameter

```
define_gr4j_scaled_parameter(ref_area: float = 250, time_span: int = 3600, pspec_gr4j: Optional[DataFrame] = None) -> TransformParameteriser
```

define a scaled and transformed parameterizer for GR4J

define a scaled and transformed parameterizer for GR4J

Parameters:

- **`ref_area`** (`float`, default: `250` ) – the reference area in square kilometres
- **`time_span`** (`int`, default: `3600` ) – the time span of the simulation intented for this model, in seconds
- **`pspec_gr4j`** (`DataFrame`, default: `None` ) – optional - data frame specifying the feasible parameter space for parameters x1 to x2 of GR4J

Returns:

- **`TransformParameteriser`** ( `TransformParameteriser` ) – a parameterizer for GR4J, combining time and area scaling and superimposed with log10 transforms for x1, x3, x4 and arc-sinh for x2

## define_parameteriser_gr4j_muskingum

```
define_parameteriser_gr4j_muskingum(ref_area=250, time_span=3600, p_spec_nlm=None, simulation=None, objfun=None, delta_t=1, param_name_k='K')
```

## describe

```
describe(simulation: Simulation, verbosity: Any = None) -> Dict
```

## deserialise_sample_series

```
deserialise_sample_series(serialised: Dict[str, Iterable])
```

## exec_simulation

```
exec_simulation(simulation: Simulation, reset_initial_states=True)
```

Execute a simulation

Execute a simulation

Parameters:

- **`simulation`** (`Simulation`) – A swift simulation object
- **`reset_initial_states`** (`Any`, default: `True` ) – logical, should the states of the model be reinitialized before the first time step.

## get_catchment_dot_graph

```
get_catchment_dot_graph(simulation: Simulation) -> str
```

Gets a catchment representation in Graphviz DOT format

Gets a catchment representation in Graphviz DOT format

Parameters:

- **`simulation`** (`Simulation`) – A swift simulation object

Returns:

- `str` – a string in a notation usable by the DiagrammeR package.

Examples:

TODO

## get_free_params

```
get_free_params(model_id: str) -> DataFrame
```

Get a default parameter set for models

Get a default parameter set for models, as a data frame

Parameters:

- **`model_id`** (`Any`) – an identifier for the model, e.g. 'GR5H'

Returns:

- `DataFrame` – a data frame with Min, Max, Value, Name

## get_link_ids

```
get_link_ids(simulation: Simulation) -> List[str]
```

Gets all the identifiers of the links in the catchment

Gets all the identifiers of the links in the catchment

Parameters:

- **`simulation`** (`Simulation`) – A swift simulation object

Returns:

- `List[str]` – The identifiers of the links in the catchment

## get_link_names

```
get_link_names(simulation)
```

Gets all the names of the links in the catchment

Gets all the names of the links in the catchment

Parameters:

- **`simulation`** (`Simulation`) – A swift simulation object

Returns:

- – The names of the links in the catchment

## get_node_ids

```
get_node_ids(simulation: Simulation) -> List[str]
```

Gets all the identifiers of the nodes in the catchment

Gets all the identifiers of the nodes in the catchment

Parameters:

- **`simulation`** (`Simulation`) – A swift simulation object

Returns:

- `List[str]` – The identifiers of the nodes in the catchment

## get_node_names

```
get_node_names(simulation)
```

Gets all the names of the nodes in the catchment

Gets all the names of the nodes in the catchment

Parameters:

- **`simulation`** (`Simulation`) – A swift simulation object

Returns:

- – The names of the nodes in the catchment

## get_state_value

```
get_state_value(simulation: Simulation, var_id: VecStr) -> Union[float, Dict[str, float]]
```

Gets the value(s) of a model state(s)

Parameters:

- **`simulation`** (`Simulation`) – A swift simulation object
- **`var_id`** (`VecStr`) – string or sequence of str, model variable state identifier(s)

Returns:

- `Union[float, Dict[str, float]]` – numeric vector, value(s) of the requested model states

## get_state_value_bool

```
get_state_value_bool(simulation: Simulation, var_id: str) -> bool
```

## get_state_value_int

```
get_state_value_int(simulation: Simulation, var_id: str) -> int
```

## get_subarea_ids

```
get_subarea_ids(simulation: Simulation) -> List[str]
```

Gets all the identifiers of the sub-areas in the catchment

Gets all the identifiers of the sub-areas in the catchment

Parameters:

- **`simulation`** (`Simulation`) – A swift simulation object

Returns:

- `List[str]` – The identifiers of the sub-areas in the catchment

## get_subarea_names

```
get_subarea_names(simulation)
```

Gets all the names of the sub-areas in the catchment

Gets all the names of the sub-areas in the catchment

Parameters:

- **`simulation`** (`Simulation`) – A swift simulation object

Returns:

- – The names of the sub-areas in the catchment

## get_variable_ids

```
get_variable_ids(simulation: Simulation, element_id: str = None, full_id: bool = True) -> List[str]
```

Gets all the names of the variables of an element within a catchment

Gets all the names of the variables of an element (link, node, subarea) within a catchment

Parameters:

- **`simulation`** (`Simulation`) – A swift simulation object
- **`element_id`** (`Any`, default: `None` ) – a character, identifier of the element within the catchment
- **`full_id`** (`Any`, default: `True` ) – boolean, if TRUE return the full hierarchical identifier

Returns:

- `List[str]` – character vector, names (identifiers) of model states in the element

## gr4j_scaled_parameteriser

```
gr4j_scaled_parameteriser(reference_area: float = 240, t_step_seconds: int = 3600)
```

Get a time step and area scaled parameterizer for the GR4 model structure

Get a time step and area scaled parameterizer for the GR4 model structure

Parameters:

- **`reference_area`** (`Any`, default: `240` ) – The reference area in km^2 for the parameter x4
- **`t_step_seconds`** (`Any`, default: `3600` ) – The simulation time step in seconds.

Returns:

- – A SWIFT catchment parameterizer for GR4 model structures

## inspect

```
inspect(simulation: Simulation, element='link', id='1', full_names=False)
```

Inspect an element of a catchment model

Inspect the current state values of an element of a catchment model

Parameters:

- **`simulation`** (`Simulation`) – A swift simulation object
- **`element`** (`Any`, default: `'link'` ) – type of top level element, within c('link','node','subarea')
- **`id`** (`Any`, default: `'1'` ) – SWIFT simulation
- **`full_names`** (`Any`, default: `False` ) – if TRUE returns the full names of state variable ids (e.g. link.link_1.OutlfowRate)

Returns:

- – named numeric vector, the current state values of the catchment model element

Examples:

TODO

## is_common_iterable

```
is_common_iterable(obj: Any) -> bool
```

True if an object is iterable but not a string (str)

## is_variable_id

```
is_variable_id(simulation: Simulation, var_id: VecStr) -> Union[bool, Dict[str, bool]]
```

Is a variable identifier valid for a simulation

Is a variable identifier valid for a simulation

Parameters:

- **`simulation`** (`Simulation`) – A swift simulation object
- **`var_id`** (`Any`) – a character, identifier(s) of the variable(s)

Returns:

- `Union[bool, Dict[str, bool]]` – logical vector

## lag_and_route_parameteriser

```
lag_and_route_parameteriser()
```

## paste0

```
paste0(*lists, collapse=None)
```

Port of R paste0 function

## pkg_versions_info

```
pkg_versions_info(preamble: str)
```

## play_subarea_input

```
play_subarea_input(simulation: Simulation, input, subarea_name, input_name)
```

Sets time series as input to a simulation

Sets time series as input to a simulation

Parameters:

- **`simulation`** (`Simulation`) – A swift simulation object
- **`input`** (`Any`) – an xts time series.
- **`subarea_name`** (`Any`) – a valid name of the subarea
- **`input_name`** (`Any`) – the name of the input variable to the model (i.e. 'P' for the precip of GR5H)

## rep

```
rep(x: Scalar, n: int)
```

## reset_model_states

```
reset_model_states(simulation: Simulation) -> None
```

Reset the model states of a simulation, and apply one or more state initialers if the simulation is configured with any.

Parameters:

- **`simulation`** (`Simulation`) – simulation

## sample_catchment_model

```
sample_catchment_model(site_id='South_Esk', config_id='catchment')
```

Deserialize a basic catchment structure from the package sample data

Deserialize a basic catchment structure from the package sample data. This function is mostly for documentation purposes.

Parameters:

- **`site_id`** (`Any`, default: `'South_Esk'` ) – a site identifier
- **`config_id`** (`Any`, default: `'catchment'` ) – a variable identifier for a model structure valid for the given site_id

Returns:

- – a model simulation

## sample_series

```
sample_series(site_id='MMH', var_name='rain')
```

Deserialize information to a UTC time series

Deserialize information to a UTC time series. This function is overcoming some behaviors in saving/loading xts series to/from binary RData format. Usage is not intended for most users.

Parameters:

- **`site_id`** (`Any`, default: `'MMH'` ) – a site identifier
- **`var_name`** (`Any`, default: `'rain'` ) – a variable identifier valid for the given site_id

Returns:

- – an xts time series with UTC time indexing

## sce_parameter

```
sce_parameter(nparams: int, nshuffle: int = 40) -> Dict[str, float]
```

Create SCE parameters suited for a given number of parameters.

Parameters:

- **`nparams`** (`int`) – number of free model parameters
- **`nshuffle`** (`int`, default: `40` ) – maximum number of shuffles to do, if no other termination criterion. Defaults to 40.

Returns:

- `Dict[str, float]` – Dict\[str,float\]: SCE hyperparameters

## set_error_correction_model

```
set_error_correction_model(simulation, model_id, element_id, length=1, seed=0)
```

Add an error correction model to an element in a catchment

Add an error correction model to an element in a catchment

Parameters:

- **`simulation`** (`Simulation`) – A swift simulation object
- **`model_id`** (`str`) – the identifier of the new model to use, e.g. 'ERRIS'
- **`element_id`** (`str`) – the identifier of the catchment element (node, link, subcatchment) whose outflow rate is corrected.
- **`length`** (`int`, default: `1` ) – other parameters to pass to the creation of the error correction model. Currently length of the AR model only supported.
- **`seed`** (`int`, default: `0` ) – other parameters to pass to the creation of the error correction model. Currently length of the AR model only supported.

## set_loglik_param_keys

```
set_loglik_param_keys(a='a', b='b', m='m', s='s', maxobs='maxobs', ct='ct', censopt='CensOpt')
```

Specify the global parameter names to use in the log-likelihood calculation

Specify the global parameter names to use in the log-likelihood calculation. Consequence of prehistoric legacy.

Parameters:

- **`a`** (`str`, default: `'a'` ) – the name of the a parameter
- **`b`** (`str`, default: `'b'` ) – the name of the b parameter
- **`m`** (`str`, default: `'m'` ) – the name of the m parameter
- **`s`** (`str`, default: `'s'` ) – the name of the s parameter
- **`maxobs`** (`str`, default: `'maxobs'` ) – the name of the maxobs parameter
- **`ct`** (`str`, default: `'ct'` ) – the name of the ct parameter
- **`censopt`** (`str`, default: `'CensOpt'` ) – the name of the censopt parameter

Examples:

TODO

## set_muskingum_routing_to_linear

```
set_muskingum_routing_to_linear(simulation)
```

## set_sample_data

```
set_sample_data(model_sim, site_id='MMH', rain_data_var='rain', evap_data_var='evap', rain_model_var='P', evap_model_var='E', t_step='daily')
```

Sets sample input data into a model simulation

Sets input data from the included sample data into a model simulation

Parameters:

- **`model_sim`** (`Any`) – an S4 object 'ExternalObjRef' [package "cinterop"] with external pointer type "MODEL_SIMULATION_PTR"
- **`site_id`** (`Any`, default: `'MMH'` ) – sample data site identifier
- **`rain_data_var`** (`Any`, default: `'rain'` ) – time series ID for the rainfall in the sample data
- **`evap_data_var`** (`Any`, default: `'evap'` ) – time series ID for the evaporation in the sample data
- **`rain_model_var`** (`Any`, default: `'P'` ) – sub-area runoff model state identifier for the rainfall, e.g. 'P'
- **`evap_model_var`** (`Any`, default: `'E'` ) – sub-area runoff model state identifier for the evaporation, e.g. 'E'
- **`t_step`** (`Any`, default: `'daily'` ) – identifier for the time step to set the simulation to.

## set_simulation_span

```
set_simulation_span(simulation: Simulation, start, end)
```

Sets simulation span

Sets the simulation span

Parameters:

- **`simulation`** (`Simulation`) – A swift simulation object
- **`start`** (`Any`) – the start date of the simulation. Time zone aware timestamps are not supported..
- **`end`** (`Any`) – the end date of the simulation. Time zone aware timestamps are not supported..

## set_simulation_time_step

```
set_simulation_time_step(simulation: Simulation, name: str)
```

Sets the time step of a SWIFT simulation

Sets the time step of a SWIFT simulation

Parameters:

- **`simulation`** (`Simulation`) – A swift simulation object
- **`name`** (`Any`) – a time step identifier, The identifier is made lower case in the function. Supported time steps include "hourly", "daily", "monthly_qpp", "monthly", and time deltas such as "24:00:00", "01:00:00", "03:00:00". An exception is raised if the string could not be parsed.

## set_state_value

```
set_state_value(simulation: Simulation, var_id: Union[str, Sequence[str], dict], value: Optional[Union[float, Sequence[float]]]) -> None
```

Sets the value(s) of one or more model state variables.

Supports setting a single state by name, a sequence of (name, value) pairs, or a dict mapping variable identifiers to float values.

Note

This function currently only supports float values. For bool or int state variables use `set_state_value_bool` or `set_state_value_int` respectively. The `_func_set_for` helper (which would auto-dispatch to the correct typed setter) is intentionally commented out here; if mixed-type bulk setting is needed it should be wired back in.

Parameters:

- **`simulation`** (`Simulation`) – A swift simulation object.
- **`var_id`** (`Union[str, Sequence[str], dict]`) – One or more model variable state identifiers. When a dict is supplied its keys are used as identifiers and its values override the value argument.
- **`value`** (`Optional[Union[float, Sequence[float]]]`) – The value(s) to assign. Must be a single float when var_id is a str, or a sequence of float of the same length as var_id. A scalar float is broadcast across all identifiers when a sequence of identifiers is provided. Ignored when var_id is a dict.

Raises:

- `ValueError` – If value is not a float when var_id is a single string, if var_id contains non-string elements, or if individual values are not float.

## set_state_value_bool

```
set_state_value_bool(simulation: Simulation, var_id: str, value: bool) -> None
```

## set_state_value_int

```
set_state_value_int(simulation: Simulation, var_id: str, value: int) -> None
```

## set_states

```
set_states(simulation: Simulation, states: MemoryStates) -> None
```

Apply memory states to a simulation

Parameters:

- **`simulation`** (`Simulation`) – simulation
- **`states`** (`MemoryStates`) – memory states

## short_var_id

```
short_var_id(var_ids: VecStr) -> VecStr
```

Shorten long model variable identifiers to the short model variable name

Shorten long model variable identifiers to the short model variable name. This is useful for instance to prepare time series names for multi-plot displays.

Parameters:

- **`var_ids`** (`Any`) – character vector

Returns:

- `VecStr` – the short model variable identifiers

Examples:

```
>>> short_var_id('elementtype|elementname|varid')
>>> short_var_id('elementtype.elementname.varid')
```

## snapshot_state

```
snapshot_state(simulation: Simulation) -> MemoryStates
```

Take a snapshot of the memory states of a simulation

Parameters:

- **`simulation`** (`Simulation`) – model simulation

Returns:

- **`MemoryStates`** ( `MemoryStates` ) – memory states, that can be stored and reapplied

## sort_by_execution_order

```
sort_by_execution_order(simulation: Simulation, split_element_ids, sorting_option='')
```

Sort the specified element ids according to the execution order of the simulation

Sort the specified element ids according to the execution order of the simulation

Parameters:

- **`simulation`** (`Simulation`) – A swift simulation object
- **`split_element_ids`** (`Any`) – a character vector with element identifiers such as 'node.n1', 'link.linkId_2'
- **`sorting_option`** (`Any`, default: `''` ) – a character - for future options. Ignored for now.

Returns:

- – values in split_element_ids sorted by simulation execution order

## swap_model

```
swap_model(simulation: Simulation, model_id, what='runoff')
```

Clone and change a simulation, using another runoff model

Clone and change a simulation, using another runoff model

Parameters:

- **`simulation`** (`Simulation`) – A swift simulation object
- **`model_id`** (`Any`) – the identifier of the new model to use, e.g. 'GR4J'
- **`what`** (`Any`, default: `'runoff'` ) – character identifying the type of structure: 'runoff', 'channel_routing'

Returns:

- – A SWIFT simulation object, clone of the simulation but with a new model type in use.

## testdata_dir

```
testdata_dir()
```
