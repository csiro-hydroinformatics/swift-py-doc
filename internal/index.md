# Module internal

# internal

Functions:

- **`arg_error_swift_type`** –
- **`check_ensemble_forecast_simulation`** –
- **`check_ensemble_forecast_time_series`** –
- **`check_ensemble_simulation`** –
- **`check_singular_simulation`** –
- **`chk_date_time`** –
- **`get_ts_window`** –
- **`internal_get_played_tts`** –
- **`internal_get_recorded_tts`** –
- **`is_ensemble_forecast_simulation`** –
- **`is_ensemble_forecast_time_series`** –
- **`is_ensemble_simulation`** –
- **`is_singular_simulation`** –
- **`is_swift_ref`** –
- **`simplify_time_series`** – simplify a 1D time series object to a representation suitable for portable serialisation.
- **`to_interop_univariate_series`** – Convert an univariate python time series to a representation suitable for interoperability with a C API

Attributes:

- **`TS_INTEROP_GEOM_KEY`** –
- **`TS_INTEROP_VALUES_KEY`** –

## TS_INTEROP_GEOM_KEY

```
TS_INTEROP_GEOM_KEY = 'tsgeom'
```

## TS_INTEROP_VALUES_KEY

```
TS_INTEROP_VALUES_KEY = 'tsvalues'
```

## arg_error_swift_type

```
arg_error_swift_type(x, expected_type_id)
```

## check_ensemble_forecast_simulation

```
check_ensemble_forecast_simulation(s)
```

## check_ensemble_forecast_time_series

```
check_ensemble_forecast_time_series(s)
```

## check_ensemble_simulation

```
check_ensemble_simulation(s)
```

## check_singular_simulation

```
check_singular_simulation(s)
```

## chk_date_time

```
chk_date_time(series, dt, xr_func)
```

## get_ts_window

```
get_ts_window(series: DataArray, start_time, end_time)
```

## internal_get_played_tts

```
internal_get_played_tts(simulation: Simulation, var_ids: VecStr) -> Optional[DataArray]
```

## internal_get_recorded_tts

```
internal_get_recorded_tts(simulation: Simulation, var_ids: VecStr) -> Optional[DataArray]
```

## is_ensemble_forecast_simulation

```
is_ensemble_forecast_simulation(s)
```

## is_ensemble_forecast_time_series

```
is_ensemble_forecast_time_series(s)
```

## is_ensemble_simulation

```
is_ensemble_simulation(s)
```

## is_singular_simulation

```
is_singular_simulation(s)
```

## is_swift_ref

```
is_swift_ref(x, type: str)
```

## simplify_time_series

```
simplify_time_series(input_ts: TimeSeriesLike) -> Dict[str, Any]
```

simplify a 1D time series object to a representation suitable for portable serialisation.

Parameters:

- **`input_ts`** (`TimeSeriesLike`) – time series

Returns:

- `Dict[str, Any]` – Dict\[str,Any\]: dictionary with keys "tsgeom" for the time series geometry, and "tsvalues" for its values.

## to_interop_univariate_series

```
to_interop_univariate_series(ts: TimeSeriesLike, from_date: ConvertibleToTimestamp = None, to_date: ConvertibleToTimestamp = None) -> Tuple[ndarray, TimeSeriesGeometryNative]
```

Convert an univariate python time series to a representation suitable for interoperability with a C API

Parameters:

- **`ts`** (`TimeSeriesLike`) – Python native time series
- **`from_date`** (`ConvertibleToTimestamp`, default: `None` ) – start timestamp of the time series to subset to. Defaults to None.
- **`to_date`** (`ConvertibleToTimestamp`, default: `None` ) – end timestamp of the time series to subset to. Defaults to None.

Returns:

- `Tuple[ndarray, TimeSeriesGeometryNative]` – Tuple\[np.ndarray, TimeSeriesGeometryNative\]: univeriate data and time series geometry for interop.
