# Module parameteriser

# parameteriser

Classes:

- **`MhData`** – Data log from metaheuristic calibration processes

Functions:

- **`add_to_hypercube`** – Add entries to a hypercube
- **`add_transform`** – Create a parameteriser for which parameter transformations can be defined
- **`apply_sys_config`** – Apply a model configuration to a simulation
- **`as_py_structure`** – Try to convert an external pointer to a native python representation
- **`backtransform`** – Get the parameteriser values in the untransformed space
- **`bound_values`** –
- **`bound_values_df`** – min/max bound a column in a data frame
- **`concatenate_parameterisers`** – Concatenate hypercubes to a single parameteriser
- **`create_multisite_obj_parameteriser`** – Builds a parameteriser usable with a multisite multiobjective calculator.
- **`create_muskingum_param_constraints`** – Create a parameteriser with Muskingum-type constraints. Given an existing parameteriser, create a wrapper that adds constraints on two of its parameters.
- **`create_parameter_sampler`** –
- **`create_parameteriser`** – Create a SWIFT parameteriser
- **`create_sce_optim_swift`** – Build an SCE optimiser for a SWIFT model
- **`create_sce_termination_wila`** – Create a type of termination criteria suitable for the SCE algorithm.
- **`evaluate_score_for_parameters`** – Computes the value of an objective for a given set of parameters
- **`example_parameteriser`** – Get examples of typical parameterisers
- **`execute_optimisation`** – Launch an optimization task, as defined by the object passed as an argument
- **`extract_optimisation_log`** – Extract the logger from a parameter extimator (optimiser or related)
- **`feasible_muskingum_bounds`** – [summary]
- **`filtered_parameters`** – Wrap a parameteriser in a filter that can hide some parameters
- **`get_best_score`** – Gets the best score in a population for a given objective
- **`get_default_sce_parameters`** – [summary]
- **`get_logger_content`** – Gets logger content on an optimiser, recorded detail of the optimisation process for post-optimisation analysis.
- **`get_marginal_termination`** – Create an termination criterion based on the rate of marginal fitness improvement
- **`get_max_iteration_termination`** – Create an termination criterion based on the number of objective evaluations
- **`get_max_runtime_termination`** – Create an termination criterion based on the wall clock runtime
- **`get_score_at_index`** – Get an objective scores in a vector thereof
- **`hide_parameters`** – Hide some parameters (from the outside e.g. optimisers) in a filter parameteriser
- **`is_hypercube`** – Is the object a native parameteriser that can be cast as a hypercube?
- **`is_sampler_seeding`** – Is the argument a native object that is a seeded candidate parameteriser factory
- **`is_score`** – OBJECTIVE_SCORES_WILA_PTR
- **`is_set_of_scores`** – VEC_OBJECTIVE_SCORES_PTR
- **`linear_parameteriser`** – Create a scaled linear parameteriser, tying by a linear transformation a (resp several) model state to a (resp several) parameter values
- **`linear_parameteriser_from`** – Create a scaled linear parameteriser, tying by a linear transformation a (resp several) model state to a (resp several) parameter values
- **`listify`** –
- **`make_state_init_parameteriser`** – [summary]
- **`mk_optim_log`** –
- **`num_free_parameters`** –
- **`parameteriser_as_dataframe`** – Convert an external object hypercube parameteriser to a pandas data frame
- **`parameteriser_for_score`** – Gets the parameteriser for a score
- **`parameters_for`** –
- **`scores_as_dataframe`** – Convert objective scores to a pandas data frame representation
- **`set_calibration_logger`** – Sets logging on an optimiser, so as to record a detail of the optimisation process for post-optimisation analysis.
- **`set_hypercube`** – Set the properties of a hypercube parameteriser
- **`set_max_parameter_value`** – Sets the maximum value of a model parameter value
- **`set_min_parameter_value`** – Sets the minimum value of a model parameter value
- **`set_parameter_value`** – Sets the value of a model parameter value
- **`show_parameters`** – Show some parameters (from the outside e.g. optimisers) in a filter parameteriser
- **`sort_by_score`** – Sort objective scores according to one of the objective values
- **`subcatchment_parameteriser`** – Create a parameteriser that gets applied to a subset of a whole catchment
- **`wrap_transform`** – Create a parameteriser for which parameter transformations can be defined.

Attributes:

- **`INTERCEPT_COL`** –
- **`MAX_VALUE_COL`** –
- **`MIN_VALUE_COL`** –
- **`PARAM_NAME_COL`** –
- **`SCALING_VAR_NAME_COL`** –
- **`STATE_NAME_COL`** –
- **`VALUE_COL`** –

## INTERCEPT_COL

```
INTERCEPT_COL = 'intercept'
```

## MAX_VALUE_COL

```
MAX_VALUE_COL = 'max_value'
```

## MIN_VALUE_COL

```
MIN_VALUE_COL = 'min_value'
```

## PARAM_NAME_COL

```
PARAM_NAME_COL = 'param_name'
```

## SCALING_VAR_NAME_COL

```
SCALING_VAR_NAME_COL = 'scaling_var_name'
```

## STATE_NAME_COL

```
STATE_NAME_COL = 'state_name'
```

## VALUE_COL

```
VALUE_COL = 'value'
```

## MhData

```
MhData(data: DataFrame, fitness: str = 'NSE', messages: str = 'Message', categories: str = 'Category')
```

Data log from metaheuristic calibration processes

Methods:

- **`bound_fitness`** – Return a copy of the log data with the fitness measure bound by min/max limits
- **`facet_plot`** – Facet plot of parameter value evolution, facetted by a category.
- **`rename_columns`** – Rename the columns of the data log according to a mapping.
- **`subset_by_message`** – Subset the log by filtering the 'Message' column by a regexp pattern
- **`subset_by_pattern`** – Subset the log by filtering an attribute by a regexp pattern

Attributes:

- **`data`** (`DataFrame`) – The inner data of this data log

### data

```
data: DataFrame
```

The inner data of this data log

### bound_fitness

```
bound_fitness(obj_lims: Sequence[float] = None) -> DataFrame
```

Return a copy of the log data with the fitness measure bound by min/max limits

Parameters:

- **`obj_lims`** (`Sequence[float]`, default: `None` ) – min/max limits, length 2. Defaults to None.

Returns:

- `DataFrame` – pd.DataFrame: log data with bound fitness

### facet_plot

```
facet_plot(y: str, facet_category: str = 'Message', col_wrap: int = 3, x: str = 'PointNumber', fig_width_in=15, fig_heigth_in=10)
```

Facet plot of parameter value evolution, facetted by a category.

This method requires the package `seaborn` to be installed.

Parameters:

- **`y`** (`str`) – variable name (model parameter) to use for the y-axis, e.g. "x4" for GR4J
- **`facet_category`** (`str`, default: `'Message'` ) – Data attribute to use to facet. Defaults to "Message".
- **`col_wrap`** (`int`, default: `3` ) – Max number of columns in the plot. Defaults to 3.
- **`x`** (`str`, default: `'PointNumber'` ) – variable name (calibration iteration, or model parameter) to use for the x-axis. Defaults to "PointNumber".
- **`fig_width_in`** (`int`, default: `15` ) – figure width in inches. Defaults to 15.
- **`fig_heigth_in`** (`int`, default: `10` ) – figure height in inches. Defaults to 10.

Returns:

- **`FacetGrid`** – The plot to display

### rename_columns

```
rename_columns(colnames_map: Dict[str, str]) -> None
```

Rename the columns of the data log according to a mapping.

This is handy for instance to change fully qualified parameter names such as 'subarea.Wolf_Creek.x1' to just 'x1' to produce more legible plots.

Parameters:

- **`colnames_map`** (`Dict[str, str]`) – mapping

### subset_by_message

```
subset_by_message(pattern: str = 'Initial.*|Reflec.*|Contrac.*|Add.*') -> MhData
```

Subset the log by filtering the 'Message' column by a regexp pattern

Parameters:

- **`pattern`** (`str`, default: `'Initial.*|Reflec.*|Contrac.*|Add.*'` ) – regexp pattern, filter definition

Returns:

- **`Any`** ( `MhData` ) – New MhData object with subset data

### subset_by_pattern

```
subset_by_pattern(colname: str, pattern: str) -> MhData
```

Subset the log by filtering an attribute by a regexp pattern

Parameters:

- **`colname`** (`str`) – column name to filter on
- **`pattern`** (`str`) – regexp pattern, filter definition

Returns:

- **`Any`** ( `MhData` ) – New MhData object with subset data

## add_to_hypercube

```
add_to_hypercube(parameteriser, specs)
```

Add entries to a hypercube

Parameters:

- **`parameteriser`** (`HypercubeParameteriser`) – A HypercubeParameteriser wrapper, or a type inheriting from it
- **`specs`** (`DataFrame`) – An optional data frame description of the parameter set, with at least columns Name, Min, Max, Value.

## add_transform

```
add_transform(parameteriser: TransformParameteriser, param_name: str, inner_param_name: str, transform_id: str, a=1.0, b=0.0)
```

Create a parameteriser for which parameter transformations can be defined

```
This allows to define e.g. a virtual parameter log_X instead of calibrating on the parameter X.
```

Parameters:

- **`parameteriser`** (`TransformParameteriser`) – A TransformParameteriser wrapper, or a type inheriting from it
- **`param_name`** (`str`) – the name of the meta-parameter. Note that it can be the same value as inner_param_name, but this is NOT recommended.
- **`inner_param_name`** (`str`) – the name of the parameter being transformed
- **`transform_id`** (`str`) – identifier for a known bijective univariate function
- **`a`** (`float`, default: `1.0` ) – parameter in Y = F(ax+b). Defaults to 1.0.
- **`b`** (`float`, default: `0.0` ) – parameter in Y = F(ax+b). Defaults to 0.0.

## apply_sys_config

```
apply_sys_config(parameteriser, simulation)
```

Apply a model configuration to a simulation

Parameters:

- **`parameteriser`** (`HypercubeParameteriser`) – A HypercubeParameteriser wrapper, or a type inheriting from it
- **`simulation`** (`Simulation`) – simulation

## as_py_structure

```
as_py_structure(x: Any)
```

Try to convert an external pointer to a native python representation

Parameters:

- **`x`** (`Any`) – object, presumably wrapper around an Xptr, to convert to a 'pure' python representation

Returns:

- –

## backtransform

```
backtransform(parameteriser)
```

Get the parameteriser values in the untransformed space

Get the parameteriser values in the untransformed space, i.e. remove any transform added via wrapTransform. This allows to transform back e.g. from a virtual parameter log_X to the underlying model (or even virtual/meta) parameter X.

Parameters:

- **`parameteriser`** (`HypercubeParameteriser`) – A HypercubeParameteriser wrapper, or a type inheriting from it

Returns:

- – \[HypercubeParameteriser\]: The parameters definitions without the transforms (if there are any)

## bound_values

```
bound_values(x, lim: List = None)
```

## bound_values_df

```
bound_values_df(x, colname, lim=None)
```

min/max bound a column in a data frame

Parameters:

- **`x`** (`[type]`) – a data frame
- **`colname`** (`[type]`) – a character vector, name of the column to bound
- **`lim`** (`[type]`, default: `None` ) – a num vector of the min/max limits to apply, for instance c(0, 1). Defaults to None.

Returns:

- –

## concatenate_parameterisers

```
concatenate_parameterisers(*args: Sequence[HypercubeParameteriser], strategy: str = '') -> CompositeParameteriser
```

Concatenate hypercubes to a single parameteriser

Parameters:

- **`strategy`** (`str`, default: `''` ) – The strategy to contatenate. Defaults to "", equivalent to "composite", the only available. May have other options in the future.

Returns:

- **`CompositeParameteriser`** ( `CompositeParameteriser` ) – A concatenated parameteriser

## create_multisite_obj_parameteriser

```
create_multisite_obj_parameteriser(func_parameterisers, func_identifiers, prefixes=None, mix_func_parameteriser=None, hydro_parameteriser=None)
```

Builds a parameteriser usable with a multisite multiobjective calculator.

This is an advanced topic; users may refer to [this sample workflow](https://csiro-hydroinformatics.github.io/swift-py-doc/notebooks/calibrate_multisite/)

Parameters:

- **`func_parameterisers`** (`[type]`) – list of external pointers, parameterisers for each function of a multiobjective calculation.
- **`func_identifiers`** (`[type]`) – character, identifiers for each of the objectives defined in an multisite objective definition.
- **`prefixes`** (`[type]`, default: `None` ) – Optional prefixes to use to disambiguate short parameter names used in each function of a multiobjective calculator.. Defaults to None.
- **`mix_func_parameteriser`** (`[type]`, default: `None` ) – parameteriser, default None. (FUTURE) Optional parameteriser used in mixing the multiple objectives.. Defaults to None.
- **`hydro_parameteriser`** (`[type]`, default: `None` ) – parameteriser, default None. Optional parameteriser applied to the simulation model.. Defaults to None.

Returns:

- –

## create_muskingum_param_constraints

```
create_muskingum_param_constraints(inner_parameters, delta_t=1, param_name_k='K', param_name_x='X', simulation=None)
```

Create a parameteriser with Muskingum-type constraints. Given an existing parameteriser, create a wrapper that adds constraints on two of its parameters.

Parameters:

- **`inner_parameters`** (`[HypercubeParameteriser]`) – A SWIFT parameteriser object.
- **`delta_t`** (`int`, default: `1` ) – the simulation time step in HOURS. Defaults to 1.
- **`param_name_k`** (`str`, default: `'K'` ) – the variable identifier to use for the delay parameter of the Muskingum routing. Defaults to "K".
- **`param_name_x`** (`str`, default: `'X'` ) – the variable identifier to use for the attenuation parameter of the Muskingum routing. Defaults to "X".
- **`simulation`** (`[Simulation]`, default: `None` ) – the model simulation from which link properties are inspected to define constraints. The links' parameters must already be set.. Defaults to None.

Raises:

- `ValueError` – [description]

Returns:

- –

## create_parameter_sampler

```
create_parameter_sampler(seed, parameteriser, type: str)
```

Parameters:

- **`seed`** (`[type]`) – seed integer, the seed to use for the sampler
- **`parameteriser`** (`HypercubeParameteriser`) – A HypercubeParameteriser wrapper, or a type inheriting from it
- **`type`** (`str`) – identifying a method such as 'urs' for uniform random sampling.

Returns:

- –

## create_parameteriser

```
create_parameteriser(type='Generic subareas', specs: DataFrame = None)
```

Create a SWIFT parameteriser

Parameters:

- **`type`** (`str`, default: `'Generic subareas'` ) – A string identifying the (likely SWIFT-specific) type of parameteriser to use. Recognised types are (case insensitive) 'log-likelihood', 'generic', 'subareas', 'links', 'nodes' and 'muskingum'. Defaults to "Generic subareas".
- **`specs`** (`DataFrame`, default: `None` ) – An optional data frame description of the parameter set, with at least columns Name, Min, Max, Value. Defaults to None.

Returns:

- – \[HypercubeParameteriser\]: new parameteriser

## create_sce_optim_swift

```
create_sce_optim_swift(objective, termination_criterion, sce_params, population_initialiser)
```

Build an SCE optimiser for a SWIFT model

Parameters:

- **`objective`** (`ObjectiveEvaluator`) – an objective calculator
- **`termination_criterion`** (`SceTerminationCondition`) – An object that can be passed to SCE for testing the completion of the algorithm.
- **`sce_params`** (`dict`) – optional; parameters controlling the behavior of the SCE optimisers.
- **`population_initialiser`** (`CandidateFactorySeed`) – an S4 object 'ExternalObjRef' [package "cinterop"] with external pointer type HYPERCUBE_PTR or coercible to it, or a type of object that can seed a sampler i.e. coercible to a type CANDIDATE_FACTORY_SEED_WILA_PTR. If the argument is a hypercube, a uniform random sampler is created.

Returns:

- –

## create_sce_termination_wila

```
create_sce_termination_wila(type: str, arguments: Sequence[str]) -> SceTerminationCondition
```

Create a type of termination criteria suitable for the SCE algorithm.

Parameters:

- **`type`** (`str`) – A type of termination criterion; currently at least "relative standard deviation" and "maximum evaluations" are valid options
- **`arguments`** (`Sequence[str]`) – Arguments, in string forms even for numeric values, options for the selected type.

Returns:

- **`SceTerminationCondition`** ( `SceTerminationCondition` ) – [description]

## evaluate_score_for_parameters

```
evaluate_score_for_parameters(objective, parameteriser)
```

Computes the value of an objective for a given set of parameters

Parameters:

- **`objective`** (`[type]`) – an objective calculator
- **`parameteriser`** (`HypercubeParameteriser`) – A HypercubeParameteriser wrapper, or a type inheriting from it

Returns:

- –

## example_parameteriser

```
example_parameteriser(type: str, strict=False)
```

Get examples of typical parameterisers

Parameters:

- **`type`** (`str`) – identifier for a type of parameteriser including 'log-likelihood'
- **`strict`** (`bool`, default: `False` ) – If True an error is raised if the type is not found, otherwise a dummy empty parameteriser is returned.. Defaults to False.

Returns:

- –

## execute_optimisation

```
execute_optimisation(optimiser)
```

Launch an optimization task, as defined by the object passed as an argument

Parameters:

- **`optimiser`** (`Optimiser`) – the instance of the optimiser that has been created for the optimisation task about to be launched.

Returns:

- –

## extract_optimisation_log

```
extract_optimisation_log(estimator, fitness_name='log.likelihood') -> MhData
```

Extract the logger from a parameter extimator (optimiser or related)

Parameters:

- **`estimator`** (`Optimiser`) – the optimiser instance
- **`fitness_name`** (`str`, default: `'log.likelihood'` ) – name of the fitness function to extract. Defaults to "log.likelihood".

Returns:

- **`MhData`** ( `MhData` ) – an object with methods to analyse the optimisation log

## feasible_muskingum_bounds

```
feasible_muskingum_bounds(simulation: Simulation, delta_t_hours=1)
```

[summary]

Parameters:

- **`simulation`** (`Simulation`) – [description]
- **`delta_t_hours`** (`int`, default: `1` ) – [description]. Defaults to 1.

Returns:

- –

## filtered_parameters

```
filtered_parameters(parameteriser)
```

Wrap a parameteriser in a filter that can hide some parameters

Parameters:

- **`parameteriser`** (`HypercubeParameteriser`) – A HypercubeParameteriser wrapper, or a type inheriting from it. A deep copy of the input is taken.

Returns:

- –

## get_best_score

```
get_best_score(scores_population, score_name='NSE', convert_to_py=False)
```

Gets the best score in a population for a given objective

Parameters:

- **`scores_population`** (`[type]`) – an S4 object 'ExternalObjRef' [package "cinterop"] with external pointer type VEC_OBJECTIVE_SCORES_PTR
- **`score_name`** (`str`, default: `'NSE'` ) – name of the objective to use for sorting. Defaults to "NSE".
- **`convert_to_py`** (`bool`, default: `False` ) – should the returned score be converted to an R representation. Default False. Defaults to False.

Returns:

- –

## get_default_sce_parameters

```
get_default_sce_parameters()
```

[summary]

Returns:

- –

## get_logger_content

```
get_logger_content(optimiser: DeletableCffiNativeHandle, add_numbering: bool = False) -> DataFrame
```

Gets logger content on an optimiser, recorded detail of the optimisation process for post-optimisation analysis.

Parameters:

- **`optimiser`** (`[type]`) – the instance of the optimiser that has been created for the optimisation task about to be launched.
- **`add_numbering`** (`bool`, default: `False` ) – Add an explicit column for numbering the lines of the log. Defaults to False.

Returns:

- `DataFrame` – pd.DataFrame: The data log of the optimiser

## get_marginal_termination

```
get_marginal_termination(tolerance=1e-06, cutoff_no_improvement=10, max_hours=0.05)
```

Create an termination criterion based on the rate of marginal fitness improvement

Parameters:

- **`tolerance`** (`[type]`, default: `1e-06` ) – the increment in the objective below which the improvement is considered negligible. Defaults to 1e-06.
- **`cutoff_no_improvement`** (`int`, default: `10` ) – the maximum number of successive times the algorithm fails to improve the objective function.. Defaults to 10.
- **`max_hours`** (`float`, default: `0.05` ) – the maximum wall time runtime for the optimisation. Defaults to 0.05.

Returns:

- –

## get_max_iteration_termination

```
get_max_iteration_termination(max_iterations=1000)
```

Create an termination criterion based on the number of objective evaluations

Parameters:

- **`max_iterations`** (`int`, default: `1000` ) – number of iterations, which, if less than total count of optim objective evaluations, defines optim termination.. Defaults to 1000.

Returns:

- –

## get_max_runtime_termination

```
get_max_runtime_termination(max_hours=0.05)
```

Create an termination criterion based on the wall clock runtime

Parameters:

- **`max_hours`** (`float`, default: `0.05` ) – the maximum wall time runtime in hours for the optimisation. Defaults to 0.05.

Returns:

- –

## get_score_at_index

```
get_score_at_index(scores_population, index: int)
```

Get an objective scores in a vector thereof

Parameters:

- **`scores_population`** (`[type]`) – an S4 object 'ExternalObjRef' [package "cinterop"] with external pointer type VEC_OBJECTIVE_SCORES_PTR
- **`index`** (`int`) – one-based index in the population

Returns:

- –

## hide_parameters

```
hide_parameters(parameteriser, patterns, regex=False, starts_with=False, strict=False)
```

Hide some parameters (from the outside e.g. optimisers) in a filter parameteriser

Parameters:

- **`parameteriser`** (`HypercubeParameteriser`) – A HypercubeParameteriser wrapper, or a type inheriting from it
- **`patterns`** (`[type]`) – character, one or more pattern to match and hide matching parameters. Match according to other parameters.
- **`regex`** (`bool`, default: `False` ) – logical, defaults False, should the patterns be used as regular expressions.. Defaults to False.
- **`starts_with`** (`bool`, default: `False` ) – logical, defaults False. Ignored if regex is True. Should the patterns be used as starting strings in the parameter names.. Defaults to False.
- **`strict`** (`bool`, default: `False` ) – logical, default False. Used only if regex and starts_with are False. If True, raises an error if one of the "patterns" has no exact match in the parameters.. Defaults to False.

## is_hypercube

```
is_hypercube(p_set: CffiNativeHandle)
```

Is the object a native parameteriser that can be cast as a hypercube?

Parameters:

- **`p_set`** (`CffiNativeHandle`) – [description]

Returns:

- –

## is_sampler_seeding

```
is_sampler_seeding(obj: CffiNativeHandle)
```

Is the argument a native object that is a seeded candidate parameteriser factory

Parameters:

- **`obj`** (`CffiNativeHandle`) – [description]

Returns:

- –

## is_score

```
is_score(x)
```

OBJECTIVE_SCORES_WILA_PTR

Parameters:

- **`x`** (`[type]`) – [description]

Returns:

- –

## is_set_of_scores

```
is_set_of_scores(x)
```

VEC_OBJECTIVE_SCORES_PTR

Parameters:

- **`x`** (`[type]`) – [description]

Returns:

- –

## linear_parameteriser

```
linear_parameteriser(param_name: VecStr, state_name: VecStr, scaling_var_name: VecStr, min_p_val: VecNum, max_p_val: VecNum, value: VecNum, selector_type: str = 'subareas', intercept: VecNum = 0.0)
```

Create a scaled linear parameteriser, tying by a linear transformation a (resp several) model state to a (resp several) parameter values

This allows to define tied parameters where pval = a * modelStateVal + intercept. The intent in particular is to define virtual model parameters such as initial store value as a fraction of the maximum storage capacity.

Args:

```
param_name (VecStr): the name of the meta-parameter. Note that it can be the same value as inner_param_name without interference, though this may be confusing a choice.
state_name (VecStr): the name of the model state to modify, based on the value of the meta-parameter and the state found in 'scalingVarName'
scaling_var_name (VecStr): the name of the parameter for each subarea model, to which to apply the area scaled value.
min_p_val (VecNum): minimum value allowed for the meta-parameter
max_p_val (VecNum): minimum value allowed for the meta-parameter
value (VecNum): value for the meta parameter.
selector_type (str, optional): an identifier to define to which catchment element(s) the parameteriser will be applied. Defaults to "subareas".
intercept (VecNum, optional): intercepts in the linear relationship(s). Defaults to 0.0.
```

Returns:

- – \[ScalingParameteriser\]: new ScalingParameteriser

## linear_parameteriser_from

```
linear_parameteriser_from(data_frame: DataFrame, selector_type: str = 'subareas')
```

Create a scaled linear parameteriser, tying by a linear transformation a (resp several) model state to a (resp several) parameter values

This allows to define tied parameters where pval = a * modelStateVal + intercept. The intent in particular is to define virtual model parameters such as initial store value as a fraction of the maximum storage capacity. Args: data_frame (pd.DataFrame): data frame with columns "param_name", "state_name", "scaling_var_name", "min_value", "max_value", "value", "intercept", selector_type (str, optional): [description]. Defaults to "subareas".

Returns:

- –

## listify

```
listify(*args)
```

## make_state_init_parameteriser

```
make_state_init_parameteriser(parameteriser)
```

[summary]

Parameters:

- **`parameteriser`** (`HypercubeParameteriser`) – A HypercubeParameteriser wrapper, or a type inheriting from it

Returns:

- – \[StateInitParameteriser\]: new state initialisation parameteriser

## mk_optim_log

```
mk_optim_log(log_dataframe: DataFrame, fitness='NSE', messages='Message', categories='Category')
```

## num_free_parameters

```
num_free_parameters(parameteriser) -> int
```

## parameteriser_as_dataframe

```
parameteriser_as_dataframe(parameteriser)
```

Convert an external object hypercube parameteriser to a pandas data frame

Parameters:

- **`parameteriser`** (`HypercubeParameteriser`) – A HypercubeParameteriser wrapper, or a type inheriting from it

Returns:

- – \[type\]: [a data frame]

## parameteriser_for_score

```
parameteriser_for_score(score: ObjectiveScores)
```

Gets the parameteriser for a score

Parameters:

- **`score`** (`[type]`) – [description]

Returns:

- –

## parameters_for

```
parameters_for(model_id: str, as_pandas_df=False)
```

## scores_as_dataframe

```
scores_as_dataframe(scores_population)
```

Convert objective scores to a pandas data frame representation

Parameters:

- **`scores_population`** (`[type]`) – [description]

Returns:

- –

## set_calibration_logger

```
set_calibration_logger(optimiser, type='')
```

Sets logging on an optimiser, so as to record a detail of the optimisation process for post-optimisation analysis.

Parameters:

- **`optimiser`** (`[type]`) – [description]
- **`type`** (`str`, default: `''` ) – [description]. Defaults to "".

Returns:

- –

## set_hypercube

```
set_hypercube(parameteriser: HypercubeParameteriser, specs: DataFrame)
```

Set the properties of a hypercube parameteriser

Parameters:

- **`parameteriser`** (`HypercubeParameteriser`) – A HypercubeParameteriser wrapper, or a type inheriting from it
- **`specs`** (`DataFrame`) – An optional data frame description of the parameter set, with at least columns Name, Min, Max, Value.

## set_max_parameter_value

```
set_max_parameter_value(parameteriser, variable_name, value)
```

Sets the maximum value of a model parameter value

Parameters:

- **`parameteriser`** (`HypercubeParameteriser`) – A HypercubeParameteriser wrapper, or a type inheriting from it
- **`variable_name`** (`str or iterable of str`) – model variable state identifier(s)
- **`value`** (`numeric or iterable of numeric`) – value(s)

## set_min_parameter_value

```
set_min_parameter_value(parameteriser, variable_name, value)
```

Sets the minimum value of a model parameter value

Parameters:

- **`parameteriser`** (`HypercubeParameteriser`) – A HypercubeParameteriser wrapper, or a type inheriting from it
- **`variable_name`** (`str or iterable of str`) – model variable state identifier(s)
- **`value`** (`numeric or iterable of numeric`) – value(s)

## set_parameter_value

```
set_parameter_value(parameteriser, variable_name, value)
```

Sets the value of a model parameter value

Parameters:

- **`parameteriser`** (`HypercubeParameteriser`) – A HypercubeParameteriser wrapper, or a type inheriting from it
- **`variable_name`** (`str or iterable of str`) – model variable state identifier(s)
- **`value`** (`numeric or iterable of numeric`) – value(s)

## show_parameters

```
show_parameters(parameteriser, patterns, regex=False, starts_with=False)
```

Show some parameters (from the outside e.g. optimisers) in a filter parameteriser

Parameters:

- **`parameteriser`** (`HypercubeParameteriser`) – A HypercubeParameteriser wrapper, or a type inheriting from it
- **`patterns`** (`[type]`) – character, one or more pattern to match and show matching parameters. Match according to other parameters
- **`regex`** (`bool`, default: `False` ) – should the patterns be used as regular expressions. Defaults to False.
- **`starts_with`** (`bool`, default: `False` ) – should the patterns be used as starting strings in the parameter names. Defaults to False.

## sort_by_score

```
sort_by_score(scores_population, score_name='NSE')
```

Sort objective scores according to one of the objective values

Parameters:

- **`scores_population`** (`[type]`) – an S4 object 'ExternalObjRef' [package "cinterop"] with external pointer type VEC_OBJECTIVE_SCORES_PTR
- **`score_name`** (`str`, default: `'NSE'` ) – name of the objective to use for sorting. Defaults to "NSE".

Returns:

- **`VectorObjectiveScores`** – an S4 object 'ExternalObjRef' [package "cinterop"] with external pointer type VEC_OBJECTIVE_SCORES_PTR

## subcatchment_parameteriser

```
subcatchment_parameteriser(parameteriser, subcatchment)
```

Create a parameteriser that gets applied to a subset of a whole catchment

Parameters:

- **`parameteriser`** (`HypercubeParameteriser`) – A HypercubeParameteriser wrapper, or a type inheriting from it
- **`subcatchment`** (`Simulation`) – the subcatchment, subset of a whole catchment, identifying which elements (subareas, nodes, links) will be parameterised by the new parameteriser. Other catchment elements are untouched.

Returns:

- – \[HypercubeParameteriser\]: New parameteriser whose application is limited to the subcatchment.

Examples:

```
>>> sub_cats = simulation.split_to_subcatchments(["node.node_7", "node.node_10"])
>>> sc = sub_cats["node.node_7"]
>>> p = sp.create_parameteriser('generic subarea')
>>> p.add_parameter_to_hypercube("x1", 32, 1, 6e3)
>>> sp = p.subcatchment_parameteriser(sc)
>>> sp.apply_sys_config(simulation)
```

## wrap_transform

```
wrap_transform(parameteriser)
```

Create a parameteriser for which parameter transformations can be defined.

This allows to define e.g. a virtual parameter log_X instead of calibrating on the parameter X.

Parameters:

- **`parameteriser`** (`HypercubeParameteriser`) – A HypercubeParameteriser wrapper, or a type inheriting from it

Returns:

- **`TransformParameteriser`** – A new parameteriser (TransformParameteriser) which has methods to define parameter transforms
