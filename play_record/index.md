# Module play_record

## `get_played(simulation, var_ids=None, start_time=None, end_time=None)`

Retrieves a played time series from a simulation

Retrieves a played time series from a simulation.

Parameters:

| Name | Type | Description | Default | | --- | --- | --- | --- | | `simulation` | `Simulation` | A swift simulation object | *required* | | `var_ids` | `Any` | name of the output variable played to a time series. 'Catchment|StreamflowRate'. If missing, a multivariate time series of all played states is returned; this may be a large amount of data. | `None` | | `start_time` | `Any` | An optional parameter, the start of a period to subset the time series | `None` | | `end_time` | `Any` | An optional parameter, the end of a period to subset the time series | `None` |

Returns:

| Type | Description | | --- | --- | | | an xts time series, possibly multivariate. |

Source code in `swift2/play_record.py`

```
def get_played(simulation: "Simulation", var_ids=None, start_time=None, end_time=None):
    """
    Retrieves a played time series from a simulation

    Retrieves a played time series from a simulation.

    Args:
        simulation (Simulation): A swift simulation object
        var_ids (Any): name of the output variable played to a time series. 'Catchment|StreamflowRate'. If missing, a multivariate time series of all played states is returned; this may be a large amount of data.
        start_time (Any): An optional parameter, the start of a period to subset the time series
        end_time (Any): An optional parameter, the end of a period to subset the time series

    Returns:
        an xts time series, possibly multivariate.

    """

    series = None
    if var_ids is None:
        var_ids = get_played_varnames(simulation)
    series = si.internal_get_played_tts(simulation, var_ids)
    return si.get_ts_window(series, start_time, end_time)

```

## `get_played_varnames(simulation)`

Gets all the names of states fed an input time series

Gets all the names of states fed an input time series

Parameters:

| Name | Type | Description | Default | | --- | --- | --- | --- | | `simulation` | `Simulation` | A swift simulation object | *required* |

Returns:

| Type | Description | | --- | --- | | | The names of the state variables fed over the simulation with values from a time series |

Source code in `swift2/play_record.py`

```
def get_played_varnames(simulation):
    """
    Gets all the names of states fed an input time series

    Gets all the names of states fed an input time series

    Args:
        simulation (Simulation): A swift simulation object

    Returns:
        The names of the state variables fed over the simulation with values from a time series

    """
    return swg.GetPlayedVariableNames_py(simulation)

```

## `get_recorded(simulation, var_ids=None, start_time=None, end_time=None)`

Retrieves a recorded time series from a simulation

Retrieves a recorded time series from a simulation.

Parameters:

| Name | Type | Description | Default | | --- | --- | --- | --- | | `simulation` | `Simulation` | A swift simulation object | *required* | | `var_ids` | `Any` | name of the output variable recorded to a time series. 'Catchment|StreamflowRate'. If missing, a multivariate time series of all recorded states is returned; this may be a large amount of data. | `None` | | `start_time` | `Any` | An optional parameter, the start of a period to subset the time series | `None` | | `end_time` | `Any` | An optional parameter, the end of a period to subset the time series | `None` |

Returns:

| Type | Description | | --- | --- | | | an xts time series, possibly multivariate. |

Source code in `swift2/play_record.py`

```
def get_recorded(
    simulation: "Simulation", var_ids=None, start_time=None, end_time=None
):
    """
    Retrieves a recorded time series from a simulation

    Retrieves a recorded time series from a simulation.

    Args:
        simulation (Simulation): A swift simulation object
        var_ids (Any): name of the output variable recorded to a time series. 'Catchment|StreamflowRate'. If missing, a multivariate time series of all recorded states is returned; this may be a large amount of data.
        start_time (Any): An optional parameter, the start of a period to subset the time series
        end_time (Any): An optional parameter, the end of a period to subset the time series

    Returns:
        an xts time series, possibly multivariate.

    """
    if si.is_ensemble_forecast_simulation(simulation):
        return get_recorded_ensemble_forecast(simulation, var_ids, start_time, end_time)
    else:
        series = None
        if var_ids is None:
            var_ids = get_recorded_varnames(simulation)
        series = si.internal_get_recorded_tts(simulation, var_ids)
        return si.get_ts_window(series, start_time, end_time)

```

## `get_recorded_ensemble_forecast(simulation, var_id, start_time=None, end_time=None)`

Retrieves a recorded time series from a simulation

Retrieves a recorded time series from a simulation.

Parameters:

| Name | Type | Description | Default | | --- | --- | --- | --- | | `simulation` | `Simulation` | A swift simulation object | *required* | | `var_ids` | `Any` | name of the output variable recorded to a time series. 'Catchment|StreamflowRate'. If missing, a multivariate time series of all recorded states is returned; this may be a large amount of data. | *required* | | `start_time` | `Any` | NOT USED YET An optional parameter, the start of a period to subset the time series | `None` | | `end_time` | `Any` | NOT USED YET An optional parameter, the end of a period to subset the time series | `None` |

Returns:

| Type | Description | | --- | --- | | | an xts time series, possibly multivariate. |

Source code in `swift2/play_record.py`

```
def get_recorded_ensemble_forecast(
    simulation, var_id: str, start_time=None, end_time=None
):
    """
    Retrieves a recorded time series from a simulation

    Retrieves a recorded time series from a simulation.

    Args:
        simulation (Simulation): A swift simulation object
        var_ids (Any): name of the output variable recorded to a time series. 'Catchment|StreamflowRate'. If missing, a multivariate time series of all recorded states is returned; this may be a large amount of data.
        start_time (Any): NOT USED YET An optional parameter, the start of a period to subset the time series
        end_time (Any): NOT USED YET An optional parameter, the end of a period to subset the time series

    Returns:
        an xts time series, possibly multivariate.

    """
    si.check_ensemble_forecast_simulation(simulation)
    return swg.GetRecordedEnsembleForecastTimeSeries_py(simulation, var_id)

```

## `get_recorded_varnames(simulation)`

Gets all the names of the recorded states

Gets all the names of the recorded states

Parameters:

| Name | Type | Description | Default | | --- | --- | --- | --- | | `simulation` | `Simulation` | A swift simulation object | *required* |

Returns:

| Type | Description | | --- | --- | | | The names of the state variables being recorded into time series |

Source code in `swift2/play_record.py`

```
def get_recorded_varnames(simulation):
    """
    Gets all the names of the recorded states

    Gets all the names of the recorded states

    Args:
        simulation (Simulation): A swift simulation object

    Returns:
        The names of the state variables being recorded into time series

    """
    return swg.GetRecordedVariableNames_py(simulation)

```

## `play_ensemble_forecast_input(simulation, input_ts, var_id)`

Sets time series as input to a simulation

Sets time series as input to a simulation

Parameters:

| Name | Type | Description | Default | | --- | --- | --- | --- | | `simulation` | `Any` | an S4 object 'ExternalObjRef' [package "cinterop"] with external pointer type "ENSEMBLE_FORECAST_SIMULATION_PTR" | *required* | | `input_ts` | `Any` | an S4 object 'ExternalObjRef' [package "cinterop"] with external pointer type "ENSEMBLE_FORECAST_TIME_SERIES_PTR" | *required* | | `var_id` | `Any` | character of length one, the variable identifier to use | *required* |

Source code in `swift2/play_record.py`

```
def play_ensemble_forecast_input(
    simulation: "EnsembleForecastSimulation",
    input_ts: "EnsembleForecastTimeSeries",
    var_id: str,
) -> None:
    """
    Sets time series as input to a simulation

    Sets time series as input to a simulation

    Args:
        simulation (Any): an S4 object 'ExternalObjRef' [package "cinterop"] with external pointer type "ENSEMBLE_FORECAST_SIMULATION_PTR"
        input_ts (Any): an S4 object 'ExternalObjRef' [package "cinterop"] with external pointer type "ENSEMBLE_FORECAST_TIME_SERIES_PTR"
        var_id (Any): character of length one, the variable identifier to use

    """
    si.check_ensemble_forecast_simulation(simulation)
    si.check_ensemble_forecast_time_series(input_ts)
    assert isinstance(var_id, str)
    swg.PlayEnsembleForecastTimeSeries_py(simulation, input_ts, var_id)

```

## `play_input(simulation, input_ts, var_ids=None)`

Sets time series as input to a simulation

Sets time series as input to a simulation

Parameters:

| Name | Type | Description | Default | | --- | --- | --- | --- | | `simulation` | `Simulation` | A swift simulation object | *required* | | `input_ts` | `Any` | an xts time series, or an S4 object 'ExternalObjRef' [package "cinterop"] with external pointer type "ENSEMBLE_FORECAST_TIME_SERIES_PTR". if an xts time series column names must be valid model variable identifiers, unless explicitely provided via varIds | *required* | | `var_ids` | `Any` | optional character, the variable identifiers to use, overriding the column names of the inputTs. If not NULL, must be of length equal to the number of columns in inputTs | `None` |

Source code in `swift2/play_record.py`

```
def play_input(
    simulation: "NdSimulation", input_ts: "TimeSeriesLike", var_ids: VecStr = None
) -> None:
    """
    Sets time series as input to a simulation

    Sets time series as input to a simulation

    Args:
        simulation (Simulation): A swift simulation object
        input_ts (Any): an xts time series, or an S4 object 'ExternalObjRef' [package "cinterop"] with external pointer type "ENSEMBLE_FORECAST_TIME_SERIES_PTR". if an xts time series column names must be valid model variable identifiers, unless explicitely provided via varIds
        var_ids (Any): optional character, the variable identifiers to use, overriding the column names of the inputTs. If not NULL, must be of length equal to the number of columns in inputTs

    """
    if si.is_ensemble_forecast_simulation(
        simulation
    ) and si.is_ensemble_forecast_time_series(input_ts):
        play_ensemble_forecast_input(simulation, input_ts, var_ids)
    elif si.is_ensemble_simulation(
        simulation
    ):  # ??? and si.is_ensemble_forecast_time_series(input_ts):
        raise NotImplementedError("play input into ensemble simulation not supported")
    # } else {
    # stopifnot(is.xts(input_ts))
    else:
        play_singular_simulation(simulation, input_ts, var_ids)

```

## `play_inputs(simulation, data_library, model_var_id, data_id, resample='')`

Assign input time series from a time series library to a model simulation

Parameters:

| Name | Type | Description | Default | | --- | --- | --- | --- | | `simulation` | `Simulation` | A swift simulation object | *required* | | `data_library` | `TimeSeriesLibrary` | external pointer type ENSEMBLE_DATA_SET_PTR, or a Python class wrapper around it | *required* | | `model_var_id` | `str or sequence of str` | model state variable unique identifier(s) | *required* | | `data_id` | `str or sequence of str` | identifier(s) for data in the data_library. If length is not the same as model_var_id, the elements of data_id are reused to match it | *required* | | `resample` | `str or sequence of str` | identifier(s) for how the series is resampled (aggregated or disaggregated). If length is not the same as model_var_id, the elements of resample are reused to match it | `''` |

Source code in `swift2/play_record.py`

```
def play_inputs(
    simulation: "Simulation", data_library:uc.TimeSeriesLibrary, model_var_id:"VecStr", data_id:"VecStr", resample:"VecStr"=""
):
    """
    Assign input time series from a time series library to a model simulation

    Args:
        simulation (Simulation): A swift simulation object
        data_library (TimeSeriesLibrary): external pointer type ENSEMBLE_DATA_SET_PTR, or a Python class wrapper around it 
        model_var_id (str or sequence of str): model state variable unique identifier(s)
        data_id (str or sequence of str): identifier(s) for data in the data_library. If length is not the same as model_var_id, the elements of data_id are reused to match it
        resample (str or sequence of str): identifier(s) for how the series is resampled (aggregated or disaggregated). If length is not the same as model_var_id, the elements of resample are reused to match it

    """
    # model_var_id <- as.character(model_var_id)
    # data_id <- as.character(data_id)
    # resample <- as.character(resample)
    # TODO: match the behavior of R, perhaps.
    assert len(model_var_id) == len(data_id)
    assert len(model_var_id) == len(resample)
    # if(len(model_var_id) != len(data_id)):
    #     # warning('Reusing argument `data_id` to match length of `model_var_id`')
    #     data_id = np.repeat(data_id, length.out=length(model_var_id))

    # if(length(resample)!=length(model_var_id)) {
    # if(length(resample) != 1 || resample[1] != '') warning('Reusing argument `resample` to match the length of `model_var_id`')
    # resample <- rep(resample, length.out=length(model_var_id))
    # }
    swg.PlayDatasetInputs_py(
        simulation, data_library, model_var_id, data_id, resample, len(model_var_id)
    )

```

## `play_subarea_input(simulation, input, subarea_name, input_name)`

Sets time series as input to a simulation

Sets time series as input to a simulation

Parameters:

| Name | Type | Description | Default | | --- | --- | --- | --- | | `simulation` | `Simulation` | A swift simulation object | *required* | | `input` | `Any` | an xts time series. | *required* | | `subarea_name` | `Any` | a valid name of the subarea | *required* | | `input_name` | `Any` | the name of the input variable to the model (i.e. 'P' for the precip of GR5H) | *required* |

Source code in `swift2/play_record.py`

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

## `record_state(simulation, var_ids=CATCHMENT_FLOWRATE_VARID, recording_provider=None, data_ids=None)`

Record a time series of one of the state of the model

Record a time series of one of the state of the model

Parameters:

| Name | Type | Description | Default | | --- | --- | --- | --- | | `simulation` | `Any` | an S4 object 'ExternalObjRef' [package "cinterop"] with external pointer type "MODEL_SIMULATION_PTR", "ENSEMBLE_SIMULATION_PTR" or "ENSEMBLE_FORECAST_SIMULATION_PTR" | *required* | | `var_ids` | `VecStr` | identifier(s) of the output variable recorded to a time series, e.g. 'Catchment|StreamflowRate' or 'subcatchment.Subarea.runoff'. Defaults to CATCHMENT_FLOWRATE_VARID. | `CATCHMENT_FLOWRATE_VARID` | | `recording_provider` | `TimeSeriesLibrary` | description. Defaults to None. | `None` | | `data_ids` | `VecStr` | description. Defaults to None. | `None` |

Raises:

| Type | Description | | --- | --- | | `ValueError` | description |

Source code in `swift2/play_record.py`

```
def record_state(
    simulation,
    var_ids: VecStr = CATCHMENT_FLOWRATE_VARID,
    recording_provider: "TimeSeriesLibrary" = None,
    data_ids: "VecStr" = None,
):
    """
    Record a time series of one of the state of the model

    Record a time series of one of the state of the model

    Args:
        simulation (Any): an S4 object 'ExternalObjRef' [package "cinterop"] with external pointer type "MODEL_SIMULATION_PTR", "ENSEMBLE_SIMULATION_PTR" or "ENSEMBLE_FORECAST_SIMULATION_PTR"
        var_ids (VecStr, optional): identifier(s) of the output variable recorded to a time series, e.g. 'Catchment|StreamflowRate' or 'subcatchment.Subarea.runoff'. Defaults to CATCHMENT_FLOWRATE_VARID.
        recording_provider (TimeSeriesLibrary, optional): _description_. Defaults to None.
        data_ids (VecStr, optional): _description_. Defaults to None.

    Raises:
        ValueError: _description_
    """
    # checkRecordingConsistency(var_ids, recording_provider, data_ids)
    # var_ids <- as.character(var_ids)
    # data_ids <- as.character(data_ids)
    # recordSingularState(simulation, var_ids, recording_provider, data_ids)Err
    if si.is_ensemble_forecast_simulation(simulation):
        record_ensemble_forecast_state(
            simulation, var_ids, recording_provider, data_ids
        )
    elif si.is_ensemble_simulation(simulation):
        record_ensemble_state(simulation, var_ids, recording_provider, data_ids)
    elif si.is_singular_simulation(simulation):
        record_singular_state(simulation, var_ids, recording_provider, data_ids)
    else:
        raise ValueError("Unknown type of simulation")

```
