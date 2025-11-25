# Module statistics

# statistics

Functions:

- **`createCompositeObjective`** – Creates a composite objective calculator
- **`create_composite_objective`** –
- **`create_multisite_objective`** – Creates an objective that combines multiple statistics
- **`create_objective`** – Creates an objective calculator
- **`get_score`** – Evaluate an objective for a given parameterisation
- **`multi_statistic_definition`** – Collate information for use in multisite multiobjective definition

## createCompositeObjective

```
createCompositeObjective(simulation, state_name, observation, yamlstring_statistic, start_date, end_date)
```

Creates a composite objective calculator

Creates a composite objective calculator

Parameters:

- **`simulation`** (`Simulation`) – A SWIFT simulation object (i.e. a model runner)
- **`state_name`** (`Any`) – The name identifying the model state variable to calibrate against the observation
- **`observation`** (`Any`) – an xts
- **`yamlstring_statistic`** (`Any`) – a yaml string representing objective functions and weights eg...
- **`start_date`** (`Any`) – start date of the period to calculate statistics on
- **`end_date`** (`Any`) – end date of the period to calculate statistics on

Returns:

- – objective evaluator

## create_composite_objective

```
create_composite_objective(objectives: Sequence[ObjectiveEvaluator], weights: Sequence[float], names: Sequence[str]) -> ObjectiveEvaluator
```

## create_multisite_objective

```
create_multisite_objective(simulation: Simulation, statspec: DataFrame, observations: Sequence[TimeSeriesLike], weights: Dict[str, float])
```

Creates an objective that combines multiple statistics

Creates an objective that combines multiple statistics. Used for joined, "whole of catchment" calibration

Parameters:

- **`simulation`** (`Simulation`) – A SWIFT simulation object (i.e. a model runner)
- **`statspec`** (`DataFrame`) – dataframe defining the objectives used. See function multi_statistic_definition to help build this dataframe.
- **`observations`** (`Sequence[TimeSeriesLike]`) – A list of (time series) observations to calculated the statistics. Must be of same length as the number of rows of statspec.
- **`weights`** (`Dict[str, float]`) – numeric vector of weights to ponderate each objective.
- **`Examples`** – todo()

## create_objective

```
create_objective(simulation: Simulation, state_name: str, observation: TimeSeriesLike, statistic: str, start_date: ConvertibleToTimestamp, end_date: ConvertibleToTimestamp)
```

Creates an objective calculator

Parameters:

- **`simulation`** (`Simulation`) – A SWIFT simulation object (i.e. a model runner)
- **`state_name`** (`Any`) – The name identifying the model state variable to calibrate against the observation
- **`observation`** (`TimeSeriesLike`) – an xts
- **`statistic`** (`str`) – statistic identifier, e.g. "NSE"
- **`start_date`** (`ConvertibleToTimestamp`) – start date of the period to calculate statistics on
- **`end_date`** (`ConvertibleToTimestamp`) – end date of the period to calculate statistics on

## get_score

```
get_score(objective_evaluator: ObjectiveEvaluator, p_set: HypercubeParameteriser) -> Dict[str, Any]
```

Evaluate an objective for a given parameterisation

Parameters:

- **`objective_evaluator`** (`ObjectiveEvaluator`) – objective evaluator
- **`p_set`** (`HypercubeParameteriser`) – parameteriser

Returns:

- `Dict[str, Any]` – Dict\[str,Any\]: score(s), and a data frame representation of the input parameters.

## multi_statistic_definition

```
multi_statistic_definition(model_var_ids, statistic_ids, objective_ids, objective_names, starts, ends)
```

Collate information for use in multisite multiobjective definition

Collate information for use in multisite multiobjective definition

Parameters:

- **`model_var_ids`** (`Any`) – character vector, model state identifiers where statistics are calculated
- **`statistic_ids`** (`Any`) – character vector, identifiers for bivariate statistics (e.g. nse, lognse, et.)
- **`objective_ids`** (`Any`) – character vector, identifiers for the objectives. Can be the same as modelVarIds.
- **`objective_names`** (`Any`) – character vector, display names for the objectives. Can be the same as modelVarIds.
- **`starts`** (`Any`) – POSIXct vector of start dates for statistics
- **`ends`** (`Any`) – POSIXct vector of end dates for statistics
