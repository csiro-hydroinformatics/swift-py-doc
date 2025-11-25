# Module prototypes

# prototypes

Functions:

- **`clone`** –
- **`create_erris_parameter_estimator`** –
- **`estimate_erris_parameters`** –
- **`estimate_transformation_parameters`** – Estimate the transformation parameters for a log-likelihood for a series of observations

## clone

```
clone(external_ptr)
```

## create_erris_parameter_estimator

```
create_erris_parameter_estimator(simulation, observed_ts, error_model_element_id, estimation_start, estimation_end, cens_thr, cens_opt, termination_condition=None, restriction_on=True, weighted_least_square=False)
```

## estimate_erris_parameters

```
estimate_erris_parameters(simulation, observed_ts, error_model_element_id, warmup_start, warmup_end, warmup, estimation_start, estimation_end, cens_thr, cens_opt, exclusion_start, exclusion_end, exclusion, termination_condition, hydro_params=None, erris_params=None, restriction_on=True, weighted_least_square=False)
```

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
