from typing import Any, Dict, Tuple, Optional, TYPE_CHECKING
import pandas as pd

if TYPE_CHECKING:
    from swift2.classes import Simulation
    from swift2.const import VecStr
import xarray as xr
import numpy as np

from refcount.interop import is_cffi_native_handle, cffi_arg_error_external_obj_type
import swift2.wrap.swift_wrap_custom as swc
import swift2.wrap.swift_wrap_generated as swg
from cinterop.cffi.marshal import(
    get_tsgeom,
    TimeSeriesGeometryNative,
)
from cinterop.timeseries import(
    xr_ts_start,
    xr_ts_end,
    slice_xr_time_series,
    ConvertibleToTimestamp,
    TimeSeriesLike,
    as_timestamp,
)
from swift2.wrap.ffi_interop import marshal

import uchronia.data_set as uds

TS_INTEROP_GEOM_KEY = "tsgeom"
TS_INTEROP_VALUES_KEY = "tsvalues"


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


# #Hmmm... is this just duplicating normalizePath??
# mkPathToPlatform (fileName):
#   if(Sys.info()['sysname'] == 'Windows'):
#     unixToWindowsPath(fileName)
#   } else {
#     windowsToUnixPath(fileName)
#   }
# }


def internal_get_recorded_tts(
    simulation: "Simulation", var_ids: "VecStr"
) -> Optional[xr.DataArray]:
    return uds.get_multiple_time_series_from_provider(
        simulation, var_ids, swc.get_recorded_pkg
    )


def internal_get_played_tts(
    simulation: "Simulation", var_ids: "VecStr"
) -> Optional[xr.DataArray]:
    return uds.get_multiple_time_series_from_provider(
        simulation, var_ids, swc.get_played_pkg
    )


# swiftMissingVal <- NA

# #' Create a functor for time series interop and missing value handling
# #'
# #' Create a functor for time series interop and missing value handling
# #'
# #' @param FUN a function that takes as arguments a date, a numeric, and a function. See for instance mkDailySeries.
# #' @return a function that takes a date, and a numeric, that considers -9999.9 as a missing value in the input numeric values.
# mkSeriesFunctor (FUN):
#   missValueCode <- -9999.9
#   # cannot seem to get the following to work, with or without caching.
#   # missValueCode <- getSwiftMissingValue()
#   funRes (start_date, x, isMissingFunc = function(val):val == missValueCode}):
#     FUN(start_date, x, isMissingFunc)
#   }
#   return(funRes)
# }


def _start(series: xr.DataArray):
    return xr_ts_start(series)


def _end(series: xr.DataArray):
    return xr_ts_end(series)


def _slice_xr_time_series(
    data: xr.DataArray, from_date: pd.Timestamp = None, to_date: pd.Timestamp = None
) -> xr.DataArray:
    return slice_xr_time_series(data, from_date, to_date)


def _window(series: xr.DataArray, start, end):
    return _slice_xr_time_series(series, start, end)


def chk_date_time(series, dt, xr_func):
    # Used to use ifelse in getTsWindow, but
    # [ifelse strips attributes](https://stackoverflow.com/questions/31133382/ifelse-stripping-posixct-attribute-from-vector-of-timestamps)
    # and a change of behavior in xts made it break
    if dt is None:
        dt = xr_func(series)
    return dt


import xarray as xr


def get_ts_window(series: xr.DataArray, start_time, end_time):
    if series is None:
        return None
    start_time = chk_date_time(series, start_time, _start)
    end_time = chk_date_time(series, end_time, _end)
    return _window(series, start_time, end_time)


def is_swift_ref(x, type: str):
    return is_cffi_native_handle(x, type)


def arg_error_swift_type(x, expected_type_id):
    cffi_arg_error_external_obj_type(x, expected_type_id)


def _raise_unexpected_xtr_ptr(x, expected_type_id):
    m = cffi_arg_error_external_obj_type(x, expected_type_id)
    raise TypeError(m)


def is_ensemble_forecast_simulation(s):
    return is_cffi_native_handle(s, type_id="ENSEMBLE_FORECAST_SIMULATION_PTR")


def is_ensemble_forecast_time_series(s):
    return is_cffi_native_handle(s, type_id="ENSEMBLE_FORECAST_TIME_SERIES_PTR")


def is_ensemble_simulation(s):
    return is_cffi_native_handle(s, type_id="ENSEMBLE_SIMULATION_PTR")


def is_singular_simulation(s):  # TODO: don't like this name with 'singular'
    return is_cffi_native_handle(s, type_id="MODEL_SIMULATION_PTR")


#############################


def check_singular_simulation(s):
    if not is_singular_simulation(s):
        _raise_unexpected_xtr_ptr(s, "MODEL_SIMULATION_PTR")


def check_ensemble_simulation(s):
    if not is_ensemble_simulation(s):
        _raise_unexpected_xtr_ptr(s, "ENSEMBLE_SIMULATION_PTR")


def check_ensemble_forecast_simulation(s):
    if not is_ensemble_forecast_simulation(s):
        _raise_unexpected_xtr_ptr(s, "ENSEMBLE_FORECAST_SIMULATION_PTR")


def check_ensemble_forecast_time_series(s):
    if not is_ensemble_forecast_time_series(s):
        _raise_unexpected_xtr_ptr(s, "ENSEMBLE_FORECAST_TIME_SERIES_PTR")
