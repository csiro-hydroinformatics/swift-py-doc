# Cascaded calibration of subcatchments defined by multiple gauges


```python
from swift2.doc_helper import pkg_versions_info

print(pkg_versions_info("This document was generated from a jupyter notebook"))
```

    This document was generated from a jupyter notebook on 2025-03-27 17:22:20.805191
        swift2 2.5.1
        uchronia 2.6.2


## Use case

**2021-01: this vignette works structurally, but is confined to overly short (and possibly difficult) data to keep runtime low**

This vignette demonstrates how one can calibrate a catchment using multiple gauging points available within this catchment. Instead of setting up a whole-of-catchment calibration definition, it makes sense, at least in a system where subareas above a gauge points do not have a behavior dependent on other catchment processes (meaning mostly, no managed reservoirs). SWIFT offers capabilities to calibrate such subcatchments sequentially, feeding the input flow of upstream and already calibrated subcatchments to other subcatchments, thus cutting down on the complexity and runtime of the overall catchment calibration. 


```python
import datetime as dt
from collections import OrderedDict

import numpy as np
```


```python
import swift2.doc_helper as std
import swift2.parameteriser as sp
```


```python
from cinterop.timeseries import xr_ts_end, xr_ts_start
from swift2.classes import CompositeParameteriser, ObjectiveEvaluator, Simulation
from swift2.const import CATCHMENT_FLOWRATE_VARID
from swift2.vis import plot_two_series
```


```python
%matplotlib inline
```

## Data

The sample data that comes with the package contains a model definition for the South Esk catchment, including a short subset of the climate and flow record data.


```python
model_id = 'GR4J'
site_id = 'South_Esk'
simulation = std.sample_catchment_model(site_id=site_id, config_id='catchment')
simulation = simulation.swap_model('LagAndRoute', 'channel_routing')
```

A visual of the catchment structure (note: may not render yet through GitHub)


```python
# import swift2.wrap.swift_wrap_generated as swg
# dot_graph = swg.GetCatchmentDOTGraph_py(simulation)
# import graphviz
# # Using graphviz package directly
# graph = graphviz.Source(dot_graph)
# graph  # This will display the graph in a Jupyter Notebook
```


```python
# Other possible visualisation resources:
# https://towardsdatascience.com/visualizing-networks-in-python-d70f4cbeb259
# https://medium.com/@ludvig.hult/drawing-graphs-with-python-in-2019-bdd42bf9d5db
```


```python
# def loadSwiftV1TextDef(controlFile, dataDir):
#     import swift2.wrap.swift_wrap_generated as swg
#     # controlFile = mkPathToPlatform(controlFile)
#     # dataDir = mkPathToPlatform(dataDir)
#     return swg.LoadVersionOneControlFile_py(controlFile, dataDir)


# ctrl_file = '/home/per202/mnt/hydrofct/work/common/Staff/per202/sample_data/South_Esk/201601/SWIFT_Control.txt')
# stopifnot(file.exists(ctrl_file))
# ms <- loadSwiftV1TextDef(ctrl_file, 'dummy')
# ms <- swapModel(ms, 'MuskingumNonLinear', 'channel_routing')


```


```python
se_climate = std.sample_series(site_id=site_id, var_name='climate')
se_flows = std.sample_series(site_id=site_id, var_name='flow')
```


```python
se_climate["subcatchment.4.P"].plot();
```


    
![png](calibrate_subcatchments_files/calibrate_subcatchments_14_0.png)
    


The names of the climate series is already set to the climate input identifiers of the model simulation, so setting them as inputs is easy:


```python
se_climate.head(3)
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
      <th>subcatchment.1.E</th>
      <th>subcatchment.1.P</th>
      <th>subcatchment.10.E</th>
      <th>subcatchment.10.P</th>
      <th>subcatchment.11.E</th>
      <th>subcatchment.11.P</th>
      <th>subcatchment.12.E</th>
      <th>subcatchment.12.P</th>
      <th>subcatchment.13.E</th>
      <th>subcatchment.13.P</th>
      <th>...</th>
      <th>subcatchment.5.E</th>
      <th>subcatchment.5.P</th>
      <th>subcatchment.6.E</th>
      <th>subcatchment.6.P</th>
      <th>subcatchment.7.E</th>
      <th>subcatchment.7.P</th>
      <th>subcatchment.8.E</th>
      <th>subcatchment.8.P</th>
      <th>subcatchment.9.E</th>
      <th>subcatchment.9.P</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>2010-11-01 00:00:00</th>
      <td>0.3918</td>
      <td>0.0</td>
      <td>0.4020</td>
      <td>0.0000</td>
      <td>0.3978</td>
      <td>0.0000</td>
      <td>0.4266</td>
      <td>0.0000</td>
      <td>0.3936</td>
      <td>0.0000</td>
      <td>...</td>
      <td>0.4325</td>
      <td>0.0</td>
      <td>0.4110</td>
      <td>0.0322</td>
      <td>0.4247</td>
      <td>0.0</td>
      <td>0.4377</td>
      <td>0.0</td>
      <td>0.4337</td>
      <td>0.0</td>
    </tr>
    <tr>
      <th>2010-11-01 01:00:00</th>
      <td>0.4385</td>
      <td>0.0</td>
      <td>0.4493</td>
      <td>0.0207</td>
      <td>0.4446</td>
      <td>0.0433</td>
      <td>0.4763</td>
      <td>0.0179</td>
      <td>0.4397</td>
      <td>0.0555</td>
      <td>...</td>
      <td>0.4823</td>
      <td>0.0</td>
      <td>0.4593</td>
      <td>0.0000</td>
      <td>0.4746</td>
      <td>0.0</td>
      <td>0.4892</td>
      <td>0.0</td>
      <td>0.4841</td>
      <td>0.0</td>
    </tr>
    <tr>
      <th>2010-11-01 02:00:00</th>
      <td>0.4614</td>
      <td>0.0</td>
      <td>0.4723</td>
      <td>0.0000</td>
      <td>0.4671</td>
      <td>0.0000</td>
      <td>0.5002</td>
      <td>0.0000</td>
      <td>0.4619</td>
      <td>0.0000</td>
      <td>...</td>
      <td>0.5060</td>
      <td>0.0</td>
      <td>0.4827</td>
      <td>0.0000</td>
      <td>0.4987</td>
      <td>0.0</td>
      <td>0.5143</td>
      <td>0.0</td>
      <td>0.5084</td>
      <td>0.0</td>
    </tr>
  </tbody>
</table>
<p>3 rows × 84 columns</p>
</div>




```python
simulation.play_input(se_climate)
simulation.set_simulation_span(xr_ts_start(se_climate), xr_ts_end(se_climate))
simulation.set_simulation_time_step('hourly')
```

The `doc_helper` submodule has helper functions to configure the gr4j model to such that it is fit to run on hourly data:


```python
std.configure_hourly_gr4j(simulation)
```

## Parameterisation

We define a function creating a realistic feasible parameter space. This is not the main object of this vignette, so we do not describe in details. 


```python
import swift2.helpers as hlp
import swift2.parameteriser as sp
from swift2.utils import as_xarray_series, c, paste0, rep

def create_meta_parameteriser(simulation:Simulation, ref_area=250, time_span=3600):  
    time_span = int(time_span)
    parameteriser = std.define_gr4j_scaled_parameter(ref_area, time_span)
  
    # Let's define _S0_ and _R0_ parameters such that for each GR4J model instance, _S = S0 * x1_ and _R = R0 * x3_
    p_states = sp.linear_parameteriser(
                      param_name=c("S0","R0"), 
                      state_name=c("S","R"), 
                      scaling_var_name=c("x1","x3"),
                      min_p_val=c(0.0,0.0), 
                      max_p_val=c(1.0,1.0), 
                      value=c(0.9,0.9), 
                      selector_type='each subarea')
  
    init_parameteriser = p_states.make_state_init_parameteriser()
    parameteriser = sp.concatenate_parameterisers(parameteriser, init_parameteriser)
    
    hlp.lag_and_route_linear_storage_type(simulation)
    hlp.set_reach_lengths_lag_n_route(simulation)

    lnrp = hlp.parameteriser_lag_and_route()
    parameteriser = CompositeParameteriser.concatenate(parameteriser, lnrp, strategy='')
    return parameteriser
```


```python
parameteriser = create_meta_parameteriser(simulation)
parameteriser.as_dataframe()
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
      <td>log_x4</td>
      <td>0.305422</td>
      <td>0.000000</td>
      <td>2.380211</td>
    </tr>
    <tr>
      <th>1</th>
      <td>log_x1</td>
      <td>0.506690</td>
      <td>0.000000</td>
      <td>3.778151</td>
    </tr>
    <tr>
      <th>2</th>
      <td>log_x3</td>
      <td>0.315425</td>
      <td>0.000000</td>
      <td>3.000000</td>
    </tr>
    <tr>
      <th>3</th>
      <td>asinh_x2</td>
      <td>2.637752</td>
      <td>-3.989327</td>
      <td>3.989327</td>
    </tr>
    <tr>
      <th>4</th>
      <td>R0</td>
      <td>0.900000</td>
      <td>0.000000</td>
      <td>1.000000</td>
    </tr>
    <tr>
      <th>5</th>
      <td>S0</td>
      <td>0.900000</td>
      <td>0.000000</td>
      <td>1.000000</td>
    </tr>
    <tr>
      <th>6</th>
      <td>alpha</td>
      <td>1.000000</td>
      <td>0.001000</td>
      <td>100.000000</td>
    </tr>
    <tr>
      <th>7</th>
      <td>inverse_velocity</td>
      <td>1.000000</td>
      <td>0.001000</td>
      <td>100.000000</td>
    </tr>
  </tbody>
</table>
</div>



Now, checking that a default parameter set works structurally on the simulation:


```python
parameteriser.set_parameter_value('asinh_x2', 0)
parameteriser.apply_sys_config(simulation)
simulation.exec_simulation()
```

We are now ready to enter the main topic of this vignette, subsetting the catchment into subcatchments for calibration purposes.

## Splitting the catchment in subcatchments

The sample gauge data flow contains identifiers that are of course distinct from the network node identifiers. We create a map between them (note - this information used to be in the NodeLink file in swiftv1), and we use these node as splitting points to derive subcatchments


```python
gauges = c( '92106', '592002', '18311', '93044',    '25',   '181')
node_ids = paste0('node.', c('7',   '12',   '25',   '30',   '40',   '43'))
node_gauges = OrderedDict([(node_ids[i], gauges[i]) for i in range(len(gauges))])
# names(gauges) = node_ids
```

### Test running and recording streamflows


```python
simulation.get_variable_ids(node_ids[0])
```




    ['node.7.InflowRate',
     'node.7.InflowVolume',
     'node.7.AdditionalInflowRate',
     'node.7.OutflowRate',
     'node.7.OutflowVolume']




```python
simulation.record_state(paste0(node_ids, ".OutflowRate"))
```


```python
simulation.exec_simulation()
```


```python
modelled = simulation.get_all_recorded()
```


```python
modelled
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
</style><pre class='xr-text-repr-fallback'>&lt;xarray.DataArray (variable_identifiers: 6, ensemble: 1, time: 480)&gt; Size: 23kB
array([[[11.80066449,  7.44947703, 18.42497666, ...,  0.28179863,
          0.27663744,  0.27165243]],

       [[11.19512081,  6.66918055, 12.49597281, ...,  0.38460207,
          0.38065825,  0.37679025]],

       [[ 6.83285487, 10.68999615, 17.44945727, ...,  2.26019515,
          2.22860765,  2.19794827]],

       [[11.86391178, 12.88237054, 11.40568098, ...,  0.13346021,
          0.13235124,  0.13125882]],

       [[19.862354  , 11.83475444,  8.23442729, ...,  3.61385335,
          3.55119926,  3.49124398]],

       [[20.9016399 , 23.51593328, 28.95913953, ...,  0.43200931,
          0.42719557,  0.42247987]]], shape=(6, 1, 480))
Coordinates:
  * ensemble              (ensemble) int64 8B 0
  * time                  (time) datetime64[ns] 4kB 2010-11-01 ... 2010-11-20...
  * variable_identifiers  (variable_identifiers) object 48B &#x27;node.12.OutflowR...</pre><div class='xr-wrap' style='display:none'><div class='xr-header'><div class='xr-obj-type'>xarray.DataArray</div><div class='xr-array-name'></div><ul class='xr-dim-list'><li><span class='xr-has-index'>variable_identifiers</span>: 6</li><li><span class='xr-has-index'>ensemble</span>: 1</li><li><span class='xr-has-index'>time</span>: 480</li></ul></div><ul class='xr-sections'><li class='xr-section-item'><div class='xr-array-wrap'><input id='section-0358d421-adb9-4f39-ba89-173adaf921f7' class='xr-array-in' type='checkbox' checked><label for='section-0358d421-adb9-4f39-ba89-173adaf921f7' title='Show/hide data repr'><svg class='icon xr-icon-database'><use xlink:href='#icon-database'></use></svg></label><div class='xr-array-preview xr-preview'><span>11.8 7.449 18.42 11.78 8.579 ... 0.4419 0.4369 0.432 0.4272 0.4225</span></div><div class='xr-array-data'><pre>array([[[11.80066449,  7.44947703, 18.42497666, ...,  0.28179863,
          0.27663744,  0.27165243]],

       [[11.19512081,  6.66918055, 12.49597281, ...,  0.38460207,
          0.38065825,  0.37679025]],

       [[ 6.83285487, 10.68999615, 17.44945727, ...,  2.26019515,
          2.22860765,  2.19794827]],

       [[11.86391178, 12.88237054, 11.40568098, ...,  0.13346021,
          0.13235124,  0.13125882]],

       [[19.862354  , 11.83475444,  8.23442729, ...,  3.61385335,
          3.55119926,  3.49124398]],

       [[20.9016399 , 23.51593328, 28.95913953, ...,  0.43200931,
          0.42719557,  0.42247987]]], shape=(6, 1, 480))</pre></div></div></li><li class='xr-section-item'><input id='section-c4c1d326-23d5-4add-8da7-a7a81d98a492' class='xr-section-summary-in' type='checkbox'  checked><label for='section-c4c1d326-23d5-4add-8da7-a7a81d98a492' class='xr-section-summary' >Coordinates: <span>(3)</span></label><div class='xr-section-inline-details'></div><div class='xr-section-details'><ul class='xr-var-list'><li class='xr-var-item'><div class='xr-var-name'><span class='xr-has-index'>ensemble</span></div><div class='xr-var-dims'>(ensemble)</div><div class='xr-var-dtype'>int64</div><div class='xr-var-preview xr-preview'>0</div><input id='attrs-5e7ef644-d478-4118-9998-31622d780dec' class='xr-var-attrs-in' type='checkbox' disabled><label for='attrs-5e7ef644-d478-4118-9998-31622d780dec' title='Show/Hide attributes'><svg class='icon xr-icon-file-text2'><use xlink:href='#icon-file-text2'></use></svg></label><input id='data-c8eef087-996b-4898-aa14-b9d5712653f8' class='xr-var-data-in' type='checkbox'><label for='data-c8eef087-996b-4898-aa14-b9d5712653f8' title='Show/Hide data repr'><svg class='icon xr-icon-database'><use xlink:href='#icon-database'></use></svg></label><div class='xr-var-attrs'><dl class='xr-attrs'></dl></div><div class='xr-var-data'><pre>array([0])</pre></div></li><li class='xr-var-item'><div class='xr-var-name'><span class='xr-has-index'>time</span></div><div class='xr-var-dims'>(time)</div><div class='xr-var-dtype'>datetime64[ns]</div><div class='xr-var-preview xr-preview'>2010-11-01 ... 2010-11-20T23:00:00</div><input id='attrs-e84ef6d5-7347-43fa-a0f5-20ed12dc8d1e' class='xr-var-attrs-in' type='checkbox' disabled><label for='attrs-e84ef6d5-7347-43fa-a0f5-20ed12dc8d1e' title='Show/Hide attributes'><svg class='icon xr-icon-file-text2'><use xlink:href='#icon-file-text2'></use></svg></label><input id='data-3e373974-cb9d-44ed-8524-89b8b39f481f' class='xr-var-data-in' type='checkbox'><label for='data-3e373974-cb9d-44ed-8524-89b8b39f481f' title='Show/Hide data repr'><svg class='icon xr-icon-database'><use xlink:href='#icon-database'></use></svg></label><div class='xr-var-attrs'><dl class='xr-attrs'></dl></div><div class='xr-var-data'><pre>array([&#x27;2010-11-01T00:00:00.000000000&#x27;, &#x27;2010-11-01T01:00:00.000000000&#x27;,
       &#x27;2010-11-01T02:00:00.000000000&#x27;, ..., &#x27;2010-11-20T21:00:00.000000000&#x27;,
       &#x27;2010-11-20T22:00:00.000000000&#x27;, &#x27;2010-11-20T23:00:00.000000000&#x27;],
      shape=(480,), dtype=&#x27;datetime64[ns]&#x27;)</pre></div></li><li class='xr-var-item'><div class='xr-var-name'><span class='xr-has-index'>variable_identifiers</span></div><div class='xr-var-dims'>(variable_identifiers)</div><div class='xr-var-dtype'>object</div><div class='xr-var-preview xr-preview'>&#x27;node.12.OutflowRate&#x27; ... &#x27;node....</div><input id='attrs-57e8121b-a981-4bea-834f-eeb589fec88a' class='xr-var-attrs-in' type='checkbox' disabled><label for='attrs-57e8121b-a981-4bea-834f-eeb589fec88a' title='Show/Hide attributes'><svg class='icon xr-icon-file-text2'><use xlink:href='#icon-file-text2'></use></svg></label><input id='data-c86f8d1f-107a-4720-a6eb-2b8f8b674231' class='xr-var-data-in' type='checkbox'><label for='data-c86f8d1f-107a-4720-a6eb-2b8f8b674231' title='Show/Hide data repr'><svg class='icon xr-icon-database'><use xlink:href='#icon-database'></use></svg></label><div class='xr-var-attrs'><dl class='xr-attrs'></dl></div><div class='xr-var-data'><pre>array([&#x27;node.12.OutflowRate&#x27;, &#x27;node.25.OutflowRate&#x27;, &#x27;node.30.OutflowRate&#x27;,
       &#x27;node.40.OutflowRate&#x27;, &#x27;node.43.OutflowRate&#x27;, &#x27;node.7.OutflowRate&#x27;],
      dtype=object)</pre></div></li></ul></div></li><li class='xr-section-item'><input id='section-a6362164-43ce-4633-bcf3-e6d7c1da816b' class='xr-section-summary-in' type='checkbox'  ><label for='section-a6362164-43ce-4633-bcf3-e6d7c1da816b' class='xr-section-summary' >Indexes: <span>(3)</span></label><div class='xr-section-inline-details'></div><div class='xr-section-details'><ul class='xr-var-list'><li class='xr-var-item'><div class='xr-index-name'><div>ensemble</div></div><div class='xr-index-preview'>PandasIndex</div><div></div><input id='index-dedd5cc4-9257-432c-8888-0b5f3835e285' class='xr-index-data-in' type='checkbox'/><label for='index-dedd5cc4-9257-432c-8888-0b5f3835e285' title='Show/Hide index repr'><svg class='icon xr-icon-database'><use xlink:href='#icon-database'></use></svg></label><div class='xr-index-data'><pre>PandasIndex(Index([0], dtype=&#x27;int64&#x27;, name=&#x27;ensemble&#x27;))</pre></div></li><li class='xr-var-item'><div class='xr-index-name'><div>time</div></div><div class='xr-index-preview'>PandasIndex</div><div></div><input id='index-f143a7e1-7c7b-4663-aa0b-cae83cb62aa9' class='xr-index-data-in' type='checkbox'/><label for='index-f143a7e1-7c7b-4663-aa0b-cae83cb62aa9' title='Show/Hide index repr'><svg class='icon xr-icon-database'><use xlink:href='#icon-database'></use></svg></label><div class='xr-index-data'><pre>PandasIndex(DatetimeIndex([&#x27;2010-11-01 00:00:00&#x27;, &#x27;2010-11-01 01:00:00&#x27;,
               &#x27;2010-11-01 02:00:00&#x27;, &#x27;2010-11-01 03:00:00&#x27;,
               &#x27;2010-11-01 04:00:00&#x27;, &#x27;2010-11-01 05:00:00&#x27;,
               &#x27;2010-11-01 06:00:00&#x27;, &#x27;2010-11-01 07:00:00&#x27;,
               &#x27;2010-11-01 08:00:00&#x27;, &#x27;2010-11-01 09:00:00&#x27;,
               ...
               &#x27;2010-11-20 14:00:00&#x27;, &#x27;2010-11-20 15:00:00&#x27;,
               &#x27;2010-11-20 16:00:00&#x27;, &#x27;2010-11-20 17:00:00&#x27;,
               &#x27;2010-11-20 18:00:00&#x27;, &#x27;2010-11-20 19:00:00&#x27;,
               &#x27;2010-11-20 20:00:00&#x27;, &#x27;2010-11-20 21:00:00&#x27;,
               &#x27;2010-11-20 22:00:00&#x27;, &#x27;2010-11-20 23:00:00&#x27;],
              dtype=&#x27;datetime64[ns]&#x27;, name=&#x27;time&#x27;, length=480, freq=&#x27;h&#x27;))</pre></div></li><li class='xr-var-item'><div class='xr-index-name'><div>variable_identifiers</div></div><div class='xr-index-preview'>PandasIndex</div><div></div><input id='index-b0f9620a-b9ae-4e9c-8744-077e58374e75' class='xr-index-data-in' type='checkbox'/><label for='index-b0f9620a-b9ae-4e9c-8744-077e58374e75' title='Show/Hide index repr'><svg class='icon xr-icon-database'><use xlink:href='#icon-database'></use></svg></label><div class='xr-index-data'><pre>PandasIndex(Index([&#x27;node.12.OutflowRate&#x27;, &#x27;node.25.OutflowRate&#x27;, &#x27;node.30.OutflowRate&#x27;,
       &#x27;node.40.OutflowRate&#x27;, &#x27;node.43.OutflowRate&#x27;, &#x27;node.7.OutflowRate&#x27;],
      dtype=&#x27;object&#x27;, name=&#x27;variable_identifiers&#x27;))</pre></div></li></ul></div></li><li class='xr-section-item'><input id='section-a9dad319-4d93-4368-8de4-3e089d90ba7c' class='xr-section-summary-in' type='checkbox' disabled ><label for='section-a9dad319-4d93-4368-8de4-3e089d90ba7c' class='xr-section-summary'  title='Expand/collapse section'>Attributes: <span>(0)</span></label><div class='xr-section-inline-details'></div><div class='xr-section-details'><dl class='xr-attrs'></dl></div></li></ul></div></div>




```python
modelled.sel(variable_identifiers='node.7.OutflowRate').plot()
```




    [<matplotlib.lines.Line2D at 0x7fe789309510>]




    
![png](calibrate_subcatchments_files/calibrate_subcatchments_33_1.png)
    



```python
se_flows[gauges[3]].plot()
```




    <Axes: >




    
![png](calibrate_subcatchments_files/calibrate_subcatchments_34_1.png)
    



```python
import seaborn as sns
import matplotlib.pyplot as plt

def plot_multivariate_time_series(df, cols_wrap=3):
    """
    Plots all columns of a Pandas DataFrame (time series) in a grid using Seaborn.

    Args:
        df (pd.DataFrame): DataFrame with a DatetimeIndex.
        cols_wrap (int): Number of columns in the grid.  Defaults to 3.
    """

    num_cols = len(df.columns)
    num_rows = (num_cols + cols_wrap - 1) // cols_wrap  # Calculate number of rows needed

    fig, axes = plt.subplots(num_rows, cols_wrap, figsize=(15, 5 * num_rows)) # Adjust figure size as needed
    axes = axes.flatten()  # Flatten the axes array for easy indexing

    for i, col in enumerate(df.columns):
        sns.lineplot(x=df.index, y=df[col], ax=axes[i])
        axes[i].set_title(col)
        axes[i].tick_params(axis='x', rotation=45)  # Rotate x-axis labels for readability

    # Remove any unused subplots
    for i in range(num_cols, len(axes)):
        fig.delaxes(axes[i])

    plt.tight_layout()  # Adjust layout to prevent overlapping titles/labels
    plt.show()

# Example usage (assuming you have a DataFrame called 'se_flows')
plot_multivariate_time_series(se_flows)
```


    
![png](calibrate_subcatchments_files/calibrate_subcatchments_35_0.png)
    



```python
split_element_ids = node_ids
sub_cats = simulation.split_to_subcatchments(split_element_ids)
sub_cats
```




    OrderedDict([('node.40',
                  Simulation wrapper for a CFFI pointer handle to a native pointer of type id "MODEL_SIMULATION_PTR"),
                 ('node.25',
                  Simulation wrapper for a CFFI pointer handle to a native pointer of type id "MODEL_SIMULATION_PTR"),
                 ('node.12',
                  Simulation wrapper for a CFFI pointer handle to a native pointer of type id "MODEL_SIMULATION_PTR"),
                 ('node.7',
                  Simulation wrapper for a CFFI pointer handle to a native pointer of type id "MODEL_SIMULATION_PTR"),
                 ('node.30',
                  Simulation wrapper for a CFFI pointer handle to a native pointer of type id "MODEL_SIMULATION_PTR"),
                 ('node.43',
                  Simulation wrapper for a CFFI pointer handle to a native pointer of type id "MODEL_SIMULATION_PTR")])



The resulting list of subcatchment simulations is already ordered in an upstream to downstream order by SWIFT.

If we are to set up the first step of the sequential calibration:


```python
sub_cats['node.40'].describe()
```




    {'subareas': {'37': 'Subarea_37', '38': 'Subarea_38', '39': 'Subarea_39'},
     'nodes': {'40': 'Node_40', '39': 'Node_39', '38': 'Node_38', '37': 'Node_37'},
     'links': {'39': 'Subarea_39', '38': 'Subarea_38', '37': 'Subarea_37'}}




```python
def first(d:OrderedDict):
    return list(sub_cats.items())[0]  
```


```python
element_id = first(sub_cats)[0]
element_id
```




    'node.40'




```python
gaugeId = node_gauges[element_id]
gaugeId
```




    np.str_('25')




```python
gauge_flow = se_flows[[gaugeId]]
gauge_flow.head()
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
      <th>25</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>2010-11-01 00:00:00</th>
      <td>1.229</td>
    </tr>
    <tr>
      <th>2010-11-01 01:00:00</th>
      <td>1.259</td>
    </tr>
    <tr>
      <th>2010-11-01 02:00:00</th>
      <td>1.280</td>
    </tr>
    <tr>
      <th>2010-11-01 03:00:00</th>
      <td>1.291</td>
    </tr>
    <tr>
      <th>2010-11-01 04:00:00</th>
      <td>1.296</td>
    </tr>
  </tbody>
</table>
</div>




```python
sc = sub_cats[element_id]
sc
```




    Simulation wrapper for a CFFI pointer handle to a native pointer of type id "MODEL_SIMULATION_PTR"




```python
parameteriser.apply_sys_config(sc)
var_id = CATCHMENT_FLOWRATE_VARID
sc.record_state(var_id)
```


```python
# DiagrammeR(getCatchmentDotGraph(sc))
```

Let's view the default, uncalibrated output 


```python
simulation.get_simulation_span()
```




    {'start': datetime.datetime(2010, 11, 1, 0, 0),
     'end': datetime.datetime(2010, 11, 20, 23, 0),
     'time step': 'hourly'}




```python
def plot_obs_vs_calc(obs, calc, ylab="streamflow (m3/s)"):
    plot_two_series(obs, calc, start_time = xr_ts_start(obs), end_time = xr_ts_end(obs))
```


```python
gauge_flow = as_xarray_series(gauge_flow)
```


```python
sc.exec_simulation()
plot_obs_vs_calc(gauge_flow, sc.get_recorded(var_id))
```


    
![png](calibrate_subcatchments_files/calibrate_subcatchments_50_0.png)
    


Now, setting up an objective (NSE) and optimiser:


```python
objectiveId = 'NSE'
objective = sc.create_objective(var_id, gauge_flow, objectiveId, xr_ts_start(se_flows), xr_ts_end(se_flows))
score = objective.get_score(parameteriser)  
```


```python
# termination = getMarginalTermination( tolerance = 1e-04, cutoff_no_improvement = 30, max_hours = 2/60) 
termination = sp.create_sce_termination_wila('relative standard deviation', c('0.05','0.0167'))
sce_params = sp.get_default_sce_parameters()
params = parameteriser.as_dataframe()
```


```python
np.count_nonzero(abs(params.Max-params.Min)>0)
```




    8




```python
npars = np.count_nonzero(abs(params.Max-params.Min)>0)
sce_params = std.sce_parameter(npars)
optimiser = objective.create_sce_optim_swift(termination_criterion = termination, population_initialiser = parameteriser,sce_params = sce_params)
calib_logger = optimiser.set_calibration_logger("dummy")
```


```python
%%time
calib_results = optimiser.execute_optimisation()
```

    CPU times: user 3min 12s, sys: 113 ms, total: 3min 13s
    Wall time: 30.3 s


And the resulting hydrograph follows. The NSE score is decent, but the magnitude of the peak is not well represented. We used a uniform value for the routing parameters; having a scaling based on link properties may be a line of enquiry.


```python
sorted_results = calib_results.sort_by_score('NSE')
d = sorted_results.as_dataframe()
d.head()
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
      <th>NSE</th>
      <th>log_x4</th>
      <th>log_x1</th>
      <th>log_x3</th>
      <th>asinh_x2</th>
      <th>R0</th>
      <th>S0</th>
      <th>alpha</th>
      <th>inverse_velocity</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>0.888691</td>
      <td>2.035628</td>
      <td>1.486090</td>
      <td>1.225119</td>
      <td>0.701559</td>
      <td>0.298493</td>
      <td>0.965622</td>
      <td>37.718084</td>
      <td>19.212767</td>
    </tr>
    <tr>
      <th>1</th>
      <td>0.888215</td>
      <td>2.014001</td>
      <td>1.434314</td>
      <td>1.211284</td>
      <td>0.825745</td>
      <td>0.311075</td>
      <td>0.913083</td>
      <td>33.815693</td>
      <td>24.118050</td>
    </tr>
    <tr>
      <th>2</th>
      <td>0.882085</td>
      <td>2.049073</td>
      <td>1.563873</td>
      <td>1.215658</td>
      <td>0.660270</td>
      <td>0.320351</td>
      <td>0.934830</td>
      <td>39.560723</td>
      <td>24.726786</td>
    </tr>
    <tr>
      <th>3</th>
      <td>0.881787</td>
      <td>2.019078</td>
      <td>1.451620</td>
      <td>1.128354</td>
      <td>0.751965</td>
      <td>0.314474</td>
      <td>0.908081</td>
      <td>43.861289</td>
      <td>24.969963</td>
    </tr>
    <tr>
      <th>4</th>
      <td>0.881515</td>
      <td>2.030478</td>
      <td>1.473141</td>
      <td>1.188788</td>
      <td>0.771365</td>
      <td>0.321442</td>
      <td>0.887965</td>
      <td>34.698517</td>
      <td>20.905070</td>
    </tr>
  </tbody>
</table>
</div>




```python
d.tail()
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
      <th>NSE</th>
      <th>log_x4</th>
      <th>log_x1</th>
      <th>log_x3</th>
      <th>asinh_x2</th>
      <th>R0</th>
      <th>S0</th>
      <th>alpha</th>
      <th>inverse_velocity</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>165</th>
      <td>0.845689</td>
      <td>2.028324</td>
      <td>1.582868</td>
      <td>1.221594</td>
      <td>0.795570</td>
      <td>0.368405</td>
      <td>0.831138</td>
      <td>40.191087</td>
      <td>31.035859</td>
    </tr>
    <tr>
      <th>166</th>
      <td>0.845672</td>
      <td>2.025205</td>
      <td>1.593455</td>
      <td>1.036830</td>
      <td>0.603336</td>
      <td>0.359309</td>
      <td>0.814243</td>
      <td>39.263846</td>
      <td>34.006800</td>
    </tr>
    <tr>
      <th>167</th>
      <td>0.845376</td>
      <td>2.053991</td>
      <td>1.633836</td>
      <td>1.079567</td>
      <td>0.692984</td>
      <td>0.355601</td>
      <td>0.867360</td>
      <td>43.172832</td>
      <td>18.738915</td>
    </tr>
    <tr>
      <th>168</th>
      <td>0.844877</td>
      <td>2.014712</td>
      <td>1.470771</td>
      <td>1.077956</td>
      <td>0.631176</td>
      <td>0.357918</td>
      <td>0.888920</td>
      <td>27.770611</td>
      <td>23.967920</td>
    </tr>
    <tr>
      <th>169</th>
      <td>0.844075</td>
      <td>2.006066</td>
      <td>1.600531</td>
      <td>1.201941</td>
      <td>0.788367</td>
      <td>0.363589</td>
      <td>0.814611</td>
      <td>36.803100</td>
      <td>29.462903</td>
    </tr>
  </tbody>
</table>
</div>




```python
p = sorted_results.get_parameters_at_index(1)
p
```




                   Name      Value       Min         Max
    0            log_x4   2.035628  0.000000    2.380211
    1            log_x1   1.486090  0.000000    3.778151
    2            log_x3   1.225119  0.000000    3.000000
    3          asinh_x2   0.701559 -3.989327    3.989327
    4                R0   0.298493  0.000000    1.000000
    5                S0   0.965622  0.000000    1.000000
    6             alpha  37.718084  0.001000  100.000000
    7  inverse_velocity  19.212767  0.001000  100.000000




```python
p.apply_sys_config(sc)
sc.exec_simulation()
plot_obs_vs_calc(gauge_flow, sc.get_recorded(var_id))
```


    
![png](calibrate_subcatchments_files/calibrate_subcatchments_61_0.png)
    


We can create a subcatchment parameteriser, such that when applied to the whole of the South Esk, only the states of the subareas, links and nodes of the subcatchment are potentially affected.


```python
sp = p.subcatchment_parameteriser(sc)
sp.apply_sys_config(simulation)
simulation.get_state_value(paste0('subarea.', np.arange(34,stop=41), '.x2'))
# saIds = get_subarea_ids(simulation)
```




    {'subarea.34.x2': 0.0,
     'subarea.35.x2': 0.0,
     'subarea.36.x2': 0.0,
     'subarea.37.x2': 0.5095629279636464,
     'subarea.38.x2': 0.5095629279636464,
     'subarea.39.x2': 0.5095629279636464,
     'subarea.40.x2': 0.0}




```python
# TODO
# spFile = tempfile()
# SaveParameterizer_R(sp, spFile)
# # Following fails 2020-06, see https://jira.csiro.au/browse/WIRADA-631 
# # sp2 = LoadParameterizer_R(spFile)

# if(file.exists(spFile)) { file.remove(spFile) }
```


```python
p = sorted_results.get_parameters_at_index(1)
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
      <td>log_x4</td>
      <td>2.035628</td>
      <td>0.000000</td>
      <td>2.380211</td>
    </tr>
    <tr>
      <th>1</th>
      <td>log_x1</td>
      <td>1.486090</td>
      <td>0.000000</td>
      <td>3.778151</td>
    </tr>
    <tr>
      <th>2</th>
      <td>log_x3</td>
      <td>1.225119</td>
      <td>0.000000</td>
      <td>3.000000</td>
    </tr>
    <tr>
      <th>3</th>
      <td>asinh_x2</td>
      <td>0.701559</td>
      <td>-3.989327</td>
      <td>3.989327</td>
    </tr>
    <tr>
      <th>4</th>
      <td>R0</td>
      <td>0.298493</td>
      <td>0.000000</td>
      <td>1.000000</td>
    </tr>
    <tr>
      <th>5</th>
      <td>S0</td>
      <td>0.965622</td>
      <td>0.000000</td>
      <td>1.000000</td>
    </tr>
    <tr>
      <th>6</th>
      <td>alpha</td>
      <td>37.718084</td>
      <td>0.001000</td>
      <td>100.000000</td>
    </tr>
    <tr>
      <th>7</th>
      <td>inverse_velocity</td>
      <td>19.212767</td>
      <td>0.001000</td>
      <td>100.000000</td>
    </tr>
  </tbody>
</table>
</div>




```python
# swoop(sc, p, param_name, from, to, num=10, var_id) {
#   if(missing(from)) { from = GetParameterMinValue_R(p, param_name)}
#   if(missing(to))   { to = GetParameterMaxValue_R(p, param_name)}
#   oat(sc, p, param_name, from=from, to=to, num=num, var_id) 
# }

# testp(sim, p, ...) {
#   q = CloneHypercubeParameterizer_R(p)
#   execSimulation(sim)
#   params = list(...)
#   for(pname in names(params)) {set_parameter_value(q, pname, params[[pname]])}
#   plot_obs_vs_calc(gaugeFlow, getRecorded(sim, var_id))
# }

# flows = swoop(sc, p, 'log_x4', var_id=var_id)

# flows = swoop('log_x1')
# flows = swoop('Alpha')
# flows = merge(flows, gaugeFlow)
# zoo::plot.zoo(flows, plot.type='single')
# col=c('orange', 'black','blue','red')

# f(...) {
# params = list(...)
# params
# set_parameter_value(p, names(params), as.numeric(params))
# applySysConfig(p, sc)
# execSimulation(sc)
# plot_obs_vs_calc(gaugeFlow, getRecorded(sc, var_id))
# }
```

## Whole of catchment calibration combining point gauges


```python
gauges = c( '92106', '592002', '18311', '93044',    '25',   '181')
node_ids = paste0('node.', c('7',   '12',   '25',   '30',   '40',   '43'))
node_gauges = OrderedDict([(node_ids[i], gauges[i]) for i in range(len(gauges))])
# names(gauges) = node_ids
```


```python
calibNodes = paste0('node.', ["7","12"])


```


```python
element_id = first(sub_cats)[0]
element_id
```




    'node.40'




```python
gaugeId = [node_gauges[k] for k in calibNodes]
gauge_flow = se_flows[gaugeId]
```


```python
sc = sub_cats[element_id]
parameteriser.apply_sys_config(sc)

var_id = paste0(calibNodes, '.OutflowRate')
simulation.record_state(var_id)
```


```python

```


```python
objectiveId = 'NSE'

def create_obj_station(i:int):
    obs = as_xarray_series(gauge_flow[[gaugeId[i]]])
    return simulation.create_objective(var_id[i], obs, objectiveId, xr_ts_start(se_flows), xr_ts_end(se_flows))

objectives = [create_obj_station(i) for i in [0,1]]

co = ObjectiveEvaluator.create_composite_objective(objectives, [1.0,1.0], var_id[:2])
```


```python
score = co.get_score(parameteriser) 
# scoresAsDataFrame(score)
```


```python
score
```




    {'scores': {'NSE:1.000000,NSE:1.000000': -262.1398134692315},
     'sysconfig':                Name     Value       Min         Max
     0            log_x4  0.305422  0.000000    2.380211
     1            log_x1  0.506690  0.000000    3.778151
     2            log_x3  0.315425  0.000000    3.000000
     3          asinh_x2  0.000000 -3.989327    3.989327
     4                R0  0.900000  0.000000    1.000000
     5                S0  0.900000  0.000000    1.000000
     6             alpha  1.000000  0.001000  100.000000
     7  inverse_velocity  1.000000  0.001000  100.000000}




```python

```
