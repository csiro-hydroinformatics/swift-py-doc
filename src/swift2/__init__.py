"""Tools for manipulating LakeOneD models and data and for running
   SWIFT from Python."""

# IMPORTANT
# it is critical to trigger the import of the uchronia (datatypes) native library BEFORE
# that of swift, at least on Linux Debian.
# If not there are some puzzling behavior in API calls that use
# upcast of opaque external pointers (e.g. passing a COMPOSITE_PARAMETERIZER_PTR to an API
# function that accepts HYPERCUBE_PTR)
# Candidate fix for https://jira.csiro.au/projects/WIRADA/issues/WIRADA-640 is thus:
import uchronia

# Trigger the loading of the native library.
import swift2.wrap.ffi_interop as _interop

# Trigger the initialisation of the custom wrapper generation function.
import swift2.classes as _s

from ._version import __version__
