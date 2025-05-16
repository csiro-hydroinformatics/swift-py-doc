# Getting started with the swift python package

## About this document

This is a minimal but realistic simulation workflow for swift. It was ported from an original [vignette](https://github.com/csiro-hydroinformatics/streamflow-forecasting-tools-onboard/blob/master/doc/vignettes/getting_started/getting_started.md) in the R package `swift`. The python package [`swift2`](https://csiro-hydroinformatics.github.io/swift-py-doc/) is, as of August 2023, at least at feature parity with the long established R package. 

This is the introduction 'notebook' to a python package for interacting with SWIFT. It shows one of the most basic usage, running a single model simulation. While basic, it is realistic and uses data from a study catchment.


```python
from swift2.doc_helper import pkg_versions_info

print(pkg_versions_info("This document was generated from a jupyter notebook"))
```

    This document was generated from a jupyter notebook on 2025-03-27 17:24:44.897481
        swift2 2.5.1
        uchronia 2.6.2


## Prerequisites

This notebook requires a working Python environment, e.g. a conda environment. See the [Streamflow Forecasting](https://csiro-hydroinformatics.github.io/streamflow-forecasting-tools-onboard/) landing page for information about installing the software.

## Imports



```python
from typing import List

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
```

Finally we import some visualisation facilities


```python
import seaborn as sns
import xarray as xr
```

Some dependencies of **swift2**, namely **cinterop**, offer generic functions for time series manipulations. While these could be imported via **swift2** as well, let's be explicit for now:


```python
from cinterop.timeseries import (
    TIME_DIMNAME,
    as_timestamp,
    pd_series_to_xr_series,
    slice_xr_time_series,
    xr_ts_end,
    xr_ts_start,
)
from swift2.doc_helper import get_free_params, sample_series
from swift2.parameteriser import (
    create_parameter_sampler,
    create_parameteriser,
    create_sce_termination_wila,
    get_default_sce_parameters,
)
from swift2.simulation import create_subarea_simulation
```


```python
from swift2.system import runoff_model_ids, runoff_model_var_ids
```

We import the main functions upfront from the package submodules. In practice this is something you may need to do only on an as needed basis of course. Jupyter notebooks can show dynanically submodules and functions listed, along with some documentation. A searchable technical documentation for the package is available from [Python swift2 documentation](https://csiro-hydroinformatics.github.io/swift-py-doc). 


```python
from swift2.utils import mk_full_data_id, paste_2, vpaste
```


```python
%matplotlib inline
```

## Lumped catchment data, daily data

The package contains some sample data for a few Australian catchments. Note that these sample data are for documentation only and not to be used for real world applications.  

**swift** now has some functions to create a single subarea simulation for testing purposes, including the function `create_subarea_simulation`. While is it perfectly possible to manually build your own model simulation from scratch, for the sake of getting started quickly let's use pre-defined functions to get a model simulation ready to run. The parameters of the function should be fairly self-explanatory. But in general you can see function documentation with commands appended with the `?` string, e.g. `create_subarea_simulation?`. You can also browse the [Python swift2 documentation](https://csiro-hydroinformatics.github.io/swift-py-doc).


```python
create_subarea_simulation?
```


```python
ms = create_subarea_simulation(data_id='MMH', simul_start='1990-01-01', simul_end='2005-12-31', 
    model_id='GR4J', tstep='daily', varname_rain='P', varname_pet='E')
```


```python
ms
```




    Simulation wrapper for a CFFI pointer handle to a native pointer of type id "MODEL_SIMULATION_PTR"




```python
type(ms)
```




    swift2.classes.Simulation



The python object `ms` may appear unusual to most users. This is basically a handle to the SWIFT simulation object written in C++. The model core is native, but wrapped by a "pythonic" `Simulation` object. The low-level interaction between python and the C API is handled by "glue code" and users will rarely if ever need to use the low-level API.

The `Simulation` object has python methods to interact with it, for instance:


```python
ms.describe?
```


```python
ms.describe()
```




    {'subareas': {'Subarea': 'Subarea'}, 'nodes': {}, 'links': {}}



Because we got a preconfigured, sample simulation, it is ready to execute, which means it already has some input data defined (a site with a codename 'MMH'). The `SWIFT` system uses the terms `playing from` and `recording to` time series, using an old style audio tape system as a metaphor. We can inspect the simulation for instance using `get_played_varnames` to check which state variable has an input time series:


```python
ms.get_played_varnames()
```




    ['subarea.Subarea.E', 'subarea.Subarea.P']



### Time series data representation

Let us have a look at these input time series to the simulation:


```python
tts = ms.get_played()
tts
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
</style><pre class='xr-text-repr-fallback'>&lt;xarray.DataArray (variable_identifiers: 2, ensemble: 1, time: 5844)&gt; Size: 94kB
array([[[5.5422, 5.5522, 5.5622, ..., 6.0744, 6.0735, 6.0725]],

       [[0.    , 0.    , 0.    , ..., 2.1569, 0.    , 0.    ]]],
      shape=(2, 1, 5844))
Coordinates:
  * ensemble              (ensemble) int64 8B 0
  * time                  (time) datetime64[ns] 47kB 1990-01-01 ... 2005-12-31
  * variable_identifiers  (variable_identifiers) object 16B &#x27;subarea.Subarea....</pre><div class='xr-wrap' style='display:none'><div class='xr-header'><div class='xr-obj-type'>xarray.DataArray</div><div class='xr-array-name'></div><ul class='xr-dim-list'><li><span class='xr-has-index'>variable_identifiers</span>: 2</li><li><span class='xr-has-index'>ensemble</span>: 1</li><li><span class='xr-has-index'>time</span>: 5844</li></ul></div><ul class='xr-sections'><li class='xr-section-item'><div class='xr-array-wrap'><input id='section-8577b12b-0837-452b-8164-0d70583dfa08' class='xr-array-in' type='checkbox' checked><label for='section-8577b12b-0837-452b-8164-0d70583dfa08' title='Show/hide data repr'><svg class='icon xr-icon-database'><use xlink:href='#icon-database'></use></svg></label><div class='xr-array-preview xr-preview'><span>5.542 5.552 5.562 5.572 5.582 5.592 ... 0.0659 0.5425 2.157 0.0 0.0</span></div><div class='xr-array-data'><pre>array([[[5.5422, 5.5522, 5.5622, ..., 6.0744, 6.0735, 6.0725]],

       [[0.    , 0.    , 0.    , ..., 2.1569, 0.    , 0.    ]]],
      shape=(2, 1, 5844))</pre></div></div></li><li class='xr-section-item'><input id='section-b951aa71-628a-4c6e-9e0c-d855c90f017b' class='xr-section-summary-in' type='checkbox'  checked><label for='section-b951aa71-628a-4c6e-9e0c-d855c90f017b' class='xr-section-summary' >Coordinates: <span>(3)</span></label><div class='xr-section-inline-details'></div><div class='xr-section-details'><ul class='xr-var-list'><li class='xr-var-item'><div class='xr-var-name'><span class='xr-has-index'>ensemble</span></div><div class='xr-var-dims'>(ensemble)</div><div class='xr-var-dtype'>int64</div><div class='xr-var-preview xr-preview'>0</div><input id='attrs-4cefde9b-d9e6-47b6-92ac-c321b176bc01' class='xr-var-attrs-in' type='checkbox' disabled><label for='attrs-4cefde9b-d9e6-47b6-92ac-c321b176bc01' title='Show/Hide attributes'><svg class='icon xr-icon-file-text2'><use xlink:href='#icon-file-text2'></use></svg></label><input id='data-80b6d073-2af0-4dcb-bf4f-84f55c23e2f2' class='xr-var-data-in' type='checkbox'><label for='data-80b6d073-2af0-4dcb-bf4f-84f55c23e2f2' title='Show/Hide data repr'><svg class='icon xr-icon-database'><use xlink:href='#icon-database'></use></svg></label><div class='xr-var-attrs'><dl class='xr-attrs'></dl></div><div class='xr-var-data'><pre>array([0])</pre></div></li><li class='xr-var-item'><div class='xr-var-name'><span class='xr-has-index'>time</span></div><div class='xr-var-dims'>(time)</div><div class='xr-var-dtype'>datetime64[ns]</div><div class='xr-var-preview xr-preview'>1990-01-01 ... 2005-12-31</div><input id='attrs-9aa27ee1-f1a4-4e01-90aa-d88c64bf3811' class='xr-var-attrs-in' type='checkbox' disabled><label for='attrs-9aa27ee1-f1a4-4e01-90aa-d88c64bf3811' title='Show/Hide attributes'><svg class='icon xr-icon-file-text2'><use xlink:href='#icon-file-text2'></use></svg></label><input id='data-5241dccf-95ce-40fa-b4ea-2df8e70874a3' class='xr-var-data-in' type='checkbox'><label for='data-5241dccf-95ce-40fa-b4ea-2df8e70874a3' title='Show/Hide data repr'><svg class='icon xr-icon-database'><use xlink:href='#icon-database'></use></svg></label><div class='xr-var-attrs'><dl class='xr-attrs'></dl></div><div class='xr-var-data'><pre>array([&#x27;1990-01-01T00:00:00.000000000&#x27;, &#x27;1990-01-02T00:00:00.000000000&#x27;,
       &#x27;1990-01-03T00:00:00.000000000&#x27;, ..., &#x27;2005-12-29T00:00:00.000000000&#x27;,
       &#x27;2005-12-30T00:00:00.000000000&#x27;, &#x27;2005-12-31T00:00:00.000000000&#x27;],
      shape=(5844,), dtype=&#x27;datetime64[ns]&#x27;)</pre></div></li><li class='xr-var-item'><div class='xr-var-name'><span class='xr-has-index'>variable_identifiers</span></div><div class='xr-var-dims'>(variable_identifiers)</div><div class='xr-var-dtype'>object</div><div class='xr-var-preview xr-preview'>&#x27;subarea.Subarea.E&#x27; &#x27;subarea.Sub...</div><input id='attrs-ae043567-e5e0-41c6-bf19-621c3281ce70' class='xr-var-attrs-in' type='checkbox' disabled><label for='attrs-ae043567-e5e0-41c6-bf19-621c3281ce70' title='Show/Hide attributes'><svg class='icon xr-icon-file-text2'><use xlink:href='#icon-file-text2'></use></svg></label><input id='data-a1133007-170a-4467-8d71-f3440de99d27' class='xr-var-data-in' type='checkbox'><label for='data-a1133007-170a-4467-8d71-f3440de99d27' title='Show/Hide data repr'><svg class='icon xr-icon-database'><use xlink:href='#icon-database'></use></svg></label><div class='xr-var-attrs'><dl class='xr-attrs'></dl></div><div class='xr-var-data'><pre>array([&#x27;subarea.Subarea.E&#x27;, &#x27;subarea.Subarea.P&#x27;], dtype=object)</pre></div></li></ul></div></li><li class='xr-section-item'><input id='section-7ca4fd2b-21d8-4870-90f3-99afb6021867' class='xr-section-summary-in' type='checkbox'  ><label for='section-7ca4fd2b-21d8-4870-90f3-99afb6021867' class='xr-section-summary' >Indexes: <span>(3)</span></label><div class='xr-section-inline-details'></div><div class='xr-section-details'><ul class='xr-var-list'><li class='xr-var-item'><div class='xr-index-name'><div>ensemble</div></div><div class='xr-index-preview'>PandasIndex</div><div></div><input id='index-edb17b03-7dec-4cd1-bbad-9b0cb8c928f1' class='xr-index-data-in' type='checkbox'/><label for='index-edb17b03-7dec-4cd1-bbad-9b0cb8c928f1' title='Show/Hide index repr'><svg class='icon xr-icon-database'><use xlink:href='#icon-database'></use></svg></label><div class='xr-index-data'><pre>PandasIndex(Index([0], dtype=&#x27;int64&#x27;, name=&#x27;ensemble&#x27;))</pre></div></li><li class='xr-var-item'><div class='xr-index-name'><div>time</div></div><div class='xr-index-preview'>PandasIndex</div><div></div><input id='index-e72dcfb7-3eb3-4b8d-9c72-58e51f912ec0' class='xr-index-data-in' type='checkbox'/><label for='index-e72dcfb7-3eb3-4b8d-9c72-58e51f912ec0' title='Show/Hide index repr'><svg class='icon xr-icon-database'><use xlink:href='#icon-database'></use></svg></label><div class='xr-index-data'><pre>PandasIndex(DatetimeIndex([&#x27;1990-01-01&#x27;, &#x27;1990-01-02&#x27;, &#x27;1990-01-03&#x27;, &#x27;1990-01-04&#x27;,
               &#x27;1990-01-05&#x27;, &#x27;1990-01-06&#x27;, &#x27;1990-01-07&#x27;, &#x27;1990-01-08&#x27;,
               &#x27;1990-01-09&#x27;, &#x27;1990-01-10&#x27;,
               ...
               &#x27;2005-12-22&#x27;, &#x27;2005-12-23&#x27;, &#x27;2005-12-24&#x27;, &#x27;2005-12-25&#x27;,
               &#x27;2005-12-26&#x27;, &#x27;2005-12-27&#x27;, &#x27;2005-12-28&#x27;, &#x27;2005-12-29&#x27;,
               &#x27;2005-12-30&#x27;, &#x27;2005-12-31&#x27;],
              dtype=&#x27;datetime64[ns]&#x27;, name=&#x27;time&#x27;, length=5844, freq=&#x27;D&#x27;))</pre></div></li><li class='xr-var-item'><div class='xr-index-name'><div>variable_identifiers</div></div><div class='xr-index-preview'>PandasIndex</div><div></div><input id='index-e93171ef-5012-4b6f-b238-c99beaf3bac1' class='xr-index-data-in' type='checkbox'/><label for='index-e93171ef-5012-4b6f-b238-c99beaf3bac1' title='Show/Hide index repr'><svg class='icon xr-icon-database'><use xlink:href='#icon-database'></use></svg></label><div class='xr-index-data'><pre>PandasIndex(Index([&#x27;subarea.Subarea.E&#x27;, &#x27;subarea.Subarea.P&#x27;], dtype=&#x27;object&#x27;, name=&#x27;variable_identifiers&#x27;))</pre></div></li></ul></div></li><li class='xr-section-item'><input id='section-f322f832-13f8-45eb-841e-968d6aad638f' class='xr-section-summary-in' type='checkbox' disabled ><label for='section-f322f832-13f8-45eb-841e-968d6aad638f' class='xr-section-summary'  title='Expand/collapse section'>Attributes: <span>(0)</span></label><div class='xr-section-inline-details'></div><div class='xr-section-details'><dl class='xr-attrs'></dl></div></li></ul></div></div>



The C++ core has its own internal representation of time series. The Python package `swift2` uses generally [`xarray`](https://docs.xarray.dev/en/stable/) to represent time series, as it is particularly suited to handle ensemble of time series of dimensionality more than 2. The ensemble dimension is thus present by default in the returned array, even when there is only one realisation. This can be removed with the [`squeeze`](https://docs.xarray.dev/en/stable/generated/xarray.DataArray.squeeze.html#xarray.DataArray.squeeze) method of xarray. 


```python
tts = tts.squeeze(drop=True)
g = tts.plot.line(add_legend=True, figsize=(16,8), col="variable_identifiers", col_wrap=1, sharey=False)
g;
```


    
![png](getting_started_files/getting_started_25_0.png)
    



Many `swift2` python functions will however also accept [pandas](https://pandas.pydata.org/docs/) `DataFrame` or `Series` as input for time series when it makes sense to accept such time series representations.


```python
ms.play_input?
```

We can check with the `get_recorded_varnames` method that simulation object as not been "told" to record an output time series yet. 


```python
ms.get_recorded_varnames()
```




    []



SWIFT is designed to record model variables on demand in a highly flexible manner. First, we can query the system to find out known rainfall-runoff models, and the model variable names that we can record.


```python
runoff_model_ids()
```




    ['NetRainfall',
     'GR2M_MOD',
     'GR4J',
     'GR4J_SG',
     'GR5H',
     'GR6J',
     'GR5J',
     'PDM',
     'AWBM',
     'SACSMA',
     'SACSMA_NSW',
     'constant_outflow',
     'external',
     'WAPABA',
     'GRKAL',
     'SimHyd',
     'HBV']



The GR4J model has the following states that can be "listened to" and "recorded" on demand over a simulation.


```python
gr4j_model_vars = runoff_model_var_ids('GR4J')
print(gr4j_model_vars)
```

    ['P', 'E', 'En', 'LAI', 'runoff', 'S', 'R', 'TWS', 'Eactual', 'Ps', 'Es', 'Pr', 'ech1', 'ech2', 'Perc', 'alpha', 'k', 'x1', 'x2', 'x3', 'x4', 'UHExponent', 'PercFactor']


These are the variable names for a single GR4J model instance; since SWIFT is for semi-distributed models, we need to use a hierarchical naming scheme to uniquely identify model variables (even when in this case we do have only one subarea). Using unique keys allow to inspect the model states in great details if needed.


```python
ms.get_subarea_ids()
ms.get_state_value('subarea.Subarea.x4')
```




    {'subarea.Subarea.x4': 0.5}




Let's record to time series all the storage and flux states of GR4J (no need to record model parameters which will be flat lines here). We can use the utility function [`mk_full_data_id`](https://csiro-hydroinformatics.github.io/swift-py-doc/code-reference/?h=mk_full_data_id#swift2.utils.mk_full_data_id) for conciseness to vectorise the handling of multiple state identifiers.



```python
to_record = ['runoff', 'S', 'R', 'Ps', 'Es', 'Pr', 'ech1', 'ech2', 'Perc']
ids = mk_full_data_id('subarea', 'Subarea', to_record)
```


```python
ms.record_state(ids)
ms.get_recorded_varnames()
```




    ['subarea.Subarea.Es',
     'subarea.Subarea.Perc',
     'subarea.Subarea.Pr',
     'subarea.Subarea.Ps',
     'subarea.Subarea.R',
     'subarea.Subarea.S',
     'subarea.Subarea.ech1',
     'subarea.Subarea.ech2',
     'subarea.Subarea.runoff']



### Model execution

`ms` was configured to record model outputs, now we can execute the simulation, with its parameters set to whatever defaults it has. Note that `ms` also has a `check_simulation` method that can provide information about  obvious configuration issues when execution fails. Typically inconstent start and end dates between simulation and input time series. In this case, nothing is reported in this simple and preconfigured case.


```python
ms.check_simulation()
```




    {'errors': []}




```python
ms.exec_simulation()
```

### Model outputs


```python
var_series = ms.get_recorded()
```

We have a 3 dimensional data array, with 9 identifiers for state variables:


```python
var_series.dims, var_series.shape
```




    (('variable_identifiers', 'ensemble', 'time'), (9, 1, 5844))




```python
var_coords = var_series.coords['variable_identifiers'].values
var_coords
```




    array(['subarea.Subarea.Es', 'subarea.Subarea.Perc', 'subarea.Subarea.Pr',
           'subarea.Subarea.Ps', 'subarea.Subarea.R', 'subarea.Subarea.S',
           'subarea.Subarea.ech1', 'subarea.Subarea.ech2',
           'subarea.Subarea.runoff'], dtype=object)



The variable identifiers are fully qualified, which is fine and certainly make a lot of sense for semi-distributed catchments. But to visualise these for a single subarea we shall override with short model names:


```python
var_series.coords['variable_identifiers'] = np.array([x.replace('subarea.Subarea.', "") for x in var_coords])
```

### Visualising model states

Let's look at a shorter period of the output. We define a couple of functions to slice and plot the last three years of the time series, for clarity.


```python
def last_three_years(tts:xr.DataArray):
    start=tts.coords[TIME_DIMNAME].values[-(365*3)]
    end=tts.coords[TIME_DIMNAME].values[-1]
    return slice_xr_time_series(tts, start, end)

def plot_obs_vs_calc(obs, calc, ylab="runoff (mm)"):
    import uchronia.utils as uu
    obs = last_three_years(obs)
    calc = last_three_years(calc)
    both = uu.xr_concat([obs,calc], ['observed','calculated'], 'type')
    both.plot.line(add_legend=True, figsize=(9,4), hue="type")
    plt.ylabel(ylab)
```


```python
s = last_three_years(var_series)
# , main = 'Default GR4J output on MMH data')
```


```python
s = s.squeeze(drop=True)
```


```python
g = s.plot.line(add_legend=True, figsize=(16,16), col="variable_identifiers", col_wrap=2, sharey=False)
```


    
![png](getting_started_files/getting_started_54_0.png)
    



## Exploring the model interactively

### Assessing a change in the input series

As mentioned earlier, it is change to define the model simulation definition directly and interactively. The following shows how a to assign another input time series. We use a somewhat contrived example of a scaled up precipitation input series, to see what is the effect on the runoff.


```python
precip_id = 'subarea.Subarea.P'
runoff_id = 'subarea.Subarea.runoff'
precip = ms.get_played(precip_id)
baseline_runoff = ms.get_recorded(runoff_id)
```

Because we are about to work on a scenario, rather than modifying `ms` we are going to keep it as a clean baseline, and create a full "clone" of the catchment model. This is an understated feature of `swift2`, but a cornerstone of proper scenario comparison (and help limit modelling mistakes)


```python
ms_wetter = ms.clone()
```


```python
precip_scaled = precip * 1.1
precip_scaled = precip_scaled.squeeze(drop=True)
ms_wetter.play_input(precip_scaled, precip_id)
ms_wetter.exec_simulation()
runoff_diff = ms_wetter.get_recorded(runoff_id) - baseline_runoff
```


```python
runoff_diff = runoff_diff.squeeze(drop=True)
```

The additional runoff depth we get with a rainfall scaled up by 10 percent is:


```python
runoff_diff.plot(figsize=(9,4))
plt.title('Change in runoff with precipitations scaled up by 10%')
plt.ylabel('runoff depth change (mm/day)');
```


    
![png](getting_started_files/getting_started_62_0.png)
    


### Assessing the impact of a change in one model parameter



```python
x4_id = 'subarea.Subarea.x4'
x4 = ms.get_state_value(x4_id)
x4
```




    {'subarea.Subarea.x4': 0.5}



The returned value for $x_4$ is in a dictionary, because `get_state_value` is vectorised and can retrieve several state values at the same time. `set_state_value` on the other hand accepts multiple types of inputs including scalars for convenience:


```python
x4_inital = x4[x4_id]
# Again, keep the baseline clean and work on a copy
ms_x4 = ms.clone()

ms_x4.set_state_value(x4_id, x4_inital*1.1)
ms_x4.exec_simulation()
runoff_diff = ms_x4.get_recorded(runoff_id) - baseline_runoff
```

One effect of $x_4$ is on the lagging effect, so the difference in runoff should be overall near zero, but with local variations:  


```python
runoff_diff = runoff_diff.squeeze(drop=True)
blah = last_three_years(runoff_diff).plot.line()
plt.title('Change in runoff with x4 scaled up by 10%')
plt.ylabel('runoff depth change (mm/day)');
```


    
![png](getting_started_files/getting_started_68_0.png)
    



## Calibration

Let's now set up a calibration against the observed runoff depth for this data 'MMH', included as sample data in the package, and view it along the current default model runoff output.


```python
obs_runoff = sample_series('MMH', 'flow') #actually, runoff depth
```

Negative data in the observed streamflow is a code for missing data. It is better to use `np.nan` in Python for this.


```python
obs_runoff[obs_runoff < -1] = np.nan
obs_runoff = pd_series_to_xr_series(obs_runoff)
```

Let's view the default modelled output from **GR4J**, overlayed with the observation


```python
plot_obs_vs_calc(obs_runoff, baseline_runoff.squeeze(drop=True));
```


    
![png](getting_started_files/getting_started_74_0.png)
    


### Defining the calibration

Before we go ahead in setting up this calibration, it is worth outlining key aspects of software architecture in `swift2` and its [metaheuristics optimisation library, "wila"](https://github.com/csiro-hydroinformatics/wila) upfront.

At a high level a calibration process conceptually needs:

* the specification of a feasible parameter space $X = x_1, x_2, ..., x_n$, typically with feasible intervals for each $x_i$
* an objective evaluation $Obj(X)$
* and an optimisation algorithm that uses $Obj$ and evaluates it on parameter values $X_p$ sampled from $X$

Formulating a calibration in `swift2` follows this pattern. There is usually no need to explicitely handle the hydrological model, which is hidden behind $Obj$, and for some reasons this can be an unfamiliar viewpoint for many hydrologist.

Readers interesting in modelling and optimisation framework design and implementation can read [Talbi, El-Ghazali. Metaheuristics: from design to implementation. John Wiley & Sons, 2009.](https://dl.acm.org/doi/abs/10.5555/1718024) for a comprehensive overview.

Now let us see what these are in practice. 

**Note**: There are several time stamp representations in the Python ecosystem. A dependency package of the `swift2` package , **cinterop**, has a [time series module](https://cinterop.readthedocs.io/en/latest/timeseries-module/) with date-time and time series related utilities, such as `xr_ts_start`, `as_timestamp` to reduce the tedium of date-time handling. You may also already be using third-party utilities as well. 

#### Objective

Part of the information for the objective is over which time span we calculate the goodness of fit, usually different from the simulation length to leave period for a model warmup


```python
s = xr_ts_start(obs_runoff)
# Warmup:
w = as_timestamp(s) + pd.DateOffset(years=2)
e = xr_ts_end(obs_runoff)
ms.set_simulation_span(s, e)
```

We now have all the information needed to create a calibration objective using for instance the Nash-Sutcliffe Efficiency 


```python
objective = ms.create_objective(runoff_id, obs_runoff, 'NSE', w, e)
```

The variable `objective` now references an objective evaluator.


```python
type(objective), objective
```




    (swift2.classes.ObjectiveEvaluator,
     CFFI pointer handle to a native pointer of type id "OBJECTIVE_EVALUATOR_WILA_PTR")



An objective evaluator evaluates one or more goodness of fit (a.k.a. "scores") via the method `objective.get_score`. We need to provide a set of model parameters to evaluate the resulting scores. The utility function `get_free_params` provides a template for some models including **GR4J**, in the form of a pandas DataFrame

#### Feasible parameter space



```python
pspec_gr4j = get_free_params('GR4J')
pspec_gr4j
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
      <td>x1</td>
      <td>650.488000</td>
      <td>1.0</td>
      <td>3000.0</td>
    </tr>
    <tr>
      <th>1</th>
      <td>x2</td>
      <td>-0.280648</td>
      <td>-27.0</td>
      <td>27.0</td>
    </tr>
    <tr>
      <th>2</th>
      <td>x3</td>
      <td>7.891230</td>
      <td>1.0</td>
      <td>660.0</td>
    </tr>
    <tr>
      <th>3</th>
      <td>x4</td>
      <td>18.917200</td>
      <td>1.0</td>
      <td>240.0</td>
    </tr>
  </tbody>
</table>
</div>



We can set some values and min/max bounds in this data frame. The min/max bounds are important for the upcoming calibration process.


```python
pspec_gr4j.Value = [542.1981111,  -0.4127542,   7.7403390 ,  1.2388548]
pspec_gr4j.Min = [1,-30, 1,1]
pspec_gr4j.Max = [1000.0, 30, 1000, 240]
```


```python
pspec_gr4j
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
      <td>x1</td>
      <td>542.198111</td>
      <td>1</td>
      <td>1000.0</td>
    </tr>
    <tr>
      <th>1</th>
      <td>x2</td>
      <td>-0.412754</td>
      <td>-30</td>
      <td>30.0</td>
    </tr>
    <tr>
      <th>2</th>
      <td>x3</td>
      <td>7.740339</td>
      <td>1</td>
      <td>1000.0</td>
    </tr>
    <tr>
      <th>3</th>
      <td>x4</td>
      <td>1.238855</td>
      <td>1</td>
      <td>240.0</td>
    </tr>
  </tbody>
</table>
</div>



Our model states have the prefix 'subarea.Subarea.', so we need to use this prefix in our data frame of parameters as well.


```python
pspec_gr4j.Name = vpaste('subarea.Subarea.', pspec_gr4j.Name)
```

We can now create a parameteriser. It can be converted back to a data frame to check its content.

**Note**: we will be using the untransformed parameters for calibration for the sake of simplicity in this introductory material. In practice we should use some transformations to facilitate the calibration, and there are many features in **swift2** to do so.


```python
p = create_parameteriser('Generic', pspec_gr4j)
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
      <td>1.0</td>
      <td>1000.0</td>
    </tr>
    <tr>
      <th>1</th>
      <td>subarea.Subarea.x2</td>
      <td>-0.412754</td>
      <td>-30.0</td>
      <td>30.0</td>
    </tr>
    <tr>
      <th>2</th>
      <td>subarea.Subarea.x3</td>
      <td>7.740339</td>
      <td>1.0</td>
      <td>1000.0</td>
    </tr>
    <tr>
      <th>3</th>
      <td>subarea.Subarea.x4</td>
      <td>1.238855</td>
      <td>1.0</td>
      <td>240.0</td>
    </tr>
  </tbody>
</table>
</div>



Now let us check that we can indeed evaluate the goodness of fit for this parameteriser `p` using the `objective`: 


```python
score = objective.get_score(p)
score
```




    {'scores': {'NSE': -2.3381787784819057},
     'sysconfig':                  Name       Value   Min     Max
     0  subarea.Subarea.x1  542.198111   1.0  1000.0
     1  subarea.Subarea.x2   -0.412754 -30.0    30.0
     2  subarea.Subarea.x3    7.740339   1.0  1000.0
     3  subarea.Subarea.x4    1.238855   1.0   240.0}



Our calibration objective calculator is structurally valid.

#### Optimiser

To create an optimiser, we need to specify a termination criterion. There are several options available to control when an optimisation process will finish in a calibration. One of them uses the standard deviation of parameter values for population based algorithms such as the shuffled complex evolution algorithm (SCE). We can specify that the optimisation has converged once the standard deviation of each parameter (x1, x2, etc. for GR4J) is within 


```python
term = create_sce_termination_wila('relative standard deviation', ['0.002','0.0167'])
```


```python
sce_params = get_default_sce_parameters()
urs = create_parameter_sampler(0, p, 'urs')
optimiser = objective.create_sce_optim_swift(term, sce_params, urs)
```


```python
optimiser.set_calibration_logger('')
```


```python
%%time
calib_results = optimiser.execute_optimisation()
```

    CPU times: user 21.7 s, sys: 42.8 ms, total: 21.7 s
    Wall time: 4.31 s


**swift** uses optimization tools that will parallelize model simulation runs if possible (i.e. if supported by the model). This may not be noticeable in this instance, but is important to scale up to larger catchment models. 

## Assessing the optimisation

There are facilities in the package to extract, exploit and visualise the optimisation log information.



```python
opt_log = optimiser.extract_optimisation_log(fitness_name = "NSE")
```


```python
opt_log.data.head()
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
      <th>subarea.Subarea.x1</th>
      <th>subarea.Subarea.x2</th>
      <th>subarea.Subarea.x3</th>
      <th>subarea.Subarea.x4</th>
      <th>PointNumber</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>Initial Population</td>
      <td></td>
      <td>Initial Population</td>
      <td>-1339.285380</td>
      <td>947.690750</td>
      <td>23.005202</td>
      <td>62.217181</td>
      <td>161.886443</td>
      <td>1</td>
    </tr>
    <tr>
      <th>1</th>
      <td>Initial Population</td>
      <td></td>
      <td>Initial Population</td>
      <td>-0.890844</td>
      <td>174.551633</td>
      <td>-7.280393</td>
      <td>710.469274</td>
      <td>96.390541</td>
      <td>2</td>
    </tr>
    <tr>
      <th>2</th>
      <td>Initial Population</td>
      <td></td>
      <td>Initial Population</td>
      <td>-0.327150</td>
      <td>214.709001</td>
      <td>-7.069954</td>
      <td>124.638641</td>
      <td>18.990489</td>
      <td>3</td>
    </tr>
    <tr>
      <th>3</th>
      <td>Initial Population</td>
      <td></td>
      <td>Initial Population</td>
      <td>-2.367463</td>
      <td>724.720289</td>
      <td>6.659042</td>
      <td>930.609993</td>
      <td>207.726829</td>
      <td>4</td>
    </tr>
    <tr>
      <th>4</th>
      <td>Initial Population</td>
      <td></td>
      <td>Initial Population</td>
      <td>-913.046415</td>
      <td>874.130073</td>
      <td>28.643820</td>
      <td>126.360349</td>
      <td>83.693269</td>
      <td>5</td>
    </tr>
  </tbody>
</table>
</div>




```python
opt_log.data.tail()
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
      <th>subarea.Subarea.x1</th>
      <th>subarea.Subarea.x2</th>
      <th>subarea.Subarea.x3</th>
      <th>subarea.Subarea.x4</th>
      <th>PointNumber</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>13967</th>
      <td>Shuffling No 28</td>
      <td></td>
      <td>Shuffling No 28</td>
      <td>0.768667</td>
      <td>999.096491</td>
      <td>-5.620413</td>
      <td>91.829530</td>
      <td>1.000574</td>
      <td>13968</td>
    </tr>
    <tr>
      <th>13968</th>
      <td>Shuffling No 28</td>
      <td></td>
      <td>Shuffling No 28</td>
      <td>0.768742</td>
      <td>996.688456</td>
      <td>-5.679336</td>
      <td>93.670035</td>
      <td>1.000339</td>
      <td>13969</td>
    </tr>
    <tr>
      <th>13969</th>
      <td>Shuffling No 28</td>
      <td></td>
      <td>Shuffling No 28</td>
      <td>0.768590</td>
      <td>995.813747</td>
      <td>-5.731252</td>
      <td>95.427583</td>
      <td>1.000443</td>
      <td>13970</td>
    </tr>
    <tr>
      <th>13970</th>
      <td>Shuffling No 28</td>
      <td></td>
      <td>Shuffling No 28</td>
      <td>0.768553</td>
      <td>994.549300</td>
      <td>-5.677011</td>
      <td>96.570436</td>
      <td>1.000202</td>
      <td>13971</td>
    </tr>
    <tr>
      <th>13971</th>
      <td>Shuffling No 28</td>
      <td></td>
      <td>Best point in shuffle</td>
      <td>0.768844</td>
      <td>997.616573</td>
      <td>-5.649821</td>
      <td>92.890522</td>
      <td>1.000003</td>
      <td>13972</td>
    </tr>
  </tbody>
</table>
</div>



Let's subset the data points to keep a subset, the points from the initial population and SCE geometric transformations (reflection, contraction, addition). We can use a regular expression pattern to do so. `MhData` is a glorified data frame, but its methods are handy to reduce tedium.


```python
geom_ops = opt_log.subset_by_message(pattern= 'Initial.*|Reflec.*|Contrac.*|Add.*') # same as default argument, but to be explicit
```

Let us also rename the column names without the fully qualified prefix


```python
p_var_ids = ['x1','x2','x3','x4']
remap = {f'subarea.Subarea.{name}': name for name in p_var_ids}
geom_ops.rename_columns(remap)
```

### Visualising the optimisation process


```python
from swift2.vis import OptimisationPlots

v = OptimisationPlots(geom_ops)
```

We can see that at least one of the parameters, namely "x1", settled at its upper boundary of 1000:


```python
g = v.parameter_evolution(p_var_ids[0], obj_lims=[0,1])
plt.gcf().set_size_inches(10,8);
```


    
![png](getting_started_files/getting_started_108_0.png)
    


Note that the parameter x4 also seems to have settled at its lower bound:


```python
v.parameter_evolution(p_var_ids[3], obj_lims=[0,1])
plt.gcf().set_size_inches(10,8);
```


    
![png](getting_started_files/getting_started_110_0.png)
    


x4 influences the unit hydrograph, and the meaning of this parameter depends on the time step of the input series. It may be justified in this case to go below 1 for its lower bound. Also, the default maximum value 240 is typically sensible for use with hourly data, not daily, so we may want to reduce this maximum. 

So let's restart the calibration, with a larger upper bound for the x1 parameter, and adjusted x4 bounds as well:


```python
pspec_gr4j.Max = [2500, 30, 1000, 10]
pspec_gr4j.Min = [1,-30, 1,0.2]
```


```python
p = create_parameteriser('Generic', pspec_gr4j)
urs = create_parameter_sampler(0, p, 'urs')
optimiser = objective.create_sce_optim_swift(term, sce_params, urs)
calib_logger = optimiser.set_calibration_logger('')
calib_results = optimiser.execute_optimisation()
opt_log = optimiser.extract_optimisation_log(fitness_name = "NSE")
```


```python
geom_ops = opt_log.subset_by_message(pattern= 'Initial.*|Reflec.*|Contrac.*|Add.*') # same as default argument, but to be explicit
```


```python
p_var_ids = ['x1','x2','x3','x4']
remap = {f'subarea.Subarea.{name}': name for name in p_var_ids}
geom_ops.rename_columns(remap)
```

Let's check that the parameter does not settle at the boundary anymore:


```python
v = OptimisationPlots(geom_ops)
g = v.parameter_evolution(p_var_ids[0], obj_lims=[0,1])
plt.gcf().set_size_inches(10,8);
```


    
![png](getting_started_files/getting_started_118_0.png)
    



```python
v.parameter_evolution(p_var_ids[3], obj_lims=[0,1])
plt.gcf().set_size_inches(10,8);
```


    
![png](getting_started_files/getting_started_119_0.png)
    


_Note_: There are a few additional visualisation options in the R package [**mhplot**](https://github.com/csiro-hydroinformatics/mhplot) that may be ported to python as needed.

We can inspect further the behavior of the SCE optimiser by using facetted plots with the package **seaborn**.


```python
df = geom_ops.data
```


```python
grid = geom_ops.facet_plot(p_var_ids[0])
```


    
![png](getting_started_files/getting_started_122_0.png)
    


Let's retrieve the parameter set with the best NSE, and see the resulting runoff time series. `calib_results` is a native C++ object, but its wrapper has functions to query it and extract the information wanted.


`calib_results` is the final population of parameter sets. To get the best score within it (i.e. the best fitness and associated parameters), we can use: 


```python
best_pset = calib_results.get_best_score('NSE')
```


```python
best_pset
```




    CFFI pointer handle to a native pointer of type id "OBJECTIVE_SCORES_WILA_PTR"
    
    Scores:
    
    {'NSE': 0.7832225081975563}
    
    Parameters:
    
                     Name        Value   Min     Max
    0  subarea.Subarea.x1  1141.419555   1.0  2500.0
    1  subarea.Subarea.x2    -5.448833 -30.0    30.0
    2  subarea.Subarea.x3    97.579250   1.0  1000.0
    3  subarea.Subarea.x4     0.414422   0.2    10.0




```python
opt_log.data.tail()
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
      <th>subarea.Subarea.x1</th>
      <th>subarea.Subarea.x2</th>
      <th>subarea.Subarea.x3</th>
      <th>subarea.Subarea.x4</th>
      <th>PointNumber</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>8697</th>
      <td>Shuffling No 17</td>
      <td></td>
      <td>Shuffling No 17</td>
      <td>0.783221</td>
      <td>1136.271566</td>
      <td>-5.462186</td>
      <td>97.798741</td>
      <td>0.425679</td>
      <td>8698</td>
    </tr>
    <tr>
      <th>8698</th>
      <td>Shuffling No 17</td>
      <td></td>
      <td>Shuffling No 17</td>
      <td>0.783220</td>
      <td>1140.838174</td>
      <td>-5.423250</td>
      <td>97.721428</td>
      <td>0.397216</td>
      <td>8699</td>
    </tr>
    <tr>
      <th>8699</th>
      <td>Shuffling No 17</td>
      <td></td>
      <td>Shuffling No 17</td>
      <td>0.783218</td>
      <td>1138.591759</td>
      <td>-5.473618</td>
      <td>98.148408</td>
      <td>0.418075</td>
      <td>8700</td>
    </tr>
    <tr>
      <th>8700</th>
      <td>Shuffling No 17</td>
      <td></td>
      <td>Shuffling No 17</td>
      <td>0.783215</td>
      <td>1151.965067</td>
      <td>-5.400726</td>
      <td>96.862435</td>
      <td>0.463490</td>
      <td>8701</td>
    </tr>
    <tr>
      <th>8701</th>
      <td>Shuffling No 17</td>
      <td></td>
      <td>Best point in shuffle</td>
      <td>0.783223</td>
      <td>1141.419555</td>
      <td>-5.448833</td>
      <td>97.579250</td>
      <td>0.414422</td>
      <td>8702</td>
    </tr>
  </tbody>
</table>
</div>



## Time series visualisation

Let's apply this parameter to the original simulation, and execute it to get output runoff.

Note, as an aside, that below for didactic purposes we see only the last 3 years of time series, while the NSE score is calculated over several more years. As it happens, the runoff prediction has a systematic negative bias over these three particular years.



```python
best_pset.apply_sys_config(ms)
ms.exec_simulation()
plot_obs_vs_calc(obs_runoff, ms.get_recorded(runoff_id).squeeze(drop=True))
plt.show()
```


    
![png](getting_started_files/getting_started_129_0.png)
    


Looking at the whole series over the simulation, indeed these last three years appear untypical in terms of match between observed and calculated


```python
from swift2.vis import plot_two_series
```


```python
plot_two_series(obs_runoff, ms.get_recorded(runoff_id).squeeze(drop=True), names = ['observed','calculated'])
```


    
![png](getting_started_files/getting_started_132_0.png)
    



```python

```
