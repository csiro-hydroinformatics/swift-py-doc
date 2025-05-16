# Sample code for log-likelihood calibration


## About this document



```python
from swift2.doc_helper import pkg_versions_info

print(pkg_versions_info("This document was generated from a jupyter notebook"))
```

    This document was generated from a jupyter notebook on 2025-03-27 17:24:58.815735
        swift2 2.5.1
        uchronia 2.6.2


## Setting up a calibration on daily data

We will use some sample data from (MMH) included in the package


```python
import numpy as np
import pandas as pd
import xarray as xr
```


```python
from cinterop.timeseries import as_timestamp
from swift2.doc_helper import get_free_params, sample_series, set_loglik_param_keys
from swift2.parameteriser import (
    concatenate_parameterisers,
    create_parameter_sampler,
    create_parameteriser,
    create_sce_termination_wila,
    extract_optimisation_log,
    get_default_sce_parameters,
    parameteriser_as_dataframe,
    sort_by_score,
)
from swift2.simulation import create_subarea
from swift2.utils import c, mk_full_data_id, paste0
from swift2.vis import OptimisationPlots

s = as_timestamp('1990-01-01')
e = as_timestamp('2005-12-31')

rain = sample_series('MMH', 'rain')[slice(s, e)]
evap = sample_series('MMH', 'evap')[slice(s, e)]
flow = sample_series('MMH', 'flow')[slice(s, e)]
```


```python
rain.describe()
```




    count    5844.000000
    mean        3.545405
    std         7.737554
    min         0.000000
    25%         0.000000
    50%         0.283600
    75%         3.308775
    max        97.645500
    dtype: float64




```python
flow.describe()
```




    count    5844.000000
    mean       -1.993059
    std        16.361702
    min       -99.999000
    25%         0.194400
    50%         0.438400
    75%         0.900200
    max        17.221100
    dtype: float64



We need to adjust the observed flow, as the SWIFTv1 legacy missing value code is `-99`. 


```python
flow[flow < 0] = np.nan
```


```python
flow
```




    1990-01-01    0.2577
    1990-01-02    0.2459
    1990-01-03    0.2374
    1990-01-04    0.2218
    1990-01-05    0.2127
                   ...  
    2005-12-27    0.3477
    2005-12-28    0.3314
    2005-12-29    0.3333
    2005-12-30    0.3066
    2005-12-31    0.2896
    Length: 5844, dtype: float64



## Catchment setup

Let's create a single catchment setup, using daily data. We need to specify the simulation time step to be consistent with the daily input data.


```python
ms = create_subarea('GR4J', 1.0)
from cinterop.timeseries import xr_ts_end, xr_ts_start

s = xr_ts_start(rain)
e = xr_ts_end(rain)
ms.set_simulation_span(s, e)
ms.set_simulation_time_step('daily')
```

Assign input time series


```python
sa_name = ms.get_subarea_names()[0]
ms.play_subarea_input(rain, sa_name, "P")
ms.play_subarea_input(evap, sa_name, "E")
```

Model variables identifiers are hierarchical, with separators '.' and '|' supported. The "dot" notation should now be preferred, as some R functions producing data frames may change the variable names and replace some characters with '.'.


```python
sa_id = paste0("subarea.", sa_name)
root_id = paste0(sa_id, ".")
print(ms.get_variable_ids(sa_id))
```

    ['subarea.Subarea.areaKm2', 'subarea.Subarea.P', 'subarea.Subarea.E', 'subarea.Subarea.En', 'subarea.Subarea.LAI', 'subarea.Subarea.runoff', 'subarea.Subarea.S', 'subarea.Subarea.R', 'subarea.Subarea.TWS', 'subarea.Subarea.Eactual', 'subarea.Subarea.Ps', 'subarea.Subarea.Es', 'subarea.Subarea.Pr', 'subarea.Subarea.ech1', 'subarea.Subarea.ech2', 'subarea.Subarea.Perc', 'subarea.Subarea.alpha', 'subarea.Subarea.k', 'subarea.Subarea.x1', 'subarea.Subarea.x2', 'subarea.Subarea.x3', 'subarea.Subarea.x4', 'subarea.Subarea.UHExponent', 'subarea.Subarea.PercFactor', 'subarea.Subarea.OutflowVolume', 'subarea.Subarea.OutflowRate']



```python
gr4_state_names = paste0(root_id, c('runoff', 'S', 'R', 'Perc'))
for name in gr4_state_names: 
    ms.record_state(name)
```

Let's check that one simulation runs fine, before we build a calibration definition.


```python
ms.exec_simulation()
sState = ms.get_recorded(gr4_state_names[2])
```


```python
sState.plot(figsize=(10,4))
```




    [<matplotlib.lines.Line2D at 0x7f04f7a3d850>]




    
![png](log_likelihood_files/log_likelihood_20_1.png)
    


Let's build the objective calculator that will guide the calibration process:


```python
w = pd.Timestamp("1992-01-01")
```


```python
runoff_depth_varname = 'subarea.Subarea.runoff'
mod_runoff = ms.get_recorded(runoff_depth_varname)
# zoo::index(flow) = zoo::index(mod_runoff)
objective = ms.create_objective(runoff_depth_varname, flow, 'log-likelihood', w, e)
```


```python
mod_runoff.plot()
```




    [<matplotlib.lines.Line2D at 0x7f04f7aed490>]




    
![png](log_likelihood_files/log_likelihood_24_1.png)
    


## Parameterisation

Define the feasible parameter space, using a generic parameter set for the model parameters. This is 'wrapped' by a log-likelihood parameter set with the extra parameters used in the log likelihood calculation, but which exposes all the parameters as 8 independent degrees of freedom to the optimiser.


```python
pspec_gr4j = get_free_params('GR4J')
pspec_gr4j.Value = c(542.1981111, -0.4127542, 7.7403390, 1.2388548)
pspec_gr4j.Min = c(1,-30, 1,1)
pspec_gr4j.Max = c(3000, 30, 1000, 240)
pspec_gr4j.Name = paste0(root_id, pspec_gr4j.Name)


maxobs = np.max(flow)
p = create_parameteriser(type='Generic', specs=pspec_gr4j)
set_loglik_param_keys(a='a', b='b', m='m', s='s', ct="ct", censopt='censopt')
censor_threshold = maxobs / 100 # TBC
censopt = 0.0

loglik = create_parameteriser(type='no apply')
loglik.add_to_hypercube( 
          pd.DataFrame({ 
          "Name": c('b','m','s','a','maxobs','ct', 'censopt'),
          "Min": c(-30, 0, -10,    -20, maxobs, censor_threshold, censopt),
          "Max":  c(5,   0, 10, 0, maxobs, censor_threshold, censopt),
          "Value": c(-7,  0, 0,  -10, maxobs, censor_threshold, censopt),
          }
          ) )
p = concatenate_parameterisers(p, loglik)
p.as_dataframe()
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Name</th>
      <th>Value</th>
      <th>Min</th>
      <th>Max</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>subarea.Subarea.x1</td>
      <td>542.198111</td>
      <td>1.000000</td>
      <td>3000.000000</td>
    </tr>
    <tr>
      <th>1</th>
      <td>subarea.Subarea.x2</td>
      <td>-0.412754</td>
      <td>-30.000000</td>
      <td>30.000000</td>
    </tr>
    <tr>
      <th>2</th>
      <td>subarea.Subarea.x3</td>
      <td>7.740339</td>
      <td>1.000000</td>
      <td>1000.000000</td>
    </tr>
    <tr>
      <th>3</th>
      <td>subarea.Subarea.x4</td>
      <td>1.238855</td>
      <td>1.000000</td>
      <td>240.000000</td>
    </tr>
    <tr>
      <th>4</th>
      <td>b</td>
      <td>-7.000000</td>
      <td>-30.000000</td>
      <td>5.000000</td>
    </tr>
    <tr>
      <th>5</th>
      <td>m</td>
      <td>0.000000</td>
      <td>0.000000</td>
      <td>0.000000</td>
    </tr>
    <tr>
      <th>6</th>
      <td>s</td>
      <td>0.000000</td>
      <td>-10.000000</td>
      <td>10.000000</td>
    </tr>
    <tr>
      <th>7</th>
      <td>a</td>
      <td>-10.000000</td>
      <td>-20.000000</td>
      <td>0.000000</td>
    </tr>
    <tr>
      <th>8</th>
      <td>maxobs</td>
      <td>17.221100</td>
      <td>17.221100</td>
      <td>17.221100</td>
    </tr>
    <tr>
      <th>9</th>
      <td>ct</td>
      <td>0.172211</td>
      <td>0.172211</td>
      <td>0.172211</td>
    </tr>
    <tr>
      <th>10</th>
      <td>censopt</td>
      <td>0.000000</td>
      <td>0.000000</td>
      <td>0.000000</td>
    </tr>
  </tbody>
</table>
</div>



Check that the objective calculator works, at least with the default values in the feasible parameter space:


```python
score = objective.get_score(p)
print(score)
```

    {'scores': {'Log-likelihood': -1e+20}, 'sysconfig':                   Name       Value        Min          Max
    0   subarea.Subarea.x1  542.198111   1.000000  3000.000000
    1   subarea.Subarea.x2   -0.412754 -30.000000    30.000000
    2   subarea.Subarea.x3    7.740339   1.000000  1000.000000
    3   subarea.Subarea.x4    1.238855   1.000000   240.000000
    4                    b   -7.000000 -30.000000     5.000000
    5                    m    0.000000   0.000000     0.000000
    6                    s    0.000000 -10.000000    10.000000
    7                    a  -10.000000 -20.000000     0.000000
    8               maxobs   17.221100  17.221100    17.221100
    9                   ct    0.172211   0.172211     0.172211
    10             censopt    0.000000   0.000000     0.000000}



```python
mod_runoff = ms.get_recorded(runoff_depth_varname)
```


```python
from swift2.vis import plot_two_series
```


```python
plot_two_series(flow, mod_runoff, ylab="obs/mod runoff", start_time = "2000-01-01", end_time = "2002-12-31", names=['observed','modelled'])
```


    
![png](log_likelihood_files/log_likelihood_31_0.png)
    


## Calibration

Build the optimiser definition, instrument with a logger.


```python
# term = getMaxRuntimeTermination(max_hours = 0.3/60)  # ~20 second appears enough with SWIFT binaries in Release mode
# term = getMarginalTermination(tolerance = 1e-06, cutoff_no_improvement = 10, max_hours = 0.3/60) 
term = create_sce_termination_wila('relative standard deviation', c('0.005',str(1/60)))

sce_params = get_default_sce_parameters()
urs = create_parameter_sampler(0, p, 'urs')
optimiser = objective.create_sce_optim_swift(term, sce_params, urs)
calib_logger = optimiser.set_calibration_logger('')
```


```python
%%time 
calib_results = optimiser.execute_optimisation()
```

    CPU times: user 5min 7s, sys: 44.1 ms, total: 5min 7s
    Wall time: 1min



```python
opt_log = extract_optimisation_log(optimiser, fitness_name = 'Log-likelihood')
geom_ops = opt_log.subset_by_message(pattern= 'Initial.*|Reflec.*|Contrac.*|Add.*') 
```


```python
import matplotlib.pyplot as plt
```


```python
ll_max = max(geom_ops._data['Log-likelihood'].values)
ll_min = np.median(geom_ops._data['Log-likelihood'].values)
```

## Parameter plots


```python
p_var_ids = p.as_dataframe().Name.values
v = OptimisationPlots(geom_ops)
for pVar in p_var_ids:
    g = v.parameter_evolution(pVar, obj_lims=[ll_min, ll_max])
    plt.gcf().set_size_inches(10,8)
```


    
![png](log_likelihood_files/log_likelihood_39_0.png)
    



    
![png](log_likelihood_files/log_likelihood_39_1.png)
    



    
![png](log_likelihood_files/log_likelihood_39_2.png)
    



    
![png](log_likelihood_files/log_likelihood_39_3.png)
    



    
![png](log_likelihood_files/log_likelihood_39_4.png)
    



    
![png](log_likelihood_files/log_likelihood_39_5.png)
    



    
![png](log_likelihood_files/log_likelihood_39_6.png)
    



    
![png](log_likelihood_files/log_likelihood_39_7.png)
    



    
![png](log_likelihood_files/log_likelihood_39_8.png)
    



    
![png](log_likelihood_files/log_likelihood_39_9.png)
    



    
![png](log_likelihood_files/log_likelihood_39_10.png)
    


Finally, get a visual of the runoff time series with the best known parameter set (the penultimate entry in the data frame with the log of the calibration process).


```python
sortedResults = sort_by_score(calib_results, 'Log-likelihood')
sortedResults.as_dataframe().head().T
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>0</th>
      <th>1</th>
      <th>2</th>
      <th>3</th>
      <th>4</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>Log-likelihood</th>
      <td>3340.915859</td>
      <td>3340.771324</td>
      <td>3340.698917</td>
      <td>3340.632166</td>
      <td>3340.481544</td>
    </tr>
    <tr>
      <th>subarea.Subarea.x1</th>
      <td>142.311803</td>
      <td>143.683797</td>
      <td>141.209587</td>
      <td>138.884465</td>
      <td>138.401395</td>
    </tr>
    <tr>
      <th>subarea.Subarea.x2</th>
      <td>-29.926501</td>
      <td>-29.985372</td>
      <td>-29.892518</td>
      <td>-29.987330</td>
      <td>-29.915535</td>
    </tr>
    <tr>
      <th>subarea.Subarea.x3</th>
      <td>769.304425</td>
      <td>771.741061</td>
      <td>768.582954</td>
      <td>768.664694</td>
      <td>768.479620</td>
    </tr>
    <tr>
      <th>subarea.Subarea.x4</th>
      <td>1.001487</td>
      <td>1.000453</td>
      <td>1.001558</td>
      <td>1.001635</td>
      <td>1.002588</td>
    </tr>
    <tr>
      <th>b</th>
      <td>-1.069403</td>
      <td>-1.180434</td>
      <td>-1.182628</td>
      <td>-0.981440</td>
      <td>-1.247725</td>
    </tr>
    <tr>
      <th>m</th>
      <td>0.000000</td>
      <td>0.000000</td>
      <td>0.000000</td>
      <td>0.000000</td>
      <td>0.000000</td>
    </tr>
    <tr>
      <th>s</th>
      <td>0.394041</td>
      <td>0.514402</td>
      <td>0.517914</td>
      <td>0.318156</td>
      <td>0.597338</td>
    </tr>
    <tr>
      <th>a</th>
      <td>-7.887809</td>
      <td>-7.851411</td>
      <td>-8.134082</td>
      <td>-7.777277</td>
      <td>-8.522691</td>
    </tr>
    <tr>
      <th>maxobs</th>
      <td>17.221100</td>
      <td>17.221100</td>
      <td>17.221100</td>
      <td>17.221100</td>
      <td>17.221100</td>
    </tr>
    <tr>
      <th>ct</th>
      <td>0.172211</td>
      <td>0.172211</td>
      <td>0.172211</td>
      <td>0.172211</td>
      <td>0.172211</td>
    </tr>
    <tr>
      <th>censopt</th>
      <td>0.000000</td>
      <td>0.000000</td>
      <td>0.000000</td>
      <td>0.000000</td>
      <td>0.000000</td>
    </tr>
  </tbody>
</table>
</div>




```python
best_pset = calib_results.get_best_score('Log-likelihood').parameteriser
best_pset.apply_sys_config(ms)
ms.exec_simulation()
mod_runoff = ms.get_recorded(runoff_depth_varname)
# joki::plot_two_series(flow, mod_runoff, ylab="obs/mod runoff", startTime = start(flow), endTime = end(flow))
```


```python
mod_runoff
```




<div><svg style="position: absolute; width: 0; height: 0; overflow: hidden">
<defs>
<symbol id="icon-database" viewBox="0 0 32 32">
<path d="M16 0c-8.837 0-16 2.239-16 5v4c0 2.761 7.163 5 16 5s16-2.239 16-5v-4c0-2.761-7.163-5-16-5z"></path>
<path d="M16 17c-8.837 0-16-2.239-16-5v6c0 2.761 7.163 5 16 5s16-2.239 16-5v-6c0 2.761-7.163 5-16 5z"></path>
<path d="M16 26c-8.837 0-16-2.239-16-5v6c0 2.761 7.163 5 16 5s16-2.239 16-5v-6c0 2.761-7.163 5-16 5z"></path>
</symbol>
<symbol id="icon-file-text2" viewBox="0 0 32 32">
<path d="M28.681 7.159c-0.694-0.947-1.662-2.053-2.724-3.116s-2.169-2.030-3.116-2.724c-1.612-1.182-2.393-1.319-2.841-1.319h-15.5c-1.378 0-2.5 1.121-2.5 2.5v27c0 1.378 1.122 2.5 2.5 2.5h23c1.378 0 2.5-1.122 2.5-2.5v-19.5c0-0.448-0.137-1.23-1.319-2.841zM24.543 5.457c0.959 0.959 1.712 1.825 2.268 2.543h-4.811v-4.811c0.718 0.556 1.584 1.309 2.543 2.268zM28 29.5c0 0.271-0.229 0.5-0.5 0.5h-23c-0.271 0-0.5-0.229-0.5-0.5v-27c0-0.271 0.229-0.5 0.5-0.5 0 0 15.499-0 15.5 0v7c0 0.552 0.448 1 1 1h7v19.5z"></path>
<path d="M23 26h-14c-0.552 0-1-0.448-1-1s0.448-1 1-1h14c0.552 0 1 0.448 1 1s-0.448 1-1 1z"></path>
<path d="M23 22h-14c-0.552 0-1-0.448-1-1s0.448-1 1-1h14c0.552 0 1 0.448 1 1s-0.448 1-1 1z"></path>
<path d="M23 18h-14c-0.552 0-1-0.448-1-1s0.448-1 1-1h14c0.552 0 1 0.448 1 1s-0.448 1-1 1z"></path>
</symbol>
</defs>
</svg>
<style>/* CSS stylesheet for displaying xarray objects in jupyterlab.
 *
 */

:root {
  --xr-font-color0: var(--jp-content-font-color0, rgba(0, 0, 0, 1));
  --xr-font-color2: var(--jp-content-font-color2, rgba(0, 0, 0, 0.54));
  --xr-font-color3: var(--jp-content-font-color3, rgba(0, 0, 0, 0.38));
  --xr-border-color: var(--jp-border-color2, #e0e0e0);
  --xr-disabled-color: var(--jp-layout-color3, #bdbdbd);
  --xr-background-color: var(--jp-layout-color0, white);
  --xr-background-color-row-even: var(--jp-layout-color1, white);
  --xr-background-color-row-odd: var(--jp-layout-color2, #eeeeee);
}

html[theme=dark],
html[data-theme=dark],
body[data-theme=dark],
body.vscode-dark {
  --xr-font-color0: rgba(255, 255, 255, 1);
  --xr-font-color2: rgba(255, 255, 255, 0.54);
  --xr-font-color3: rgba(255, 255, 255, 0.38);
  --xr-border-color: #1F1F1F;
  --xr-disabled-color: #515151;
  --xr-background-color: #111111;
  --xr-background-color-row-even: #111111;
  --xr-background-color-row-odd: #313131;
}

.xr-wrap {
  display: block !important;
  min-width: 300px;
  max-width: 700px;
}

.xr-text-repr-fallback {
  /* fallback to plain text repr when CSS is not injected (untrusted notebook) */
  display: none;
}

.xr-header {
  padding-top: 6px;
  padding-bottom: 6px;
  margin-bottom: 4px;
  border-bottom: solid 1px var(--xr-border-color);
}

.xr-header > div,
.xr-header > ul {
  display: inline;
  margin-top: 0;
  margin-bottom: 0;
}

.xr-obj-type,
.xr-array-name {
  margin-left: 2px;
  margin-right: 10px;
}

.xr-obj-type {
  color: var(--xr-font-color2);
}

.xr-sections {
  padding-left: 0 !important;
  display: grid;
  grid-template-columns: 150px auto auto 1fr 0 20px 0 20px;
}

.xr-section-item {
  display: contents;
}

.xr-section-item input {
  display: inline-block;
  opacity: 0;
}

.xr-section-item input + label {
  color: var(--xr-disabled-color);
}

.xr-section-item input:enabled + label {
  cursor: pointer;
  color: var(--xr-font-color2);
}

.xr-section-item input:focus + label {
  border: 2px solid var(--xr-font-color0);
}

.xr-section-item input:enabled + label:hover {
  color: var(--xr-font-color0);
}

.xr-section-summary {
  grid-column: 1;
  color: var(--xr-font-color2);
  font-weight: 500;
}

.xr-section-summary > span {
  display: inline-block;
  padding-left: 0.5em;
}

.xr-section-summary-in:disabled + label {
  color: var(--xr-font-color2);
}

.xr-section-summary-in + label:before {
  display: inline-block;
  content: '►';
  font-size: 11px;
  width: 15px;
  text-align: center;
}

.xr-section-summary-in:disabled + label:before {
  color: var(--xr-disabled-color);
}

.xr-section-summary-in:checked + label:before {
  content: '▼';
}

.xr-section-summary-in:checked + label > span {
  display: none;
}

.xr-section-summary,
.xr-section-inline-details {
  padding-top: 4px;
  padding-bottom: 4px;
}

.xr-section-inline-details {
  grid-column: 2 / -1;
}

.xr-section-details {
  display: none;
  grid-column: 1 / -1;
  margin-bottom: 5px;
}

.xr-section-summary-in:checked ~ .xr-section-details {
  display: contents;
}

.xr-array-wrap {
  grid-column: 1 / -1;
  display: grid;
  grid-template-columns: 20px auto;
}

.xr-array-wrap > label {
  grid-column: 1;
  vertical-align: top;
}

.xr-preview {
  color: var(--xr-font-color3);
}

.xr-array-preview,
.xr-array-data {
  padding: 0 5px !important;
  grid-column: 2;
}

.xr-array-data,
.xr-array-in:checked ~ .xr-array-preview {
  display: none;
}

.xr-array-in:checked ~ .xr-array-data,
.xr-array-preview {
  display: inline-block;
}

.xr-dim-list {
  display: inline-block !important;
  list-style: none;
  padding: 0 !important;
  margin: 0;
}

.xr-dim-list li {
  display: inline-block;
  padding: 0;
  margin: 0;
}

.xr-dim-list:before {
  content: '(';
}

.xr-dim-list:after {
  content: ')';
}

.xr-dim-list li:not(:last-child):after {
  content: ',';
  padding-right: 5px;
}

.xr-has-index {
  font-weight: bold;
}

.xr-var-list,
.xr-var-item {
  display: contents;
}

.xr-var-item > div,
.xr-var-item label,
.xr-var-item > .xr-var-name span {
  background-color: var(--xr-background-color-row-even);
  margin-bottom: 0;
}

.xr-var-item > .xr-var-name:hover span {
  padding-right: 5px;
}

.xr-var-list > li:nth-child(odd) > div,
.xr-var-list > li:nth-child(odd) > label,
.xr-var-list > li:nth-child(odd) > .xr-var-name span {
  background-color: var(--xr-background-color-row-odd);
}

.xr-var-name {
  grid-column: 1;
}

.xr-var-dims {
  grid-column: 2;
}

.xr-var-dtype {
  grid-column: 3;
  text-align: right;
  color: var(--xr-font-color2);
}

.xr-var-preview {
  grid-column: 4;
}

.xr-index-preview {
  grid-column: 2 / 5;
  color: var(--xr-font-color2);
}

.xr-var-name,
.xr-var-dims,
.xr-var-dtype,
.xr-preview,
.xr-attrs dt {
  white-space: nowrap;
  overflow: hidden;
  text-overflow: ellipsis;
  padding-right: 10px;
}

.xr-var-name:hover,
.xr-var-dims:hover,
.xr-var-dtype:hover,
.xr-attrs dt:hover {
  overflow: visible;
  width: auto;
  z-index: 1;
}

.xr-var-attrs,
.xr-var-data,
.xr-index-data {
  display: none;
  background-color: var(--xr-background-color) !important;
  padding-bottom: 5px !important;
}

.xr-var-attrs-in:checked ~ .xr-var-attrs,
.xr-var-data-in:checked ~ .xr-var-data,
.xr-index-data-in:checked ~ .xr-index-data {
  display: block;
}

.xr-var-data > table {
  float: right;
}

.xr-var-name span,
.xr-var-data,
.xr-index-name div,
.xr-index-data,
.xr-attrs {
  padding-left: 25px !important;
}

.xr-attrs,
.xr-var-attrs,
.xr-var-data,
.xr-index-data {
  grid-column: 1 / -1;
}

dl.xr-attrs {
  padding: 0;
  margin: 0;
  display: grid;
  grid-template-columns: 125px auto;
}

.xr-attrs dt,
.xr-attrs dd {
  padding: 0;
  margin: 0;
  float: left;
  padding-right: 10px;
  width: auto;
}

.xr-attrs dt {
  font-weight: normal;
  grid-column: 1;
}

.xr-attrs dt:hover span {
  display: inline-block;
  background: var(--xr-background-color);
  padding-right: 10px;
}

.xr-attrs dd {
  grid-column: 2;
  white-space: pre-wrap;
  word-break: break-all;
}

.xr-icon-database,
.xr-icon-file-text2,
.xr-no-icon {
  display: inline-block;
  vertical-align: middle;
  width: 1em;
  height: 1.5em !important;
  stroke-width: 0;
  stroke: currentColor;
  fill: currentColor;
}
</style><pre class='xr-text-repr-fallback'>&lt;xarray.DataArray (variable_identifiers: 1, ensemble: 1, time: 5844)&gt; Size: 47kB
array([[[0.        , 0.        , 0.        , ..., 0.41868723,
         0.41110903, 0.40375453]]], shape=(1, 1, 5844))
Coordinates:
  * ensemble              (ensemble) int64 8B 0
  * time                  (time) datetime64[ns] 47kB 1990-01-01 ... 2005-12-31
  * variable_identifiers  (variable_identifiers) object 8B &#x27;subarea.Subarea.r...</pre><div class='xr-wrap' style='display:none'><div class='xr-header'><div class='xr-obj-type'>xarray.DataArray</div><div class='xr-array-name'></div><ul class='xr-dim-list'><li><span class='xr-has-index'>variable_identifiers</span>: 1</li><li><span class='xr-has-index'>ensemble</span>: 1</li><li><span class='xr-has-index'>time</span>: 5844</li></ul></div><ul class='xr-sections'><li class='xr-section-item'><div class='xr-array-wrap'><input id='section-42898296-f414-4b0f-afd2-fd89d5fcfa3d' class='xr-array-in' type='checkbox' checked><label for='section-42898296-f414-4b0f-afd2-fd89d5fcfa3d' title='Show/hide data repr'><svg class='icon xr-icon-database'><use xlink:href='#icon-database'></use></svg></label><div class='xr-array-preview xr-preview'><span>0.0 0.0 0.0 0.0 0.0 0.0 ... 0.4429 0.4346 0.4265 0.4187 0.4111 0.4038</span></div><div class='xr-array-data'><pre>array([[[0.        , 0.        , 0.        , ..., 0.41868723,
         0.41110903, 0.40375453]]], shape=(1, 1, 5844))</pre></div></div></li><li class='xr-section-item'><input id='section-fc3f90c8-453a-4f18-8454-d4734ff35258' class='xr-section-summary-in' type='checkbox'  checked><label for='section-fc3f90c8-453a-4f18-8454-d4734ff35258' class='xr-section-summary' >Coordinates: <span>(3)</span></label><div class='xr-section-inline-details'></div><div class='xr-section-details'><ul class='xr-var-list'><li class='xr-var-item'><div class='xr-var-name'><span class='xr-has-index'>ensemble</span></div><div class='xr-var-dims'>(ensemble)</div><div class='xr-var-dtype'>int64</div><div class='xr-var-preview xr-preview'>0</div><input id='attrs-228500b4-ec67-4e1d-b182-04d8c02cc876' class='xr-var-attrs-in' type='checkbox' disabled><label for='attrs-228500b4-ec67-4e1d-b182-04d8c02cc876' title='Show/Hide attributes'><svg class='icon xr-icon-file-text2'><use xlink:href='#icon-file-text2'></use></svg></label><input id='data-64f2262a-fc59-409d-b858-b12fcc530781' class='xr-var-data-in' type='checkbox'><label for='data-64f2262a-fc59-409d-b858-b12fcc530781' title='Show/Hide data repr'><svg class='icon xr-icon-database'><use xlink:href='#icon-database'></use></svg></label><div class='xr-var-attrs'><dl class='xr-attrs'></dl></div><div class='xr-var-data'><pre>array([0])</pre></div></li><li class='xr-var-item'><div class='xr-var-name'><span class='xr-has-index'>time</span></div><div class='xr-var-dims'>(time)</div><div class='xr-var-dtype'>datetime64[ns]</div><div class='xr-var-preview xr-preview'>1990-01-01 ... 2005-12-31</div><input id='attrs-e730057c-82a2-4c5c-9d84-4f336e99998a' class='xr-var-attrs-in' type='checkbox' disabled><label for='attrs-e730057c-82a2-4c5c-9d84-4f336e99998a' title='Show/Hide attributes'><svg class='icon xr-icon-file-text2'><use xlink:href='#icon-file-text2'></use></svg></label><input id='data-669b46b4-3964-460d-8f93-2b7d1b82326c' class='xr-var-data-in' type='checkbox'><label for='data-669b46b4-3964-460d-8f93-2b7d1b82326c' title='Show/Hide data repr'><svg class='icon xr-icon-database'><use xlink:href='#icon-database'></use></svg></label><div class='xr-var-attrs'><dl class='xr-attrs'></dl></div><div class='xr-var-data'><pre>array([&#x27;1990-01-01T00:00:00.000000000&#x27;, &#x27;1990-01-02T00:00:00.000000000&#x27;,
       &#x27;1990-01-03T00:00:00.000000000&#x27;, ..., &#x27;2005-12-29T00:00:00.000000000&#x27;,
       &#x27;2005-12-30T00:00:00.000000000&#x27;, &#x27;2005-12-31T00:00:00.000000000&#x27;],
      shape=(5844,), dtype=&#x27;datetime64[ns]&#x27;)</pre></div></li><li class='xr-var-item'><div class='xr-var-name'><span class='xr-has-index'>variable_identifiers</span></div><div class='xr-var-dims'>(variable_identifiers)</div><div class='xr-var-dtype'>object</div><div class='xr-var-preview xr-preview'>&#x27;subarea.Subarea.runoff&#x27;</div><input id='attrs-1b6431dc-dfe7-44b2-903e-f6aa0815ec66' class='xr-var-attrs-in' type='checkbox' disabled><label for='attrs-1b6431dc-dfe7-44b2-903e-f6aa0815ec66' title='Show/Hide attributes'><svg class='icon xr-icon-file-text2'><use xlink:href='#icon-file-text2'></use></svg></label><input id='data-83325ec9-07a9-43fd-b226-21716a14f02b' class='xr-var-data-in' type='checkbox'><label for='data-83325ec9-07a9-43fd-b226-21716a14f02b' title='Show/Hide data repr'><svg class='icon xr-icon-database'><use xlink:href='#icon-database'></use></svg></label><div class='xr-var-attrs'><dl class='xr-attrs'></dl></div><div class='xr-var-data'><pre>array([&#x27;subarea.Subarea.runoff&#x27;], dtype=object)</pre></div></li></ul></div></li><li class='xr-section-item'><input id='section-9e30e3a7-c62d-499e-a1fa-dc0dc1d3bb91' class='xr-section-summary-in' type='checkbox'  ><label for='section-9e30e3a7-c62d-499e-a1fa-dc0dc1d3bb91' class='xr-section-summary' >Indexes: <span>(3)</span></label><div class='xr-section-inline-details'></div><div class='xr-section-details'><ul class='xr-var-list'><li class='xr-var-item'><div class='xr-index-name'><div>ensemble</div></div><div class='xr-index-preview'>PandasIndex</div><div></div><input id='index-568f5b9d-e7dd-469a-8df1-07aa7f0e7508' class='xr-index-data-in' type='checkbox'/><label for='index-568f5b9d-e7dd-469a-8df1-07aa7f0e7508' title='Show/Hide index repr'><svg class='icon xr-icon-database'><use xlink:href='#icon-database'></use></svg></label><div class='xr-index-data'><pre>PandasIndex(Index([0], dtype=&#x27;int64&#x27;, name=&#x27;ensemble&#x27;))</pre></div></li><li class='xr-var-item'><div class='xr-index-name'><div>time</div></div><div class='xr-index-preview'>PandasIndex</div><div></div><input id='index-b4e20eed-2a60-410b-b5ad-09b5f25995f6' class='xr-index-data-in' type='checkbox'/><label for='index-b4e20eed-2a60-410b-b5ad-09b5f25995f6' title='Show/Hide index repr'><svg class='icon xr-icon-database'><use xlink:href='#icon-database'></use></svg></label><div class='xr-index-data'><pre>PandasIndex(DatetimeIndex([&#x27;1990-01-01&#x27;, &#x27;1990-01-02&#x27;, &#x27;1990-01-03&#x27;, &#x27;1990-01-04&#x27;,
               &#x27;1990-01-05&#x27;, &#x27;1990-01-06&#x27;, &#x27;1990-01-07&#x27;, &#x27;1990-01-08&#x27;,
               &#x27;1990-01-09&#x27;, &#x27;1990-01-10&#x27;,
               ...
               &#x27;2005-12-22&#x27;, &#x27;2005-12-23&#x27;, &#x27;2005-12-24&#x27;, &#x27;2005-12-25&#x27;,
               &#x27;2005-12-26&#x27;, &#x27;2005-12-27&#x27;, &#x27;2005-12-28&#x27;, &#x27;2005-12-29&#x27;,
               &#x27;2005-12-30&#x27;, &#x27;2005-12-31&#x27;],
              dtype=&#x27;datetime64[ns]&#x27;, name=&#x27;time&#x27;, length=5844, freq=&#x27;D&#x27;))</pre></div></li><li class='xr-var-item'><div class='xr-index-name'><div>variable_identifiers</div></div><div class='xr-index-preview'>PandasIndex</div><div></div><input id='index-af09afa8-0b67-4e47-a69e-3a23a54317a3' class='xr-index-data-in' type='checkbox'/><label for='index-af09afa8-0b67-4e47-a69e-3a23a54317a3' title='Show/Hide index repr'><svg class='icon xr-icon-database'><use xlink:href='#icon-database'></use></svg></label><div class='xr-index-data'><pre>PandasIndex(Index([&#x27;subarea.Subarea.runoff&#x27;], dtype=&#x27;object&#x27;, name=&#x27;variable_identifiers&#x27;))</pre></div></li></ul></div></li><li class='xr-section-item'><input id='section-be0ffd04-3178-4874-b941-285b2296b5dd' class='xr-section-summary-in' type='checkbox' disabled ><label for='section-be0ffd04-3178-4874-b941-285b2296b5dd' class='xr-section-summary'  title='Expand/collapse section'>Attributes: <span>(0)</span></label><div class='xr-section-inline-details'></div><div class='xr-section-details'><dl class='xr-attrs'></dl></div></li></ul></div></div>




```python
mod_runoff.squeeze(drop=True).sel(time=slice(e - pd.offsets.DateOffset(years=1), e)).plot(figsize=(16,9))
```




    [<matplotlib.lines.Line2D at 0x7f04df4f7e50>]




    
![png](log_likelihood_files/log_likelihood_44_1.png)
    



```python
plot_two_series(flow, mod_runoff, ylab="obs/mod runoff", start_time = "2000-01-01", end_time = "2002-12-31", names=['observed','modelled'])
```


    
![png](log_likelihood_files/log_likelihood_45_0.png)
    





