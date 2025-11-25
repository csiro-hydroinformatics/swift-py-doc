# Module const

# const

Attributes:

- **`CATCHMENT_FLOWRATE_VARID`** –
- **`NdSimulation`** (`TypeAlias`) –
- **`RecordToSignature`** (`TypeAlias`) –

## CATCHMENT_FLOWRATE_VARID

```
CATCHMENT_FLOWRATE_VARID = 'Catchment.StreamflowRate'
```

## NdSimulation

```
NdSimulation: TypeAlias = Union[Simulation, EnsembleSimulation, EnsembleForecastSimulation]
```

## RecordToSignature

```
RecordToSignature: TypeAlias = Callable[[Any, VecStr, TimeSeriesLibrary, VecStr, int], None]
```
