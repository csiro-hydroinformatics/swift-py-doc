# Module system

# system

Functions:

- **`channel_routing_model_ids`** – Gets all the names of known channel routing models
- **`get_last_swift_error`** – Retrieve the message for the last known error in SWIFT
- **`objective_statistic_ids`** – Gets all the names of known objective statistics
- **`runoff_model_ids`** – Gets all the names of known runoff models
- **`runoff_model_var_ids`** – Gets all the names of the variables a runoff model exposes
- **`set_default_max_parallelism_threads`** – Sets the level of thread parallelism to use by default for new objects such as optimisers. May be overwritten for each instance afterwards.
- **`set_maximum_threads`** – Sets the maximum level of parallelism of an optimizer

## channel_routing_model_ids

```
channel_routing_model_ids()
```

Gets all the names of known channel routing models

Gets all the names of known channel routing models

Returns:

- – character vector, names (identifiers) of channel routing models

## get_last_swift_error

```
get_last_swift_error()
```

Retrieve the message for the last known error in SWIFT

Retrieve the message for the last known error in SWIFT. Error means here that an exception was thrown by the core SWIFT library. The SWIFT C API intercepts these messages to make them available to users for diagnosis.

Returns:

- – A character, the message for the last known error in SWIFT.

## objective_statistic_ids

```
objective_statistic_ids()
```

Gets all the names of known objective statistics

Gets all the names of known objective statistics

Returns:

- – character vector, names (identifiers) of objective statistics

## runoff_model_ids

```
runoff_model_ids()
```

Gets all the names of known runoff models

Gets all the names of known runoff models

Returns:

- – character vector, names (identifiers) of runoff models

## runoff_model_var_ids

```
runoff_model_var_ids(model_id)
```

Gets all the names of the variables a runoff model exposes

Gets all the names of the variables a runoff model exposes for dynamic query.

Parameters:

- **`model_id`** (`Any`) – character; A recognized model identifier

Returns:

- – a character vector, the known model variable that can be set/gotten

## set_default_max_parallelism_threads

```
set_default_max_parallelism_threads(n_threads: int = -1)
```

Sets the level of thread parallelism to use by default for new objects such as optimisers. May be overwritten for each instance afterwards.

Parameters:

- **`n_threads`** (`int`, default: `-1` ) – number of threads. Positive, or -1 to mean "as many as available"

## set_maximum_threads

```
set_maximum_threads(optimiser, n_threads=-1)
```

Sets the maximum level of parallelism of an optimizer

Sets the maximum level of threading of an optimizer. NOTE: this also modifies a global default for further optimizers, which is a hack for ERRIS, acceptable but still likely to change in the future. It is VERY important to use this function prior to running calibrations on some systems such as clusters, as the default hardware detection may not be appropriate if the cluster node is not dedicated.

Parameters:

- **`optimizer`** (`Any`) – an S4 object 'ExternalObjRef' [package "cinterop"] with external pointer type "OPTIMIZER_PTR"
- **`n_threads`** (`Any`, default: `-1` ) – integer, maximum number of threads allowed. If -1, the system defaults to using all but one of the CPU cores detected on the hardware.
