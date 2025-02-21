from typing import Any, Sequence
import numpy as np
import pandas as pd
from swift2.utils import as_xarray_series
import xarray as xr

from cinterop.timeseries import as_timestamp
import matplotlib.pyplot as plt


def plot_two_series(
    a: xr.DataArray,
    b: xr.DataArray,
    start_time=None,
    end_time=None,
    names: Sequence[str] = None,
    xlab="time",
    ylab=None,
    title=None,
    **kwargs
):
    a = as_xarray_series(a)
    b = as_xarray_series(b)
    _, ax = plt.subplots(figsize=(16, 9))
    a = a.squeeze(drop=True)
    b = b.squeeze(drop=True)
    if start_time is not None:
        start_time = as_timestamp(start_time)
        end_time = as_timestamp(end_time)
        s = slice(start_time, end_time)
        a = a.sel(time=s)
        b = b.sel(time=s)
    if names is None:
        names = ["First series", "Second series"]
    ax.plot(a.time.values, a, linewidth=2, label=names[0])
    ax.plot(b.time.values, b, linewidth=2, label=names[1])
    ax.legend()
    if xlab is not None:
        ax.set_xlabel(xlab)
    if ylab is not None:
        ax.set_ylabel(ylab)
    if title is not None:
        ax.set_title(title)
    plt.show()


def plot_series(
    a: xr.DataArray,
    start_time=None,
    end_time=None,
    name: str = None,
    xlab="time",
    ylab=None,
    title=None,
    **kwargs
):
    a = as_xarray_series(a)
    _, ax = plt.subplots(figsize=(16, 9))
    a = a.squeeze(drop=True)
    if start_time is not None:
        start_time = as_timestamp(start_time)
        end_time = as_timestamp(end_time)
        s = slice(start_time, end_time)
        a = a.sel(time=s)
    if name is None:
        name = "First series"
    ax.plot(a.time.values, a, linewidth=2, label=name)
    ax.legend()
    if xlab is not None:
        ax.set_xlabel(xlab)
    if ylab is not None:
        ax.set_ylabel(ylab)
    if title is not None:
        ax.set_title(title)
    plt.show()


from swift2.parameteriser import MhData
import seaborn as sns


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
