# Ensemble SWIFT model runs

## About this document



```python
from swift2.doc_helper import pkg_versions_info

print(pkg_versions_info("This document was generated from a jupyter notebook"))
```

    This document was generated from a jupyter notebook on 2025-03-27 17:23:03.954002
        swift2 2.5.1
        uchronia 2.6.2


## Imports


```python
import os

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

import swift2.doc_helper as std
import swift2.parameteriser as sp
import swift2.play_record as spr
import uchronia.sample_data as usd
import xarray as xr

from swift2.const import CATCHMENT_FLOWRATE_VARID
from swift2.simulation import get_subarea_ids
from swift2.utils import mk_full_data_id, paste0
from uchronia.data_set import datasets_summaries, get_dataset_ids
```


```python
%matplotlib inline
```

## Synthetic catchment

Let's create a test catchment with a few subareas. Since we will work in a simulation mode, not calibration, we can afford a fairly arbitrary structure. 

A catchment structure can be captured with a set of items about subareas, links and nodes, and the connectivity of links and nodes


```python
runoff_model='GR4J'
```


```python
node_ids=paste0('n', [i+1 for i in range(6)])
link_ids = paste0('lnk', [i+1 for i in range(5)])
node_names = paste0(node_ids, '_name')
link_names = paste0(link_ids, '_name')
from_node = paste0('n', [2,5,4,3,1])
to_node = paste0('n', [6,2,2,4,4])
areas_km2 = np.array([1.2, 2.3, 4.4, 2.2, 1.5])
```


```python
simulation = std.create_catchment(node_ids, node_names, link_ids, link_names, from_node, to_node, runoff_model, areas_km2)
```


```python
simulation.describe()
```




    {'subareas': {'lnk1': 'lnk1_name',
      'lnk2': 'lnk2_name',
      'lnk3': 'lnk3_name',
      'lnk4': 'lnk4_name',
      'lnk5': 'lnk5_name'},
     'nodes': {'n1': 'n1_name',
      'n2': 'n2_name',
      'n3': 'n3_name',
      'n4': 'n4_name',
      'n5': 'n5_name',
      'n6': 'n6_name'},
     'links': {'lnk1': 'lnk1_name',
      'lnk2': 'lnk2_name',
      'lnk3': 'lnk3_name',
      'lnk4': 'lnk4_name',
      'lnk5': 'lnk5_name'}}



## Input data management

Working with ensemble time series is complicated.

The package `uchronia` includes facilities to access time series from a "library", akin to what you would do to manage books. This hides a lot of the lower level code for reading and writing file. To an extent, the python package `xarray` overlaps with the features of these `uchronia` data libraries, but do not fully supersede them.

Let's load a predefined data library with data for the Upper Murray river.


```python
if not 'SWIFT_TEST_DIR' in os.environ:
    os.environ['SWIFT_TEST_DIR'] = os.path.expanduser('~/data/documentation') 
```


```python
doc_data_path = usd.sample_data_dir()
data_path = os.path.join(doc_data_path, 'UpperMurray')
```


```python
data_library = usd.sample_time_series_library('upper murray')
```


```python
data_library
```




    CFFI pointer handle to a native pointer of type id "ENSEMBLE_DATA_SET_PTR"




```python
data_ids = data_library.get_dataset_ids()
data_ids
```




    ['pet_fcast_ens', 'pet_obs', 'rain_obs', 'rain_fcast_ens']




```python
data_library.datasets_summaries()
```




    {'pet_fcast_ens': 'variable name: pet_der, identifier: 1, start: 1989-12-31T00:00:00, end: 2012-12-30T00:00:00, time length: 8401, time step: daily',
     'pet_obs': 'variable name: pet_der, identifier: 1, start: 1988-12-31T00:00:00, end: 2012-12-30T00:00:00, time length: 8766, time step: daily',
     'rain_obs': 'variable name: rain_der, identifier: 1, start: 1989-12-31T13:00:00, end: 2012-10-31T12:00:00, time length: 200160, time step: hourly',
     'rain_fcast_ens': 'variable name: rain_fcast_ens, identifier: 1, index: 0, start: 2010-08-01T21:00:00, end: 2010-08-06T21:00:00, time length: 5, time step: <not yet supported>'}



The sample catchment structure is obviously not the real "Upper Murray". For the sake of a didactic example, let's set the same inputs across all the subareas.


```python
rain_obs = data_library.get_dataset('rain_obs').to_xarray()
```


```python
print(rain_obs)
```

    <xarray.DataArray (ensemble: 1, time: 200160)> Size: 2MB
    array([[-9999., -9999., -9999., ..., -9999., -9999., -9999.]],
          shape=(1, 200160))
    Coordinates:
      * ensemble  (ensemble) int64 8B 0
      * time      (time) datetime64[ns] 2MB 1989-12-31T14:00:00 ... 2012-10-31T13...



```python
rain_obs = rain_obs.where(rain_obs >= 0)
```


```python
rain_obs.time[:-10].values
```




    array(['1989-12-31T14:00:00.000000000', '1989-12-31T15:00:00.000000000',
           '1989-12-31T16:00:00.000000000', ...,
           '2012-10-31T01:00:00.000000000', '2012-10-31T02:00:00.000000000',
           '2012-10-31T03:00:00.000000000'],
          shape=(200150,), dtype='datetime64[ns]')



Note that the rainfall is hourly, but the pet is daily. This will matter later for the simulation


```python
pet_obs = data_library.get_dataset('pet_obs').to_xarray()
pet_obs.time[:-10]
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
</style><pre class='xr-text-repr-fallback'>&lt;xarray.DataArray &#x27;time&#x27; (time: 8756)&gt; Size: 70kB
array([&#x27;1989-01-01T00:00:00.000000000&#x27;, &#x27;1989-01-02T00:00:00.000000000&#x27;,
       &#x27;1989-01-03T00:00:00.000000000&#x27;, ..., &#x27;2012-12-19T00:00:00.000000000&#x27;,
       &#x27;2012-12-20T00:00:00.000000000&#x27;, &#x27;2012-12-21T00:00:00.000000000&#x27;],
      shape=(8756,), dtype=&#x27;datetime64[ns]&#x27;)
Coordinates:
  * time     (time) datetime64[ns] 70kB 1989-01-01 1989-01-02 ... 2012-12-21</pre><div class='xr-wrap' style='display:none'><div class='xr-header'><div class='xr-obj-type'>xarray.DataArray</div><div class='xr-array-name'>'time'</div><ul class='xr-dim-list'><li><span class='xr-has-index'>time</span>: 8756</li></ul></div><ul class='xr-sections'><li class='xr-section-item'><div class='xr-array-wrap'><input id='section-98cfba7f-7ab1-4938-a5a8-079629abca26' class='xr-array-in' type='checkbox' checked><label for='section-98cfba7f-7ab1-4938-a5a8-079629abca26' title='Show/hide data repr'><svg class='icon xr-icon-database'><use xlink:href='#icon-database'></use></svg></label><div class='xr-array-preview xr-preview'><span>1989-01-01 1989-01-02 1989-01-03 ... 2012-12-19 2012-12-20 2012-12-21</span></div><div class='xr-array-data'><pre>array([&#x27;1989-01-01T00:00:00.000000000&#x27;, &#x27;1989-01-02T00:00:00.000000000&#x27;,
       &#x27;1989-01-03T00:00:00.000000000&#x27;, ..., &#x27;2012-12-19T00:00:00.000000000&#x27;,
       &#x27;2012-12-20T00:00:00.000000000&#x27;, &#x27;2012-12-21T00:00:00.000000000&#x27;],
      shape=(8756,), dtype=&#x27;datetime64[ns]&#x27;)</pre></div></div></li><li class='xr-section-item'><input id='section-1823b872-45de-41e0-a4ff-6f157f69e8db' class='xr-section-summary-in' type='checkbox'  checked><label for='section-1823b872-45de-41e0-a4ff-6f157f69e8db' class='xr-section-summary' >Coordinates: <span>(1)</span></label><div class='xr-section-inline-details'></div><div class='xr-section-details'><ul class='xr-var-list'><li class='xr-var-item'><div class='xr-var-name'><span class='xr-has-index'>time</span></div><div class='xr-var-dims'>(time)</div><div class='xr-var-dtype'>datetime64[ns]</div><div class='xr-var-preview xr-preview'>1989-01-01 ... 2012-12-21</div><input id='attrs-5478961b-7325-440e-8f98-b32760190870' class='xr-var-attrs-in' type='checkbox' disabled><label for='attrs-5478961b-7325-440e-8f98-b32760190870' title='Show/Hide attributes'><svg class='icon xr-icon-file-text2'><use xlink:href='#icon-file-text2'></use></svg></label><input id='data-c345422f-92b5-4ec8-bcee-2bd3c0bc2a81' class='xr-var-data-in' type='checkbox'><label for='data-c345422f-92b5-4ec8-bcee-2bd3c0bc2a81' title='Show/Hide data repr'><svg class='icon xr-icon-database'><use xlink:href='#icon-database'></use></svg></label><div class='xr-var-attrs'><dl class='xr-attrs'></dl></div><div class='xr-var-data'><pre>array([&#x27;1989-01-01T00:00:00.000000000&#x27;, &#x27;1989-01-02T00:00:00.000000000&#x27;,
       &#x27;1989-01-03T00:00:00.000000000&#x27;, ..., &#x27;2012-12-19T00:00:00.000000000&#x27;,
       &#x27;2012-12-20T00:00:00.000000000&#x27;, &#x27;2012-12-21T00:00:00.000000000&#x27;],
      shape=(8756,), dtype=&#x27;datetime64[ns]&#x27;)</pre></div></li></ul></div></li><li class='xr-section-item'><input id='section-25b2267f-ebef-4692-8859-375f19e133c6' class='xr-section-summary-in' type='checkbox'  ><label for='section-25b2267f-ebef-4692-8859-375f19e133c6' class='xr-section-summary' >Indexes: <span>(1)</span></label><div class='xr-section-inline-details'></div><div class='xr-section-details'><ul class='xr-var-list'><li class='xr-var-item'><div class='xr-index-name'><div>time</div></div><div class='xr-index-preview'>PandasIndex</div><div></div><input id='index-4b434bf3-1fdc-4a86-b48d-d294533e9390' class='xr-index-data-in' type='checkbox'/><label for='index-4b434bf3-1fdc-4a86-b48d-d294533e9390' title='Show/Hide index repr'><svg class='icon xr-icon-database'><use xlink:href='#icon-database'></use></svg></label><div class='xr-index-data'><pre>PandasIndex(DatetimeIndex([&#x27;1989-01-01&#x27;, &#x27;1989-01-02&#x27;, &#x27;1989-01-03&#x27;, &#x27;1989-01-04&#x27;,
               &#x27;1989-01-05&#x27;, &#x27;1989-01-06&#x27;, &#x27;1989-01-07&#x27;, &#x27;1989-01-08&#x27;,
               &#x27;1989-01-09&#x27;, &#x27;1989-01-10&#x27;,
               ...
               &#x27;2012-12-12&#x27;, &#x27;2012-12-13&#x27;, &#x27;2012-12-14&#x27;, &#x27;2012-12-15&#x27;,
               &#x27;2012-12-16&#x27;, &#x27;2012-12-17&#x27;, &#x27;2012-12-18&#x27;, &#x27;2012-12-19&#x27;,
               &#x27;2012-12-20&#x27;, &#x27;2012-12-21&#x27;],
              dtype=&#x27;datetime64[ns]&#x27;, name=&#x27;time&#x27;, length=8756, freq=&#x27;D&#x27;))</pre></div></li></ul></div></li><li class='xr-section-item'><input id='section-ae503c16-77e7-4f1f-9bf5-3dbd8bade63b' class='xr-section-summary-in' type='checkbox' disabled ><label for='section-ae503c16-77e7-4f1f-9bf5-3dbd8bade63b' class='xr-section-summary'  title='Expand/collapse section'>Attributes: <span>(0)</span></label><div class='xr-section-inline-details'></div><div class='xr-section-details'><dl class='xr-attrs'></dl></div></li></ul></div></div>



### Setting simulation inputs by reading from a data library

swift simulations have a `play_inputs` (with an s) method designed to retrieve inputs from a library. 


```python
simulation.play_inputs?
```

`play_inputs` can accept vectorised arguments, which is handy for cases like the following:

> For each precipitation model input, use the same time series 'rain_obs' from the data library.


```python
precip_ids = mk_full_data_id( 'subarea', get_subarea_ids(simulation), 'P')
evapIds = mk_full_data_id( 'subarea', get_subarea_ids(simulation), 'E')
precip_ids, evapIds
```




    (['subarea.lnk1.P',
      'subarea.lnk2.P',
      'subarea.lnk3.P',
      'subarea.lnk4.P',
      'subarea.lnk5.P'],
     ['subarea.lnk1.E',
      'subarea.lnk2.E',
      'subarea.lnk3.E',
      'subarea.lnk4.E',
      'subarea.lnk5.E'])




```python
def _rep(x): return np.repeat(x, len(precip_ids))
simulation.play_inputs(data_library, precip_ids, _rep('rain_obs'), _rep(''))
```

We noted that the pet_obs is a daily series, not hourly as per . `swift2` can disaggregate on the fly, using the 'daily_to_hourly' method when assigning inputs to the simulation. This saves a lot of tedium!


```python
simulation.play_inputs(data_library, evapIds, _rep('pet_obs'), _rep('daily_to_hourly'))
# And the flow rate we will record
outflow_id = CATCHMENT_FLOWRATE_VARID
```

Given the information from the input data, let's define a suitable simulation time span. We have define an ensemble simulation where we will do a warmup simulation on a single input (no "ensemble") for 3 years or so, then five days of an ensemble simulation.


```python
from cinterop.timeseries import as_timestamp
 
s = as_timestamp('2007-01-01')
e = as_timestamp('2010-08-01 20')
s_hot = as_timestamp('2010-08-01 21')
e_hot = as_timestamp('2010-08-05 21')
```

## Warmup the simulation to get 'hot' states

First, before demonstrating ensemble forecasting simulations, let's demonstrate how we can get a snapshot of the model states at a point in time and restore it later on, hot-starting further simulation.

We deliberately get into details here to illustrate how to capture states, and run simulation without or without state reset.


```python
simulation.set_simulation_span(start=s, end=e_hot)
simulation.record_state(outflow_id)
simulation.exec_simulation()
baseline = simulation.get_recorded(outflow_id)
```


```python
baseline = baseline.squeeze(drop=True).sel(time = slice(s_hot, e_hot))
```


```python
baseline.plot(figsize=(10,5))
plt.title("streamflow with long term simulation, slice to the end of the series")
```




    Text(0.5, 1.0, 'streamflow with long term simulation, slice to the end of the series')




    
![png](ensemble_model_runs_files/ensemble_model_runs_37_1.png)
    



```python
simulation.set_simulation_span(start=s, end=e)
simulation.exec_simulation()
snapshot = simulation.snapshot_state()
```

We can execute a simulation over the new time span, but requesting model states to NOT be reset. If we compare with a simulation where, as per default, the states are reset before the first time step, we notice a difference:


```python
simulation.set_simulation_span(start=s_hot, end=e_hot)
simulation.exec_simulation(reset_initial_states = False)
noReset = simulation.get_recorded(outflow_id)
simulation.exec_simulation(reset_initial_states = True)
withReset = simulation.get_recorded(outflow_id)
```


```python
noReset = noReset.squeeze(drop=True)

x = xr.concat([noReset,withReset], dim=pd.Index(['no reset','reset'], name='scenario')).squeeze(drop=True)
```


```python
fig, ax = plt.subplots(figsize=(10,5))
ax.plot(x.time.values, x.sel(scenario='no reset'), linewidth=2, label='No reset')
ax.plot(x.time.values, x.sel(scenario='reset'), linewidth=2, label='Reset')
ax.legend()
plt.show()
```


    
![png](ensemble_model_runs_files/ensemble_model_runs_42_0.png)
    


The simulation hot-started and run with no reset is like the previous long simulation baseline. If we reset the states to zero, we even have ho streamflow yet produced over these 5 days...

## Ensemble forecasts

Now let'd ready the simulation to do ensemble forecasts. We define a list `inputMap` such that keys are the names of ensemble forecast time series found in `data_library` and the values is one or more of the model properties found in the simulation. In this instance we use the same series for all model precipitation inputs in `precip_ids` 


```python
simulation.reset_model_states()
simulation.set_states(snapshot)
```


```python
inputMap = {'rain_fcast_ens':precip_ids}
```


```python
ems = simulation.create_ensemble_forecast_simulation(
    data_library, 
    start=s_hot, 
    end=e_hot, 
    input_map=inputMap, 
    lead_time=(24*2+23), 
    ensemble_size=100, 
    n_time_steps_between_forecasts=24)
```


```python
ems
```




    CFFI pointer handle to a native pointer of type id "ENSEMBLE_FORECAST_SIMULATION_PTR"



`ems` is an ensemble forecast simulation object, which is an augmentation of the `Simulation` object that deals with non-ensemble simulation. It is very important to note that whenever possible, the object methods are named identically, just that the time series in and out of the simulations are of higher dimension.    


```python
ems.get_simulation_span()
```




    {'start': datetime.datetime(2010, 8, 1, 21, 0),
     'end': datetime.datetime(2010, 8, 4, 21, 0),
     'time step': 'hourly'}




```python
ems.record_state(outflow_id)
ems.exec_simulation()
forecasts = ems.get_recorded_ensemble_forecast(outflow_id)
```


```python
type(forecasts)
```




    uchronia.classes.EnsembleForecastTimeSeries



We have four forecast issue times:


```python
forecasts.time_index()
```




    DatetimeIndex(['2010-08-01 21:00:00', '2010-08-02 21:00:00',
                   '2010-08-03 21:00:00', '2010-08-04 21:00:00'],
                  dtype='datetime64[ns]', freq='D')



We can retrieve the first forecast issues at '2010-08-01 21:00:00' by indexing


```python
flow_forecasts = forecasts[0]
```


```python
flow_forecasts
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
</style><pre class='xr-text-repr-fallback'>&lt;xarray.DataArray (ensemble: 100, time: 71)&gt; Size: 57kB
array([[0.8898914 , 0.97225084, 1.05916427, ..., 0.76254716, 0.6787237 ,
        0.6702664 ],
       [0.63547795, 0.62744525, 0.61985413, ..., 0.47899561, 0.48934704,
        0.49825249],
       [0.62397353, 0.61255692, 0.60179053, ..., 0.41359509, 0.4271383 ,
        0.43487164],
       ...,
       [0.61988133, 0.6072754 , 0.59540094, ..., 0.48367713, 0.47991112,
        0.47624805],
       [0.61967395, 0.60698496, 0.59505003, ..., 0.46636062, 0.46183589,
        0.45746333],
       [0.61967228, 0.60698117, 0.59504373, ..., 0.34924574, 0.34735597,
        0.34549876]], shape=(100, 71))
Coordinates:
  * ensemble  (ensemble) int64 800B 0 1 2 3 4 5 6 7 ... 92 93 94 95 96 97 98 99
  * time      (time) datetime64[ns] 568B 2010-08-01T22:00:00 ... 2010-08-04T2...</pre><div class='xr-wrap' style='display:none'><div class='xr-header'><div class='xr-obj-type'>xarray.DataArray</div><div class='xr-array-name'></div><ul class='xr-dim-list'><li><span class='xr-has-index'>ensemble</span>: 100</li><li><span class='xr-has-index'>time</span>: 71</li></ul></div><ul class='xr-sections'><li class='xr-section-item'><div class='xr-array-wrap'><input id='section-8b16a1fd-0a17-4564-98b6-ce8694d73628' class='xr-array-in' type='checkbox' checked><label for='section-8b16a1fd-0a17-4564-98b6-ce8694d73628' title='Show/hide data repr'><svg class='icon xr-icon-database'><use xlink:href='#icon-database'></use></svg></label><div class='xr-array-preview xr-preview'><span>0.8899 0.9723 1.059 1.522 1.817 ... 0.3531 0.3512 0.3492 0.3474 0.3455</span></div><div class='xr-array-data'><pre>array([[0.8898914 , 0.97225084, 1.05916427, ..., 0.76254716, 0.6787237 ,
        0.6702664 ],
       [0.63547795, 0.62744525, 0.61985413, ..., 0.47899561, 0.48934704,
        0.49825249],
       [0.62397353, 0.61255692, 0.60179053, ..., 0.41359509, 0.4271383 ,
        0.43487164],
       ...,
       [0.61988133, 0.6072754 , 0.59540094, ..., 0.48367713, 0.47991112,
        0.47624805],
       [0.61967395, 0.60698496, 0.59505003, ..., 0.46636062, 0.46183589,
        0.45746333],
       [0.61967228, 0.60698117, 0.59504373, ..., 0.34924574, 0.34735597,
        0.34549876]], shape=(100, 71))</pre></div></div></li><li class='xr-section-item'><input id='section-88b7e43f-0da6-4624-b01b-6ef0464103ce' class='xr-section-summary-in' type='checkbox'  checked><label for='section-88b7e43f-0da6-4624-b01b-6ef0464103ce' class='xr-section-summary' >Coordinates: <span>(2)</span></label><div class='xr-section-inline-details'></div><div class='xr-section-details'><ul class='xr-var-list'><li class='xr-var-item'><div class='xr-var-name'><span class='xr-has-index'>ensemble</span></div><div class='xr-var-dims'>(ensemble)</div><div class='xr-var-dtype'>int64</div><div class='xr-var-preview xr-preview'>0 1 2 3 4 5 6 ... 94 95 96 97 98 99</div><input id='attrs-e3b8e10d-d9e2-4e35-a3dd-af0930a9466c' class='xr-var-attrs-in' type='checkbox' disabled><label for='attrs-e3b8e10d-d9e2-4e35-a3dd-af0930a9466c' title='Show/Hide attributes'><svg class='icon xr-icon-file-text2'><use xlink:href='#icon-file-text2'></use></svg></label><input id='data-7cf0e693-16ae-4f08-b799-106f443ebba0' class='xr-var-data-in' type='checkbox'><label for='data-7cf0e693-16ae-4f08-b799-106f443ebba0' title='Show/Hide data repr'><svg class='icon xr-icon-database'><use xlink:href='#icon-database'></use></svg></label><div class='xr-var-attrs'><dl class='xr-attrs'></dl></div><div class='xr-var-data'><pre>array([ 0,  1,  2,  3,  4,  5,  6,  7,  8,  9, 10, 11, 12, 13, 14, 15, 16, 17,
       18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35,
       36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53,
       54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71,
       72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89,
       90, 91, 92, 93, 94, 95, 96, 97, 98, 99])</pre></div></li><li class='xr-var-item'><div class='xr-var-name'><span class='xr-has-index'>time</span></div><div class='xr-var-dims'>(time)</div><div class='xr-var-dtype'>datetime64[ns]</div><div class='xr-var-preview xr-preview'>2010-08-01T22:00:00 ... 2010-08-...</div><input id='attrs-a10925af-d8df-4d8e-aaa8-6f7543d7e0e2' class='xr-var-attrs-in' type='checkbox' disabled><label for='attrs-a10925af-d8df-4d8e-aaa8-6f7543d7e0e2' title='Show/Hide attributes'><svg class='icon xr-icon-file-text2'><use xlink:href='#icon-file-text2'></use></svg></label><input id='data-e392a560-3bd9-49b6-9fd6-557d64f6990b' class='xr-var-data-in' type='checkbox'><label for='data-e392a560-3bd9-49b6-9fd6-557d64f6990b' title='Show/Hide data repr'><svg class='icon xr-icon-database'><use xlink:href='#icon-database'></use></svg></label><div class='xr-var-attrs'><dl class='xr-attrs'></dl></div><div class='xr-var-data'><pre>array([&#x27;2010-08-01T22:00:00.000000000&#x27;, &#x27;2010-08-01T23:00:00.000000000&#x27;,
       &#x27;2010-08-02T00:00:00.000000000&#x27;, &#x27;2010-08-02T01:00:00.000000000&#x27;,
       &#x27;2010-08-02T02:00:00.000000000&#x27;, &#x27;2010-08-02T03:00:00.000000000&#x27;,
       &#x27;2010-08-02T04:00:00.000000000&#x27;, &#x27;2010-08-02T05:00:00.000000000&#x27;,
       &#x27;2010-08-02T06:00:00.000000000&#x27;, &#x27;2010-08-02T07:00:00.000000000&#x27;,
       &#x27;2010-08-02T08:00:00.000000000&#x27;, &#x27;2010-08-02T09:00:00.000000000&#x27;,
       &#x27;2010-08-02T10:00:00.000000000&#x27;, &#x27;2010-08-02T11:00:00.000000000&#x27;,
       &#x27;2010-08-02T12:00:00.000000000&#x27;, &#x27;2010-08-02T13:00:00.000000000&#x27;,
       &#x27;2010-08-02T14:00:00.000000000&#x27;, &#x27;2010-08-02T15:00:00.000000000&#x27;,
       &#x27;2010-08-02T16:00:00.000000000&#x27;, &#x27;2010-08-02T17:00:00.000000000&#x27;,
       &#x27;2010-08-02T18:00:00.000000000&#x27;, &#x27;2010-08-02T19:00:00.000000000&#x27;,
       &#x27;2010-08-02T20:00:00.000000000&#x27;, &#x27;2010-08-02T21:00:00.000000000&#x27;,
       &#x27;2010-08-02T22:00:00.000000000&#x27;, &#x27;2010-08-02T23:00:00.000000000&#x27;,
       &#x27;2010-08-03T00:00:00.000000000&#x27;, &#x27;2010-08-03T01:00:00.000000000&#x27;,
       &#x27;2010-08-03T02:00:00.000000000&#x27;, &#x27;2010-08-03T03:00:00.000000000&#x27;,
       &#x27;2010-08-03T04:00:00.000000000&#x27;, &#x27;2010-08-03T05:00:00.000000000&#x27;,
       &#x27;2010-08-03T06:00:00.000000000&#x27;, &#x27;2010-08-03T07:00:00.000000000&#x27;,
       &#x27;2010-08-03T08:00:00.000000000&#x27;, &#x27;2010-08-03T09:00:00.000000000&#x27;,
       &#x27;2010-08-03T10:00:00.000000000&#x27;, &#x27;2010-08-03T11:00:00.000000000&#x27;,
       &#x27;2010-08-03T12:00:00.000000000&#x27;, &#x27;2010-08-03T13:00:00.000000000&#x27;,
       &#x27;2010-08-03T14:00:00.000000000&#x27;, &#x27;2010-08-03T15:00:00.000000000&#x27;,
       &#x27;2010-08-03T16:00:00.000000000&#x27;, &#x27;2010-08-03T17:00:00.000000000&#x27;,
       &#x27;2010-08-03T18:00:00.000000000&#x27;, &#x27;2010-08-03T19:00:00.000000000&#x27;,
       &#x27;2010-08-03T20:00:00.000000000&#x27;, &#x27;2010-08-03T21:00:00.000000000&#x27;,
       &#x27;2010-08-03T22:00:00.000000000&#x27;, &#x27;2010-08-03T23:00:00.000000000&#x27;,
       &#x27;2010-08-04T00:00:00.000000000&#x27;, &#x27;2010-08-04T01:00:00.000000000&#x27;,
       &#x27;2010-08-04T02:00:00.000000000&#x27;, &#x27;2010-08-04T03:00:00.000000000&#x27;,
       &#x27;2010-08-04T04:00:00.000000000&#x27;, &#x27;2010-08-04T05:00:00.000000000&#x27;,
       &#x27;2010-08-04T06:00:00.000000000&#x27;, &#x27;2010-08-04T07:00:00.000000000&#x27;,
       &#x27;2010-08-04T08:00:00.000000000&#x27;, &#x27;2010-08-04T09:00:00.000000000&#x27;,
       &#x27;2010-08-04T10:00:00.000000000&#x27;, &#x27;2010-08-04T11:00:00.000000000&#x27;,
       &#x27;2010-08-04T12:00:00.000000000&#x27;, &#x27;2010-08-04T13:00:00.000000000&#x27;,
       &#x27;2010-08-04T14:00:00.000000000&#x27;, &#x27;2010-08-04T15:00:00.000000000&#x27;,
       &#x27;2010-08-04T16:00:00.000000000&#x27;, &#x27;2010-08-04T17:00:00.000000000&#x27;,
       &#x27;2010-08-04T18:00:00.000000000&#x27;, &#x27;2010-08-04T19:00:00.000000000&#x27;,
       &#x27;2010-08-04T20:00:00.000000000&#x27;], dtype=&#x27;datetime64[ns]&#x27;)</pre></div></li></ul></div></li><li class='xr-section-item'><input id='section-904ac233-5de2-4c35-9339-6b55811ee3f9' class='xr-section-summary-in' type='checkbox'  ><label for='section-904ac233-5de2-4c35-9339-6b55811ee3f9' class='xr-section-summary' >Indexes: <span>(2)</span></label><div class='xr-section-inline-details'></div><div class='xr-section-details'><ul class='xr-var-list'><li class='xr-var-item'><div class='xr-index-name'><div>ensemble</div></div><div class='xr-index-preview'>PandasIndex</div><div></div><input id='index-dd249386-82ab-4f28-a2f9-06a776fbc330' class='xr-index-data-in' type='checkbox'/><label for='index-dd249386-82ab-4f28-a2f9-06a776fbc330' title='Show/Hide index repr'><svg class='icon xr-icon-database'><use xlink:href='#icon-database'></use></svg></label><div class='xr-index-data'><pre>PandasIndex(Index([ 0,  1,  2,  3,  4,  5,  6,  7,  8,  9, 10, 11, 12, 13, 14, 15, 16, 17,
       18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35,
       36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53,
       54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71,
       72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89,
       90, 91, 92, 93, 94, 95, 96, 97, 98, 99],
      dtype=&#x27;int64&#x27;, name=&#x27;ensemble&#x27;))</pre></div></li><li class='xr-var-item'><div class='xr-index-name'><div>time</div></div><div class='xr-index-preview'>PandasIndex</div><div></div><input id='index-b7a15f82-4674-4ce6-a2fa-e860cb0193db' class='xr-index-data-in' type='checkbox'/><label for='index-b7a15f82-4674-4ce6-a2fa-e860cb0193db' title='Show/Hide index repr'><svg class='icon xr-icon-database'><use xlink:href='#icon-database'></use></svg></label><div class='xr-index-data'><pre>PandasIndex(DatetimeIndex([&#x27;2010-08-01 22:00:00&#x27;, &#x27;2010-08-01 23:00:00&#x27;,
               &#x27;2010-08-02 00:00:00&#x27;, &#x27;2010-08-02 01:00:00&#x27;,
               &#x27;2010-08-02 02:00:00&#x27;, &#x27;2010-08-02 03:00:00&#x27;,
               &#x27;2010-08-02 04:00:00&#x27;, &#x27;2010-08-02 05:00:00&#x27;,
               &#x27;2010-08-02 06:00:00&#x27;, &#x27;2010-08-02 07:00:00&#x27;,
               &#x27;2010-08-02 08:00:00&#x27;, &#x27;2010-08-02 09:00:00&#x27;,
               &#x27;2010-08-02 10:00:00&#x27;, &#x27;2010-08-02 11:00:00&#x27;,
               &#x27;2010-08-02 12:00:00&#x27;, &#x27;2010-08-02 13:00:00&#x27;,
               &#x27;2010-08-02 14:00:00&#x27;, &#x27;2010-08-02 15:00:00&#x27;,
               &#x27;2010-08-02 16:00:00&#x27;, &#x27;2010-08-02 17:00:00&#x27;,
               &#x27;2010-08-02 18:00:00&#x27;, &#x27;2010-08-02 19:00:00&#x27;,
               &#x27;2010-08-02 20:00:00&#x27;, &#x27;2010-08-02 21:00:00&#x27;,
               &#x27;2010-08-02 22:00:00&#x27;, &#x27;2010-08-02 23:00:00&#x27;,
               &#x27;2010-08-03 00:00:00&#x27;, &#x27;2010-08-03 01:00:00&#x27;,
               &#x27;2010-08-03 02:00:00&#x27;, &#x27;2010-08-03 03:00:00&#x27;,
               &#x27;2010-08-03 04:00:00&#x27;, &#x27;2010-08-03 05:00:00&#x27;,
               &#x27;2010-08-03 06:00:00&#x27;, &#x27;2010-08-03 07:00:00&#x27;,
               &#x27;2010-08-03 08:00:00&#x27;, &#x27;2010-08-03 09:00:00&#x27;,
               &#x27;2010-08-03 10:00:00&#x27;, &#x27;2010-08-03 11:00:00&#x27;,
               &#x27;2010-08-03 12:00:00&#x27;, &#x27;2010-08-03 13:00:00&#x27;,
               &#x27;2010-08-03 14:00:00&#x27;, &#x27;2010-08-03 15:00:00&#x27;,
               &#x27;2010-08-03 16:00:00&#x27;, &#x27;2010-08-03 17:00:00&#x27;,
               &#x27;2010-08-03 18:00:00&#x27;, &#x27;2010-08-03 19:00:00&#x27;,
               &#x27;2010-08-03 20:00:00&#x27;, &#x27;2010-08-03 21:00:00&#x27;,
               &#x27;2010-08-03 22:00:00&#x27;, &#x27;2010-08-03 23:00:00&#x27;,
               &#x27;2010-08-04 00:00:00&#x27;, &#x27;2010-08-04 01:00:00&#x27;,
               &#x27;2010-08-04 02:00:00&#x27;, &#x27;2010-08-04 03:00:00&#x27;,
               &#x27;2010-08-04 04:00:00&#x27;, &#x27;2010-08-04 05:00:00&#x27;,
               &#x27;2010-08-04 06:00:00&#x27;, &#x27;2010-08-04 07:00:00&#x27;,
               &#x27;2010-08-04 08:00:00&#x27;, &#x27;2010-08-04 09:00:00&#x27;,
               &#x27;2010-08-04 10:00:00&#x27;, &#x27;2010-08-04 11:00:00&#x27;,
               &#x27;2010-08-04 12:00:00&#x27;, &#x27;2010-08-04 13:00:00&#x27;,
               &#x27;2010-08-04 14:00:00&#x27;, &#x27;2010-08-04 15:00:00&#x27;,
               &#x27;2010-08-04 16:00:00&#x27;, &#x27;2010-08-04 17:00:00&#x27;,
               &#x27;2010-08-04 18:00:00&#x27;, &#x27;2010-08-04 19:00:00&#x27;,
               &#x27;2010-08-04 20:00:00&#x27;],
              dtype=&#x27;datetime64[ns]&#x27;, name=&#x27;time&#x27;, freq=&#x27;h&#x27;))</pre></div></li></ul></div></li><li class='xr-section-item'><input id='section-f1761aa7-ed1b-490a-b339-b3cfbe53c5f5' class='xr-section-summary-in' type='checkbox' disabled ><label for='section-f1761aa7-ed1b-490a-b339-b3cfbe53c5f5' class='xr-section-summary'  title='Expand/collapse section'>Attributes: <span>(0)</span></label><div class='xr-section-inline-details'></div><div class='xr-section-details'><dl class='xr-attrs'></dl></div></li></ul></div></div>



## Visualisation

Let's visualise each of these successive ensemble forecasts. We define a function to determine and visualise the quantiles:


```python
def plot_ensemble_forecast(flow_forecasts, issue_date):
    q = flow_forecasts.quantile([0.05, .25, .5, .75, 0.95], 'ensemble')
    fig, ax = plt.subplots(figsize=(10,5))
    ax.fill_between(q.time.values, q.sel(quantile=0.05), q.sel(quantile=0.95), alpha=0.3, label='Perc. 50-95')
    ax.fill_between(q.time.values, q.sel(quantile=0.25), q.sel(quantile=.75), alpha=0.5, label='Perc. 25-75')
    ax._get_lines.get_next_color()  # Hack to get different line
    ax.plot(q.time.values, q.sel(quantile=.5), linewidth=2, label='Median')
    ax.legend()
    dd = pd.Timestamp(issue_date).strftime('%Y-%m-%dT%H')
    plt.title(f"Ensemble forecast streamflow {dd}")
    plt.ylabel("Streamflow (m3/s)")
    plt.show()
```


```python
issue_dates = forecasts.time_index().values
```


```python
plot_ensemble_forecast(forecasts[0], issue_dates[0])
```


    
![png](ensemble_model_runs_files/ensemble_model_runs_62_0.png)
    



```python
plot_ensemble_forecast(forecasts[1], issue_dates[1])
```


    
![png](ensemble_model_runs_files/ensemble_model_runs_63_0.png)
    



```python
plot_ensemble_forecast(forecasts[2], issue_dates[2])
```


    
![png](ensemble_model_runs_files/ensemble_model_runs_64_0.png)
    



```python
plot_ensemble_forecast(forecasts[3], issue_dates[3])
```


    
![png](ensemble_model_runs_files/ensemble_model_runs_65_0.png)
    


## Appendix

### Data library sample definition

The sample data library used in this vignette is defined by a YAML file defining where time series (or ensemble time series) are on disk in netcdf files. Note that one series can be in several netCDF files, and conversely it is possible to define multiple series (e.g. per station) in one file.

```yaml
pet_fcast_ens:
  Type: single
  Id: pet_fcast_ens
  Storage:
    Type: single_nc_file
    File: ./Fct_Data/Upper_Murray_pet_clim_1990_2010.nc
    Identifier: 1
    Var: pet_der
pet_obs:
  Type: single
  Id: pet_obs
  Storage:
    Type: single_nc_file
    File: ./Obs_data/Upper_Murray_pet_24h_89_2012.nc
    Identifier: 1
    Var: pet_der
rain_obs:
  Type: single
  Id: rain_obs
  Storage:
    Type: single_nc_file
    File: ./Obs_data/Upper_Murray_rain_1hr.nc
    Identifier: 1
    Var: rain_der
rain_fcast_ens:
  Type: ts_ensemble_ts
  Id: rain_fcast_ens
  # The following 6 values are placeholders - may not yet be used by time series library
  TimeStep: 24:00:00
  Start: 2010-08-01T21:00:00
  Length: 5
  EnsembleSize: 1000
  EnsembleLength: 240
  EnsembleTimeStep: 01:00:00
  Storage:
    Type: multiple_nc_files_filename_date_pattern
    File: ./Fct_Data/Upper_Murray_F1_1_{0}21_shuffle.nc
    Var: rain_fcast_ens
    Identifier: 1
    Index: 0
```



```python

```


```python

```


```python

```
