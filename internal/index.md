# Module internal

## `simplify_time_series(input_ts)`

simplify a 1D time series object to a representation suitable for portable serialisation.

Parameters:

| Name       | Type             | Description | Default    |
| ---------- | ---------------- | ----------- | ---------- |
| `input_ts` | `TimeSeriesLike` | time series | *required* |

Returns:

| Type             | Description                                                                                                 |
| ---------------- | ----------------------------------------------------------------------------------------------------------- |
| `Dict[str, Any]` | Dict\[str,Any\]: dictionary with keys "tsgeom" for the time series geometry, and "tsvalues" for its values. |

Source code in `swift2/internal.py`

```
def simplify_time_series(input_ts: TimeSeriesLike) -> Dict[str, Any]:
    """simplify a 1D time series object to a representation suitable for portable serialisation.

    Args:
        input_ts (TimeSeriesLike): time series

    Returns:
        Dict[str,Any]: dictionary with keys "tsgeom" for the time series geometry, and "tsvalues" for its values.

    """
    # from cinterop.timeseries import getTsGeometry
    # stopifnot(is.xts(input_ts))
    # def getSeriesColumn(k):
    #     return(as.numeric(input_ts[,k]))
    return {
        TS_INTEROP_GEOM_KEY: marshal.as_native_tsgeom(get_tsgeom(input_ts)),
        TS_INTEROP_VALUES_KEY: input_ts.values.squeeze(),  # lapply(1:ncol(input_ts), FUN=getSeriesColumn)
    }

```

## `to_interop_univariate_series(ts, from_date=None, to_date=None)`

Convert an univariate python time series to a representation suitable for interoperability with a C API

Parameters:

| Name        | Type                     | Description                                                        | Default    |
| ----------- | ------------------------ | ------------------------------------------------------------------ | ---------- |
| `ts`        | `TimeSeriesLike`         | Python native time series                                          | *required* |
| `from_date` | `ConvertibleToTimestamp` | start timestamp of the time series to subset to. Defaults to None. | `None`     |
| `to_date`   | `ConvertibleToTimestamp` | end timestamp of the time series to subset to. Defaults to None.   | `None`     |

Returns:

| Type                                       | Description                                                                                          |
| ------------------------------------------ | ---------------------------------------------------------------------------------------------------- |
| `Tuple[ndarray, TimeSeriesGeometryNative]` | Tuple\[np.ndarray, TimeSeriesGeometryNative\]: univeriate data and time series geometry for interop. |

Source code in `swift2/internal.py`

```
def to_interop_univariate_series(
    ts: TimeSeriesLike,
    from_date: ConvertibleToTimestamp = None,
    to_date: ConvertibleToTimestamp = None,
) -> Tuple[np.ndarray, TimeSeriesGeometryNative]:
    """Convert an univariate python time series to a representation suitable for interoperability with a C API

    Args:
        ts (TimeSeriesLike): Python native time series
        from_date (ConvertibleToTimestamp, optional): start timestamp of the time series to subset to. Defaults to None.
        to_date (ConvertibleToTimestamp, optional): end timestamp of the time series to subset to. Defaults to None.

    Returns:
        Tuple[np.ndarray, TimeSeriesGeometryNative]: univeriate data and time series geometry for interop.
    """
    from cinterop.timeseries import ts_window
    from swift2.internal import simplify_time_series

    from_date = as_timestamp(from_date) if not from_date is None else None
    to_date = as_timestamp(to_date) if not from_date is None else None
    observation = ts_window(ts, from_date, to_date)
    simple_ts = simplify_time_series(observation)
    return (simple_ts[TS_INTEROP_VALUES_KEY], simple_ts[TS_INTEROP_GEOM_KEY])

```
