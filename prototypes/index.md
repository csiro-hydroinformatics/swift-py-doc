# Module prototypes

## `estimate_transformation_parameters(calib_obs, estimation_start, estimation_end, censor_threshold, exclusion, exclusion_start, exclusion_end, termination_condition=None)`

Estimate the transformation parameters for a log-likelihood for a series of observations

Parameters:

| Name                    | Type                      | Description                                                                                        | Default    |
| ----------------------- | ------------------------- | -------------------------------------------------------------------------------------------------- | ---------- |
| `calib_obs`             | `TimeSeriesLike`          | An timeseries of observed data                                                                     | *required* |
| `estimation_start`      | `datetime`                | Start of estimation period                                                                         | *required* |
| `estimation_end`        | `datetime`                | End of estimation period                                                                           | *required* |
| `censor_threshold`      | `float`                   | The value below which observations are treated a censored data (Default=0.0)                       | *required* |
| `exclusion`             | `bool`                    | Start of period exclued from estimation                                                            | *required* |
| `exclusion_start`       | `datetime`                | End of period exclued from estimation                                                              | *required* |
| `exclusion_end`         | `datetime`                | Use the exclusion period (bool)                                                                    | *required* |
| `termination_condition` | `SceTerminationCondition` | A SWIFT termination condition used by the optimisation. Default max runtime of ~3 minutes if None. | `None`     |

Returns:

| Name                     | Type                     | Description               |
| ------------------------ | ------------------------ | ------------------------- |
| `HypercubeParameteriser` | `HypercubeParameteriser` | transformation parameters |

Source code in `swift2/prototypes.py`

```
def estimate_transformation_parameters(
    calib_obs: TimeSeriesLike,
    estimation_start: datetime,
    estimation_end: datetime,
    censor_threshold: float,
    exclusion: bool,
    exclusion_start: datetime,
    exclusion_end: datetime,
    termination_condition: "SceTerminationCondition" = None,
) -> "HypercubeParameteriser":
    """Estimate the transformation parameters for a log-likelihood for a series of observations

    Args:
        calib_obs (TimeSeriesLike):  An timeseries of observed data
        estimation_start (datetime): Start of estimation period
        estimation_end (datetime): End of estimation period
        censor_threshold (float): The value below which observations are treated a censored data (Default=0.0)
        exclusion (bool): Start of period exclued from estimation
        exclusion_start (datetime): End of period exclued from estimation
        exclusion_end (datetime): Use the exclusion period (bool)
        termination_condition (SceTerminationCondition): A SWIFT termination condition used by the optimisation. Default max runtime of ~3 minutes if None.

    Returns:
        HypercubeParameteriser: transformation parameters
    """
    import swift2.internal as si

    CENS_OPTION = 2
    simple_ts = si.simplify_time_series(calib_obs)
    if termination_condition is None:
        termination_condition = get_max_runtime_termination()

    return swg.EstimateTransformationParameters_py(
        obsValues=simple_ts[si.TS_INTEROP_VALUES_KEY],
        obsGeom=simple_ts[si.TS_INTEROP_GEOM_KEY],
        estimationStart=estimation_start,
        estimationEnd=estimation_end,
        censThr=censor_threshold,
        censOpt=CENS_OPTION,
        exclusionStart=exclusion_start,
        exclusionEnd=exclusion_end,
        exclusion=exclusion,
        terminationCondition=termination_condition,
    )

```
