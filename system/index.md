# Module system

## `get_last_swift_error()`

Retrieve the message for the last known error in SWIFT

Retrieve the message for the last known error in SWIFT. Error means here that an exception was thrown by the core SWIFT library. The SWIFT C API intercepts these messages to make them available to users for diagnosis.

Returns:

| Type | Description                                                 |
| ---- | ----------------------------------------------------------- |
|      | A character, the message for the last known error in SWIFT. |

Source code in `swift2/system.py`

```
def get_last_swift_error():
    """
    Retrieve the message for the last known error in SWIFT

    Retrieve the message for the last known error in SWIFT. Error means here that an exception was thrown by the core
    SWIFT library. The SWIFT C API intercepts these messages to make them available to users for diagnosis.

    Returns:
        A character, the message for the last known error in SWIFT.
    """

    return swg.GetLastStdExceptionMessage_py()

```

## `runoff_model_ids()`

Gets all the names of known runoff models

Gets all the names of known runoff models

Returns:

| Type | Description                                            |
| ---- | ------------------------------------------------------ |
|      | character vector, names (identifiers) of runoff models |

Source code in `swift2/system.py`

```
def runoff_model_ids():
    """
    Gets all the names of known runoff models

    Gets all the names of known runoff models

    Returns:
        character vector, names (identifiers) of runoff models

    """
    return swg.GetRunoffModelIdentifiers_py()

```

## `runoff_model_var_ids(model_id)`

Gets all the names of the variables a runoff model exposes

Gets all the names of the variables a runoff model exposes for dynamic query.

Parameters:

| Name       | Type  | Description                              | Default    |
| ---------- | ----- | ---------------------------------------- | ---------- |
| `model_id` | `Any` | character; A recognized model identifier | *required* |

Returns:

| Type | Description                                                         |
| ---- | ------------------------------------------------------------------- |
|      | a character vector, the known model variable that can be set/gotten |

Source code in `swift2/system.py`

```
def runoff_model_var_ids(model_id):
    """
    Gets all the names of the variables a runoff model exposes

    Gets all the names of the variables a runoff model exposes for dynamic query.

    Args:
        model_id (Any): character; A recognized model identifier

    Returns:
        a character vector, the known model variable that can be set/gotten

    """
    if model_id not in runoff_model_ids():
        raise ValueError("Unrecognized runoff model identifier: " + model_id)
    return swg.GetRunoffModelVarIdentifiers_py(model_id)

```

## `set_default_max_parallelism_threads(n_threads=-1)`

Sets the level of thread parallelism to use by default for new objects such as optimisers. May be overwritten for each instance afterwards.

Parameters:

| Name        | Type  | Description                                                       | Default |
| ----------- | ----- | ----------------------------------------------------------------- | ------- |
| `n_threads` | `int` | number of threads. Positive, or -1 to mean "as many as available" | `-1`    |

Source code in `swift2/system.py`

```
def set_default_max_parallelism_threads(n_threads: int = -1):
    """Sets the level of thread parallelism to use by default for new objects such as optimisers. May be overwritten for each instance afterwards.

    Args:
        n_threads (int): number of threads. Positive, or -1 to mean "as many as available"
    """
    swg.SetDefaultMaxThreadsWila_py(n_threads)

```

## `set_maximum_threads(optimiser, n_threads=-1)`

Sets the maximum level of parallelism of an optimizer

Sets the maximum level of threading of an optimizer. NOTE: this also modifies a global default for further optimizers, which is a hack for ERRIS, acceptable but still likely to change in the future. It is VERY important to use this function prior to running calibrations on some systems such as clusters, as the default hardware detection may not be appropriate if the cluster node is not dedicated.

Parameters:

| Name        | Type  | Description                                                                                                                            | Default    |
| ----------- | ----- | -------------------------------------------------------------------------------------------------------------------------------------- | ---------- |
| `optimizer` | `Any` | an S4 object 'ExternalObjRef' [package "cinterop"] with external pointer type "OPTIMIZER_PTR"                                          | *required* |
| `n_threads` | `Any` | integer, maximum number of threads allowed. If -1, the system defaults to using all but one of the CPU cores detected on the hardware. | `-1`       |

Source code in `swift2/system.py`

```
def set_maximum_threads(optimiser, n_threads=-1):
    """
    Sets the maximum level of parallelism of an optimizer

    Sets the maximum level of threading of an optimizer. NOTE: this also modifies a global default for further optimizers,
    which is a hack for ERRIS, acceptable but still likely to change in the future.
    It is VERY important to use this function prior to running calibrations on some systems such as clusters,
    as the default hardware detection may not be appropriate if the cluster node is not dedicated.

    Args:
        optimizer (Any): an S4 object 'ExternalObjRef' [package "cinterop"] with external pointer type "OPTIMIZER_PTR"
        n_threads (Any): integer, maximum number of threads allowed. If -1, the system defaults to using all but one of the CPU cores detected on the hardware.

    """
    swg.SetMaxThreadsOptimizerWila_py(optimiser, n_threads)

```
