# Module parameteriser

## `MhData`

Data log from metaheuristic calibration processes

Source code in `swift2/parameteriser.py`

```
class MhData:
    """Data log from metaheuristic calibration processes"""

    def __init__(
        self,
        data: pd.DataFrame,
        fitness: str = "NSE",
        messages: str = "Message",
        categories: str = "Category",
    ) -> None:
        self._fitness = fitness
        self._messages: str = messages
        self._categories: str = categories
        self._data: pd.DataFrame = data

    @property
    def data(self) -> pd.DataFrame:
        """The inner data of this data log"""
        return self._data

    def rename_columns(self, colnames_map: Dict[str, str]) -> None:
        """Rename the columns of the data log according to a mapping. 

        This is handy for instance to change fully qualified parameter names 
        such as 'subarea.Wolf_Creek.x1' to just 'x1' to produce more legible plots.

        Args:
            colnames_map (Dict[str, str]): mapping
        """        
        d = self._data.rename(colnames_map, axis=1, inplace=False)
        self._data = d

    def subset_by_pattern(self, colname: str, pattern: str) -> "MhData":
        """Subset the log by filtering an attribute by a regexp pattern

        Args:
            colname (str): column name to filter on
            pattern (str): regexp pattern, filter definition

        Returns:
            Any: New MhData object with subset data
        """
        criterion: pd.DataFrame = self._data[[colname]]
        indices = criterion.squeeze().str.match(pattern)
        data = self._data.loc[indices.values]
        return MhData(data, self._fitness, self._messages, self._categories)

    def bound_fitness(self, obj_lims: Sequence[float] = None) -> pd.DataFrame:
        """Return a copy of the log data with the fitness measure bound by min/max limits

        Args:
            obj_lims (Sequence[float], optional): min/max limits, length 2. Defaults to None.

        Returns:
            pd.DataFrame: log data with bound fitness
        """
        if obj_lims is None:
            return self._data
        d = self._data.copy()
        d = bound_values_df(d, self._fitness, obj_lims)
        return d

    def subset_by_message(
        self, pattern: str = "Initial.*|Reflec.*|Contrac.*|Add.*"
    ) -> "MhData":
        """Subset the log by filtering the 'Message' column by a regexp pattern

        Args:
            pattern (str): regexp pattern, filter definition

        Returns:
            Any: New MhData object with subset data
        """
        return self.subset_by_pattern(self._messages, pattern)

    def facet_plot(
        self,
        y: str,
        facet_category: str = "Message",
        col_wrap: int = 3,
        x: str = "PointNumber",
        fig_width_in=15,
        fig_heigth_in=10,
    ):
        """Facet plot of parameter value evolution, facetted by a category.

        This method requires the package `seaborn` to be installed.

        Args:
            y (str): variable name (model parameter) to use for the y-axis, e.g. "x4" for GR4J
            facet_category (str, optional): Data attribute to use to facet. Defaults to "Message".
            col_wrap (int, optional): Max number of columns in the plot. Defaults to 3.
            x (str, optional): variable name (calibration iteration, or model parameter) to use for the x-axis. Defaults to "PointNumber".
            fig_width_in (int, optional): figure width in inches. Defaults to 15.
            fig_heigth_in (int, optional): figure height in inches. Defaults to 10.

        Returns:
            FacetGrid: The plot to display
        """
        import seaborn as sns
        df = self.data
        grid = sns.FacetGrid(df, col = facet_category, col_wrap=col_wrap)
        grid.map(sns.scatterplot, x, y)
        grid.figure.set_size_inches(fig_width_in, fig_heigth_in)
        grid.add_legend()
        return grid

```

### `data`

The inner data of this data log

### `bound_fitness(obj_lims=None)`

Return a copy of the log data with the fitness measure bound by min/max limits

Parameters:

| Name | Type | Description | Default | | --- | --- | --- | --- | | `obj_lims` | `Sequence[float]` | min/max limits, length 2. Defaults to None. | `None` |

Returns:

| Type | Description | | --- | --- | | `DataFrame` | pd.DataFrame: log data with bound fitness |

Source code in `swift2/parameteriser.py`

```
def bound_fitness(self, obj_lims: Sequence[float] = None) -> pd.DataFrame:
    """Return a copy of the log data with the fitness measure bound by min/max limits

    Args:
        obj_lims (Sequence[float], optional): min/max limits, length 2. Defaults to None.

    Returns:
        pd.DataFrame: log data with bound fitness
    """
    if obj_lims is None:
        return self._data
    d = self._data.copy()
    d = bound_values_df(d, self._fitness, obj_lims)
    return d

```

### `facet_plot(y, facet_category='Message', col_wrap=3, x='PointNumber', fig_width_in=15, fig_heigth_in=10)`

Facet plot of parameter value evolution, facetted by a category.

This method requires the package `seaborn` to be installed.

Parameters:

| Name | Type | Description | Default | | --- | --- | --- | --- | | `y` | `str` | variable name (model parameter) to use for the y-axis, e.g. "x4" for GR4J | *required* | | `facet_category` | `str` | Data attribute to use to facet. Defaults to "Message". | `'Message'` | | `col_wrap` | `int` | Max number of columns in the plot. Defaults to 3. | `3` | | `x` | `str` | variable name (calibration iteration, or model parameter) to use for the x-axis. Defaults to "PointNumber". | `'PointNumber'` | | `fig_width_in` | `int` | figure width in inches. Defaults to 15. | `15` | | `fig_heigth_in` | `int` | figure height in inches. Defaults to 10. | `10` |

Returns:

| Name | Type | Description | | --- | --- | --- | | `FacetGrid` | | The plot to display |

Source code in `swift2/parameteriser.py`

```
def facet_plot(
    self,
    y: str,
    facet_category: str = "Message",
    col_wrap: int = 3,
    x: str = "PointNumber",
    fig_width_in=15,
    fig_heigth_in=10,
):
    """Facet plot of parameter value evolution, facetted by a category.

    This method requires the package `seaborn` to be installed.

    Args:
        y (str): variable name (model parameter) to use for the y-axis, e.g. "x4" for GR4J
        facet_category (str, optional): Data attribute to use to facet. Defaults to "Message".
        col_wrap (int, optional): Max number of columns in the plot. Defaults to 3.
        x (str, optional): variable name (calibration iteration, or model parameter) to use for the x-axis. Defaults to "PointNumber".
        fig_width_in (int, optional): figure width in inches. Defaults to 15.
        fig_heigth_in (int, optional): figure height in inches. Defaults to 10.

    Returns:
        FacetGrid: The plot to display
    """
    import seaborn as sns
    df = self.data
    grid = sns.FacetGrid(df, col = facet_category, col_wrap=col_wrap)
    grid.map(sns.scatterplot, x, y)
    grid.figure.set_size_inches(fig_width_in, fig_heigth_in)
    grid.add_legend()
    return grid

```

### `rename_columns(colnames_map)`

Rename the columns of the data log according to a mapping.

This is handy for instance to change fully qualified parameter names such as 'subarea.Wolf_Creek.x1' to just 'x1' to produce more legible plots.

Parameters:

| Name | Type | Description | Default | | --- | --- | --- | --- | | `colnames_map` | `Dict[str, str]` | mapping | *required* |

Source code in `swift2/parameteriser.py`

```
def rename_columns(self, colnames_map: Dict[str, str]) -> None:
    """Rename the columns of the data log according to a mapping. 

    This is handy for instance to change fully qualified parameter names 
    such as 'subarea.Wolf_Creek.x1' to just 'x1' to produce more legible plots.

    Args:
        colnames_map (Dict[str, str]): mapping
    """        
    d = self._data.rename(colnames_map, axis=1, inplace=False)
    self._data = d

```

### `subset_by_message(pattern='Initial.*|Reflec.*|Contrac.*|Add.*')`

Subset the log by filtering the 'Message' column by a regexp pattern

Parameters:

| Name | Type | Description | Default | | --- | --- | --- | --- | | `pattern` | `str` | regexp pattern, filter definition | `'Initial.*|Reflec.*|Contrac.*|Add.*'` |

Returns:

| Name | Type | Description | | --- | --- | --- | | `Any` | `MhData` | New MhData object with subset data |

Source code in `swift2/parameteriser.py`

```
def subset_by_message(
    self, pattern: str = "Initial.*|Reflec.*|Contrac.*|Add.*"
) -> "MhData":
    """Subset the log by filtering the 'Message' column by a regexp pattern

    Args:
        pattern (str): regexp pattern, filter definition

    Returns:
        Any: New MhData object with subset data
    """
    return self.subset_by_pattern(self._messages, pattern)

```

### `subset_by_pattern(colname, pattern)`

Subset the log by filtering an attribute by a regexp pattern

Parameters:

| Name | Type | Description | Default | | --- | --- | --- | --- | | `colname` | `str` | column name to filter on | *required* | | `pattern` | `str` | regexp pattern, filter definition | *required* |

Returns:

| Name | Type | Description | | --- | --- | --- | | `Any` | `MhData` | New MhData object with subset data |

Source code in `swift2/parameteriser.py`

```
def subset_by_pattern(self, colname: str, pattern: str) -> "MhData":
    """Subset the log by filtering an attribute by a regexp pattern

    Args:
        colname (str): column name to filter on
        pattern (str): regexp pattern, filter definition

    Returns:
        Any: New MhData object with subset data
    """
    criterion: pd.DataFrame = self._data[[colname]]
    indices = criterion.squeeze().str.match(pattern)
    data = self._data.loc[indices.values]
    return MhData(data, self._fitness, self._messages, self._categories)

```

## `add_to_hypercube(parameteriser, specs)`

Add entries to a hypercube

Parameters:

| Name | Type | Description | Default | | --- | --- | --- | --- | | `parameteriser` | `HypercubeParameteriser` | A HypercubeParameteriser wrapper, or a type inheriting from it | *required* | | `specs` | `DataFrame` | An optional data frame description of the parameter set, with at least columns Name, Min, Max, Value. | *required* |

Source code in `swift2/parameteriser.py`

```
def add_to_hypercube(parameteriser, specs):
    """Add entries to a hypercube

    Args:
        parameteriser (HypercubeParameteriser): A HypercubeParameteriser wrapper, or a type inheriting from it
        specs (pd.DataFrame): An optional data frame description of the parameter set, with at least columns Name, Min, Max, Value.
    """
    swc.add_parameters_pkg(parameteriser, specs)

```

## `add_transform(parameteriser, param_name, inner_param_name, transform_id, a=1.0, b=0.0)`

Create a parameteriser for which parameter transformations can be defined

```
This allows to define e.g. a virtual parameter log_X instead of calibrating on the parameter X.

```

Parameters:

| Name | Type | Description | Default | | --- | --- | --- | --- | | `parameteriser` | `TransformParameteriser` | A TransformParameteriser wrapper, or a type inheriting from it | *required* | | `param_name` | `str` | the name of the meta-parameter. Note that it can be the same value as inner_param_name, but this is NOT recommended. | *required* | | `inner_param_name` | `str` | the name of the parameter being transformed | *required* | | `transform_id` | `str` | identifier for a known bijective univariate function | *required* | | `a` | `float` | parameter in Y = F(ax+b). Defaults to 1.0. | `1.0` | | `b` | `float` | parameter in Y = F(ax+b). Defaults to 0.0. | `0.0` |

Source code in `swift2/parameteriser.py`

```
def add_transform(
    parameteriser: "TransformParameteriser",
    param_name: str,
    inner_param_name: str,
    transform_id: str,
    a=1.0,
    b=0.0,
):
    """Create a parameteriser for which parameter transformations can be defined

        This allows to define e.g. a virtual parameter log_X instead of calibrating on the parameter X.

    Args:
        parameteriser (TransformParameteriser): A TransformParameteriser wrapper, or a type inheriting from it
        param_name (str): the name of the meta-parameter. Note that it can be the same value as inner_param_name, but this is NOT recommended.
        inner_param_name (str): the name of the parameter being transformed
        transform_id (str): identifier for a known bijective univariate function
        a (float, optional): parameter in Y = F(ax+b). Defaults to 1.0.
        b (float, optional): parameter in Y = F(ax+b). Defaults to 0.0.
    """
    swg.AddParameterTransform_py(
        parameteriser, param_name, inner_param_name, transform_id, a, b
    )

```

## `apply_sys_config(parameteriser, simulation)`

Apply a model configuration to a simulation

Parameters:

| Name | Type | Description | Default | | --- | --- | --- | --- | | `parameteriser` | `HypercubeParameteriser` | A HypercubeParameteriser wrapper, or a type inheriting from it | *required* | | `simulation` | `Simulation` | simulation | *required* |

Source code in `swift2/parameteriser.py`

```
def apply_sys_config(parameteriser, simulation):
    """Apply a model configuration to a simulation

    Args:
        parameteriser (HypercubeParameteriser): A HypercubeParameteriser wrapper, or a type inheriting from it
        simulation (Simulation): simulation
    """
    if is_score(parameteriser):
        parameteriser = swg.GetSystemConfigurationWila_py(parameteriser)
    assert is_hypercube(parameteriser)
    swg.ApplyConfiguration_py(parameteriser, simulation)

```

## `as_py_structure(x)`

Try to convert an external pointer to a native python representation

Parameters:

| Name | Type | Description | Default | | --- | --- | --- | --- | | `x` | `Any` | object, presumably wrapper around an Xptr, to convert to a 'pure' python representation | *required* |

Returns:

| Type | Description | | --- | --- | | | |

Source code in `swift2/parameteriser.py`

```
def as_py_structure(x: Any):
    """Try to convert an external pointer to a native python representation

    Args:
        x (Any): object, presumably wrapper around an Xptr, to convert to a 'pure' python representation

    Returns:
        [type]: [description]
    """
    if not is_cffi_native_handle(x):
        return x
    if is_score(x):
        return swc.scores_as_rpy_dict_pkg(x)
    elif is_set_of_scores(x):
        return scores_as_dataframe(x)
    else:
        return x

```

## `backtransform(parameteriser)`

Get the parameteriser values in the untransformed space

Get the parameteriser values in the untransformed space, i.e. remove any transform added via wrapTransform. This allows to transform back e.g. from a virtual parameter log_X to the underlying model (or even virtual/meta) parameter X.

Parameters:

| Name | Type | Description | Default | | --- | --- | --- | --- | | `parameteriser` | `HypercubeParameteriser` | A HypercubeParameteriser wrapper, or a type inheriting from it | *required* |

Returns:

| Type | Description | | --- | --- | | | \[HypercubeParameteriser\]: The parameters definitions without the transforms (if there are any) |

Source code in `swift2/parameteriser.py`

```
def backtransform(parameteriser):
    """Get the parameteriser values in the untransformed space

    Get the parameteriser values in the untransformed space, i.e. remove any transform added via wrapTransform.
    This allows to transform back e.g. from a virtual parameter log_X to the underlying model (or even virtual/meta) parameter X.

    Args:
        parameteriser (HypercubeParameteriser): A HypercubeParameteriser wrapper, or a type inheriting from it

    Returns:
        [HypercubeParameteriser]: The parameters definitions without the transforms (if there are any)
    """
    return swg.UntransformHypercubeParameterizer_py(parameteriser)

```

## `bound_values_df(x, colname, lim=None)`

min/max bound a column in a data frame

Parameters:

| Name | Type | Description | Default | | --- | --- | --- | --- | | `x` | `[type]` | a data frame | *required* | | `colname` | `[type]` | a character vector, name of the column to bound | *required* | | `lim` | `[type]` | a num vector of the min/max limits to apply, for instance c(0, 1). Defaults to None. | `None` |

Returns:

| Type | Description | | --- | --- | | | |

Source code in `swift2/parameteriser.py`

```
def bound_values_df(x, colname, lim=None):
    """min/max bound a column in a data frame

    Args:
        x ([type]):   a data frame
        colname ([type]): a character vector, name of the column to bound
        lim ([type], optional): a num vector of the min/max limits to apply, for instance c(0, 1). Defaults to None.

    Returns:
        [type]: [description]
    """
    if lim is None:
        return x
    return x.assign(**{colname: bound_values(x[[colname]], lim)})

```

## `concatenate_parameterisers(*args, strategy='')`

Concatenate hypercubes to a single parameteriser

Parameters:

| Name | Type | Description | Default | | --- | --- | --- | --- | | `strategy` | `str` | The strategy to contatenate. Defaults to "", equivalent to "composite", the only available. May have other options in the future. | `''` |

Returns:

| Name | Type | Description | | --- | --- | --- | | `CompositeParameteriser` | `CompositeParameteriser` | A concatenated parameteriser |

Source code in `swift2/parameteriser.py`

```
def concatenate_parameterisers(
    *args: Sequence['HypercubeParameteriser'], strategy: str = ""
) -> "CompositeParameteriser":
    """Concatenate hypercubes to a single parameteriser

    Args:
        strategy (str, optional): The strategy to contatenate. Defaults to "", equivalent to "composite", the only available. May have other options in the future.

    Returns:
        CompositeParameteriser: A concatenated parameteriser
    """
    parameterisers = [x for x in args]
    return swc.aggregate_parameterisers_pkg(strategy, parameterisers)

```

## `create_multisite_obj_parameteriser(func_parameterisers, func_identifiers, prefixes=None, mix_func_parameteriser=None, hydro_parameteriser=None)`

Builds a parameteriser usable with a multisite multiobjective calculator.

Parameters:

| Name | Type | Description | Default | | --- | --- | --- | --- | | `func_parameterisers` | `[type]` | list of external pointers, parameterisers for each function of a multiobjective calculation. | *required* | | `func_identifiers` | `[type]` | character, identifiers for each of the objectives defined in an multisite objective definition. | *required* | | `prefixes` | `[type]` | Optional prefixes to use to disambiguate short parameter names used in each function of a multiobjective calculator.. Defaults to None. | `None` | | `mix_func_parameteriser` | `[type]` | parameteriser, default None. (FUTURE) Optional parameteriser used in mixing the multiple objectives.. Defaults to None. | `None` | | `hydro_parameteriser` | `[type]` | parameteriser, default None. Optional parameteriser applied to the simulation model.. Defaults to None. | `None` |

Returns:

| Type | Description | | --- | --- | | | |

Source code in `swift2/parameteriser.py`

```
def create_multisite_obj_parameteriser(
    func_parameterisers,
    func_identifiers,
    prefixes=None,
    mix_func_parameteriser=None,
    hydro_parameteriser=None,
):
    """Builds a parameteriser usable with a multisite multiobjective calculator.

    Args:
        func_parameterisers ([type]): list of external pointers, parameterisers for each function of a multiobjective calculation.
        func_identifiers ([type]): character, identifiers for each of the objectives defined in an multisite objective definition.
        prefixes ([type], optional): Optional prefixes to use to disambiguate short parameter names used in each function of a multiobjective calculator.. Defaults to None.
        mix_func_parameteriser ([type], optional): parameteriser, default None. (FUTURE) Optional parameteriser used in mixing the multiple objectives.. Defaults to None.
        hydro_parameteriser ([type], optional): parameteriser, default None. Optional parameteriser applied to the simulation model.. Defaults to None.

    Returns:
        [FunctionsParameteriser]: [description]
    """
    # stopifnot(is.list(func_parameterisers))
    # stopifnot(len(func_parameterisers) == len(func_identifiers))
    if not prefixes is None:
        assert len(func_parameterisers) == len(prefixes)
    cp = swg.CreateCompositeParameterizer_py()
    n = len(func_parameterisers)
    for i in range(n):
        swg.TagParameterizer_py(func_parameterisers[i], func_identifiers[i])
        if not prefixes is None:
            pp = swg.CreatePrefixingParameterizer_py(
                func_parameterisers[i], prefixes[i]
            )
            swg.AddToCompositeParameterizer_py(cp, pp)
        # else:
        #     TODO: what? forgot and the R implementation had a minor bug I think
        #     swg.AddToCompositeParameterizer_py(cp, pp)
    if not mix_func_parameteriser is None:
        swg.TagParameterizer_py(mix_func_parameteriser, "mixing_function")
        pmix_func_parameteriser = swg.CreatePrefixingParameterizer_py(
            mix_func_parameteriser, "mixing_function."
        )
        swg.AddToCompositeParameterizer_py(cp, pmix_func_parameteriser)
    if hydro_parameteriser is None:  # create a dummy
        hydro_parameteriser = swg.CreateHypercubeParameterizer_py("no apply")
    fp = swg.CreateFunctionsParameterizer_py(hydro_parameteriser, cp)
    return fp

```

## `create_muskingum_param_constraints(inner_parameters, delta_t=1, param_name_k='K', param_name_x='X', simulation=None)`

Create a parameteriser with Muskingum-type constraints. Given an existing parameteriser, create a wrapper that adds constraints on two of its parameters.

Parameters:

| Name | Type | Description | Default | | --- | --- | --- | --- | | `inner_parameters` | `[HypercubeParameteriser]` | A SWIFT parameteriser object. | *required* | | `delta_t` | `int` | the simulation time step in HOURS. Defaults to 1. | `1` | | `param_name_k` | `str` | the variable identifier to use for the delay parameter of the Muskingum routing. Defaults to "K". | `'K'` | | `param_name_x` | `str` | the variable identifier to use for the attenuation parameter of the Muskingum routing. Defaults to "X". | `'X'` | | `simulation` | `[Simulation]` | the model simulation from which link properties are inspected to define constraints. The links' parameters must already be set.. Defaults to None. | `None` |

Raises:

| Type | Description | | --- | --- | | `ValueError` | [description] |

Returns:

| Type | Description | | --- | --- | | | |

Source code in `swift2/parameteriser.py`

```
def create_muskingum_param_constraints(
    inner_parameters, delta_t=1, param_name_k="K", param_name_x="X", simulation=None
):
    """Create a parameteriser with Muskingum-type constraints. Given an existing parameteriser, create a wrapper that adds constraints on two of its parameters.

    Args:
        inner_parameters ([HypercubeParameteriser]): A SWIFT parameteriser object.
        delta_t (int, optional): the simulation time step in HOURS. Defaults to 1.
        param_name_k (str, optional): the variable identifier to use for the delay parameter of the Muskingum routing. Defaults to "K".
        param_name_x (str, optional): the variable identifier to use for the attenuation parameter of the Muskingum routing. Defaults to "X".
        simulation ([Simulation], optional): the model simulation from which link properties are inspected to define constraints. The links' parameters must already be set.. Defaults to None.

    Raises:
        ValueError: [description]

    Returns:
        [ConstraintParameteriser]: [description]
    """
    if simulation is None:
        raise ValueError("simulation argument must not be None")
    p = swg.CreateMuskingumConstraint_py(
        inner_parameters, delta_t, param_name_k, param_name_x, simulation
    )
    return p

```

## `create_parameter_sampler(seed, parameteriser, type)`

Parameters:

| Name | Type | Description | Default | | --- | --- | --- | --- | | `seed` | `[type]` | seed integer, the seed to use for the sampler | *required* | | `parameteriser` | `HypercubeParameteriser` | A HypercubeParameteriser wrapper, or a type inheriting from it | *required* | | `type` | `str` | identifying a method such as 'urs' for uniform random sampling. | *required* |

Returns:

| Type | Description | | --- | --- | | | |

Source code in `swift2/parameteriser.py`

```
def create_parameter_sampler(seed, parameteriser, type: str):
    """

    Args:
        seed ([type]): seed integer, the seed to use for the sampler
        parameteriser (HypercubeParameteriser): A HypercubeParameteriser wrapper, or a type inheriting from it
        type (str): identifying a method such as 'urs' for uniform random sampling.

    Returns:
        [type]: [description]
    """
    return swg.CreateCandidateFactorySeedWila_py(parameteriser, type, seed)

```

## `create_parameteriser(type='Generic subareas', specs=None)`

Create a SWIFT parameteriser

Parameters:

| Name | Type | Description | Default | | --- | --- | --- | --- | | `type` | `str` | A string identifying the (likely SWIFT-specific) type of parameteriser to use. Recognised types are (case insensitive) 'log-likelihood', 'generic', 'subareas', 'links', 'nodes' and 'muskingum'. Defaults to "Generic subareas". | `'Generic subareas'` | | `specs` | `DataFrame` | An optional data frame description of the parameter set, with at least columns Name, Min, Max, Value. Defaults to None. | `None` |

Returns:

| Type | Description | | --- | --- | | | \[HypercubeParameteriser\]: new parameteriser |

Source code in `swift2/parameteriser.py`

```
def create_parameteriser(type="Generic subareas", specs: pd.DataFrame = None):
    """Create a SWIFT parameteriser

    Args:
        type (str, optional): A string identifying the (likely SWIFT-specific) type of parameteriser to use. Recognised types are (case insensitive) 'log-likelihood', 'generic', 'subareas', 'links', 'nodes' and 'muskingum'. Defaults to "Generic subareas".
        specs (pd.DataFrame, optional): An optional data frame description of the parameter set, with at least columns Name, Min, Max, Value. Defaults to None.

    Returns:
        [HypercubeParameteriser]: new parameteriser
    """
    p = swg.CreateHypercubeParameterizer_py(strategy=type)
    # TODO: consider how to reuse mh::setHyperCube without introducing an undesirable package dependency
    # Maybe pass a function to a function in the mh package
    if specs is not None:
        add_to_hypercube(p, specs)
    return p

```

## `create_sce_optim_swift(objective, termination_criterion, sce_params, population_initialiser)`

Build an SCE optimiser for a SWIFT model

Parameters:

| Name | Type | Description | Default | | --- | --- | --- | --- | | `objective` | `ObjectiveEvaluator` | an objective calculator | *required* | | `termination_criterion` | `SceTerminationCondition` | An object that can be passed to SCE for testing the completion of the algorithm. | *required* | | `sce_params` | `dict` | optional; parameters controlling the behavior of the SCE optimisers. | *required* | | `population_initialiser` | `CandidateFactorySeed` | an S4 object 'ExternalObjRef' [package "cinterop"] with external pointer type HYPERCUBE_PTR or coercible to it, or a type of object that can seed a sampler i.e. coercible to a type CANDIDATE_FACTORY_SEED_WILA_PTR. If the argument is a hypercube, a uniform random sampler is created. | *required* |

Returns:

| Type | Description | | --- | --- | | | |

Source code in `swift2/parameteriser.py`

```
def create_sce_optim_swift(
    objective, termination_criterion, sce_params, population_initialiser
):
    """Build an SCE optimiser for a SWIFT model

    Args:
        objective ('ObjectiveEvaluator'):  an objective calculator
        termination_criterion ('SceTerminationCondition'):  An object that can be passed to SCE for testing the completion of the algorithm.
        sce_params (dict):  optional; parameters controlling the behavior of the SCE optimisers.
        population_initialiser ('CandidateFactorySeed'):  an S4 object 'ExternalObjRef' [package "cinterop"] with external pointer type HYPERCUBE_PTR or coercible to it, or a type of object that can seed a sampler i.e. coercible to a type CANDIDATE_FACTORY_SEED_WILA_PTR. If the argument is a hypercube, a uniform random sampler is created.

    Returns:
        [Optimiser]: [description]
    """

    if is_sampler_seeding(population_initialiser):
        # nothing to do.
        pass
    elif is_hypercube(population_initialiser):
        population_initialiser = create_parameter_sampler(
            0, population_initialiser, "urs"
        )
    else:
        raise ValueError(
            "population_initialiser must be provided (can be a sampler or a hypercube)"
        )
    # if(missing(terminationCriterion)) terminationCriterion = maxWallTimeTermination()
    # if(missing(SCEpars)) SCEpars = getDefaultSceParameters()
    if termination_criterion is None:
        max_hours = str(10 / 3600)
        termination_criterion = create_sce_termination_wila(
            "relative standard deviation", ["0.002", max_hours]
        )
    if sce_params is None:
        sce_params = get_default_sce_parameters()
    return swg.CreateShuffledComplexEvolutionWila_py(
        objective, termination_criterion, sce_params, population_initialiser
    )

```

## `create_sce_termination_wila(type, arguments)`

Create a type of termination criteria suitable for the SCE algorithm.

Parameters:

| Name | Type | Description | Default | | --- | --- | --- | --- | | `type` | `str` | A type of termination criterion; currently at least "relative standard deviation" and "maximum evaluations" are valid options | *required* | | `arguments` | `Sequence[str]` | Arguments, in string forms even for numeric values, options for the selected type. | *required* |

Returns:

| Name | Type | Description | | --- | --- | --- | | `SceTerminationCondition` | `SceTerminationCondition` | [description] |

Source code in `swift2/parameteriser.py`

```
def create_sce_termination_wila(
    type: str, arguments: Sequence[str]
) -> "SceTerminationCondition":
    """Create a type of termination criteria suitable for the SCE algorithm.

    Args:
        type (str): A type of termination criterion; currently at least "relative standard deviation" and "maximum evaluations" are valid options
        arguments (Sequence[str]): Arguments, in string forms even for numeric values, options for the selected type.

    Returns:
        SceTerminationCondition: [description]
    """
    return swg.CreateSceTerminationWila_py(type, arguments, len(arguments))

```

## `evaluate_score_for_parameters(objective, parameteriser)`

Computes the value of an objective for a given set of parameters

Parameters:

| Name | Type | Description | Default | | --- | --- | --- | --- | | `objective` | `[type]` | an objective calculator | *required* | | `parameteriser` | `HypercubeParameteriser` | A HypercubeParameteriser wrapper, or a type inheriting from it | *required* |

Returns:

| Type | Description | | --- | --- | | | |

Source code in `swift2/parameteriser.py`

```
def evaluate_score_for_parameters(objective, parameteriser):
    """Computes the value of an objective for a given set of parameters

    Args:
        objective ([type]): an objective calculator
        parameteriser (HypercubeParameteriser): A HypercubeParameteriser wrapper, or a type inheriting from it

    Returns:
        [type]: [description]
    """
    return swc.evaluate_score_wila_pkg(objective, parameteriser)

```

## `example_parameteriser(type, strict=False)`

Get examples of typical parameterisers

Parameters:

| Name | Type | Description | Default | | --- | --- | --- | --- | | `type` | `str` | identifier for a type of parameteriser including 'log-likelihood' | *required* | | `strict` | `bool` | If True an error is raised if the type is not found, otherwise a dummy empty parameteriser is returned.. Defaults to False. | `False` |

Returns:

| Type | Description | | --- | --- | | | |

Source code in `swift2/parameteriser.py`

```
def example_parameteriser(type: str, strict=False):
    """Get examples of typical parameterisers

    Args:
        type (str): identifier for a type of parameteriser including 'log-likelihood'
        strict (bool, optional): If True an error is raised if the type is not found, otherwise a dummy empty parameteriser is returned.. Defaults to False.

    Returns:
        [HypercubeParameteriser]: [description]
    """
    type = type.lower()
    if type == "log-likelihood":
        p = create_parameteriser(type="no apply")
        calc_m_and_s = 1.0  # meaning true
        censopt = 0.0
        add_to_hypercube(
            p,
            _df_from_dict(
                Name=["b", "m", "s", "a", "maxobs", "ct", "censopt", "calc_mod_m_s"],
                Min=_npf([-30, 0, 1, -30, 100.0, 0.01, censopt, calc_m_and_s]),
                Max=_npf([0, 0, 1000, 1, 100.0, 0.01, censopt, calc_m_and_s]),
                Value=_npf([-7, 0, 100, -10, 100.0, 0.01, censopt, calc_m_and_s]),
            ),
        )
        return p
    if not strict:
        return create_parameteriser(type="Generic")
    else:
        raise Exception("No example parameteriser yet for type " + type)

```

## `execute_optimisation(optimiser)`

Launch an optimization task, as defined by the object passed as an argument

Parameters:

| Name | Type | Description | Default | | --- | --- | --- | --- | | `optimiser` | `Optimiser` | the instance of the optimiser that has been created for the optimisation task about to be launched. | *required* |

Returns:

| Type | Description | | --- | --- | | | |

Source code in `swift2/parameteriser.py`

```
def execute_optimisation(optimiser):
    """Launch an optimization task, as defined by the object passed as an argument

    Args:
        optimiser (Optimiser): the instance of the optimiser that has been created for the optimisation task about to be launched.

    Returns:
        [VectorObjectiveScores]: [description]
    """
    return swg.ExecuteOptimizerWila_py(optimiser)

```

## `extract_optimisation_log(estimator, fitness_name='log.likelihood')`

Extract the logger from a parameter extimator (optimiser or related)

Parameters:

| Name | Type | Description | Default | | --- | --- | --- | --- | | `estimator` | `Optimiser` | the optimiser instance | *required* | | `fitness_name` | `str` | name of the fitness function to extract. Defaults to "log.likelihood". | `'log.likelihood'` |

Returns:

| Name | Type | Description | | --- | --- | --- | | `MhData` | `MhData` | an object with methods to analyse the optimisation log |

Source code in `swift2/parameteriser.py`

```
def extract_optimisation_log(estimator, fitness_name="log.likelihood") -> 'MhData':
    """Extract the logger from a parameter extimator (optimiser or related)

    Args:
        estimator (Optimiser): the optimiser instance
        fitness_name (str, optional): name of the fitness function to extract. Defaults to "log.likelihood".

    Returns:
        MhData: an object with methods to analyse the optimisation log
    """
    optim_log = get_logger_content(estimator, add_numbering=True)
    log_mh = mk_optim_log(
        optim_log, fitness=fitness_name, messages="Message", categories="Category"
    )
    # geom_ops = log_mh.subset_by_message()
    # return {"data": log_mh, "geom_ops": geom_ops}
    return log_mh

```

## `feasible_muskingum_bounds(simulation, delta_t_hours=1)`

[summary]

Parameters:

| Name | Type | Description | Default | | --- | --- | --- | --- | | `simulation` | `Simulation` | [description] | *required* | | `delta_t_hours` | `int` | [description]. Defaults to 1. | `1` |

Returns:

| Type | Description | | --- | --- | | | |

Source code in `swift2/parameteriser.py`

```
def feasible_muskingum_bounds(simulation: "Simulation", delta_t_hours=1):
    """[summary]

    Args:
        simulation (Simulation): [description]
        delta_t_hours (int, optional): [description]. Defaults to 1.

    Returns:
        [type]: [description]
    """
    return swg.GetFeasibleMuskingumBounds_py(simulation, delta_t_hours)

```

## `filtered_parameters(parameteriser)`

Wrap a parameteriser in a filter that can hide some parameters

Parameters:

| Name | Type | Description | Default | | --- | --- | --- | --- | | `parameteriser` | `HypercubeParameteriser` | A HypercubeParameteriser wrapper, or a type inheriting from it. A deep copy of the input is taken. | *required* |

Returns:

| Type | Description | | --- | --- | | | |

Source code in `swift2/parameteriser.py`

```
def filtered_parameters(parameteriser):
    """Wrap a parameteriser in a filter that can hide some parameters

    Args:
        parameteriser (HypercubeParameteriser): A HypercubeParameteriser wrapper, or a type inheriting from it. A deep copy of the input is taken.

    Returns:
        [FilteringParameteriser]: [description]
    """
    return swg.CreateFilteringParameterizer_py(parameteriser)

```

## `get_best_score(scores_population, score_name='NSE', convert_to_py=False)`

Gets the best score in a population for a given objective

Parameters:

| Name | Type | Description | Default | | --- | --- | --- | --- | | `scores_population` | `[type]` | an S4 object 'ExternalObjRef' [package "cinterop"] with external pointer type VEC_OBJECTIVE_SCORES_PTR | *required* | | `score_name` | `str` | name of the objective to use for sorting. Defaults to "NSE". | `'NSE'` | | `convert_to_py` | `bool` | should the returned score be converted to an R representation. Default False. Defaults to False. | `False` |

Returns:

| Type | Description | | --- | --- | | | |

Source code in `swift2/parameteriser.py`

```
def get_best_score(scores_population, score_name="NSE", convert_to_py=False):
    """Gets the best score in a population for a given objective

    Args:
        scores_population ([type]): an S4 object 'ExternalObjRef' [package "cinterop"] with external pointer type VEC_OBJECTIVE_SCORES_PTR
        score_name (str, optional): name of the objective to use for sorting. Defaults to "NSE".
        convert_to_py (bool, optional): should the returned score be converted to an R representation. Default False. Defaults to False.

    Returns:
        [ObjectiveScores or Dict]: [description]
    """
    sorted_results = sort_by_score(scores_population, score_name)
    s = get_score_at_index(sorted_results, 1)
    if convert_to_py:
        return swc.scores_as_rpy_dict_pkg(s)
    else:
        return s

```

## `get_default_sce_parameters()`

[summary]

Returns:

| Type | Description | | --- | --- | | | |

Source code in `swift2/parameteriser.py`

```
def get_default_sce_parameters():
    """[summary]

    Returns:
        [type]: [description]
    """
    from swift2.wrap.swift_wrap_custom import default_sce_parameters_pkg

    return default_sce_parameters_pkg()

```

## `get_logger_content(optimiser, add_numbering=False)`

Gets logger content on an optimiser, recorded detail of the optimisation process for post-optimisation analysis.

Parameters:

| Name | Type | Description | Default | | --- | --- | --- | --- | | `optimiser` | `[type]` | the instance of the optimiser that has been created for the optimisation task about to be launched. | *required* | | `add_numbering` | `bool` | Add an explicit column for numbering the lines of the log. Defaults to False. | `False` |

Returns:

| Type | Description | | --- | --- | | `DataFrame` | pd.DataFrame: The data log of the optimiser |

Source code in `swift2/parameteriser.py`

```
def get_logger_content(optimiser:DeletableCffiNativeHandle, add_numbering:bool=False) -> pd.DataFrame:
    """Gets logger content on an optimiser, recorded detail of the optimisation process for post-optimisation analysis.

    Args:
        optimiser ([type]): the instance of the optimiser that has been created for the optimisation task about to be launched.
        add_numbering (bool, optional): Add an explicit column for numbering the lines of the log. Defaults to False.

    Returns:
        pd.DataFrame: The data log of the optimiser
    """
    # coercion to data.frame is a workaround for https://jira.csiro.au/browse/WIRADA-245
    if is_cffi_native_handle(optimiser, type_id="ERRIS_STAGED_CALIBRATION_PTR"):
        log_data = swg.GetERRISCalibrationLog_py(optimiser)
    else:
        log_data = swg.GetOptimizerLogDataWila_py(optimiser)
    return convert_optimisation_logger(log_data, add_numbering)

```

## `get_marginal_termination(tolerance=1e-06, cutoff_no_improvement=10, max_hours=0.05)`

Create an termination criterion based on the rate of marginal fitness improvement

Parameters:

| Name | Type | Description | Default | | --- | --- | --- | --- | | `tolerance` | `[type]` | the increment in the objective below which the improvement is considered negligible. Defaults to 1e-06. | `1e-06` | | `cutoff_no_improvement` | `int` | the maximum number of successive times the algorithm fails to improve the objective function.. Defaults to 10. | `10` | | `max_hours` | `float` | the maximum wall time runtime for the optimisation. Defaults to 0.05. | `0.05` |

Returns:

| Type | Description | | --- | --- | | | |

Source code in `swift2/parameteriser.py`

```
def get_marginal_termination(tolerance=1e-06, cutoff_no_improvement=10, max_hours=0.05):
    """Create an termination criterion based on the rate of marginal fitness improvement

    Args:
        tolerance ([type], optional): the increment in the objective below which the improvement is considered negligible. Defaults to 1e-06.
        cutoff_no_improvement (int, optional): the maximum number of successive times the algorithm fails to improve the objective function.. Defaults to 10.
        max_hours (float, optional): the maximum wall time runtime for the optimisation. Defaults to 0.05.

    Returns:
        [SceTerminationCondition]: [description]
    """
    return swg.CreateSceMarginalTerminationWila_py(
        tolerance=tolerance,
        cutoffNoImprovement=cutoff_no_improvement,
        maxHours=max_hours,
    )

```

## `get_max_iteration_termination(max_iterations=1000)`

Create an termination criterion based on the number of objective evaluations

Parameters:

| Name | Type | Description | Default | | --- | --- | --- | --- | | `max_iterations` | `int` | number of iterations, which, if less than total count of optim objective evaluations, defines optim termination.. Defaults to 1000. | `1000` |

Returns:

| Type | Description | | --- | --- | | | |

Source code in `swift2/parameteriser.py`

```
def get_max_iteration_termination(max_iterations=1000):
    """Create an termination criterion based on the number of objective evaluations

    Args:
        max_iterations (int, optional): number of iterations, which, if less than total count of optim objective evaluations, defines optim termination.. Defaults to 1000.

    Returns:
        [SceTerminationCondition]: [description]
    """
    return swg.CreateSceMaxIterationTerminationWila_py(maxIterations=max_iterations)

```

## `get_max_runtime_termination(max_hours=0.05)`

Create an termination criterion based on the wall clock runtime

Parameters:

| Name | Type | Description | Default | | --- | --- | --- | --- | | `max_hours` | `float` | the maximum wall time runtime in hours for the optimisation. Defaults to 0.05. | `0.05` |

Returns:

| Type | Description | | --- | --- | | | |

Source code in `swift2/parameteriser.py`

```
def get_max_runtime_termination(max_hours=0.05):
    """Create an termination criterion based on the wall clock runtime

    Args:
        max_hours (float, optional): the maximum wall time runtime in hours for the optimisation. Defaults to 0.05.

    Returns:
        [SceTerminationCondition]: [description]
    """
    return swg.CreateSceMaxRuntimeTerminationWila_py(maxHours=max_hours)

```

## `get_score_at_index(scores_population, index)`

Get an objective scores in a vector thereof

Parameters:

| Name | Type | Description | Default | | --- | --- | --- | --- | | `scores_population` | `[type]` | an S4 object 'ExternalObjRef' [package "cinterop"] with external pointer type VEC_OBJECTIVE_SCORES_PTR | *required* | | `index` | `int` | one-based index in the population | *required* |

Returns:

| Type | Description | | --- | --- | | | |

Source code in `swift2/parameteriser.py`

```
def get_score_at_index(scores_population, index: int):
    """Get an objective scores in a vector thereof

    Args:
        scores_population ([type]): an S4 object 'ExternalObjRef' [package "cinterop"] with external pointer type VEC_OBJECTIVE_SCORES_PTR
        index (int): one-based index in the population

    Returns:
        [ObjectiveScores]: [description]
    """
    return swg.GetScoresAtIndex_py(scores_population, index - 1)

```

## `hide_parameters(parameteriser, patterns, regex=False, starts_with=False, strict=False)`

Hide some parameters (from the outside e.g. optimisers) in a filter parameteriser

Parameters:

| Name | Type | Description | Default | | --- | --- | --- | --- | | `parameteriser` | `HypercubeParameteriser` | A HypercubeParameteriser wrapper, or a type inheriting from it | *required* | | `patterns` | `[type]` | character, one or more pattern to match and hide matching parameters. Match according to other parameters. | *required* | | `regex` | `bool` | logical, defaults False, should the patterns be used as regular expressions.. Defaults to False. | `False` | | `starts_with` | `bool` | logical, defaults False. Ignored if regex is True. Should the patterns be used as starting strings in the parameter names.. Defaults to False. | `False` | | `strict` | `bool` | logical, default False. Used only if regex and starts_with are False. If True, raises an error if one of the "patterns" has no exact match in the parameters.. Defaults to False. | `False` |

Source code in `swift2/parameteriser.py`

```
def hide_parameters(
    parameteriser, patterns, regex=False, starts_with=False, strict=False
):
    """Hide some parameters (from the outside e.g. optimisers) in a filter parameteriser

    Args:
        parameteriser (HypercubeParameteriser): A HypercubeParameteriser wrapper, or a type inheriting from it
        patterns ([type]):  character, one or more pattern to match and hide matching parameters. Match according to other parameters.
        regex (bool, optional): logical, defaults False, should the patterns be used as regular expressions.. Defaults to False.
        starts_with (bool, optional): logical, defaults False. Ignored if regex is True. Should the patterns be used as starting strings in the parameter names.. Defaults to False.
        strict (bool, optional): logical, default False. Used only if regex and starts_with are False. If True, raises an error if one of the "patterns" has no exact match in the parameters.. Defaults to False.
    """
    swg.HideParameters_py(parameteriser, patterns, regex, starts_with, strict)

```

## `is_hypercube(p_set)`

Is the object a native parameteriser that can be cast as a hypercube?

Parameters:

| Name | Type | Description | Default | | --- | --- | --- | --- | | `p_set` | `CffiNativeHandle` | [description] | *required* |

Returns:

| Type | Description | | --- | --- | | | |

Source code in `swift2/parameteriser.py`

```
def is_hypercube(p_set: CffiNativeHandle):
    """Is the object a native parameteriser that can be cast as a hypercube?

    Args:
        p_set (CffiNativeHandle): [description]

    Returns:
        [type]: [description]
    """
    # TODO: implement a SWIFT API function to check this.
    # KLUDGE:
    from refcount.interop import is_cffi_native_handle

    return is_cffi_native_handle(p_set) and p_set.type_id in [
        "HYPERCUBE_PTR",
        "COMPOSITE_PARAMETERIZER_PTR",
        "FUNCTIONS_PARAMETERIZER_PTR",
        "CONSTRAINT_PARAMETERIZER_PTR",
        "SCALING_PARAMETERIZER_PTR",
        "STATE_INIT_PARAMETERIZER_PTR",
        "TRANSFORM_PARAMETERIZER_PTR",
        "STATE_INITIALIZER_PTR",
        "SUBAREAS_SCALING_PARAMETERIZER_PTR",
        "HYPERCUBE_WILA_PTR",
        "XPtr<OpaquePointer>",  # TODO this is to circumvent issues now that some functions are generated from Rcpp code rather than API. See e.g. aggregate_parameterisers_pkg
    ]

```

## `is_sampler_seeding(obj)`

Is the argument a native object that is a seeded candidate parameteriser factory

Parameters:

| Name | Type | Description | Default | | --- | --- | --- | --- | | `obj` | `CffiNativeHandle` | [description] | *required* |

Returns:

| Type | Description | | --- | --- | | | |

Source code in `swift2/parameteriser.py`

```
def is_sampler_seeding(obj: CffiNativeHandle):
    """Is the argument a native object that is a seeded candidate parameteriser factory

    Args:
        obj (CffiNativeHandle): [description]

    Returns:
        [type]: [description]
    """
    # KLUDGE:
    from refcount.interop import is_cffi_native_handle

    return is_cffi_native_handle(obj, "CANDIDATE_FACTORY_SEED_WILA_PTR")

```

## `is_score(x)`

OBJECTIVE_SCORES_WILA_PTR

Parameters:

| Name | Type | Description | Default | | --- | --- | --- | --- | | `x` | `[type]` | [description] | *required* |

Returns:

| Type | Description | | --- | --- | | | |

Source code in `swift2/parameteriser.py`

```
def is_score(x):
    """OBJECTIVE_SCORES_WILA_PTR

    Args:
        x ([type]): [description]

    Returns:
        [type]: [description]
    """
    # TODO: implement a SWIFT API function to check this.
    # KLUDGE?:
    return is_cffi_native_handle(x, type_id="OBJECTIVE_SCORES_WILA_PTR")

```

## `is_set_of_scores(x)`

VEC_OBJECTIVE_SCORES_PTR

Parameters:

| Name | Type | Description | Default | | --- | --- | --- | --- | | `x` | `[type]` | [description] | *required* |

Returns:

| Type | Description | | --- | --- | | | |

Source code in `swift2/parameteriser.py`

```
def is_set_of_scores(x):
    """VEC_OBJECTIVE_SCORES_PTR

    Args:
        x ([type]): [description]

    Returns:
        [type]: [description]
    """
    return is_cffi_native_handle(x, type_id="VEC_OBJECTIVE_SCORES_PTR")

```

## `linear_parameteriser(param_name, state_name, scaling_var_name, min_p_val, max_p_val, value, selector_type='subareas', intercept=0.0)`

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

| Type | Description | | --- | --- | | | \[ScalingParameteriser\]: new ScalingParameteriser |

Source code in `swift2/parameteriser.py`

```
def linear_parameteriser(
    param_name: VecStr,
    state_name: VecStr,
    scaling_var_name: VecStr,
    min_p_val: VecNum,
    max_p_val: VecNum,
    value: VecNum,
    selector_type: str = "subareas",
    intercept: VecNum = 0.0,
):
    """Create a scaled linear parameteriser, tying by a linear transformation a (resp several) model state to a (resp several) parameter values

    This allows to define tied parameters where pval = a * modelStateVal + intercept.
    The intent in particular is to define virtual model parameters such as initial store value as a fraction of the maximum storage capacity.

    Args:

        param_name (VecStr): the name of the meta-parameter. Note that it can be the same value as inner_param_name without interference, though this may be confusing a choice.
        state_name (VecStr): the name of the model state to modify, based on the value of the meta-parameter and the state found in 'scalingVarName'
        scaling_var_name (VecStr): the name of the parameter for each subarea model, to which to apply the area scaled value.
        min_p_val (VecNum): minimum value allowed for the meta-parameter
        max_p_val (VecNum): minimum value allowed for the meta-parameter
        value (VecNum): value for the meta parameter.
        selector_type (str, optional): an identifier to define to which catchment element(s) the parameteriser will be applied. Defaults to "subareas".
        intercept (VecNum, optional): intercepts in the linear relationship(s). Defaults to 0.0.

    Returns:
        [ScalingParameteriser]: new ScalingParameteriser
    """
    # stopifnot(len(selectorType) == 1)
    param_name, state_name, scaling_var_name, min_p_val, max_p_val, value = listify(
        param_name, state_name, scaling_var_name, min_p_val, max_p_val, value
    )
    lengths = [
        len(x)
        for x in [param_name, state_name, scaling_var_name, min_p_val, max_p_val, value]
    ]
    if len(set(lengths)) != 1:
        raise Exception(
            "arguments must all be vectors of same length: param_name, state_name, scalingVarName, minPval, maxPval, value"
        )
    if not is_common_iterable(intercept):
        intercept = np.repeat(intercept, lengths[0])
    elif len(intercept) != lengths[0]:
        raise Exception(
            'argument "intercept" be of length 1 or the same as: param_name, state_name, scalingVarName, minPval, maxPval, value'
        )
    p = swg.CreateTargetScalingParameterizer_py(selector_type)
    for i in range(lengths[0]):
        swg.AddLinearScalingParameterizer_py(
            p,
            param_name[i],
            state_name[i],
            scaling_var_name[i],
            intercept[i],
            min_p_val[i],
            max_p_val[i],
            value[i],
        )
    return p

```

## `linear_parameteriser_from(data_frame, selector_type='subareas')`

Create a scaled linear parameteriser, tying by a linear transformation a (resp several) model state to a (resp several) parameter values

This allows to define tied parameters where pval = a * modelStateVal + intercept. The intent in particular is to define virtual model parameters such as initial store value as a fraction of the maximum storage capacity. Args: data_frame (pd.DataFrame): data frame with columns "param_name", "state_name", "scaling_var_name", "min_value", "max_value", "value", "intercept", selector_type (str, optional): [description]. Defaults to "subareas".

Returns:

| Type | Description | | --- | --- | | | |

Source code in `swift2/parameteriser.py`

```
def linear_parameteriser_from(
    data_frame: pd.DataFrame, selector_type: str = "subareas"
):
    """Create a scaled linear parameteriser, tying by a linear transformation a (resp several) model state to a (resp several) parameter values

    This allows to define tied parameters where pval = a * modelStateVal + intercept.
    The intent in particular is to define virtual model parameters such as initial store value as a fraction of the maximum storage capacity.
    Args:
        data_frame (pd.DataFrame): data frame with columns "param_name", "state_name", "scaling_var_name", "min_value", "max_value", "value", "intercept",
        selector_type (str, optional): [description]. Defaults to "subareas".

    Returns:
        [ScalingParameteriser]: ScalingParameteriser
    """
    return linear_parameteriser(
        param_name=data_frame[[PARAM_NAME_COL]],
        state_name=data_frame[[STATE_NAME_COL]],
        scaling_var_name=data_frame[[SCALING_VAR_NAME_COL]],
        min_p_val=data_frame[[MIN_VALUE_COL]],
        max_p_val=data_frame[[MAX_VALUE_COL]],
        value=data_frame[[VALUE_COL]],
        selector_type=selector_type,
        intercept=data_frame[[INTERCEPT_COL]],
    )

```

## `make_state_init_parameteriser(parameteriser)`

[summary]

Parameters:

| Name | Type | Description | Default | | --- | --- | --- | --- | | `parameteriser` | `HypercubeParameteriser` | A HypercubeParameteriser wrapper, or a type inheriting from it | *required* |

Returns:

| Type | Description | | --- | --- | | | \[StateInitParameteriser\]: new state initialisation parameteriser |

Source code in `swift2/parameteriser.py`

```
def make_state_init_parameteriser(parameteriser):
    """[summary]

    Args:
        parameteriser (HypercubeParameteriser): A HypercubeParameteriser wrapper, or a type inheriting from it

    Returns:
        [StateInitParameteriser]: new state initialisation parameteriser
    """
    return swg.CreateStateInitParameterizer_py(parameteriser)

```

## `parameteriser_as_dataframe(parameteriser)`

Convert an external object hypercube parameteriser to a pandas data frame

Parameters:

| Name | Type | Description | Default | | --- | --- | --- | --- | | `parameteriser` | `HypercubeParameteriser` | A HypercubeParameteriser wrapper, or a type inheriting from it | *required* |

Returns:

| Type | Description | | --- | --- | | | \[type\]: [a data frame] |

Source code in `swift2/parameteriser.py`

```
def parameteriser_as_dataframe(parameteriser):
    """Convert an external object hypercube parameteriser to a pandas data frame

    Args:
        parameteriser (HypercubeParameteriser): A HypercubeParameteriser wrapper, or a type inheriting from it

    Returns:
        [type]: [a data frame]
    """
    return swc.parameteriser_to_data_frame_pkg(parameteriser)

```

## `parameteriser_for_score(score)`

Gets the parameteriser for a score

Parameters:

| Name | Type | Description | Default | | --- | --- | --- | --- | | `score` | `[type]` | [description] | *required* |

Returns:

| Type | Description | | --- | --- | | | |

Source code in `swift2/parameteriser.py`

```
def parameteriser_for_score(score:'ObjectiveScores'):
    """Gets the parameteriser for a score

    Args:
        score ([type]): [description]

    Returns:
        [HypercubeParameteriser]: [description]
    """
    return swg.GetSystemConfigurationWila_py(score)

```

## `scores_as_dataframe(scores_population)`

Convert objective scores to a pandas data frame representation

Parameters:

| Name | Type | Description | Default | | --- | --- | --- | --- | | `scores_population` | `[type]` | [description] | *required* |

Returns:

| Type | Description | | --- | --- | | | |

Source code in `swift2/parameteriser.py`

```
def scores_as_dataframe(scores_population):
    """Convert objective scores to a pandas data frame representation

    Args:
        scores_population ([type]): [description]

    Returns:
        [type]: [description]
    """
    return swc.vec_scores_as_dataframe_pkg(scores_population)

```

## `set_calibration_logger(optimiser, type='')`

Sets logging on an optimiser, so as to record a detail of the optimisation process for post-optimisation analysis.

Parameters:

| Name | Type | Description | Default | | --- | --- | --- | --- | | `optimiser` | `[type]` | [description] | *required* | | `type` | `str` | [description]. Defaults to "". | `''` |

Returns:

| Type | Description | | --- | --- | | | |

Source code in `swift2/parameteriser.py`

```
def set_calibration_logger(optimiser, type=""):
    """Sets logging on an optimiser, so as to record a detail of the optimisation process for post-optimisation analysis.

    Args:
        optimiser ([type]): [description]
        type (str, optional): [description]. Defaults to "".

    Returns:
        [type]: [description]
    """
    return swg.SetOptimizerLoggerWila_py(optimiser, type)

```

## `set_hypercube(parameteriser, specs)`

Set the properties of a hypercube parameteriser

Parameters:

| Name | Type | Description | Default | | --- | --- | --- | --- | | `parameteriser` | `HypercubeParameteriser` | A HypercubeParameteriser wrapper, or a type inheriting from it | *required* | | `specs` | `DataFrame` | An optional data frame description of the parameter set, with at least columns Name, Min, Max, Value. | *required* |

Source code in `swift2/parameteriser.py`

```
def set_hypercube(parameteriser: "HypercubeParameteriser", specs: pd.DataFrame):
    """Set the properties of a hypercube parameteriser

    Args:
        parameteriser (HypercubeParameteriser): A HypercubeParameteriser wrapper, or a type inheriting from it
        specs (pd.DataFrame): An optional data frame description of the parameter set, with at least columns Name, Min, Max, Value.
    """
    swc.set_parameters_pkg(parameteriser, specs)

```

## `set_max_parameter_value(parameteriser, variable_name, value)`

Sets the maximum value of a model parameter value

Parameters:

| Name | Type | Description | Default | | --- | --- | --- | --- | | `parameteriser` | `HypercubeParameteriser` | A HypercubeParameteriser wrapper, or a type inheriting from it | *required* | | `variable_name` | `str or iterable of str` | model variable state identifier(s) | *required* | | `value` | `numeric or iterable of numeric` | value(s) | *required* |

Source code in `swift2/parameteriser.py`

```
def set_max_parameter_value(parameteriser, variable_name, value):
    """Sets the maximum value of a model parameter value

    Args:
        parameteriser (HypercubeParameteriser): A HypercubeParameteriser wrapper, or a type inheriting from it
        variable_name (str or iterable of str): model variable state identifier(s)
        value (numeric or iterable of numeric): value(s)
    """
    _sapply_parameter_set(
        parameteriser, variable_name, value, swg.SetMaxParameterValue_py
    )

```

## `set_min_parameter_value(parameteriser, variable_name, value)`

Sets the minimum value of a model parameter value

Parameters:

| Name | Type | Description | Default | | --- | --- | --- | --- | | `parameteriser` | `HypercubeParameteriser` | A HypercubeParameteriser wrapper, or a type inheriting from it | *required* | | `variable_name` | `str or iterable of str` | model variable state identifier(s) | *required* | | `value` | `numeric or iterable of numeric` | value(s) | *required* |

Source code in `swift2/parameteriser.py`

```
def set_min_parameter_value(parameteriser, variable_name, value):
    """Sets the minimum value of a model parameter value

    Args:
        parameteriser (HypercubeParameteriser): A HypercubeParameteriser wrapper, or a type inheriting from it
        variable_name (str or iterable of str): model variable state identifier(s)
        value (numeric or iterable of numeric): value(s)
    """
    _sapply_parameter_set(
        parameteriser, variable_name, value, swg.SetMinParameterValue_py
    )

```

## `set_parameter_value(parameteriser, variable_name, value)`

Sets the value of a model parameter value

Parameters:

| Name | Type | Description | Default | | --- | --- | --- | --- | | `parameteriser` | `HypercubeParameteriser` | A HypercubeParameteriser wrapper, or a type inheriting from it | *required* | | `variable_name` | `str or iterable of str` | model variable state identifier(s) | *required* | | `value` | `numeric or iterable of numeric` | value(s) | *required* |

Source code in `swift2/parameteriser.py`

```
def set_parameter_value(parameteriser, variable_name, value):
    """Sets the value of a model parameter value

    Args:
        parameteriser (HypercubeParameteriser): A HypercubeParameteriser wrapper, or a type inheriting from it
        variable_name (str or iterable of str): model variable state identifier(s)
        value (numeric or iterable of numeric): value(s)
    """
    _sapply_parameter_set(parameteriser, variable_name, value, swg.SetParameterValue_py)

```

## `show_parameters(parameteriser, patterns, regex=False, starts_with=False)`

Show some parameters (from the outside e.g. optimisers) in a filter parameteriser

Parameters:

| Name | Type | Description | Default | | --- | --- | --- | --- | | `parameteriser` | `HypercubeParameteriser` | A HypercubeParameteriser wrapper, or a type inheriting from it | *required* | | `patterns` | `[type]` | character, one or more pattern to match and show matching parameters. Match according to other parameters | *required* | | `regex` | `bool` | should the patterns be used as regular expressions. Defaults to False. | `False` | | `starts_with` | `bool` | should the patterns be used as starting strings in the parameter names. Defaults to False. | `False` |

Source code in `swift2/parameteriser.py`

```
def show_parameters(parameteriser, patterns, regex=False, starts_with=False):
    """Show some parameters (from the outside e.g. optimisers) in a filter parameteriser

    Args:
        parameteriser (HypercubeParameteriser): A HypercubeParameteriser wrapper, or a type inheriting from it
        patterns ([type]):  character, one or more pattern to match and show matching parameters. Match according to other parameters
        regex (bool, optional): should the patterns be used as regular expressions. Defaults to False.
        starts_with (bool, optional): should the patterns be used as starting strings in the parameter names. Defaults to False.
    """
    swg.ShowParameters_py(parameteriser, patterns, regex, starts_with)

```

## `sort_by_score(scores_population, score_name='NSE')`

Sort objective scores according to one of the objective values

Parameters:

| Name | Type | Description | Default | | --- | --- | --- | --- | | `scores_population` | `[type]` | an S4 object 'ExternalObjRef' [package "cinterop"] with external pointer type VEC_OBJECTIVE_SCORES_PTR | *required* | | `score_name` | `str` | name of the objective to use for sorting. Defaults to "NSE". | `'NSE'` |

Returns:

| Name | Type | Description | | --- | --- | --- | | `VectorObjectiveScores` | | an S4 object 'ExternalObjRef' [package "cinterop"] with external pointer type VEC_OBJECTIVE_SCORES_PTR |

Source code in `swift2/parameteriser.py`

```
def sort_by_score(scores_population, score_name="NSE"):
    """Sort objective scores according to one of the objective values

    Args:
        scores_population ([type]): an S4 object 'ExternalObjRef' [package "cinterop"] with external pointer type VEC_OBJECTIVE_SCORES_PTR
        score_name (str, optional): name of the objective to use for sorting. Defaults to "NSE".

    Returns:
        VectorObjectiveScores: an S4 object 'ExternalObjRef' [package "cinterop"] with external pointer type VEC_OBJECTIVE_SCORES_PTR
    """
    return swg.SortSetOfScoresBy_py(scores_population, score_name)

```

## `subcatchment_parameteriser(parameteriser, subcatchment)`

Create a parameteriser that gets applied to a subset of a whole catchment

Parameters:

| Name | Type | Description | Default | | --- | --- | --- | --- | | `parameteriser` | `HypercubeParameteriser` | A HypercubeParameteriser wrapper, or a type inheriting from it | *required* | | `subcatchment` | `Simulation` | the subcatchment, subset of a whole catchment, identifying which elements (subareas, nodes, links) will be parameterised by the new parameteriser. Other catchment elements are untouched. | *required* |

Returns:

| Type | Description | | --- | --- | | | \[HypercubeParameteriser\]: New parameteriser whose application is limited to the subcatchment. |

Examples:

```
>>> sub_cats = simulation.split_to_subcatchments(["node.node_7", "node.node_10"])
>>> sc = sub_cats["node.node_7"]
>>> p = sp.create_parameteriser('generic subarea')
>>> p.add_parameter_to_hypercube("x1", 32, 1, 6e3)
>>> sp = p.subcatchment_parameteriser(sc)
>>> sp.apply_sys_config(simulation)

```

Source code in `swift2/parameteriser.py`

```
def subcatchment_parameteriser(parameteriser, subcatchment):
    """Create a parameteriser that gets applied to a subset of a whole catchment

    Args:
        parameteriser (HypercubeParameteriser): A HypercubeParameteriser wrapper, or a type inheriting from it
        subcatchment (Simulation): the subcatchment, subset of a whole catchment, identifying which elements (subareas, nodes, links) will be parameterised by the new parameteriser. Other catchment elements are untouched.

    Returns:
        [HypercubeParameteriser]: New parameteriser whose application is limited to the subcatchment.

    Examples:
        >>> sub_cats = simulation.split_to_subcatchments(["node.node_7", "node.node_10"])
        >>> sc = sub_cats["node.node_7"]
        >>> p = sp.create_parameteriser('generic subarea')
        >>> p.add_parameter_to_hypercube("x1", 32, 1, 6e3)
        >>> sp = p.subcatchment_parameteriser(sc)
        >>> sp.apply_sys_config(simulation)

    """
    p = swg.CreateSubcatchmentHypercubeParameterizer_py(parameteriser, subcatchment)
    return p

```

## `wrap_transform(parameteriser)`

Create a parameteriser for which parameter transformations can be defined.

This allows to define e.g. a virtual parameter log_X instead of calibrating on the parameter X.

Parameters:

| Name | Type | Description | Default | | --- | --- | --- | --- | | `parameteriser` | `HypercubeParameteriser` | A HypercubeParameteriser wrapper, or a type inheriting from it | *required* |

Returns:

| Name | Type | Description | | --- | --- | --- | | `TransformParameteriser` | | A new parameteriser (TransformParameteriser) which has methods to define parameter transforms |

Source code in `swift2/parameteriser.py`

```
def wrap_transform(parameteriser):
    """Create a parameteriser for which parameter transformations can be defined.

    This allows to define e.g. a virtual parameter log_X instead of calibrating on the parameter X.

    Args:
        parameteriser (HypercubeParameteriser): A HypercubeParameteriser wrapper, or a type inheriting from it

    Returns:
        TransformParameteriser: A new parameteriser (TransformParameteriser) which has methods to define parameter transforms
    """
    return swg.CreateTransformParameterizer_py(parameteriser)

```
