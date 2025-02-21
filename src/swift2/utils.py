from typing import Any, List, Sequence, Tuple, Union
from cinterop.timeseries import start_ts, end_ts
import numpy as np
from swift2.common import _df_from_dict, _npf
from swift2.const import Scalar, VecScalars
import pandas as pd
import xarray as xr


def c(*args) -> np.ndarray:
    """Emulate the R c (concatenate) function, somewhat.

    Returns:
        np.ndarray: [description]
    """
    return np.array([x for x in args])


# from swift2.swift_simulation import *

# #' convert a unix style path to a windows one
# #'
# #' convert a unix style path to a windows one. This function is mostly used for internally passing paths to the SWIFT API.
# #'
# #' @param fileName a Unix style file path
# #' @return win style path such as '\\\\wron\\path\\to\\some\\controlfile.txt'
# #' @import stringr
# #' @export
# unixToWindowsPath(fileName):
#   if(stringr::str_detect(fileName, '/')):
#     fileName = stringr::str_replace_all(fileName, '/', replacement='\\\\')
#   }
#   fileName
# }

# #' convert a windows style path to a unix one
# #'
# #' convert a windows style path to a unix one. This function is mostly used for internally passing paths to the SWIFT API.
# #'
# #' @param fileName a file path, possibly with a win style path such as '\\\\wron\\path\\to\\some\\controlfile.txt'
# #' @return unix style path such as '//wron/path/to/some/controlfile.txt'
# #' @import stringr
# #' @export
# windowsToUnixPath(fileName):
#   if(stringr::str_detect(fileName, '\\\\')):
#     fileName = stringr::str_replace_all(fileName, '\\\\', replacement='/')
#   }
#   fileName
# }


def sort_by(x, unsorted_reference, sorted_reference):
    """
    Sort one vector according to the known reordering of another

    Args:
        x (Any): values to sort
        unsorted_reference (Any): unique 'keys' corresponding to each element in x
        sorted_reference (Any): set of 'keys', identical as a set to unsorted_reference, but sorted

    Returns:
        the values in x reordered such that the same reordering of unsorted_reference matches sorted_reference

    Examples:
        TODO

    """
    # >>> # set.seed(12)
    # >>> # (x = sample(1:5))
    # >>> # (unsorted_reference = letters[x])
    # >>> # (sorted_reference = letters[1:5])
    # >>> # (x[order(match(unsorted_reference,sorted_reference))])
    # >>> # sortBy(x, unsorted_reference, sorted_reference)
    assert len(x) == len(unsorted_reference)
    assert len(sorted_reference) == len(unsorted_reference)
    assert set(unsorted_reference) == set(sorted_reference)
    # There may be something more elegant
    def find_index(shuffled, sorted):
        if isinstance(shuffled, list):
            shuffled = np.array(shuffled)
        s = [np.argwhere(x == shuffled) for x in sorted]
        for v in s:
            assert v.shape == (1, 1)
        return [v[0][0] for v in s]

    # TODO unit test of course:
    # x = np.array([2, 5, 3, 1, 4])
    # unsorted_reference = np.array(["b","e","c","a","d"])
    # sorted_reference = np.array(["a","b","c","d","e"])
    # indx = find_index(unsorted_reference, sorted_reference)
    # [x[i] for i in indx]
    indx = find_index(unsorted_reference, sorted_reference)
    return [x[i] for i in indx]


# checkValidInputTs(obs, sim):
#   stopifnot(is.xts(sim) && is.xts(obs))
#   stopifnot(ncol(sim)==1)
#   stopifnot(ncol(obs)==1)
#   stopifnot(all(index(sim) == index(obs)))
# }

# toNumVec(x):
#   return(joki::asNumericVector(x))
# }


def mk_full_data_id(*args):
    """
    Create swift IDs (dot separated hierarchical naming scheme)

    Create swift IDs (dot separated hierarchical naming scheme). Note that the behavior is different than 'paste' for empty characters.

    Args:
        args (Any): one or more character vectors.

    Examples:
        TODO

    """
    #    >>> # (obsVarname <- mkFullDataId('link','corin_dam','ec','Observed'))
    #    >>> # subareaFullIds <- mkFullDataId( 'subarea', getSubareaIds(simulation))
    #    >>> # mkFullDataId(character(0),'corin_dam','ec','Observed')
    ids = list(args)
    if len(ids) == 0:
        return None
    else:
        lengths = [len(x) for x in ids if not isinstance(x, str)]
        if len(lengths) > 0:
            minl = min(lengths)
            if minl < 1:
                return None
        return paste(*args, sep=".")


def is_common_iterable(obj: Any) -> bool:
    """True if an object is iterable but not a string (str)"""
    if isinstance(obj, str):
        return False
    # if isinstance(obj, np.ndarray) and obj.size == 1:
    #     return False # otherwise likely to get error "len() of unsized object"
    return hasattr(type(obj), "__iter__")


def rep(x: Scalar, n: int):
    return np.repeat(x, n)


def paste_lists(x: VecScalars, y: VecScalars, sep: str = " ") -> Sequence[str]:
    assert is_common_iterable(x)
    assert is_common_iterable(y)
    assert len(x) == len(y)
    return [sep.join([str(x[i]), str(y[i])]) for i in range(len(x))]


def paste_list_scalar(x: VecScalars, y: Scalar, sep: str = " ") -> Sequence[str]:
    assert is_common_iterable(x)
    return [sep.join([str(x[i]), str(y)]) for i in range(len(x))]


def paste_scalar_list(x: Scalar, y: Sequence[Scalar], sep: str = " ") -> Sequence[str]:
    assert is_common_iterable(y)
    return [sep.join([str(x), str(y[i])]) for i in range(len(y))]


def paste_scalar_scalar(x: Scalar, y: Scalar, sep: str = " ") -> str:
    return sep.join([str(x), str(y)])


def paste_2(x: VecScalars, y: VecScalars, sep: str = " "):
    """Port of R vectorised paste, for 2 elements"""
    if is_common_iterable(x):
        if is_common_iterable(y):
            return paste_lists(x, y, sep)
        else:
            return paste_list_scalar(x, y, sep)
    else:
        if is_common_iterable(y):
            return paste_scalar_list(x, y, sep)
        else:
            return paste_scalar_scalar(x, y, sep)


def vpaste(root: VecScalars, vars: VecScalars) -> Union[str, Sequence[str]]:
    """vectorised paste for 2 elements; Port of R paste0 in spirit

    Args:
        root (VecScalars): left hand side(s) of the paste
        vars (VecScalars): right hand side(s) of the paste

    Returns:
        Union[str,Sequence[str]]: pasted scalars
    """
    return paste_2(root, vars, sep="")


import functools


def reduce_concat(z, sep=""):
    return functools.reduce(lambda x, y: paste_2(x, y, sep), z)


## adapted from: https://eulertech.wordpress.com/author/eulertech/
def paste(*lists, sep=" ", collapse=None):
    """Port of R paste function"""
    result = reduce_concat(lists, sep=sep)
    if collapse is not None:
        return reduce_concat(result, sep=collapse)
    return result


def paste0(*lists, collapse=None):
    """Port of R paste0 function"""
    return paste(*lists, sep="", collapse=collapse)


from cinterop.timeseries import TimeSeriesLike, TIME_DIMNAME


def as_xarray_series(x: TimeSeriesLike):
    if isinstance(x, pd.Series):
        return xr.DataArray(x.values, coords=[x.index], dims=[TIME_DIMNAME])
    elif isinstance(x, pd.DataFrame):
        # TODO checks
        return xr.DataArray(x.values.squeeze(), coords=[x.index], dims=[TIME_DIMNAME])
    elif isinstance(x, xr.DataArray):
        return x
    else:
        raise NotImplementedError(
            "Don't know how to convert an object of type {} to an xarray time series".format(
                type(x)
            )
        )


def parameter_df(name: str, value: float, min: float, max: float):
    return _df_from_dict(
        Name=[name],
        Value=_npf([value]),
        Min=_npf([min]),
        Max=_npf([max]),
    )


def parameters_df(
    names: List[str],
    values: Sequence[float],
    minima: Sequence[float],
    maxima: Sequence[float],
):
    return _df_from_dict(
        Name=names,
        Value=_npf(values),
        Min=_npf(minima),
        Max=_npf(maxima),
    )
