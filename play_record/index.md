# Module play_record

# play_record

Functions:

- **`apply_recording_function`** –
- **`get_all_played`** –
- **`get_all_recorded`** –
- **`get_played`** – Retrieves a played time series from a simulation
- **`get_played_varnames`** – Gets all the names of states fed an input time series
- **`get_recorded`** – Retrieves a recorded time series from a simulation
- **`get_recorded_ensemble_forecast`** – Retrieves a recorded time series from a simulation
- **`get_recorded_varnames`** – Gets all the names of the recorded states
- **`play_ensemble_forecast_input`** – Sets time series as input to a simulation
- **`play_input`** – Sets time series as input to a simulation
- **`play_inputs`** – Assign input time series from a time series library to a model simulation
- **`play_singular_simulation`** –
- **`play_subarea_input`** – Sets time series as input to a simulation
- **`record_ensemble_forecast_state`** –
- **`record_ensemble_state`** –
- **`record_singular_state`** –
- **`record_state`** – Record a time series of one of the state of the model
- **`remove_recorded`** –
- **`remove_singular_played_input`** –

## apply_recording_function

```
apply_recording_function(simulation: Simulation, recording_func: Optional[RecordToSignature], var_ids: VecStr, recording_provider, data_ids)
```

## get_all_played

```
get_all_played(simulation)
```

## get_all_recorded

```
get_all_recorded(simulation)
```

## get_played

```
get_played(simulation: Simulation, var_ids=None, start_time=None, end_time=None)
```

Retrieves a played time series from a simulation

Retrieves a played time series from a simulation.

Parameters:

- **`simulation`** (`Simulation`) – A swift simulation object
- **`var_ids`** (`Any`, default: `None` ) – name of the output variable played to a time series. 'Catchment|StreamflowRate'. If missing, a multivariate time series of all played states is returned; this may be a large amount of data.
- **`start_time`** (`Any`, default: `None` ) – An optional parameter, the start of a period to subset the time series
- **`end_time`** (`Any`, default: `None` ) – An optional parameter, the end of a period to subset the time series

Returns:

- – an xts time series, possibly multivariate.

## get_played_varnames

```
get_played_varnames(simulation)
```

Gets all the names of states fed an input time series

Gets all the names of states fed an input time series

Parameters:

- **`simulation`** (`Simulation`) – A swift simulation object

Returns:

- – The names of the state variables fed over the simulation with values from a time series

## get_recorded

```
get_recorded(simulation: Simulation, var_ids=None, start_time=None, end_time=None)
```

Retrieves a recorded time series from a simulation

Retrieves a recorded time series from a simulation.

Parameters:

- **`simulation`** (`Simulation`) – A swift simulation object
- **`var_ids`** (`Any`, default: `None` ) – name of the output variable recorded to a time series. 'Catchment|StreamflowRate'. If missing, a multivariate time series of all recorded states is returned; this may be a large amount of data.
- **`start_time`** (`Any`, default: `None` ) – An optional parameter, the start of a period to subset the time series
- **`end_time`** (`Any`, default: `None` ) – An optional parameter, the end of a period to subset the time series

Returns:

- – an xts time series, possibly multivariate.

## get_recorded_ensemble_forecast

```
get_recorded_ensemble_forecast(simulation, var_id: str, start_time=None, end_time=None)
```

Retrieves a recorded time series from a simulation

Retrieves a recorded time series from a simulation.

Parameters:

- **`simulation`** (`Simulation`) – A swift simulation object
- **`var_ids`** (`Any`) – name of the output variable recorded to a time series. 'Catchment|StreamflowRate'. If missing, a multivariate time series of all recorded states is returned; this may be a large amount of data.
- **`start_time`** (`Any`, default: `None` ) – NOT USED YET An optional parameter, the start of a period to subset the time series
- **`end_time`** (`Any`, default: `None` ) – NOT USED YET An optional parameter, the end of a period to subset the time series

Returns:

- – an xts time series, possibly multivariate.

## get_recorded_varnames

```
get_recorded_varnames(simulation)
```

Gets all the names of the recorded states

Gets all the names of the recorded states

Parameters:

- **`simulation`** (`Simulation`) – A swift simulation object

Returns:

- – The names of the state variables being recorded into time series

## play_ensemble_forecast_input

```
play_ensemble_forecast_input(simulation: EnsembleForecastSimulation, input_ts: EnsembleForecastTimeSeries, var_id: str) -> None
```

Sets time series as input to a simulation

Sets time series as input to a simulation

Parameters:

- **`simulation`** (`Any`) – an S4 object 'ExternalObjRef' [package "cinterop"] with external pointer type "ENSEMBLE_FORECAST_SIMULATION_PTR"
- **`input_ts`** (`Any`) – an S4 object 'ExternalObjRef' [package "cinterop"] with external pointer type "ENSEMBLE_FORECAST_TIME_SERIES_PTR"
- **`var_id`** (`Any`) – character of length one, the variable identifier to use

## play_input

```
play_input(simulation: NdSimulation, input_ts: TimeSeriesLike, var_ids: VecStr = None) -> None
```

Sets time series as input to a simulation

Sets time series as input to a simulation

Parameters:

- **`simulation`** (`Simulation`) – A swift simulation object
- **`input_ts`** (`Any`) – an xts time series, or an S4 object 'ExternalObjRef' [package "cinterop"] with external pointer type "ENSEMBLE_FORECAST_TIME_SERIES_PTR". if an xts time series column names must be valid model variable identifiers, unless explicitely provided via varIds
- **`var_ids`** (`Any`, default: `None` ) – optional character, the variable identifiers to use, overriding the column names of the inputTs. If not NULL, must be of length equal to the number of columns in inputTs

## play_inputs

```
play_inputs(simulation: Simulation, data_library: TimeSeriesLibrary, model_var_id: VecStr, data_id: VecStr, resample: VecStr = '')
```

Assign input time series from a time series library to a model simulation

Parameters:

- **`simulation`** (`Simulation`) – A swift simulation object
- **`data_library`** (`TimeSeriesLibrary`) – external pointer type ENSEMBLE_DATA_SET_PTR, or a Python class wrapper around it
- **`model_var_id`** (`str or sequence of str`) – model state variable unique identifier(s)
- **`data_id`** (`str or sequence of str`) – identifier(s) for data in the data_library. If length is not the same as model_var_id, the elements of data_id are reused to match it
- **`resample`** (`str or sequence of str`, default: `''` ) – identifier(s) for how the series is resampled (aggregated or disaggregated). If length is not the same as model_var_id, the elements of resample are reused to match it

## play_singular_simulation

```
play_singular_simulation(simulation, input_ts, var_ids)
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

## record_ensemble_forecast_state

```
record_ensemble_forecast_state(simulation: EnsembleForecastSimulation, var_ids: VecStr = CATCHMENT_FLOWRATE_VARID, recording_provider: TimeSeriesLibrary = None, data_ids: VecStr = None)
```

## record_ensemble_state

```
record_ensemble_state(simulation: EnsembleSimulation, var_ids: VecStr = CATCHMENT_FLOWRATE_VARID, recording_provider: TimeSeriesLibrary = None, data_ids: VecStr = None)
```

## record_singular_state

```
record_singular_state(simulation: Simulation, var_ids: VecStr = CATCHMENT_FLOWRATE_VARID, recording_provider: TimeSeriesLibrary = None, data_ids: VecStr = None)
```

## record_state

```
record_state(simulation, var_ids: VecStr = CATCHMENT_FLOWRATE_VARID, recording_provider: TimeSeriesLibrary = None, data_ids: VecStr = None)
```

Record a time series of one of the state of the model

Record a time series of one of the state of the model

Parameters:

- **`simulation`** (`Any`) – an S4 object 'ExternalObjRef' [package "cinterop"] with external pointer type "MODEL_SIMULATION_PTR", "ENSEMBLE_SIMULATION_PTR" or "ENSEMBLE_FORECAST_SIMULATION_PTR"
- **`var_ids`** (`VecStr`, default: `CATCHMENT_FLOWRATE_VARID` ) – identifier(s) of the output variable recorded to a time series, e.g. 'Catchment|StreamflowRate' or 'subcatchment.Subarea.runoff'. Defaults to CATCHMENT_FLOWRATE_VARID.
- **`recording_provider`** (`TimeSeriesLibrary`, default: `None` ) – description. Defaults to None.
- **`data_ids`** (`VecStr`, default: `None` ) – description. Defaults to None.

Raises:

- `ValueError` – description

## remove_recorded

```
remove_recorded(self, var_ids: VecStr) -> None
```

## remove_singular_played_input

```
remove_singular_played_input(self, var_ids: VecStr) -> None
```
