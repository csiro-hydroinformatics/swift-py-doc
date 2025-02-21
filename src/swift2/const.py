from typing import Any, Callable, Sequence, Union, TYPE_CHECKING

from uchronia.const import Scalar, VecNum, VecScalars, VecStr

CATCHMENT_FLOWRATE_VARID = "Catchment.StreamflowRate"

from typing_extensions import TypeAlias 

if TYPE_CHECKING:
    from uchronia.classes import (
        TimeSeriesLibrary,
    )
    from swift2.classes import (
        Simulation,
        EnsembleSimulation,
        EnsembleForecastSimulation,
    )

    RecordToSignature: TypeAlias = Callable[[Any, VecStr, TimeSeriesLibrary, VecStr, int], None]
    NdSimulation: TypeAlias = Union[Simulation, EnsembleSimulation, EnsembleForecastSimulation]
