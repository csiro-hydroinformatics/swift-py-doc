# Module vis

## `OptimisationPlots`

Source code in `.venv/lib/python3.13/site-packages/swift2/vis.py`

```
class OptimisationPlots:
    def __init__(self, optim_geom: MhData) -> None:
        self._optim_geom = optim_geom

    def parameter_evolution(
        self,
        param_name: str,
        obj_lims: Sequence[float] = None,
        title: str = "Evolution of parameter values",
        xlab="Logged point",
        ylab=None,
        **kwargs
    ):
        d = self._optim_geom.bound_fitness(obj_lims)
        if ylab is None:
            ylab = param_name
        ax = d.plot.scatter(
            x="PointNumber",
            y=param_name,
            c=self._optim_geom._fitness,
            colormap="viridis",
            **kwargs
        )
        if xlab is not None:
            ax.set_xlabel(xlab)
        if ylab is not None:
            ax.set_ylabel(ylab)
        if title is not None:
            ax.set_title(title)
        return ax

    def shuffles(self, x: str, y: str, obj_lims: Sequence[float] = None) -> Any:
        """Facetted bi-parameter scatter plots of the value of a parameter along the optimisation process

        Plot the value of a parameter along the optimisation process.
        The color scale is the objective score. Useful to check the behavior of the optimisation process.

        Args:
            x (str): the exact name of one of the model parameters
            y (str): the exact name of a second model parameter
            obj_lims (Sequence[float], optional): min/max limits to plot the fitness, for example min 0 for NSE. Defaults to None.

        Returns:
            sns.FacetGrid: FacetGrid object
        """
        import matplotlib.pyplot as plt

        d = self._optim_geom.bound_fitness(obj_lims)
        # matplotlib makes it difficult to use continuous color scales for num values...
        # https://stackoverflow.com/a/44642014/2752565
        g = sns.FacetGrid(
            d,
            col=self._optim_geom._categories,
            hue=self._optim_geom._fitness,
            col_wrap=3,
        )

        def facet_scatter(x, y, c, **kwargs):
            """Draw scatterplot with point colors from a faceted DataFrame columns."""
            kwargs.pop("color")
            plt.scatter(x, y, c=c, **kwargs)

        values = d[self._optim_geom._fitness].values
        vmin, vmax = np.min(values), np.max(values)
        # cmap = sns.diverging_palette(240, 10, l=65, center="light", as_cmap=True)
        cmap = sns.color_palette(
            palette="viridis", n_colors=None, desat=None, as_cmap=True
        )

        g = g.map(
            facet_scatter,
            x,
            y,
            self._optim_geom._fitness,
            s=100,
            alpha=0.5,
            vmin=vmin,
            vmax=vmax,
            cmap=cmap,
        )

        # Make space for the colorbar
        g.fig.subplots_adjust(right=0.92)

        # Define a new Axes where the colorbar will go
        cax = g.fig.add_axes([0.94, 0.25, 0.02, 0.6])

        # Get a mappable object with the same colormap as the data
        points = plt.scatter([], [], c=[], vmin=vmin, vmax=vmax, cmap=cmap)

        # Draw the colorbar
        g.fig.colorbar(points, cax=cax)

        g.fig.set_size_inches(15, 10)  # Sorry, only silly imperial units available
        # grid.add_legend()
        return g

```

### `shuffles(x, y, obj_lims=None)`

Facetted bi-parameter scatter plots of the value of a parameter along the optimisation process

Plot the value of a parameter along the optimisation process. The color scale is the objective score. Useful to check the behavior of the optimisation process.

Parameters:

| Name | Type | Description | Default | | --- | --- | --- | --- | | `x` | `str` | the exact name of one of the model parameters | *required* | | `y` | `str` | the exact name of a second model parameter | *required* | | `obj_lims` | `Sequence[float]` | min/max limits to plot the fitness, for example min 0 for NSE. Defaults to None. | `None` |

Returns:

| Type | Description | | --- | --- | | `Any` | sns.FacetGrid: FacetGrid object |

Source code in `.venv/lib/python3.13/site-packages/swift2/vis.py`

```
def shuffles(self, x: str, y: str, obj_lims: Sequence[float] = None) -> Any:
    """Facetted bi-parameter scatter plots of the value of a parameter along the optimisation process

    Plot the value of a parameter along the optimisation process.
    The color scale is the objective score. Useful to check the behavior of the optimisation process.

    Args:
        x (str): the exact name of one of the model parameters
        y (str): the exact name of a second model parameter
        obj_lims (Sequence[float], optional): min/max limits to plot the fitness, for example min 0 for NSE. Defaults to None.

    Returns:
        sns.FacetGrid: FacetGrid object
    """
    import matplotlib.pyplot as plt

    d = self._optim_geom.bound_fitness(obj_lims)
    # matplotlib makes it difficult to use continuous color scales for num values...
    # https://stackoverflow.com/a/44642014/2752565
    g = sns.FacetGrid(
        d,
        col=self._optim_geom._categories,
        hue=self._optim_geom._fitness,
        col_wrap=3,
    )

    def facet_scatter(x, y, c, **kwargs):
        """Draw scatterplot with point colors from a faceted DataFrame columns."""
        kwargs.pop("color")
        plt.scatter(x, y, c=c, **kwargs)

    values = d[self._optim_geom._fitness].values
    vmin, vmax = np.min(values), np.max(values)
    # cmap = sns.diverging_palette(240, 10, l=65, center="light", as_cmap=True)
    cmap = sns.color_palette(
        palette="viridis", n_colors=None, desat=None, as_cmap=True
    )

    g = g.map(
        facet_scatter,
        x,
        y,
        self._optim_geom._fitness,
        s=100,
        alpha=0.5,
        vmin=vmin,
        vmax=vmax,
        cmap=cmap,
    )

    # Make space for the colorbar
    g.fig.subplots_adjust(right=0.92)

    # Define a new Axes where the colorbar will go
    cax = g.fig.add_axes([0.94, 0.25, 0.02, 0.6])

    # Get a mappable object with the same colormap as the data
    points = plt.scatter([], [], c=[], vmin=vmin, vmax=vmax, cmap=cmap)

    # Draw the colorbar
    g.fig.colorbar(points, cax=cax)

    g.fig.set_size_inches(15, 10)  # Sorry, only silly imperial units available
    # grid.add_legend()
    return g

```
