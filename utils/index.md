# Module utils

# utils

Functions:

- **`as_xarray_series`** –
- **`c`** – Emulate the R c (concatenate) function, somewhat.
- **`handle_file_path`** – Check input filename for suitability to be passed to SWIFT API for disk operations.
- **`is_common_iterable`** – True if an object is iterable but not a string (str)
- **`mk_full_data_id`** – Create swift IDs (dot separated hierarchical naming scheme)
- **`parameter_df`** –
- **`parameters_df`** –
- **`paste`** – Port of R paste function
- **`paste0`** – Port of R paste0 function
- **`paste_2`** – Port of R vectorised paste, for 2 elements
- **`paste_list_scalar`** –
- **`paste_lists`** –
- **`paste_scalar_list`** –
- **`paste_scalar_scalar`** –
- **`reduce_concat`** –
- **`rep`** –
- **`sort_by`** – Sort one vector according to the known reordering of another
- **`vpaste`** – vectorised paste for 2 elements; Port of R paste0 in spirit

## as_xarray_series

```
as_xarray_series(x: TimeSeriesLike)
```

## c

```
c(*args) -> ndarray
```

Emulate the R c (concatenate) function, somewhat.

Returns:

- `ndarray` – np.ndarray: [description]

## handle_file_path

```
handle_file_path(file_path: Union[Path, str], must_exist: bool) -> str
```

Check input filename for suitability to be passed to SWIFT API for disk operations.

Parameters:

- **`filename`** (`Union[Path, str]`) – input filename
- **`must_exist`** (`bool`) – if True, check that the file exists

Returns:

- **`str`** ( `str` ) – path to the file

## is_common_iterable

```
is_common_iterable(obj: Any) -> bool
```

True if an object is iterable but not a string (str)

## mk_full_data_id

```
mk_full_data_id(*args)
```

Create swift IDs (dot separated hierarchical naming scheme)

Create swift IDs (dot separated hierarchical naming scheme). Note that the behavior is different than 'paste' for empty characters.

Parameters:

- **`args`** (`Any`, default: `()` ) – one or more character vectors.

Examples:

TODO

## parameter_df

```
parameter_df(name: str, value: float, min: float, max: float)
```

## parameters_df

```
parameters_df(names: List[str], values: Sequence[float], minima: Sequence[float], maxima: Sequence[float])
```

## paste

```
paste(*lists, sep=' ', collapse=None)
```

Port of R paste function

## paste0

```
paste0(*lists, collapse=None)
```

Port of R paste0 function

## paste_2

```
paste_2(x: VecScalars, y: VecScalars, sep: str = ' ')
```

Port of R vectorised paste, for 2 elements

## paste_list_scalar

```
paste_list_scalar(x: VecScalars, y: Scalar, sep: str = ' ') -> Sequence[str]
```

## paste_lists

```
paste_lists(x: VecScalars, y: VecScalars, sep: str = ' ') -> Sequence[str]
```

## paste_scalar_list

```
paste_scalar_list(x: Scalar, y: Sequence[Scalar], sep: str = ' ') -> Sequence[str]
```

## paste_scalar_scalar

```
paste_scalar_scalar(x: Scalar, y: Scalar, sep: str = ' ') -> str
```

## reduce_concat

```
reduce_concat(z, sep='')
```

## rep

```
rep(x: Scalar, n: int)
```

## sort_by

```
sort_by(x, unsorted_reference, sorted_reference)
```

Sort one vector according to the known reordering of another

Parameters:

- **`x`** (`Any`) – values to sort
- **`unsorted_reference`** (`Any`) – unique 'keys' corresponding to each element in x
- **`sorted_reference`** (`Any`) – set of 'keys', identical as a set to unsorted_reference, but sorted

Returns:

- – the values in x reordered such that the same reordering of unsorted_reference matches sorted_reference

Examples:

TODO

## vpaste

```
vpaste(root: VecScalars, vars: VecScalars) -> Union[str, Sequence[str]]
```

vectorised paste for 2 elements; Port of R paste0 in spirit

Parameters:

- **`root`** (`VecScalars`) – left hand side(s) of the paste
- **`vars`** (`VecScalars`) – right hand side(s) of the paste

Returns:

- `Union[str, Sequence[str]]` – Union\[str,Sequence[str]\]: pasted scalars
