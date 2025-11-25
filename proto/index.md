# Module proto

# proto

Prototypes

Classes:

- **`PbmCalibration`** –
- **`PbmCalibrationBuilder`** –
- **`PbmModelFactory`** –

Functions:

- **`parameters_for`** –
- **`scatter_plot`** –
- **`ts_plot`** –

Attributes:

- **`MODELLED_SERIES_COLNAME`** –
- **`OBSERVED_SERIES_COLNAME`** –

## MODELLED_SERIES_COLNAME

```
MODELLED_SERIES_COLNAME = 'Modelled'
```

## OBSERVED_SERIES_COLNAME

```
OBSERVED_SERIES_COLNAME = 'Observed'
```

## PbmCalibration

```
PbmCalibration(station_id: str, model_id, simulation: Simulation, data_repo: OzDataProvider)
```

Methods:

- **`best_modelled_runoff`** –
- **`best_runoff_series`** –
- **`calibrate`** –
- **`extract_optimisation_log`** –
- **`get_geom_ops`** –
- **`max_walltime_seconds`** –
- **`save_to`** –
- **`scatter_plot_calib`** –
- **`scatter_plot_valid`** –
- **`set_metrics`** –
- **`validate`** –

Attributes:

- **`calib_end`** –
- **`calib_start`** –
- **`data_repo`** –
- **`model_id`** –
- **`objective_id`** –
- **`opt_log`** –
- **`optimiser`** –
- **`parameter_template`** –
- **`run_start`** –
- **`runoff_id`** –
- **`runoff_ts`** –
- **`s_calib`** –
- **`s_valid`** –
- **`station_id`** –
- **`valid_end`** –
- **`valid_start`** –

### calib_end

```
calib_end = Timestamp('1995-12-01')
```

### calib_start

```
calib_start = Timestamp('1952-01-01')
```

### data_repo

```
data_repo = data_repo
```

### model_id

```
model_id = model_id
```

### objective_id

```
objective_id = 'NSE'
```

### opt_log

```
opt_log = None
```

### optimiser

```
optimiser = None
```

### parameter_template

```
parameter_template = parameters_for(model_id)
```

### run_start

```
run_start = Timestamp('1950-01-01')
```

### runoff_id

```
runoff_id = 'subarea.Subarea.runoff'
```

### runoff_ts

```
runoff_ts = monthly_data(station_id, 'runoff', cf_time=True)
```

### s_calib

```
s_calib = slice(calib_start, calib_end)
```

### s_valid

```
s_valid = slice(valid_start, valid_end)
```

### station_id

```
station_id = station_id
```

### valid_end

```
valid_end = Timestamp('2014-12-01')
```

### valid_start

```
valid_start = Timestamp('1996-01-01')
```

### best_modelled_runoff

```
best_modelled_runoff()
```

### best_runoff_series

```
best_runoff_series()
```

### calibrate

```
calibrate()
```

### extract_optimisation_log

```
extract_optimisation_log()
```

### get_geom_ops

```
get_geom_ops()
```

### max_walltime_seconds

```
max_walltime_seconds(sec: int)
```

### save_to

```
save_to(root_path: str = None)
```

### scatter_plot_calib

```
scatter_plot_calib()
```

### scatter_plot_valid

```
scatter_plot_valid()
```

### set_metrics

```
set_metrics(metrics)
```

### validate

```
validate()
```

## PbmCalibrationBuilder

```
PbmCalibrationBuilder(model_factory: PbmModelFactory)
```

Methods:

- **`build_calibration`** –
- **`max_walltime_seconds`** –
- **`set_sampling_periods`** –

Attributes:

- **`convergence_criterion`** –
- **`model_factory`** –
- **`objective_id`** –

### convergence_criterion

```
convergence_criterion = 0.002
```

### model_factory

```
model_factory = model_factory
```

### objective_id

```
objective_id = 'NSE'
```

### build_calibration

```
build_calibration(station_id, model_id)
```

### max_walltime_seconds

```
max_walltime_seconds(sec: int)
```

### set_sampling_periods

```
set_sampling_periods(run_start='1950-01-01', calib_start='1952-01-01', calib_end='1995-12-01', valid_start='1996-01-01', valid_end='2014-12-01')
```

## PbmModelFactory

```
PbmModelFactory(data_repo: OzDataProvider)
```

Methods:

- **`new_monthly_lumped_model`** –

Attributes:

- **`data_repo`** –

### data_repo

```
data_repo = data_repo
```

### new_monthly_lumped_model

```
new_monthly_lumped_model(station_id: str, model_id: str, rain_varid='P', evap_varid='E')
```

## parameters_for

```
parameters_for(model_id: str)
```

## scatter_plot

```
scatter_plot(obs_runoff_ts, mod_runoff_ts, title)
```

## ts_plot

```
ts_plot(x, title, y_units)
```
