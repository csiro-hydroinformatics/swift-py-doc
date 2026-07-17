# Module prototypes

# prototypes

Functions:

- **`clone`** –
- **`create_erris_parameter_estimator`** –
- **`estimate_erris_parameters`** – Estimates parameters of the ERRIS error model.
- **`estimate_maerris_parameters`** – Estimates parameters of the MAERRIS error model.
- **`estimate_transformation_parameters`** – Estimate the transformation parameters for a log-likelihood for a series of observations

## clone

```
clone(external_ptr)
```

## create_erris_parameter_estimator

```
create_erris_parameter_estimator(simulation: Simulation, observed_ts: TimeSeriesLike, error_model_element_id: str, estimation_start: ConvertibleToTimestamp, estimation_end: ConvertibleToTimestamp, cens_thr: float, cens_opt: float, termination_condition: Optional[SceTerminationCondition] = None, restriction_on: bool = True, weighted_least_square: bool = False) -> ErrisStagedCalibration
```

## estimate_erris_parameters

```
estimate_erris_parameters(simulation: Simulation, observed_ts: TimeSeriesLike, error_model_element_id: str, warmup_start: ConvertibleToTimestamp, warmup_end: ConvertibleToTimestamp, warmup: ConvertibleToTimestamp, estimation_start: ConvertibleToTimestamp, estimation_end: ConvertibleToTimestamp, cens_thr: float, cens_opt: float, exclusion_start: ConvertibleToTimestamp, exclusion_end: ConvertibleToTimestamp, exclusion: bool, termination_condition: Optional[SceTerminationCondition] = None, hydro_params: Optional[HypercubeParameteriser] = None, erris_params: Optional[HypercubeParameteriser] = None, restriction_on=False, weighted_least_square=False) -> HypercubeParameteriser
```

Estimates parameters of the ERRIS error model.

This is using the pre-canned ERRIS parameter estimation routine in SWIFT that executes the four stages of the ERRIS estimation in one go. We may want to expose the individual stages in the future.

Parameters:

- **`simulation`** (`Simulation`) – The simulation object providing catchment structure.
- **`observed_ts`** (`TimeSerieLike`) – Observed time series used for estimation.
- **`error_model_element_id`** (`str`) – Element ID for the error model (e.g., 'node.123').
- **`warmup_start`** (`ConvertibleToTimestamp`) – Start time for warmup.
- **`warmup_end`** (`Optional[ConvertibleToTimestamp]`) – End time for warmup
- **`warmup`** (`bool`) – Whether to perform warmup.
- **`estimation_start`** (`ConvertibleToTimestamp`) – Start time for estimation.
- **`estimation_end`** (`ConvertibleToTimestamp`) – End time for estimation.
- **`s2_window`** (`float`) – S2 window size for the estimation, in number of time steps. S2 window is a parameter that defines the size of the moving window used by the bias-correction.
- **`cens_thr`** (`float`) – Censoring threshold for the estimation
- **`cens_opt`** (`float`) – Censoring option for the estimation
- **`termination_condition`** (`Optional`, default: `None` ) – Termination condition for the estimation. If None, uses a default termination condition. Default is None.
- **`hydro_params`** (`HypercubeParameteriser or OwningCffiNativeHandle`, default: `None` ) – Not used. Default is None.
- **`erris_params`** (`HypercubeParameteriser or OwningCffiNativeHandle`, default: `None` ) – Can be used to change param bounds of error params if defaults not satsifactory. Proceed with caution - only to be used by those who know what they are doing. Default is None.
- **`restriction_on`** (`bool`, default: `False` ) – Whether to apply the AR restriction. Default is False

Returns:

- **`HypercubeParameteriser`** ( `HypercubeParameteriser` ) – A parameteriser for an ERRIS instance.

## estimate_maerris_parameters

```
estimate_maerris_parameters(simulation: Simulation, observed_ts: TimeSeriesLike, error_model_element_id: str, warmup_start: ConvertibleToTimestamp, warmup_end: ConvertibleToTimestamp, warmup: bool, estimation_start: ConvertibleToTimestamp, estimation_end: ConvertibleToTimestamp, s2_window: float, cens_thr: float, cens_opt: float, exclusion_start: ConvertibleToTimestamp, exclusion_end: ConvertibleToTimestamp, exclusion: bool, termination_condition: Optional[SceTerminationCondition] = None, hydro_params: Optional[HypercubeParameteriser] = None, maerris_params: Optional[HypercubeParameteriser] = None, restriction_on=False) -> HypercubeParameteriser
```

Estimates parameters of the MAERRIS error model.

This is using the pre-canned MAERRIS parameter estimation routine in SWIFT that executes the four stages of the MAERRIS estimation in one go. We may want to expose the individual stages in the future.

Parameters:

- **`simulation`** (`Simulation`) – The simulation object providing catchment structure.
- **`observed_ts`** (`TimeSerieLike`) – Observed time series used for estimation.
- **`error_model_element_id`** (`str`) – Element ID for the error model (e.g., 'node.123').
- **`warmup_start`** (`ConvertibleToTimestamp`) – Start time for warmup.
- **`warmup_end`** (`Optional[ConvertibleToTimestamp]`) – End time for warmup
- **`warmup`** (`bool`) – Whether to perform warmup.
- **`estimation_start`** (`ConvertibleToTimestamp`) – Start time for estimation.
- **`estimation_end`** (`ConvertibleToTimestamp`) – End time for estimation.
- **`s2_window`** (`float`) – S2 window size for the estimation, in number of time steps. S2 window is a parameter that defines the size of the moving window used by the bias-correction.
- **`cens_thr`** (`float`) – Censoring threshold for the estimation
- **`cens_opt`** (`float`) – Censoring option for the estimation
- **`termination_condition`** (`Optional`, default: `None` ) – Termination condition for the estimation. If None, uses a default termination condition. Default is None.
- **`hydro_params`** (`HypercubeParameteriser or OwningCffiNativeHandle`, default: `None` ) – Not used. Default is None.
- **`maerris_params`** (`HypercubeParameteriser or OwningCffiNativeHandle`, default: `None` ) – Can be used to change param bounds of error params if defaults not satsifactory. Proceed with caution - only to be used by those who know what they are doing. Default is None.
- **`restriction_on`** (`bool`, default: `False` ) – Whether to apply the AR restriction. Default is False

Returns:

- **`HypercubeParameteriser`** ( `HypercubeParameteriser` ) – A parameteriser for a MAERRIS instance.

## estimate_transformation_parameters

```
estimate_transformation_parameters(calib_obs: TimeSeriesLike, estimation_start: datetime, estimation_end: datetime, censor_threshold: float, exclusion: bool, exclusion_start: datetime, exclusion_end: datetime, termination_condition: SceTerminationCondition = None) -> HypercubeParameteriser
```

Estimate the transformation parameters for a log-likelihood for a series of observations

Parameters:

- **`calib_obs`** (`TimeSeriesLike`) – An timeseries of observed data
- **`estimation_start`** (`datetime`) – Start of estimation period
- **`estimation_end`** (`datetime`) – End of estimation period
- **`censor_threshold`** (`float`) – The value below which observations are treated a censored data (Default=0.0)
- **`exclusion`** (`bool`) – Start of period exclued from estimation
- **`exclusion_start`** (`datetime`) – End of period exclued from estimation
- **`exclusion_end`** (`datetime`) – Use the exclusion period (bool)
- **`termination_condition`** (`SceTerminationCondition`, default: `None` ) – A SWIFT termination condition used by the optimisation. Default max runtime of ~3 minutes if None.

Returns:

- **`HypercubeParameteriser`** ( `HypercubeParameteriser` ) – transformation parameters
