# Module simulation

# simulation

Functions:

- **`check_simulation`** – Checks whether a simulation is configured to a state where it is executable
- **`create_catchment`** – Create a SWIFT catchment with a specified hydrologic model
- **`create_ensemble_forecast_simulation`** – Create an ensemble forecast simulation
- **`create_subarea`** – Create a SWIFT subarea with a specified hydrologic model
- **`create_subarea_simulation`** – Creates a one sub-catchment simulation
- **`describe`** –
- **`exec_simulation`** – Execute a simulation
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
- **`is_variable_id`** – Is a variable identifier valid for a simulation
- **`reset_model_states`** – Reset the model states of a simulation, and apply one or more state initialers if the simulation is configured with any.
- **`set_error_correction_model`** – Add an error correction model to an element in a catchment
- **`set_simulation_span`** – Sets simulation span
- **`set_simulation_time_step`** – Sets the time step of a SWIFT simulation
- **`set_state_value`** – Sets the value(s) of one or more model state variables.
- **`set_state_value_bool`** –
- **`set_state_value_int`** –
- **`set_states`** – Apply memory states to a simulation
- **`snapshot_state`** – Take a snapshot of the memory states of a simulation
- **`sort_by_execution_order`** – Sort the specified element ids according to the execution order of the simulation
- **`swap_model`** – Clone and change a simulation, using another runoff model

## check_simulation

```
check_simulation(simulation) -> Dict
```

Checks whether a simulation is configured to a state where it is executable

Checks whether a simulation is configured to a state where it is executable

Parameters:

- **`simulation`** (`Simulation`) – A swift simulation object

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

## describe

```
describe(simulation: Simulation, verbosity: Any = None) -> Dict
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

## reset_model_states

```
reset_model_states(simulation: Simulation) -> None
```

Reset the model states of a simulation, and apply one or more state initialers if the simulation is configured with any.

Parameters:

- **`simulation`** (`Simulation`) – simulation

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
