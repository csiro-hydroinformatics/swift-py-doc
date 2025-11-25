# Module model_definitions

# model_definitions

Functions:

- **`cookie_cut_dendritic_catchment`** – cookie cut a dendritic catchment (without confluences)
- **`get_catchment_structure`** – Gets the essential connective structure of a catchment
- **`model_from_json_file`** – Create a model simulation from a file with a JSON serialisation.
- **`model_to_json_file`** – Save a model simulation from a file with a JSON serialisation.
- **`split_to_subcatchments`** – Split a catchment in subcatchments, given a list of node/link element identifiers
- **`subset_catchment`** – Subsets a catchment, keeping only a portion above or below a node, link or subarea.

## cookie_cut_dendritic_catchment

```
cookie_cut_dendritic_catchment(simulation: Simulation, bottom_element_id: str, top_element_ids: VecStr) -> Simulation
```

cookie cut a dendritic catchment (without confluences)

Parameters:

- **`simulation`** (`Simulation`) – base catchment simulation
- **`bottom_element_id`** (`str`) – identifier of the most downstream element to keep
- **`top_element_ids`** (`str`) – identifier(s) of the most upstream element(s) to keep

Returns:

- **`Simulation`** ( `Simulation` ) – a subcatchment simulation, cookie cut from the base simulation. Deep clone of objects.

## get_catchment_structure

```
get_catchment_structure(simulation) -> Dict
```

Gets the essential connective structure of a catchment

Parameters:

- **`simulation`** (`Simulation`) – base catchment simulation

Returns:

- `Dict` –

Examples:

```
>>> _, simulation = sdh.create_test_catchment_structure()
>>> smd.get_catchment_structure(simulation)
{'Node':    Id     Name
0  n1  n1_name
1  n2  n2_name
2  n3  n3_name
3  n4  n4_name
4  n5  n5_name
5  n6  n6_name, 'Link':      Id       Name  LengthMetres    f  ManningsN  Slope
0  lnk1  lnk1_name           0.0  0.0        0.0    0.0
1  lnk2  lnk2_name           0.0  0.0        0.0    0.0
2  lnk3  lnk3_name           0.0  0.0        0.0    0.0
3  lnk4  lnk4_name           0.0  0.0        0.0    0.0
4  lnk5  lnk5_name           0.0  0.0        0.0    0.0, 'Subarea':      Id       Name  AreaKm2
0  lnk1  lnk1_name      1.1
1  lnk2  lnk2_name      2.2
2  lnk3  lnk3_name      3.3
3  lnk4  lnk4_name      4.4
4  lnk5  lnk5_name      5.5, 'NodeLink':   DownstreamId UpstreamId LinkId
0           n6         n2   lnk1
1           n2         n5   lnk2
2           n2         n4   lnk3
3           n4         n3   lnk4
4           n4         n1   lnk5, 'SubareaLink':   LinkId SubareaId
0   lnk1      lnk1
1   lnk2      lnk2
2   lnk3      lnk3
3   lnk4      lnk4
```

## model_from_json_file

```
model_from_json_file(file_path: str) -> Simulation
```

Create a model simulation from a file with a JSON serialisation.

Parameters:

- **`file_path`** (`str`) – valid file path.

Returns:

- **`Simulation`** ( `Simulation` ) – a catchment simulation.

## model_to_json_file

```
model_to_json_file(simulation: Simulation, file_path: str) -> None
```

Save a model simulation from a file with a JSON serialisation.

Parameters:

- **`simulation`** (`Simulation`) – Catchment simulation
- **`file_path`** (`str`) – file path to save to

## split_to_subcatchments

```
split_to_subcatchments(simulation, split_element_ids, include_upstream=None) -> OrderedDict[str, Simulation]
```

Split a catchment in subcatchments, given a list of node/link element identifiers

Parameters:

- **`simulation`** (`Simulation`) – base catchment simulation
- **`split_element_ids`** (`str`) – element identifiers such as 'node.n1', 'link.linkId_2'
- **`include_upstream`** (`bool`, default: `None` ) – indicates whether for each element in split_element_ids it should be including in the upstream portion of the subcatchment. Defaults to None.

Returns:

- **`OrderedDict`** ( `OrderedDict[str, Simulation]` ) – list of subcatchments resulting from the split

Examples:

```
>>> _, simulation = sdh.create_test_catchment_structure()
>>> e_ids = ['node.n2', 'node.n4']
>>> sub_sims = smd.split_to_subcatchments(simulation, e_ids)
>>>
>>> for k in sub_sims:
...     print(k)
...     print(sub_sims[k].get_node_ids())
...     print(sub_sims[k].get_node_names())
...
node.n4
['n4', 'n3', 'n1']
['n4_name', 'n3_name', 'n1_name']
node.n2
['n2', 'n5']
['n2_name', 'n5_name']
remainder
['n6']
['n6_name']
```

## subset_catchment

```
subset_catchment(simulation: Simulation, element_id: str, action: str = 'keep_above') -> Simulation
```

Subsets a catchment, keeping only a portion above or below a node, link or subarea.

Parameters:

- **`simulation`** (`Simulation`) – an S4 object 'ExternalObjRef' [package "cinterop"] with external pointer type "MODEL_SIMULATION_PTR"
- **`element_id`** (`str`) – id of the element to cut at.
- **`action`** (`str`, default: `'keep_above'` ) – how to cut; currently limited to 'keep_above'

Returns:

- **`Simulation`** ( `Simulation` ) – a subcatchment simulation, cookie cut from the base simulation. Deep clone of objects.
