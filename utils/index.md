# Module utils

## `c(*args)`

Emulate the R c (concatenate) function, somewhat.

Returns:

| Type | Description | | --- | --- | | `ndarray` | np.ndarray: [description] |

Source code in `swift2/utils.py`

```
def c(*args) -> np.ndarray:
    """Emulate the R c (concatenate) function, somewhat.

    Returns:
        np.ndarray: [description]
    """
    return np.array([x for x in args])

```

## `is_common_iterable(obj)`

True if an object is iterable but not a string (str)

Source code in `swift2/utils.py`

```
def is_common_iterable(obj: Any) -> bool:
    """True if an object is iterable but not a string (str)"""
    if isinstance(obj, str):
        return False
    # if isinstance(obj, np.ndarray) and obj.size == 1:
    #     return False # otherwise likely to get error "len() of unsized object"
    return hasattr(type(obj), "__iter__")

```

## `mk_full_data_id(*args)`

Create swift IDs (dot separated hierarchical naming scheme)

Create swift IDs (dot separated hierarchical naming scheme). Note that the behavior is different than 'paste' for empty characters.

Parameters:

| Name | Type | Description | Default | | --- | --- | --- | --- | | `args` | `Any` | one or more character vectors. | `()` |

Examples:

TODO

Source code in `swift2/utils.py`

```
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

```

## `paste(*lists, sep=' ', collapse=None)`

Port of R paste function

Source code in `swift2/utils.py`

```
def paste(*lists, sep=" ", collapse=None):
    """Port of R paste function"""
    result = reduce_concat(lists, sep=sep)
    if collapse is not None:
        return reduce_concat(result, sep=collapse)
    return result

```

## `paste0(*lists, collapse=None)`

Port of R paste0 function

Source code in `swift2/utils.py`

```
def paste0(*lists, collapse=None):
    """Port of R paste0 function"""
    return paste(*lists, sep="", collapse=collapse)

```

## `paste_2(x, y, sep=' ')`

Port of R vectorised paste, for 2 elements

Source code in `swift2/utils.py`

```
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

```

## `sort_by(x, unsorted_reference, sorted_reference)`

Sort one vector according to the known reordering of another

Parameters:

| Name | Type | Description | Default | | --- | --- | --- | --- | | `x` | `Any` | values to sort | *required* | | `unsorted_reference` | `Any` | unique 'keys' corresponding to each element in x | *required* | | `sorted_reference` | `Any` | set of 'keys', identical as a set to unsorted_reference, but sorted | *required* |

Returns:

| Type | Description | | --- | --- | | | the values in x reordered such that the same reordering of unsorted_reference matches sorted_reference |

Examples:

TODO

Source code in `swift2/utils.py`

```
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

```

## `vpaste(root, vars)`

vectorised paste for 2 elements; Port of R paste0 in spirit

Parameters:

| Name | Type | Description | Default | | --- | --- | --- | --- | | `root` | `VecScalars` | left hand side(s) of the paste | *required* | | `vars` | `VecScalars` | right hand side(s) of the paste | *required* |

Returns:

| Type | Description | | --- | --- | | `Union[str, Sequence[str]]` | Union\[str,Sequence[str]\]: pasted scalars |

Source code in `swift2/utils.py`

```
def vpaste(root: VecScalars, vars: VecScalars) -> Union[str, Sequence[str]]:
    """vectorised paste for 2 elements; Port of R paste0 in spirit

    Args:
        root (VecScalars): left hand side(s) of the paste
        vars (VecScalars): right hand side(s) of the paste

    Returns:
        Union[str,Sequence[str]]: pasted scalars
    """
    return paste_2(root, vars, sep="")

```
