# Reservoir geometry

## About this document



```python
from swift2.doc_helper import pkg_versions_info

print(pkg_versions_info("This document was generated from a jupyter notebook"))
```

    This document was generated from a jupyter notebook on 2025-03-27 17:26:37.302534
        swift2 2.5.1
        uchronia 2.6.2



```python
from cinterop.timeseries import xr_ts_end, xr_ts_start
from swift2.doc_helper import (
    configure_hourly_gr4j,
    define_parameteriser_gr4j_muskingum,
    sample_catchment_model,
    sample_series,
)
from swift2.simulation import swap_model
from swift2.utils import mk_full_data_id
from swift2.vis import plot_two_series
```

## Model structure

**Note**: Setting up this model prior to adding a reservoir node is not the primary purpose of this vignette, so you may skip this section.


```python
catchmentStructure = sample_catchment_model(site_id = "Adelaide", config_id = "catchment")

hydromodel = "GR4J"
channel_routing = 'MuskingumNonLinear'
hydroModelRainfallId = 'P'
hydroModelEvapId = 'E'

# set models
insimulation = swap_model(catchmentStructure, model_id = hydromodel ,what = "runoff")
simulation = swap_model(insimulation, model_id = channel_routing ,what = "channel_routing")

saId = simulation.get_subarea_ids()
assert len(saId) == 1

precipTs = sample_series(site_id = "Adelaide", var_name = "rain")
evapTs = sample_series(site_id = "Adelaide", var_name = "evap")
flowRateTs = sample_series(site_id = "Adelaide", var_name = "flow")
```


```python
mk_full_data_id('subarea', saId, hydroModelRainfallId)
```




    ['subarea.1.P']




```python
simulation.play_input(precipTs, mk_full_data_id('subarea', saId, hydroModelRainfallId))
simulation.play_input(evapTs, mk_full_data_id('subarea', saId, hydroModelEvapId))
configure_hourly_gr4j(simulation)
simulation.set_simulation_time_step('hourly')

# Small time interval only, to reduce runtimes in this vignette

from uchronia.time_series import mk_date

simstart = mk_date(2010,9,1)  
simend = mk_date(2012,6,30,23)  
simwarmup = simstart
simulation.set_simulation_span(simstart, simend)
```


```python

```


```python
def templateHydroParameterizer(simulation):
    return define_parameteriser_gr4j_muskingum(ref_area=250.0,
        time_span=3600,
        simulation=simulation,
        objfun="NSE",
        delta_t=1.0,
        param_name_k='Alpha')


nodeId = 'node.2'
flowId = mk_full_data_id(nodeId, 'OutflowRate')

simulation.record_state(flowId)
```

We use pre-calibrated hydrologic parameters 


```python
p = templateHydroParameterizer(simulation)
p.set_min_parameter_value('R0', 0.0)
p.set_max_parameter_value('R0', 1.0)
p.set_min_parameter_value('S0', 0.0)
p.set_max_parameter_value('S0', 1.0)
p.set_parameter_value('log_x4', 1.017730e+00)
p.set_parameter_value('log_x1', 2.071974e+00	)
p.set_parameter_value('log_x3', 1.797909e+00	)
p.set_parameter_value('asinh_x2', -1.653842e+00)	
p.set_parameter_value('R0', 2.201930e-11	)
p.set_parameter_value('S0', 3.104968e-11	)
p.set_parameter_value('X', 6.595537e-03	) # Gotcha: needs to be set before alpha is changed.
p.set_parameter_value('Alpha', 6.670534e-01	)
p
```




           Name         Value       Min       Max
    0    log_x4  1.017730e+00  0.000000  2.380211
    1    log_x1  2.071974e+00  0.000000  3.778151
    2    log_x3  1.797909e+00  0.000000  3.000000
    3  asinh_x2 -1.653842e+00 -3.989327  3.989327
    4        R0  2.201930e-11  0.000000  1.000000
    5        S0  3.104968e-11  0.000000  1.000000
    6         X  6.595537e-03  0.001000  0.016622
    7     Alpha  6.670534e-01  0.011162  1.681129



We get a visual on the output of the catchment simulation.


```python
sViz = mk_date(2010,12,1)
eViz = mk_date(2011,4,30,23)

def subsetPlot(tts):
    from cinterop.timeseries import ts_window
    return ts_window(tts, from_date=sViz, to_date=eViz) 

def plot_obs_vs_calc(obs, calc, names= None, ylab="flow (m3/s)"):
    obs = subsetPlot(obs)
    calc = subsetPlot(calc)
    return plot_two_series(obs, calc, ylab=ylab, names=names, start_time = xr_ts_start(calc), end_time = xr_ts_end(calc))

p.apply_sys_config(simulation)
```

## A look at the model simulation prior to setting up a reservoir


```python
simulation.exec_simulation()
catchmentOutflowNoReservoir = simulation.get_recorded(flowId)
plot_obs_vs_calc(flowRateTs, catchmentOutflowNoReservoir, names=["observed", "modelled - no reservoir"])
```


    
![png](reservoir_geometry_files/reservoir_geometry_15_0.png)
    


From here on we will only work with modelled time series, as the reservoir set up will be synthetic and there is no real observations to "match".

## Set up the reservoir model

The catchment is simple, with node 2 being the outlet of the catchment so this is where we will add the reservoir


```python
simulation.describe()
```




    {'subareas': {'1': 'Subarea_1'},
     'nodes': {'2': 'Outlet', '1': 'Node_1'},
     'links': {'1': 'Subarea_1'}}




```python
simulation.get_node_ids(), simulation.get_node_names()
```




    (['2', '1'], ['Outlet', 'Node_1'])



We create a synthetic, simple reservoir geometry (level-volume-area) for this vignette.


```python
simulation.set_reservoir_model('LevelVolumeAreaReservoir', nodeId)
```


```python
import numpy as np
def seq(start, stop, by):
    import math
    assert by > 0
    n = int(math.floor( (stop - start + 1) / by ))
    return np.linspace(start=start, stop=(start+n*by-1), num=n)
```


```python
seq(1, 6, 1)
```




    array([1., 2., 3., 4., 5., 6.])




```python
seq(1, 6-0.1, 1)
```




    array([1., 2., 3., 4., 5.])




```python
import numpy as np

levels = seq(start=10.0, stop=30, by=0.1)
volumes = (levels - 10) ** 3.1 * 17000
area = volumes * 0.0
```


```python
fsv_height = 27.0
levels >= fsv_height
```




    array([False, False, False, False, False, False, False, False, False,
           False, False, False, False, False, False, False, False, False,
           False, False, False, False, False, False, False, False, False,
           False, False, False, False, False, False, False, False, False,
           False, False, False, False, False, False, False, False, False,
           False, False, False, False, False, False, False, False, False,
           False, False, False, False, False, False, False, False, False,
           False, False, False, False, False, False, False, False, False,
           False, False, False, False, False, False, False, False, False,
           False, False, False, False, False, False, False, False, False,
           False, False, False, False, False, False, False, False, False,
           False, False, False, False, False, False, False, False, False,
           False, False, False, False, False, False, False, False, False,
           False, False, False, False, False, False, False, False, False,
           False, False, False, False, False, False, False, False, False,
           False, False, False, False, False, False, False, False, False,
           False, False, False, False, False, False, False, False, False,
           False, False, False, False, False, False, False, False, False,
           False, False, False, False, False, False, False, False, False,
           False, False, False, False, False, False, False,  True,  True,
            True,  True,  True,  True,  True,  True,  True,  True,  True,
            True,  True,  True,  True,  True,  True,  True,  True,  True,
            True,  True,  True,  True,  True,  True,  True,  True,  True,
            True,  True,  True])




```python
fsv_index = np.where(levels >= fsv_height)[0][0]
```


```python
fsv = volumes[fsv_index]
fsv
```




    np.float64(111555356.428012)



Our synthetic dam can hold 111 millon cubic metres at full supply volume.


```python
import matplotlib.pyplot as plt
plt.plot(levels, volumes)
plt.xlabel("level")
plt.ylabel("volume (m3)")
# Add a horizontal line at y = fsv
plt.axhline(y=fsv, color='r', linestyle='-');
```


    
![png](reservoir_geometry_files/reservoir_geometry_29_0.png)
    



```python
simulation.set_reservoir_geometry(nodeId, levels, volumes, area)
```

### level-discharge relationships

We also create synthetic level-discharge relationships. These define the minimum and maximum outflow rates for a reservoir, given its current level. This is a generic way to capture the behavior of many reservoirs; the minimum discharge curve is typically capture the uncontrolled overspill. The maximum discharge curve is for the outflow rate with all outlets and spillway gates open. Specialisations of this reservoir (for instance as inheriting C++ classes) can then refine the behavior with additional rules on the controlled releases.  

In this example for the sake of simplicity we set up identical minimal and maximal curves. Let's say the reservoir spills above 27 metres, and between 20 and 27 the outflow rate is a linear function of the level above 20 metres datum.


```python
min_d_levels = seq(start=20, stop=fsv_height-0.01, by=0.1)
max_outlet_rate = 20 # outlet cumecs at or near full supply volume 
discharge = np.linspace( 1, len(min_d_levels), num=len(min_d_levels)) / len(min_d_levels) * max_outlet_rate
min_d_levels_spill = seq(start=fsv_height, stop=30, by=0.1)
# we define a spillover discharge function that is purely synthetic; basically made up to "work" with the sample data.  
discharge_spill = (min_d_levels_spill - fsv_height) ** 3.5 * 40 + max_outlet_rate
min_d_levels = np.concatenate([min_d_levels, min_d_levels_spill])
discharge = np.concatenate([discharge, discharge_spill])
```


```python
plt.plot(min_d_levels, discharge)
plt.xlabel("reservoir level")
plt.ylabel("discharge (m3/s)");
```


    
![png](reservoir_geometry_files/reservoir_geometry_34_0.png)
    



```python
plt.plot(min_d_levels, discharge)
plt.xlabel("reservoir level")
plt.yscale("log")  # Set the y-axis to a logarithmic scale
plt.ylabel("discharge (m3/s)");
```


    
![png](reservoir_geometry_files/reservoir_geometry_35_0.png)
    



```python
simulation.set_reservoir_min_discharge(nodeId, min_d_levels, discharge)
simulation.set_reservoir_max_discharge(nodeId, min_d_levels, discharge)
```

Let's see the resulting behavior of this storage


```python
simulation.get_variable_ids(mk_full_data_id(nodeId))
```




    ['node.2.InflowRate',
     'node.2.InflowVolume',
     'node.2.AdditionalInflowRate',
     'node.2.OutflowRate',
     'node.2.OutflowVolume',
     'node.2.reservoir.Diversion',
     'node.2.reservoir.cRelease',
     'node.2.reservoir.PreviousDiversion',
     'node.2.reservoir.PreviouscRelease',
     'node.2.reservoir.PrevioussFlow',
     'node.2.reservoir.Seepage',
     'node.2.reservoir.PreviousSeepage',
     'node.2.reservoir.rainfall',
     'node.2.reservoir.pet',
     'node.2.reservoir.PreviousInflowRate',
     'node.2.reservoir.PreviousOutflowRate',
     'node.2.reservoir.PreviousStorage',
     'node.2.reservoir.InflowRate',
     'node.2.reservoir.OutflowRate',
     'node.2.reservoir.Storage']



The reservoir model has several states to influence the mass balance. For simplicity in this vignette we will leave these at zero, but it is possible to "play" time series.


```python
simulation.record_state(mk_full_data_id(nodeId, 'reservoir.Storage'))
simulation.record_state(mk_full_data_id(nodeId, 'reservoir.OutflowRate'))
simulation.record_state(mk_full_data_id(nodeId, 'reservoir.InflowRate'))

simulation.exec_simulation()

st = simulation.get_recorded(mk_full_data_id(nodeId, 'reservoir.Storage'))
st_gl = st / 1e6 # m3 to GL
hline = st_gl.copy()
hline[:] = fsv / 1e6
```


```python
from swift2.vis import plot_series
```


```python
plot_two_series(st_gl, hline, names=['storage','FSV'], ylab='gigalitres', title=f"Reservoir levels at node {nodeId}")
```


    
![png](reservoir_geometry_files/reservoir_geometry_42_0.png)
    


### Effect of the reservoir; changed catchment outflow


```python
catchmentOutflowWithReservoir = simulation.get_recorded(flowId)
```


```python
plot_two_series(catchmentOutflowNoReservoir, catchmentOutflowWithReservoir, 
                names=["No reservoir", "With reservoir"], 
                ylab='m3/s', 
                title=f"Outflow rate at {nodeId}")
```


    
![png](reservoir_geometry_files/reservoir_geometry_45_0.png)
    



```python
catchmentOutflowWithReservoir
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
</style><pre class='xr-text-repr-fallback'>&lt;xarray.DataArray (variable_identifiers: 1, ensemble: 1, time: 16056)&gt; Size: 128kB
array([[[0.        , 0.        , 0.        , ..., 4.09947517,
         4.09481659, 4.0901634 ]]], shape=(1, 1, 16056))
Coordinates:
  * ensemble              (ensemble) int64 8B 0
  * time                  (time) datetime64[ns] 128kB 2010-09-01 ... 2012-06-...
  * variable_identifiers  (variable_identifiers) object 8B &#x27;node.2.OutflowRate&#x27;</pre><div class='xr-wrap' style='display:none'><div class='xr-header'><div class='xr-obj-type'>xarray.DataArray</div><div class='xr-array-name'></div><ul class='xr-dim-list'><li><span class='xr-has-index'>variable_identifiers</span>: 1</li><li><span class='xr-has-index'>ensemble</span>: 1</li><li><span class='xr-has-index'>time</span>: 16056</li></ul></div><ul class='xr-sections'><li class='xr-section-item'><div class='xr-array-wrap'><input id='section-49e4f24e-6d7c-405f-ae46-2c06ad63b866' class='xr-array-in' type='checkbox' checked><label for='section-49e4f24e-6d7c-405f-ae46-2c06ad63b866' title='Show/hide data repr'><svg class='icon xr-icon-database'><use xlink:href='#icon-database'></use></svg></label><div class='xr-array-preview xr-preview'><span>0.0 0.0 0.0 0.0 0.0 0.0 0.0 ... 4.113 4.109 4.104 4.099 4.095 4.09</span></div><div class='xr-array-data'><pre>array([[[0.        , 0.        , 0.        , ..., 4.09947517,
         4.09481659, 4.0901634 ]]], shape=(1, 1, 16056))</pre></div></div></li><li class='xr-section-item'><input id='section-77a607f4-e9c9-44f3-9fb2-92cbb659bca5' class='xr-section-summary-in' type='checkbox'  checked><label for='section-77a607f4-e9c9-44f3-9fb2-92cbb659bca5' class='xr-section-summary' >Coordinates: <span>(3)</span></label><div class='xr-section-inline-details'></div><div class='xr-section-details'><ul class='xr-var-list'><li class='xr-var-item'><div class='xr-var-name'><span class='xr-has-index'>ensemble</span></div><div class='xr-var-dims'>(ensemble)</div><div class='xr-var-dtype'>int64</div><div class='xr-var-preview xr-preview'>0</div><input id='attrs-31ef427d-90e7-4976-a6be-7c671aaeb1f1' class='xr-var-attrs-in' type='checkbox' disabled><label for='attrs-31ef427d-90e7-4976-a6be-7c671aaeb1f1' title='Show/Hide attributes'><svg class='icon xr-icon-file-text2'><use xlink:href='#icon-file-text2'></use></svg></label><input id='data-137f34ba-3cc5-4649-835c-6388497bfa56' class='xr-var-data-in' type='checkbox'><label for='data-137f34ba-3cc5-4649-835c-6388497bfa56' title='Show/Hide data repr'><svg class='icon xr-icon-database'><use xlink:href='#icon-database'></use></svg></label><div class='xr-var-attrs'><dl class='xr-attrs'></dl></div><div class='xr-var-data'><pre>array([0])</pre></div></li><li class='xr-var-item'><div class='xr-var-name'><span class='xr-has-index'>time</span></div><div class='xr-var-dims'>(time)</div><div class='xr-var-dtype'>datetime64[ns]</div><div class='xr-var-preview xr-preview'>2010-09-01 ... 2012-06-30T23:00:00</div><input id='attrs-6214d3e9-b5cd-4293-a286-ba5bd301c59a' class='xr-var-attrs-in' type='checkbox' disabled><label for='attrs-6214d3e9-b5cd-4293-a286-ba5bd301c59a' title='Show/Hide attributes'><svg class='icon xr-icon-file-text2'><use xlink:href='#icon-file-text2'></use></svg></label><input id='data-6a9dd47c-6469-4a73-b825-36100f9be47a' class='xr-var-data-in' type='checkbox'><label for='data-6a9dd47c-6469-4a73-b825-36100f9be47a' title='Show/Hide data repr'><svg class='icon xr-icon-database'><use xlink:href='#icon-database'></use></svg></label><div class='xr-var-attrs'><dl class='xr-attrs'></dl></div><div class='xr-var-data'><pre>array([&#x27;2010-09-01T00:00:00.000000000&#x27;, &#x27;2010-09-01T01:00:00.000000000&#x27;,
       &#x27;2010-09-01T02:00:00.000000000&#x27;, ..., &#x27;2012-06-30T21:00:00.000000000&#x27;,
       &#x27;2012-06-30T22:00:00.000000000&#x27;, &#x27;2012-06-30T23:00:00.000000000&#x27;],
      shape=(16056,), dtype=&#x27;datetime64[ns]&#x27;)</pre></div></li><li class='xr-var-item'><div class='xr-var-name'><span class='xr-has-index'>variable_identifiers</span></div><div class='xr-var-dims'>(variable_identifiers)</div><div class='xr-var-dtype'>object</div><div class='xr-var-preview xr-preview'>&#x27;node.2.OutflowRate&#x27;</div><input id='attrs-10543ea5-4fe0-4a88-ae04-9001066c7202' class='xr-var-attrs-in' type='checkbox' disabled><label for='attrs-10543ea5-4fe0-4a88-ae04-9001066c7202' title='Show/Hide attributes'><svg class='icon xr-icon-file-text2'><use xlink:href='#icon-file-text2'></use></svg></label><input id='data-a7c5718c-41b5-46c1-bf6c-2bdfd566bd7c' class='xr-var-data-in' type='checkbox'><label for='data-a7c5718c-41b5-46c1-bf6c-2bdfd566bd7c' title='Show/Hide data repr'><svg class='icon xr-icon-database'><use xlink:href='#icon-database'></use></svg></label><div class='xr-var-attrs'><dl class='xr-attrs'></dl></div><div class='xr-var-data'><pre>array([&#x27;node.2.OutflowRate&#x27;], dtype=object)</pre></div></li></ul></div></li><li class='xr-section-item'><input id='section-fc9e182d-6ff7-42c7-a750-8c3b3a8675ec' class='xr-section-summary-in' type='checkbox'  ><label for='section-fc9e182d-6ff7-42c7-a750-8c3b3a8675ec' class='xr-section-summary' >Indexes: <span>(3)</span></label><div class='xr-section-inline-details'></div><div class='xr-section-details'><ul class='xr-var-list'><li class='xr-var-item'><div class='xr-index-name'><div>ensemble</div></div><div class='xr-index-preview'>PandasIndex</div><div></div><input id='index-27b86edd-bb08-4557-b291-0e67b01f6c10' class='xr-index-data-in' type='checkbox'/><label for='index-27b86edd-bb08-4557-b291-0e67b01f6c10' title='Show/Hide index repr'><svg class='icon xr-icon-database'><use xlink:href='#icon-database'></use></svg></label><div class='xr-index-data'><pre>PandasIndex(Index([0], dtype=&#x27;int64&#x27;, name=&#x27;ensemble&#x27;))</pre></div></li><li class='xr-var-item'><div class='xr-index-name'><div>time</div></div><div class='xr-index-preview'>PandasIndex</div><div></div><input id='index-461720de-5446-419b-879b-ae3490600605' class='xr-index-data-in' type='checkbox'/><label for='index-461720de-5446-419b-879b-ae3490600605' title='Show/Hide index repr'><svg class='icon xr-icon-database'><use xlink:href='#icon-database'></use></svg></label><div class='xr-index-data'><pre>PandasIndex(DatetimeIndex([&#x27;2010-09-01 00:00:00&#x27;, &#x27;2010-09-01 01:00:00&#x27;,
               &#x27;2010-09-01 02:00:00&#x27;, &#x27;2010-09-01 03:00:00&#x27;,
               &#x27;2010-09-01 04:00:00&#x27;, &#x27;2010-09-01 05:00:00&#x27;,
               &#x27;2010-09-01 06:00:00&#x27;, &#x27;2010-09-01 07:00:00&#x27;,
               &#x27;2010-09-01 08:00:00&#x27;, &#x27;2010-09-01 09:00:00&#x27;,
               ...
               &#x27;2012-06-30 14:00:00&#x27;, &#x27;2012-06-30 15:00:00&#x27;,
               &#x27;2012-06-30 16:00:00&#x27;, &#x27;2012-06-30 17:00:00&#x27;,
               &#x27;2012-06-30 18:00:00&#x27;, &#x27;2012-06-30 19:00:00&#x27;,
               &#x27;2012-06-30 20:00:00&#x27;, &#x27;2012-06-30 21:00:00&#x27;,
               &#x27;2012-06-30 22:00:00&#x27;, &#x27;2012-06-30 23:00:00&#x27;],
              dtype=&#x27;datetime64[ns]&#x27;, name=&#x27;time&#x27;, length=16056, freq=&#x27;h&#x27;))</pre></div></li><li class='xr-var-item'><div class='xr-index-name'><div>variable_identifiers</div></div><div class='xr-index-preview'>PandasIndex</div><div></div><input id='index-197b1fc3-a54d-474b-8104-6c6adcae6431' class='xr-index-data-in' type='checkbox'/><label for='index-197b1fc3-a54d-474b-8104-6c6adcae6431' title='Show/Hide index repr'><svg class='icon xr-icon-database'><use xlink:href='#icon-database'></use></svg></label><div class='xr-index-data'><pre>PandasIndex(Index([&#x27;node.2.OutflowRate&#x27;], dtype=&#x27;object&#x27;, name=&#x27;variable_identifiers&#x27;))</pre></div></li></ul></div></li><li class='xr-section-item'><input id='section-3428d643-d7ae-417a-b3bd-31d50a2e54bc' class='xr-section-summary-in' type='checkbox' disabled ><label for='section-3428d643-d7ae-417a-b3bd-31d50a2e54bc' class='xr-section-summary'  title='Expand/collapse section'>Attributes: <span>(0)</span></label><div class='xr-section-inline-details'></div><div class='xr-section-details'><dl class='xr-attrs'></dl></div></li></ul></div></div>




```python
simulation.exec_simulation()
```


```python
simulation.get_recorded(mk_full_data_id(nodeId, 'reservoir.Storage'))
orate = simulation.get_recorded(mk_full_data_id(nodeId, 'reservoir.OutflowRate'))
irate = simulation.get_recorded(mk_full_data_id(nodeId, 'reservoir.InflowRate'))
```


```python
plot_two_series(irate, orate, 
                names=["inflow rate", "outflow rate"], 
                ylab='m3/s', 
                title=f"Inflow and Outflow rate at {nodeId}")
```


    
![png](reservoir_geometry_files/reservoir_geometry_49_0.png)
    



```python

```
