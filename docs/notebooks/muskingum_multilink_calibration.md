# Linear Muskingum channel routing model - constrained subcatchment calibration

## Purpose

This vignette focuses on explaining how to calibrate the linear version of Muskingum jointly across river reaches, respecting stability constraints across all these reaches. The second part of the document is an indepth explanation of the scheme that is also used as a reference for unit testing swift.


```python
from swift2.doc_helper import pkg_versions_info

print(pkg_versions_info("This document was generated from a jupyter notebook"))
```

    This document was generated from a jupyter notebook on 2025-03-27 17:26:28.496798
        swift2 2.5.1
        uchronia 2.6.2


## Guidelines for global calibration of Muskingum constrainted parameters


```python
import datetime as dt

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
```


```python
import seaborn as sns
```


```python
import swift2
import swift2.wrap.swift_wrap_custom as swc
```


```python
# Only temporary, under construction...
import swift2.wrap.swift_wrap_generated as swg
import xarray as xr
```


```python

```


```python
from cinterop.timeseries import (
    TIME_DIMNAME,
    pd_series_to_xr_series,
    slice_xr_time_series,
    xr_ts_end,
    xr_ts_start,
)
```


```python
from swift2.doc_helper import *
from swift2.parameteriser import *
from swift2.play_record import *
from swift2.simulation import *
from swift2.statistics import *
from swift2.system import *
from swift2.utils import *

# from swift2.prototypes import extract_optimisation_log
from uchronia.time_series import get_item
```


```python
%matplotlib inline
```

For this example we will use data derived from the South Esk catchment in Tasmania.

## Baseline model structure

We load and configure the model simulation in the next section, without detailed explanation; please read other introductory vignettes if this is unclear.


```python
model_id = 'GR4J'
site_id = 'South_Esk'
simulation = sample_catchment_model(site_id=site_id, config_id='catchment')
simulation = swap_model(simulation, 'MuskingumNonLinear', 'channel_routing')

# # revert back to derfautl values as expected from sample simulation..
# sc = 1 # reach slope in m/m
# n = 1  # default Manning's parameter value for the reach
# f = 1  # "Fudge factor" to allow for a different range of Alpha values. 
# oneHour = 1
# delt = oneHour

se_climate = sample_series(site_id=site_id, var_name='climate')
se_flows = sample_series(site_id=site_id, var_name='flow')

play_input(simulation, se_climate)
set_simulation_span(simulation, xr_ts_start(se_climate), xr_ts_end(se_climate))
set_simulation_time_step(simulation, 'hourly')
configure_hourly_gr4j(simulation)
```

We can get a topologic view of the model setup (albeit crowded as this is a fairly large catchment). 

(Note: may not render yet through GitHub)


```python
# TODO:
# from graphviz import Digraph
# DiagrammeR(GetCatchmentDOTGraph_R(simulation))
```

We cookie cut to get a subcatchment near the headwaters.


```python
from swift2.model_definitions import *

# from graphviz import Digraph

subsim = subset_catchment(simulation, 'node.5')
subsim
```




    Simulation wrapper for a CFFI pointer handle to a native pointer of type id "MODEL_SIMULATION_PTR"




```python
dot_graph = swg.GetCatchmentDOTGraph_py(subsim)
```

We configure the routing scheme to be linear (parameter N set and fixed to 1)


```python
link_ids = mk_full_data_id('link', get_link_ids(subsim))
set_state_value(subsim, mk_full_data_id(link_ids, 'N'), rep(1.0, len(link_ids)))
```

Let's have a look at the link properties and other default routing parameters


```python
lnkpnames = ['Length', 'f', 'ManningsN', 'Slope', 'N', 'X', 'Alpha']
get_state_value(subsim,mk_full_data_id('link.1', lnkpnames))
```




    {'link.1.Length': 6140.0,
     'link.1.f': 1.0,
     'link.1.ManningsN': 1.0,
     'link.1.Slope': 1.0,
     'link.1.N': 1.0,
     'link.1.X': 0.1,
     'link.1.Alpha': 1.0}



X is between 0 and 0.5, without stability constraints. Setting a default Alpha is... trickier.


```python
set_state_value(subsim, mk_full_data_id(link_ids, 'X'), rep(1e-6, len(link_ids)))
set_state_value(subsim, mk_full_data_id(link_ids, 'Alpha'), rep(0.0005, len(link_ids)))
```

If we look at the subcatchment outflow in this configuration, it is a series of unfeasible values - at least one link was in an unfeasible zone for (Alpha, X)


```python
from swift2.const import CATCHMENT_FLOWRATE_VARID

var_id = CATCHMENT_FLOWRATE_VARID
catOutflowId = 'subarea.1.OutflowRate'

record_state(subsim,var_id)
record_state(subsim,catOutflowId)

exec_simulation(subsim)
someFlow = get_recorded(subsim, var_id)
```


```python
someFlow.head()
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
</style><pre class='xr-text-repr-fallback'>&lt;xarray.DataArray (variable_identifiers: 1, ensemble: 1, time: 5)&gt; Size: 40B
array([[[0., 0., 0., 0., 0.]]])
Coordinates:
  * ensemble              (ensemble) int64 8B 0
  * time                  (time) datetime64[ns] 40B 2010-11-01 ... 2010-11-01...
  * variable_identifiers  (variable_identifiers) object 8B &#x27;Catchment.Streamf...</pre><div class='xr-wrap' style='display:none'><div class='xr-header'><div class='xr-obj-type'>xarray.DataArray</div><div class='xr-array-name'></div><ul class='xr-dim-list'><li><span class='xr-has-index'>variable_identifiers</span>: 1</li><li><span class='xr-has-index'>ensemble</span>: 1</li><li><span class='xr-has-index'>time</span>: 5</li></ul></div><ul class='xr-sections'><li class='xr-section-item'><div class='xr-array-wrap'><input id='section-1e4ace4e-2df6-4d8c-8703-8ed5f45c3df8' class='xr-array-in' type='checkbox' checked><label for='section-1e4ace4e-2df6-4d8c-8703-8ed5f45c3df8' title='Show/hide data repr'><svg class='icon xr-icon-database'><use xlink:href='#icon-database'></use></svg></label><div class='xr-array-preview xr-preview'><span>0.0 0.0 0.0 0.0 0.0</span></div><div class='xr-array-data'><pre>array([[[0., 0., 0., 0., 0.]]])</pre></div></div></li><li class='xr-section-item'><input id='section-65830689-5dda-456c-83da-c08a02e23bff' class='xr-section-summary-in' type='checkbox'  checked><label for='section-65830689-5dda-456c-83da-c08a02e23bff' class='xr-section-summary' >Coordinates: <span>(3)</span></label><div class='xr-section-inline-details'></div><div class='xr-section-details'><ul class='xr-var-list'><li class='xr-var-item'><div class='xr-var-name'><span class='xr-has-index'>ensemble</span></div><div class='xr-var-dims'>(ensemble)</div><div class='xr-var-dtype'>int64</div><div class='xr-var-preview xr-preview'>0</div><input id='attrs-d5b5e049-5ceb-414b-ae96-9c15eb45ddf1' class='xr-var-attrs-in' type='checkbox' disabled><label for='attrs-d5b5e049-5ceb-414b-ae96-9c15eb45ddf1' title='Show/Hide attributes'><svg class='icon xr-icon-file-text2'><use xlink:href='#icon-file-text2'></use></svg></label><input id='data-5827c4cc-a935-43eb-a1a8-006f1d87809e' class='xr-var-data-in' type='checkbox'><label for='data-5827c4cc-a935-43eb-a1a8-006f1d87809e' title='Show/Hide data repr'><svg class='icon xr-icon-database'><use xlink:href='#icon-database'></use></svg></label><div class='xr-var-attrs'><dl class='xr-attrs'></dl></div><div class='xr-var-data'><pre>array([0])</pre></div></li><li class='xr-var-item'><div class='xr-var-name'><span class='xr-has-index'>time</span></div><div class='xr-var-dims'>(time)</div><div class='xr-var-dtype'>datetime64[ns]</div><div class='xr-var-preview xr-preview'>2010-11-01 ... 2010-11-01T04:00:00</div><input id='attrs-f43766ec-0eaa-45e5-a6ef-1e55b5bda5aa' class='xr-var-attrs-in' type='checkbox' disabled><label for='attrs-f43766ec-0eaa-45e5-a6ef-1e55b5bda5aa' title='Show/Hide attributes'><svg class='icon xr-icon-file-text2'><use xlink:href='#icon-file-text2'></use></svg></label><input id='data-410d8ce2-a3d1-4682-b769-0de888ee23bc' class='xr-var-data-in' type='checkbox'><label for='data-410d8ce2-a3d1-4682-b769-0de888ee23bc' title='Show/Hide data repr'><svg class='icon xr-icon-database'><use xlink:href='#icon-database'></use></svg></label><div class='xr-var-attrs'><dl class='xr-attrs'></dl></div><div class='xr-var-data'><pre>array([&#x27;2010-11-01T00:00:00.000000000&#x27;, &#x27;2010-11-01T01:00:00.000000000&#x27;,
       &#x27;2010-11-01T02:00:00.000000000&#x27;, &#x27;2010-11-01T03:00:00.000000000&#x27;,
       &#x27;2010-11-01T04:00:00.000000000&#x27;], dtype=&#x27;datetime64[ns]&#x27;)</pre></div></li><li class='xr-var-item'><div class='xr-var-name'><span class='xr-has-index'>variable_identifiers</span></div><div class='xr-var-dims'>(variable_identifiers)</div><div class='xr-var-dtype'>object</div><div class='xr-var-preview xr-preview'>&#x27;Catchment.StreamflowRate&#x27;</div><input id='attrs-a6c927f4-af76-4ff9-86b1-3a9943bd0bab' class='xr-var-attrs-in' type='checkbox' disabled><label for='attrs-a6c927f4-af76-4ff9-86b1-3a9943bd0bab' title='Show/Hide attributes'><svg class='icon xr-icon-file-text2'><use xlink:href='#icon-file-text2'></use></svg></label><input id='data-fa38fa07-bc76-4dc9-b924-3c5fa6a2fab6' class='xr-var-data-in' type='checkbox'><label for='data-fa38fa07-bc76-4dc9-b924-3c5fa6a2fab6' title='Show/Hide data repr'><svg class='icon xr-icon-database'><use xlink:href='#icon-database'></use></svg></label><div class='xr-var-attrs'><dl class='xr-attrs'></dl></div><div class='xr-var-data'><pre>array([&#x27;Catchment.StreamflowRate&#x27;], dtype=object)</pre></div></li></ul></div></li><li class='xr-section-item'><input id='section-2291029e-2168-43d3-84e4-a365a2a60114' class='xr-section-summary-in' type='checkbox'  ><label for='section-2291029e-2168-43d3-84e4-a365a2a60114' class='xr-section-summary' >Indexes: <span>(3)</span></label><div class='xr-section-inline-details'></div><div class='xr-section-details'><ul class='xr-var-list'><li class='xr-var-item'><div class='xr-index-name'><div>ensemble</div></div><div class='xr-index-preview'>PandasIndex</div><div></div><input id='index-ee71d484-f942-4d8d-8c9d-38e2597666b7' class='xr-index-data-in' type='checkbox'/><label for='index-ee71d484-f942-4d8d-8c9d-38e2597666b7' title='Show/Hide index repr'><svg class='icon xr-icon-database'><use xlink:href='#icon-database'></use></svg></label><div class='xr-index-data'><pre>PandasIndex(Index([0], dtype=&#x27;int64&#x27;, name=&#x27;ensemble&#x27;))</pre></div></li><li class='xr-var-item'><div class='xr-index-name'><div>time</div></div><div class='xr-index-preview'>PandasIndex</div><div></div><input id='index-210921a0-1ca3-4deb-9cbd-4299eabafcb3' class='xr-index-data-in' type='checkbox'/><label for='index-210921a0-1ca3-4deb-9cbd-4299eabafcb3' title='Show/Hide index repr'><svg class='icon xr-icon-database'><use xlink:href='#icon-database'></use></svg></label><div class='xr-index-data'><pre>PandasIndex(DatetimeIndex([&#x27;2010-11-01 00:00:00&#x27;, &#x27;2010-11-01 01:00:00&#x27;,
               &#x27;2010-11-01 02:00:00&#x27;, &#x27;2010-11-01 03:00:00&#x27;,
               &#x27;2010-11-01 04:00:00&#x27;],
              dtype=&#x27;datetime64[ns]&#x27;, name=&#x27;time&#x27;, freq=&#x27;h&#x27;))</pre></div></li><li class='xr-var-item'><div class='xr-index-name'><div>variable_identifiers</div></div><div class='xr-index-preview'>PandasIndex</div><div></div><input id='index-b3799b9f-c603-4364-ad48-877fb857d703' class='xr-index-data-in' type='checkbox'/><label for='index-b3799b9f-c603-4364-ad48-877fb857d703' title='Show/Hide index repr'><svg class='icon xr-icon-database'><use xlink:href='#icon-database'></use></svg></label><div class='xr-index-data'><pre>PandasIndex(Index([&#x27;Catchment.StreamflowRate&#x27;], dtype=&#x27;object&#x27;, name=&#x27;variable_identifiers&#x27;))</pre></div></li></ul></div></li><li class='xr-section-item'><input id='section-1bdcc868-12a6-4c51-848e-7d2415f1b18d' class='xr-section-summary-in' type='checkbox' disabled ><label for='section-1bdcc868-12a6-4c51-848e-7d2415f1b18d' class='xr-section-summary'  title='Expand/collapse section'>Attributes: <span>(0)</span></label><div class='xr-section-inline-details'></div><div class='xr-section-details'><dl class='xr-attrs'></dl></div></li></ul></div></div>



We can double-check that the subarea does produce runoff yield; the links are where the model does not work yet.


```python
get_state_value(subsim, get_variable_ids(subsim, 'node.5'))
```




    {'node.5.InflowRate': 7.942047038196456e-05,
     'node.5.InflowVolume': 0.28591369337507244,
     'node.5.AdditionalInflowRate': 0.0,
     'node.5.OutflowRate': 7.942047038196456e-05,
     'node.5.OutflowVolume': 0.28591369337507244}




```python
get_recorded(subsim, catOutflowId).head()
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
</style><pre class='xr-text-repr-fallback'>&lt;xarray.DataArray (variable_identifiers: 1, ensemble: 1, time: 5)&gt; Size: 40B
array([[[0., 0., 0., 0., 0.]]])
Coordinates:
  * ensemble              (ensemble) int64 8B 0
  * time                  (time) datetime64[ns] 40B 2010-11-01 ... 2010-11-01...
  * variable_identifiers  (variable_identifiers) object 8B &#x27;subarea.1.Outflow...</pre><div class='xr-wrap' style='display:none'><div class='xr-header'><div class='xr-obj-type'>xarray.DataArray</div><div class='xr-array-name'></div><ul class='xr-dim-list'><li><span class='xr-has-index'>variable_identifiers</span>: 1</li><li><span class='xr-has-index'>ensemble</span>: 1</li><li><span class='xr-has-index'>time</span>: 5</li></ul></div><ul class='xr-sections'><li class='xr-section-item'><div class='xr-array-wrap'><input id='section-51a5ed4d-7d75-4d77-8457-73574a8274af' class='xr-array-in' type='checkbox' checked><label for='section-51a5ed4d-7d75-4d77-8457-73574a8274af' title='Show/hide data repr'><svg class='icon xr-icon-database'><use xlink:href='#icon-database'></use></svg></label><div class='xr-array-preview xr-preview'><span>0.0 0.0 0.0 0.0 0.0</span></div><div class='xr-array-data'><pre>array([[[0., 0., 0., 0., 0.]]])</pre></div></div></li><li class='xr-section-item'><input id='section-2fde3415-c86f-4c29-a61d-1a740d5992cd' class='xr-section-summary-in' type='checkbox'  checked><label for='section-2fde3415-c86f-4c29-a61d-1a740d5992cd' class='xr-section-summary' >Coordinates: <span>(3)</span></label><div class='xr-section-inline-details'></div><div class='xr-section-details'><ul class='xr-var-list'><li class='xr-var-item'><div class='xr-var-name'><span class='xr-has-index'>ensemble</span></div><div class='xr-var-dims'>(ensemble)</div><div class='xr-var-dtype'>int64</div><div class='xr-var-preview xr-preview'>0</div><input id='attrs-0b09a438-4840-404b-883a-0bd56adfe34c' class='xr-var-attrs-in' type='checkbox' disabled><label for='attrs-0b09a438-4840-404b-883a-0bd56adfe34c' title='Show/Hide attributes'><svg class='icon xr-icon-file-text2'><use xlink:href='#icon-file-text2'></use></svg></label><input id='data-54e4d0cb-1b7b-4210-9aa4-b3a20f63466e' class='xr-var-data-in' type='checkbox'><label for='data-54e4d0cb-1b7b-4210-9aa4-b3a20f63466e' title='Show/Hide data repr'><svg class='icon xr-icon-database'><use xlink:href='#icon-database'></use></svg></label><div class='xr-var-attrs'><dl class='xr-attrs'></dl></div><div class='xr-var-data'><pre>array([0])</pre></div></li><li class='xr-var-item'><div class='xr-var-name'><span class='xr-has-index'>time</span></div><div class='xr-var-dims'>(time)</div><div class='xr-var-dtype'>datetime64[ns]</div><div class='xr-var-preview xr-preview'>2010-11-01 ... 2010-11-01T04:00:00</div><input id='attrs-c0c76511-b8ac-4a9f-8e07-ca85e6c3746d' class='xr-var-attrs-in' type='checkbox' disabled><label for='attrs-c0c76511-b8ac-4a9f-8e07-ca85e6c3746d' title='Show/Hide attributes'><svg class='icon xr-icon-file-text2'><use xlink:href='#icon-file-text2'></use></svg></label><input id='data-9153c586-f68f-4b8d-8974-2447d5bc776c' class='xr-var-data-in' type='checkbox'><label for='data-9153c586-f68f-4b8d-8974-2447d5bc776c' title='Show/Hide data repr'><svg class='icon xr-icon-database'><use xlink:href='#icon-database'></use></svg></label><div class='xr-var-attrs'><dl class='xr-attrs'></dl></div><div class='xr-var-data'><pre>array([&#x27;2010-11-01T00:00:00.000000000&#x27;, &#x27;2010-11-01T01:00:00.000000000&#x27;,
       &#x27;2010-11-01T02:00:00.000000000&#x27;, &#x27;2010-11-01T03:00:00.000000000&#x27;,
       &#x27;2010-11-01T04:00:00.000000000&#x27;], dtype=&#x27;datetime64[ns]&#x27;)</pre></div></li><li class='xr-var-item'><div class='xr-var-name'><span class='xr-has-index'>variable_identifiers</span></div><div class='xr-var-dims'>(variable_identifiers)</div><div class='xr-var-dtype'>object</div><div class='xr-var-preview xr-preview'>&#x27;subarea.1.OutflowRate&#x27;</div><input id='attrs-fd400c39-c35e-416b-8b78-d8590cd845dc' class='xr-var-attrs-in' type='checkbox' disabled><label for='attrs-fd400c39-c35e-416b-8b78-d8590cd845dc' title='Show/Hide attributes'><svg class='icon xr-icon-file-text2'><use xlink:href='#icon-file-text2'></use></svg></label><input id='data-5a97d751-6885-408e-90ba-b4b8839448cc' class='xr-var-data-in' type='checkbox'><label for='data-5a97d751-6885-408e-90ba-b4b8839448cc' title='Show/Hide data repr'><svg class='icon xr-icon-database'><use xlink:href='#icon-database'></use></svg></label><div class='xr-var-attrs'><dl class='xr-attrs'></dl></div><div class='xr-var-data'><pre>array([&#x27;subarea.1.OutflowRate&#x27;], dtype=object)</pre></div></li></ul></div></li><li class='xr-section-item'><input id='section-db07318b-6cf8-48b9-909c-11dd1c7ed582' class='xr-section-summary-in' type='checkbox'  ><label for='section-db07318b-6cf8-48b9-909c-11dd1c7ed582' class='xr-section-summary' >Indexes: <span>(3)</span></label><div class='xr-section-inline-details'></div><div class='xr-section-details'><ul class='xr-var-list'><li class='xr-var-item'><div class='xr-index-name'><div>ensemble</div></div><div class='xr-index-preview'>PandasIndex</div><div></div><input id='index-35db44e9-88c1-4e3f-981b-9b0f97d1733b' class='xr-index-data-in' type='checkbox'/><label for='index-35db44e9-88c1-4e3f-981b-9b0f97d1733b' title='Show/Hide index repr'><svg class='icon xr-icon-database'><use xlink:href='#icon-database'></use></svg></label><div class='xr-index-data'><pre>PandasIndex(Index([0], dtype=&#x27;int64&#x27;, name=&#x27;ensemble&#x27;))</pre></div></li><li class='xr-var-item'><div class='xr-index-name'><div>time</div></div><div class='xr-index-preview'>PandasIndex</div><div></div><input id='index-19498056-636a-486a-8342-dca08de36d6c' class='xr-index-data-in' type='checkbox'/><label for='index-19498056-636a-486a-8342-dca08de36d6c' title='Show/Hide index repr'><svg class='icon xr-icon-database'><use xlink:href='#icon-database'></use></svg></label><div class='xr-index-data'><pre>PandasIndex(DatetimeIndex([&#x27;2010-11-01 00:00:00&#x27;, &#x27;2010-11-01 01:00:00&#x27;,
               &#x27;2010-11-01 02:00:00&#x27;, &#x27;2010-11-01 03:00:00&#x27;,
               &#x27;2010-11-01 04:00:00&#x27;],
              dtype=&#x27;datetime64[ns]&#x27;, name=&#x27;time&#x27;, freq=&#x27;h&#x27;))</pre></div></li><li class='xr-var-item'><div class='xr-index-name'><div>variable_identifiers</div></div><div class='xr-index-preview'>PandasIndex</div><div></div><input id='index-34073ef3-d4fd-4ce2-8aea-0b90b82b7ac6' class='xr-index-data-in' type='checkbox'/><label for='index-34073ef3-d4fd-4ce2-8aea-0b90b82b7ac6' title='Show/Hide index repr'><svg class='icon xr-icon-database'><use xlink:href='#icon-database'></use></svg></label><div class='xr-index-data'><pre>PandasIndex(Index([&#x27;subarea.1.OutflowRate&#x27;], dtype=&#x27;object&#x27;, name=&#x27;variable_identifiers&#x27;))</pre></div></li></ul></div></li><li class='xr-section-item'><input id='section-6758b286-de7e-4875-99cb-a5bc5f93616c' class='xr-section-summary-in' type='checkbox' disabled ><label for='section-6758b286-de7e-4875-99cb-a5bc5f93616c' class='xr-section-summary'  title='Expand/collapse section'>Attributes: <span>(0)</span></label><div class='xr-section-inline-details'></div><div class='xr-section-details'><dl class='xr-attrs'></dl></div></li></ul></div></div>



So, given that each routing link parameters Alpha and X are subject to constraint that vary depending on 'Length', 'f', 'ManningsN', 'Slope', how do we get a pair (Alpha, X) that globaly respect these constraints? This is not complex science but complicated enough to get wrong.

'swift' offers facilities to remove the error prone tedium. First, `feasibleMuskingumBounds` lists the extremas of the feasible (Alpha, X) parameter space.


```python
akbounds = feasible_muskingum_bounds(subsim, 1)
akbounds
```




    {'min_alpha': np.float64(0.08143322475570032),
     'max_x': np.float64(0.37382039573820397),
     'alpha_for_max_x': np.float64(0.13004771187286124)}



The numbers above can play a *crucial* role when setting up an optimiser for this model; more on this soon.


```python

oneHour = 1

pSpecMusk = pd.DataFrame(dict(Name = ['X', 'Alpha'],
  Value = [akbounds['max_x'] / 2, akbounds['alpha_for_max_x']],
  Min= [1.0E-06, akbounds['min_alpha']],   
  Max = [akbounds['max_x'], 1e5]) 
)

# Basic parameteriser
def pzm(simulation, pSpecs=pSpecMusk):
    akbounds = feasible_muskingum_bounds(simulation, 1)
    p_musk = create_parameteriser('generic links',pSpecs)
    return p_musk

# Wrapper parameteriser, with constraints added around.
def pzc(simulation, pSpecs=pSpecMusk):
    p_musk = pzm(simulation, pSpecs)
    p_musk_c = create_muskingum_param_constraints(p_musk, oneHour, "Alpha", "X", simulation)
    return p_musk_c


pp = parameteriser_as_dataframe
```


```python
pp(pzm(subsim))
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
      <td>X</td>
      <td>0.186910</td>
      <td>0.000001</td>
      <td>0.37382</td>
    </tr>
    <tr>
      <th>1</th>
      <td>Alpha</td>
      <td>0.130048</td>
      <td>0.081433</td>
      <td>100000.00000</td>
    </tr>
  </tbody>
</table>
</div>




```python
p = pzc(subsim)
pp(p)
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
      <td>X</td>
      <td>0.186910</td>
      <td>0.000001</td>
      <td>0.373820</td>
    </tr>
    <tr>
      <th>1</th>
      <td>Alpha</td>
      <td>0.130048</td>
      <td>0.100153</td>
      <td>0.260095</td>
    </tr>
  </tbody>
</table>
</div>



Let's get a trace of the subcatchment outflow, as a synthetic data to calibrated against.


```python
apply_sys_config(p, subsim)
exec_simulation(subsim)
someFlow = get_recorded(subsim, var_id)
```


```python
someFlow.to_series().describe()
```




    count    4.800000e+02
    mean     6.164971e-03
    std      2.694368e-02
    min      0.000000e+00
    25%      8.691205e-07
    50%      8.687524e-05
    75%      6.349944e-04
    max      2.682614e-01
    dtype: float64



We do now get a valid outflow since (Alpha-K) respects feasibility constraints on all links.


```python
someFlow.plot();
```


    
![png](muskingum_multilink_calibration_files/muskingum_multilink_calibration_40_0.png)
    


## Setting up calibration


```python
def c(*args):
    return np.array([x for x in args])

pSpecMaxBounds = pd.DataFrame(dict(
  Name =  c('X',     'Alpha'),
  Value = c(1.0E-6, akbounds['alpha_for_max_x']), # IMPORTANT to use these values.
  Min=    c(1.0E-6, akbounds['min_alpha']),   
  Max =   c(akbounds['max_x'], 1e6), # Alpha_max can get very large. 
)
                             )
pp(pzc(subsim, pSpecMaxBounds))
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
      <td>X</td>
      <td>0.000001</td>
      <td>0.000001</td>
      <td>0.373820</td>
    </tr>
    <tr>
      <th>1</th>
      <td>Alpha</td>
      <td>0.130048</td>
      <td>0.081433</td>
      <td>48614.487117</td>
    </tr>
  </tbody>
</table>
</div>



If we were to use another (X, Alpha) point e.g. X=0.1869102, the feasible bounds for Alpha change drastically. If an optimiser samples this for an initial population of points (SCE), this is unnecessarily restrictive for Alpha. Many hydrological calibration schemes were designed without consideration on feasible space that are not hypercubes.


```python
pp(pzc(subsim, pSpecMusk))
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
      <td>X</td>
      <td>0.186910</td>
      <td>0.000001</td>
      <td>0.373820</td>
    </tr>
    <tr>
      <th>1</th>
      <td>Alpha</td>
      <td>0.130048</td>
      <td>0.100153</td>
      <td>0.260095</td>
    </tr>
  </tbody>
</table>
</div>



While calibrating in the (Alpha,X) space is possible, perhaps preferable in some cases, (1/Alpha,X) has a triangular shaped feasibility region that may be easier to handle for optimisers that work with geometric transformation in the parameter space (SCE). Swift can add this on top of the constrained calibration:


```python
# (X, 1/Alpha) parametrizer with dynamically constrained min/max bounds.
def pzer_inv(simulation, pSpecs=pSpecMusk):
    p_musk_c = pzc(simulation, pSpecs)
    p_musk_inv_a = wrap_transform(p_musk_c)
    add_transform(p_musk_inv_a, 'inv_alpha', 'Alpha', '1/x')
    return p_musk_inv_a

p = pzer_inv(subsim, pSpecMaxBounds)
pp(p)
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
      <td>inv_alpha</td>
      <td>7.689486</td>
      <td>0.000021</td>
      <td>12.279988</td>
    </tr>
    <tr>
      <th>1</th>
      <td>X</td>
      <td>0.000001</td>
      <td>0.000001</td>
      <td>0.373820</td>
    </tr>
  </tbody>
</table>
</div>



We check that backtransforming to (Alpha-X) works:


```python
pp(backtransform(p))
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
      <td>X</td>
      <td>0.000001</td>
      <td>0.000001</td>
      <td>0.373820</td>
    </tr>
    <tr>
      <th>1</th>
      <td>Alpha</td>
      <td>0.130048</td>
      <td>0.081433</td>
      <td>48614.487117</td>
    </tr>
  </tbody>
</table>
</div>




```python
someFlow = someFlow.squeeze()
```


```python
objectiveId = 'NSE'
objective = create_objective(subsim, var_id, someFlow, objectiveId, xr_ts_start(someFlow), xr_ts_end(someFlow))
```


```python
score = get_score(objective,p)  
score
```




    {'scores': {'NSE': 0.9997748469565144},
     'sysconfig':         Name     Value       Min        Max
     0  inv_alpha  7.689486  0.000021  12.279988
     1          X  0.000001  0.000001   0.373820}




```python
#termination = swift::CreateSceMaxRuntimeTerminationWila_R(1/60)
termination = create_sce_termination_wila('relative standard deviation', c('0.001','0.0167'))
npars = 2
sce_params = sce_parameter(npars)
optimiser = create_sce_optim_swift(objective,termination_criterion = termination, population_initialiser = p,sce_params = sce_params)
calib_logger = set_calibration_logger(optimiser,"dummy")
```


```python
%%time
calib_results = execute_optimisation(optimiser)
```

    CPU times: user 999 ms, sys: 4.36 ms, total: 1 s
    Wall time: 324 ms



```python
opt_log = optimiser.extract_optimisation_log(fitness_name = "NSE")
```


```python
from swift2.vis import OptimisationPlots

shuffleLogs = opt_log.subset_by_message(pattern = "Initial.*|Shuffling.*") 
shuffleLogs.data
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
      <th>Category</th>
      <th>CurrentShuffle</th>
      <th>Message</th>
      <th>NSE</th>
      <th>X</th>
      <th>inv_alpha</th>
      <th>PointNumber</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>Initial Population</td>
      <td></td>
      <td>Initial Population</td>
      <td>0.999286</td>
      <td>0.330241</td>
      <td>11.636989</td>
      <td>1</td>
    </tr>
    <tr>
      <th>1</th>
      <td>Initial Population</td>
      <td></td>
      <td>Initial Population</td>
      <td>0.979734</td>
      <td>0.251643</td>
      <td>0.752518</td>
      <td>2</td>
    </tr>
    <tr>
      <th>2</th>
      <td>Initial Population</td>
      <td></td>
      <td>Initial Population</td>
      <td>0.993863</td>
      <td>0.141551</td>
      <td>2.133362</td>
      <td>3</td>
    </tr>
    <tr>
      <th>3</th>
      <td>Initial Population</td>
      <td></td>
      <td>Initial Population</td>
      <td>0.999939</td>
      <td>0.149201</td>
      <td>8.721001</td>
      <td>4</td>
    </tr>
    <tr>
      <th>4</th>
      <td>Initial Population</td>
      <td></td>
      <td>Initial Population</td>
      <td>0.995707</td>
      <td>0.142863</td>
      <td>2.626987</td>
      <td>5</td>
    </tr>
    <tr>
      <th>...</th>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
    </tr>
    <tr>
      <th>1117</th>
      <td>Shuffling No 6</td>
      <td></td>
      <td>Shuffling No 6</td>
      <td>1.000000</td>
      <td>0.186814</td>
      <td>7.690154</td>
      <td>1118</td>
    </tr>
    <tr>
      <th>1118</th>
      <td>Shuffling No 6</td>
      <td></td>
      <td>Shuffling No 6</td>
      <td>1.000000</td>
      <td>0.186973</td>
      <td>7.686830</td>
      <td>1119</td>
    </tr>
    <tr>
      <th>1119</th>
      <td>Shuffling No 6</td>
      <td></td>
      <td>Shuffling No 6</td>
      <td>1.000000</td>
      <td>0.186925</td>
      <td>7.690300</td>
      <td>1120</td>
    </tr>
    <tr>
      <th>1120</th>
      <td>Shuffling No 6</td>
      <td></td>
      <td>Shuffling No 6</td>
      <td>1.000000</td>
      <td>0.187077</td>
      <td>7.691259</td>
      <td>1121</td>
    </tr>
    <tr>
      <th>1121</th>
      <td>Shuffling No 6</td>
      <td></td>
      <td>Shuffling No 6</td>
      <td>1.000000</td>
      <td>0.186800</td>
      <td>7.694139</td>
      <td>1122</td>
    </tr>
  </tbody>
</table>
<p>140 rows × 7 columns</p>
</div>




```python
v = OptimisationPlots(shuffleLogs)
g = v.shuffles('X', 'inv_alpha', obj_lims = [0.0,1.0])
plt.gcf().set_size_inches(10,8)
```


    
![png](muskingum_multilink_calibration_files/muskingum_multilink_calibration_56_0.png)
    



```python
sortedResults = sort_by_score(calib_results, 'NSE')
scores_as_dataframe(sortedResults).head()
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
      <th>inv_alpha</th>
      <th>X</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>1.0</td>
      <td>7.689032</td>
      <td>0.186874</td>
    </tr>
    <tr>
      <th>1</th>
      <td>1.0</td>
      <td>7.690300</td>
      <td>0.186925</td>
    </tr>
    <tr>
      <th>2</th>
      <td>1.0</td>
      <td>7.690382</td>
      <td>0.186887</td>
    </tr>
    <tr>
      <th>3</th>
      <td>1.0</td>
      <td>7.690224</td>
      <td>0.186842</td>
    </tr>
    <tr>
      <th>4</th>
      <td>1.0</td>
      <td>7.689243</td>
      <td>0.186813</td>
    </tr>
  </tbody>
</table>
</div>




```python
q = get_best_score(calib_results, 'NSE', False)
q = swg.GetSystemConfigurationWila_py(q)
pp(q)
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
      <td>inv_alpha</td>
      <td>7.689032</td>
      <td>3.844007</td>
      <td>9.985182</td>
    </tr>
    <tr>
      <th>1</th>
      <td>X</td>
      <td>0.186874</td>
      <td>0.000001</td>
      <td>0.373798</td>
    </tr>
  </tbody>
</table>
</div>




```python
pp(backtransform(q))
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
      <td>X</td>
      <td>0.186874</td>
      <td>0.000001</td>
      <td>0.373798</td>
    </tr>
    <tr>
      <th>1</th>
      <td>Alpha</td>
      <td>0.130055</td>
      <td>0.100148</td>
      <td>0.260145</td>
    </tr>
  </tbody>
</table>
</div>



## Seeding the optimisation point population with restrictive constraint bounds

This section is a *counter-example*. Do not do this.

Say, instead of seeding with alpha set to alpha_for_x_max (0.37382040) we instead use a value close to its global minimum, 0.083:


```python
pSpecRestrictiveBounds = pSpecMaxBounds

pSpecRestrictiveBounds.loc[pSpecRestrictiveBounds.Name == 'Alpha', 'Value'] = 0.083
```


```python
pSpecRestrictiveBounds
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
      <td>X</td>
      <td>0.000001</td>
      <td>0.000001</td>
      <td>0.37382</td>
    </tr>
    <tr>
      <th>1</th>
      <td>Alpha</td>
      <td>0.083000</td>
      <td>0.081433</td>
      <td>1000000.00000</td>
    </tr>
  </tbody>
</table>
</div>




```python
p = pzer_inv(subsim, pSpecRestrictiveBounds)
pp(p)
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
      <td>inv_alpha</td>
      <td>12.048193</td>
      <td>0.000021</td>
      <td>12.279988</td>
    </tr>
    <tr>
      <th>1</th>
      <td>X</td>
      <td>0.000001</td>
      <td>0.000001</td>
      <td>0.018877</td>
    </tr>
  </tbody>
</table>
</div>



X is now much more constrained in its feasible range, and initializing a population fails to cover large sections of the feasible triangle. If used in the optimiser (uniform random sampling)



```python
termination = create_sce_termination_wila('relative standard deviation', c('0.001','0.0167'))
sce_params = get_default_sce_parameters()
npars = 2
sce_params = sce_parameter(npars)
optimiser = create_sce_optim_swift(objective,termination_criterion = termination, population_initialiser = p,sce_params = sce_params)
calib_logger = set_calibration_logger(optimiser,"dummy")
calib_results = execute_optimisation(optimiser)
```


```python
opt_log = extract_optimisation_log(optimiser, fitness_name = "NSE")
```


```python
shuffleLogs = opt_log.subset_by_message(pattern = "Initial.*|Shuffling.*") 
```


```python
v = OptimisationPlots(shuffleLogs)
g = v.shuffles('X', 'inv_alpha', obj_lims = [0.0,1.0])
plt.gcf().set_size_inches(10,8)
```


    
![png](muskingum_multilink_calibration_files/muskingum_multilink_calibration_68_0.png)
    



```python
# shuffleLogs = mhplot::subsetByCategory(opt_log$data, pattern = "Initial.*|Shuffling.*") 
# mhplot::plotShuffles(shuffleLogs, 'X', 'inv_alpha', obj_lims = (0:1))
```

SCE does manage to converge towards the optimum, but it takes a larger number of iterations. Anecdotally, we observed cases where the calibration does fail to go near the optimum, when interplaying with a convergence criterion configured for "leniency".

# Detailed explanation and unit test design

See other document [muskingum_multilink_calibration_explanation.ipynb](./muskingum_multilink_calibration_explanation.ipynb)

