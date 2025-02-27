# Python swift2 documentation

**swift2** is a python package for short-term streamflow forcasting with uncertainty quantification, as well as traditional hydrology model simulations. The python package is a wrapper around a high-performance C`++` core. See [this site](https://csiro-hydroinformatics.github.io/streamflow-forecasting-tools-onboard/) for more context.

This present documentation includes two types of information:

* example modelling workflows (from jupyter notebooks) under the _Notebooks_ tab
* an API documentation under the _Submodules_ tab.

## Installation

See the [installation section of the onboarding guide for streamflow forecasting software tools](https://csiro-hydroinformatics.github.io/streamflow-forecasting-tools-onboard/installation.html)

## License

The swift2 python package itself is licensed with the [BSD 3-Clause Licence](./license.md)

## Source code

The python package `swift2` itself is [open source](./license.md), and this present documentation include source code. But the python package accesses `C++` code that, for many reasons, is closed source. As of 2025-01 the reference source code remain at [this repository](https://bitbucket.csiro.au/projects/SF/repos/swift/browse/bindings/python/swift2?at=refs%2Fheads%2Ftesting).
