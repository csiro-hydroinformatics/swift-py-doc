# Module doc_helper

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

## `configure_daily_gr4j(simulation)`

Configure a simulation with GR4J models for daily time step modelling

Configure a simulation with GR4J models for daily time step modelling

Parameters:

| Name | Type | Description | Default | | --- | --- | --- | --- | | `simulation` | `Simulation` | A swift simulation object | *required* |

Source code in `.venv/lib/python3.13/site-packages/swift2/doc_helper.py`

```
def configure_daily_gr4j(simulation):
    """
    Configure a simulation with GR4J models for daily time step modelling

    Configure a simulation with GR4J models for daily time step modelling

    Args:
        simulation (Simulation): A swift simulation object

    """
    pGr4jHourly = create_gr4jh_parameters(hourly=False)
    apply_sys_config(pGr4jHourly, simulation)

```

## `configure_hourly_gr4j(simulation)`

Configure a simulation with GR4J models for hourly time step modelling

Configure a simulation with GR4J models for hourly time step modelling

Parameters:

| Name | Type | Description | Default | | --- | --- | --- | --- | | `simulation` | `Simulation` | A swift simulation object | *required* |

Source code in `.venv/lib/python3.13/site-packages/swift2/doc_helper.py`

```
def configure_hourly_gr4j(simulation):
    """
    Configure a simulation with GR4J models for hourly time step modelling

    Configure a simulation with GR4J models for hourly time step modelling

    Args:
        simulation (Simulation): A swift simulation object

    """
    pGr4jHourly = create_gr4jh_parameters(hourly=True)
    apply_sys_config(pGr4jHourly, simulation)

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

## `create_gr4jh_parameters(hourly=True)`

Get a parameter set that configures GR4J for hourly or daily operations

Derived from the initial Fortran implementation in SWIFTv1 * UHExponent = 2.5 is the default value for daily time step. Set to 1.25 for hourly time step * PercFactor = 9.0 / 4.0 for daily, 4.0 for hourly time step.

Returns:

| Name | Type | Description | | --- | --- | --- | | `HyperCubeParameteriser` | | a parameter set that can be applied to SWIFT systems with GR4J |

Source code in `.venv/lib/python3.13/site-packages/swift2/doc_helper.py`

```
def create_gr4jh_parameters(hourly:bool = True):
    """
    Get a parameter set that configures GR4J for hourly or daily operations

    Derived from the initial Fortran implementation in SWIFTv1
    * UHExponent = 2.5 is the default value for daily time step. Set to 1.25 for hourly time step
    * PercFactor = 9.0 / 4.0 for daily, 4.0  for hourly time step.

    Returns:
        HyperCubeParameteriser: a parameter set that can be applied to SWIFT systems with GR4J

    """
    # Configure for GR4J but with changed parameters, supposed to be OK for hourly operations according to SWIFTv1
    uhexponent = 1.25 if hourly else 2.5
    percfactor = 4.0 if hourly else 9.0 / 4.0
    return create_parameteriser(
        type = "Generic subareas",
        specs=_df_from_dict(
            Name=["PercFactor", "UHExponent"],
            Value=_npf([percfactor, uhexponent]),
            Min=_npf([percfactor, uhexponent]),
            Max=_npf([percfactor, uhexponent]),
        )
    )

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

## `define_gr4j_scaled_parameter(ref_area=250, time_span=3600, pspec_gr4j=None)`

define a scaled and transformed parameterizer for GR4J

define a scaled and transformed parameterizer for GR4J

Parameters:

| Name | Type | Description | Default | | --- | --- | --- | --- | | `ref_area` | `float` | the reference area in square kilometres | `250` | | `time_span` | `int` | the time span of the simulation intented for this model, in seconds | `3600` | | `pspec_gr4j` | `DataFrame` | optional - data frame specifying the feasible parameter space for parameters x1 to x2 of GR4J | `None` |

Returns:

| Name | Type | Description | | --- | --- | --- | | `TransformParameteriser` | | a parameterizer for GR4J, combining time and area scaling and superimposed with log10 transforms for x1, x3, x4 and arc-sinh for x2 |

Source code in `.venv/lib/python3.13/site-packages/swift2/doc_helper.py`

```
def define_gr4j_scaled_parameter(ref_area:float=250, time_span:int=3600, pspec_gr4j:Optional[pd.DataFrame]=None):
    """
    define a scaled and transformed parameterizer for GR4J

    define a scaled and transformed parameterizer for GR4J

    Args:
        ref_area (float): the reference area in square kilometres
        time_span (int): the time span of the simulation intented for this model, in seconds
        pspec_gr4j (pd.DataFrame): optional - data frame specifying the feasible parameter space for parameters x1 to x2 of GR4J

    Returns:
        TransformParameteriser: a parameterizer for GR4J, combining time and area scaling and superimposed with log10 transforms for x1, x3, x4 and arc-sinh for x2
    """
    time_span = int(time_span)
    parameteriser = gr4j_scaled_parameteriser(ref_area, time_span)
    if pspec_gr4j is None:
        pspec_gr4j = _df_from_dict(
            Name=["x1", "x2", "x3", "x4"],
            Value=_npf([3.21137e00, 6.95511e00, 2.06740e00, 2.02033e00]),
            Min=_npf([1.0e00, -27.0, 1.0e00, 1.0e00]),
            Max=_npf([6.0e03, 27.0, 1.0e03, 2.4e02]),
        )
    set_hypercube(parameteriser, pspec_gr4j)
    parameteriser = wrap_transform(parameteriser)
    add_transform(parameteriser, "log_x4", "x4", "log10")
    add_transform(parameteriser, "log_x1", "x1", "log10")
    add_transform(parameteriser, "log_x3", "x3", "log10")
    add_transform(parameteriser, "asinh_x2", "x2", "asinh")

    return parameteriser

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

## `get_catchment_dot_graph(simulation)`

Gets a catchment representation in Graphviz DOT format

Gets a catchment representation in Graphviz DOT format

Parameters:

| Name | Type | Description | Default | | --- | --- | --- | --- | | `simulation` | `Simulation` | A swift simulation object | *required* |

Returns:

| Type | Description | | --- | --- | | | a string in a notation usable by the DiagrammeR package. |

Examples:

TODO

Source code in `.venv/lib/python3.13/site-packages/swift2/doc_helper.py`

```
def get_catchment_dot_graph(simulation):
    """
    Gets a catchment representation in Graphviz DOT format

    Gets a catchment representation in Graphviz DOT format

    Args:
        simulation (Simulation): A swift simulation object

    Returns:
        a string in a notation usable by the DiagrammeR package.

    Examples:
        TODO

    """
    # Examples:
    # >>> # library(swift)
    # >>> # library('DiagrammeR')
    # >>> # dataId <- 'MMH'
    # >>> # simulation <- createTestCatchment(nSubareas=4, dataId=dataId, varNameDataRain='rain', varNameDataPet='evap')
    # >>> # DiagrammeR(getCatchmentDotGraph(simulation))
    return swg.GetCatchmentDOTGraph_py(simulation)

```

## `get_free_params(model_id)`

Get a default parameter set for models

Get a default parameter set for models, as a data frame

Parameters:

| Name | Type | Description | Default | | --- | --- | --- | --- | | `model_id` | `Any` | an identifier for the model, e.g. 'GR5H' | *required* |

Returns:

| Type | Description | | --- | --- | | | a data frame with Min, Max, Value, Name |

Source code in `.venv/lib/python3.13/site-packages/swift2/doc_helper.py`

```
def get_free_params(model_id):
    """
    Get a default parameter set for models

    Get a default parameter set for models, as a data frame

    Args:
        model_id (Any): an identifier for the model, e.g. 'GR5H'

    Returns:
        a data frame with Min, Max, Value, Name

    """
    pSpec = None
    if model_id == "GR5H":
        pSpec = _df_from_dict(
            Name=["x1", "x2", "x3", "x4", "x5"],
            Value=_npf([44.6, 30.0, 10.0, 14.0, 200.0]),
            Min=_npf([1, 1, 0, 1, 1]),
            Max=_npf([1000, 400, 1000, 240, 1000.0]),
        )
    elif model_id == "GR6J":
        # per202 2014-09-25
        # I take some values for the parameters from the unit tests, but the min/max bounds are PURE guesses. Q/A TBC.
        pSpec = _df_from_dict(
            Name=["x1", "x2", "x3", "x4", "x5", "x6"],
            Value=_npf([20, -2, 10, 2, 0, 1]),
            Min=_npf([1, -5, 0, 1, 0, 0]),
            Max=_npf([1000, 400, 1000, 240, 1, 1]),
        )
    elif model_id == "PDM":
        # per202 2014-11-13
        #
        pSpec = _df_from_dict(
            Name=[
                "cmax",
                "cminrat",
                "b",
                "be",
                "kg",
                "bg",
                "Strat",
                "k1",
                "k2rat",
                "kb",
            ],
            Value=_npf([400, 0.5, 1.8, 1.0, 1300.0, 1.0, 0.5, 35.0, 0.3, 2.4]),
            Min=_npf([1, 0, 0.001, 1.0, 1.0, 1.0, 0.0, 1.0, 0.0001, 1.0]),
            Max=_npf([3000, 1, 2.0, 2.0, 50000.0, 1.0, 1.0, 300.0, 1.0000, 2000.0]),
        )
    elif model_id == "SAC" or model_id == "SACSMA":
        # rob635 2015-01-11
        #
        pSpec = _df_from_dict(
            Name=[
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
            Value=_npf(
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
                ]
            ),
            Min=_npf(
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
                ]
            ),
            Max=_npf(
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
                ]
            ),
        )
    elif model_id == "GR4J":
        # \\OSM-01-MEL.it.csiro.au\CLW_HYDROFORECAST_common\Projects\WIRADA_4_1\Work\2013_2014_Act2_Flood_Cal\SWIFT_hourly\C-F2+F3+F5\South_Esk\Output\Out_CaliPara.txt
        # \\OSM-01-MEL.it.csiro.au\CLW_HYDROFORECAST_common\Projects\WIRADA_4_1\Work\2013_2014_Act2_Flood_Cal\SWIFT_hourly\C-F2+F3+F5\South_Esk\Setup\Model_Parameters.txt
        pSpec = _df_from_dict(
            # Name                 X1             X2             X3             X4
            # Number                1              2              3              4
            # Fit(Y\N)              1              1              1              1
            # LowBound    1.00000E+00   -2.70000E+01    1.00000E+00    1.00000E+00
            # UpBound     3.00000E+03    2.70000E+01    6.60000E+02    2.40000E+02
            # #-Calibrated parameters-----------------------------------------------------------------
            # Chmt_001    6.50488E+02   -2.80648E-01    7.89123E+00    1.89172E+01
            Name=["x1", "x2", "x3", "x4"],
            Value=_npf([6.50488e02, -2.80648e-01, 7.89123e00, 1.89172e01]),
            Min=_npf([1, -27, 1, 1]),
            Max=_npf([3.00000e03, 2.70000e01, 6.60000e02, 2.40000e02]),
        )
    elif model_id == "SAC" or model_id == "SACSMA":
        # rob635 2015-01-11
        #
        pSpec = _df_from_dict(
            Name=[
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
            Value=_npf(
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
                ]
            ),
            Min=_npf(
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
                ]
            ),
            Max=_npf(
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
                ]
            ),
        )
    else:
        raise Exception("Model identifier not recognised: " + model_id)
    return pSpec

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

## `gr4j_scaled_parameteriser(reference_area=240, t_step_seconds=3600)`

Get a time step and area scaled parameterizer for the GR4 model structure

Get a time step and area scaled parameterizer for the GR4 model structure

Parameters:

| Name | Type | Description | Default | | --- | --- | --- | --- | | `reference_area` | `Any` | The reference area in km^2 for the parameter x4 | `240` | | `t_step_seconds` | `Any` | The simulation time step in seconds. | `3600` |

Returns:

| Type | Description | | --- | --- | | | A SWIFT catchment parameterizer for GR4 model structures |

Source code in `.venv/lib/python3.13/site-packages/swift2/doc_helper.py`

```
def gr4j_scaled_parameteriser(reference_area: float = 240, t_step_seconds: int = 3600):
    """
    Get a time step and area scaled parameterizer for the GR4 model structure

    Get a time step and area scaled parameterizer for the GR4 model structure

    Args:
        reference_area (Any): The reference area in km^2 for the parameter x4
        t_step_seconds (Any): The simulation time step in seconds.

    Returns:
        A SWIFT catchment parameterizer for GR4 model structures

    """
    return swg.CreateGr4ScaledParameterizer_py(reference_area, t_step_seconds)

```

## `inspect(simulation, element='link', id='1', full_names=False)`

Inspect an element of a catchment model

Inspect the current state values of an element of a catchment model

Parameters:

| Name | Type | Description | Default | | --- | --- | --- | --- | | `simulation` | `Simulation` | A swift simulation object | *required* | | `element` | `Any` | type of top level element, within c('link','node','subarea') | `'link'` | | `id` | `Any` | SWIFT simulation | `'1'` | | `full_names` | `Any` | if TRUE returns the full names of state variable ids (e.g. link.link_1.OutlfowRate) | `False` |

Returns:

| Type | Description | | --- | --- | | | named numeric vector, the current state values of the catchment model element |

Examples:

TODO

Source code in `.venv/lib/python3.13/site-packages/swift2/doc_helper.py`

```
def inspect(simulation: "Simulation", element="link", id="1", full_names=False):
    """
    Inspect an element of a catchment model

    Inspect the current state values of an element of a catchment model

    Args:
        simulation (Simulation): A swift simulation object
        element (Any): type of top level element, within c('link','node','subarea')
        id (Any): SWIFT simulation
        full_names (Any): if TRUE returns the full names of state variable ids (e.g. link.link_1.OutlfowRate)

    Returns:
        named numeric vector, the current state values of the catchment model element

    Examples:
        TODO
    """
    # Examples:
    #     >>> # ms <- createTestCatchmentStructure()$model
    #     >>> # inspect(ms, element='link', id='lnk1')
    #     >>> # inspect(ms, element='subarea', id='lnk1')
    #     >>> # inspect(ms, element='subarea', id='lnk1', fullNames=TRUE)
    all_f_ids = get_variable_ids(simulation, mk_full_data_id(element, id), full_id=True)
    all_f_ids = np.sort([s for s in set(all_f_ids)])
    x = get_state_value(simulation, all_f_ids)

    def last_in_vec(v):
        if len(v) > 0:
            return v[-1]
        else:
            return ""

    if not full_names:
        new_k = dict([(k, last_in_vec(k.split("."))) for k in x.keys()])
        # if len(new_k) != len(set(new_k)): raise Exception()
        new_x = dict([(new_k[k], x[k]) for k in x.keys()])
        x = new_x
    return x

```

## `is_common_iterable(obj)`

True if an object is iterable but not a string (str)

Source code in `.venv/lib/python3.13/site-packages/swift2/utils.py`

```
def is_common_iterable(obj: Any) -> bool:
    """True if an object is iterable but not a string (str)"""
    if isinstance(obj, str):
        return False
    # if isinstance(obj, np.ndarray) and obj.size == 1:
    #     return False # otherwise likely to get error "len() of unsized object"
    return hasattr(type(obj), "__iter__")

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

## `paste0(*lists, collapse=None)`

Port of R paste0 function

Source code in `.venv/lib/python3.13/site-packages/swift2/utils.py`

```
def paste0(*lists, collapse=None):
    """Port of R paste0 function"""
    return paste(*lists, sep="", collapse=collapse)

```

## `play_subarea_input(simulation, input, subarea_name, input_name)`

Sets time series as input to a simulation

Sets time series as input to a simulation

Parameters:

| Name | Type | Description | Default | | --- | --- | --- | --- | | `simulation` | `Simulation` | A swift simulation object | *required* | | `input` | `Any` | an xts time series. | *required* | | `subarea_name` | `Any` | a valid name of the subarea | *required* | | `input_name` | `Any` | the name of the input variable to the model (i.e. 'P' for the precip of GR5H) | *required* |

Source code in `.venv/lib/python3.13/site-packages/swift2/play_record.py`

```
def play_subarea_input(simulation: "Simulation", input, subarea_name, input_name):
    """
    Sets time series as input to a simulation

    Sets time series as input to a simulation

    Args:
        simulation (Simulation): A swift simulation object
        input (Any): an xts time series.
        subarea_name (Any): a valid name of the subarea
        input_name (Any): the name of the input variable to the model (i.e. 'P' for the precip of GR5H)

    """
    play_input(simulation, input, _mkid("subarea", subarea_name, input_name))

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

## `sample_catchment_model(site_id='South_Esk', config_id='catchment')`

Deserialize a basic catchment structure from the package sample data

Deserialize a basic catchment structure from the package sample data. This function is mostly for documentation purposes.

Parameters:

| Name | Type | Description | Default | | --- | --- | --- | --- | | `site_id` | `Any` | a site identifier | `'South_Esk'` | | `config_id` | `Any` | a variable identifier for a model structure valid for the given site_id | `'catchment'` |

Returns:

| Type | Description | | --- | --- | | | a model simulation |

Source code in `.venv/lib/python3.13/site-packages/swift2/doc_helper.py`

```
def sample_catchment_model(site_id="South_Esk", config_id="catchment"):
    """
    Deserialize a basic catchment structure from the package sample data

    Deserialize a basic catchment structure from the package sample data. This function is mostly for documentation purposes.

    Args:
        site_id (Any): a site identifier
        config_id (Any): a variable identifier for a model structure valid for the given site_id

    Returns:
        a model simulation

    """
    # if not exists('swiftSampleData')) data(swift_sample_data)
    s = _sample_data()
    site_data: Dict = s[site_id]
    if config_id not in site_data.keys():
        raise ValueError(
            "Sample catchment model for site "
            + site_id
            + " identified by "
            + config_id
            + " not found"
        )
    cat_structure = site_data[config_id]
    return create_catchment_model_from_structure(cat_structure)

```

## `sample_series(site_id='MMH', var_name='rain')`

Deserialize information to a UTC time series

Deserialize information to a UTC time series. This function is overcoming some behaviors in saving/loading xts series to/from binary RData format. Usage is not intended for most users.

Parameters:

| Name | Type | Description | Default | | --- | --- | --- | --- | | `site_id` | `Any` | a site identifier | `'MMH'` | | `var_name` | `Any` | a variable identifier valid for the given site_id | `'rain'` |

Returns:

| Type | Description | | --- | --- | | | an xts time series with UTC time indexing |

Source code in `.venv/lib/python3.13/site-packages/swift2/doc_helper.py`

```
def sample_series(site_id="MMH", var_name="rain"):
    """
    Deserialize information to a UTC time series

    Deserialize information to a UTC time series. This function is overcoming some behaviors in saving/loading xts series to/from binary RData format. Usage is not intended for most users.

    Args:
        site_id (Any): a site identifier
        var_name (Any): a variable identifier valid for the given site_id

    Returns:
        an xts time series with UTC time indexing

    """
    s = _sample_data()
    siteData = s[site_id]
    if var_name not in siteData.keys():
        keys = list(siteData.keys())
        kstring = ', '.join(keys)
        raise KeyError(f"key {var_name} not found. Valid keys are {kstring}")
    varData = siteData[var_name]
    # if (varData)) stop(paste('Sample data for site', site_id, 'and variable name', var_name, 'not found'))
    return deserialise_sample_series(varData)

```

## `sce_parameter(nparams, nshuffle=40)`

Create SCE parameters suited for a given number of parameters.

Parameters:

| Name | Type | Description | Default | | --- | --- | --- | --- | | `nparams` | `int` | number of free model parameters | *required* | | `nshuffle` | `int` | maximum number of shuffles to do, if no other termination criterion. Defaults to 40. | `40` |

Returns:

| Type | Description | | --- | --- | | `Dict[str, float]` | Dict\[str,float\]: SCE hyperparameters |

Source code in `.venv/lib/python3.13/site-packages/swift2/doc_helper.py`

```
def sce_parameter(nparams: int, nshuffle: int = 40) -> Dict[str, float]:
    """Create SCE parameters suited for a given number of parameters.

    Args:
        nparams (int): number of free model parameters
        nshuffle (int, optional): maximum number of shuffles to do, if no other termination criterion. Defaults to 40.

    Returns:
        Dict[str,float]: SCE hyperparameters
    """
    sce_params = get_default_sce_parameters()
    sce_params["P"] = nparams + 2
    sce_params["Pmin"] = nparams + 2
    sce_params["M"] = 2 * nparams + 1
    sce_params["Q"] = max(sce_params["M"] - 2, 2)
    sce_params["NumShuffle"] = nshuffle
    return sce_params

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

## `set_loglik_param_keys(a='a', b='b', m='m', s='s', maxobs='maxobs', ct='ct', censopt='CensOpt')`

Specify the global parameter names to use in the log-likelihood calculation

Specify the global parameter names to use in the log-likelihood calculation. Consequence of prehistoric legacy.

Parameters:

| Name | Type | Description | Default | | --- | --- | --- | --- | | `a` | `str` | the name of the a parameter | `'a'` | | `b` | `str` | the name of the b parameter | `'b'` | | `m` | `str` | the name of the m parameter | `'m'` | | `s` | `str` | the name of the s parameter | `'s'` | | `maxobs` | `str` | the name of the maxobs parameter | `'maxobs'` | | `ct` | `str` | the name of the ct parameter | `'ct'` | | `censopt` | `str` | the name of the censopt parameter | `'CensOpt'` |

Examples:

TODO

Source code in `.venv/lib/python3.13/site-packages/swift2/doc_helper.py`

```
def set_loglik_param_keys(
    a="a", b="b", m="m", s="s", maxobs="maxobs", ct="ct", censopt="CensOpt"
):
    """
    Specify the global parameter names to use in the log-likelihood calculation

    Specify the global parameter names to use in the log-likelihood calculation. Consequence of prehistoric legacy.

    Args:
        a (str): the name of the a parameter
        b (str): the name of the b parameter
        m (str): the name of the m parameter
        s (str): the name of the s parameter
        maxobs (str): the name of the maxobs parameter
        ct (str): the name of the ct parameter
        censopt (str): the name of the censopt parameter

    Examples:
        TODO
    """
    # Examples:
    #     >>> # set_loglik_param_keys('lambda', 'epsilon', 'm', 's')
    #     >>> # pSpecGr4j = get_free_params('GR4J')
    #     >>> # # pSpecGr4j$Value = c(542.1981111, -0.4127542, 7.7403390, 1.2388548)
    #     >>> # # pSpecGr4j$Min = c(1,-30, 1,1)
    #     >>> # # pSpecGr4j$Max = c(3000, 30, 1000, 240)
    #     >>> # # pSpecGr4j$Name = paste0(rootId, pSpecGr4j$Name)
    #     >>> # pgr4 = create_parameterizer(type='Generic', specs=pSpecGr4j)
    #     >>> # p = create_parameterizer(type='log-likelihood')
    #     >>> # p.add("epsilon", -30, 0, -7)
    #     >>> # p.add("m", 0, 0, 0)
    #     >>> # p.add("s", 1, 1000, 100)
    #     >>> # p.add("lambda", -30, 1, -10)
    #     >>> # parameterizer = concatenate_parameterisers(pgr4, p)
    #     >>> # print(parameterizer)
    swg.SetLogLikelihoodVariableNames_py(a, b, m, s, maxobs, ct, censopt)

```

## `set_sample_data(model_sim, site_id='MMH', rain_data_var='rain', evap_data_var='evap', rain_model_var='P', evap_model_var='E', t_step='daily')`

Sets sample input data into a model simulation

Sets input data from the included sample data into a model simulation

Parameters:

| Name | Type | Description | Default | | --- | --- | --- | --- | | `model_sim` | `Any` | an S4 object 'ExternalObjRef' [package "cinterop"] with external pointer type "MODEL_SIMULATION_PTR" | *required* | | `site_id` | `Any` | sample data site identifier | `'MMH'` | | `rain_data_var` | `Any` | time series ID for the rainfall in the sample data | `'rain'` | | `evap_data_var` | `Any` | time series ID for the evaporation in the sample data | `'evap'` | | `rain_model_var` | `Any` | sub-area runoff model state identifier for the rainfall, e.g. 'P' | `'P'` | | `evap_model_var` | `Any` | sub-area runoff model state identifier for the evaporation, e.g. 'E' | `'E'` | | `t_step` | `Any` | identifier for the time step to set the simulation to. | `'daily'` |

Source code in `.venv/lib/python3.13/site-packages/swift2/doc_helper.py`

```
def set_sample_data(
    model_sim,
    site_id="MMH",
    rain_data_var="rain",
    evap_data_var="evap",
    rain_model_var="P",
    evap_model_var="E",
    t_step="daily",
):
    """
    Sets sample input data into a model simulation

    Sets input data from the included sample data into a model simulation

    Args:
        model_sim (Any): an S4 object 'ExternalObjRef' [package "cinterop"] with external pointer type "MODEL_SIMULATION_PTR"
        site_id (Any): sample data site identifier
        rain_data_var (Any): time series ID for the rainfall in the sample data
        evap_data_var (Any): time series ID for the evaporation in the sample data
        rain_model_var (Any): sub-area runoff model state identifier for the rainfall, e.g. 'P'
        evap_model_var (Any): sub-area runoff model state identifier for the evaporation, e.g. 'E'
        t_step (Any): identifier for the time step to set the simulation to.

    """

    rain = sample_series(site_id, var_name=rain_data_var)
    evap = sample_series(site_id, var_name=evap_data_var)
    sa_ids = get_subarea_ids(model_sim)
    for sa_id in sa_ids:
        play_subarea_input(model_sim, rain, sa_id, rain_model_var)
        play_subarea_input(model_sim, evap, sa_id, evap_model_var)
    set_simulation_time_step(model_sim, t_step)
    set_simulation_span(model_sim, start_ts(rain), end_ts(rain))

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

## `short_var_id(var_ids)`

Shorten long model variable identifiers to the short model variable name

Shorten long model variable identifiers to the short model variable name. This is useful for instance to prepare time series names for multi-plot displays.

Parameters:

| Name | Type | Description | Default | | --- | --- | --- | --- | | `var_ids` | `Any` | character vector | *required* |

Returns:

| Type | Description | | --- | --- | | `VecStr` | the short model variable identifiers |

Examples:

```
>>> short_var_id('elementtype|elementname|varid')
>>> short_var_id('elementtype.elementname.varid')

```

Source code in `.venv/lib/python3.13/site-packages/swift2/doc_helper.py`

```
def short_var_id(var_ids: "VecStr") -> "VecStr":
    """
    Shorten long model variable identifiers to the short model variable name

    Shorten long model variable identifiers to the short model variable name. This is useful for instance to prepare time series names for multi-plot displays.

    Args:
        var_ids (Any): character vector

    Returns:
        the short model variable identifiers

    Examples:
        >>> short_var_id('elementtype|elementname|varid')
        >>> short_var_id('elementtype.elementname.varid')

    """
    if is_common_iterable(var_ids):
        return [short_var_id(v) for v in var_ids]
    else:
        return var_ids.split("|")[-1].split["."][-1]

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
