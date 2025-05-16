# Module simulation

## `check_simulation(simulation)`

Checks whether a simulation is configured to a state where it is executable

Checks whether a simulation is configured to a state where it is executable

Parameters:

| Name | Type | Description | Default | | --- | --- | --- | --- | | `simulation` | `Simulation` | A swift simulation object | *required* |

Source code in `.venv/lib/python3.13/site-packages/swift2/simulation.py`

```
def check_simulation(simulation) -> Dict:
    """
    Checks whether a simulation is configured to a state where it is executable

    Checks whether a simulation is configured to a state where it is executable

    Args:
        simulation (Simulation): A swift simulation object

    """
    # Trying to design this such that we can have several types of messages
    return {"errors": swg.CheckSimulationErrors_py(simulation)}

```

## `create_catchment(node_ids, node_names, link_ids, link_names, link_from_node, link_to_node, runoff_model_name='GR4J', areas_km2=None)`

Create a SWIFT catchment with a specified hydrologic model

Create a SWIFT catchment with a specified hydrologic model. This function is intended mostly for testing, not for usual modelling code.

Parameters:

| Name | Type | Description | Default | | --- | --- | --- | --- | | `node_ids` | `Any` | character, node unique identifiers | *required* | | `node_names` | `Any` | character, node display names | *required* | | `link_ids` | `Any` | character, links unique identifiers | *required* | | `link_names` | `Any` | character, links display names | *required* | | `link_from_node` | `Any` | character, identifier of the links' upstream node | *required* | | `link_to_node` | `Any` | character, identifier of the links' downstream node | *required* | | `runoff_model_name` | `Any` | A valid, known SWIFT model name (e.g. 'GR5H') | `'GR4J'` | | `areas_km2` | `Any` | The areas in square kilometres | `None` |

Returns:

| Type | Description | | --- | --- | | | A SWIFT simulation object (i.e. a model runner) |

Examples:

TODO

Source code in `.venv/lib/python3.13/site-packages/swift2/simulation.py`

```
def create_catchment(
    node_ids: List,
    node_names: List,
    link_ids: List,
    link_names: List,
    link_from_node: List,
    link_to_node: List,
    runoff_model_name: str = "GR4J",
    areas_km2: List[float] = None,
):
    """
    Create a SWIFT catchment with a specified hydrologic model

    Create a SWIFT catchment with a specified hydrologic model.
    This function is intended mostly for testing, not for usual modelling code.

    Args:
        node_ids (Any): character, node unique identifiers
        node_names (Any): character, node display names
        link_ids (Any): character, links unique identifiers
        link_names (Any): character, links display names
        link_from_node (Any): character, identifier of the links' upstream node
        link_to_node (Any): character, identifier of the links' downstream node
        runoff_model_name (Any): A valid, known SWIFT model name (e.g. 'GR5H')
        areas_km2 (Any): The areas in square kilometres

    Returns:
        A SWIFT simulation object (i.e. a model runner)

    Examples:
        TODO

    """
    # >>> # nodeIds=paste0('n', 1:6)
    # >>> # linkIds = paste0('lnk', 1:5)
    # >>> # defn <- list(
    # >>> # nodeIds=nodeIds,
    # >>> # nodeNames = paste0(nodeIds, '_name'),
    # >>> # linkIds=linkIds,
    # >>> # linkNames = paste0(linkIds, '_name'),
    # >>> # fromNode = paste0('n', c(2,5,4,3,1)),
    # >>> # toNode = paste0('n', c(6,2,2,4,4)),
    # >>> # areasKm2 = c(1.2, 2.3, 4.4, 2.2, 1.5),
    # >>> # runoffModel = 'GR4J'
    # >>> # )
    # >>> # ms <- createCatchment(defn$nodeIds, defn$nodeNames, defn$linkIds, defn$linkNames, defn$fromNode, defn$toNode, defn$runoffModel, defn$areasKm2)
    if areas_km2 is None:
        areas_km2 = rep(1.0, len(link_ids))
    return swg.CreateCatchment_py(
        numNodes=len(node_ids),
        nodeIds=node_ids,
        nodeNames=node_names,
        numLinks=len(link_ids),
        linkIds=link_ids,
        linkNames=link_names,
        linkFromNode=link_from_node,
        linkToNode=link_to_node,
        runoffModelName=runoff_model_name,
        areasKm2=areas_km2,
    )

```

## `create_ensemble_forecast_simulation(simulation, data_library, start, end, input_map, lead_time, ensemble_size, n_time_steps_between_forecasts)`

Create an ensemble forecast simulation

Create an ensemble forecast simulation

Parameters:

| Name | Type | Description | Default | | --- | --- | --- | --- | | `simulation` | `Simulation` | A swift simulation object | *required* | | `data_library` | `Any` | external pointer type ENSEMBLE_DATA_SET_PTR, or a Python class wrapper around it | *required* | | `start` | `Any` | the start date of the simulation. The time zone will be forced to UTC. | *required* | | `end` | `Any` | the end date of the simulation. The time zone will be forced to UTC. | *required* | | `input_map` | `Any` | a named list were names are the data library data identifiers, and values are character vectors with model state identifiers. | *required* | | `lead_time` | `Any` | integer, the length in time steps of the forecasts. | *required* | | `ensemble_size` | `Any` | ensemble size | *required* | | `n_time_steps_between_forecasts` | `Any` | nTimeStepsBetweenForecasts | *required* |

Returns:

| Type | Description | | --- | --- | | | An external pointer |

Source code in `.venv/lib/python3.13/site-packages/swift2/simulation.py`

```
def create_ensemble_forecast_simulation(
    simulation,
    data_library,
    start,
    end,
    input_map: Dict[str, List[str]],
    lead_time,
    ensemble_size,
    n_time_steps_between_forecasts,
):
    """
    Create an ensemble forecast simulation

    Create an ensemble forecast simulation

    Args:
        simulation (Simulation): A swift simulation object
        data_library (Any): external pointer type ENSEMBLE_DATA_SET_PTR, or a Python class wrapper around it 
        start (Any): the start date of the simulation. The time zone will be forced to UTC.
        end (Any): the end date of the simulation. The time zone will be forced to UTC.
        input_map (Any): a named list were names are the data library data identifiers, and values are character vectors with model state identifiers.
        lead_time (Any): integer, the length in time steps of the forecasts.
        ensemble_size (Any): ensemble size
        n_time_steps_between_forecasts (Any): nTimeStepsBetweenForecasts

    Returns:
        An external pointer

    """
    s = as_timestamp(start)
    e = as_timestamp(end)
    simulation_length = swg.GetNumStepsForTimeSpan_py(simulation, s, e)
    ef_simulation = swg.CreateEnsembleForecastSimulation_py(
        simulation,
        s,
        lead_time,
        ensemble_size,
        simulation_length,
        nTimeStepsBetweenForecasts=n_time_steps_between_forecasts,
    )
    data_ids = input_map.keys()
    for data_id in data_ids:
        identifiers = input_map[data_id]
        swg.PlayDatasetEnsembleForecastInput_py(
            ef_simulation,
            data_library,
            identifiers,
            rep(data_id, len(identifiers)),
            len(identifiers),
        )
    return ef_simulation

```

## `create_subarea(model_name, area_km2)`

Create a SWIFT subarea with a specified hydrologic model

Create a SWIFT subarea with a specified hydrologic model

Parameters:

| Name | Type | Description | Default | | --- | --- | --- | --- | | `model_name` | `Any` | A valid, known SWIFT model name (e.g. 'GR5H') | *required* | | `area_km2` | `Any` | The area in square kilometres | *required* |

Returns:

| Type | Description | | --- | --- | | | A SWIFT simulation object (i.e. a model runner) |

Source code in `.venv/lib/python3.13/site-packages/swift2/simulation.py`

```
def create_subarea(model_name, area_km2):
    """
    Create a SWIFT subarea with a specified hydrologic model

    Create a SWIFT subarea with a specified hydrologic model

    Args:
        model_name (Any): A valid, known SWIFT model name (e.g. 'GR5H')
        area_km2 (Any): The area in square kilometres

    Returns:
        A SWIFT simulation object (i.e. a model runner)

    """
    return swg.CreateSubarea_py(model_name, area_km2)

```

## `create_subarea_simulation(data_id='MMH', simul_start='1990-01-01', simul_end='2005-12-31', model_id='GR4J', tstep='daily', varname_rain='P', varname_pet='E', data_rain_id='rain', data_evap_id='evap')`

Creates a one sub-catchment simulation

Creates a one sub-catchment simulation. This function is intended for creating sample simulations, not for use in production.

Parameters:

| Name | Type | Description | Default | | --- | --- | --- | --- | | `data_id` | `str` | data identifier in swift_sample_data | `'MMH'` | | `simul_start` | `str` | ISO string for the simulation start date time | `'1990-01-01'` | | `simul_end` | `str` | ISO string for the simulation end date time | `'2005-12-31'` | | `model_id` | `str` | model identifier | `'GR4J'` | | `tstep` | `str` | character, 'daily' or 'hourly' | `'daily'` | | `varname_rain` | `str` | variable name to assign rainfall to | `'P'` | | `varname_pet` | `str` | variable name to assign PET to | `'E'` | | `data_rain_id` | `str` | key to use to retrieve the rainfall series from the sample data | `'rain'` | | `data_evap_id` | `str` | key to use to retrieve the evaporation series from the sample data | `'evap'` |

Returns:

| Type | Description | | --- | --- | | | A SWIFT simulation object, clone of the simulation but with a new model type in use. |

Source code in `.venv/lib/python3.13/site-packages/swift2/simulation.py`

```
def create_subarea_simulation(
    data_id:str="MMH",
    simul_start:str="1990-01-01",
    simul_end:str="2005-12-31",
    model_id:str="GR4J",
    tstep:str="daily",
    varname_rain:str="P",
    varname_pet:str="E",
    data_rain_id:str="rain",
    data_evap_id:str="evap",
):
    """
    Creates a one sub-catchment simulation

    Creates a one sub-catchment simulation. This function is intended for creating sample simulations, not for use in production.

    Args:
        data_id (str): data identifier in swift_sample_data
        simul_start (str): ISO string for the simulation start date time
        simul_end (str): ISO string for the simulation end date time
        model_id (str): model identifier
        tstep (str): character, 'daily' or 'hourly'
        varname_rain (str): variable name to assign rainfall to
        varname_pet (str): variable name to assign PET to
        data_rain_id (str): key to use to retrieve the rainfall series from the sample data
        data_evap_id (str): key to use to retrieve the evaporation series from the sample data

    Returns:
        A SWIFT simulation object, clone of the simulation but with a new model type in use.

    """
    from swift2.doc_helper import sample_series
    from swift2.wrap.swift_wrap_generated import CreateSubarea_py

    s_span = slice(simul_start, simul_end)
    rain = sample_series(data_id, data_rain_id)[s_span]
    evap = sample_series(data_id, data_evap_id)[s_span]

    ms = CreateSubarea_py(model_id, 1.0)
    s = rain.index[0]
    e = rain.index[-1]
    set_simulation_span(ms, s, e)
    set_simulation_time_step(ms, tstep)

    sa_name = swg.GetSubareaNames_py(ms)[0]
    play_subarea_input(ms, rain, sa_name, varname_rain)
    play_subarea_input(ms, evap, sa_name, varname_pet)
    return ms

```

## `exec_simulation(simulation, reset_initial_states=True)`

Execute a simulation

Execute a simulation

Parameters:

| Name | Type | Description | Default | | --- | --- | --- | --- | | `simulation` | `Simulation` | A swift simulation object | *required* | | `reset_initial_states` | `Any` | logical, should the states of the model be reinitialized before the first time step. | `True` |

Source code in `.venv/lib/python3.13/site-packages/swift2/simulation.py`

```
def exec_simulation(simulation: "Simulation", reset_initial_states=True):
    """
    Execute a simulation

    Execute a simulation

    Args:
        simulation (Simulation): A swift simulation object
        reset_initial_states (Any): logical, should the states of the model be reinitialized before the first time step.

    """
    if simulation.type_id == "ENSEMBLE_FORECAST_SIMULATION_PTR":
        swg.ExecuteEnsembleForecastSimulation_py(simulation)
    elif simulation.type_id == "ENSEMBLE_SIMULATION_PTR":
        raise NotImplementedError(
            "execution api entry point for 'ENSEMBLE_SIMULATION_PTR' is not available??"
        )
    else:
        swg.ExecuteSimulation_py(simulation, reset_initial_states)

```

## `get_link_ids(simulation)`

Gets all the identifiers of the links in the catchment

Gets all the identifiers of the links in the catchment

Parameters:

| Name | Type | Description | Default | | --- | --- | --- | --- | | `simulation` | `Simulation` | A swift simulation object | *required* |

Returns:

| Type | Description | | --- | --- | | | The identifiers of the links in the catchment |

Source code in `.venv/lib/python3.13/site-packages/swift2/simulation.py`

```
def get_link_ids(simulation):
    """
    Gets all the identifiers of the links in the catchment

    Gets all the identifiers of the links in the catchment

    Args:
        simulation (Simulation): A swift simulation object

    Returns:
        The identifiers of the links in the catchment

    """
    return swg.GetLinkIdentifiers_py(simulation)

```

## `get_link_names(simulation)`

Gets all the names of the links in the catchment

Gets all the names of the links in the catchment

Parameters:

| Name | Type | Description | Default | | --- | --- | --- | --- | | `simulation` | `Simulation` | A swift simulation object | *required* |

Returns:

| Type | Description | | --- | --- | | | The names of the links in the catchment |

Source code in `.venv/lib/python3.13/site-packages/swift2/simulation.py`

```
def get_link_names(simulation):
    """
    Gets all the names of the links in the catchment

    Gets all the names of the links in the catchment

    Args:
        simulation (Simulation): A swift simulation object

    Returns:
        The names of the links in the catchment

    """

    return swg.GetLinkNames_py(simulation)

```

## `get_node_ids(simulation)`

Gets all the identifiers of the nodes in the catchment

Gets all the identifiers of the nodes in the catchment

Parameters:

| Name | Type | Description | Default | | --- | --- | --- | --- | | `simulation` | `Simulation` | A swift simulation object | *required* |

Returns:

| Type | Description | | --- | --- | | | The identifiers of the nodes in the catchment |

Source code in `.venv/lib/python3.13/site-packages/swift2/simulation.py`

```
def get_node_ids(simulation):
    """
    Gets all the identifiers of the nodes in the catchment

    Gets all the identifiers of the nodes in the catchment

    Args:
        simulation (Simulation): A swift simulation object

    Returns:
        The identifiers of the nodes in the catchment

    """
    return swg.GetNodeIdentifiers_py(simulation)

```

## `get_node_names(simulation)`

Gets all the names of the nodes in the catchment

Gets all the names of the nodes in the catchment

Parameters:

| Name | Type | Description | Default | | --- | --- | --- | --- | | `simulation` | `Simulation` | A swift simulation object | *required* |

Returns:

| Type | Description | | --- | --- | | | The names of the nodes in the catchment |

Source code in `.venv/lib/python3.13/site-packages/swift2/simulation.py`

```
def get_node_names(simulation):
    """
    Gets all the names of the nodes in the catchment

    Gets all the names of the nodes in the catchment

    Args:
        simulation (Simulation): A swift simulation object

    Returns:
        The names of the nodes in the catchment

    """
    return swg.GetNodeNames_py(simulation)

```

## `get_state_value(simulation, var_id)`

Gets the value(s) of a model state(s)

Parameters:

| Name | Type | Description | Default | | --- | --- | --- | --- | | `simulation` | `Simulation` | A swift simulation object | *required* | | `var_id` | `VecStr` | string or sequence of str, model variable state identifier(s) | *required* |

Returns:

| Type | Description | | --- | --- | | | numeric vector, value(s) of the requested model states |

Source code in `.venv/lib/python3.13/site-packages/swift2/simulation.py`

```
def get_state_value(simulation: "Simulation", var_id: "VecStr"):
    """
    Gets the value(s) of a model state(s)

    Args:
        simulation (Simulation): A swift simulation object
        var_id (VecStr): string or sequence of str, model variable state identifier(s)

    Returns:
        numeric vector, value(s) of the requested model states

    """
    if isinstance(var_id, str):
        var_ids = [var_id]
    else:
        var_ids = var_id
    #  if(is.numeric(value)):
    f = swg.GetVariable_py
    #  } else if(is.integer(value)):
    #    f = GetVariableInt_R
    #  } else if(is.logical(value)):
    #    f = GetVariableBool_R
    #  else:
    #    stop(paste('value type', type(value), 'is not supported by getStateValue'))
    #  }
    return dict([(v, f(simulation, v)) for v in var_ids])

```

## `get_subarea_ids(simulation)`

Gets all the identifiers of the sub-areas in the catchment

Gets all the identifiers of the sub-areas in the catchment

Parameters:

| Name | Type | Description | Default | | --- | --- | --- | --- | | `simulation` | `Simulation` | A swift simulation object | *required* |

Returns:

| Type | Description | | --- | --- | | | The identifiers of the sub-areas in the catchment |

Source code in `.venv/lib/python3.13/site-packages/swift2/simulation.py`

```
def get_subarea_ids(simulation):
    """
    Gets all the identifiers of the sub-areas in the catchment

    Gets all the identifiers of the sub-areas in the catchment

    Args:
        simulation (Simulation): A swift simulation object

    Returns:
        The identifiers of the sub-areas in the catchment

    """
    return swg.GetSubareaIdentifiers_py(simulation)

```

## `get_subarea_names(simulation)`

Gets all the names of the sub-areas in the catchment

Gets all the names of the sub-areas in the catchment

Parameters:

| Name | Type | Description | Default | | --- | --- | --- | --- | | `simulation` | `Simulation` | A swift simulation object | *required* |

Returns:

| Type | Description | | --- | --- | | | The names of the sub-areas in the catchment |

Source code in `.venv/lib/python3.13/site-packages/swift2/simulation.py`

```
def get_subarea_names(simulation):
    """
    Gets all the names of the sub-areas in the catchment

    Gets all the names of the sub-areas in the catchment

    Args:
        simulation (Simulation): A swift simulation object

    Returns:
        The names of the sub-areas in the catchment

    """

    return swg.GetSubareaNames_py(simulation)

```

## `get_variable_ids(simulation, element_id=None, full_id=True)`

Gets all the names of the variables of an element within a catchment

Gets all the names of the variables of an element (link, node, subarea) within a catchment

Parameters:

| Name | Type | Description | Default | | --- | --- | --- | --- | | `simulation` | `Simulation` | A swift simulation object | *required* | | `element_id` | `Any` | a character, identifier of the element within the catchment | `None` | | `full_id` | `Any` | boolean, if TRUE return the full hierarchical identifier | `True` |

Returns:

| Type | Description | | --- | --- | | | character vector, names (identifiers) of model states in the element |

Source code in `.venv/lib/python3.13/site-packages/swift2/simulation.py`

```
def get_variable_ids(simulation: "Simulation", element_id=None, full_id=True):
    """
    Gets all the names of the variables of an element within a catchment

    Gets all the names of the variables of an element (link, node, subarea) within a catchment

    Args:
        simulation (Simulation): A swift simulation object
        element_id (Any): a character, identifier of the element within the catchment
        full_id (Any): boolean, if TRUE return the full hierarchical identifier

    Returns:
        character vector, names (identifiers) of model states in the element

    """
    s = swg.GetElementVarIdentifiers_py(simulation, element_id)
    if full_id and element_id is not None:
        s = [_mkid(element_id, v) for v in s]
    return s

```

## `is_variable_id(simulation, var_id)`

Is a variable identifier valid for a simulation

Is a variable identifier valid for a simulation

Parameters:

| Name | Type | Description | Default | | --- | --- | --- | --- | | `simulation` | `Simulation` | A swift simulation object | *required* | | `var_id` | `Any` | a character, identifier(s) of the variable(s) | *required* |

Returns:

| Type | Description | | --- | --- | | | logical vector |

Source code in `.venv/lib/python3.13/site-packages/swift2/simulation.py`

```
def is_variable_id(simulation: "Simulation", var_id: "VecStr"):
    """
    Is a variable identifier valid for a simulation

    Is a variable identifier valid for a simulation

    Args:
        simulation (Simulation): A swift simulation object
        var_id (Any): a character, identifier(s) of the variable(s)

    Returns:
        logical vector

    """
    if is_common_iterable(var_id):
        return dict(
            [(v, swg.IsValidVariableIdentifier_py(simulation, v)) for v in var_id]
        )
    else:
        return swg.IsValidVariableIdentifier_py(simulation, var_id)

```

## `reset_model_states(simulation)`

Reset the model states of a simulation, and apply one or more state initialers if the simulation is configured with any.

Parameters:

| Name | Type | Description | Default | | --- | --- | --- | --- | | `simulation` | `Simulation` | simulation | *required* |

Source code in `.venv/lib/python3.13/site-packages/swift2/simulation.py`

```
def reset_model_states(simulation: "Simulation"):
    """Reset the model states of a simulation, and apply one or more state initialers if the simulation is configured with any.

    Args:
        simulation (Simulation): simulation
    """
    swg.ResetModelStates_py(simulation)

```

## `set_error_correction_model(simulation, model_id, element_id, length=1, seed=0)`

Add an error correction model to an element in a catchment

Add an error correction model to an element in a catchment

Parameters:

| Name | Type | Description | Default | | --- | --- | --- | --- | | `simulation` | `Simulation` | A swift simulation object | *required* | | `model_id` | `str` | the identifier of the new model to use, e.g. 'ERRIS' | *required* | | `element_id` | `str` | the identifier of the catchment element (node, link, subcatchment) whose outflow rate is corrected. | *required* | | `length` | `int` | other parameters to pass to the creation of the error correction model. Currently length of the AR model only supported. | `1` | | `seed` | `int` | other parameters to pass to the creation of the error correction model. Currently length of the AR model only supported. | `0` |

Source code in `.venv/lib/python3.13/site-packages/swift2/simulation.py`

```
def set_error_correction_model(
    simulation, model_id, element_id, length=1, seed=0
):  # TODO: revert to use ... if other kind of ECM
    """
    Add an error correction model to an element in a catchment

    Add an error correction model to an element in a catchment

    Args:
        simulation (Simulation): A swift simulation object
        model_id (str): the identifier of the new model to use, e.g. 'ERRIS'
        element_id (str): the identifier of the catchment element (node, link, subcatchment) whose outflow rate is corrected.
        length (int): other parameters to pass to the creation of the error correction model. Currently length of the AR model only supported.
        seed (int): other parameters to pass to the creation of the error correction model. Currently length of the AR model only supported.

    """
    swg.SetErrorCorrectionModel_py(simulation, model_id, element_id, length, seed)

```

## `set_simulation_span(simulation, start, end)`

Sets simulation span

Sets the simulation span

Parameters:

| Name | Type | Description | Default | | --- | --- | --- | --- | | `simulation` | `Simulation` | A swift simulation object | *required* | | `start` | `Any` | the start date of the simulation. The time zone will be forced to UTC. | *required* | | `end` | `Any` | the end date of the simulation. The time zone will be forced to UTC. | *required* |

Source code in `.venv/lib/python3.13/site-packages/swift2/simulation.py`

```
def set_simulation_span(simulation: "Simulation", start, end):
    """
    Sets simulation span

    Sets the simulation span

    Args:
        simulation (Simulation): A swift simulation object
        start (Any): the start date of the simulation. The time zone will be forced to UTC.
        end (Any): the end date of the simulation. The time zone will be forced to UTC.

    """
    s = as_timestamp(start)  # = as_timestamp(start, tz='UTC')
    e = as_timestamp(end)  # = as_timestamp(end, tz='UTC')
    swg.SetSpan_py(simulation, s, e)

```

## `set_simulation_time_step(simulation, name)`

Sets the time step of a SWIFT simulation

Sets the time step of a SWIFT simulation

Parameters:

| Name | Type | Description | Default | | --- | --- | --- | --- | | `simulation` | `Simulation` | A swift simulation object | *required* | | `name` | `Any` | a time step identifier, The identifier is made lower case in the function. Supported time steps include "hourly", "daily", "monthly_qpp", "monthly", and time deltas such as "24:00:00", "01:00:00", "03:00:00". An exception is raised if the string could not be parsed. | *required* |

Source code in `.venv/lib/python3.13/site-packages/swift2/simulation.py`

```
def set_simulation_time_step(simulation: "Simulation", name: str):
    """
    Sets the time step of a SWIFT simulation

    Sets the time step of a SWIFT simulation

    Args:
        simulation (Simulation): A swift simulation object
        name (Any): a time step identifier, The identifier is made lower case in the function. Supported time steps include "hourly", "daily", "monthly_qpp", "monthly", and time deltas such as "24:00:00", "01:00:00", "03:00:00". An exception is raised if the string could not be parsed.

    """
    name = name.lower()
    # assert name in set(['daily','hourly'])
    swg.SetTimeStep_py(simulation, name)

```

## `set_state_value(simulation, var_id, value)`

Sets the value of a model state

Sets the value of a model state

Parameters:

| Name | Type | Description | Default | | --- | --- | --- | --- | | `simulation` | `Simulation` | A swift simulation object | *required* | | `var_id` | `(str, Sequence[str])` | character, model variable state identifier(s) | *required* | | `value` | `(float, int, bool, Sequence)` | numeric value(s) | *required* |

Source code in `.venv/lib/python3.13/site-packages/swift2/simulation.py`

```
def set_state_value(
    simulation: "Simulation",
    var_id: Union[str, Sequence[str]],
    value: Union[float, int, bool, Sequence],
) -> None:
    """
    Sets the value of a model state

    Sets the value of a model state

    Args:
        simulation (Simulation): A swift simulation object
        var_id (str, Sequence[str]): character, model variable state identifier(s)
        value (float, int, bool, Sequence): numeric value(s)

    """

    def func_set_for(v):
        if isinstance(v, float): # or isinstance(v, np.float): # np obsolete?
            return swg.SetVariable_py
        elif isinstance(v, int): # or isinstance(v, np.int):
            return swg.SetVariableInt_py
        elif isinstance(v, bool): # or isinstance(v, np.bool8):
            return swg.SetVariableBool_py
        else:
            raise TypeError(
                "value type " + str(type(v)) + "is not supported by setStateValue"
            )

    if isinstance(var_id, str):
        f = func_set_for(value)
        f(simulation, var_id, value)
        return
    if isinstance(var_id, dict):
        d = [(k, v) for k, v in var_id.items()]
        var_id = [x[0] for x in d]
        value = [x[1] for x in d]
    if not is_common_iterable(var_id):
        raise ValueError("var_id must be a string, or an iterable of strings")
    if not is_common_iterable(value):
        value = rep(value, len(var_id))
    else:
        assert len(var_id) == len(value)

    for i in range(len(var_id)):
        k = var_id[i]
        v = value[i]
        f = func_set_for(v)
        f(simulation, k, v)

```

## `set_states(simulation, states)`

Apply memory states to a simulation

Parameters:

| Name | Type | Description | Default | | --- | --- | --- | --- | | `simulation` | `Simulation` | simulation | *required* | | `states` | `MemoryStates` | memory states | *required* |

Source code in `.venv/lib/python3.13/site-packages/swift2/simulation.py`

```
def set_states(simulation: "Simulation", states: "MemoryStates"):
    """Apply memory states to a simulation

    Args:
        simulation (Simulation): simulation
        states (MemoryStates): memory states
    """
    swg.ApplyMemoryStates_py(simulation, states)

```

## `snapshot_state(simulation)`

Take a snapshot of the memory states of a simulation

Parameters:

| Name | Type | Description | Default | | --- | --- | --- | --- | | `simulation` | `Simulation` | model simulation | *required* |

Returns:

| Name | Type | Description | | --- | --- | --- | | `MemoryStates` | `MemoryStates` | memory states, that can be stored and reapplied |

Source code in `.venv/lib/python3.13/site-packages/swift2/simulation.py`

```
def snapshot_state(simulation: "Simulation") -> "MemoryStates":
    """Take a snapshot of the memory states of a simulation

    Args:
        simulation (Simulation): model simulation

    Returns:
        MemoryStates: memory states, that can be stored and reapplied
    """
    return swg.SnapshotMemoryStates_py(simulation)

```

## `sort_by_execution_order(simulation, split_element_ids, sorting_option='')`

Sort the specified element ids according to the execution order of the simulation

Sort the specified element ids according to the execution order of the simulation

Parameters:

| Name | Type | Description | Default | | --- | --- | --- | --- | | `simulation` | `Simulation` | A swift simulation object | *required* | | `split_element_ids` | `Any` | a character vector with element identifiers such as 'node.n1', 'link.linkId_2' | *required* | | `sorting_option` | `Any` | a character - for future options. Ignored for now. | `''` |

Returns:

| Type | Description | | --- | --- | | | values in split_element_ids sorted by simulation execution order |

Source code in `.venv/lib/python3.13/site-packages/swift2/simulation.py`

```
def sort_by_execution_order(
    simulation: "Simulation", split_element_ids, sorting_option=""
):
    """
    Sort the specified element ids according to the execution order of the simulation

    Sort the specified element ids according to the execution order of the simulation

    Args:
        simulation (Simulation): A swift simulation object
        split_element_ids (Any): a character vector with element identifiers such as 'node.n1', 'link.linkId_2'
        sorting_option (Any): a character - for future options. Ignored for now.

    Returns:
        values in split_element_ids sorted by simulation execution order

    """
    return swc.sort_simulation_elements_by_run_order_pkg(
        simulation, split_element_ids, sorting_option
    )

```

## `swap_model(simulation, model_id, what='runoff')`

Clone and change a simulation, using another runoff model

Clone and change a simulation, using another runoff model

Parameters:

| Name | Type | Description | Default | | --- | --- | --- | --- | | `simulation` | `Simulation` | A swift simulation object | *required* | | `model_id` | `Any` | the identifier of the new model to use, e.g. 'GR4J' | *required* | | `what` | `Any` | character identifying the type of structure: 'runoff', 'channel_routing' | `'runoff'` |

Returns:

| Type | Description | | --- | --- | | | A SWIFT simulation object, clone of the simulation but with a new model type in use. |

Source code in `.venv/lib/python3.13/site-packages/swift2/simulation.py`

```
def swap_model(simulation: "Simulation", model_id, what="runoff"):
    """
    Clone and change a simulation, using another runoff model

    Clone and change a simulation, using another runoff model

    Args:
        simulation (Simulation): A swift simulation object
        model_id (Any): the identifier of the new model to use, e.g. 'GR4J'
        what (Any): character identifying the type of structure: 'runoff', 'channel_routing'

    Returns:
        A SWIFT simulation object, clone of the simulation but with a new model type in use.

    """
    if what == "runoff":
        cloned = swg.SwapRunoffModel_py(simulation, model_id)
    elif what == "channel_routing":
        cloned = swg.CloneModel_py(simulation)
        swg.SetChannelRoutingModel_py(cloned, model_id)
    else:
        raise ValueError(f"option not supported: {what}")
    return cloned

```
