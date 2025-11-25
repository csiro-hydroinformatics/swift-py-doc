# Module vis

# vis

Classes:

- **`OptimisationPlots`** –

Functions:

- **`plot_series`** –
- **`plot_two_series`** –

## OptimisationPlots

```
OptimisationPlots(optim_geom: MhData)
```

Methods:

- **`parameter_evolution`** –
- **`shuffles`** – Facetted bi-parameter scatter plots of the value of a parameter along the optimisation process

### parameter_evolution

```
parameter_evolution(param_name: str, obj_lims: Sequence[float] = None, title: str = 'Evolution of parameter values', xlab='Logged point', ylab=None, **kwargs)
```

### shuffles

```
shuffles(x: str, y: str, obj_lims: Sequence[float] = None) -> Any
```

Facetted bi-parameter scatter plots of the value of a parameter along the optimisation process

Plot the value of a parameter along the optimisation process. The color scale is the objective score. Useful to check the behavior of the optimisation process.

Parameters:

- **`x`** (`str`) – the exact name of one of the model parameters
- **`y`** (`str`) – the exact name of a second model parameter
- **`obj_lims`** (`Sequence[float]`, default: `None` ) – min/max limits to plot the fitness, for example min 0 for NSE. Defaults to None.

Returns:

- `Any` – sns.FacetGrid: FacetGrid object

## plot_series

```
plot_series(a: DataArray, start_time=None, end_time=None, name: str = None, xlab='time', ylab=None, title=None, **kwargs)
```

## plot_two_series

```
plot_two_series(a: DataArray, b: DataArray, start_time=None, end_time=None, names: Sequence[str] = None, xlab='time', ylab=None, title=None, figsize=(16, 9), **kwargs)
```
