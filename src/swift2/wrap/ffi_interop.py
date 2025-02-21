"""
    Wrapper around SWIFT2 C API functions using CFFI.
"""
from functools import wraps
from cffi import FFI
import os
from typing import List, Dict, Any
from refcount.putils import library_short_filename, update_path_windows
import pandas as pd

from refcount.interop import OwningCffiNativeHandle, CffiNativeHandle
from cinterop.cffi.marshal import CffiMarshal

swift_ffi = FFI()
here = os.path.abspath(os.path.dirname(__file__))
swift_pkg_dir = os.path.join(here, "..")
cdefs_dir = os.path.join(swift_pkg_dir, "data")
assert os.path.exists(cdefs_dir)

with open(os.path.join(cdefs_dir, "structs_cdef.h")) as f_headers:
    swift_ffi.cdef(f_headers.read())

with open(os.path.join(cdefs_dir, "funcs_cdef.h")) as f_headers:
    swift_ffi.cdef(f_headers.read())

short_fname = library_short_filename("swift")
update_path_windows(from_env="LIBRARY_PATH", to_env="PATH")
# TODO is there a concrete use case to search custom paths and not let dlopen do its default??
# long_fname = find_first_full_path(short_fname, "swift")
long_fname = short_fname

swift_so = swift_ffi.dlopen(long_fname, swift_ffi.RTLD_LAZY)

marshal = CffiMarshal(swift_ffi)


class SwiftError(Exception):
    """Exception when calling a swift function."""

    def __init__(self, message):
        super(SwiftError, self).__init__(message)


# This will store the exception message raised by swift
_exception_txt_raised_swift = None


@swift_ffi.callback("void(char *)")
def _exception_callback_swift(exception_string):
    """
    This function is called when swift raises an exception.
    It sets the global variable ``_exception_txt_raised_swift``

    :param cdata exception_string: Exception string.
    """
    global _exception_txt_raised_swift
    _exception_txt_raised_swift = swift_ffi.string(exception_string)


def check_exceptions(func):
    """
    Returns a wrapper that raises a Python exception if a swift exception
    occured.
    """

    @wraps(func)
    def wrapper(*args, **kwargs):
        """
        This decorator will first call the function ``func``
        After that it will raise a Python SwiftError exception if the
        global variable ``_exception_txt_raised_swift`` is set.

        :param func func: Python function wrapping a swift function.
        """
        # log_func_call(func, *args, **kwargs)
        # Call the function
        return_value = func(*args, **kwargs)
        # Check if an exception was raised
        global _exception_txt_raised_swift
        if _exception_txt_raised_swift is not None:
            temp_exception = _exception_txt_raised_swift
            _exception_txt_raised_swift = None
            raise SwiftError(temp_exception)
        return return_value

    return wrapper


swift_so.RegisterExceptionCallback(_exception_callback_swift)


@check_exceptions
def swift_dispose_multi_time_series_data(data):
    """
    :param ptr data: Pointer to a MultiTimeSeriesData.
    """
    swift_so.DisposeMultiTimeSeriesData(data)


RCPP_STAT_LENGTH_NAME = "Length"
RCPP_STAT_SPEC_NAME = "Statistics"
RCPP_STAT_OBSERVATIONS_NAME = "Observations"
RCPP_STAT_VAR_ID_NAME = "ModelVarId"
RCPP_STAT_STAT_ID_NAME = "StatisticId"
RCPP_STAT_OBJ_ID_NAME = "ObjectiveId"
RCPP_STAT_OBJ_NAME_NAME = "ObjectiveName"
RCPP_TS_START_NAME = "Start"
RCPP_TS_END_NAME = "End"


def to_multi_statistic_definition(rTsInfo: Dict[str, Any]):

    msd = marshal.new_native_struct("multi_statistic_definition*")
    specs = rTsInfo[RCPP_STAT_SPEC_NAME]
    n = len(specs)
    msd.keepalive = []
    msd.ptr.size = n
    array: OwningCffiNativeHandle = marshal.new_ctype_array(
        "statistic_definition*", n, wrap=True
    )
    msd.keepalive.append(array)
    msd.ptr.statistics = array.ptr
    msd.ptr.mix_statistics_id = marshal.nullptr

    observations: List[OwningCffiNativeHandle] = rTsInfo[RCPP_STAT_OBSERVATIONS_NAME]

    model_variable_id: List[str] = specs[RCPP_STAT_VAR_ID_NAME]
    statistic_identifier: List[str] = specs[RCPP_STAT_STAT_ID_NAME]
    objective_identifier: List[str] = specs[RCPP_STAT_OBJ_ID_NAME]
    objective_name: List[str] = specs[RCPP_STAT_OBJ_NAME_NAME]
    start: List[pd.Timestamp] = specs[RCPP_TS_START_NAME]
    end: List[pd.Timestamp] = specs[RCPP_TS_END_NAME]

    for i in range(n):
        mvid = model_variable_id[i]
        sid = statistic_identifier[i]
        objid = objective_identifier[i]
        objname = objective_name[i]
        obsSeries = observations[i]
        s = marshal.new_native_struct("statistic_definition*")
        msd.ptr.statistics[i] = s.ptr
        s.ptr.observations = obsSeries.ptr

        objname_c = marshal.as_charptr(objname, True)
        sid_c = marshal.as_charptr(sid, True)
        objid_c = marshal.as_charptr(objid, True)
        mvid_c = marshal.as_charptr(mvid, True)
        s_start = marshal.datetime_to_dtts(start[i])
        s_end = marshal.datetime_to_dtts(end[i])

        s.ptr.model_variable_id = mvid_c.ptr
        s.ptr.objective_identifier = objid_c.ptr
        s.ptr.objective_name = objname_c.ptr
        s.ptr.statistic_identifier = sid_c.ptr
        s.ptr.start = s_start.ptr[
            0
        ]  # not sure whether this performs a memory copy, or passes a reference (which would be problematic)
        s.ptr.end = s_end.ptr[0]

        msd.keepalive.append(objname_c)
        msd.keepalive.append(mvid_c)
        msd.keepalive.append(sid_c)
        msd.keepalive.append(objid_c)
        msd.keepalive.append(s_start)
        msd.keepalive.append(s_end)
        msd.keepalive.append(obsSeries)
        msd.keepalive.append(s)
    return msd


def unwrap(x):
    y = x
    if isinstance(x, CffiNativeHandle):
        y = x.ptr
    return y


def cc(x):
    y = unwrap(x)
    try:
        return marshal.c_string_as_py_string(y)
    except UnicodeDecodeError:
        return str(",".join([str(y[i]) for i in range(5)]))


def debug_msd(msd):
    msd = unwrap(msd)
    print("")
    print("msd.size: %d" % (msd.size,))
    print("")
    n = msd.size
    for i in range(n):
        s = msd.statistics[i]
        debug_stat_ser(s)
    print("")


def debug_dt_ser(d):
    return "%i-%i-%i %i-%i-%i" % (d.year, d.month, d.day, d.hour, d.minute, d.second)


def debug_stat_ser(s):
    s = unwrap(s)
    print("model_variable_id: %s" % (cc(s.model_variable_id),))
    print("objective_identifier: %s" % (cc(s.objective_identifier),))
    print("objective_name: %s" % (cc(s.objective_name),))
    print("statistic_identifier: %s" % (cc(s.statistic_identifier),))
    print("start: " + debug_dt_ser(s.start))
    print("end: " + debug_dt_ser(s.end))
    print("")
