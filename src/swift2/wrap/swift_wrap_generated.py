##################
# 
# *** THIS FILE IS GENERATED ****
# DO NOT MODIFY IT MANUALLY, AS YOU ARE VERY LIKELY TO LOSE WORK
# 
##################

import xarray as xr
import pandas as pd
import numpy as np
from typing import TYPE_CHECKING, Dict, List, Tuple, Any, Optional
from datetime import datetime
from refcount.interop import CffiData, OwningCffiNativeHandle, DeletableCffiNativeHandle, wrap_as_pointer_handle
from cinterop.cffi.marshal import as_bytes, TimeSeriesGeometryNative
from swift2.wrap.ffi_interop import marshal, swift_so
# phase out importing from swift2.classes, to prevent cyclic imports
# from swift2.classes import wrap_cffi_native_handle
# Additional specific imports for this package

from swift2.wrap.ffi_interop import to_multi_statistic_definition
import swift2.wrap.ffi_interop as _s_wrap


if TYPE_CHECKING:
    from swift2.classes import (
        Simulation,
        EnsembleSimulation,
        HypercubeParameteriser,
        CompositeParameteriser,
        FunctionsParameteriser,
        FilteringParameteriser,
        ObjectiveEvaluator,
        StateInitParameteriser,
        TransformParameteriser,
        ConstraintParameteriser,
        ScalingParameteriser,
        Optimiser,
        SceTerminationCondition,
        CandidateFactorySeed,
        ObjectiveScores,
        VectorObjectiveScores,
        ErrisStagedCalibration,
        MaerrisStagedCalibration,
        StateInitialiser,
        MemoryStates,
        EnsembleForecastSimulation,
    )
    from uchronia.classes import (
        EnsembleTimeSeries,
        TimeSeriesLibrary,
        EnsembleForecastTimeSeries,
        TimeSeries,
        EnsemblePtrTimeSeries,
        TimeSeriesProvider,
    )

    from refcount.interop import WrapperCreationFunction

__wrap_cffi_native_handle:Optional['WrapperCreationFunction']=None

def set_wrap_cffi_native_handle(wrapper_function:'WrapperCreationFunction'):
    global __wrap_cffi_native_handle
    __wrap_cffi_native_handle = wrapper_function

def custom_wrap_cffi_native_handle(obj, type_id='', release_native = None):
    '''Create a wrapper around a cffi pointer (if this is one), 
    with the suitable native release function call specific to this external pointer. 
    '''
    if __wrap_cffi_native_handle is None:
        raise RuntimeError('The function creating custom wrappers around native objects is None: you must use set_wrap_cffi_native_handle to initialise it')
    if release_native is None:
        release_native = dispose_shared_pointer_py
    return __wrap_cffi_native_handle(obj, type_id, release_native)

def charp_array_to_py(values:CffiData, size:int, dispose:bool=True) -> List[str]:
    pystrings = marshal.c_charptrptr_as_string_list(values, size)
    if dispose:
        swift_so.DeleteAnsiStringArray(values, size)
    return pystrings

def char_array_to_py(values:CffiData, dispose:bool=True) -> str:
    pystring = marshal.c_string_as_py_string(values)
    if dispose:
        swift_so.DeleteAnsiString(values)
    return pystring

def named_values_to_py(values:CffiData, dispose:bool=True) -> Dict[str,float]:
    x = marshal.named_values_to_dict(values)
    if dispose:
        swift_so.DisposeNamedValuedVectorsSwift(values)
    return x

def opaque_ts_as_xarray_time_series(ptr:CffiData, dispose:bool=True) -> xr.DataArray:
    res = marshal.as_xarray_time_series(ptr)
    if dispose:
        swift_so.DisposeMultiTimeSeriesData(ptr)
    return res

def py_time_series_dimensions_description(ptr:CffiData, dispose:bool=True) -> List[Tuple[str,int]]:
    n = ptr.num_dimensions
    def dim_spec(i):
        d = ptr.dimensions[i]
        return(marshal.c_string_as_py_string(d.dimension_type), d.size)
    res = [dim_spec(i) for i in range(n)]
    if dispose:
        swift_so.DisposeDataDimensionsDescriptions(ptr)
    return res

def toSceParametersNative(x:dict) -> OwningCffiNativeHandle:
    res = marshal.new_native_struct('SceParameters*')
    p = res.ptr
    p.Alpha = int(x['Alpha'])
    p.Beta = int(x['Beta'])
    p.P = int(x['P'])
    p.Pmin = int(x['Pmin'])
    p.M = int(x['M'])
    p.Q = int(x['Q'])
    p.NumShuffle = x['NumShuffle']
    p.TrapezoidalDensityParameter = float(x['TrapezoidalDensityParameter'])
    p.ReflectionRatio = float(x['ReflectionRatio'])
    p.ContractionRatio = float(x['ContractionRatio'])
    return res

def dispose_shared_pointer_py(ptr:Any) -> None:
    # Upon a process terminating, somehow wrap_as_pointer_handle can end up being None,
    # leading to a TypeError: 'NoneType' object is not callable.
    # This is a nuisance, and hard to fully diagnose.
    # So, we will use the following workaround to guard against it. See WIRADA-659.
    if wrap_as_pointer_handle is None:
        return
    ptr_xptr = wrap_as_pointer_handle(ptr)
    # Upon a process terminating, somehow 'swift_so' can end up being None,
    # leading to a TypeError: 'NoneType' object is not callable.
    # This is a nuisance, and hard to fully diagnose.
    # So, we will use the following workaround to guard against it. See WIRADA-659.
    if swift_so is not None: #  and swift_so.DisposeSharedPointer is not None:
        swift_so.DisposeSharedPointer(ptr_xptr.ptr)

@_s_wrap.check_exceptions
def _GetLastStdExceptionMessage_native():
    result = swift_so.GetLastStdExceptionMessage()
    return result

def GetLastStdExceptionMessage_py() -> str:
    """GetLastStdExceptionMessage_py
    
    GetLastStdExceptionMessage_py: generated wrapper function for API function GetLastStdExceptionMessage
    
    Args:
    
    Returns:
        (str): returned result
    
    """
    result = _GetLastStdExceptionMessage_native()
    return char_array_to_py(result, dispose=True)


@_s_wrap.check_exceptions
def _RegisterExceptionCallback_native(callback):
    swift_so.RegisterExceptionCallback(callback)

def RegisterExceptionCallback_py(callback:Any) -> None:
    """RegisterExceptionCallback_py
    
    RegisterExceptionCallback_py: generated wrapper function for API function RegisterExceptionCallback
    
    Args:
        callback (Any): callback
    
    """
    _RegisterExceptionCallback_native(callback)


@_s_wrap.check_exceptions
def _RegisterExceptionCallbackSwift_native(callback):
    swift_so.RegisterExceptionCallbackSwift(callback)

def RegisterExceptionCallbackSwift_py(callback:Any) -> None:
    """RegisterExceptionCallbackSwift_py
    
    RegisterExceptionCallbackSwift_py: generated wrapper function for API function RegisterExceptionCallbackSwift
    
    Args:
        callback (Any): callback
    
    """
    _RegisterExceptionCallbackSwift_native(callback)


@_s_wrap.check_exceptions
def _DisposeSharedPointer_native(ptr):
    swift_so.DisposeSharedPointer(ptr)

def DisposeSharedPointer_py(ptr:Any) -> None:
    """DisposeSharedPointer_py
    
    DisposeSharedPointer_py: generated wrapper function for API function DisposeSharedPointer
    
    Args:
        ptr (Any): ptr
    
    """
    ptr_xptr = wrap_as_pointer_handle(ptr)
    _DisposeSharedPointer_native(ptr_xptr.ptr)


@_s_wrap.check_exceptions
def _GetNumRunoffModelIdentifiers_native():
    result = swift_so.GetNumRunoffModelIdentifiers()
    return result

def GetNumRunoffModelIdentifiers_py() -> int:
    """GetNumRunoffModelIdentifiers_py
    
    GetNumRunoffModelIdentifiers_py: generated wrapper function for API function GetNumRunoffModelIdentifiers
    
    Args:
    
    Returns:
        (int): returned result
    
    """
    result = _GetNumRunoffModelIdentifiers_native()
    return result


@_s_wrap.check_exceptions
def _GetNumRunoffModelVarIdentifiers_native(modelId):
    result = swift_so.GetNumRunoffModelVarIdentifiers(modelId)
    return result

def GetNumRunoffModelVarIdentifiers_py(modelId:str) -> int:
    """GetNumRunoffModelVarIdentifiers_py
    
    GetNumRunoffModelVarIdentifiers_py: generated wrapper function for API function GetNumRunoffModelVarIdentifiers
    
    Args:
        modelId (str): modelId
    
    Returns:
        (int): returned result
    
    """
    modelId_c_charp = wrap_as_pointer_handle(as_bytes(modelId))
    result = _GetNumRunoffModelVarIdentifiers_native(modelId_c_charp.ptr)
    # no cleanup for const char*
    return result


@_s_wrap.check_exceptions
def _GetRunoffModelIdentifier_native(index):
    result = swift_so.GetRunoffModelIdentifier(index)
    return result

def GetRunoffModelIdentifier_py(index:int) -> str:
    """GetRunoffModelIdentifier_py
    
    GetRunoffModelIdentifier_py: generated wrapper function for API function GetRunoffModelIdentifier
    
    Args:
        index (int): index
    
    Returns:
        (str): returned result
    
    """
    result = _GetRunoffModelIdentifier_native(index)
    return char_array_to_py(result, dispose=True)


@_s_wrap.check_exceptions
def _GetRunoffModelVarIdentifier_native(modelId, index):
    result = swift_so.GetRunoffModelVarIdentifier(modelId, index)
    return result

def GetRunoffModelVarIdentifier_py(modelId:str, index:int) -> str:
    """GetRunoffModelVarIdentifier_py
    
    GetRunoffModelVarIdentifier_py: generated wrapper function for API function GetRunoffModelVarIdentifier
    
    Args:
        modelId (str): modelId
        index (int): index
    
    Returns:
        (str): returned result
    
    """
    modelId_c_charp = wrap_as_pointer_handle(as_bytes(modelId))
    result = _GetRunoffModelVarIdentifier_native(modelId_c_charp.ptr, index)
    # no cleanup for const char*
    return char_array_to_py(result, dispose=True)



def _GetRunoffModelIdentifiers_native( size):
    return swift_so.GetRunoffModelIdentifiers( size)

def GetRunoffModelIdentifiers_py():
    """GetRunoffModelIdentifiers_py
    
    GetRunoffModelIdentifiers_py: generated wrapper function for API function GetRunoffModelIdentifiers
    
    
    """



    size = marshal.new_int_scalar_ptr()
    values = _GetRunoffModelIdentifiers_native( size)


    result = charp_array_to_py(values, size[0], True)
    return result


def _GetRunoffModelVarIdentifiers_native(modelId, size):
    return swift_so.GetRunoffModelVarIdentifiers(modelId, size)

def GetRunoffModelVarIdentifiers_py(modelId:str):
    """GetRunoffModelVarIdentifiers_py
    
    GetRunoffModelVarIdentifiers_py: generated wrapper function for API function GetRunoffModelVarIdentifiers
    
    
    """

    modelId_c_charp = wrap_as_pointer_handle(as_bytes(modelId))

    size = marshal.new_int_scalar_ptr()
    values = _GetRunoffModelVarIdentifiers_native(modelId_c_charp.ptr, size)
    # no cleanup for const char*

    result = charp_array_to_py(values, size[0], True)
    return result

@_s_wrap.check_exceptions
def _CloneModel_native(simulation):
    result = swift_so.CloneModel(simulation)
    return result

def CloneModel_py(simulation:'Simulation') -> 'Simulation':
    """CloneModel_py
    
    CloneModel_py: generated wrapper function for API function CloneModel
    
    Args:
        simulation ('Simulation'): simulation
    
    Returns:
        ('Simulation'): returned result
    
    """
    simulation_xptr = wrap_as_pointer_handle(simulation)
    result = _CloneModel_native(simulation_xptr.ptr)
    return custom_wrap_cffi_native_handle(result, 'MODEL_SIMULATION_PTR')


@_s_wrap.check_exceptions
def _SubsetModel_native(simulation, elementName, selectNetworkAboveElement, includeElementInSelection, invertSelection, terminationElements, terminationElementsLength):
    result = swift_so.SubsetModel(simulation, elementName, selectNetworkAboveElement, includeElementInSelection, invertSelection, terminationElements, terminationElementsLength)
    return result

def SubsetModel_py(simulation:'Simulation', elementName:str, selectNetworkAboveElement:bool, includeElementInSelection:bool, invertSelection:bool, terminationElements:List[str], terminationElementsLength:int) -> 'Simulation':
    """SubsetModel_py
    
    SubsetModel_py: generated wrapper function for API function SubsetModel
    
    Args:
        simulation ('Simulation'): simulation
        elementName (str): elementName
        selectNetworkAboveElement (bool): selectNetworkAboveElement
        includeElementInSelection (bool): includeElementInSelection
        invertSelection (bool): invertSelection
        terminationElements (List[str]): terminationElements
        terminationElementsLength (int): terminationElementsLength
    
    Returns:
        ('Simulation'): returned result
    
    """
    simulation_xptr = wrap_as_pointer_handle(simulation)
    elementName_c_charp = wrap_as_pointer_handle(as_bytes(elementName))
    terminationElements_charpp = wrap_as_pointer_handle(marshal.as_arrayof_bytes(terminationElements))
    result = _SubsetModel_native(simulation_xptr.ptr, elementName_c_charp.ptr, selectNetworkAboveElement, includeElementInSelection, invertSelection, terminationElements_charpp.ptr, terminationElementsLength)
    # no cleanup for const char*
    # clean terminationElements_charpp ?
    return custom_wrap_cffi_native_handle(result, 'MODEL_SIMULATION_PTR')



def _SortSimulationElementsByRunOrder_native(simulation, elementIds, numElements, orderingMethod, size):
    return swift_so.SortSimulationElementsByRunOrder(simulation, elementIds, numElements, orderingMethod, size)

def SortSimulationElementsByRunOrder_py(simulation:'Simulation', elementIds:List[str], numElements:int, orderingMethod:str):
    """SortSimulationElementsByRunOrder_py
    
    SortSimulationElementsByRunOrder_py: generated wrapper function for API function SortSimulationElementsByRunOrder
    
    
    """

    simulation_xptr = wrap_as_pointer_handle(simulation)
    elementIds_charpp = wrap_as_pointer_handle(marshal.as_arrayof_bytes(elementIds))
    orderingMethod_c_charp = wrap_as_pointer_handle(as_bytes(orderingMethod))

    size = marshal.new_int_scalar_ptr()
    values = _SortSimulationElementsByRunOrder_native(simulation_xptr.ptr, elementIds_charpp.ptr, numElements, orderingMethod_c_charp.ptr, size)
    # clean elementIds_charpp ?
    # no cleanup for const char*

    result = charp_array_to_py(values, size[0], True)
    return result

@_s_wrap.check_exceptions
def _SwapRunoffModel_native(simulation, newModelId):
    result = swift_so.SwapRunoffModel(simulation, newModelId)
    return result

def SwapRunoffModel_py(simulation:'Simulation', newModelId:str) -> 'Simulation':
    """SwapRunoffModel_py
    
    SwapRunoffModel_py: generated wrapper function for API function SwapRunoffModel
    
    Args:
        simulation ('Simulation'): simulation
        newModelId (str): newModelId
    
    Returns:
        ('Simulation'): returned result
    
    """
    simulation_xptr = wrap_as_pointer_handle(simulation)
    newModelId_c_charp = wrap_as_pointer_handle(as_bytes(newModelId))
    result = _SwapRunoffModel_native(simulation_xptr.ptr, newModelId_c_charp.ptr)
    # no cleanup for const char*
    return custom_wrap_cffi_native_handle(result, 'MODEL_SIMULATION_PTR')


@_s_wrap.check_exceptions
def _SetChannelRoutingModel_native(simulation, newModelId):
    swift_so.SetChannelRoutingModel(simulation, newModelId)

def SetChannelRoutingModel_py(simulation:'Simulation', newModelId:str) -> None:
    """SetChannelRoutingModel_py
    
    SetChannelRoutingModel_py: generated wrapper function for API function SetChannelRoutingModel
    
    Args:
        simulation ('Simulation'): simulation
        newModelId (str): newModelId
    
    """
    simulation_xptr = wrap_as_pointer_handle(simulation)
    newModelId_c_charp = wrap_as_pointer_handle(as_bytes(newModelId))
    _SetChannelRoutingModel_native(simulation_xptr.ptr, newModelId_c_charp.ptr)
    # no cleanup for const char*


@_s_wrap.check_exceptions
def _SetErrorCorrectionModel_native(simulation, newModelId, elementId, length, seed):
    swift_so.SetErrorCorrectionModel(simulation, newModelId, elementId, length, seed)

def SetErrorCorrectionModel_py(simulation:'Simulation', newModelId:str, elementId:str, length:int, seed:int) -> None:
    """SetErrorCorrectionModel_py
    
    SetErrorCorrectionModel_py: generated wrapper function for API function SetErrorCorrectionModel
    
    Args:
        simulation ('Simulation'): simulation
        newModelId (str): newModelId
        elementId (str): elementId
        length (int): length
        seed (int): seed
    
    """
    simulation_xptr = wrap_as_pointer_handle(simulation)
    newModelId_c_charp = wrap_as_pointer_handle(as_bytes(newModelId))
    elementId_c_charp = wrap_as_pointer_handle(as_bytes(elementId))
    _SetErrorCorrectionModel_native(simulation_xptr.ptr, newModelId_c_charp.ptr, elementId_c_charp.ptr, length, seed)
    # no cleanup for const char*
    # no cleanup for const char*


@_s_wrap.check_exceptions
def _SetSeedForModel_native(simulation, modelObjectIdentifier, seed):
    swift_so.SetSeedForModel(simulation, modelObjectIdentifier, seed)

def SetSeedForModel_py(simulation:'Simulation', modelObjectIdentifier:str, seed:int) -> None:
    """SetSeedForModel_py
    
    SetSeedForModel_py: generated wrapper function for API function SetSeedForModel
    
    Args:
        simulation ('Simulation'): simulation
        modelObjectIdentifier (str): modelObjectIdentifier
        seed (int): seed
    
    """
    simulation_xptr = wrap_as_pointer_handle(simulation)
    modelObjectIdentifier_c_charp = wrap_as_pointer_handle(as_bytes(modelObjectIdentifier))
    _SetSeedForModel_native(simulation_xptr.ptr, modelObjectIdentifier_c_charp.ptr, seed)
    # no cleanup for const char*


@_s_wrap.check_exceptions
def _SetReservoirModel_native(simulation, newModelId, elementId):
    swift_so.SetReservoirModel(simulation, newModelId, elementId)

def SetReservoirModel_py(simulation:'Simulation', newModelId:str, elementId:str) -> None:
    """SetReservoirModel_py
    
    SetReservoirModel_py: generated wrapper function for API function SetReservoirModel
    
    Args:
        simulation ('Simulation'): simulation
        newModelId (str): newModelId
        elementId (str): elementId
    
    """
    simulation_xptr = wrap_as_pointer_handle(simulation)
    newModelId_c_charp = wrap_as_pointer_handle(as_bytes(newModelId))
    elementId_c_charp = wrap_as_pointer_handle(as_bytes(elementId))
    _SetReservoirModel_native(simulation_xptr.ptr, newModelId_c_charp.ptr, elementId_c_charp.ptr)
    # no cleanup for const char*
    # no cleanup for const char*


@_s_wrap.check_exceptions
def _SetRunoffPostProcessingModel_native(src, newModelId, elementId):
    swift_so.SetRunoffPostProcessingModel(src, newModelId, elementId)

def SetRunoffPostProcessingModel_py(src:'Simulation', newModelId:str, elementId:str) -> None:
    """SetRunoffPostProcessingModel_py
    
    SetRunoffPostProcessingModel_py: generated wrapper function for API function SetRunoffPostProcessingModel
    
    Args:
        src ('Simulation'): src
        newModelId (str): newModelId
        elementId (str): elementId
    
    """
    src_xptr = wrap_as_pointer_handle(src)
    newModelId_c_charp = wrap_as_pointer_handle(as_bytes(newModelId))
    elementId_c_charp = wrap_as_pointer_handle(as_bytes(elementId))
    _SetRunoffPostProcessingModel_native(src_xptr.ptr, newModelId_c_charp.ptr, elementId_c_charp.ptr)
    # no cleanup for const char*
    # no cleanup for const char*


@_s_wrap.check_exceptions
def _SetReservoirGeometry_native(simulation, elementId, numEntries, level, storage, area):
    swift_so.SetReservoirGeometry(simulation, elementId, numEntries, level, storage, area)

def SetReservoirGeometry_py(simulation:'Simulation', elementId:str, numEntries:int, level:np.ndarray, storage:np.ndarray, area:np.ndarray) -> None:
    """SetReservoirGeometry_py
    
    SetReservoirGeometry_py: generated wrapper function for API function SetReservoirGeometry
    
    Args:
        simulation ('Simulation'): simulation
        elementId (str): elementId
        numEntries (int): numEntries
        level (np.ndarray): level
        storage (np.ndarray): storage
        area (np.ndarray): area
    
    """
    simulation_xptr = wrap_as_pointer_handle(simulation)
    elementId_c_charp = wrap_as_pointer_handle(as_bytes(elementId))
    level_numarray = marshal.as_c_double_array(level, shallow=True)
    storage_numarray = marshal.as_c_double_array(storage, shallow=True)
    area_numarray = marshal.as_c_double_array(area, shallow=True)
    _SetReservoirGeometry_native(simulation_xptr.ptr, elementId_c_charp.ptr, numEntries, level_numarray.ptr, storage_numarray.ptr, area_numarray.ptr)
    # no cleanup for const char*
    # level_numarray - no cleanup needed?
    # storage_numarray - no cleanup needed?
    # area_numarray - no cleanup needed?


@_s_wrap.check_exceptions
def _SetReservoirMinDischarge_native(simulation, elementId, numEntries, level, discharge):
    swift_so.SetReservoirMinDischarge(simulation, elementId, numEntries, level, discharge)

def SetReservoirMinDischarge_py(simulation:'Simulation', elementId:str, numEntries:int, level:np.ndarray, discharge:np.ndarray) -> None:
    """SetReservoirMinDischarge_py
    
    SetReservoirMinDischarge_py: generated wrapper function for API function SetReservoirMinDischarge
    
    Args:
        simulation ('Simulation'): simulation
        elementId (str): elementId
        numEntries (int): numEntries
        level (np.ndarray): level
        discharge (np.ndarray): discharge
    
    """
    simulation_xptr = wrap_as_pointer_handle(simulation)
    elementId_c_charp = wrap_as_pointer_handle(as_bytes(elementId))
    level_numarray = marshal.as_c_double_array(level, shallow=True)
    discharge_numarray = marshal.as_c_double_array(discharge, shallow=True)
    _SetReservoirMinDischarge_native(simulation_xptr.ptr, elementId_c_charp.ptr, numEntries, level_numarray.ptr, discharge_numarray.ptr)
    # no cleanup for const char*
    # level_numarray - no cleanup needed?
    # discharge_numarray - no cleanup needed?


@_s_wrap.check_exceptions
def _SetReservoirMaxDischarge_native(simulation, elementId, numEntries, level, discharge):
    swift_so.SetReservoirMaxDischarge(simulation, elementId, numEntries, level, discharge)

def SetReservoirMaxDischarge_py(simulation:'Simulation', elementId:str, numEntries:int, level:np.ndarray, discharge:np.ndarray) -> None:
    """SetReservoirMaxDischarge_py
    
    SetReservoirMaxDischarge_py: generated wrapper function for API function SetReservoirMaxDischarge
    
    Args:
        simulation ('Simulation'): simulation
        elementId (str): elementId
        numEntries (int): numEntries
        level (np.ndarray): level
        discharge (np.ndarray): discharge
    
    """
    simulation_xptr = wrap_as_pointer_handle(simulation)
    elementId_c_charp = wrap_as_pointer_handle(as_bytes(elementId))
    level_numarray = marshal.as_c_double_array(level, shallow=True)
    discharge_numarray = marshal.as_c_double_array(discharge, shallow=True)
    _SetReservoirMaxDischarge_native(simulation_xptr.ptr, elementId_c_charp.ptr, numEntries, level_numarray.ptr, discharge_numarray.ptr)
    # no cleanup for const char*
    # level_numarray - no cleanup needed?
    # discharge_numarray - no cleanup needed?


@_s_wrap.check_exceptions
def _SetReservoirOpsReleaseCurve_native(simulation, elementId, numEntries, level, discharge):
    swift_so.SetReservoirOpsReleaseCurve(simulation, elementId, numEntries, level, discharge)

def SetReservoirOpsReleaseCurve_py(simulation:'Simulation', elementId:str, numEntries:int, level:np.ndarray, discharge:np.ndarray) -> None:
    """SetReservoirOpsReleaseCurve_py
    
    SetReservoirOpsReleaseCurve_py: generated wrapper function for API function SetReservoirOpsReleaseCurve
    
    Args:
        simulation ('Simulation'): simulation
        elementId (str): elementId
        numEntries (int): numEntries
        level (np.ndarray): level
        discharge (np.ndarray): discharge
    
    """
    simulation_xptr = wrap_as_pointer_handle(simulation)
    elementId_c_charp = wrap_as_pointer_handle(as_bytes(elementId))
    level_numarray = marshal.as_c_double_array(level, shallow=True)
    discharge_numarray = marshal.as_c_double_array(discharge, shallow=True)
    _SetReservoirOpsReleaseCurve_native(simulation_xptr.ptr, elementId_c_charp.ptr, numEntries, level_numarray.ptr, discharge_numarray.ptr)
    # no cleanup for const char*
    # level_numarray - no cleanup needed?
    # discharge_numarray - no cleanup needed?


@_s_wrap.check_exceptions
def _RemoveStorageDischargeRelationship_native(simulation, elementId, relationshipType):
    swift_so.RemoveStorageDischargeRelationship(simulation, elementId, relationshipType)

def RemoveStorageDischargeRelationship_py(simulation:'Simulation', elementId:str, relationshipType:str) -> None:
    """RemoveStorageDischargeRelationship_py
    
    RemoveStorageDischargeRelationship_py: generated wrapper function for API function RemoveStorageDischargeRelationship
    
    Args:
        simulation ('Simulation'): simulation
        elementId (str): elementId
        relationshipType (str): relationshipType
    
    """
    simulation_xptr = wrap_as_pointer_handle(simulation)
    elementId_c_charp = wrap_as_pointer_handle(as_bytes(elementId))
    relationshipType_c_charp = wrap_as_pointer_handle(as_bytes(relationshipType))
    _RemoveStorageDischargeRelationship_native(simulation_xptr.ptr, elementId_c_charp.ptr, relationshipType_c_charp.ptr)
    # no cleanup for const char*
    # no cleanup for const char*


@_s_wrap.check_exceptions
def _SetSubareaInputsPreprocessorModel_native(simulation, newModelId, subAreaId):
    swift_so.SetSubareaInputsPreprocessorModel(simulation, newModelId, subAreaId)

def SetSubareaInputsPreprocessorModel_py(simulation:'Simulation', newModelId:str, subAreaId:str) -> None:
    """SetSubareaInputsPreprocessorModel_py
    
    SetSubareaInputsPreprocessorModel_py: generated wrapper function for API function SetSubareaInputsPreprocessorModel
    
    Args:
        simulation ('Simulation'): simulation
        newModelId (str): newModelId
        subAreaId (str): subAreaId
    
    """
    simulation_xptr = wrap_as_pointer_handle(simulation)
    newModelId_c_charp = wrap_as_pointer_handle(as_bytes(newModelId))
    subAreaId_c_charp = wrap_as_pointer_handle(as_bytes(subAreaId))
    _SetSubareaInputsPreprocessorModel_native(simulation_xptr.ptr, newModelId_c_charp.ptr, subAreaId_c_charp.ptr)
    # no cleanup for const char*
    # no cleanup for const char*


@_s_wrap.check_exceptions
def _WireSubareaInputsPreprocessorModel_native(simulation, fromOutput, toInput, subAreaId):
    swift_so.WireSubareaInputsPreprocessorModel(simulation, fromOutput, toInput, subAreaId)

def WireSubareaInputsPreprocessorModel_py(simulation:'Simulation', fromOutput:str, toInput:str, subAreaId:str) -> None:
    """WireSubareaInputsPreprocessorModel_py
    
    WireSubareaInputsPreprocessorModel_py: generated wrapper function for API function WireSubareaInputsPreprocessorModel
    
    Args:
        simulation ('Simulation'): simulation
        fromOutput (str): fromOutput
        toInput (str): toInput
        subAreaId (str): subAreaId
    
    """
    simulation_xptr = wrap_as_pointer_handle(simulation)
    fromOutput_c_charp = wrap_as_pointer_handle(as_bytes(fromOutput))
    toInput_c_charp = wrap_as_pointer_handle(as_bytes(toInput))
    subAreaId_c_charp = wrap_as_pointer_handle(as_bytes(subAreaId))
    _WireSubareaInputsPreprocessorModel_native(simulation_xptr.ptr, fromOutput_c_charp.ptr, toInput_c_charp.ptr, subAreaId_c_charp.ptr)
    # no cleanup for const char*
    # no cleanup for const char*
    # no cleanup for const char*


@_s_wrap.check_exceptions
def _RemoveModel_native(simulation, fullModelId):
    swift_so.RemoveModel(simulation, fullModelId)

def RemoveModel_py(simulation:'Simulation', fullModelId:str) -> None:
    """RemoveModel_py
    
    RemoveModel_py: generated wrapper function for API function RemoveModel
    
    Args:
        simulation ('Simulation'): simulation
        fullModelId (str): fullModelId
    
    """
    simulation_xptr = wrap_as_pointer_handle(simulation)
    fullModelId_c_charp = wrap_as_pointer_handle(as_bytes(fullModelId))
    _RemoveModel_native(simulation_xptr.ptr, fullModelId_c_charp.ptr)
    # no cleanup for const char*


@_s_wrap.check_exceptions
def _CreateCatchment_native(numNodes, nodeIds, nodeNames, numLinks, linkIds, linkNames, linkFromNode, linkToNode, runoffModelName, areasKm2):
    result = swift_so.CreateCatchment(numNodes, nodeIds, nodeNames, numLinks, linkIds, linkNames, linkFromNode, linkToNode, runoffModelName, areasKm2)
    return result

def CreateCatchment_py(numNodes:int, nodeIds:List[str], nodeNames:List[str], numLinks:int, linkIds:List[str], linkNames:List[str], linkFromNode:List[str], linkToNode:List[str], runoffModelName:str, areasKm2:np.ndarray) -> 'Simulation':
    """CreateCatchment_py
    
    CreateCatchment_py: generated wrapper function for API function CreateCatchment
    
    Args:
        numNodes (int): numNodes
        nodeIds (List[str]): nodeIds
        nodeNames (List[str]): nodeNames
        numLinks (int): numLinks
        linkIds (List[str]): linkIds
        linkNames (List[str]): linkNames
        linkFromNode (List[str]): linkFromNode
        linkToNode (List[str]): linkToNode
        runoffModelName (str): runoffModelName
        areasKm2 (np.ndarray): areasKm2
    
    Returns:
        ('Simulation'): returned result
    
    """
    nodeIds_charpp = wrap_as_pointer_handle(marshal.as_arrayof_bytes(nodeIds))
    nodeNames_charpp = wrap_as_pointer_handle(marshal.as_arrayof_bytes(nodeNames))
    linkIds_charpp = wrap_as_pointer_handle(marshal.as_arrayof_bytes(linkIds))
    linkNames_charpp = wrap_as_pointer_handle(marshal.as_arrayof_bytes(linkNames))
    linkFromNode_charpp = wrap_as_pointer_handle(marshal.as_arrayof_bytes(linkFromNode))
    linkToNode_charpp = wrap_as_pointer_handle(marshal.as_arrayof_bytes(linkToNode))
    runoffModelName_c_charp = wrap_as_pointer_handle(as_bytes(runoffModelName))
    areasKm2_numarray = marshal.as_c_double_array(areasKm2, shallow=True)
    result = _CreateCatchment_native(numNodes, nodeIds_charpp.ptr, nodeNames_charpp.ptr, numLinks, linkIds_charpp.ptr, linkNames_charpp.ptr, linkFromNode_charpp.ptr, linkToNode_charpp.ptr, runoffModelName_c_charp.ptr, areasKm2_numarray.ptr)
    # clean nodeIds_charpp ?
    # clean nodeNames_charpp ?
    # clean linkIds_charpp ?
    # clean linkNames_charpp ?
    # clean linkFromNode_charpp ?
    # clean linkToNode_charpp ?
    # no cleanup for const char*
    # areasKm2_numarray - no cleanup needed?
    return custom_wrap_cffi_native_handle(result, 'MODEL_SIMULATION_PTR')


@_s_wrap.check_exceptions
def _GetCatchmentStructure_native(simulation):
    result = swift_so.GetCatchmentStructure(simulation)
    return result

def GetCatchmentStructure_py(simulation:'Simulation') -> DeletableCffiNativeHandle:
    """GetCatchmentStructure_py
    
    GetCatchmentStructure_py: generated wrapper function for API function GetCatchmentStructure
    
    Args:
        simulation ('Simulation'): simulation
    
    Returns:
        (DeletableCffiNativeHandle): returned result
    
    """
    simulation_xptr = wrap_as_pointer_handle(simulation)
    result = _GetCatchmentStructure_native(simulation_xptr.ptr)
    return custom_wrap_cffi_native_handle(result, 'CatchmentStructure*', DisposeCatchmentStructure_py)


@_s_wrap.check_exceptions
def _DisposeCatchmentStructure_native(structure):
    swift_so.DisposeCatchmentStructure(structure)

def DisposeCatchmentStructure_py(structure:DeletableCffiNativeHandle) -> None:
    """DisposeCatchmentStructure_py
    
    DisposeCatchmentStructure_py: generated wrapper function for API function DisposeCatchmentStructure
    
    Args:
        structure (DeletableCffiNativeHandle): structure
    
    """
    _DisposeCatchmentStructure_native(structure)


@_s_wrap.check_exceptions
def _CreateNewFromNetworkInfo_native(nodes, numNodes, links, numLinks):
    result = swift_so.CreateNewFromNetworkInfo(nodes, numNodes, links, numLinks)
    return result

def CreateNewFromNetworkInfo_py(nodes:Any, numNodes:int, links:Any, numLinks:int) -> 'Simulation':
    """CreateNewFromNetworkInfo_py
    
    CreateNewFromNetworkInfo_py: generated wrapper function for API function CreateNewFromNetworkInfo
    
    Args:
        nodes (Any): nodes
        numNodes (int): numNodes
        links (Any): links
        numLinks (int): numLinks
    
    Returns:
        ('Simulation'): returned result
    
    """
    nodes_xptr = wrap_as_pointer_handle(nodes)
    links_xptr = wrap_as_pointer_handle(links)
    result = _CreateNewFromNetworkInfo_native(nodes_xptr.ptr, numNodes, links_xptr.ptr, numLinks)
    return custom_wrap_cffi_native_handle(result, 'MODEL_SIMULATION_PTR')


@_s_wrap.check_exceptions
def _Play_native(simulation, variableIdentifier, values, geom):
    swift_so.Play(simulation, variableIdentifier, values, geom)

def Play_py(simulation:'Simulation', variableIdentifier:str, values:np.ndarray, geom:TimeSeriesGeometryNative) -> None:
    """Play_py
    
    Play_py: generated wrapper function for API function Play
    
    Args:
        simulation ('Simulation'): simulation
        variableIdentifier (str): variableIdentifier
        values (np.ndarray): values
        geom (TimeSeriesGeometryNative): geom
    
    """
    simulation_xptr = wrap_as_pointer_handle(simulation)
    variableIdentifier_c_charp = wrap_as_pointer_handle(as_bytes(variableIdentifier))
    values_numarray = marshal.as_c_double_array(values, shallow=True)
    geom_xptr = wrap_as_pointer_handle(geom)
    _Play_native(simulation_xptr.ptr, variableIdentifier_c_charp.ptr, values_numarray.ptr, geom_xptr.ptr)
    # no cleanup for const char*
    # values_numarray - no cleanup needed?


@_s_wrap.check_exceptions
def _Record_native(simulation, variableIdentifier):
    swift_so.Record(simulation, variableIdentifier)

def Record_py(simulation:'Simulation', variableIdentifier:str) -> None:
    """Record_py
    
    Record_py: generated wrapper function for API function Record
    
    Args:
        simulation ('Simulation'): simulation
        variableIdentifier (str): variableIdentifier
    
    """
    simulation_xptr = wrap_as_pointer_handle(simulation)
    variableIdentifier_c_charp = wrap_as_pointer_handle(as_bytes(variableIdentifier))
    _Record_native(simulation_xptr.ptr, variableIdentifier_c_charp.ptr)
    # no cleanup for const char*


@_s_wrap.check_exceptions
def _RemovePlayedTimeSeries_native(modelInstance, variableIdentifier):
    swift_so.RemovePlayedTimeSeries(modelInstance, variableIdentifier)

def RemovePlayedTimeSeries_py(modelInstance:'Simulation', variableIdentifier:str) -> None:
    """RemovePlayedTimeSeries_py
    
    RemovePlayedTimeSeries_py: generated wrapper function for API function RemovePlayedTimeSeries
    
    Args:
        modelInstance ('Simulation'): modelInstance
        variableIdentifier (str): variableIdentifier
    
    """
    modelInstance_xptr = wrap_as_pointer_handle(modelInstance)
    variableIdentifier_c_charp = wrap_as_pointer_handle(as_bytes(variableIdentifier))
    _RemovePlayedTimeSeries_native(modelInstance_xptr.ptr, variableIdentifier_c_charp.ptr)
    # no cleanup for const char*


@_s_wrap.check_exceptions
def _RemoveRecorder_native(modelInstance, variableIdentifier):
    swift_so.RemoveRecorder(modelInstance, variableIdentifier)

def RemoveRecorder_py(modelInstance:'Simulation', variableIdentifier:str) -> None:
    """RemoveRecorder_py
    
    RemoveRecorder_py: generated wrapper function for API function RemoveRecorder
    
    Args:
        modelInstance ('Simulation'): modelInstance
        variableIdentifier (str): variableIdentifier
    
    """
    modelInstance_xptr = wrap_as_pointer_handle(modelInstance)
    variableIdentifier_c_charp = wrap_as_pointer_handle(as_bytes(variableIdentifier))
    _RemoveRecorder_native(modelInstance_xptr.ptr, variableIdentifier_c_charp.ptr)
    # no cleanup for const char*


@_s_wrap.check_exceptions
def _SetSpan_native(simulation, start, end):
    swift_so.SetSpan(simulation, start, end)

def SetSpan_py(simulation:Any, start:datetime, end:datetime) -> None:
    """SetSpan_py
    
    SetSpan_py: generated wrapper function for API function SetSpan
    
    Args:
        simulation (Any): simulation
        start (datetime): start
        end (datetime): end
    
    """
    simulation_xptr = wrap_as_pointer_handle(simulation)
    start_datetime = marshal.datetime_to_dtts(start)
    end_datetime = marshal.datetime_to_dtts(end)
    _SetSpan_native(simulation_xptr.ptr, start_datetime.obj, end_datetime.obj)
    # start_datetime - no cleanup needed?
    # end_datetime - no cleanup needed?


@_s_wrap.check_exceptions
def _CreateSubarea_native(modelId, areaKm2):
    result = swift_so.CreateSubarea(modelId, areaKm2)
    return result

def CreateSubarea_py(modelId:str, areaKm2:float) -> 'Simulation':
    """CreateSubarea_py
    
    CreateSubarea_py: generated wrapper function for API function CreateSubarea
    
    Args:
        modelId (str): modelId
        areaKm2 (float): areaKm2
    
    Returns:
        ('Simulation'): returned result
    
    """
    modelId_c_charp = wrap_as_pointer_handle(as_bytes(modelId))
    result = _CreateSubarea_native(modelId_c_charp.ptr, areaKm2)
    # no cleanup for const char*
    return custom_wrap_cffi_native_handle(result, 'MODEL_SIMULATION_PTR')


@_s_wrap.check_exceptions
def _ExecuteSimulation_native(simulation, resetInitialStates):
    swift_so.ExecuteSimulation(simulation, resetInitialStates)

def ExecuteSimulation_py(simulation:'Simulation', resetInitialStates:bool) -> None:
    """ExecuteSimulation_py
    
    ExecuteSimulation_py: generated wrapper function for API function ExecuteSimulation
    
    Args:
        simulation ('Simulation'): simulation
        resetInitialStates (bool): resetInitialStates
    
    """
    simulation_xptr = wrap_as_pointer_handle(simulation)
    _ExecuteSimulation_native(simulation_xptr.ptr, resetInitialStates)


@_s_wrap.check_exceptions
def _ResetModelStates_native(simulation):
    swift_so.ResetModelStates(simulation)

def ResetModelStates_py(simulation:'Simulation') -> None:
    """ResetModelStates_py
    
    ResetModelStates_py: generated wrapper function for API function ResetModelStates
    
    Args:
        simulation ('Simulation'): simulation
    
    """
    simulation_xptr = wrap_as_pointer_handle(simulation)
    _ResetModelStates_native(simulation_xptr.ptr)



def _CheckSimulationErrors_native(simulation, size):
    return swift_so.CheckSimulationErrors(simulation, size)

def CheckSimulationErrors_py(simulation:'Simulation'):
    """CheckSimulationErrors_py
    
    CheckSimulationErrors_py: generated wrapper function for API function CheckSimulationErrors
    
    
    """

    simulation_xptr = wrap_as_pointer_handle(simulation)

    size = marshal.new_int_scalar_ptr()
    values = _CheckSimulationErrors_native(simulation_xptr.ptr, size)


    result = charp_array_to_py(values, size[0], True)
    return result

@_s_wrap.check_exceptions
def _GetStart_native(simulation, start):
    swift_so.GetStart(simulation, start)

def GetStart_py(simulation:Any, start:Any) -> None:
    """GetStart_py
    
    GetStart_py: generated wrapper function for API function GetStart
    
    Args:
        simulation (Any): simulation
        start (Any): start
    
    """
    simulation_xptr = wrap_as_pointer_handle(simulation)
    start_xptr = wrap_as_pointer_handle(start)
    _GetStart_native(simulation_xptr.ptr, start_xptr.ptr)


@_s_wrap.check_exceptions
def _GetEnd_native(simulation, end):
    swift_so.GetEnd(simulation, end)

def GetEnd_py(simulation:Any, end:Any) -> None:
    """GetEnd_py
    
    GetEnd_py: generated wrapper function for API function GetEnd
    
    Args:
        simulation (Any): simulation
        end (Any): end
    
    """
    simulation_xptr = wrap_as_pointer_handle(simulation)
    end_xptr = wrap_as_pointer_handle(end)
    _GetEnd_native(simulation_xptr.ptr, end_xptr.ptr)


@_s_wrap.check_exceptions
def _SetTimeStep_native(simulation, timeStepName):
    swift_so.SetTimeStep(simulation, timeStepName)

def SetTimeStep_py(simulation:Any, timeStepName:str) -> None:
    """SetTimeStep_py
    
    SetTimeStep_py: generated wrapper function for API function SetTimeStep
    
    Args:
        simulation (Any): simulation
        timeStepName (str): timeStepName
    
    """
    simulation_xptr = wrap_as_pointer_handle(simulation)
    timeStepName_c_charp = wrap_as_pointer_handle(as_bytes(timeStepName))
    _SetTimeStep_native(simulation_xptr.ptr, timeStepName_c_charp.ptr)
    # no cleanup for const char*


@_s_wrap.check_exceptions
def _GetTimeStepName_native(simulation):
    result = swift_so.GetTimeStepName(simulation)
    return result

def GetTimeStepName_py(simulation:Any) -> str:
    """GetTimeStepName_py
    
    GetTimeStepName_py: generated wrapper function for API function GetTimeStepName
    
    Args:
        simulation (Any): simulation
    
    Returns:
        (str): returned result
    
    """
    simulation_xptr = wrap_as_pointer_handle(simulation)
    result = _GetTimeStepName_native(simulation_xptr.ptr)
    return char_array_to_py(result, dispose=True)


@_s_wrap.check_exceptions
def _GetNumSteps_native(simulation):
    result = swift_so.GetNumSteps(simulation)
    return result

def GetNumSteps_py(simulation:'Simulation') -> int:
    """GetNumSteps_py
    
    GetNumSteps_py: generated wrapper function for API function GetNumSteps
    
    Args:
        simulation ('Simulation'): simulation
    
    Returns:
        (int): returned result
    
    """
    simulation_xptr = wrap_as_pointer_handle(simulation)
    result = _GetNumSteps_native(simulation_xptr.ptr)
    return result


@_s_wrap.check_exceptions
def _GetNumStepsForTimeSpan_native(modelSimulation, start, end):
    result = swift_so.GetNumStepsForTimeSpan(modelSimulation, start, end)
    return result

def GetNumStepsForTimeSpan_py(modelSimulation:'Simulation', start:datetime, end:datetime) -> int:
    """GetNumStepsForTimeSpan_py
    
    GetNumStepsForTimeSpan_py: generated wrapper function for API function GetNumStepsForTimeSpan
    
    Args:
        modelSimulation ('Simulation'): modelSimulation
        start (datetime): start
        end (datetime): end
    
    Returns:
        (int): returned result
    
    """
    modelSimulation_xptr = wrap_as_pointer_handle(modelSimulation)
    start_datetime = marshal.datetime_to_dtts(start)
    end_datetime = marshal.datetime_to_dtts(end)
    result = _GetNumStepsForTimeSpan_native(modelSimulation_xptr.ptr, start_datetime.obj, end_datetime.obj)
    # start_datetime - no cleanup needed?
    # end_datetime - no cleanup needed?
    return result


@_s_wrap.check_exceptions
def _GetPlayedTimeSeriesLength_native(simulation, variableIdentifier):
    result = swift_so.GetPlayedTimeSeriesLength(simulation, variableIdentifier)
    return result

def GetPlayedTimeSeriesLength_py(simulation:'Simulation', variableIdentifier:str) -> int:
    """GetPlayedTimeSeriesLength_py
    
    GetPlayedTimeSeriesLength_py: generated wrapper function for API function GetPlayedTimeSeriesLength
    
    Args:
        simulation ('Simulation'): simulation
        variableIdentifier (str): variableIdentifier
    
    Returns:
        (int): returned result
    
    """
    simulation_xptr = wrap_as_pointer_handle(simulation)
    variableIdentifier_c_charp = wrap_as_pointer_handle(as_bytes(variableIdentifier))
    result = _GetPlayedTimeSeriesLength_native(simulation_xptr.ptr, variableIdentifier_c_charp.ptr)
    # no cleanup for const char*
    return result


@_s_wrap.check_exceptions
def _GetPlayed_native(simulation, variableIdentifier, values, arrayLength):
    swift_so.GetPlayed(simulation, variableIdentifier, values, arrayLength)

def GetPlayed_py(simulation:'Simulation', variableIdentifier:str, values:np.ndarray, arrayLength:int) -> None:
    """GetPlayed_py
    
    GetPlayed_py: generated wrapper function for API function GetPlayed
    
    Args:
        simulation ('Simulation'): simulation
        variableIdentifier (str): variableIdentifier
        values (np.ndarray): values
        arrayLength (int): arrayLength
    
    """
    simulation_xptr = wrap_as_pointer_handle(simulation)
    variableIdentifier_c_charp = wrap_as_pointer_handle(as_bytes(variableIdentifier))
    values_numarray = marshal.as_c_double_array(values, shallow=True)
    _GetPlayed_native(simulation_xptr.ptr, variableIdentifier_c_charp.ptr, values_numarray.ptr, arrayLength)
    # no cleanup for const char*
    # values_numarray - no cleanup needed?


@_s_wrap.check_exceptions
def _GetPlayedTsGeometry_native(simulation, variableIdentifier, geom):
    swift_so.GetPlayedTsGeometry(simulation, variableIdentifier, geom)

def GetPlayedTsGeometry_py(simulation:'Simulation', variableIdentifier:str, geom:TimeSeriesGeometryNative) -> None:
    """GetPlayedTsGeometry_py
    
    GetPlayedTsGeometry_py: generated wrapper function for API function GetPlayedTsGeometry
    
    Args:
        simulation ('Simulation'): simulation
        variableIdentifier (str): variableIdentifier
        geom (TimeSeriesGeometryNative): geom
    
    """
    simulation_xptr = wrap_as_pointer_handle(simulation)
    variableIdentifier_c_charp = wrap_as_pointer_handle(as_bytes(variableIdentifier))
    geom_xptr = wrap_as_pointer_handle(geom)
    _GetPlayedTsGeometry_native(simulation_xptr.ptr, variableIdentifier_c_charp.ptr, geom_xptr.ptr)
    # no cleanup for const char*


@_s_wrap.check_exceptions
def _GetRecorded_native(simulation, variableIdentifier, values, arrayLength):
    swift_so.GetRecorded(simulation, variableIdentifier, values, arrayLength)

def GetRecorded_py(simulation:'Simulation', variableIdentifier:str, values:np.ndarray, arrayLength:int) -> None:
    """GetRecorded_py
    
    GetRecorded_py: generated wrapper function for API function GetRecorded
    
    Args:
        simulation ('Simulation'): simulation
        variableIdentifier (str): variableIdentifier
        values (np.ndarray): values
        arrayLength (int): arrayLength
    
    """
    simulation_xptr = wrap_as_pointer_handle(simulation)
    variableIdentifier_c_charp = wrap_as_pointer_handle(as_bytes(variableIdentifier))
    values_numarray = marshal.as_c_double_array(values, shallow=True)
    _GetRecorded_native(simulation_xptr.ptr, variableIdentifier_c_charp.ptr, values_numarray.ptr, arrayLength)
    # no cleanup for const char*
    # values_numarray - no cleanup needed?


@_s_wrap.check_exceptions
def _GetRecordedTsGeometry_native(simulation, variableIdentifier, geom):
    swift_so.GetRecordedTsGeometry(simulation, variableIdentifier, geom)

def GetRecordedTsGeometry_py(simulation:'Simulation', variableIdentifier:str, geom:TimeSeriesGeometryNative) -> None:
    """GetRecordedTsGeometry_py
    
    GetRecordedTsGeometry_py: generated wrapper function for API function GetRecordedTsGeometry
    
    Args:
        simulation ('Simulation'): simulation
        variableIdentifier (str): variableIdentifier
        geom (TimeSeriesGeometryNative): geom
    
    """
    simulation_xptr = wrap_as_pointer_handle(simulation)
    variableIdentifier_c_charp = wrap_as_pointer_handle(as_bytes(variableIdentifier))
    geom_xptr = wrap_as_pointer_handle(geom)
    _GetRecordedTsGeometry_native(simulation_xptr.ptr, variableIdentifier_c_charp.ptr, geom_xptr.ptr)
    # no cleanup for const char*


@_s_wrap.check_exceptions
def _GetNumRecordedVariables_native(simulation):
    result = swift_so.GetNumRecordedVariables(simulation)
    return result

def GetNumRecordedVariables_py(simulation:'Simulation') -> int:
    """GetNumRecordedVariables_py
    
    GetNumRecordedVariables_py: generated wrapper function for API function GetNumRecordedVariables
    
    Args:
        simulation ('Simulation'): simulation
    
    Returns:
        (int): returned result
    
    """
    simulation_xptr = wrap_as_pointer_handle(simulation)
    result = _GetNumRecordedVariables_native(simulation_xptr.ptr)
    return result


@_s_wrap.check_exceptions
def _GetNumPlayedVariables_native(simulation):
    result = swift_so.GetNumPlayedVariables(simulation)
    return result

def GetNumPlayedVariables_py(simulation:'Simulation') -> int:
    """GetNumPlayedVariables_py
    
    GetNumPlayedVariables_py: generated wrapper function for API function GetNumPlayedVariables
    
    Args:
        simulation ('Simulation'): simulation
    
    Returns:
        (int): returned result
    
    """
    simulation_xptr = wrap_as_pointer_handle(simulation)
    result = _GetNumPlayedVariables_native(simulation_xptr.ptr)
    return result


@_s_wrap.check_exceptions
def _GetNumLinks_native(simulation):
    result = swift_so.GetNumLinks(simulation)
    return result

def GetNumLinks_py(simulation:'Simulation') -> int:
    """GetNumLinks_py
    
    GetNumLinks_py: generated wrapper function for API function GetNumLinks
    
    Args:
        simulation ('Simulation'): simulation
    
    Returns:
        (int): returned result
    
    """
    simulation_xptr = wrap_as_pointer_handle(simulation)
    result = _GetNumLinks_native(simulation_xptr.ptr)
    return result


@_s_wrap.check_exceptions
def _GetNumNodes_native(simulation):
    result = swift_so.GetNumNodes(simulation)
    return result

def GetNumNodes_py(simulation:'Simulation') -> int:
    """GetNumNodes_py
    
    GetNumNodes_py: generated wrapper function for API function GetNumNodes
    
    Args:
        simulation ('Simulation'): simulation
    
    Returns:
        (int): returned result
    
    """
    simulation_xptr = wrap_as_pointer_handle(simulation)
    result = _GetNumNodes_native(simulation_xptr.ptr)
    return result


@_s_wrap.check_exceptions
def _GetNumSubareas_native(simulation):
    result = swift_so.GetNumSubareas(simulation)
    return result

def GetNumSubareas_py(simulation:'Simulation') -> int:
    """GetNumSubareas_py
    
    GetNumSubareas_py: generated wrapper function for API function GetNumSubareas
    
    Args:
        simulation ('Simulation'): simulation
    
    Returns:
        (int): returned result
    
    """
    simulation_xptr = wrap_as_pointer_handle(simulation)
    result = _GetNumSubareas_native(simulation_xptr.ptr)
    return result


@_s_wrap.check_exceptions
def _GetNumVarIdentifiers_native(simulation, elementId):
    result = swift_so.GetNumVarIdentifiers(simulation, elementId)
    return result

def GetNumVarIdentifiers_py(simulation:'Simulation', elementId:str) -> int:
    """GetNumVarIdentifiers_py
    
    GetNumVarIdentifiers_py: generated wrapper function for API function GetNumVarIdentifiers
    
    Args:
        simulation ('Simulation'): simulation
        elementId (str): elementId
    
    Returns:
        (int): returned result
    
    """
    simulation_xptr = wrap_as_pointer_handle(simulation)
    elementId_c_charp = wrap_as_pointer_handle(as_bytes(elementId))
    result = _GetNumVarIdentifiers_native(simulation_xptr.ptr, elementId_c_charp.ptr)
    # no cleanup for const char*
    return result


@_s_wrap.check_exceptions
def _IsValidVariableIdentifier_native(simulation, varId):
    result = swift_so.IsValidVariableIdentifier(simulation, varId)
    return result

def IsValidVariableIdentifier_py(simulation:'Simulation', varId:str) -> bool:
    """IsValidVariableIdentifier_py
    
    IsValidVariableIdentifier_py: generated wrapper function for API function IsValidVariableIdentifier
    
    Args:
        simulation ('Simulation'): simulation
        varId (str): varId
    
    Returns:
        (bool): returned result
    
    """
    simulation_xptr = wrap_as_pointer_handle(simulation)
    varId_c_charp = wrap_as_pointer_handle(as_bytes(varId))
    result = _IsValidVariableIdentifier_native(simulation_xptr.ptr, varId_c_charp.ptr)
    # no cleanup for const char*
    return result


@_s_wrap.check_exceptions
def _GetCatchmentDOTGraph_native(simulation):
    result = swift_so.GetCatchmentDOTGraph(simulation)
    return result

def GetCatchmentDOTGraph_py(simulation:'Simulation') -> str:
    """GetCatchmentDOTGraph_py
    
    GetCatchmentDOTGraph_py: generated wrapper function for API function GetCatchmentDOTGraph
    
    Args:
        simulation ('Simulation'): simulation
    
    Returns:
        (str): returned result
    
    """
    simulation_xptr = wrap_as_pointer_handle(simulation)
    result = _GetCatchmentDOTGraph_native(simulation_xptr.ptr)
    return char_array_to_py(result, dispose=True)



def _GetPlayedVariableNames_native(simulation, size):
    return swift_so.GetPlayedVariableNames(simulation, size)

def GetPlayedVariableNames_py(simulation:'Simulation'):
    """GetPlayedVariableNames_py
    
    GetPlayedVariableNames_py: generated wrapper function for API function GetPlayedVariableNames
    
    
    """

    simulation_xptr = wrap_as_pointer_handle(simulation)

    size = marshal.new_int_scalar_ptr()
    values = _GetPlayedVariableNames_native(simulation_xptr.ptr, size)


    result = charp_array_to_py(values, size[0], True)
    return result


def _GetRecordedVariableNames_native(simulation, size):
    return swift_so.GetRecordedVariableNames(simulation, size)

def GetRecordedVariableNames_py(simulation:'Simulation'):
    """GetRecordedVariableNames_py
    
    GetRecordedVariableNames_py: generated wrapper function for API function GetRecordedVariableNames
    
    
    """

    simulation_xptr = wrap_as_pointer_handle(simulation)

    size = marshal.new_int_scalar_ptr()
    values = _GetRecordedVariableNames_native(simulation_xptr.ptr, size)


    result = charp_array_to_py(values, size[0], True)
    return result


def _GetSubareaNames_native(simulation, size):
    return swift_so.GetSubareaNames(simulation, size)

def GetSubareaNames_py(simulation:'Simulation'):
    """GetSubareaNames_py
    
    GetSubareaNames_py: generated wrapper function for API function GetSubareaNames
    
    
    """

    simulation_xptr = wrap_as_pointer_handle(simulation)

    size = marshal.new_int_scalar_ptr()
    values = _GetSubareaNames_native(simulation_xptr.ptr, size)


    result = charp_array_to_py(values, size[0], True)
    return result


def _GetLinkNames_native(simulation, size):
    return swift_so.GetLinkNames(simulation, size)

def GetLinkNames_py(simulation:'Simulation'):
    """GetLinkNames_py
    
    GetLinkNames_py: generated wrapper function for API function GetLinkNames
    
    
    """

    simulation_xptr = wrap_as_pointer_handle(simulation)

    size = marshal.new_int_scalar_ptr()
    values = _GetLinkNames_native(simulation_xptr.ptr, size)


    result = charp_array_to_py(values, size[0], True)
    return result


def _GetNodeNames_native(simulation, size):
    return swift_so.GetNodeNames(simulation, size)

def GetNodeNames_py(simulation:'Simulation'):
    """GetNodeNames_py
    
    GetNodeNames_py: generated wrapper function for API function GetNodeNames
    
    
    """

    simulation_xptr = wrap_as_pointer_handle(simulation)

    size = marshal.new_int_scalar_ptr()
    values = _GetNodeNames_native(simulation_xptr.ptr, size)


    result = charp_array_to_py(values, size[0], True)
    return result


def _GetSubareaIdentifiers_native(simulation, size):
    return swift_so.GetSubareaIdentifiers(simulation, size)

def GetSubareaIdentifiers_py(simulation:'Simulation'):
    """GetSubareaIdentifiers_py
    
    GetSubareaIdentifiers_py: generated wrapper function for API function GetSubareaIdentifiers
    
    
    """

    simulation_xptr = wrap_as_pointer_handle(simulation)

    size = marshal.new_int_scalar_ptr()
    values = _GetSubareaIdentifiers_native(simulation_xptr.ptr, size)


    result = charp_array_to_py(values, size[0], True)
    return result


def _GetLinkIdentifiers_native(simulation, size):
    return swift_so.GetLinkIdentifiers(simulation, size)

def GetLinkIdentifiers_py(simulation:'Simulation'):
    """GetLinkIdentifiers_py
    
    GetLinkIdentifiers_py: generated wrapper function for API function GetLinkIdentifiers
    
    
    """

    simulation_xptr = wrap_as_pointer_handle(simulation)

    size = marshal.new_int_scalar_ptr()
    values = _GetLinkIdentifiers_native(simulation_xptr.ptr, size)


    result = charp_array_to_py(values, size[0], True)
    return result


def _GetNodeIdentifiers_native(simulation, size):
    return swift_so.GetNodeIdentifiers(simulation, size)

def GetNodeIdentifiers_py(simulation:'Simulation'):
    """GetNodeIdentifiers_py
    
    GetNodeIdentifiers_py: generated wrapper function for API function GetNodeIdentifiers
    
    
    """

    simulation_xptr = wrap_as_pointer_handle(simulation)

    size = marshal.new_int_scalar_ptr()
    values = _GetNodeIdentifiers_native(simulation_xptr.ptr, size)


    result = charp_array_to_py(values, size[0], True)
    return result


def _GetElementVarIdentifiers_native(simulation, elementId, size):
    return swift_so.GetElementVarIdentifiers(simulation, elementId, size)

def GetElementVarIdentifiers_py(simulation:'Simulation', elementId:str):
    """GetElementVarIdentifiers_py
    
    GetElementVarIdentifiers_py: generated wrapper function for API function GetElementVarIdentifiers
    
    
    """

    simulation_xptr = wrap_as_pointer_handle(simulation)
    elementId_c_charp = wrap_as_pointer_handle(as_bytes(elementId))

    size = marshal.new_int_scalar_ptr()
    values = _GetElementVarIdentifiers_native(simulation_xptr.ptr, elementId_c_charp.ptr, size)
    # no cleanup for const char*

    result = charp_array_to_py(values, size[0], True)
    return result

@_s_wrap.check_exceptions
def _SetVariable_native(simulation, variableIdentifier, value):
    swift_so.SetVariable(simulation, variableIdentifier, value)

def SetVariable_py(simulation:'Simulation', variableIdentifier:str, value:float) -> None:
    """SetVariable_py
    
    SetVariable_py: generated wrapper function for API function SetVariable
    
    Args:
        simulation ('Simulation'): simulation
        variableIdentifier (str): variableIdentifier
        value (float): value
    
    """
    simulation_xptr = wrap_as_pointer_handle(simulation)
    variableIdentifier_c_charp = wrap_as_pointer_handle(as_bytes(variableIdentifier))
    _SetVariable_native(simulation_xptr.ptr, variableIdentifier_c_charp.ptr, value)
    # no cleanup for const char*


@_s_wrap.check_exceptions
def _SetVariableInt_native(simulation, variableIdentifier, value):
    swift_so.SetVariableInt(simulation, variableIdentifier, value)

def SetVariableInt_py(simulation:'Simulation', variableIdentifier:str, value:int) -> None:
    """SetVariableInt_py
    
    SetVariableInt_py: generated wrapper function for API function SetVariableInt
    
    Args:
        simulation ('Simulation'): simulation
        variableIdentifier (str): variableIdentifier
        value (int): value
    
    """
    simulation_xptr = wrap_as_pointer_handle(simulation)
    variableIdentifier_c_charp = wrap_as_pointer_handle(as_bytes(variableIdentifier))
    _SetVariableInt_native(simulation_xptr.ptr, variableIdentifier_c_charp.ptr, value)
    # no cleanup for const char*


@_s_wrap.check_exceptions
def _SetVariableBool_native(simulation, variableIdentifier, value):
    swift_so.SetVariableBool(simulation, variableIdentifier, value)

def SetVariableBool_py(simulation:'Simulation', variableIdentifier:str, value:bool) -> None:
    """SetVariableBool_py
    
    SetVariableBool_py: generated wrapper function for API function SetVariableBool
    
    Args:
        simulation ('Simulation'): simulation
        variableIdentifier (str): variableIdentifier
        value (bool): value
    
    """
    simulation_xptr = wrap_as_pointer_handle(simulation)
    variableIdentifier_c_charp = wrap_as_pointer_handle(as_bytes(variableIdentifier))
    _SetVariableBool_native(simulation_xptr.ptr, variableIdentifier_c_charp.ptr, value)
    # no cleanup for const char*


@_s_wrap.check_exceptions
def _GetVariable_native(simulation, variableIdentifier):
    result = swift_so.GetVariable(simulation, variableIdentifier)
    return result

def GetVariable_py(simulation:'Simulation', variableIdentifier:str) -> float:
    """GetVariable_py
    
    GetVariable_py: generated wrapper function for API function GetVariable
    
    Args:
        simulation ('Simulation'): simulation
        variableIdentifier (str): variableIdentifier
    
    Returns:
        (float): returned result
    
    """
    simulation_xptr = wrap_as_pointer_handle(simulation)
    variableIdentifier_c_charp = wrap_as_pointer_handle(as_bytes(variableIdentifier))
    result = _GetVariable_native(simulation_xptr.ptr, variableIdentifier_c_charp.ptr)
    # no cleanup for const char*
    return result


@_s_wrap.check_exceptions
def _GetModelConfigurationSwift_native(simulation, elementIdentifier):
    result = swift_so.GetModelConfigurationSwift(simulation, elementIdentifier)
    return result

def GetModelConfigurationSwift_py(simulation:'Simulation', elementIdentifier:str) -> Dict[str,str]:
    """GetModelConfigurationSwift_py
    
    GetModelConfigurationSwift_py: generated wrapper function for API function GetModelConfigurationSwift
    
    Args:
        simulation ('Simulation'): simulation
        elementIdentifier (str): elementIdentifier
    
    Returns:
        (Dict[str,str]): returned result
    
    """
    simulation_xptr = wrap_as_pointer_handle(simulation)
    elementIdentifier_c_charp = wrap_as_pointer_handle(as_bytes(elementIdentifier))
    result = _GetModelConfigurationSwift_native(simulation_xptr.ptr, elementIdentifier_c_charp.ptr)
    # no cleanup for const char*
    return result


@_s_wrap.check_exceptions
def _GetVariableInt_native(simulation, variableIdentifier):
    result = swift_so.GetVariableInt(simulation, variableIdentifier)
    return result

def GetVariableInt_py(simulation:'Simulation', variableIdentifier:str) -> int:
    """GetVariableInt_py
    
    GetVariableInt_py: generated wrapper function for API function GetVariableInt
    
    Args:
        simulation ('Simulation'): simulation
        variableIdentifier (str): variableIdentifier
    
    Returns:
        (int): returned result
    
    """
    simulation_xptr = wrap_as_pointer_handle(simulation)
    variableIdentifier_c_charp = wrap_as_pointer_handle(as_bytes(variableIdentifier))
    result = _GetVariableInt_native(simulation_xptr.ptr, variableIdentifier_c_charp.ptr)
    # no cleanup for const char*
    return result


@_s_wrap.check_exceptions
def _GetVariableBool_native(simulation, variableIdentifier):
    result = swift_so.GetVariableBool(simulation, variableIdentifier)
    return result

def GetVariableBool_py(simulation:'Simulation', variableIdentifier:str) -> bool:
    """GetVariableBool_py
    
    GetVariableBool_py: generated wrapper function for API function GetVariableBool
    
    Args:
        simulation ('Simulation'): simulation
        variableIdentifier (str): variableIdentifier
    
    Returns:
        (bool): returned result
    
    """
    simulation_xptr = wrap_as_pointer_handle(simulation)
    variableIdentifier_c_charp = wrap_as_pointer_handle(as_bytes(variableIdentifier))
    result = _GetVariableBool_native(simulation_xptr.ptr, variableIdentifier_c_charp.ptr)
    # no cleanup for const char*
    return result


@_s_wrap.check_exceptions
def _VariableIsDouble_native(simulation, variableIdentifier):
    result = swift_so.VariableIsDouble(simulation, variableIdentifier)
    return result

def VariableIsDouble_py(simulation:'Simulation', variableIdentifier:str) -> bool:
    """VariableIsDouble_py
    
    VariableIsDouble_py: generated wrapper function for API function VariableIsDouble
    
    Args:
        simulation ('Simulation'): simulation
        variableIdentifier (str): variableIdentifier
    
    Returns:
        (bool): returned result
    
    """
    simulation_xptr = wrap_as_pointer_handle(simulation)
    variableIdentifier_c_charp = wrap_as_pointer_handle(as_bytes(variableIdentifier))
    result = _VariableIsDouble_native(simulation_xptr.ptr, variableIdentifier_c_charp.ptr)
    # no cleanup for const char*
    return result


@_s_wrap.check_exceptions
def _VariableIsInt_native(simulation, variableIdentifier):
    result = swift_so.VariableIsInt(simulation, variableIdentifier)
    return result

def VariableIsInt_py(simulation:'Simulation', variableIdentifier:str) -> bool:
    """VariableIsInt_py
    
    VariableIsInt_py: generated wrapper function for API function VariableIsInt
    
    Args:
        simulation ('Simulation'): simulation
        variableIdentifier (str): variableIdentifier
    
    Returns:
        (bool): returned result
    
    """
    simulation_xptr = wrap_as_pointer_handle(simulation)
    variableIdentifier_c_charp = wrap_as_pointer_handle(as_bytes(variableIdentifier))
    result = _VariableIsInt_native(simulation_xptr.ptr, variableIdentifier_c_charp.ptr)
    # no cleanup for const char*
    return result


@_s_wrap.check_exceptions
def _VariableIsBool_native(simulation, variableIdentifier):
    result = swift_so.VariableIsBool(simulation, variableIdentifier)
    return result

def VariableIsBool_py(simulation:'Simulation', variableIdentifier:str) -> bool:
    """VariableIsBool_py
    
    VariableIsBool_py: generated wrapper function for API function VariableIsBool
    
    Args:
        simulation ('Simulation'): simulation
        variableIdentifier (str): variableIdentifier
    
    Returns:
        (bool): returned result
    
    """
    simulation_xptr = wrap_as_pointer_handle(simulation)
    variableIdentifier_c_charp = wrap_as_pointer_handle(as_bytes(variableIdentifier))
    result = _VariableIsBool_native(simulation_xptr.ptr, variableIdentifier_c_charp.ptr)
    # no cleanup for const char*
    return result


@_s_wrap.check_exceptions
def _CreateEnsembleModelRunner_native(simulation, ensembleSize):
    result = swift_so.CreateEnsembleModelRunner(simulation, ensembleSize)
    return result

def CreateEnsembleModelRunner_py(simulation:'Simulation', ensembleSize:int) -> 'EnsembleSimulation':
    """CreateEnsembleModelRunner_py
    
    CreateEnsembleModelRunner_py: generated wrapper function for API function CreateEnsembleModelRunner
    
    Args:
        simulation ('Simulation'): simulation
        ensembleSize (int): ensembleSize
    
    Returns:
        ('EnsembleSimulation'): returned result
    
    """
    simulation_xptr = wrap_as_pointer_handle(simulation)
    result = _CreateEnsembleModelRunner_native(simulation_xptr.ptr, ensembleSize)
    return custom_wrap_cffi_native_handle(result, 'ENSEMBLE_SIMULATION_PTR')


@_s_wrap.check_exceptions
def _PrepareEnsembleModelRunner_native(simulation, warmupStart, warmupEnd, obsTsValues, obsTsGeom, errorModelElementId):
    result = swift_so.PrepareEnsembleModelRunner(simulation, warmupStart, warmupEnd, obsTsValues, obsTsGeom, errorModelElementId)
    return result

def PrepareEnsembleModelRunner_py(simulation:'Simulation', warmupStart:datetime, warmupEnd:datetime, obsTsValues:np.ndarray, obsTsGeom:TimeSeriesGeometryNative, errorModelElementId:str) -> 'EnsembleSimulation':
    """PrepareEnsembleModelRunner_py
    
    PrepareEnsembleModelRunner_py: generated wrapper function for API function PrepareEnsembleModelRunner
    
    Args:
        simulation ('Simulation'): simulation
        warmupStart (datetime): warmupStart
        warmupEnd (datetime): warmupEnd
        obsTsValues (np.ndarray): obsTsValues
        obsTsGeom (TimeSeriesGeometryNative): obsTsGeom
        errorModelElementId (str): errorModelElementId
    
    Returns:
        ('EnsembleSimulation'): returned result
    
    """
    simulation_xptr = wrap_as_pointer_handle(simulation)
    warmupStart_datetime = marshal.datetime_to_dtts(warmupStart)
    warmupEnd_datetime = marshal.datetime_to_dtts(warmupEnd)
    obsTsValues_numarray = marshal.as_c_double_array(obsTsValues, shallow=True)
    obsTsGeom_xptr = wrap_as_pointer_handle(obsTsGeom)
    errorModelElementId_c_charp = wrap_as_pointer_handle(as_bytes(errorModelElementId))
    result = _PrepareEnsembleModelRunner_native(simulation_xptr.ptr, warmupStart_datetime.obj, warmupEnd_datetime.obj, obsTsValues_numarray.ptr, obsTsGeom_xptr.ptr, errorModelElementId_c_charp.ptr)
    # warmupStart_datetime - no cleanup needed?
    # warmupEnd_datetime - no cleanup needed?
    # obsTsValues_numarray - no cleanup needed?
    # no cleanup for const char*
    return custom_wrap_cffi_native_handle(result, 'ENSEMBLE_SIMULATION_PTR')


@_s_wrap.check_exceptions
def _SetupEnsembleModelRunner_native(emr, forecastStart, ensembleSize, forecastHorizonLength):
    swift_so.SetupEnsembleModelRunner(emr, forecastStart, ensembleSize, forecastHorizonLength)

def SetupEnsembleModelRunner_py(emr:'EnsembleSimulation', forecastStart:datetime, ensembleSize:int, forecastHorizonLength:int) -> None:
    """SetupEnsembleModelRunner_py
    
    SetupEnsembleModelRunner_py: generated wrapper function for API function SetupEnsembleModelRunner
    
    Args:
        emr ('EnsembleSimulation'): emr
        forecastStart (datetime): forecastStart
        ensembleSize (int): ensembleSize
        forecastHorizonLength (int): forecastHorizonLength
    
    """
    emr_xptr = wrap_as_pointer_handle(emr)
    forecastStart_datetime = marshal.datetime_to_dtts(forecastStart)
    _SetupEnsembleModelRunner_native(emr_xptr.ptr, forecastStart_datetime.obj, ensembleSize, forecastHorizonLength)
    # forecastStart_datetime - no cleanup needed?


@_s_wrap.check_exceptions
def _RecordEnsembleModelRunner_native(emr, variableIdentifier):
    swift_so.RecordEnsembleModelRunner(emr, variableIdentifier)

def RecordEnsembleModelRunner_py(emr:'EnsembleSimulation', variableIdentifier:str) -> None:
    """RecordEnsembleModelRunner_py
    
    RecordEnsembleModelRunner_py: generated wrapper function for API function RecordEnsembleModelRunner
    
    Args:
        emr ('EnsembleSimulation'): emr
        variableIdentifier (str): variableIdentifier
    
    """
    emr_xptr = wrap_as_pointer_handle(emr)
    variableIdentifier_c_charp = wrap_as_pointer_handle(as_bytes(variableIdentifier))
    _RecordEnsembleModelRunner_native(emr_xptr.ptr, variableIdentifier_c_charp.ptr)
    # no cleanup for const char*


@_s_wrap.check_exceptions
def _ApplyConfiguration_native(parameterizer, simulation):
    swift_so.ApplyConfiguration(parameterizer, simulation)

def ApplyConfiguration_py(parameterizer:Any, simulation:'Simulation') -> None:
    """ApplyConfiguration_py
    
    ApplyConfiguration_py: generated wrapper function for API function ApplyConfiguration
    
    Args:
        parameterizer (Any): parameterizer
        simulation ('Simulation'): simulation
    
    """
    parameterizer_xptr = wrap_as_pointer_handle(parameterizer)
    simulation_xptr = wrap_as_pointer_handle(simulation)
    _ApplyConfiguration_native(parameterizer_xptr.ptr, simulation_xptr.ptr)


@_s_wrap.check_exceptions
def _SupportsThreadSafeCloning_native(parameterizer):
    result = swift_so.SupportsThreadSafeCloning(parameterizer)
    return result

def SupportsThreadSafeCloning_py(parameterizer:Any) -> bool:
    """SupportsThreadSafeCloning_py
    
    SupportsThreadSafeCloning_py: generated wrapper function for API function SupportsThreadSafeCloning
    
    Args:
        parameterizer (Any): parameterizer
    
    Returns:
        (bool): returned result
    
    """
    parameterizer_xptr = wrap_as_pointer_handle(parameterizer)
    result = _SupportsThreadSafeCloning_native(parameterizer_xptr.ptr)
    return result


@_s_wrap.check_exceptions
def _CloneHypercubeParameterizer_native(hypercubeParameterizer):
    result = swift_so.CloneHypercubeParameterizer(hypercubeParameterizer)
    return result

def CloneHypercubeParameterizer_py(hypercubeParameterizer:'HypercubeParameteriser') -> 'HypercubeParameteriser':
    """CloneHypercubeParameterizer_py
    
    CloneHypercubeParameterizer_py: generated wrapper function for API function CloneHypercubeParameterizer
    
    Args:
        hypercubeParameterizer ('HypercubeParameteriser'): hypercubeParameterizer
    
    Returns:
        ('HypercubeParameteriser'): returned result
    
    """
    hypercubeParameterizer_xptr = wrap_as_pointer_handle(hypercubeParameterizer)
    result = _CloneHypercubeParameterizer_native(hypercubeParameterizer_xptr.ptr)
    return custom_wrap_cffi_native_handle(result, 'HYPERCUBE_PTR')


@_s_wrap.check_exceptions
def _CreateHypercubeParameterizer_native(strategy):
    result = swift_so.CreateHypercubeParameterizer(strategy)
    return result

def CreateHypercubeParameterizer_py(strategy:str) -> 'HypercubeParameteriser':
    """CreateHypercubeParameterizer_py
    
    CreateHypercubeParameterizer_py: generated wrapper function for API function CreateHypercubeParameterizer
    
    Args:
        strategy (str): strategy
    
    Returns:
        ('HypercubeParameteriser'): returned result
    
    """
    strategy_c_charp = wrap_as_pointer_handle(as_bytes(strategy))
    result = _CreateHypercubeParameterizer_native(strategy_c_charp.ptr)
    # no cleanup for const char*
    return custom_wrap_cffi_native_handle(result, 'HYPERCUBE_PTR')


@_s_wrap.check_exceptions
def _CreateSubcatchmentHypercubeParameterizer_native(parameterizer, subcatchment):
    result = swift_so.CreateSubcatchmentHypercubeParameterizer(parameterizer, subcatchment)
    return result

def CreateSubcatchmentHypercubeParameterizer_py(parameterizer:'HypercubeParameteriser', subcatchment:'Simulation') -> 'HypercubeParameteriser':
    """CreateSubcatchmentHypercubeParameterizer_py
    
    CreateSubcatchmentHypercubeParameterizer_py: generated wrapper function for API function CreateSubcatchmentHypercubeParameterizer
    
    Args:
        parameterizer ('HypercubeParameteriser'): parameterizer
        subcatchment ('Simulation'): subcatchment
    
    Returns:
        ('HypercubeParameteriser'): returned result
    
    """
    parameterizer_xptr = wrap_as_pointer_handle(parameterizer)
    subcatchment_xptr = wrap_as_pointer_handle(subcatchment)
    result = _CreateSubcatchmentHypercubeParameterizer_native(parameterizer_xptr.ptr, subcatchment_xptr.ptr)
    return custom_wrap_cffi_native_handle(result, 'HYPERCUBE_PTR')



def _GetKnownParameterizationStrategies_native( size):
    return swift_so.GetKnownParameterizationStrategies( size)

def GetKnownParameterizationStrategies_py():
    """GetKnownParameterizationStrategies_py
    
    GetKnownParameterizationStrategies_py: generated wrapper function for API function GetKnownParameterizationStrategies
    
    
    """



    size = marshal.new_int_scalar_ptr()
    values = _GetKnownParameterizationStrategies_native( size)


    result = charp_array_to_py(values, size[0], True)
    return result

@_s_wrap.check_exceptions
def _UntransformHypercubeParameterizer_native(hypercubeParameterizer):
    result = swift_so.UntransformHypercubeParameterizer(hypercubeParameterizer)
    return result

def UntransformHypercubeParameterizer_py(hypercubeParameterizer:'HypercubeParameteriser') -> 'HypercubeParameteriser':
    """UntransformHypercubeParameterizer_py
    
    UntransformHypercubeParameterizer_py: generated wrapper function for API function UntransformHypercubeParameterizer
    
    Args:
        hypercubeParameterizer ('HypercubeParameteriser'): hypercubeParameterizer
    
    Returns:
        ('HypercubeParameteriser'): returned result
    
    """
    hypercubeParameterizer_xptr = wrap_as_pointer_handle(hypercubeParameterizer)
    result = _UntransformHypercubeParameterizer_native(hypercubeParameterizer_xptr.ptr)
    return custom_wrap_cffi_native_handle(result, 'HYPERCUBE_PTR')


@_s_wrap.check_exceptions
def _HomotheticTransform_native(centre, point, factor):
    result = swift_so.HomotheticTransform(centre, point, factor)
    return result

def HomotheticTransform_py(centre:'HypercubeParameteriser', point:'HypercubeParameteriser', factor:float) -> 'HypercubeParameteriser':
    """HomotheticTransform_py
    
    HomotheticTransform_py: generated wrapper function for API function HomotheticTransform
    
    Args:
        centre ('HypercubeParameteriser'): centre
        point ('HypercubeParameteriser'): point
        factor (float): factor
    
    Returns:
        ('HypercubeParameteriser'): returned result
    
    """
    centre_xptr = wrap_as_pointer_handle(centre)
    point_xptr = wrap_as_pointer_handle(point)
    result = _HomotheticTransform_native(centre_xptr.ptr, point_xptr.ptr, factor)
    return custom_wrap_cffi_native_handle(result, 'HYPERCUBE_PTR')


@_s_wrap.check_exceptions
def _AggregateParameterizers_native(strategy, parameterizers, numParameterizers):
    result = swift_so.AggregateParameterizers(strategy, parameterizers, numParameterizers)
    return result

def AggregateParameterizers_py(strategy:str, parameterizers:Any, numParameterizers:int) -> 'CompositeParameteriser':
    """AggregateParameterizers_py
    
    AggregateParameterizers_py: generated wrapper function for API function AggregateParameterizers
    
    Args:
        strategy (str): strategy
        parameterizers (Any): parameterizers
        numParameterizers (int): numParameterizers
    
    Returns:
        ('CompositeParameteriser'): returned result
    
    """
    strategy_c_charp = wrap_as_pointer_handle(as_bytes(strategy))
    parameterizers_xptr = wrap_as_pointer_handle(parameterizers)
    result = _AggregateParameterizers_native(strategy_c_charp.ptr, parameterizers_xptr.ptr, numParameterizers)
    # no cleanup for const char*
    return custom_wrap_cffi_native_handle(result, 'COMPOSITE_PARAMETERIZER_PTR')


@_s_wrap.check_exceptions
def _TagParameterizer_native(p, tag):
    swift_so.TagParameterizer(p, tag)

def TagParameterizer_py(p:'HypercubeParameteriser', tag:str) -> None:
    """TagParameterizer_py
    
    TagParameterizer_py: generated wrapper function for API function TagParameterizer
    
    Args:
        p ('HypercubeParameteriser'): p
        tag (str): tag
    
    """
    p_xptr = wrap_as_pointer_handle(p)
    tag_c_charp = wrap_as_pointer_handle(as_bytes(tag))
    _TagParameterizer_native(p_xptr.ptr, tag_c_charp.ptr)
    # no cleanup for const char*


@_s_wrap.check_exceptions
def _CreateCompositeParameterizer_native():
    result = swift_so.CreateCompositeParameterizer()
    return result

def CreateCompositeParameterizer_py() -> 'CompositeParameteriser':
    """CreateCompositeParameterizer_py
    
    CreateCompositeParameterizer_py: generated wrapper function for API function CreateCompositeParameterizer
    
    Args:
    
    Returns:
        ('CompositeParameteriser'): returned result
    
    """
    result = _CreateCompositeParameterizer_native()
    return custom_wrap_cffi_native_handle(result, 'COMPOSITE_PARAMETERIZER_PTR')


@_s_wrap.check_exceptions
def _CreateFunctionsParameterizer_native(modelParameters, functionsParameters):
    result = swift_so.CreateFunctionsParameterizer(modelParameters, functionsParameters)
    return result

def CreateFunctionsParameterizer_py(modelParameters:'HypercubeParameteriser', functionsParameters:'HypercubeParameteriser') -> 'FunctionsParameteriser':
    """CreateFunctionsParameterizer_py
    
    CreateFunctionsParameterizer_py: generated wrapper function for API function CreateFunctionsParameterizer
    
    Args:
        modelParameters ('HypercubeParameteriser'): modelParameters
        functionsParameters ('HypercubeParameteriser'): functionsParameters
    
    Returns:
        ('FunctionsParameteriser'): returned result
    
    """
    modelParameters_xptr = wrap_as_pointer_handle(modelParameters)
    functionsParameters_xptr = wrap_as_pointer_handle(functionsParameters)
    result = _CreateFunctionsParameterizer_native(modelParameters_xptr.ptr, functionsParameters_xptr.ptr)
    return custom_wrap_cffi_native_handle(result, 'FUNCTIONS_PARAMETERIZER_PTR')


@_s_wrap.check_exceptions
def _CreateFilteringParameterizer_native(p):
    result = swift_so.CreateFilteringParameterizer(p)
    return result

def CreateFilteringParameterizer_py(p:'HypercubeParameteriser') -> 'FilteringParameteriser':
    """CreateFilteringParameterizer_py
    
    CreateFilteringParameterizer_py: generated wrapper function for API function CreateFilteringParameterizer
    
    Args:
        p ('HypercubeParameteriser'): p
    
    Returns:
        ('FilteringParameteriser'): returned result
    
    """
    p_xptr = wrap_as_pointer_handle(p)
    result = _CreateFilteringParameterizer_native(p_xptr.ptr)
    return custom_wrap_cffi_native_handle(result, 'FILTERING_PARAMETERIZER_PTR')


@_s_wrap.check_exceptions
def _HideParameters_native(p, pnames, regex, startsWith, strict):
    swift_so.HideParameters(p, pnames, regex, startsWith, strict)

def HideParameters_py(p:'HypercubeParameteriser', pnames:List, regex:bool, startsWith:bool, strict:bool) -> None:
    """HideParameters_py
    
    HideParameters_py: generated wrapper function for API function HideParameters
    
    Args:
        p ('HypercubeParameteriser'): p
        pnames (List): pnames
        regex (bool): regex
        startsWith (bool): startsWith
        strict (bool): strict
    
    """
    p_xptr = wrap_as_pointer_handle(p)
    _HideParameters_native(p_xptr.ptr, pnames, regex, startsWith, strict)


@_s_wrap.check_exceptions
def _ShowParameters_native(p, pnames, regex, startsWith):
    swift_so.ShowParameters(p, pnames, regex, startsWith)

def ShowParameters_py(p:'HypercubeParameteriser', pnames:List, regex:bool, startsWith:bool) -> None:
    """ShowParameters_py
    
    ShowParameters_py: generated wrapper function for API function ShowParameters
    
    Args:
        p ('HypercubeParameteriser'): p
        pnames (List): pnames
        regex (bool): regex
        startsWith (bool): startsWith
    
    """
    p_xptr = wrap_as_pointer_handle(p)
    _ShowParameters_native(p_xptr.ptr, pnames, regex, startsWith)


@_s_wrap.check_exceptions
def _CreatePrefixingParameterizer_native(p, prefix):
    result = swift_so.CreatePrefixingParameterizer(p, prefix)
    return result

def CreatePrefixingParameterizer_py(p:'HypercubeParameteriser', prefix:str) -> 'HypercubeParameteriser':
    """CreatePrefixingParameterizer_py
    
    CreatePrefixingParameterizer_py: generated wrapper function for API function CreatePrefixingParameterizer
    
    Args:
        p ('HypercubeParameteriser'): p
        prefix (str): prefix
    
    Returns:
        ('HypercubeParameteriser'): returned result
    
    """
    p_xptr = wrap_as_pointer_handle(p)
    prefix_c_charp = wrap_as_pointer_handle(as_bytes(prefix))
    result = _CreatePrefixingParameterizer_native(p_xptr.ptr, prefix_c_charp.ptr)
    # no cleanup for const char*
    return custom_wrap_cffi_native_handle(result, 'HYPERCUBE_PTR')


@_s_wrap.check_exceptions
def _AddToCompositeParameterizer_native(compositeParameterizer, parameterizer):
    swift_so.AddToCompositeParameterizer(compositeParameterizer, parameterizer)

def AddToCompositeParameterizer_py(compositeParameterizer:'CompositeParameteriser', parameterizer:'HypercubeParameteriser') -> None:
    """AddToCompositeParameterizer_py
    
    AddToCompositeParameterizer_py: generated wrapper function for API function AddToCompositeParameterizer
    
    Args:
        compositeParameterizer ('CompositeParameteriser'): compositeParameterizer
        parameterizer ('HypercubeParameteriser'): parameterizer
    
    """
    compositeParameterizer_xptr = wrap_as_pointer_handle(compositeParameterizer)
    parameterizer_xptr = wrap_as_pointer_handle(parameterizer)
    _AddToCompositeParameterizer_native(compositeParameterizer_xptr.ptr, parameterizer_xptr.ptr)


@_s_wrap.check_exceptions
def _WrapObjectiveEvaluatorWila_native(objective, clone):
    result = swift_so.WrapObjectiveEvaluatorWila(objective, clone)
    return result

def WrapObjectiveEvaluatorWila_py(objective:'DeletableCffiNativeHandle', clone:bool) -> 'ObjectiveEvaluator':
    """WrapObjectiveEvaluatorWila_py
    
    WrapObjectiveEvaluatorWila_py: generated wrapper function for API function WrapObjectiveEvaluatorWila
    
    Args:
        objective ('DeletableCffiNativeHandle'): objective
        clone (bool): clone
    
    Returns:
        ('ObjectiveEvaluator'): returned result
    
    """
    objective_xptr = wrap_as_pointer_handle(objective)
    result = _WrapObjectiveEvaluatorWila_native(objective_xptr.ptr, clone)
    return custom_wrap_cffi_native_handle(result, 'OBJECTIVE_EVALUATOR_WILA_PTR')


@_s_wrap.check_exceptions
def _UnwrapObjectiveEvaluatorWila_native(objective):
    result = swift_so.UnwrapObjectiveEvaluatorWila(objective)
    return result

def UnwrapObjectiveEvaluatorWila_py(objective:'ObjectiveEvaluator') -> 'DeletableCffiNativeHandle':
    """UnwrapObjectiveEvaluatorWila_py
    
    UnwrapObjectiveEvaluatorWila_py: generated wrapper function for API function UnwrapObjectiveEvaluatorWila
    
    Args:
        objective ('ObjectiveEvaluator'): objective
    
    Returns:
        ('DeletableCffiNativeHandle'): returned result
    
    """
    objective_xptr = wrap_as_pointer_handle(objective)
    result = _UnwrapObjectiveEvaluatorWila_native(objective_xptr.ptr)
    return custom_wrap_cffi_native_handle(result, 'OBJECTIVE_EVALUATOR_PTR')



def _GetKnownParameterizerAggregationStrategies_native( size):
    return swift_so.GetKnownParameterizerAggregationStrategies( size)

def GetKnownParameterizerAggregationStrategies_py():
    """GetKnownParameterizerAggregationStrategies_py
    
    GetKnownParameterizerAggregationStrategies_py: generated wrapper function for API function GetKnownParameterizerAggregationStrategies
    
    
    """



    size = marshal.new_int_scalar_ptr()
    values = _GetKnownParameterizerAggregationStrategies_native( size)


    result = charp_array_to_py(values, size[0], True)
    return result

@_s_wrap.check_exceptions
def _CreateGr4ScaledParameterizer_native(referenceAreaKm2, tStepSeconds):
    result = swift_so.CreateGr4ScaledParameterizer(referenceAreaKm2, tStepSeconds)
    return result

def CreateGr4ScaledParameterizer_py(referenceAreaKm2:float, tStepSeconds:int) -> 'CompositeParameteriser':
    """CreateGr4ScaledParameterizer_py
    
    CreateGr4ScaledParameterizer_py: generated wrapper function for API function CreateGr4ScaledParameterizer
    
    Args:
        referenceAreaKm2 (float): referenceAreaKm2
        tStepSeconds (int): tStepSeconds
    
    Returns:
        ('CompositeParameteriser'): returned result
    
    """
    result = _CreateGr4ScaledParameterizer_native(referenceAreaKm2, tStepSeconds)
    return custom_wrap_cffi_native_handle(result, 'COMPOSITE_PARAMETERIZER_PTR')


@_s_wrap.check_exceptions
def _CreateStateInitParameterizer_native(hypercubeParameterizer):
    result = swift_so.CreateStateInitParameterizer(hypercubeParameterizer)
    return result

def CreateStateInitParameterizer_py(hypercubeParameterizer:'HypercubeParameteriser') -> 'StateInitParameteriser':
    """CreateStateInitParameterizer_py
    
    CreateStateInitParameterizer_py: generated wrapper function for API function CreateStateInitParameterizer
    
    Args:
        hypercubeParameterizer ('HypercubeParameteriser'): hypercubeParameterizer
    
    Returns:
        ('StateInitParameteriser'): returned result
    
    """
    hypercubeParameterizer_xptr = wrap_as_pointer_handle(hypercubeParameterizer)
    result = _CreateStateInitParameterizer_native(hypercubeParameterizer_xptr.ptr)
    return custom_wrap_cffi_native_handle(result, 'STATE_INIT_PARAMETERIZER_PTR')


@_s_wrap.check_exceptions
def _CreateTransformParameterizer_native(hypercubeParameterizer):
    result = swift_so.CreateTransformParameterizer(hypercubeParameterizer)
    return result

def CreateTransformParameterizer_py(hypercubeParameterizer:'HypercubeParameteriser') -> 'TransformParameteriser':
    """CreateTransformParameterizer_py
    
    CreateTransformParameterizer_py: generated wrapper function for API function CreateTransformParameterizer
    
    Args:
        hypercubeParameterizer ('HypercubeParameteriser'): hypercubeParameterizer
    
    Returns:
        ('TransformParameteriser'): returned result
    
    """
    hypercubeParameterizer_xptr = wrap_as_pointer_handle(hypercubeParameterizer)
    result = _CreateTransformParameterizer_native(hypercubeParameterizer_xptr.ptr)
    return custom_wrap_cffi_native_handle(result, 'TRANSFORM_PARAMETERIZER_PTR')


@_s_wrap.check_exceptions
def _CreateMuskingumConstraint_native(hypercubeParameterizer, deltaTHours, paramNameK, paramNameX, simulation):
    result = swift_so.CreateMuskingumConstraint(hypercubeParameterizer, deltaTHours, paramNameK, paramNameX, simulation)
    return result

def CreateMuskingumConstraint_py(hypercubeParameterizer:'HypercubeParameteriser', deltaTHours:float, paramNameK:str, paramNameX:str, simulation:'Simulation') -> 'ConstraintParameteriser':
    """CreateMuskingumConstraint_py
    
    CreateMuskingumConstraint_py: generated wrapper function for API function CreateMuskingumConstraint
    
    Args:
        hypercubeParameterizer ('HypercubeParameteriser'): hypercubeParameterizer
        deltaTHours (float): deltaTHours
        paramNameK (str): paramNameK
        paramNameX (str): paramNameX
        simulation ('Simulation'): simulation
    
    Returns:
        ('ConstraintParameteriser'): returned result
    
    """
    hypercubeParameterizer_xptr = wrap_as_pointer_handle(hypercubeParameterizer)
    paramNameK_c_charp = wrap_as_pointer_handle(as_bytes(paramNameK))
    paramNameX_c_charp = wrap_as_pointer_handle(as_bytes(paramNameX))
    simulation_xptr = wrap_as_pointer_handle(simulation)
    result = _CreateMuskingumConstraint_native(hypercubeParameterizer_xptr.ptr, deltaTHours, paramNameK_c_charp.ptr, paramNameX_c_charp.ptr, simulation_xptr.ptr)
    # no cleanup for const char*
    # no cleanup for const char*
    return custom_wrap_cffi_native_handle(result, 'CONSTRAINT_PARAMETERIZER_PTR')


@_s_wrap.check_exceptions
def _GetFeasibleMuskingumBounds_native(simulation, deltaTHours):
    result = swift_so.GetFeasibleMuskingumBounds(simulation, deltaTHours)
    return result

def GetFeasibleMuskingumBounds_py(simulation:'Simulation', deltaTHours:float) -> Dict[str,float]:
    """GetFeasibleMuskingumBounds_py
    
    GetFeasibleMuskingumBounds_py: generated wrapper function for API function GetFeasibleMuskingumBounds
    
    Args:
        simulation ('Simulation'): simulation
        deltaTHours (float): deltaTHours
    
    Returns:
        (Dict[str,float]): returned result
    
    """
    simulation_xptr = wrap_as_pointer_handle(simulation)
    result = _GetFeasibleMuskingumBounds_native(simulation_xptr.ptr, deltaTHours)
    return named_values_to_py(result, dispose=True)


@_s_wrap.check_exceptions
def _DisposeNamedValuedVectorsSwift_native(v):
    swift_so.DisposeNamedValuedVectorsSwift(v)

def DisposeNamedValuedVectorsSwift_py(v:Dict[str,float]) -> None:
    """DisposeNamedValuedVectorsSwift_py
    
    DisposeNamedValuedVectorsSwift_py: generated wrapper function for API function DisposeNamedValuedVectorsSwift
    
    Args:
        v (Dict[str,float]): v
    
    """
    v_nvv = marshal.dict_to_named_values(v)
    _DisposeNamedValuedVectorsSwift_native(v_nvv.ptr)
    # v_nvv - no cleanup needed?


@_s_wrap.check_exceptions
def _DisposeStringStringMapSwift_native(v):
    swift_so.DisposeStringStringMapSwift(v)

def DisposeStringStringMapSwift_py(v:Dict[str,str]) -> None:
    """DisposeStringStringMapSwift_py
    
    DisposeStringStringMapSwift_py: generated wrapper function for API function DisposeStringStringMapSwift
    
    Args:
        v (Dict[str,str]): v
    
    """
    v_dict = marshal.dict_to_string_map(v)
    _DisposeStringStringMapSwift_native(v_dict.ptr)
    # v_dict - no cleanup needed?


@_s_wrap.check_exceptions
def _CreateTargetScalingParameterizer_native(selectorType):
    result = swift_so.CreateTargetScalingParameterizer(selectorType)
    return result

def CreateTargetScalingParameterizer_py(selectorType:str) -> 'ScalingParameteriser':
    """CreateTargetScalingParameterizer_py
    
    CreateTargetScalingParameterizer_py: generated wrapper function for API function CreateTargetScalingParameterizer
    
    Args:
        selectorType (str): selectorType
    
    Returns:
        ('ScalingParameteriser'): returned result
    
    """
    selectorType_c_charp = wrap_as_pointer_handle(as_bytes(selectorType))
    result = _CreateTargetScalingParameterizer_native(selectorType_c_charp.ptr)
    # no cleanup for const char*
    return custom_wrap_cffi_native_handle(result, 'SCALING_PARAMETERIZER_PTR')



def _GetKnownParameterizationTargetSelectorTypes_native( size):
    return swift_so.GetKnownParameterizationTargetSelectorTypes( size)

def GetKnownParameterizationTargetSelectorTypes_py():
    """GetKnownParameterizationTargetSelectorTypes_py
    
    GetKnownParameterizationTargetSelectorTypes_py: generated wrapper function for API function GetKnownParameterizationTargetSelectorTypes
    
    
    """



    size = marshal.new_int_scalar_ptr()
    values = _GetKnownParameterizationTargetSelectorTypes_native( size)


    result = charp_array_to_py(values, size[0], True)
    return result

@_s_wrap.check_exceptions
def _CreateLinearFuncParameterizer_native(paramName, innerParamName, observedState, constant, min, max, value, selectorType):
    result = swift_so.CreateLinearFuncParameterizer(paramName, innerParamName, observedState, constant, min, max, value, selectorType)
    return result

def CreateLinearFuncParameterizer_py(paramName:str, innerParamName:str, observedState:str, constant:float, min:float, max:float, value:float, selectorType:str) -> 'ScalingParameteriser':
    """CreateLinearFuncParameterizer_py
    
    CreateLinearFuncParameterizer_py: generated wrapper function for API function CreateLinearFuncParameterizer
    
    Args:
        paramName (str): paramName
        innerParamName (str): innerParamName
        observedState (str): observedState
        constant (float): constant
        min (float): min
        max (float): max
        value (float): value
        selectorType (str): selectorType
    
    Returns:
        ('ScalingParameteriser'): returned result
    
    """
    paramName_c_charp = wrap_as_pointer_handle(as_bytes(paramName))
    innerParamName_c_charp = wrap_as_pointer_handle(as_bytes(innerParamName))
    observedState_c_charp = wrap_as_pointer_handle(as_bytes(observedState))
    selectorType_c_charp = wrap_as_pointer_handle(as_bytes(selectorType))
    result = _CreateLinearFuncParameterizer_native(paramName_c_charp.ptr, innerParamName_c_charp.ptr, observedState_c_charp.ptr, constant, min, max, value, selectorType_c_charp.ptr)
    # no cleanup for const char*
    # no cleanup for const char*
    # no cleanup for const char*
    # no cleanup for const char*
    return custom_wrap_cffi_native_handle(result, 'SCALING_PARAMETERIZER_PTR')


@_s_wrap.check_exceptions
def _CreateSqrtAreaRatioParameterizer_native(referenceAreaKm2, paramName, innerParamName, min, max, value):
    result = swift_so.CreateSqrtAreaRatioParameterizer(referenceAreaKm2, paramName, innerParamName, min, max, value)
    return result

def CreateSqrtAreaRatioParameterizer_py(referenceAreaKm2:float, paramName:str, innerParamName:str, min:float, max:float, value:float) -> 'DeletableCffiNativeHandle':
    """CreateSqrtAreaRatioParameterizer_py
    
    CreateSqrtAreaRatioParameterizer_py: generated wrapper function for API function CreateSqrtAreaRatioParameterizer
    
    Args:
        referenceAreaKm2 (float): referenceAreaKm2
        paramName (str): paramName
        innerParamName (str): innerParamName
        min (float): min
        max (float): max
        value (float): value
    
    Returns:
        ('DeletableCffiNativeHandle'): returned result
    
    """
    paramName_c_charp = wrap_as_pointer_handle(as_bytes(paramName))
    innerParamName_c_charp = wrap_as_pointer_handle(as_bytes(innerParamName))
    result = _CreateSqrtAreaRatioParameterizer_native(referenceAreaKm2, paramName_c_charp.ptr, innerParamName_c_charp.ptr, min, max, value)
    # no cleanup for const char*
    # no cleanup for const char*
    return custom_wrap_cffi_native_handle(result, 'SUBAREAS_SCALING_PARAMETERIZER_PTR')


@_s_wrap.check_exceptions
def _GetParameterMinValue_native(hypercubeParameterizer, variableName):
    result = swift_so.GetParameterMinValue(hypercubeParameterizer, variableName)
    return result

def GetParameterMinValue_py(hypercubeParameterizer:'HypercubeParameteriser', variableName:str) -> float:
    """GetParameterMinValue_py
    
    GetParameterMinValue_py: generated wrapper function for API function GetParameterMinValue
    
    Args:
        hypercubeParameterizer ('HypercubeParameteriser'): hypercubeParameterizer
        variableName (str): variableName
    
    Returns:
        (float): returned result
    
    """
    hypercubeParameterizer_xptr = wrap_as_pointer_handle(hypercubeParameterizer)
    variableName_c_charp = wrap_as_pointer_handle(as_bytes(variableName))
    result = _GetParameterMinValue_native(hypercubeParameterizer_xptr.ptr, variableName_c_charp.ptr)
    # no cleanup for const char*
    return result


@_s_wrap.check_exceptions
def _GetParameterMaxValue_native(hypercubeParameterizer, variableName):
    result = swift_so.GetParameterMaxValue(hypercubeParameterizer, variableName)
    return result

def GetParameterMaxValue_py(hypercubeParameterizer:'HypercubeParameteriser', variableName:str) -> float:
    """GetParameterMaxValue_py
    
    GetParameterMaxValue_py: generated wrapper function for API function GetParameterMaxValue
    
    Args:
        hypercubeParameterizer ('HypercubeParameteriser'): hypercubeParameterizer
        variableName (str): variableName
    
    Returns:
        (float): returned result
    
    """
    hypercubeParameterizer_xptr = wrap_as_pointer_handle(hypercubeParameterizer)
    variableName_c_charp = wrap_as_pointer_handle(as_bytes(variableName))
    result = _GetParameterMaxValue_native(hypercubeParameterizer_xptr.ptr, variableName_c_charp.ptr)
    # no cleanup for const char*
    return result


@_s_wrap.check_exceptions
def _GetParameterValue_native(hypercubeParameterizer, variableName):
    result = swift_so.GetParameterValue(hypercubeParameterizer, variableName)
    return result

def GetParameterValue_py(hypercubeParameterizer:'HypercubeParameteriser', variableName:str) -> float:
    """GetParameterValue_py
    
    GetParameterValue_py: generated wrapper function for API function GetParameterValue
    
    Args:
        hypercubeParameterizer ('HypercubeParameteriser'): hypercubeParameterizer
        variableName (str): variableName
    
    Returns:
        (float): returned result
    
    """
    hypercubeParameterizer_xptr = wrap_as_pointer_handle(hypercubeParameterizer)
    variableName_c_charp = wrap_as_pointer_handle(as_bytes(variableName))
    result = _GetParameterValue_native(hypercubeParameterizer_xptr.ptr, variableName_c_charp.ptr)
    # no cleanup for const char*
    return result


@_s_wrap.check_exceptions
def _GetNumParameters_native(hypercubeParameterizer):
    result = swift_so.GetNumParameters(hypercubeParameterizer)
    return result

def GetNumParameters_py(hypercubeParameterizer:'HypercubeParameteriser') -> int:
    """GetNumParameters_py
    
    GetNumParameters_py: generated wrapper function for API function GetNumParameters
    
    Args:
        hypercubeParameterizer ('HypercubeParameteriser'): hypercubeParameterizer
    
    Returns:
        (int): returned result
    
    """
    hypercubeParameterizer_xptr = wrap_as_pointer_handle(hypercubeParameterizer)
    result = _GetNumParameters_native(hypercubeParameterizer_xptr.ptr)
    return result


@_s_wrap.check_exceptions
def _GetParameterName_native(hypercubeParameterizer, index):
    result = swift_so.GetParameterName(hypercubeParameterizer, index)
    return result

def GetParameterName_py(hypercubeParameterizer:'HypercubeParameteriser', index:int) -> str:
    """GetParameterName_py
    
    GetParameterName_py: generated wrapper function for API function GetParameterName
    
    Args:
        hypercubeParameterizer ('HypercubeParameteriser'): hypercubeParameterizer
        index (int): index
    
    Returns:
        (str): returned result
    
    """
    hypercubeParameterizer_xptr = wrap_as_pointer_handle(hypercubeParameterizer)
    result = _GetParameterName_native(hypercubeParameterizer_xptr.ptr, index)
    return char_array_to_py(result, dispose=True)


@_s_wrap.check_exceptions
def _IsWithinBounds_native(hypercubeParameterizer):
    result = swift_so.IsWithinBounds(hypercubeParameterizer)
    return result

def IsWithinBounds_py(hypercubeParameterizer:'HypercubeParameteriser') -> bool:
    """IsWithinBounds_py
    
    IsWithinBounds_py: generated wrapper function for API function IsWithinBounds
    
    Args:
        hypercubeParameterizer ('HypercubeParameteriser'): hypercubeParameterizer
    
    Returns:
        (bool): returned result
    
    """
    hypercubeParameterizer_xptr = wrap_as_pointer_handle(hypercubeParameterizer)
    result = _IsWithinBounds_native(hypercubeParameterizer_xptr.ptr)
    return result


@_s_wrap.check_exceptions
def _SetParameterValue_native(hypercubeParameterizer, variableName, value):
    swift_so.SetParameterValue(hypercubeParameterizer, variableName, value)

def SetParameterValue_py(hypercubeParameterizer:'HypercubeParameteriser', variableName:str, value:float) -> None:
    """SetParameterValue_py
    
    SetParameterValue_py: generated wrapper function for API function SetParameterValue
    
    Args:
        hypercubeParameterizer ('HypercubeParameteriser'): hypercubeParameterizer
        variableName (str): variableName
        value (float): value
    
    """
    hypercubeParameterizer_xptr = wrap_as_pointer_handle(hypercubeParameterizer)
    variableName_c_charp = wrap_as_pointer_handle(as_bytes(variableName))
    _SetParameterValue_native(hypercubeParameterizer_xptr.ptr, variableName_c_charp.ptr, value)
    # no cleanup for const char*


@_s_wrap.check_exceptions
def _SetMaxParameterValue_native(hypercubeParameterizer, variableName, value):
    swift_so.SetMaxParameterValue(hypercubeParameterizer, variableName, value)

def SetMaxParameterValue_py(hypercubeParameterizer:'HypercubeParameteriser', variableName:str, value:float) -> None:
    """SetMaxParameterValue_py
    
    SetMaxParameterValue_py: generated wrapper function for API function SetMaxParameterValue
    
    Args:
        hypercubeParameterizer ('HypercubeParameteriser'): hypercubeParameterizer
        variableName (str): variableName
        value (float): value
    
    """
    hypercubeParameterizer_xptr = wrap_as_pointer_handle(hypercubeParameterizer)
    variableName_c_charp = wrap_as_pointer_handle(as_bytes(variableName))
    _SetMaxParameterValue_native(hypercubeParameterizer_xptr.ptr, variableName_c_charp.ptr, value)
    # no cleanup for const char*


@_s_wrap.check_exceptions
def _SetMinParameterValue_native(hypercubeParameterizer, variableName, value):
    swift_so.SetMinParameterValue(hypercubeParameterizer, variableName, value)

def SetMinParameterValue_py(hypercubeParameterizer:'HypercubeParameteriser', variableName:str, value:float) -> None:
    """SetMinParameterValue_py
    
    SetMinParameterValue_py: generated wrapper function for API function SetMinParameterValue
    
    Args:
        hypercubeParameterizer ('HypercubeParameteriser'): hypercubeParameterizer
        variableName (str): variableName
        value (float): value
    
    """
    hypercubeParameterizer_xptr = wrap_as_pointer_handle(hypercubeParameterizer)
    variableName_c_charp = wrap_as_pointer_handle(as_bytes(variableName))
    _SetMinParameterValue_native(hypercubeParameterizer_xptr.ptr, variableName_c_charp.ptr, value)
    # no cleanup for const char*


@_s_wrap.check_exceptions
def _AddParameterDefinition_native(hypercubeParameterizer, variableName, min, max, value):
    swift_so.AddParameterDefinition(hypercubeParameterizer, variableName, min, max, value)

def AddParameterDefinition_py(hypercubeParameterizer:'HypercubeParameteriser', variableName:str, min:float, max:float, value:float) -> None:
    """AddParameterDefinition_py
    
    AddParameterDefinition_py: generated wrapper function for API function AddParameterDefinition
    
    Args:
        hypercubeParameterizer ('HypercubeParameteriser'): hypercubeParameterizer
        variableName (str): variableName
        min (float): min
        max (float): max
        value (float): value
    
    """
    hypercubeParameterizer_xptr = wrap_as_pointer_handle(hypercubeParameterizer)
    variableName_c_charp = wrap_as_pointer_handle(as_bytes(variableName))
    _AddParameterDefinition_native(hypercubeParameterizer_xptr.ptr, variableName_c_charp.ptr, min, max, value)
    # no cleanup for const char*


@_s_wrap.check_exceptions
def _SetParameterDefinition_native(hypercubeParameterizer, variableName, min, max, value):
    swift_so.SetParameterDefinition(hypercubeParameterizer, variableName, min, max, value)

def SetParameterDefinition_py(hypercubeParameterizer:'HypercubeParameteriser', variableName:str, min:float, max:float, value:float) -> None:
    """SetParameterDefinition_py
    
    SetParameterDefinition_py: generated wrapper function for API function SetParameterDefinition
    
    Args:
        hypercubeParameterizer ('HypercubeParameteriser'): hypercubeParameterizer
        variableName (str): variableName
        min (float): min
        max (float): max
        value (float): value
    
    """
    hypercubeParameterizer_xptr = wrap_as_pointer_handle(hypercubeParameterizer)
    variableName_c_charp = wrap_as_pointer_handle(as_bytes(variableName))
    _SetParameterDefinition_native(hypercubeParameterizer_xptr.ptr, variableName_c_charp.ptr, min, max, value)
    # no cleanup for const char*


@_s_wrap.check_exceptions
def _SetDefaultParameters_native(hypercubeParameterizer, modelId):
    swift_so.SetDefaultParameters(hypercubeParameterizer, modelId)

def SetDefaultParameters_py(hypercubeParameterizer:'HypercubeParameteriser', modelId:str) -> None:
    """SetDefaultParameters_py
    
    SetDefaultParameters_py: generated wrapper function for API function SetDefaultParameters
    
    Args:
        hypercubeParameterizer ('HypercubeParameteriser'): hypercubeParameterizer
        modelId (str): modelId
    
    """
    hypercubeParameterizer_xptr = wrap_as_pointer_handle(hypercubeParameterizer)
    modelId_c_charp = wrap_as_pointer_handle(as_bytes(modelId))
    _SetDefaultParameters_native(hypercubeParameterizer_xptr.ptr, modelId_c_charp.ptr)
    # no cleanup for const char*


@_s_wrap.check_exceptions
def _AddLinearScalingParameterizer_native(scalingParameterizer, paramName, stateName, scalingVarName, constant, min, max, value):
    swift_so.AddLinearScalingParameterizer(scalingParameterizer, paramName, stateName, scalingVarName, constant, min, max, value)

def AddLinearScalingParameterizer_py(scalingParameterizer:'ScalingParameteriser', paramName:str, stateName:str, scalingVarName:str, constant:float, min:float, max:float, value:float) -> None:
    """AddLinearScalingParameterizer_py
    
    AddLinearScalingParameterizer_py: generated wrapper function for API function AddLinearScalingParameterizer
    
    Args:
        scalingParameterizer ('ScalingParameteriser'): scalingParameterizer
        paramName (str): paramName
        stateName (str): stateName
        scalingVarName (str): scalingVarName
        constant (float): constant
        min (float): min
        max (float): max
        value (float): value
    
    """
    scalingParameterizer_xptr = wrap_as_pointer_handle(scalingParameterizer)
    paramName_c_charp = wrap_as_pointer_handle(as_bytes(paramName))
    stateName_c_charp = wrap_as_pointer_handle(as_bytes(stateName))
    scalingVarName_c_charp = wrap_as_pointer_handle(as_bytes(scalingVarName))
    _AddLinearScalingParameterizer_native(scalingParameterizer_xptr.ptr, paramName_c_charp.ptr, stateName_c_charp.ptr, scalingVarName_c_charp.ptr, constant, min, max, value)
    # no cleanup for const char*
    # no cleanup for const char*
    # no cleanup for const char*


@_s_wrap.check_exceptions
def _AddParameterTransform_native(transformParameterizer, paramName, innerParamName, transformId, a, b):
    swift_so.AddParameterTransform(transformParameterizer, paramName, innerParamName, transformId, a, b)

def AddParameterTransform_py(transformParameterizer:'TransformParameteriser', paramName:str, innerParamName:str, transformId:str, a:float, b:float) -> None:
    """AddParameterTransform_py
    
    AddParameterTransform_py: generated wrapper function for API function AddParameterTransform
    
    Args:
        transformParameterizer ('TransformParameteriser'): transformParameterizer
        paramName (str): paramName
        innerParamName (str): innerParamName
        transformId (str): transformId
        a (float): a
        b (float): b
    
    """
    transformParameterizer_xptr = wrap_as_pointer_handle(transformParameterizer)
    paramName_c_charp = wrap_as_pointer_handle(as_bytes(paramName))
    innerParamName_c_charp = wrap_as_pointer_handle(as_bytes(innerParamName))
    transformId_c_charp = wrap_as_pointer_handle(as_bytes(transformId))
    _AddParameterTransform_native(transformParameterizer_xptr.ptr, paramName_c_charp.ptr, innerParamName_c_charp.ptr, transformId_c_charp.ptr, a, b)
    # no cleanup for const char*
    # no cleanup for const char*
    # no cleanup for const char*


@_s_wrap.check_exceptions
def _CreateSingleObservationObjectiveEvaluator_native(simulation, obsVarId, observations, obsGeom, statisticId):
    result = swift_so.CreateSingleObservationObjectiveEvaluator(simulation, obsVarId, observations, obsGeom, statisticId)
    return result

def CreateSingleObservationObjectiveEvaluator_py(simulation:'Simulation', obsVarId:str, observations:np.ndarray, obsGeom:TimeSeriesGeometryNative, statisticId:str) -> 'DeletableCffiNativeHandle':
    """CreateSingleObservationObjectiveEvaluator_py
    
    CreateSingleObservationObjectiveEvaluator_py: generated wrapper function for API function CreateSingleObservationObjectiveEvaluator
    
    Args:
        simulation ('Simulation'): simulation
        obsVarId (str): obsVarId
        observations (np.ndarray): observations
        obsGeom (TimeSeriesGeometryNative): obsGeom
        statisticId (str): statisticId
    
    Returns:
        ('DeletableCffiNativeHandle'): returned result
    
    """
    simulation_xptr = wrap_as_pointer_handle(simulation)
    obsVarId_c_charp = wrap_as_pointer_handle(as_bytes(obsVarId))
    observations_numarray = marshal.as_c_double_array(observations, shallow=True)
    obsGeom_xptr = wrap_as_pointer_handle(obsGeom)
    statisticId_c_charp = wrap_as_pointer_handle(as_bytes(statisticId))
    result = _CreateSingleObservationObjectiveEvaluator_native(simulation_xptr.ptr, obsVarId_c_charp.ptr, observations_numarray.ptr, obsGeom_xptr.ptr, statisticId_c_charp.ptr)
    # no cleanup for const char*
    # observations_numarray - no cleanup needed?
    # no cleanup for const char*
    return custom_wrap_cffi_native_handle(result, 'OBJECTIVE_EVALUATOR_PTR')


@_s_wrap.check_exceptions
def _CreateEmptyCompositeObjectiveEvaluator_native():
    result = swift_so.CreateEmptyCompositeObjectiveEvaluator()
    return result

def CreateEmptyCompositeObjectiveEvaluator_py() -> 'DeletableCffiNativeHandle':
    """CreateEmptyCompositeObjectiveEvaluator_py
    
    CreateEmptyCompositeObjectiveEvaluator_py: generated wrapper function for API function CreateEmptyCompositeObjectiveEvaluator
    
    Args:
    
    Returns:
        ('DeletableCffiNativeHandle'): returned result
    
    """
    result = _CreateEmptyCompositeObjectiveEvaluator_native()
    return custom_wrap_cffi_native_handle(result, 'OBJECTIVE_EVALUATOR_PTR')


@_s_wrap.check_exceptions
def _AddSingleObservationObjectiveEvaluator_native(compositeObjective, singleObjective, weight, name):
    swift_so.AddSingleObservationObjectiveEvaluator(compositeObjective, singleObjective, weight, name)

def AddSingleObservationObjectiveEvaluator_py(compositeObjective:'DeletableCffiNativeHandle', singleObjective:'DeletableCffiNativeHandle', weight:float, name:str) -> None:
    """AddSingleObservationObjectiveEvaluator_py
    
    AddSingleObservationObjectiveEvaluator_py: generated wrapper function for API function AddSingleObservationObjectiveEvaluator
    
    Args:
        compositeObjective ('DeletableCffiNativeHandle'): compositeObjective
        singleObjective ('DeletableCffiNativeHandle'): singleObjective
        weight (float): weight
        name (str): name
    
    """
    compositeObjective_xptr = wrap_as_pointer_handle(compositeObjective)
    singleObjective_xptr = wrap_as_pointer_handle(singleObjective)
    name_c_charp = wrap_as_pointer_handle(as_bytes(name))
    _AddSingleObservationObjectiveEvaluator_native(compositeObjective_xptr.ptr, singleObjective_xptr.ptr, weight, name_c_charp.ptr)
    # no cleanup for const char*


@_s_wrap.check_exceptions
def _CreateCompositeObservationObjectiveEvaluator_native(simulation, obsVarId, observations, obsGeom, yamlStatIdString):
    result = swift_so.CreateCompositeObservationObjectiveEvaluator(simulation, obsVarId, observations, obsGeom, yamlStatIdString)
    return result

def CreateCompositeObservationObjectiveEvaluator_py(simulation:'Simulation', obsVarId:str, observations:np.ndarray, obsGeom:TimeSeriesGeometryNative, yamlStatIdString:str) -> 'DeletableCffiNativeHandle':
    """CreateCompositeObservationObjectiveEvaluator_py
    
    CreateCompositeObservationObjectiveEvaluator_py: generated wrapper function for API function CreateCompositeObservationObjectiveEvaluator
    
    Args:
        simulation ('Simulation'): simulation
        obsVarId (str): obsVarId
        observations (np.ndarray): observations
        obsGeom (TimeSeriesGeometryNative): obsGeom
        yamlStatIdString (str): yamlStatIdString
    
    Returns:
        ('DeletableCffiNativeHandle'): returned result
    
    """
    simulation_xptr = wrap_as_pointer_handle(simulation)
    obsVarId_c_charp = wrap_as_pointer_handle(as_bytes(obsVarId))
    observations_numarray = marshal.as_c_double_array(observations, shallow=True)
    obsGeom_xptr = wrap_as_pointer_handle(obsGeom)
    yamlStatIdString_c_charp = wrap_as_pointer_handle(as_bytes(yamlStatIdString))
    result = _CreateCompositeObservationObjectiveEvaluator_native(simulation_xptr.ptr, obsVarId_c_charp.ptr, observations_numarray.ptr, obsGeom_xptr.ptr, yamlStatIdString_c_charp.ptr)
    # no cleanup for const char*
    # observations_numarray - no cleanup needed?
    # no cleanup for const char*
    return custom_wrap_cffi_native_handle(result, 'OBJECTIVE_EVALUATOR_PTR')


@_s_wrap.check_exceptions
def _CreateMultisiteObjectiveEvaluator_native(simulation, defn, weights):
    result = swift_so.CreateMultisiteObjectiveEvaluator(simulation, defn, weights)
    return result

def CreateMultisiteObjectiveEvaluator_py(simulation:'Simulation', defn:Any, weights:Dict[str,float]) -> 'DeletableCffiNativeHandle':
    """CreateMultisiteObjectiveEvaluator_py
    
    CreateMultisiteObjectiveEvaluator_py: generated wrapper function for API function CreateMultisiteObjectiveEvaluator
    
    Args:
        simulation ('Simulation'): simulation
        defn (Any): defn
        weights (Dict[str,float]): weights
    
    Returns:
        ('DeletableCffiNativeHandle'): returned result
    
    """
    simulation_xptr = wrap_as_pointer_handle(simulation)
    defn_mstatdef = to_multi_statistic_definition(defn)
    weights_nvv = marshal.dict_to_named_values(weights)
    result = _CreateMultisiteObjectiveEvaluator_native(simulation_xptr.ptr, defn_mstatdef.ptr, weights_nvv.ptr)
    # defn_mstatdef - no cleanup needed?
    # weights_nvv - no cleanup needed?
    return custom_wrap_cffi_native_handle(result, 'OBJECTIVE_EVALUATOR_PTR')


@_s_wrap.check_exceptions
def _CloneObjectiveEvaluator_native(objectiveEvaluator, simulation):
    result = swift_so.CloneObjectiveEvaluator(objectiveEvaluator, simulation)
    return result

def CloneObjectiveEvaluator_py(objectiveEvaluator:'DeletableCffiNativeHandle', simulation:'Simulation') -> 'DeletableCffiNativeHandle':
    """CloneObjectiveEvaluator_py
    
    CloneObjectiveEvaluator_py: generated wrapper function for API function CloneObjectiveEvaluator
    
    Args:
        objectiveEvaluator ('DeletableCffiNativeHandle'): objectiveEvaluator
        simulation ('Simulation'): simulation
    
    Returns:
        ('DeletableCffiNativeHandle'): returned result
    
    """
    objectiveEvaluator_xptr = wrap_as_pointer_handle(objectiveEvaluator)
    simulation_xptr = wrap_as_pointer_handle(simulation)
    result = _CloneObjectiveEvaluator_native(objectiveEvaluator_xptr.ptr, simulation_xptr.ptr)
    return custom_wrap_cffi_native_handle(result, 'OBJECTIVE_EVALUATOR_PTR')


@_s_wrap.check_exceptions
def _EvaluateScore_native(objectiveEvaluator):
    result = swift_so.EvaluateScore(objectiveEvaluator)
    return result

def EvaluateScore_py(objectiveEvaluator:'DeletableCffiNativeHandle') -> float:
    """EvaluateScore_py
    
    EvaluateScore_py: generated wrapper function for API function EvaluateScore
    
    Args:
        objectiveEvaluator ('DeletableCffiNativeHandle'): objectiveEvaluator
    
    Returns:
        (float): returned result
    
    """
    objectiveEvaluator_xptr = wrap_as_pointer_handle(objectiveEvaluator)
    result = _EvaluateScore_native(objectiveEvaluator_xptr.ptr)
    return result


@_s_wrap.check_exceptions
def _EvaluateScoreForParameters_native(objectiveEvaluator, parameterizer):
    result = swift_so.EvaluateScoreForParameters(objectiveEvaluator, parameterizer)
    return result

def EvaluateScoreForParameters_py(objectiveEvaluator:'DeletableCffiNativeHandle', parameterizer:Any) -> float:
    """EvaluateScoreForParameters_py
    
    EvaluateScoreForParameters_py: generated wrapper function for API function EvaluateScoreForParameters
    
    Args:
        objectiveEvaluator ('DeletableCffiNativeHandle'): objectiveEvaluator
        parameterizer (Any): parameterizer
    
    Returns:
        (float): returned result
    
    """
    objectiveEvaluator_xptr = wrap_as_pointer_handle(objectiveEvaluator)
    parameterizer_xptr = wrap_as_pointer_handle(parameterizer)
    result = _EvaluateScoreForParameters_native(objectiveEvaluator_xptr.ptr, parameterizer_xptr.ptr)
    return result


@_s_wrap.check_exceptions
def _EvaluateScoreForParametersInitState_native(objectiveEvaluator, parameterizer):
    result = swift_so.EvaluateScoreForParametersInitState(objectiveEvaluator, parameterizer)
    return result

def EvaluateScoreForParametersInitState_py(objectiveEvaluator:'DeletableCffiNativeHandle', parameterizer:Any) -> float:
    """EvaluateScoreForParametersInitState_py
    
    EvaluateScoreForParametersInitState_py: generated wrapper function for API function EvaluateScoreForParametersInitState
    
    Args:
        objectiveEvaluator ('DeletableCffiNativeHandle'): objectiveEvaluator
        parameterizer (Any): parameterizer
    
    Returns:
        (float): returned result
    
    """
    objectiveEvaluator_xptr = wrap_as_pointer_handle(objectiveEvaluator)
    parameterizer_xptr = wrap_as_pointer_handle(parameterizer)
    result = _EvaluateScoreForParametersInitState_native(objectiveEvaluator_xptr.ptr, parameterizer_xptr.ptr)
    return result


@_s_wrap.check_exceptions
def _EvaluateScoresForParametersWila_native(objectiveEvaluator, parameterizer):
    result = swift_so.EvaluateScoresForParametersWila(objectiveEvaluator, parameterizer)
    return result

def EvaluateScoresForParametersWila_py(objectiveEvaluator:'ObjectiveEvaluator', parameterizer:'HypercubeParameteriser') -> Dict[str,float]:
    """EvaluateScoresForParametersWila_py
    
    EvaluateScoresForParametersWila_py: generated wrapper function for API function EvaluateScoresForParametersWila
    
    Args:
        objectiveEvaluator ('ObjectiveEvaluator'): objectiveEvaluator
        parameterizer ('HypercubeParameteriser'): parameterizer
    
    Returns:
        (Dict[str,float]): returned result
    
    """
    objectiveEvaluator_xptr = wrap_as_pointer_handle(objectiveEvaluator)
    parameterizer_xptr = wrap_as_pointer_handle(parameterizer)
    result = _EvaluateScoresForParametersWila_native(objectiveEvaluator_xptr.ptr, parameterizer_xptr.ptr)
    return named_values_to_py(result, dispose=True)


@_s_wrap.check_exceptions
def _GetNameObjectiveEvaluator_native(objectiveEvaluator):
    result = swift_so.GetNameObjectiveEvaluator(objectiveEvaluator)
    return result

def GetNameObjectiveEvaluator_py(objectiveEvaluator:'DeletableCffiNativeHandle') -> str:
    """GetNameObjectiveEvaluator_py
    
    GetNameObjectiveEvaluator_py: generated wrapper function for API function GetNameObjectiveEvaluator
    
    Args:
        objectiveEvaluator ('DeletableCffiNativeHandle'): objectiveEvaluator
    
    Returns:
        (str): returned result
    
    """
    objectiveEvaluator_xptr = wrap_as_pointer_handle(objectiveEvaluator)
    result = _GetNameObjectiveEvaluator_native(objectiveEvaluator_xptr.ptr)
    return char_array_to_py(result, dispose=True)


@_s_wrap.check_exceptions
def _ObjectiveEvaluatorIsMaximizable_native(objectiveEvaluator):
    result = swift_so.ObjectiveEvaluatorIsMaximizable(objectiveEvaluator)
    return result

def ObjectiveEvaluatorIsMaximizable_py(objectiveEvaluator:'DeletableCffiNativeHandle') -> bool:
    """ObjectiveEvaluatorIsMaximizable_py
    
    ObjectiveEvaluatorIsMaximizable_py: generated wrapper function for API function ObjectiveEvaluatorIsMaximizable
    
    Args:
        objectiveEvaluator ('DeletableCffiNativeHandle'): objectiveEvaluator
    
    Returns:
        (bool): returned result
    
    """
    objectiveEvaluator_xptr = wrap_as_pointer_handle(objectiveEvaluator)
    result = _ObjectiveEvaluatorIsMaximizable_native(objectiveEvaluator_xptr.ptr)
    return result


@_s_wrap.check_exceptions
def _CreateSingleObservationObjectiveEvaluatorWila_native(simulation, obsVarId, observations, obsGeom, statisticId):
    result = swift_so.CreateSingleObservationObjectiveEvaluatorWila(simulation, obsVarId, observations, obsGeom, statisticId)
    return result

def CreateSingleObservationObjectiveEvaluatorWila_py(simulation:'Simulation', obsVarId:str, observations:np.ndarray, obsGeom:TimeSeriesGeometryNative, statisticId:str) -> 'ObjectiveEvaluator':
    """CreateSingleObservationObjectiveEvaluatorWila_py
    
    CreateSingleObservationObjectiveEvaluatorWila_py: generated wrapper function for API function CreateSingleObservationObjectiveEvaluatorWila
    
    Args:
        simulation ('Simulation'): simulation
        obsVarId (str): obsVarId
        observations (np.ndarray): observations
        obsGeom (TimeSeriesGeometryNative): obsGeom
        statisticId (str): statisticId
    
    Returns:
        ('ObjectiveEvaluator'): returned result
    
    """
    simulation_xptr = wrap_as_pointer_handle(simulation)
    obsVarId_c_charp = wrap_as_pointer_handle(as_bytes(obsVarId))
    observations_numarray = marshal.as_c_double_array(observations, shallow=True)
    obsGeom_xptr = wrap_as_pointer_handle(obsGeom)
    statisticId_c_charp = wrap_as_pointer_handle(as_bytes(statisticId))
    result = _CreateSingleObservationObjectiveEvaluatorWila_native(simulation_xptr.ptr, obsVarId_c_charp.ptr, observations_numarray.ptr, obsGeom_xptr.ptr, statisticId_c_charp.ptr)
    # no cleanup for const char*
    # observations_numarray - no cleanup needed?
    # no cleanup for const char*
    return custom_wrap_cffi_native_handle(result, 'OBJECTIVE_EVALUATOR_WILA_PTR')


@_s_wrap.check_exceptions
def _CreateShuffledComplexEvolutionWila_native(objective, terminationCriterion, SCEpars, populationInitializer):
    result = swift_so.CreateShuffledComplexEvolutionWila(objective, terminationCriterion, SCEpars, populationInitializer)
    return result

def CreateShuffledComplexEvolutionWila_py(objective:'ObjectiveEvaluator', terminationCriterion:'SceTerminationCondition', SCEpars:Dict[str,float], populationInitializer:'CandidateFactorySeed') -> 'Optimiser':
    """CreateShuffledComplexEvolutionWila_py
    
    CreateShuffledComplexEvolutionWila_py: generated wrapper function for API function CreateShuffledComplexEvolutionWila
    
    Args:
        objective ('ObjectiveEvaluator'): objective
        terminationCriterion ('SceTerminationCondition'): terminationCriterion
        SCEpars (Dict[str,float]): SCEpars
        populationInitializer ('CandidateFactorySeed'): populationInitializer
    
    Returns:
        ('Optimiser'): returned result
    
    """
    objective_xptr = wrap_as_pointer_handle(objective)
    terminationCriterion_xptr = wrap_as_pointer_handle(terminationCriterion)
    SCEpars_sceparams = toSceParametersNative(SCEpars)
    populationInitializer_xptr = wrap_as_pointer_handle(populationInitializer)
    result = _CreateShuffledComplexEvolutionWila_native(objective_xptr.ptr, terminationCriterion_xptr.ptr, SCEpars_sceparams.obj, populationInitializer_xptr.ptr)
    # SCEpars_sceparams - no cleanup needed
    return custom_wrap_cffi_native_handle(result, 'OPTIMIZER_PTR')


@_s_wrap.check_exceptions
def _CreateOptimizerWila_native(objective, parameterizer, parameters):
    result = swift_so.CreateOptimizerWila(objective, parameterizer, parameters)
    return result

def CreateOptimizerWila_py(objective:'ObjectiveEvaluator', parameterizer:'HypercubeParameteriser', parameters:Dict[str,str]) -> 'Optimiser':
    """CreateOptimizerWila_py
    
    CreateOptimizerWila_py: generated wrapper function for API function CreateOptimizerWila
    
    Args:
        objective ('ObjectiveEvaluator'): objective
        parameterizer ('HypercubeParameteriser'): parameterizer
        parameters (Dict[str,str]): parameters
    
    Returns:
        ('Optimiser'): returned result
    
    """
    objective_xptr = wrap_as_pointer_handle(objective)
    parameterizer_xptr = wrap_as_pointer_handle(parameterizer)
    parameters_dict = marshal.dict_to_string_map(parameters)
    result = _CreateOptimizerWila_native(objective_xptr.ptr, parameterizer_xptr.ptr, parameters_dict.ptr)
    # parameters_dict - no cleanup needed?
    return custom_wrap_cffi_native_handle(result, 'OPTIMIZER_PTR')


@_s_wrap.check_exceptions
def _CreateSceMarginalTerminationWila_native(tolerance, cutoffNoImprovement, maxHours):
    result = swift_so.CreateSceMarginalTerminationWila(tolerance, cutoffNoImprovement, maxHours)
    return result

def CreateSceMarginalTerminationWila_py(tolerance:float, cutoffNoImprovement:int, maxHours:float) -> 'SceTerminationCondition':
    """CreateSceMarginalTerminationWila_py
    
    CreateSceMarginalTerminationWila_py: generated wrapper function for API function CreateSceMarginalTerminationWila
    
    Args:
        tolerance (float): tolerance
        cutoffNoImprovement (int): cutoffNoImprovement
        maxHours (float): maxHours
    
    Returns:
        ('SceTerminationCondition'): returned result
    
    """
    result = _CreateSceMarginalTerminationWila_native(tolerance, cutoffNoImprovement, maxHours)
    return custom_wrap_cffi_native_handle(result, 'SCE_TERMINATION_CONDITION_WILA_PTR')


@_s_wrap.check_exceptions
def _CreateSceMaxRuntimeTerminationWila_native(maxHours):
    result = swift_so.CreateSceMaxRuntimeTerminationWila(maxHours)
    return result

def CreateSceMaxRuntimeTerminationWila_py(maxHours:float) -> 'SceTerminationCondition':
    """CreateSceMaxRuntimeTerminationWila_py
    
    CreateSceMaxRuntimeTerminationWila_py: generated wrapper function for API function CreateSceMaxRuntimeTerminationWila
    
    Args:
        maxHours (float): maxHours
    
    Returns:
        ('SceTerminationCondition'): returned result
    
    """
    result = _CreateSceMaxRuntimeTerminationWila_native(maxHours)
    return custom_wrap_cffi_native_handle(result, 'SCE_TERMINATION_CONDITION_WILA_PTR')


@_s_wrap.check_exceptions
def _CreateSceMaxIterationTerminationWila_native(maxIterations):
    result = swift_so.CreateSceMaxIterationTerminationWila(maxIterations)
    return result

def CreateSceMaxIterationTerminationWila_py(maxIterations:int) -> 'SceTerminationCondition':
    """CreateSceMaxIterationTerminationWila_py
    
    CreateSceMaxIterationTerminationWila_py: generated wrapper function for API function CreateSceMaxIterationTerminationWila
    
    Args:
        maxIterations (int): maxIterations
    
    Returns:
        ('SceTerminationCondition'): returned result
    
    """
    result = _CreateSceMaxIterationTerminationWila_native(maxIterations)
    return custom_wrap_cffi_native_handle(result, 'SCE_TERMINATION_CONDITION_WILA_PTR')


@_s_wrap.check_exceptions
def _CreateSceTerminationWila_native(type, arguments, numArguments):
    result = swift_so.CreateSceTerminationWila(type, arguments, numArguments)
    return result

def CreateSceTerminationWila_py(type:str, arguments:List[str], numArguments:int) -> 'SceTerminationCondition':
    """CreateSceTerminationWila_py
    
    CreateSceTerminationWila_py: generated wrapper function for API function CreateSceTerminationWila
    
    Args:
        type (str): type
        arguments (List[str]): arguments
        numArguments (int): numArguments
    
    Returns:
        ('SceTerminationCondition'): returned result
    
    """
    type_c_charp = wrap_as_pointer_handle(as_bytes(type))
    arguments_charpp = wrap_as_pointer_handle(marshal.as_arrayof_bytes(arguments))
    result = _CreateSceTerminationWila_native(type_c_charp.ptr, arguments_charpp.ptr, numArguments)
    # no cleanup for const char*
    # clean arguments_charpp ?
    return custom_wrap_cffi_native_handle(result, 'SCE_TERMINATION_CONDITION_WILA_PTR')


@_s_wrap.check_exceptions
def _CreateCandidateFactorySeedWila_native(hypercubeParameterizer, type, seed):
    result = swift_so.CreateCandidateFactorySeedWila(hypercubeParameterizer, type, seed)
    return result

def CreateCandidateFactorySeedWila_py(hypercubeParameterizer:'HypercubeParameteriser', type:str, seed:int) -> 'CandidateFactorySeed':
    """CreateCandidateFactorySeedWila_py
    
    CreateCandidateFactorySeedWila_py: generated wrapper function for API function CreateCandidateFactorySeedWila
    
    Args:
        hypercubeParameterizer ('HypercubeParameteriser'): hypercubeParameterizer
        type (str): type
        seed (int): seed
    
    Returns:
        ('CandidateFactorySeed'): returned result
    
    """
    hypercubeParameterizer_xptr = wrap_as_pointer_handle(hypercubeParameterizer)
    type_c_charp = wrap_as_pointer_handle(as_bytes(type))
    result = _CreateCandidateFactorySeedWila_native(hypercubeParameterizer_xptr.ptr, type_c_charp.ptr, seed)
    # no cleanup for const char*
    return custom_wrap_cffi_native_handle(result, 'CANDIDATE_FACTORY_SEED_WILA_PTR')


@_s_wrap.check_exceptions
def _EvaluateScoreForParametersWila_native(objectiveEvaluator, hypercubeParameterizer):
    result = swift_so.EvaluateScoreForParametersWila(objectiveEvaluator, hypercubeParameterizer)
    return result

def EvaluateScoreForParametersWila_py(objectiveEvaluator:'ObjectiveEvaluator', hypercubeParameterizer:'HypercubeParameteriser') -> 'ObjectiveScores':
    """EvaluateScoreForParametersWila_py
    
    EvaluateScoreForParametersWila_py: generated wrapper function for API function EvaluateScoreForParametersWila
    
    Args:
        objectiveEvaluator ('ObjectiveEvaluator'): objectiveEvaluator
        hypercubeParameterizer ('HypercubeParameteriser'): hypercubeParameterizer
    
    Returns:
        ('ObjectiveScores'): returned result
    
    """
    objectiveEvaluator_xptr = wrap_as_pointer_handle(objectiveEvaluator)
    hypercubeParameterizer_xptr = wrap_as_pointer_handle(hypercubeParameterizer)
    result = _EvaluateScoreForParametersWila_native(objectiveEvaluator_xptr.ptr, hypercubeParameterizer_xptr.ptr)
    return custom_wrap_cffi_native_handle(result, 'OBJECTIVE_SCORES_WILA_PTR')


@_s_wrap.check_exceptions
def _EvaluateScoreForParametersWilaInitState_native(objectiveEvaluator, hypercubeParameterizer):
    result = swift_so.EvaluateScoreForParametersWilaInitState(objectiveEvaluator, hypercubeParameterizer)
    return result

def EvaluateScoreForParametersWilaInitState_py(objectiveEvaluator:'ObjectiveEvaluator', hypercubeParameterizer:'HypercubeParameteriser') -> 'ObjectiveScores':
    """EvaluateScoreForParametersWilaInitState_py
    
    EvaluateScoreForParametersWilaInitState_py: generated wrapper function for API function EvaluateScoreForParametersWilaInitState
    
    Args:
        objectiveEvaluator ('ObjectiveEvaluator'): objectiveEvaluator
        hypercubeParameterizer ('HypercubeParameteriser'): hypercubeParameterizer
    
    Returns:
        ('ObjectiveScores'): returned result
    
    """
    objectiveEvaluator_xptr = wrap_as_pointer_handle(objectiveEvaluator)
    hypercubeParameterizer_xptr = wrap_as_pointer_handle(hypercubeParameterizer)
    result = _EvaluateScoreForParametersWilaInitState_native(objectiveEvaluator_xptr.ptr, hypercubeParameterizer_xptr.ptr)
    return custom_wrap_cffi_native_handle(result, 'OBJECTIVE_SCORES_WILA_PTR')


@_s_wrap.check_exceptions
def _GetScoresAtIndex_native(vectorScores, index):
    result = swift_so.GetScoresAtIndex(vectorScores, index)
    return result

def GetScoresAtIndex_py(vectorScores:'VectorObjectiveScores', index:int) -> 'ObjectiveScores':
    """GetScoresAtIndex_py
    
    GetScoresAtIndex_py: generated wrapper function for API function GetScoresAtIndex
    
    Args:
        vectorScores ('VectorObjectiveScores'): vectorScores
        index (int): index
    
    Returns:
        ('ObjectiveScores'): returned result
    
    """
    vectorScores_xptr = wrap_as_pointer_handle(vectorScores)
    result = _GetScoresAtIndex_native(vectorScores_xptr.ptr, index)
    return custom_wrap_cffi_native_handle(result, 'OBJECTIVE_SCORES_WILA_PTR')


@_s_wrap.check_exceptions
def _SortSetOfScoresBy_native(vectorScores, scoreName):
    result = swift_so.SortSetOfScoresBy(vectorScores, scoreName)
    return result

def SortSetOfScoresBy_py(vectorScores:'VectorObjectiveScores', scoreName:str) -> 'VectorObjectiveScores':
    """SortSetOfScoresBy_py
    
    SortSetOfScoresBy_py: generated wrapper function for API function SortSetOfScoresBy
    
    Args:
        vectorScores ('VectorObjectiveScores'): vectorScores
        scoreName (str): scoreName
    
    Returns:
        ('VectorObjectiveScores'): returned result
    
    """
    vectorScores_xptr = wrap_as_pointer_handle(vectorScores)
    scoreName_c_charp = wrap_as_pointer_handle(as_bytes(scoreName))
    result = _SortSetOfScoresBy_native(vectorScores_xptr.ptr, scoreName_c_charp.ptr)
    # no cleanup for const char*
    return custom_wrap_cffi_native_handle(result, 'VEC_OBJECTIVE_SCORES_PTR')


@_s_wrap.check_exceptions
def _EstimateERRISParameters_native(simulation, obsValues, obsGeom, errorModelElementId, warmupStart, warmupEnd, warmup, estimationStart, estimationEnd, censThr, censOpt, exclusionStart, exclusionEnd, exclusion, terminationCondition, errisParams, hydroParams, restrictionOn, weightedLeastSquare):
    result = swift_so.EstimateERRISParameters(simulation, obsValues, obsGeom, errorModelElementId, warmupStart, warmupEnd, warmup, estimationStart, estimationEnd, censThr, censOpt, exclusionStart, exclusionEnd, exclusion, terminationCondition, errisParams, hydroParams, restrictionOn, weightedLeastSquare)
    return result

def EstimateERRISParameters_py(simulation:'Simulation', obsValues:np.ndarray, obsGeom:TimeSeriesGeometryNative, errorModelElementId:str, warmupStart:datetime, warmupEnd:datetime, warmup:bool, estimationStart:datetime, estimationEnd:datetime, censThr:float, censOpt:float, exclusionStart:datetime, exclusionEnd:datetime, exclusion:bool, terminationCondition:'SceTerminationCondition', errisParams:'HypercubeParameteriser', hydroParams:'HypercubeParameteriser', restrictionOn:bool, weightedLeastSquare:bool) -> 'HypercubeParameteriser':
    """EstimateERRISParameters_py
    
    EstimateERRISParameters_py: generated wrapper function for API function EstimateERRISParameters
    
    Args:
        simulation ('Simulation'): simulation
        obsValues (np.ndarray): obsValues
        obsGeom (TimeSeriesGeometryNative): obsGeom
        errorModelElementId (str): errorModelElementId
        warmupStart (datetime): warmupStart
        warmupEnd (datetime): warmupEnd
        warmup (bool): warmup
        estimationStart (datetime): estimationStart
        estimationEnd (datetime): estimationEnd
        censThr (float): censThr
        censOpt (float): censOpt
        exclusionStart (datetime): exclusionStart
        exclusionEnd (datetime): exclusionEnd
        exclusion (bool): exclusion
        terminationCondition ('SceTerminationCondition'): terminationCondition
        errisParams ('HypercubeParameteriser'): errisParams
        hydroParams ('HypercubeParameteriser'): hydroParams
        restrictionOn (bool): restrictionOn
        weightedLeastSquare (bool): weightedLeastSquare
    
    Returns:
        ('HypercubeParameteriser'): returned result
    
    """
    simulation_xptr = wrap_as_pointer_handle(simulation)
    obsValues_numarray = marshal.as_c_double_array(obsValues, shallow=True)
    obsGeom_xptr = wrap_as_pointer_handle(obsGeom)
    errorModelElementId_c_charp = wrap_as_pointer_handle(as_bytes(errorModelElementId))
    warmupStart_datetime = marshal.datetime_to_dtts(warmupStart)
    warmupEnd_datetime = marshal.datetime_to_dtts(warmupEnd)
    estimationStart_datetime = marshal.datetime_to_dtts(estimationStart)
    estimationEnd_datetime = marshal.datetime_to_dtts(estimationEnd)
    exclusionStart_datetime = marshal.datetime_to_dtts(exclusionStart)
    exclusionEnd_datetime = marshal.datetime_to_dtts(exclusionEnd)
    terminationCondition_xptr = wrap_as_pointer_handle(terminationCondition)
    errisParams_xptr = wrap_as_pointer_handle(errisParams)
    hydroParams_xptr = wrap_as_pointer_handle(hydroParams)
    result = _EstimateERRISParameters_native(simulation_xptr.ptr, obsValues_numarray.ptr, obsGeom_xptr.ptr, errorModelElementId_c_charp.ptr, warmupStart_datetime.obj, warmupEnd_datetime.obj, warmup, estimationStart_datetime.obj, estimationEnd_datetime.obj, censThr, censOpt, exclusionStart_datetime.obj, exclusionEnd_datetime.obj, exclusion, terminationCondition_xptr.ptr, errisParams_xptr.ptr, hydroParams_xptr.ptr, restrictionOn, weightedLeastSquare)
    # obsValues_numarray - no cleanup needed?
    # no cleanup for const char*
    # warmupStart_datetime - no cleanup needed?
    # warmupEnd_datetime - no cleanup needed?
    # estimationStart_datetime - no cleanup needed?
    # estimationEnd_datetime - no cleanup needed?
    # exclusionStart_datetime - no cleanup needed?
    # exclusionEnd_datetime - no cleanup needed?
    return custom_wrap_cffi_native_handle(result, 'HYPERCUBE_PTR')


@_s_wrap.check_exceptions
def _CreateERRISParameterEstimator_native(mr, obsValues, obsGeom, errorModelElementId, estimationStart, estimationEnd, censThr, censOpt, terminationCondition, restrictionOn, weightedLeastSquare):
    result = swift_so.CreateERRISParameterEstimator(mr, obsValues, obsGeom, errorModelElementId, estimationStart, estimationEnd, censThr, censOpt, terminationCondition, restrictionOn, weightedLeastSquare)
    return result

def CreateERRISParameterEstimator_py(mr:'Simulation', obsValues:np.ndarray, obsGeom:TimeSeriesGeometryNative, errorModelElementId:str, estimationStart:datetime, estimationEnd:datetime, censThr:float, censOpt:float, terminationCondition:'SceTerminationCondition', restrictionOn:bool, weightedLeastSquare:bool) -> 'ErrisStagedCalibration':
    """CreateERRISParameterEstimator_py
    
    CreateERRISParameterEstimator_py: generated wrapper function for API function CreateERRISParameterEstimator
    
    Args:
        mr ('Simulation'): mr
        obsValues (np.ndarray): obsValues
        obsGeom (TimeSeriesGeometryNative): obsGeom
        errorModelElementId (str): errorModelElementId
        estimationStart (datetime): estimationStart
        estimationEnd (datetime): estimationEnd
        censThr (float): censThr
        censOpt (float): censOpt
        terminationCondition ('SceTerminationCondition'): terminationCondition
        restrictionOn (bool): restrictionOn
        weightedLeastSquare (bool): weightedLeastSquare
    
    Returns:
        ('ErrisStagedCalibration'): returned result
    
    """
    mr_xptr = wrap_as_pointer_handle(mr)
    obsValues_numarray = marshal.as_c_double_array(obsValues, shallow=True)
    obsGeom_xptr = wrap_as_pointer_handle(obsGeom)
    errorModelElementId_c_charp = wrap_as_pointer_handle(as_bytes(errorModelElementId))
    estimationStart_datetime = marshal.datetime_to_dtts(estimationStart)
    estimationEnd_datetime = marshal.datetime_to_dtts(estimationEnd)
    terminationCondition_xptr = wrap_as_pointer_handle(terminationCondition)
    result = _CreateERRISParameterEstimator_native(mr_xptr.ptr, obsValues_numarray.ptr, obsGeom_xptr.ptr, errorModelElementId_c_charp.ptr, estimationStart_datetime.obj, estimationEnd_datetime.obj, censThr, censOpt, terminationCondition_xptr.ptr, restrictionOn, weightedLeastSquare)
    # obsValues_numarray - no cleanup needed?
    # no cleanup for const char*
    # estimationStart_datetime - no cleanup needed?
    # estimationEnd_datetime - no cleanup needed?
    return custom_wrap_cffi_native_handle(result, 'ERRIS_STAGED_CALIBRATION_PTR')


@_s_wrap.check_exceptions
def _SetERRISHydrologicParameterSpace_native(calibObject, hydroParams):
    swift_so.SetERRISHydrologicParameterSpace(calibObject, hydroParams)

def SetERRISHydrologicParameterSpace_py(calibObject:'ErrisStagedCalibration', hydroParams:'HypercubeParameteriser') -> None:
    """SetERRISHydrologicParameterSpace_py
    
    SetERRISHydrologicParameterSpace_py: generated wrapper function for API function SetERRISHydrologicParameterSpace
    
    Args:
        calibObject ('ErrisStagedCalibration'): calibObject
        hydroParams ('HypercubeParameteriser'): hydroParams
    
    """
    calibObject_xptr = wrap_as_pointer_handle(calibObject)
    hydroParams_xptr = wrap_as_pointer_handle(hydroParams)
    _SetERRISHydrologicParameterSpace_native(calibObject_xptr.ptr, hydroParams_xptr.ptr)


@_s_wrap.check_exceptions
def _SetERRISErrorCorrectionParameterSpace_native(calibObject, errisParams):
    swift_so.SetERRISErrorCorrectionParameterSpace(calibObject, errisParams)

def SetERRISErrorCorrectionParameterSpace_py(calibObject:'ErrisStagedCalibration', errisParams:'HypercubeParameteriser') -> None:
    """SetERRISErrorCorrectionParameterSpace_py
    
    SetERRISErrorCorrectionParameterSpace_py: generated wrapper function for API function SetERRISErrorCorrectionParameterSpace
    
    Args:
        calibObject ('ErrisStagedCalibration'): calibObject
        errisParams ('HypercubeParameteriser'): errisParams
    
    """
    calibObject_xptr = wrap_as_pointer_handle(calibObject)
    errisParams_xptr = wrap_as_pointer_handle(errisParams)
    _SetERRISErrorCorrectionParameterSpace_native(calibObject_xptr.ptr, errisParams_xptr.ptr)


@_s_wrap.check_exceptions
def _SetERRISEstimationPeriod_native(calibObject, estimationStart, estimationEnd):
    swift_so.SetERRISEstimationPeriod(calibObject, estimationStart, estimationEnd)

def SetERRISEstimationPeriod_py(calibObject:'ErrisStagedCalibration', estimationStart:datetime, estimationEnd:datetime) -> None:
    """SetERRISEstimationPeriod_py
    
    SetERRISEstimationPeriod_py: generated wrapper function for API function SetERRISEstimationPeriod
    
    Args:
        calibObject ('ErrisStagedCalibration'): calibObject
        estimationStart (datetime): estimationStart
        estimationEnd (datetime): estimationEnd
    
    """
    calibObject_xptr = wrap_as_pointer_handle(calibObject)
    estimationStart_datetime = marshal.datetime_to_dtts(estimationStart)
    estimationEnd_datetime = marshal.datetime_to_dtts(estimationEnd)
    _SetERRISEstimationPeriod_native(calibObject_xptr.ptr, estimationStart_datetime.obj, estimationEnd_datetime.obj)
    # estimationStart_datetime - no cleanup needed?
    # estimationEnd_datetime - no cleanup needed?


@_s_wrap.check_exceptions
def _SetERRISWarmupPeriod_native(calibObject, warmupStart, warmupEnd):
    swift_so.SetERRISWarmupPeriod(calibObject, warmupStart, warmupEnd)

def SetERRISWarmupPeriod_py(calibObject:'ErrisStagedCalibration', warmupStart:datetime, warmupEnd:datetime) -> None:
    """SetERRISWarmupPeriod_py
    
    SetERRISWarmupPeriod_py: generated wrapper function for API function SetERRISWarmupPeriod
    
    Args:
        calibObject ('ErrisStagedCalibration'): calibObject
        warmupStart (datetime): warmupStart
        warmupEnd (datetime): warmupEnd
    
    """
    calibObject_xptr = wrap_as_pointer_handle(calibObject)
    warmupStart_datetime = marshal.datetime_to_dtts(warmupStart)
    warmupEnd_datetime = marshal.datetime_to_dtts(warmupEnd)
    _SetERRISWarmupPeriod_native(calibObject_xptr.ptr, warmupStart_datetime.obj, warmupEnd_datetime.obj)
    # warmupStart_datetime - no cleanup needed?
    # warmupEnd_datetime - no cleanup needed?


@_s_wrap.check_exceptions
def _SetERRISExclusionPeriod_native(calibObject, exclusionStart, exclusionEnd):
    swift_so.SetERRISExclusionPeriod(calibObject, exclusionStart, exclusionEnd)

def SetERRISExclusionPeriod_py(calibObject:'ErrisStagedCalibration', exclusionStart:datetime, exclusionEnd:datetime) -> None:
    """SetERRISExclusionPeriod_py
    
    SetERRISExclusionPeriod_py: generated wrapper function for API function SetERRISExclusionPeriod
    
    Args:
        calibObject ('ErrisStagedCalibration'): calibObject
        exclusionStart (datetime): exclusionStart
        exclusionEnd (datetime): exclusionEnd
    
    """
    calibObject_xptr = wrap_as_pointer_handle(calibObject)
    exclusionStart_datetime = marshal.datetime_to_dtts(exclusionStart)
    exclusionEnd_datetime = marshal.datetime_to_dtts(exclusionEnd)
    _SetERRISExclusionPeriod_native(calibObject_xptr.ptr, exclusionStart_datetime.obj, exclusionEnd_datetime.obj)
    # exclusionStart_datetime - no cleanup needed?
    # exclusionEnd_datetime - no cleanup needed?


@_s_wrap.check_exceptions
def _RemoveERRISWarmupPeriod_native(calibObject):
    swift_so.RemoveERRISWarmupPeriod(calibObject)

def RemoveERRISWarmupPeriod_py(calibObject:'ErrisStagedCalibration') -> None:
    """RemoveERRISWarmupPeriod_py
    
    RemoveERRISWarmupPeriod_py: generated wrapper function for API function RemoveERRISWarmupPeriod
    
    Args:
        calibObject ('ErrisStagedCalibration'): calibObject
    
    """
    calibObject_xptr = wrap_as_pointer_handle(calibObject)
    _RemoveERRISWarmupPeriod_native(calibObject_xptr.ptr)


@_s_wrap.check_exceptions
def _RemoveERRISExclusionPeriod_native(calibObject):
    swift_so.RemoveERRISExclusionPeriod(calibObject)

def RemoveERRISExclusionPeriod_py(calibObject:'ErrisStagedCalibration') -> None:
    """RemoveERRISExclusionPeriod_py
    
    RemoveERRISExclusionPeriod_py: generated wrapper function for API function RemoveERRISExclusionPeriod
    
    Args:
        calibObject ('ErrisStagedCalibration'): calibObject
    
    """
    calibObject_xptr = wrap_as_pointer_handle(calibObject)
    _RemoveERRISExclusionPeriod_native(calibObject_xptr.ptr)


@_s_wrap.check_exceptions
def _SetERRISMaxObservation_native(calibObject, maxObs):
    swift_so.SetERRISMaxObservation(calibObject, maxObs)

def SetERRISMaxObservation_py(calibObject:'ErrisStagedCalibration', maxObs:float) -> None:
    """SetERRISMaxObservation_py
    
    SetERRISMaxObservation_py: generated wrapper function for API function SetERRISMaxObservation
    
    Args:
        calibObject ('ErrisStagedCalibration'): calibObject
        maxObs (float): maxObs
    
    """
    calibObject_xptr = wrap_as_pointer_handle(calibObject)
    _SetERRISMaxObservation_native(calibObject_xptr.ptr, maxObs)


@_s_wrap.check_exceptions
def _SetERRISCensOptions_native(calibObject, censOpt):
    swift_so.SetERRISCensOptions(calibObject, censOpt)

def SetERRISCensOptions_py(calibObject:'ErrisStagedCalibration', censOpt:float) -> None:
    """SetERRISCensOptions_py
    
    SetERRISCensOptions_py: generated wrapper function for API function SetERRISCensOptions
    
    Args:
        calibObject ('ErrisStagedCalibration'): calibObject
        censOpt (float): censOpt
    
    """
    calibObject_xptr = wrap_as_pointer_handle(calibObject)
    _SetERRISCensOptions_native(calibObject_xptr.ptr, censOpt)


@_s_wrap.check_exceptions
def _SetERRISVerboseCalibration_native(calibObject, verboseCalibrationLog):
    swift_so.SetERRISVerboseCalibration(calibObject, verboseCalibrationLog)

def SetERRISVerboseCalibration_py(calibObject:'ErrisStagedCalibration', verboseCalibrationLog:bool) -> None:
    """SetERRISVerboseCalibration_py
    
    SetERRISVerboseCalibration_py: generated wrapper function for API function SetERRISVerboseCalibration
    
    Args:
        calibObject ('ErrisStagedCalibration'): calibObject
        verboseCalibrationLog (bool): verboseCalibrationLog
    
    """
    calibObject_xptr = wrap_as_pointer_handle(calibObject)
    _SetERRISVerboseCalibration_native(calibObject_xptr.ptr, verboseCalibrationLog)


@_s_wrap.check_exceptions
def _CalibrateERRISStageOne_native(calibObject):
    result = swift_so.CalibrateERRISStageOne(calibObject)
    return result

def CalibrateERRISStageOne_py(calibObject:'ErrisStagedCalibration') -> 'HypercubeParameteriser':
    """CalibrateERRISStageOne_py
    
    CalibrateERRISStageOne_py: generated wrapper function for API function CalibrateERRISStageOne
    
    Args:
        calibObject ('ErrisStagedCalibration'): calibObject
    
    Returns:
        ('HypercubeParameteriser'): returned result
    
    """
    calibObject_xptr = wrap_as_pointer_handle(calibObject)
    result = _CalibrateERRISStageOne_native(calibObject_xptr.ptr)
    return custom_wrap_cffi_native_handle(result, 'HYPERCUBE_PTR')


@_s_wrap.check_exceptions
def _CalibrateERRISStageTwo_native(calibObject, previousStage):
    result = swift_so.CalibrateERRISStageTwo(calibObject, previousStage)
    return result

def CalibrateERRISStageTwo_py(calibObject:'ErrisStagedCalibration', previousStage:'HypercubeParameteriser') -> 'HypercubeParameteriser':
    """CalibrateERRISStageTwo_py
    
    CalibrateERRISStageTwo_py: generated wrapper function for API function CalibrateERRISStageTwo
    
    Args:
        calibObject ('ErrisStagedCalibration'): calibObject
        previousStage ('HypercubeParameteriser'): previousStage
    
    Returns:
        ('HypercubeParameteriser'): returned result
    
    """
    calibObject_xptr = wrap_as_pointer_handle(calibObject)
    previousStage_xptr = wrap_as_pointer_handle(previousStage)
    result = _CalibrateERRISStageTwo_native(calibObject_xptr.ptr, previousStage_xptr.ptr)
    return custom_wrap_cffi_native_handle(result, 'HYPERCUBE_PTR')


@_s_wrap.check_exceptions
def _CalibrateERRISStageThree_native(calibObject, previousStage):
    result = swift_so.CalibrateERRISStageThree(calibObject, previousStage)
    return result

def CalibrateERRISStageThree_py(calibObject:'ErrisStagedCalibration', previousStage:'HypercubeParameteriser') -> 'HypercubeParameteriser':
    """CalibrateERRISStageThree_py
    
    CalibrateERRISStageThree_py: generated wrapper function for API function CalibrateERRISStageThree
    
    Args:
        calibObject ('ErrisStagedCalibration'): calibObject
        previousStage ('HypercubeParameteriser'): previousStage
    
    Returns:
        ('HypercubeParameteriser'): returned result
    
    """
    calibObject_xptr = wrap_as_pointer_handle(calibObject)
    previousStage_xptr = wrap_as_pointer_handle(previousStage)
    result = _CalibrateERRISStageThree_native(calibObject_xptr.ptr, previousStage_xptr.ptr)
    return custom_wrap_cffi_native_handle(result, 'HYPERCUBE_PTR')


@_s_wrap.check_exceptions
def _CalibrateERRISStageFour_native(calibObject, previousStage, useRising):
    result = swift_so.CalibrateERRISStageFour(calibObject, previousStage, useRising)
    return result

def CalibrateERRISStageFour_py(calibObject:'ErrisStagedCalibration', previousStage:'HypercubeParameteriser', useRising:bool) -> 'HypercubeParameteriser':
    """CalibrateERRISStageFour_py
    
    CalibrateERRISStageFour_py: generated wrapper function for API function CalibrateERRISStageFour
    
    Args:
        calibObject ('ErrisStagedCalibration'): calibObject
        previousStage ('HypercubeParameteriser'): previousStage
        useRising (bool): useRising
    
    Returns:
        ('HypercubeParameteriser'): returned result
    
    """
    calibObject_xptr = wrap_as_pointer_handle(calibObject)
    previousStage_xptr = wrap_as_pointer_handle(previousStage)
    result = _CalibrateERRISStageFour_native(calibObject_xptr.ptr, previousStage_xptr.ptr, useRising)
    return custom_wrap_cffi_native_handle(result, 'HYPERCUBE_PTR')


@_s_wrap.check_exceptions
def _CalibrateERRISStageThreeMS_native(calibObject, previousStage):
    result = swift_so.CalibrateERRISStageThreeMS(calibObject, previousStage)
    return result

def CalibrateERRISStageThreeMS_py(calibObject:'ErrisStagedCalibration', previousStage:'HypercubeParameteriser') -> 'HypercubeParameteriser':
    """CalibrateERRISStageThreeMS_py
    
    CalibrateERRISStageThreeMS_py: generated wrapper function for API function CalibrateERRISStageThreeMS
    
    Args:
        calibObject ('ErrisStagedCalibration'): calibObject
        previousStage ('HypercubeParameteriser'): previousStage
    
    Returns:
        ('HypercubeParameteriser'): returned result
    
    """
    calibObject_xptr = wrap_as_pointer_handle(calibObject)
    previousStage_xptr = wrap_as_pointer_handle(previousStage)
    result = _CalibrateERRISStageThreeMS_native(calibObject_xptr.ptr, previousStage_xptr.ptr)
    return custom_wrap_cffi_native_handle(result, 'HYPERCUBE_PTR')


@_s_wrap.check_exceptions
def _ConcatenateERRISStagesParameters_native(calibObject, hydroParams, stage1_result, stage2_result, stage3_result, stage4a_result, stage4b_result, toLongParameterName):
    result = swift_so.ConcatenateERRISStagesParameters(calibObject, hydroParams, stage1_result, stage2_result, stage3_result, stage4a_result, stage4b_result, toLongParameterName)
    return result

def ConcatenateERRISStagesParameters_py(calibObject:'ErrisStagedCalibration', hydroParams:'HypercubeParameteriser', stage1_result:'HypercubeParameteriser', stage2_result:'HypercubeParameteriser', stage3_result:'HypercubeParameteriser', stage4a_result:'HypercubeParameteriser', stage4b_result:'HypercubeParameteriser', toLongParameterName:bool) -> 'HypercubeParameteriser':
    """ConcatenateERRISStagesParameters_py
    
    ConcatenateERRISStagesParameters_py: generated wrapper function for API function ConcatenateERRISStagesParameters
    
    Args:
        calibObject ('ErrisStagedCalibration'): calibObject
        hydroParams ('HypercubeParameteriser'): hydroParams
        stage1_result ('HypercubeParameteriser'): stage1_result
        stage2_result ('HypercubeParameteriser'): stage2_result
        stage3_result ('HypercubeParameteriser'): stage3_result
        stage4a_result ('HypercubeParameteriser'): stage4a_result
        stage4b_result ('HypercubeParameteriser'): stage4b_result
        toLongParameterName (bool): toLongParameterName
    
    Returns:
        ('HypercubeParameteriser'): returned result
    
    """
    calibObject_xptr = wrap_as_pointer_handle(calibObject)
    hydroParams_xptr = wrap_as_pointer_handle(hydroParams)
    stage1_result_xptr = wrap_as_pointer_handle(stage1_result)
    stage2_result_xptr = wrap_as_pointer_handle(stage2_result)
    stage3_result_xptr = wrap_as_pointer_handle(stage3_result)
    stage4a_result_xptr = wrap_as_pointer_handle(stage4a_result)
    stage4b_result_xptr = wrap_as_pointer_handle(stage4b_result)
    result = _ConcatenateERRISStagesParameters_native(calibObject_xptr.ptr, hydroParams_xptr.ptr, stage1_result_xptr.ptr, stage2_result_xptr.ptr, stage3_result_xptr.ptr, stage4a_result_xptr.ptr, stage4b_result_xptr.ptr, toLongParameterName)
    return custom_wrap_cffi_native_handle(result, 'HYPERCUBE_PTR')


@_s_wrap.check_exceptions
def _GetERRISCalibrationLog_native(calibObject):
    result = swift_so.GetERRISCalibrationLog(calibObject)
    return result

def GetERRISCalibrationLog_py(calibObject:'ErrisStagedCalibration') -> DeletableCffiNativeHandle:
    """GetERRISCalibrationLog_py
    
    GetERRISCalibrationLog_py: generated wrapper function for API function GetERRISCalibrationLog
    
    Args:
        calibObject ('ErrisStagedCalibration'): calibObject
    
    Returns:
        (DeletableCffiNativeHandle): returned result
    
    """
    calibObject_xptr = wrap_as_pointer_handle(calibObject)
    result = _GetERRISCalibrationLog_native(calibObject_xptr.ptr)
    return custom_wrap_cffi_native_handle(result, 'OptimizerLogData*', DisposeOptimizerLogDataWila_py)


@_s_wrap.check_exceptions
def _PrepareERRISForecasting_native(mr, obsValues, obsGeom, errorModelElementId, warmupStart, warmupEnd):
    result = swift_so.PrepareERRISForecasting(mr, obsValues, obsGeom, errorModelElementId, warmupStart, warmupEnd)
    return result

def PrepareERRISForecasting_py(mr:'Simulation', obsValues:np.ndarray, obsGeom:TimeSeriesGeometryNative, errorModelElementId:str, warmupStart:datetime, warmupEnd:datetime) -> 'EnsembleSimulation':
    """PrepareERRISForecasting_py
    
    PrepareERRISForecasting_py: generated wrapper function for API function PrepareERRISForecasting
    
    Args:
        mr ('Simulation'): mr
        obsValues (np.ndarray): obsValues
        obsGeom (TimeSeriesGeometryNative): obsGeom
        errorModelElementId (str): errorModelElementId
        warmupStart (datetime): warmupStart
        warmupEnd (datetime): warmupEnd
    
    Returns:
        ('EnsembleSimulation'): returned result
    
    """
    mr_xptr = wrap_as_pointer_handle(mr)
    obsValues_numarray = marshal.as_c_double_array(obsValues, shallow=True)
    obsGeom_xptr = wrap_as_pointer_handle(obsGeom)
    errorModelElementId_c_charp = wrap_as_pointer_handle(as_bytes(errorModelElementId))
    warmupStart_datetime = marshal.datetime_to_dtts(warmupStart)
    warmupEnd_datetime = marshal.datetime_to_dtts(warmupEnd)
    result = _PrepareERRISForecasting_native(mr_xptr.ptr, obsValues_numarray.ptr, obsGeom_xptr.ptr, errorModelElementId_c_charp.ptr, warmupStart_datetime.obj, warmupEnd_datetime.obj)
    # obsValues_numarray - no cleanup needed?
    # no cleanup for const char*
    # warmupStart_datetime - no cleanup needed?
    # warmupEnd_datetime - no cleanup needed?
    return custom_wrap_cffi_native_handle(result, 'ENSEMBLE_SIMULATION_PTR')


@_s_wrap.check_exceptions
def _EstimateMAERRISParameters_native(simulation, obsValues, obsGeom, errorModelElementId, warmupStart, warmupEnd, warmup, estimationStart, estimationEnd, s2Window, censThr, censOpt, exclusionStart, exclusionEnd, exclusion, terminationCondition, maerrisParams, hydroParams, restrictionOn):
    result = swift_so.EstimateMAERRISParameters(simulation, obsValues, obsGeom, errorModelElementId, warmupStart, warmupEnd, warmup, estimationStart, estimationEnd, s2Window, censThr, censOpt, exclusionStart, exclusionEnd, exclusion, terminationCondition, maerrisParams, hydroParams, restrictionOn)
    return result

def EstimateMAERRISParameters_py(simulation:'Simulation', obsValues:np.ndarray, obsGeom:TimeSeriesGeometryNative, errorModelElementId:str, warmupStart:datetime, warmupEnd:datetime, warmup:bool, estimationStart:datetime, estimationEnd:datetime, s2Window:float, censThr:float, censOpt:float, exclusionStart:datetime, exclusionEnd:datetime, exclusion:bool, terminationCondition:'SceTerminationCondition', maerrisParams:'HypercubeParameteriser', hydroParams:'HypercubeParameteriser', restrictionOn:bool) -> 'HypercubeParameteriser':
    """EstimateMAERRISParameters_py
    
    EstimateMAERRISParameters_py: generated wrapper function for API function EstimateMAERRISParameters
    
    Args:
        simulation ('Simulation'): simulation
        obsValues (np.ndarray): obsValues
        obsGeom (TimeSeriesGeometryNative): obsGeom
        errorModelElementId (str): errorModelElementId
        warmupStart (datetime): warmupStart
        warmupEnd (datetime): warmupEnd
        warmup (bool): warmup
        estimationStart (datetime): estimationStart
        estimationEnd (datetime): estimationEnd
        s2Window (float): s2Window
        censThr (float): censThr
        censOpt (float): censOpt
        exclusionStart (datetime): exclusionStart
        exclusionEnd (datetime): exclusionEnd
        exclusion (bool): exclusion
        terminationCondition ('SceTerminationCondition'): terminationCondition
        maerrisParams ('HypercubeParameteriser'): maerrisParams
        hydroParams ('HypercubeParameteriser'): hydroParams
        restrictionOn (bool): restrictionOn
    
    Returns:
        ('HypercubeParameteriser'): returned result
    
    """
    simulation_xptr = wrap_as_pointer_handle(simulation)
    obsValues_numarray = marshal.as_c_double_array(obsValues, shallow=True)
    obsGeom_xptr = wrap_as_pointer_handle(obsGeom)
    errorModelElementId_c_charp = wrap_as_pointer_handle(as_bytes(errorModelElementId))
    warmupStart_datetime = marshal.datetime_to_dtts(warmupStart)
    warmupEnd_datetime = marshal.datetime_to_dtts(warmupEnd)
    estimationStart_datetime = marshal.datetime_to_dtts(estimationStart)
    estimationEnd_datetime = marshal.datetime_to_dtts(estimationEnd)
    exclusionStart_datetime = marshal.datetime_to_dtts(exclusionStart)
    exclusionEnd_datetime = marshal.datetime_to_dtts(exclusionEnd)
    terminationCondition_xptr = wrap_as_pointer_handle(terminationCondition)
    maerrisParams_xptr = wrap_as_pointer_handle(maerrisParams)
    hydroParams_xptr = wrap_as_pointer_handle(hydroParams)
    result = _EstimateMAERRISParameters_native(simulation_xptr.ptr, obsValues_numarray.ptr, obsGeom_xptr.ptr, errorModelElementId_c_charp.ptr, warmupStart_datetime.obj, warmupEnd_datetime.obj, warmup, estimationStart_datetime.obj, estimationEnd_datetime.obj, s2Window, censThr, censOpt, exclusionStart_datetime.obj, exclusionEnd_datetime.obj, exclusion, terminationCondition_xptr.ptr, maerrisParams_xptr.ptr, hydroParams_xptr.ptr, restrictionOn)
    # obsValues_numarray - no cleanup needed?
    # no cleanup for const char*
    # warmupStart_datetime - no cleanup needed?
    # warmupEnd_datetime - no cleanup needed?
    # estimationStart_datetime - no cleanup needed?
    # estimationEnd_datetime - no cleanup needed?
    # exclusionStart_datetime - no cleanup needed?
    # exclusionEnd_datetime - no cleanup needed?
    return custom_wrap_cffi_native_handle(result, 'HYPERCUBE_PTR')


@_s_wrap.check_exceptions
def _CreateMAERRISParameterEstimator_native(mr, obsValues, obsGeom, errorModelElementId, estimationStart, estimationEnd, s2Window, censThr, censOpt, terminationCondition, restrictionOn):
    result = swift_so.CreateMAERRISParameterEstimator(mr, obsValues, obsGeom, errorModelElementId, estimationStart, estimationEnd, s2Window, censThr, censOpt, terminationCondition, restrictionOn)
    return result

def CreateMAERRISParameterEstimator_py(mr:'Simulation', obsValues:np.ndarray, obsGeom:TimeSeriesGeometryNative, errorModelElementId:str, estimationStart:datetime, estimationEnd:datetime, s2Window:float, censThr:float, censOpt:float, terminationCondition:'SceTerminationCondition', restrictionOn:bool) -> 'MaerrisStagedCalibration':
    """CreateMAERRISParameterEstimator_py
    
    CreateMAERRISParameterEstimator_py: generated wrapper function for API function CreateMAERRISParameterEstimator
    
    Args:
        mr ('Simulation'): mr
        obsValues (np.ndarray): obsValues
        obsGeom (TimeSeriesGeometryNative): obsGeom
        errorModelElementId (str): errorModelElementId
        estimationStart (datetime): estimationStart
        estimationEnd (datetime): estimationEnd
        s2Window (float): s2Window
        censThr (float): censThr
        censOpt (float): censOpt
        terminationCondition ('SceTerminationCondition'): terminationCondition
        restrictionOn (bool): restrictionOn
    
    Returns:
        ('MaerrisStagedCalibration'): returned result
    
    """
    mr_xptr = wrap_as_pointer_handle(mr)
    obsValues_numarray = marshal.as_c_double_array(obsValues, shallow=True)
    obsGeom_xptr = wrap_as_pointer_handle(obsGeom)
    errorModelElementId_c_charp = wrap_as_pointer_handle(as_bytes(errorModelElementId))
    estimationStart_datetime = marshal.datetime_to_dtts(estimationStart)
    estimationEnd_datetime = marshal.datetime_to_dtts(estimationEnd)
    terminationCondition_xptr = wrap_as_pointer_handle(terminationCondition)
    result = _CreateMAERRISParameterEstimator_native(mr_xptr.ptr, obsValues_numarray.ptr, obsGeom_xptr.ptr, errorModelElementId_c_charp.ptr, estimationStart_datetime.obj, estimationEnd_datetime.obj, s2Window, censThr, censOpt, terminationCondition_xptr.ptr, restrictionOn)
    # obsValues_numarray - no cleanup needed?
    # no cleanup for const char*
    # estimationStart_datetime - no cleanup needed?
    # estimationEnd_datetime - no cleanup needed?
    return custom_wrap_cffi_native_handle(result, 'MAERRIS_STAGED_CALIBRATION_PTR')


@_s_wrap.check_exceptions
def _SetMAERRISHydrologicParameterSpace_native(calibObject, hydroParams):
    swift_so.SetMAERRISHydrologicParameterSpace(calibObject, hydroParams)

def SetMAERRISHydrologicParameterSpace_py(calibObject:'MaerrisStagedCalibration', hydroParams:'HypercubeParameteriser') -> None:
    """SetMAERRISHydrologicParameterSpace_py
    
    SetMAERRISHydrologicParameterSpace_py: generated wrapper function for API function SetMAERRISHydrologicParameterSpace
    
    Args:
        calibObject ('MaerrisStagedCalibration'): calibObject
        hydroParams ('HypercubeParameteriser'): hydroParams
    
    """
    calibObject_xptr = wrap_as_pointer_handle(calibObject)
    hydroParams_xptr = wrap_as_pointer_handle(hydroParams)
    _SetMAERRISHydrologicParameterSpace_native(calibObject_xptr.ptr, hydroParams_xptr.ptr)


@_s_wrap.check_exceptions
def _SetMAERRISErrorCorrectionParameterSpace_native(calibObject, maerrisParams):
    swift_so.SetMAERRISErrorCorrectionParameterSpace(calibObject, maerrisParams)

def SetMAERRISErrorCorrectionParameterSpace_py(calibObject:'MaerrisStagedCalibration', maerrisParams:'HypercubeParameteriser') -> None:
    """SetMAERRISErrorCorrectionParameterSpace_py
    
    SetMAERRISErrorCorrectionParameterSpace_py: generated wrapper function for API function SetMAERRISErrorCorrectionParameterSpace
    
    Args:
        calibObject ('MaerrisStagedCalibration'): calibObject
        maerrisParams ('HypercubeParameteriser'): maerrisParams
    
    """
    calibObject_xptr = wrap_as_pointer_handle(calibObject)
    maerrisParams_xptr = wrap_as_pointer_handle(maerrisParams)
    _SetMAERRISErrorCorrectionParameterSpace_native(calibObject_xptr.ptr, maerrisParams_xptr.ptr)


@_s_wrap.check_exceptions
def _SetMAERRISEstimationPeriod_native(calibObject, estimationStart, estimationEnd):
    swift_so.SetMAERRISEstimationPeriod(calibObject, estimationStart, estimationEnd)

def SetMAERRISEstimationPeriod_py(calibObject:'MaerrisStagedCalibration', estimationStart:datetime, estimationEnd:datetime) -> None:
    """SetMAERRISEstimationPeriod_py
    
    SetMAERRISEstimationPeriod_py: generated wrapper function for API function SetMAERRISEstimationPeriod
    
    Args:
        calibObject ('MaerrisStagedCalibration'): calibObject
        estimationStart (datetime): estimationStart
        estimationEnd (datetime): estimationEnd
    
    """
    calibObject_xptr = wrap_as_pointer_handle(calibObject)
    estimationStart_datetime = marshal.datetime_to_dtts(estimationStart)
    estimationEnd_datetime = marshal.datetime_to_dtts(estimationEnd)
    _SetMAERRISEstimationPeriod_native(calibObject_xptr.ptr, estimationStart_datetime.obj, estimationEnd_datetime.obj)
    # estimationStart_datetime - no cleanup needed?
    # estimationEnd_datetime - no cleanup needed?


@_s_wrap.check_exceptions
def _SetMAERRISWarmupPeriod_native(calibObject, warmupStart, warmupEnd):
    swift_so.SetMAERRISWarmupPeriod(calibObject, warmupStart, warmupEnd)

def SetMAERRISWarmupPeriod_py(calibObject:'MaerrisStagedCalibration', warmupStart:datetime, warmupEnd:datetime) -> None:
    """SetMAERRISWarmupPeriod_py
    
    SetMAERRISWarmupPeriod_py: generated wrapper function for API function SetMAERRISWarmupPeriod
    
    Args:
        calibObject ('MaerrisStagedCalibration'): calibObject
        warmupStart (datetime): warmupStart
        warmupEnd (datetime): warmupEnd
    
    """
    calibObject_xptr = wrap_as_pointer_handle(calibObject)
    warmupStart_datetime = marshal.datetime_to_dtts(warmupStart)
    warmupEnd_datetime = marshal.datetime_to_dtts(warmupEnd)
    _SetMAERRISWarmupPeriod_native(calibObject_xptr.ptr, warmupStart_datetime.obj, warmupEnd_datetime.obj)
    # warmupStart_datetime - no cleanup needed?
    # warmupEnd_datetime - no cleanup needed?


@_s_wrap.check_exceptions
def _SetMAERRISExclusionPeriod_native(calibObject, exclusionStart, exclusionEnd):
    swift_so.SetMAERRISExclusionPeriod(calibObject, exclusionStart, exclusionEnd)

def SetMAERRISExclusionPeriod_py(calibObject:'MaerrisStagedCalibration', exclusionStart:datetime, exclusionEnd:datetime) -> None:
    """SetMAERRISExclusionPeriod_py
    
    SetMAERRISExclusionPeriod_py: generated wrapper function for API function SetMAERRISExclusionPeriod
    
    Args:
        calibObject ('MaerrisStagedCalibration'): calibObject
        exclusionStart (datetime): exclusionStart
        exclusionEnd (datetime): exclusionEnd
    
    """
    calibObject_xptr = wrap_as_pointer_handle(calibObject)
    exclusionStart_datetime = marshal.datetime_to_dtts(exclusionStart)
    exclusionEnd_datetime = marshal.datetime_to_dtts(exclusionEnd)
    _SetMAERRISExclusionPeriod_native(calibObject_xptr.ptr, exclusionStart_datetime.obj, exclusionEnd_datetime.obj)
    # exclusionStart_datetime - no cleanup needed?
    # exclusionEnd_datetime - no cleanup needed?


@_s_wrap.check_exceptions
def _RemoveMAERRISWarmupPeriod_native(calibObject):
    swift_so.RemoveMAERRISWarmupPeriod(calibObject)

def RemoveMAERRISWarmupPeriod_py(calibObject:'MaerrisStagedCalibration') -> None:
    """RemoveMAERRISWarmupPeriod_py
    
    RemoveMAERRISWarmupPeriod_py: generated wrapper function for API function RemoveMAERRISWarmupPeriod
    
    Args:
        calibObject ('MaerrisStagedCalibration'): calibObject
    
    """
    calibObject_xptr = wrap_as_pointer_handle(calibObject)
    _RemoveMAERRISWarmupPeriod_native(calibObject_xptr.ptr)


@_s_wrap.check_exceptions
def _RemoveMAERRISExclusionPeriod_native(calibObject):
    swift_so.RemoveMAERRISExclusionPeriod(calibObject)

def RemoveMAERRISExclusionPeriod_py(calibObject:'MaerrisStagedCalibration') -> None:
    """RemoveMAERRISExclusionPeriod_py
    
    RemoveMAERRISExclusionPeriod_py: generated wrapper function for API function RemoveMAERRISExclusionPeriod
    
    Args:
        calibObject ('MaerrisStagedCalibration'): calibObject
    
    """
    calibObject_xptr = wrap_as_pointer_handle(calibObject)
    _RemoveMAERRISExclusionPeriod_native(calibObject_xptr.ptr)


@_s_wrap.check_exceptions
def _SetMAERRISS2Window_native(calibObject, s2Window):
    swift_so.SetMAERRISS2Window(calibObject, s2Window)

def SetMAERRISS2Window_py(calibObject:'MaerrisStagedCalibration', s2Window:float) -> None:
    """SetMAERRISS2Window_py
    
    SetMAERRISS2Window_py: generated wrapper function for API function SetMAERRISS2Window
    
    Args:
        calibObject ('MaerrisStagedCalibration'): calibObject
        s2Window (float): s2Window
    
    """
    calibObject_xptr = wrap_as_pointer_handle(calibObject)
    _SetMAERRISS2Window_native(calibObject_xptr.ptr, s2Window)


@_s_wrap.check_exceptions
def _SetMAERRISMaxObservation_native(calibObject, maxObs):
    swift_so.SetMAERRISMaxObservation(calibObject, maxObs)

def SetMAERRISMaxObservation_py(calibObject:'MaerrisStagedCalibration', maxObs:float) -> None:
    """SetMAERRISMaxObservation_py
    
    SetMAERRISMaxObservation_py: generated wrapper function for API function SetMAERRISMaxObservation
    
    Args:
        calibObject ('MaerrisStagedCalibration'): calibObject
        maxObs (float): maxObs
    
    """
    calibObject_xptr = wrap_as_pointer_handle(calibObject)
    _SetMAERRISMaxObservation_native(calibObject_xptr.ptr, maxObs)


@_s_wrap.check_exceptions
def _SetMAERRISRestrictionOn_native(calibObject, restrictionOn):
    swift_so.SetMAERRISRestrictionOn(calibObject, restrictionOn)

def SetMAERRISRestrictionOn_py(calibObject:'MaerrisStagedCalibration', restrictionOn:bool) -> None:
    """SetMAERRISRestrictionOn_py
    
    SetMAERRISRestrictionOn_py: generated wrapper function for API function SetMAERRISRestrictionOn
    
    Args:
        calibObject ('MaerrisStagedCalibration'): calibObject
        restrictionOn (bool): restrictionOn
    
    """
    calibObject_xptr = wrap_as_pointer_handle(calibObject)
    _SetMAERRISRestrictionOn_native(calibObject_xptr.ptr, restrictionOn)


@_s_wrap.check_exceptions
def _SetMAERRISCensOptions_native(calibObject, censOpt):
    swift_so.SetMAERRISCensOptions(calibObject, censOpt)

def SetMAERRISCensOptions_py(calibObject:'MaerrisStagedCalibration', censOpt:float) -> None:
    """SetMAERRISCensOptions_py
    
    SetMAERRISCensOptions_py: generated wrapper function for API function SetMAERRISCensOptions
    
    Args:
        calibObject ('MaerrisStagedCalibration'): calibObject
        censOpt (float): censOpt
    
    """
    calibObject_xptr = wrap_as_pointer_handle(calibObject)
    _SetMAERRISCensOptions_native(calibObject_xptr.ptr, censOpt)


@_s_wrap.check_exceptions
def _SetMAERRISVerboseCalibration_native(calibObject, verboseCalibrationLog):
    swift_so.SetMAERRISVerboseCalibration(calibObject, verboseCalibrationLog)

def SetMAERRISVerboseCalibration_py(calibObject:'MaerrisStagedCalibration', verboseCalibrationLog:bool) -> None:
    """SetMAERRISVerboseCalibration_py
    
    SetMAERRISVerboseCalibration_py: generated wrapper function for API function SetMAERRISVerboseCalibration
    
    Args:
        calibObject ('MaerrisStagedCalibration'): calibObject
        verboseCalibrationLog (bool): verboseCalibrationLog
    
    """
    calibObject_xptr = wrap_as_pointer_handle(calibObject)
    _SetMAERRISVerboseCalibration_native(calibObject_xptr.ptr, verboseCalibrationLog)


@_s_wrap.check_exceptions
def _CalibrateMAERRISStageOne_native(calibObject):
    result = swift_so.CalibrateMAERRISStageOne(calibObject)
    return result

def CalibrateMAERRISStageOne_py(calibObject:'MaerrisStagedCalibration') -> 'HypercubeParameteriser':
    """CalibrateMAERRISStageOne_py
    
    CalibrateMAERRISStageOne_py: generated wrapper function for API function CalibrateMAERRISStageOne
    
    Args:
        calibObject ('MaerrisStagedCalibration'): calibObject
    
    Returns:
        ('HypercubeParameteriser'): returned result
    
    """
    calibObject_xptr = wrap_as_pointer_handle(calibObject)
    result = _CalibrateMAERRISStageOne_native(calibObject_xptr.ptr)
    return custom_wrap_cffi_native_handle(result, 'HYPERCUBE_PTR')


@_s_wrap.check_exceptions
def _CalibrateMAERRISStageTwo_native(calibObject, previousStage):
    result = swift_so.CalibrateMAERRISStageTwo(calibObject, previousStage)
    return result

def CalibrateMAERRISStageTwo_py(calibObject:'MaerrisStagedCalibration', previousStage:'HypercubeParameteriser') -> 'HypercubeParameteriser':
    """CalibrateMAERRISStageTwo_py
    
    CalibrateMAERRISStageTwo_py: generated wrapper function for API function CalibrateMAERRISStageTwo
    
    Args:
        calibObject ('MaerrisStagedCalibration'): calibObject
        previousStage ('HypercubeParameteriser'): previousStage
    
    Returns:
        ('HypercubeParameteriser'): returned result
    
    """
    calibObject_xptr = wrap_as_pointer_handle(calibObject)
    previousStage_xptr = wrap_as_pointer_handle(previousStage)
    result = _CalibrateMAERRISStageTwo_native(calibObject_xptr.ptr, previousStage_xptr.ptr)
    return custom_wrap_cffi_native_handle(result, 'HYPERCUBE_PTR')


@_s_wrap.check_exceptions
def _CalibrateMAERRISStageThree_native(calibObject, previousStage):
    result = swift_so.CalibrateMAERRISStageThree(calibObject, previousStage)
    return result

def CalibrateMAERRISStageThree_py(calibObject:'MaerrisStagedCalibration', previousStage:'HypercubeParameteriser') -> 'HypercubeParameteriser':
    """CalibrateMAERRISStageThree_py
    
    CalibrateMAERRISStageThree_py: generated wrapper function for API function CalibrateMAERRISStageThree
    
    Args:
        calibObject ('MaerrisStagedCalibration'): calibObject
        previousStage ('HypercubeParameteriser'): previousStage
    
    Returns:
        ('HypercubeParameteriser'): returned result
    
    """
    calibObject_xptr = wrap_as_pointer_handle(calibObject)
    previousStage_xptr = wrap_as_pointer_handle(previousStage)
    result = _CalibrateMAERRISStageThree_native(calibObject_xptr.ptr, previousStage_xptr.ptr)
    return custom_wrap_cffi_native_handle(result, 'HYPERCUBE_PTR')


@_s_wrap.check_exceptions
def _CalibrateMAERRISStageFour_native(calibObject, previousStage, useRising):
    result = swift_so.CalibrateMAERRISStageFour(calibObject, previousStage, useRising)
    return result

def CalibrateMAERRISStageFour_py(calibObject:'MaerrisStagedCalibration', previousStage:'HypercubeParameteriser', useRising:bool) -> 'HypercubeParameteriser':
    """CalibrateMAERRISStageFour_py
    
    CalibrateMAERRISStageFour_py: generated wrapper function for API function CalibrateMAERRISStageFour
    
    Args:
        calibObject ('MaerrisStagedCalibration'): calibObject
        previousStage ('HypercubeParameteriser'): previousStage
        useRising (bool): useRising
    
    Returns:
        ('HypercubeParameteriser'): returned result
    
    """
    calibObject_xptr = wrap_as_pointer_handle(calibObject)
    previousStage_xptr = wrap_as_pointer_handle(previousStage)
    result = _CalibrateMAERRISStageFour_native(calibObject_xptr.ptr, previousStage_xptr.ptr, useRising)
    return custom_wrap_cffi_native_handle(result, 'HYPERCUBE_PTR')


@_s_wrap.check_exceptions
def _CalibrateMAERRISStageThreeMS_native(calibObject, previousStage):
    result = swift_so.CalibrateMAERRISStageThreeMS(calibObject, previousStage)
    return result

def CalibrateMAERRISStageThreeMS_py(calibObject:'MaerrisStagedCalibration', previousStage:'HypercubeParameteriser') -> 'HypercubeParameteriser':
    """CalibrateMAERRISStageThreeMS_py
    
    CalibrateMAERRISStageThreeMS_py: generated wrapper function for API function CalibrateMAERRISStageThreeMS
    
    Args:
        calibObject ('MaerrisStagedCalibration'): calibObject
        previousStage ('HypercubeParameteriser'): previousStage
    
    Returns:
        ('HypercubeParameteriser'): returned result
    
    """
    calibObject_xptr = wrap_as_pointer_handle(calibObject)
    previousStage_xptr = wrap_as_pointer_handle(previousStage)
    result = _CalibrateMAERRISStageThreeMS_native(calibObject_xptr.ptr, previousStage_xptr.ptr)
    return custom_wrap_cffi_native_handle(result, 'HYPERCUBE_PTR')


@_s_wrap.check_exceptions
def _ConcatenateMAERRISStagesParameters_native(calibObject, hydroParams, stage1_result, stage2_result, stage3_result, stage4a_result, stage4b_result, toLongParameterName):
    result = swift_so.ConcatenateMAERRISStagesParameters(calibObject, hydroParams, stage1_result, stage2_result, stage3_result, stage4a_result, stage4b_result, toLongParameterName)
    return result

def ConcatenateMAERRISStagesParameters_py(calibObject:'MaerrisStagedCalibration', hydroParams:'HypercubeParameteriser', stage1_result:'HypercubeParameteriser', stage2_result:'HypercubeParameteriser', stage3_result:'HypercubeParameteriser', stage4a_result:'HypercubeParameteriser', stage4b_result:'HypercubeParameteriser', toLongParameterName:bool) -> 'HypercubeParameteriser':
    """ConcatenateMAERRISStagesParameters_py
    
    ConcatenateMAERRISStagesParameters_py: generated wrapper function for API function ConcatenateMAERRISStagesParameters
    
    Args:
        calibObject ('MaerrisStagedCalibration'): calibObject
        hydroParams ('HypercubeParameteriser'): hydroParams
        stage1_result ('HypercubeParameteriser'): stage1_result
        stage2_result ('HypercubeParameteriser'): stage2_result
        stage3_result ('HypercubeParameteriser'): stage3_result
        stage4a_result ('HypercubeParameteriser'): stage4a_result
        stage4b_result ('HypercubeParameteriser'): stage4b_result
        toLongParameterName (bool): toLongParameterName
    
    Returns:
        ('HypercubeParameteriser'): returned result
    
    """
    calibObject_xptr = wrap_as_pointer_handle(calibObject)
    hydroParams_xptr = wrap_as_pointer_handle(hydroParams)
    stage1_result_xptr = wrap_as_pointer_handle(stage1_result)
    stage2_result_xptr = wrap_as_pointer_handle(stage2_result)
    stage3_result_xptr = wrap_as_pointer_handle(stage3_result)
    stage4a_result_xptr = wrap_as_pointer_handle(stage4a_result)
    stage4b_result_xptr = wrap_as_pointer_handle(stage4b_result)
    result = _ConcatenateMAERRISStagesParameters_native(calibObject_xptr.ptr, hydroParams_xptr.ptr, stage1_result_xptr.ptr, stage2_result_xptr.ptr, stage3_result_xptr.ptr, stage4a_result_xptr.ptr, stage4b_result_xptr.ptr, toLongParameterName)
    return custom_wrap_cffi_native_handle(result, 'HYPERCUBE_PTR')


@_s_wrap.check_exceptions
def _GetMAERRISCalibrationLog_native(calibObject):
    result = swift_so.GetMAERRISCalibrationLog(calibObject)
    return result

def GetMAERRISCalibrationLog_py(calibObject:'MaerrisStagedCalibration') -> DeletableCffiNativeHandle:
    """GetMAERRISCalibrationLog_py
    
    GetMAERRISCalibrationLog_py: generated wrapper function for API function GetMAERRISCalibrationLog
    
    Args:
        calibObject ('MaerrisStagedCalibration'): calibObject
    
    Returns:
        (DeletableCffiNativeHandle): returned result
    
    """
    calibObject_xptr = wrap_as_pointer_handle(calibObject)
    result = _GetMAERRISCalibrationLog_native(calibObject_xptr.ptr)
    return custom_wrap_cffi_native_handle(result, 'OptimizerLogData*', DisposeOptimizerLogDataWila_py)


@_s_wrap.check_exceptions
def _EstimateDualPassParameters_native(simulation, obsValues, obsGeom, errorModelElementId, warmupStart, warmupEnd, warmup, estimationStart, estimationEnd, windowL, windowDecayL, windowDecayS, useLongPass, objFuncDescYaml, exclusionStart, exclusionEnd, exclusion, terminationCondition):
    result = swift_so.EstimateDualPassParameters(simulation, obsValues, obsGeom, errorModelElementId, warmupStart, warmupEnd, warmup, estimationStart, estimationEnd, windowL, windowDecayL, windowDecayS, useLongPass, objFuncDescYaml, exclusionStart, exclusionEnd, exclusion, terminationCondition)
    return result

def EstimateDualPassParameters_py(simulation:'Simulation', obsValues:np.ndarray, obsGeom:TimeSeriesGeometryNative, errorModelElementId:str, warmupStart:datetime, warmupEnd:datetime, warmup:bool, estimationStart:datetime, estimationEnd:datetime, windowL:int, windowDecayL:int, windowDecayS:int, useLongPass:bool, objFuncDescYaml:str, exclusionStart:datetime, exclusionEnd:datetime, exclusion:bool, terminationCondition:'SceTerminationCondition') -> 'HypercubeParameteriser':
    """EstimateDualPassParameters_py
    
    EstimateDualPassParameters_py: generated wrapper function for API function EstimateDualPassParameters
    
    Args:
        simulation ('Simulation'): simulation
        obsValues (np.ndarray): obsValues
        obsGeom (TimeSeriesGeometryNative): obsGeom
        errorModelElementId (str): errorModelElementId
        warmupStart (datetime): warmupStart
        warmupEnd (datetime): warmupEnd
        warmup (bool): warmup
        estimationStart (datetime): estimationStart
        estimationEnd (datetime): estimationEnd
        windowL (int): windowL
        windowDecayL (int): windowDecayL
        windowDecayS (int): windowDecayS
        useLongPass (bool): useLongPass
        objFuncDescYaml (str): objFuncDescYaml
        exclusionStart (datetime): exclusionStart
        exclusionEnd (datetime): exclusionEnd
        exclusion (bool): exclusion
        terminationCondition ('SceTerminationCondition'): terminationCondition
    
    Returns:
        ('HypercubeParameteriser'): returned result
    
    """
    simulation_xptr = wrap_as_pointer_handle(simulation)
    obsValues_numarray = marshal.as_c_double_array(obsValues, shallow=True)
    obsGeom_xptr = wrap_as_pointer_handle(obsGeom)
    errorModelElementId_c_charp = wrap_as_pointer_handle(as_bytes(errorModelElementId))
    warmupStart_datetime = marshal.datetime_to_dtts(warmupStart)
    warmupEnd_datetime = marshal.datetime_to_dtts(warmupEnd)
    estimationStart_datetime = marshal.datetime_to_dtts(estimationStart)
    estimationEnd_datetime = marshal.datetime_to_dtts(estimationEnd)
    objFuncDescYaml_charp = wrap_as_pointer_handle(as_bytes(objFuncDescYaml))
    exclusionStart_datetime = marshal.datetime_to_dtts(exclusionStart)
    exclusionEnd_datetime = marshal.datetime_to_dtts(exclusionEnd)
    terminationCondition_xptr = wrap_as_pointer_handle(terminationCondition)
    result = _EstimateDualPassParameters_native(simulation_xptr.ptr, obsValues_numarray.ptr, obsGeom_xptr.ptr, errorModelElementId_c_charp.ptr, warmupStart_datetime.obj, warmupEnd_datetime.obj, warmup, estimationStart_datetime.obj, estimationEnd_datetime.obj, windowL, windowDecayL, windowDecayS, useLongPass, objFuncDescYaml_charp.ptr, exclusionStart_datetime.obj, exclusionEnd_datetime.obj, exclusion, terminationCondition_xptr.ptr)
    # obsValues_numarray - no cleanup needed?
    # no cleanup for const char*
    # warmupStart_datetime - no cleanup needed?
    # warmupEnd_datetime - no cleanup needed?
    # estimationStart_datetime - no cleanup needed?
    # estimationEnd_datetime - no cleanup needed?
    # no cleanup for char*?
    # exclusionStart_datetime - no cleanup needed?
    # exclusionEnd_datetime - no cleanup needed?
    return custom_wrap_cffi_native_handle(result, 'HYPERCUBE_PTR')


@_s_wrap.check_exceptions
def _PrepareDualPassForecasting_native(mr, obsValues, obsGeom, errorModelElementId, warmupStart, warmupEnd, requiredWindowPercentage):
    result = swift_so.PrepareDualPassForecasting(mr, obsValues, obsGeom, errorModelElementId, warmupStart, warmupEnd, requiredWindowPercentage)
    return result

def PrepareDualPassForecasting_py(mr:'Simulation', obsValues:np.ndarray, obsGeom:TimeSeriesGeometryNative, errorModelElementId:str, warmupStart:datetime, warmupEnd:datetime, requiredWindowPercentage:float) -> 'EnsembleSimulation':
    """PrepareDualPassForecasting_py
    
    PrepareDualPassForecasting_py: generated wrapper function for API function PrepareDualPassForecasting
    
    Args:
        mr ('Simulation'): mr
        obsValues (np.ndarray): obsValues
        obsGeom (TimeSeriesGeometryNative): obsGeom
        errorModelElementId (str): errorModelElementId
        warmupStart (datetime): warmupStart
        warmupEnd (datetime): warmupEnd
        requiredWindowPercentage (float): requiredWindowPercentage
    
    Returns:
        ('EnsembleSimulation'): returned result
    
    """
    mr_xptr = wrap_as_pointer_handle(mr)
    obsValues_numarray = marshal.as_c_double_array(obsValues, shallow=True)
    obsGeom_xptr = wrap_as_pointer_handle(obsGeom)
    errorModelElementId_c_charp = wrap_as_pointer_handle(as_bytes(errorModelElementId))
    warmupStart_datetime = marshal.datetime_to_dtts(warmupStart)
    warmupEnd_datetime = marshal.datetime_to_dtts(warmupEnd)
    result = _PrepareDualPassForecasting_native(mr_xptr.ptr, obsValues_numarray.ptr, obsGeom_xptr.ptr, errorModelElementId_c_charp.ptr, warmupStart_datetime.obj, warmupEnd_datetime.obj, requiredWindowPercentage)
    # obsValues_numarray - no cleanup needed?
    # no cleanup for const char*
    # warmupStart_datetime - no cleanup needed?
    # warmupEnd_datetime - no cleanup needed?
    return custom_wrap_cffi_native_handle(result, 'ENSEMBLE_SIMULATION_PTR')


@_s_wrap.check_exceptions
def _EstimateTransformationParameters_native(obsValues, obsGeom, estimationStart, estimationEnd, censThr, censOpt, exclusionStart, exclusionEnd, exclusion, terminationCondition):
    result = swift_so.EstimateTransformationParameters(obsValues, obsGeom, estimationStart, estimationEnd, censThr, censOpt, exclusionStart, exclusionEnd, exclusion, terminationCondition)
    return result

def EstimateTransformationParameters_py(obsValues:np.ndarray, obsGeom:TimeSeriesGeometryNative, estimationStart:datetime, estimationEnd:datetime, censThr:float, censOpt:float, exclusionStart:datetime, exclusionEnd:datetime, exclusion:bool, terminationCondition:'SceTerminationCondition') -> 'HypercubeParameteriser':
    """EstimateTransformationParameters_py
    
    EstimateTransformationParameters_py: generated wrapper function for API function EstimateTransformationParameters
    
    Args:
        obsValues (np.ndarray): obsValues
        obsGeom (TimeSeriesGeometryNative): obsGeom
        estimationStart (datetime): estimationStart
        estimationEnd (datetime): estimationEnd
        censThr (float): censThr
        censOpt (float): censOpt
        exclusionStart (datetime): exclusionStart
        exclusionEnd (datetime): exclusionEnd
        exclusion (bool): exclusion
        terminationCondition ('SceTerminationCondition'): terminationCondition
    
    Returns:
        ('HypercubeParameteriser'): returned result
    
    """
    obsValues_numarray = marshal.as_c_double_array(obsValues, shallow=True)
    obsGeom_xptr = wrap_as_pointer_handle(obsGeom)
    estimationStart_datetime = marshal.datetime_to_dtts(estimationStart)
    estimationEnd_datetime = marshal.datetime_to_dtts(estimationEnd)
    exclusionStart_datetime = marshal.datetime_to_dtts(exclusionStart)
    exclusionEnd_datetime = marshal.datetime_to_dtts(exclusionEnd)
    terminationCondition_xptr = wrap_as_pointer_handle(terminationCondition)
    result = _EstimateTransformationParameters_native(obsValues_numarray.ptr, obsGeom_xptr.ptr, estimationStart_datetime.obj, estimationEnd_datetime.obj, censThr, censOpt, exclusionStart_datetime.obj, exclusionEnd_datetime.obj, exclusion, terminationCondition_xptr.ptr)
    # obsValues_numarray - no cleanup needed?
    # estimationStart_datetime - no cleanup needed?
    # estimationEnd_datetime - no cleanup needed?
    # exclusionStart_datetime - no cleanup needed?
    # exclusionEnd_datetime - no cleanup needed?
    return custom_wrap_cffi_native_handle(result, 'HYPERCUBE_PTR')


@_s_wrap.check_exceptions
def _EstimateTransformationParametersMS_native(obsValues, obsGeom, estimationStart, estimationEnd, exclusionStart, exclusionEnd, exclusion, terminationCondition, Params):
    result = swift_so.EstimateTransformationParametersMS(obsValues, obsGeom, estimationStart, estimationEnd, exclusionStart, exclusionEnd, exclusion, terminationCondition, Params)
    return result

def EstimateTransformationParametersMS_py(obsValues:np.ndarray, obsGeom:TimeSeriesGeometryNative, estimationStart:datetime, estimationEnd:datetime, exclusionStart:datetime, exclusionEnd:datetime, exclusion:bool, terminationCondition:'SceTerminationCondition', Params:'HypercubeParameteriser') -> 'HypercubeParameteriser':
    """EstimateTransformationParametersMS_py
    
    EstimateTransformationParametersMS_py: generated wrapper function for API function EstimateTransformationParametersMS
    
    Args:
        obsValues (np.ndarray): obsValues
        obsGeom (TimeSeriesGeometryNative): obsGeom
        estimationStart (datetime): estimationStart
        estimationEnd (datetime): estimationEnd
        exclusionStart (datetime): exclusionStart
        exclusionEnd (datetime): exclusionEnd
        exclusion (bool): exclusion
        terminationCondition ('SceTerminationCondition'): terminationCondition
        Params ('HypercubeParameteriser'): Params
    
    Returns:
        ('HypercubeParameteriser'): returned result
    
    """
    obsValues_numarray = marshal.as_c_double_array(obsValues, shallow=True)
    obsGeom_xptr = wrap_as_pointer_handle(obsGeom)
    estimationStart_datetime = marshal.datetime_to_dtts(estimationStart)
    estimationEnd_datetime = marshal.datetime_to_dtts(estimationEnd)
    exclusionStart_datetime = marshal.datetime_to_dtts(exclusionStart)
    exclusionEnd_datetime = marshal.datetime_to_dtts(exclusionEnd)
    terminationCondition_xptr = wrap_as_pointer_handle(terminationCondition)
    Params_xptr = wrap_as_pointer_handle(Params)
    result = _EstimateTransformationParametersMS_native(obsValues_numarray.ptr, obsGeom_xptr.ptr, estimationStart_datetime.obj, estimationEnd_datetime.obj, exclusionStart_datetime.obj, exclusionEnd_datetime.obj, exclusion, terminationCondition_xptr.ptr, Params_xptr.ptr)
    # obsValues_numarray - no cleanup needed?
    # estimationStart_datetime - no cleanup needed?
    # estimationEnd_datetime - no cleanup needed?
    # exclusionStart_datetime - no cleanup needed?
    # exclusionEnd_datetime - no cleanup needed?
    return custom_wrap_cffi_native_handle(result, 'HYPERCUBE_PTR')


@_s_wrap.check_exceptions
def _GetSystemConfigurationWila_native(scores):
    result = swift_so.GetSystemConfigurationWila(scores)
    return result

def GetSystemConfigurationWila_py(scores:'ObjectiveScores') -> 'HypercubeParameteriser':
    """GetSystemConfigurationWila_py
    
    GetSystemConfigurationWila_py: generated wrapper function for API function GetSystemConfigurationWila
    
    Args:
        scores ('ObjectiveScores'): scores
    
    Returns:
        ('HypercubeParameteriser'): returned result
    
    """
    scores_xptr = wrap_as_pointer_handle(scores)
    result = _GetSystemConfigurationWila_native(scores_xptr.ptr)
    return custom_wrap_cffi_native_handle(result, 'HYPERCUBE_PTR')


@_s_wrap.check_exceptions
def _GetNumScoresWila_native(scores):
    result = swift_so.GetNumScoresWila(scores)
    return result

def GetNumScoresWila_py(scores:'ObjectiveScores') -> int:
    """GetNumScoresWila_py
    
    GetNumScoresWila_py: generated wrapper function for API function GetNumScoresWila
    
    Args:
        scores ('ObjectiveScores'): scores
    
    Returns:
        (int): returned result
    
    """
    scores_xptr = wrap_as_pointer_handle(scores)
    result = _GetNumScoresWila_native(scores_xptr.ptr)
    return result


@_s_wrap.check_exceptions
def _GetScoreWila_native(scores, index):
    result = swift_so.GetScoreWila(scores, index)
    return result

def GetScoreWila_py(scores:'ObjectiveScores', index:int) -> float:
    """GetScoreWila_py
    
    GetScoreWila_py: generated wrapper function for API function GetScoreWila
    
    Args:
        scores ('ObjectiveScores'): scores
        index (int): index
    
    Returns:
        (float): returned result
    
    """
    scores_xptr = wrap_as_pointer_handle(scores)
    result = _GetScoreWila_native(scores_xptr.ptr, index)
    return result


@_s_wrap.check_exceptions
def _GetScoreNameWila_native(scores, index):
    result = swift_so.GetScoreNameWila(scores, index)
    return result

def GetScoreNameWila_py(scores:'ObjectiveScores', index:int) -> str:
    """GetScoreNameWila_py
    
    GetScoreNameWila_py: generated wrapper function for API function GetScoreNameWila
    
    Args:
        scores ('ObjectiveScores'): scores
        index (int): index
    
    Returns:
        (str): returned result
    
    """
    scores_xptr = wrap_as_pointer_handle(scores)
    result = _GetScoreNameWila_native(scores_xptr.ptr, index)
    return char_array_to_py(result, dispose=True)


@_s_wrap.check_exceptions
def _GetLengthSetOfScores_native(vectorScores):
    result = swift_so.GetLengthSetOfScores(vectorScores)
    return result

def GetLengthSetOfScores_py(vectorScores:'VectorObjectiveScores') -> int:
    """GetLengthSetOfScores_py
    
    GetLengthSetOfScores_py: generated wrapper function for API function GetLengthSetOfScores
    
    Args:
        vectorScores ('VectorObjectiveScores'): vectorScores
    
    Returns:
        (int): returned result
    
    """
    vectorScores_xptr = wrap_as_pointer_handle(vectorScores)
    result = _GetLengthSetOfScores_native(vectorScores_xptr.ptr)
    return result


@_s_wrap.check_exceptions
def _ExecuteOptimizerWila_native(optimizer):
    result = swift_so.ExecuteOptimizerWila(optimizer)
    return result

def ExecuteOptimizerWila_py(optimizer:'Optimiser') -> 'VectorObjectiveScores':
    """ExecuteOptimizerWila_py
    
    ExecuteOptimizerWila_py: generated wrapper function for API function ExecuteOptimizerWila
    
    Args:
        optimizer ('Optimiser'): optimizer
    
    Returns:
        ('VectorObjectiveScores'): returned result
    
    """
    optimizer_xptr = wrap_as_pointer_handle(optimizer)
    result = _ExecuteOptimizerWila_native(optimizer_xptr.ptr)
    return custom_wrap_cffi_native_handle(result, 'VEC_OBJECTIVE_SCORES_PTR')


@_s_wrap.check_exceptions
def _SetMaxThreadsOptimizerWila_native(optimizer, nThreads):
    swift_so.SetMaxThreadsOptimizerWila(optimizer, nThreads)

def SetMaxThreadsOptimizerWila_py(optimizer:'Optimiser', nThreads:int) -> None:
    """SetMaxThreadsOptimizerWila_py
    
    SetMaxThreadsOptimizerWila_py: generated wrapper function for API function SetMaxThreadsOptimizerWila
    
    Args:
        optimizer ('Optimiser'): optimizer
        nThreads (int): nThreads
    
    """
    optimizer_xptr = wrap_as_pointer_handle(optimizer)
    _SetMaxThreadsOptimizerWila_native(optimizer_xptr.ptr, nThreads)


@_s_wrap.check_exceptions
def _SetDefaultMaxThreadsWila_native(nThreads):
    swift_so.SetDefaultMaxThreadsWila(nThreads)

def SetDefaultMaxThreadsWila_py(nThreads:int) -> None:
    """SetDefaultMaxThreadsWila_py
    
    SetDefaultMaxThreadsWila_py: generated wrapper function for API function SetDefaultMaxThreadsWila
    
    Args:
        nThreads (int): nThreads
    
    """
    _SetDefaultMaxThreadsWila_native(nThreads)


@_s_wrap.check_exceptions
def _GetDefaultMaxThreadsWila_native():
    result = swift_so.GetDefaultMaxThreadsWila()
    return result

def GetDefaultMaxThreadsWila_py() -> int:
    """GetDefaultMaxThreadsWila_py
    
    GetDefaultMaxThreadsWila_py: generated wrapper function for API function GetDefaultMaxThreadsWila
    
    Args:
    
    Returns:
        (int): returned result
    
    """
    result = _GetDefaultMaxThreadsWila_native()
    return result


@_s_wrap.check_exceptions
def _GetOptimizerLogDataWila_native(optimizer):
    result = swift_so.GetOptimizerLogDataWila(optimizer)
    return result

def GetOptimizerLogDataWila_py(optimizer:'Optimiser') -> DeletableCffiNativeHandle:
    """GetOptimizerLogDataWila_py
    
    GetOptimizerLogDataWila_py: generated wrapper function for API function GetOptimizerLogDataWila
    
    Args:
        optimizer ('Optimiser'): optimizer
    
    Returns:
        (DeletableCffiNativeHandle): returned result
    
    """
    optimizer_xptr = wrap_as_pointer_handle(optimizer)
    result = _GetOptimizerLogDataWila_native(optimizer_xptr.ptr)
    return custom_wrap_cffi_native_handle(result, 'OptimizerLogData*', DisposeOptimizerLogDataWila_py)


@_s_wrap.check_exceptions
def _DisposeOptimizerLogDataWila_native(logData):
    swift_so.DisposeOptimizerLogDataWila(logData)

def DisposeOptimizerLogDataWila_py(logData:DeletableCffiNativeHandle) -> None:
    """DisposeOptimizerLogDataWila_py
    
    DisposeOptimizerLogDataWila_py: generated wrapper function for API function DisposeOptimizerLogDataWila
    
    Args:
        logData (DeletableCffiNativeHandle): logData
    
    """
    _DisposeOptimizerLogDataWila_native(logData)


@_s_wrap.check_exceptions
def _SetOptimizerLoggerWila_native(optimizer, type):
    swift_so.SetOptimizerLoggerWila(optimizer, type)

def SetOptimizerLoggerWila_py(optimizer:'Optimiser', type:str) -> None:
    """SetOptimizerLoggerWila_py
    
    SetOptimizerLoggerWila_py: generated wrapper function for API function SetOptimizerLoggerWila
    
    Args:
        optimizer ('Optimiser'): optimizer
        type (str): type
    
    """
    optimizer_xptr = wrap_as_pointer_handle(optimizer)
    type_c_charp = wrap_as_pointer_handle(as_bytes(type))
    _SetOptimizerLoggerWila_native(optimizer_xptr.ptr, type_c_charp.ptr)
    # no cleanup for const char*


@_s_wrap.check_exceptions
def _GetOptimizerLogDataWilaDims_native(logData, logLength, stringDataCount, numericDataCount):
    swift_so.GetOptimizerLogDataWilaDims(logData, logLength, stringDataCount, numericDataCount)

def GetOptimizerLogDataWilaDims_py(logData:DeletableCffiNativeHandle, logLength:np.ndarray, stringDataCount:np.ndarray, numericDataCount:np.ndarray) -> None:
    """GetOptimizerLogDataWilaDims_py
    
    GetOptimizerLogDataWilaDims_py: generated wrapper function for API function GetOptimizerLogDataWilaDims
    
    Args:
        logData (DeletableCffiNativeHandle): logData
        logLength (np.ndarray): logLength
        stringDataCount (np.ndarray): stringDataCount
        numericDataCount (np.ndarray): numericDataCount
    
    """
    _GetOptimizerLogDataWilaDims_native(logData, logLength, stringDataCount, numericDataCount)


@_s_wrap.check_exceptions
def _GetOptimizerLogDataWilaNumericDataNames_native(logData, numericDataIndex):
    result = swift_so.GetOptimizerLogDataWilaNumericDataNames(logData, numericDataIndex)
    return result

def GetOptimizerLogDataWilaNumericDataNames_py(logData:DeletableCffiNativeHandle, numericDataIndex:int) -> str:
    """GetOptimizerLogDataWilaNumericDataNames_py
    
    GetOptimizerLogDataWilaNumericDataNames_py: generated wrapper function for API function GetOptimizerLogDataWilaNumericDataNames
    
    Args:
        logData (DeletableCffiNativeHandle): logData
        numericDataIndex (int): numericDataIndex
    
    Returns:
        (str): returned result
    
    """
    result = _GetOptimizerLogDataWilaNumericDataNames_native(logData, numericDataIndex)
    return char_array_to_py(result, dispose=True)


@_s_wrap.check_exceptions
def _GetOptimizerLogDataWilaStringDataNames_native(logData, stringDataIndex):
    result = swift_so.GetOptimizerLogDataWilaStringDataNames(logData, stringDataIndex)
    return result

def GetOptimizerLogDataWilaStringDataNames_py(logData:DeletableCffiNativeHandle, stringDataIndex:int) -> str:
    """GetOptimizerLogDataWilaStringDataNames_py
    
    GetOptimizerLogDataWilaStringDataNames_py: generated wrapper function for API function GetOptimizerLogDataWilaStringDataNames
    
    Args:
        logData (DeletableCffiNativeHandle): logData
        stringDataIndex (int): stringDataIndex
    
    Returns:
        (str): returned result
    
    """
    result = _GetOptimizerLogDataWilaStringDataNames_native(logData, stringDataIndex)
    return char_array_to_py(result, dispose=True)


@_s_wrap.check_exceptions
def _GetOptimizerLogDataWilaNumericData_native(logData, numericDataIndex, data):
    swift_so.GetOptimizerLogDataWilaNumericData(logData, numericDataIndex, data)

def GetOptimizerLogDataWilaNumericData_py(logData:DeletableCffiNativeHandle, numericDataIndex:int, data:np.ndarray) -> None:
    """GetOptimizerLogDataWilaNumericData_py
    
    GetOptimizerLogDataWilaNumericData_py: generated wrapper function for API function GetOptimizerLogDataWilaNumericData
    
    Args:
        logData (DeletableCffiNativeHandle): logData
        numericDataIndex (int): numericDataIndex
        data (np.ndarray): data
    
    """
    data_numarray = marshal.as_c_double_array(data, shallow=True)
    _GetOptimizerLogDataWilaNumericData_native(logData, numericDataIndex, data_numarray.ptr)
    # data_numarray - no cleanup needed?



def _GetOptimizerLogDataWilaStringData_native(logData, size):
    return swift_so.GetOptimizerLogDataWilaStringData(logData, size)

def GetOptimizerLogDataWilaStringData_py(logData:DeletableCffiNativeHandle):
    """GetOptimizerLogDataWilaStringData_py
    
    GetOptimizerLogDataWilaStringData_py: generated wrapper function for API function GetOptimizerLogDataWilaStringData
    
    
    """



    size = marshal.new_int_scalar_ptr()
    values = _GetOptimizerLogDataWilaStringData_native(logData, size)


    result = charp_array_to_py(values, size[0], True)
    return result

@_s_wrap.check_exceptions
def _CreateStateInitializer_native(type):
    result = swift_so.CreateStateInitializer(type)
    return result

def CreateStateInitializer_py(type:str) -> 'StateInitialiser':
    """CreateStateInitializer_py
    
    CreateStateInitializer_py: generated wrapper function for API function CreateStateInitializer
    
    Args:
        type (str): type
    
    Returns:
        ('StateInitialiser'): returned result
    
    """
    type_c_charp = wrap_as_pointer_handle(as_bytes(type))
    result = _CreateStateInitializer_native(type_c_charp.ptr)
    # no cleanup for const char*
    return custom_wrap_cffi_native_handle(result, 'STATE_INITIALIZER_PTR')


@_s_wrap.check_exceptions
def _CloneStateInitializer_native(stateInitializer):
    result = swift_so.CloneStateInitializer(stateInitializer)
    return result

def CloneStateInitializer_py(stateInitializer:'StateInitialiser') -> 'StateInitialiser':
    """CloneStateInitializer_py
    
    CloneStateInitializer_py: generated wrapper function for API function CloneStateInitializer
    
    Args:
        stateInitializer ('StateInitialiser'): stateInitializer
    
    Returns:
        ('StateInitialiser'): returned result
    
    """
    stateInitializer_xptr = wrap_as_pointer_handle(stateInitializer)
    result = _CloneStateInitializer_native(stateInitializer_xptr.ptr)
    return custom_wrap_cffi_native_handle(result, 'STATE_INITIALIZER_PTR')


@_s_wrap.check_exceptions
def _IsDictionaryStateInitializer_native(stateInitializer):
    result = swift_so.IsDictionaryStateInitializer(stateInitializer)
    return result

def IsDictionaryStateInitializer_py(stateInitializer:'StateInitialiser') -> bool:
    """IsDictionaryStateInitializer_py
    
    IsDictionaryStateInitializer_py: generated wrapper function for API function IsDictionaryStateInitializer
    
    Args:
        stateInitializer ('StateInitialiser'): stateInitializer
    
    Returns:
        (bool): returned result
    
    """
    stateInitializer_xptr = wrap_as_pointer_handle(stateInitializer)
    result = _IsDictionaryStateInitializer_native(stateInitializer_xptr.ptr)
    return result


@_s_wrap.check_exceptions
def _GetValueStateInitializer_native(stateInitializer, identifier):
    result = swift_so.GetValueStateInitializer(stateInitializer, identifier)
    return result

def GetValueStateInitializer_py(stateInitializer:'StateInitialiser', identifier:str) -> float:
    """GetValueStateInitializer_py
    
    GetValueStateInitializer_py: generated wrapper function for API function GetValueStateInitializer
    
    Args:
        stateInitializer ('StateInitialiser'): stateInitializer
        identifier (str): identifier
    
    Returns:
        (float): returned result
    
    """
    stateInitializer_xptr = wrap_as_pointer_handle(stateInitializer)
    identifier_c_charp = wrap_as_pointer_handle(as_bytes(identifier))
    result = _GetValueStateInitializer_native(stateInitializer_xptr.ptr, identifier_c_charp.ptr)
    # no cleanup for const char*
    return result


@_s_wrap.check_exceptions
def _SetValueStateInitializer_native(stateInitializer, identifier, value):
    swift_so.SetValueStateInitializer(stateInitializer, identifier, value)

def SetValueStateInitializer_py(stateInitializer:'StateInitialiser', identifier:str, value:float) -> None:
    """SetValueStateInitializer_py
    
    SetValueStateInitializer_py: generated wrapper function for API function SetValueStateInitializer
    
    Args:
        stateInitializer ('StateInitialiser'): stateInitializer
        identifier (str): identifier
        value (float): value
    
    """
    stateInitializer_xptr = wrap_as_pointer_handle(stateInitializer)
    identifier_c_charp = wrap_as_pointer_handle(as_bytes(identifier))
    _SetValueStateInitializer_native(stateInitializer_xptr.ptr, identifier_c_charp.ptr, value)
    # no cleanup for const char*


@_s_wrap.check_exceptions
def _UseStateInitializerModelRunner_native(simulation, stateInitializer):
    swift_so.UseStateInitializerModelRunner(simulation, stateInitializer)

def UseStateInitializerModelRunner_py(simulation:'Simulation', stateInitializer:'StateInitialiser') -> None:
    """UseStateInitializerModelRunner_py
    
    UseStateInitializerModelRunner_py: generated wrapper function for API function UseStateInitializerModelRunner
    
    Args:
        simulation ('Simulation'): simulation
        stateInitializer ('StateInitialiser'): stateInitializer
    
    """
    simulation_xptr = wrap_as_pointer_handle(simulation)
    stateInitializer_xptr = wrap_as_pointer_handle(stateInitializer)
    _UseStateInitializerModelRunner_native(simulation_xptr.ptr, stateInitializer_xptr.ptr)


@_s_wrap.check_exceptions
def _RemoveStateInitializerModelRunner_native(modelSimulation):
    swift_so.RemoveStateInitializerModelRunner(modelSimulation)

def RemoveStateInitializerModelRunner_py(modelSimulation:'Simulation') -> None:
    """RemoveStateInitializerModelRunner_py
    
    RemoveStateInitializerModelRunner_py: generated wrapper function for API function RemoveStateInitializerModelRunner
    
    Args:
        modelSimulation ('Simulation'): modelSimulation
    
    """
    modelSimulation_xptr = wrap_as_pointer_handle(modelSimulation)
    _RemoveStateInitializerModelRunner_native(modelSimulation_xptr.ptr)


@_s_wrap.check_exceptions
def _AddStateInitializerModelRunner_native(modelSimulation, stateInit):
    swift_so.AddStateInitializerModelRunner(modelSimulation, stateInit)

def AddStateInitializerModelRunner_py(modelSimulation:'Simulation', stateInit:'StateInitialiser') -> None:
    """AddStateInitializerModelRunner_py
    
    AddStateInitializerModelRunner_py: generated wrapper function for API function AddStateInitializerModelRunner
    
    Args:
        modelSimulation ('Simulation'): modelSimulation
        stateInit ('StateInitialiser'): stateInit
    
    """
    modelSimulation_xptr = wrap_as_pointer_handle(modelSimulation)
    stateInit_xptr = wrap_as_pointer_handle(stateInit)
    _AddStateInitializerModelRunner_native(modelSimulation_xptr.ptr, stateInit_xptr.ptr)


@_s_wrap.check_exceptions
def _SnapshotMemoryStates_native(simulation):
    result = swift_so.SnapshotMemoryStates(simulation)
    return result

def SnapshotMemoryStates_py(simulation:'Simulation') -> 'MemoryStates':
    """SnapshotMemoryStates_py
    
    SnapshotMemoryStates_py: generated wrapper function for API function SnapshotMemoryStates
    
    Args:
        simulation ('Simulation'): simulation
    
    Returns:
        ('MemoryStates'): returned result
    
    """
    simulation_xptr = wrap_as_pointer_handle(simulation)
    result = _SnapshotMemoryStates_native(simulation_xptr.ptr)
    return custom_wrap_cffi_native_handle(result, 'MEMORY_STATES_PTR')


@_s_wrap.check_exceptions
def _ApplyMemoryStates_native(simulation, memoryStates):
    swift_so.ApplyMemoryStates(simulation, memoryStates)

def ApplyMemoryStates_py(simulation:'Simulation', memoryStates:'MemoryStates') -> None:
    """ApplyMemoryStates_py
    
    ApplyMemoryStates_py: generated wrapper function for API function ApplyMemoryStates
    
    Args:
        simulation ('Simulation'): simulation
        memoryStates ('MemoryStates'): memoryStates
    
    """
    simulation_xptr = wrap_as_pointer_handle(simulation)
    memoryStates_xptr = wrap_as_pointer_handle(memoryStates)
    _ApplyMemoryStates_native(simulation_xptr.ptr, memoryStates_xptr.ptr)


@_s_wrap.check_exceptions
def _SetMemoryStates_native(simulation, memoryStates):
    swift_so.SetMemoryStates(simulation, memoryStates)

def SetMemoryStates_py(simulation:'Simulation', memoryStates:'MemoryStates') -> None:
    """SetMemoryStates_py
    
    SetMemoryStates_py: generated wrapper function for API function SetMemoryStates
    
    Args:
        simulation ('Simulation'): simulation
        memoryStates ('MemoryStates'): memoryStates
    
    """
    simulation_xptr = wrap_as_pointer_handle(simulation)
    memoryStates_xptr = wrap_as_pointer_handle(memoryStates)
    _SetMemoryStates_native(simulation_xptr.ptr, memoryStates_xptr.ptr)


@_s_wrap.check_exceptions
def _ClearMemoryStates_native(simulation):
    swift_so.ClearMemoryStates(simulation)

def ClearMemoryStates_py(simulation:'Simulation') -> None:
    """ClearMemoryStates_py
    
    ClearMemoryStates_py: generated wrapper function for API function ClearMemoryStates
    
    Args:
        simulation ('Simulation'): simulation
    
    """
    simulation_xptr = wrap_as_pointer_handle(simulation)
    _ClearMemoryStates_native(simulation_xptr.ptr)


@_s_wrap.check_exceptions
def _SaveParameterizer_native(parameterizer, filepath):
    swift_so.SaveParameterizer(parameterizer, filepath)

def SaveParameterizer_py(parameterizer:'HypercubeParameteriser', filepath:str) -> None:
    """SaveParameterizer_py
    
    SaveParameterizer_py: generated wrapper function for API function SaveParameterizer
    
    Args:
        parameterizer ('HypercubeParameteriser'): parameterizer
        filepath (str): filepath
    
    """
    parameterizer_xptr = wrap_as_pointer_handle(parameterizer)
    filepath_c_charp = wrap_as_pointer_handle(as_bytes(filepath))
    _SaveParameterizer_native(parameterizer_xptr.ptr, filepath_c_charp.ptr)
    # no cleanup for const char*


@_s_wrap.check_exceptions
def _LoadParameterizer_native(filepath):
    result = swift_so.LoadParameterizer(filepath)
    return result

def LoadParameterizer_py(filepath:str) -> 'HypercubeParameteriser':
    """LoadParameterizer_py
    
    LoadParameterizer_py: generated wrapper function for API function LoadParameterizer
    
    Args:
        filepath (str): filepath
    
    Returns:
        ('HypercubeParameteriser'): returned result
    
    """
    filepath_c_charp = wrap_as_pointer_handle(as_bytes(filepath))
    result = _LoadParameterizer_native(filepath_c_charp.ptr)
    # no cleanup for const char*
    return custom_wrap_cffi_native_handle(result, 'HYPERCUBE_PTR')


@_s_wrap.check_exceptions
def _SaveMemoryStatesToFile_native(memoryStates, filePath, format):
    swift_so.SaveMemoryStatesToFile(memoryStates, filePath, format)

def SaveMemoryStatesToFile_py(memoryStates:'MemoryStates', filePath:str, format:str) -> None:
    """SaveMemoryStatesToFile_py
    
    SaveMemoryStatesToFile_py: generated wrapper function for API function SaveMemoryStatesToFile
    
    Args:
        memoryStates ('MemoryStates'): memoryStates
        filePath (str): filePath
        format (str): format
    
    """
    memoryStates_xptr = wrap_as_pointer_handle(memoryStates)
    filePath_c_charp = wrap_as_pointer_handle(as_bytes(filePath))
    format_c_charp = wrap_as_pointer_handle(as_bytes(format))
    _SaveMemoryStatesToFile_native(memoryStates_xptr.ptr, filePath_c_charp.ptr, format_c_charp.ptr)
    # no cleanup for const char*
    # no cleanup for const char*


@_s_wrap.check_exceptions
def _LoadMemoryStatesFromFile_native(filePath, format):
    result = swift_so.LoadMemoryStatesFromFile(filePath, format)
    return result

def LoadMemoryStatesFromFile_py(filePath:str, format:str) -> 'MemoryStates':
    """LoadMemoryStatesFromFile_py
    
    LoadMemoryStatesFromFile_py: generated wrapper function for API function LoadMemoryStatesFromFile
    
    Args:
        filePath (str): filePath
        format (str): format
    
    Returns:
        ('MemoryStates'): returned result
    
    """
    filePath_c_charp = wrap_as_pointer_handle(as_bytes(filePath))
    format_c_charp = wrap_as_pointer_handle(as_bytes(format))
    result = _LoadMemoryStatesFromFile_native(filePath_c_charp.ptr, format_c_charp.ptr)
    # no cleanup for const char*
    # no cleanup for const char*
    return custom_wrap_cffi_native_handle(result, 'MEMORY_STATES_PTR')


@_s_wrap.check_exceptions
def _GetMemoryStates_native(memoryStates):
    result = swift_so.GetMemoryStates(memoryStates)
    return result

def GetMemoryStates_py(memoryStates:'MemoryStates') -> str:
    """GetMemoryStates_py
    
    GetMemoryStates_py: generated wrapper function for API function GetMemoryStates
    
    Args:
        memoryStates ('MemoryStates'): memoryStates
    
    Returns:
        (str): returned result
    
    """
    memoryStates_xptr = wrap_as_pointer_handle(memoryStates)
    result = _GetMemoryStates_native(memoryStates_xptr.ptr)
    return char_array_to_py(result, dispose=True)


@_s_wrap.check_exceptions
def _MemoryStatesFromString_native(jsonString):
    result = swift_so.MemoryStatesFromString(jsonString)
    return result

def MemoryStatesFromString_py(jsonString:str) -> 'MemoryStates':
    """MemoryStatesFromString_py
    
    MemoryStatesFromString_py: generated wrapper function for API function MemoryStatesFromString
    
    Args:
        jsonString (str): jsonString
    
    Returns:
        ('MemoryStates'): returned result
    
    """
    jsonString_c_charp = wrap_as_pointer_handle(as_bytes(jsonString))
    result = _MemoryStatesFromString_native(jsonString_c_charp.ptr)
    # no cleanup for const char*
    return custom_wrap_cffi_native_handle(result, 'MEMORY_STATES_PTR')


@_s_wrap.check_exceptions
def _SaveModelSimulationToJson_native(simulation, jsonFilePath):
    swift_so.SaveModelSimulationToJson(simulation, jsonFilePath)

def SaveModelSimulationToJson_py(simulation:'Simulation', jsonFilePath:str) -> None:
    """SaveModelSimulationToJson_py
    
    SaveModelSimulationToJson_py: generated wrapper function for API function SaveModelSimulationToJson
    
    Args:
        simulation ('Simulation'): simulation
        jsonFilePath (str): jsonFilePath
    
    """
    simulation_xptr = wrap_as_pointer_handle(simulation)
    jsonFilePath_c_charp = wrap_as_pointer_handle(as_bytes(jsonFilePath))
    _SaveModelSimulationToJson_native(simulation_xptr.ptr, jsonFilePath_c_charp.ptr)
    # no cleanup for const char*


@_s_wrap.check_exceptions
def _LoadModelSimulationFromJson_native(jsonFilePath):
    result = swift_so.LoadModelSimulationFromJson(jsonFilePath)
    return result

def LoadModelSimulationFromJson_py(jsonFilePath:str) -> 'Simulation':
    """LoadModelSimulationFromJson_py
    
    LoadModelSimulationFromJson_py: generated wrapper function for API function LoadModelSimulationFromJson
    
    Args:
        jsonFilePath (str): jsonFilePath
    
    Returns:
        ('Simulation'): returned result
    
    """
    jsonFilePath_c_charp = wrap_as_pointer_handle(as_bytes(jsonFilePath))
    result = _LoadModelSimulationFromJson_native(jsonFilePath_c_charp.ptr)
    # no cleanup for const char*
    return custom_wrap_cffi_native_handle(result, 'MODEL_SIMULATION_PTR')


@_s_wrap.check_exceptions
def _PlayDatasetInputs_native(simulation, dataLibrary, identifiers, dataId, resampleMethod, size):
    swift_so.PlayDatasetInputs(simulation, dataLibrary, identifiers, dataId, resampleMethod, size)

def PlayDatasetInputs_py(simulation:'Simulation', dataLibrary:'TimeSeriesLibrary', identifiers:List[str], dataId:List[str], resampleMethod:List[str], size:int) -> None:
    """PlayDatasetInputs_py
    
    PlayDatasetInputs_py: generated wrapper function for API function PlayDatasetInputs
    
    Args:
        simulation ('Simulation'): simulation
        dataLibrary ('TimeSeriesLibrary'): dataLibrary
        identifiers (List[str]): identifiers
        dataId (List[str]): dataId
        resampleMethod (List[str]): resampleMethod
        size (int): size
    
    """
    simulation_xptr = wrap_as_pointer_handle(simulation)
    dataLibrary_xptr = wrap_as_pointer_handle(dataLibrary)
    identifiers_charpp = wrap_as_pointer_handle(marshal.as_arrayof_bytes(identifiers))
    dataId_charpp = wrap_as_pointer_handle(marshal.as_arrayof_bytes(dataId))
    resampleMethod_charpp = wrap_as_pointer_handle(marshal.as_arrayof_bytes(resampleMethod))
    _PlayDatasetInputs_native(simulation_xptr.ptr, dataLibrary_xptr.ptr, identifiers_charpp.ptr, dataId_charpp.ptr, resampleMethod_charpp.ptr, size)
    # clean identifiers_charpp ?
    # clean dataId_charpp ?
    # clean resampleMethod_charpp ?


@_s_wrap.check_exceptions
def _CreateEnsembleForecastSimulation_native(simulation, start, leadTime, ensembleSize, simulationLength, nTimeStepsBetweenForecasts):
    result = swift_so.CreateEnsembleForecastSimulation(simulation, start, leadTime, ensembleSize, simulationLength, nTimeStepsBetweenForecasts)
    return result

def CreateEnsembleForecastSimulation_py(simulation:'Simulation', start:datetime, leadTime:int, ensembleSize:int, simulationLength:int, nTimeStepsBetweenForecasts:int) -> 'EnsembleForecastSimulation':
    """CreateEnsembleForecastSimulation_py
    
    CreateEnsembleForecastSimulation_py: generated wrapper function for API function CreateEnsembleForecastSimulation
    
    Args:
        simulation ('Simulation'): simulation
        start (datetime): start
        leadTime (int): leadTime
        ensembleSize (int): ensembleSize
        simulationLength (int): simulationLength
        nTimeStepsBetweenForecasts (int): nTimeStepsBetweenForecasts
    
    Returns:
        ('EnsembleForecastSimulation'): returned result
    
    """
    simulation_xptr = wrap_as_pointer_handle(simulation)
    start_datetime = marshal.datetime_to_dtts(start)
    result = _CreateEnsembleForecastSimulation_native(simulation_xptr.ptr, start_datetime.obj, leadTime, ensembleSize, simulationLength, nTimeStepsBetweenForecasts)
    # start_datetime - no cleanup needed?
    return custom_wrap_cffi_native_handle(result, 'ENSEMBLE_FORECAST_SIMULATION_PTR')


@_s_wrap.check_exceptions
def _PlayDatasetSingleInput_native(efSimulation, dataLibrary, identifiers, dataId, size):
    swift_so.PlayDatasetSingleInput(efSimulation, dataLibrary, identifiers, dataId, size)

def PlayDatasetSingleInput_py(efSimulation:'EnsembleForecastSimulation', dataLibrary:'TimeSeriesLibrary', identifiers:List[str], dataId:List[str], size:int) -> None:
    """PlayDatasetSingleInput_py
    
    PlayDatasetSingleInput_py: generated wrapper function for API function PlayDatasetSingleInput
    
    Args:
        efSimulation ('EnsembleForecastSimulation'): efSimulation
        dataLibrary ('TimeSeriesLibrary'): dataLibrary
        identifiers (List[str]): identifiers
        dataId (List[str]): dataId
        size (int): size
    
    """
    efSimulation_xptr = wrap_as_pointer_handle(efSimulation)
    dataLibrary_xptr = wrap_as_pointer_handle(dataLibrary)
    identifiers_charpp = wrap_as_pointer_handle(marshal.as_arrayof_bytes(identifiers))
    dataId_charpp = wrap_as_pointer_handle(marshal.as_arrayof_bytes(dataId))
    _PlayDatasetSingleInput_native(efSimulation_xptr.ptr, dataLibrary_xptr.ptr, identifiers_charpp.ptr, dataId_charpp.ptr, size)
    # clean identifiers_charpp ?
    # clean dataId_charpp ?


@_s_wrap.check_exceptions
def _PlayDatasetEnsembleForecastInput_native(efSimulation, dataLibrary, identifiers, dataId, size):
    swift_so.PlayDatasetEnsembleForecastInput(efSimulation, dataLibrary, identifiers, dataId, size)

def PlayDatasetEnsembleForecastInput_py(efSimulation:'EnsembleForecastSimulation', dataLibrary:'TimeSeriesLibrary', identifiers:List[str], dataId:List[str], size:int) -> None:
    """PlayDatasetEnsembleForecastInput_py
    
    PlayDatasetEnsembleForecastInput_py: generated wrapper function for API function PlayDatasetEnsembleForecastInput
    
    Args:
        efSimulation ('EnsembleForecastSimulation'): efSimulation
        dataLibrary ('TimeSeriesLibrary'): dataLibrary
        identifiers (List[str]): identifiers
        dataId (List[str]): dataId
        size (int): size
    
    """
    efSimulation_xptr = wrap_as_pointer_handle(efSimulation)
    dataLibrary_xptr = wrap_as_pointer_handle(dataLibrary)
    identifiers_charpp = wrap_as_pointer_handle(marshal.as_arrayof_bytes(identifiers))
    dataId_charpp = wrap_as_pointer_handle(marshal.as_arrayof_bytes(dataId))
    _PlayDatasetEnsembleForecastInput_native(efSimulation_xptr.ptr, dataLibrary_xptr.ptr, identifiers_charpp.ptr, dataId_charpp.ptr, size)
    # clean identifiers_charpp ?
    # clean dataId_charpp ?


@_s_wrap.check_exceptions
def _ExecuteEnsembleForecastSimulation_native(efSimulation):
    swift_so.ExecuteEnsembleForecastSimulation(efSimulation)

def ExecuteEnsembleForecastSimulation_py(efSimulation:'EnsembleForecastSimulation') -> None:
    """ExecuteEnsembleForecastSimulation_py
    
    ExecuteEnsembleForecastSimulation_py: generated wrapper function for API function ExecuteEnsembleForecastSimulation
    
    Args:
        efSimulation ('EnsembleForecastSimulation'): efSimulation
    
    """
    efSimulation_xptr = wrap_as_pointer_handle(efSimulation)
    _ExecuteEnsembleForecastSimulation_native(efSimulation_xptr.ptr)


@_s_wrap.check_exceptions
def _GetEnsembleForecastSingleRecorded_native(efSimulation, variableIdentifier, leadTimeIndex, ensembleIndex, values):
    swift_so.GetEnsembleForecastSingleRecorded(efSimulation, variableIdentifier, leadTimeIndex, ensembleIndex, values)

def GetEnsembleForecastSingleRecorded_py(efSimulation:'EnsembleForecastSimulation', variableIdentifier:str, leadTimeIndex:int, ensembleIndex:int, values:np.ndarray) -> None:
    """GetEnsembleForecastSingleRecorded_py
    
    GetEnsembleForecastSingleRecorded_py: generated wrapper function for API function GetEnsembleForecastSingleRecorded
    
    Args:
        efSimulation ('EnsembleForecastSimulation'): efSimulation
        variableIdentifier (str): variableIdentifier
        leadTimeIndex (int): leadTimeIndex
        ensembleIndex (int): ensembleIndex
        values (np.ndarray): values
    
    """
    efSimulation_xptr = wrap_as_pointer_handle(efSimulation)
    variableIdentifier_c_charp = wrap_as_pointer_handle(as_bytes(variableIdentifier))
    values_numarray = marshal.as_c_double_array(values, shallow=True)
    _GetEnsembleForecastSingleRecorded_native(efSimulation_xptr.ptr, variableIdentifier_c_charp.ptr, leadTimeIndex, ensembleIndex, values_numarray.ptr)
    # no cleanup for const char*
    # values_numarray - no cleanup needed?


@_s_wrap.check_exceptions
def _GetEnsembleForecastEnsembleRecorded_native(efSimulation, variableIdentifier, leadTimeIndex, values):
    swift_so.GetEnsembleForecastEnsembleRecorded(efSimulation, variableIdentifier, leadTimeIndex, values)

def GetEnsembleForecastEnsembleRecorded_py(efSimulation:'EnsembleForecastSimulation', variableIdentifier:str, leadTimeIndex:int, values:np.ndarray) -> None:
    """GetEnsembleForecastEnsembleRecorded_py
    
    GetEnsembleForecastEnsembleRecorded_py: generated wrapper function for API function GetEnsembleForecastEnsembleRecorded
    
    Args:
        efSimulation ('EnsembleForecastSimulation'): efSimulation
        variableIdentifier (str): variableIdentifier
        leadTimeIndex (int): leadTimeIndex
        values (np.ndarray): values
    
    """
    efSimulation_xptr = wrap_as_pointer_handle(efSimulation)
    variableIdentifier_c_charp = wrap_as_pointer_handle(as_bytes(variableIdentifier))
    values_doublepp = wrap_as_pointer_handle(as_double_ptr_array(values))
    _GetEnsembleForecastEnsembleRecorded_native(efSimulation_xptr.ptr, variableIdentifier_c_charp.ptr, leadTimeIndex, values_doublepp.ptr)
    # no cleanup for const char*
    # delete[] values_doublepp


@_s_wrap.check_exceptions
def _GetEnsembleForecastLeadLength_native(efSimulation):
    result = swift_so.GetEnsembleForecastLeadLength(efSimulation)
    return result

def GetEnsembleForecastLeadLength_py(efSimulation:'EnsembleForecastSimulation') -> int:
    """GetEnsembleForecastLeadLength_py
    
    GetEnsembleForecastLeadLength_py: generated wrapper function for API function GetEnsembleForecastLeadLength
    
    Args:
        efSimulation ('EnsembleForecastSimulation'): efSimulation
    
    Returns:
        (int): returned result
    
    """
    efSimulation_xptr = wrap_as_pointer_handle(efSimulation)
    result = _GetEnsembleForecastLeadLength_native(efSimulation_xptr.ptr)
    return result


@_s_wrap.check_exceptions
def _GetEnsembleForecastEnsembleSize_native(efSimulation):
    result = swift_so.GetEnsembleForecastEnsembleSize(efSimulation)
    return result

def GetEnsembleForecastEnsembleSize_py(efSimulation:'EnsembleForecastSimulation') -> int:
    """GetEnsembleForecastEnsembleSize_py
    
    GetEnsembleForecastEnsembleSize_py: generated wrapper function for API function GetEnsembleForecastEnsembleSize
    
    Args:
        efSimulation ('EnsembleForecastSimulation'): efSimulation
    
    Returns:
        (int): returned result
    
    """
    efSimulation_xptr = wrap_as_pointer_handle(efSimulation)
    result = _GetEnsembleForecastEnsembleSize_native(efSimulation_xptr.ptr)
    return result


@_s_wrap.check_exceptions
def _PlayEnsembleForecastTimeSeries_native(efSimulation, series, variableIdentifier):
    swift_so.PlayEnsembleForecastTimeSeries(efSimulation, series, variableIdentifier)

def PlayEnsembleForecastTimeSeries_py(efSimulation:'EnsembleForecastSimulation', series:'EnsembleForecastTimeSeries', variableIdentifier:str) -> None:
    """PlayEnsembleForecastTimeSeries_py
    
    PlayEnsembleForecastTimeSeries_py: generated wrapper function for API function PlayEnsembleForecastTimeSeries
    
    Args:
        efSimulation ('EnsembleForecastSimulation'): efSimulation
        series ('EnsembleForecastTimeSeries'): series
        variableIdentifier (str): variableIdentifier
    
    """
    efSimulation_xptr = wrap_as_pointer_handle(efSimulation)
    series_xptr = wrap_as_pointer_handle(series)
    variableIdentifier_c_charp = wrap_as_pointer_handle(as_bytes(variableIdentifier))
    _PlayEnsembleForecastTimeSeries_native(efSimulation_xptr.ptr, series_xptr.ptr, variableIdentifier_c_charp.ptr)
    # no cleanup for const char*


@_s_wrap.check_exceptions
def _RecordEnsembleForecastTimeSeries_native(efSimulation, variableIdentifier):
    swift_so.RecordEnsembleForecastTimeSeries(efSimulation, variableIdentifier)

def RecordEnsembleForecastTimeSeries_py(efSimulation:'EnsembleForecastSimulation', variableIdentifier:str) -> None:
    """RecordEnsembleForecastTimeSeries_py
    
    RecordEnsembleForecastTimeSeries_py: generated wrapper function for API function RecordEnsembleForecastTimeSeries
    
    Args:
        efSimulation ('EnsembleForecastSimulation'): efSimulation
        variableIdentifier (str): variableIdentifier
    
    """
    efSimulation_xptr = wrap_as_pointer_handle(efSimulation)
    variableIdentifier_c_charp = wrap_as_pointer_handle(as_bytes(variableIdentifier))
    _RecordEnsembleForecastTimeSeries_native(efSimulation_xptr.ptr, variableIdentifier_c_charp.ptr)
    # no cleanup for const char*


@_s_wrap.check_exceptions
def _GetRecordedEnsembleForecastTimeSeries_native(efSimulation, variableIdentifier):
    result = swift_so.GetRecordedEnsembleForecastTimeSeries(efSimulation, variableIdentifier)
    return result

def GetRecordedEnsembleForecastTimeSeries_py(efSimulation:'EnsembleForecastSimulation', variableIdentifier:str) -> 'EnsembleForecastTimeSeries':
    """GetRecordedEnsembleForecastTimeSeries_py
    
    GetRecordedEnsembleForecastTimeSeries_py: generated wrapper function for API function GetRecordedEnsembleForecastTimeSeries
    
    Args:
        efSimulation ('EnsembleForecastSimulation'): efSimulation
        variableIdentifier (str): variableIdentifier
    
    Returns:
        ('EnsembleForecastTimeSeries'): returned result
    
    """
    efSimulation_xptr = wrap_as_pointer_handle(efSimulation)
    variableIdentifier_c_charp = wrap_as_pointer_handle(as_bytes(variableIdentifier))
    result = _GetRecordedEnsembleForecastTimeSeries_native(efSimulation_xptr.ptr, variableIdentifier_c_charp.ptr)
    # no cleanup for const char*
    return custom_wrap_cffi_native_handle(result, 'ENSEMBLE_FORECAST_TIME_SERIES_PTR')


@_s_wrap.check_exceptions
def _RecordEnsembleForecastToRecorder_native(efSimulation, variableIdentifiers, dataLibrary, dataIdentifiers, size):
    swift_so.RecordEnsembleForecastToRecorder(efSimulation, variableIdentifiers, dataLibrary, dataIdentifiers, size)

def RecordEnsembleForecastToRecorder_py(efSimulation:'EnsembleForecastSimulation', variableIdentifiers:List[str], dataLibrary:'TimeSeriesLibrary', dataIdentifiers:List[str], size:int) -> None:
    """RecordEnsembleForecastToRecorder_py
    
    RecordEnsembleForecastToRecorder_py: generated wrapper function for API function RecordEnsembleForecastToRecorder
    
    Args:
        efSimulation ('EnsembleForecastSimulation'): efSimulation
        variableIdentifiers (List[str]): variableIdentifiers
        dataLibrary ('TimeSeriesLibrary'): dataLibrary
        dataIdentifiers (List[str]): dataIdentifiers
        size (int): size
    
    """
    efSimulation_xptr = wrap_as_pointer_handle(efSimulation)
    variableIdentifiers_charpp = wrap_as_pointer_handle(marshal.as_arrayof_bytes(variableIdentifiers))
    dataLibrary_xptr = wrap_as_pointer_handle(dataLibrary)
    dataIdentifiers_charpp = wrap_as_pointer_handle(marshal.as_arrayof_bytes(dataIdentifiers))
    _RecordEnsembleForecastToRecorder_native(efSimulation_xptr.ptr, variableIdentifiers_charpp.ptr, dataLibrary_xptr.ptr, dataIdentifiers_charpp.ptr, size)
    # clean variableIdentifiers_charpp ?
    # clean dataIdentifiers_charpp ?


@_s_wrap.check_exceptions
def _GetNumModelRunners_native():
    result = swift_so.GetNumModelRunners()
    return result

def GetNumModelRunners_py() -> int:
    """GetNumModelRunners_py
    
    GetNumModelRunners_py: generated wrapper function for API function GetNumModelRunners
    
    Args:
    
    Returns:
        (int): returned result
    
    """
    result = _GetNumModelRunners_native()
    return result


@_s_wrap.check_exceptions
def _GetNumCatchments_native():
    result = swift_so.GetNumCatchments()
    return result

def GetNumCatchments_py() -> int:
    """GetNumCatchments_py
    
    GetNumCatchments_py: generated wrapper function for API function GetNumCatchments
    
    Args:
    
    Returns:
        (int): returned result
    
    """
    result = _GetNumCatchments_native()
    return result


@_s_wrap.check_exceptions
def _GetNumRainfallRunoff_native():
    result = swift_so.GetNumRainfallRunoff()
    return result

def GetNumRainfallRunoff_py() -> int:
    """GetNumRainfallRunoff_py
    
    GetNumRainfallRunoff_py: generated wrapper function for API function GetNumRainfallRunoff
    
    Args:
    
    Returns:
        (int): returned result
    
    """
    result = _GetNumRainfallRunoff_native()
    return result


@_s_wrap.check_exceptions
def _GetNumHyperCubes_native():
    result = swift_so.GetNumHyperCubes()
    return result

def GetNumHyperCubes_py() -> int:
    """GetNumHyperCubes_py
    
    GetNumHyperCubes_py: generated wrapper function for API function GetNumHyperCubes
    
    Args:
    
    Returns:
        (int): returned result
    
    """
    result = _GetNumHyperCubes_native()
    return result


@_s_wrap.check_exceptions
def _GetNumHyperCubesWila_native():
    result = swift_so.GetNumHyperCubesWila()
    return result

def GetNumHyperCubesWila_py() -> int:
    """GetNumHyperCubesWila_py
    
    GetNumHyperCubesWila_py: generated wrapper function for API function GetNumHyperCubesWila
    
    Args:
    
    Returns:
        (int): returned result
    
    """
    result = _GetNumHyperCubesWila_native()
    return result


@_s_wrap.check_exceptions
def _GetNumStateInitializers_native():
    result = swift_so.GetNumStateInitializers()
    return result

def GetNumStateInitializers_py() -> int:
    """GetNumStateInitializers_py
    
    GetNumStateInitializers_py: generated wrapper function for API function GetNumStateInitializers
    
    Args:
    
    Returns:
        (int): returned result
    
    """
    result = _GetNumStateInitializers_native()
    return result


@_s_wrap.check_exceptions
def _SetLogLikelihoodVariableNames_native(a, b, m, s, maxobs, ct, censopt):
    swift_so.SetLogLikelihoodVariableNames(a, b, m, s, maxobs, ct, censopt)

def SetLogLikelihoodVariableNames_py(a:str, b:str, m:str, s:str, maxobs:str, ct:str, censopt:str) -> None:
    """SetLogLikelihoodVariableNames_py
    
    SetLogLikelihoodVariableNames_py: generated wrapper function for API function SetLogLikelihoodVariableNames
    
    Args:
        a (str): a
        b (str): b
        m (str): m
        s (str): s
        maxobs (str): maxobs
        ct (str): ct
        censopt (str): censopt
    
    """
    a_c_charp = wrap_as_pointer_handle(as_bytes(a))
    b_c_charp = wrap_as_pointer_handle(as_bytes(b))
    m_c_charp = wrap_as_pointer_handle(as_bytes(m))
    s_c_charp = wrap_as_pointer_handle(as_bytes(s))
    maxobs_c_charp = wrap_as_pointer_handle(as_bytes(maxobs))
    ct_c_charp = wrap_as_pointer_handle(as_bytes(ct))
    censopt_c_charp = wrap_as_pointer_handle(as_bytes(censopt))
    _SetLogLikelihoodVariableNames_native(a_c_charp.ptr, b_c_charp.ptr, m_c_charp.ptr, s_c_charp.ptr, maxobs_c_charp.ptr, ct_c_charp.ptr, censopt_c_charp.ptr)
    # no cleanup for const char*
    # no cleanup for const char*
    # no cleanup for const char*
    # no cleanup for const char*
    # no cleanup for const char*
    # no cleanup for const char*
    # no cleanup for const char*


@_s_wrap.check_exceptions
def _SetLogLikelihoodXVariableNames_native(a, b, m, s1, s2, w, maxobs, ct, censopt):
    swift_so.SetLogLikelihoodXVariableNames(a, b, m, s1, s2, w, maxobs, ct, censopt)

def SetLogLikelihoodXVariableNames_py(a:str, b:str, m:str, s1:str, s2:str, w:str, maxobs:str, ct:str, censopt:str) -> None:
    """SetLogLikelihoodXVariableNames_py
    
    SetLogLikelihoodXVariableNames_py: generated wrapper function for API function SetLogLikelihoodXVariableNames
    
    Args:
        a (str): a
        b (str): b
        m (str): m
        s1 (str): s1
        s2 (str): s2
        w (str): w
        maxobs (str): maxobs
        ct (str): ct
        censopt (str): censopt
    
    """
    a_c_charp = wrap_as_pointer_handle(as_bytes(a))
    b_c_charp = wrap_as_pointer_handle(as_bytes(b))
    m_c_charp = wrap_as_pointer_handle(as_bytes(m))
    s1_c_charp = wrap_as_pointer_handle(as_bytes(s1))
    s2_c_charp = wrap_as_pointer_handle(as_bytes(s2))
    w_c_charp = wrap_as_pointer_handle(as_bytes(w))
    maxobs_c_charp = wrap_as_pointer_handle(as_bytes(maxobs))
    ct_c_charp = wrap_as_pointer_handle(as_bytes(ct))
    censopt_c_charp = wrap_as_pointer_handle(as_bytes(censopt))
    _SetLogLikelihoodXVariableNames_native(a_c_charp.ptr, b_c_charp.ptr, m_c_charp.ptr, s1_c_charp.ptr, s2_c_charp.ptr, w_c_charp.ptr, maxobs_c_charp.ptr, ct_c_charp.ptr, censopt_c_charp.ptr)
    # no cleanup for const char*
    # no cleanup for const char*
    # no cleanup for const char*
    # no cleanup for const char*
    # no cleanup for const char*
    # no cleanup for const char*
    # no cleanup for const char*
    # no cleanup for const char*
    # no cleanup for const char*


@_s_wrap.check_exceptions
def _SetLogLikelihoodMixtureVariableNames_native(a, b, m, s1, s2, w, maxobs, ct, censopt):
    swift_so.SetLogLikelihoodMixtureVariableNames(a, b, m, s1, s2, w, maxobs, ct, censopt)

def SetLogLikelihoodMixtureVariableNames_py(a:str, b:str, m:str, s1:str, s2:str, w:str, maxobs:str, ct:str, censopt:str) -> None:
    """SetLogLikelihoodMixtureVariableNames_py
    
    SetLogLikelihoodMixtureVariableNames_py: generated wrapper function for API function SetLogLikelihoodMixtureVariableNames
    
    Args:
        a (str): a
        b (str): b
        m (str): m
        s1 (str): s1
        s2 (str): s2
        w (str): w
        maxobs (str): maxobs
        ct (str): ct
        censopt (str): censopt
    
    """
    a_c_charp = wrap_as_pointer_handle(as_bytes(a))
    b_c_charp = wrap_as_pointer_handle(as_bytes(b))
    m_c_charp = wrap_as_pointer_handle(as_bytes(m))
    s1_c_charp = wrap_as_pointer_handle(as_bytes(s1))
    s2_c_charp = wrap_as_pointer_handle(as_bytes(s2))
    w_c_charp = wrap_as_pointer_handle(as_bytes(w))
    maxobs_c_charp = wrap_as_pointer_handle(as_bytes(maxobs))
    ct_c_charp = wrap_as_pointer_handle(as_bytes(ct))
    censopt_c_charp = wrap_as_pointer_handle(as_bytes(censopt))
    _SetLogLikelihoodMixtureVariableNames_native(a_c_charp.ptr, b_c_charp.ptr, m_c_charp.ptr, s1_c_charp.ptr, s2_c_charp.ptr, w_c_charp.ptr, maxobs_c_charp.ptr, ct_c_charp.ptr, censopt_c_charp.ptr)
    # no cleanup for const char*
    # no cleanup for const char*
    # no cleanup for const char*
    # no cleanup for const char*
    # no cleanup for const char*
    # no cleanup for const char*
    # no cleanup for const char*
    # no cleanup for const char*
    # no cleanup for const char*


@_s_wrap.check_exceptions
def _LoadVersionOneControlFile_native(controlFileName, rootDataDir):
    result = swift_so.LoadVersionOneControlFile(controlFileName, rootDataDir)
    return result

def LoadVersionOneControlFile_py(controlFileName:str, rootDataDir:str) -> 'Simulation':
    """LoadVersionOneControlFile_py
    
    LoadVersionOneControlFile_py: generated wrapper function for API function LoadVersionOneControlFile
    
    Args:
        controlFileName (str): controlFileName
        rootDataDir (str): rootDataDir
    
    Returns:
        ('Simulation'): returned result
    
    """
    controlFileName_c_charp = wrap_as_pointer_handle(as_bytes(controlFileName))
    rootDataDir_c_charp = wrap_as_pointer_handle(as_bytes(rootDataDir))
    result = _LoadVersionOneControlFile_native(controlFileName_c_charp.ptr, rootDataDir_c_charp.ptr)
    # no cleanup for const char*
    # no cleanup for const char*
    return custom_wrap_cffi_native_handle(result, 'MODEL_SIMULATION_PTR')


@_s_wrap.check_exceptions
def _LoadVersionOneTimeSeriesFile_native(fileName):
    result = swift_so.LoadVersionOneTimeSeriesFile(fileName)
    return result

def LoadVersionOneTimeSeriesFile_py(fileName:str) -> 'TimeSeriesProvider':
    """LoadVersionOneTimeSeriesFile_py
    
    LoadVersionOneTimeSeriesFile_py: generated wrapper function for API function LoadVersionOneTimeSeriesFile
    
    Args:
        fileName (str): fileName
    
    Returns:
        ('TimeSeriesProvider'): returned result
    
    """
    fileName_c_charp = wrap_as_pointer_handle(as_bytes(fileName))
    result = _LoadVersionOneTimeSeriesFile_native(fileName_c_charp.ptr)
    # no cleanup for const char*
    return custom_wrap_cffi_native_handle(result, 'TIME_SERIES_PROVIDER_PTR')


@_s_wrap.check_exceptions
def _RegisterAdditionalSwiftDataHandling_native(type):
    result = swift_so.RegisterAdditionalSwiftDataHandling(type)
    return result

def RegisterAdditionalSwiftDataHandling_py(type:str) -> bool:
    """RegisterAdditionalSwiftDataHandling_py
    
    RegisterAdditionalSwiftDataHandling_py: generated wrapper function for API function RegisterAdditionalSwiftDataHandling
    
    Args:
        type (str): type
    
    Returns:
        (bool): returned result
    
    """
    type_c_charp = wrap_as_pointer_handle(as_bytes(type))
    result = _RegisterAdditionalSwiftDataHandling_native(type_c_charp.ptr)
    # no cleanup for const char*
    return result


@_s_wrap.check_exceptions
def _GetNumMemTestCatchments_native():
    result = swift_so.GetNumMemTestCatchments()
    return result

def GetNumMemTestCatchments_py() -> int:
    """GetNumMemTestCatchments_py
    
    GetNumMemTestCatchments_py: generated wrapper function for API function GetNumMemTestCatchments
    
    Args:
    
    Returns:
        (int): returned result
    
    """
    result = _GetNumMemTestCatchments_native()
    return result


@_s_wrap.check_exceptions
def _GetNumMemTestModelRunners_native():
    result = swift_so.GetNumMemTestModelRunners()
    return result

def GetNumMemTestModelRunners_py() -> int:
    """GetNumMemTestModelRunners_py
    
    GetNumMemTestModelRunners_py: generated wrapper function for API function GetNumMemTestModelRunners
    
    Args:
    
    Returns:
        (int): returned result
    
    """
    result = _GetNumMemTestModelRunners_native()
    return result


@_s_wrap.check_exceptions
def _CreateTestMemoryTrackedSimulation_native():
    result = swift_so.CreateTestMemoryTrackedSimulation()
    return result

def CreateTestMemoryTrackedSimulation_py() -> 'Simulation':
    """CreateTestMemoryTrackedSimulation_py
    
    CreateTestMemoryTrackedSimulation_py: generated wrapper function for API function CreateTestMemoryTrackedSimulation
    
    Args:
    
    Returns:
        ('Simulation'): returned result
    
    """
    result = _CreateTestMemoryTrackedSimulation_native()
    return custom_wrap_cffi_native_handle(result, 'MODEL_SIMULATION_PTR')


@_s_wrap.check_exceptions
def _GetNumMemTestParameterizers_native():
    result = swift_so.GetNumMemTestParameterizers()
    return result

def GetNumMemTestParameterizers_py() -> int:
    """GetNumMemTestParameterizers_py
    
    GetNumMemTestParameterizers_py: generated wrapper function for API function GetNumMemTestParameterizers
    
    Args:
    
    Returns:
        (int): returned result
    
    """
    result = _GetNumMemTestParameterizers_native()
    return result


@_s_wrap.check_exceptions
def _CreateTestMemoryTrackedParameterizer_native():
    result = swift_so.CreateTestMemoryTrackedParameterizer()
    return result

def CreateTestMemoryTrackedParameterizer_py() -> 'HypercubeParameteriser':
    """CreateTestMemoryTrackedParameterizer_py
    
    CreateTestMemoryTrackedParameterizer_py: generated wrapper function for API function CreateTestMemoryTrackedParameterizer
    
    Args:
    
    Returns:
        ('HypercubeParameteriser'): returned result
    
    """
    result = _CreateTestMemoryTrackedParameterizer_native()
    return custom_wrap_cffi_native_handle(result, 'HYPERCUBE_PTR')


@_s_wrap.check_exceptions
def _GetNodeName_native(simulation, index):
    result = swift_so.GetNodeName(simulation, index)
    return result

def GetNodeName_py(simulation:'Simulation', index:int) -> str:
    """GetNodeName_py
    
    GetNodeName_py: generated wrapper function for API function GetNodeName
    
    Args:
        simulation ('Simulation'): simulation
        index (int): index
    
    Returns:
        (str): returned result
    
    """
    simulation_xptr = wrap_as_pointer_handle(simulation)
    result = _GetNodeName_native(simulation_xptr.ptr, index)
    return char_array_to_py(result, dispose=True)


@_s_wrap.check_exceptions
def _GetLinkName_native(simulation, index):
    result = swift_so.GetLinkName(simulation, index)
    return result

def GetLinkName_py(simulation:'Simulation', index:int) -> str:
    """GetLinkName_py
    
    GetLinkName_py: generated wrapper function for API function GetLinkName
    
    Args:
        simulation ('Simulation'): simulation
        index (int): index
    
    Returns:
        (str): returned result
    
    """
    simulation_xptr = wrap_as_pointer_handle(simulation)
    result = _GetLinkName_native(simulation_xptr.ptr, index)
    return char_array_to_py(result, dispose=True)


@_s_wrap.check_exceptions
def _GetRecordedVariableName_native(simulation, index):
    result = swift_so.GetRecordedVariableName(simulation, index)
    return result

def GetRecordedVariableName_py(simulation:'Simulation', index:int) -> str:
    """GetRecordedVariableName_py
    
    GetRecordedVariableName_py: generated wrapper function for API function GetRecordedVariableName
    
    Args:
        simulation ('Simulation'): simulation
        index (int): index
    
    Returns:
        (str): returned result
    
    """
    simulation_xptr = wrap_as_pointer_handle(simulation)
    result = _GetRecordedVariableName_native(simulation_xptr.ptr, index)
    return char_array_to_py(result, dispose=True)


@_s_wrap.check_exceptions
def _GetPlayedVariableName_native(simulation, index):
    result = swift_so.GetPlayedVariableName(simulation, index)
    return result

def GetPlayedVariableName_py(simulation:'Simulation', index:int) -> str:
    """GetPlayedVariableName_py
    
    GetPlayedVariableName_py: generated wrapper function for API function GetPlayedVariableName
    
    Args:
        simulation ('Simulation'): simulation
        index (int): index
    
    Returns:
        (str): returned result
    
    """
    simulation_xptr = wrap_as_pointer_handle(simulation)
    result = _GetPlayedVariableName_native(simulation_xptr.ptr, index)
    return char_array_to_py(result, dispose=True)


@_s_wrap.check_exceptions
def _GetSubareaName_native(simulation, index):
    result = swift_so.GetSubareaName(simulation, index)
    return result

def GetSubareaName_py(simulation:'Simulation', index:int) -> str:
    """GetSubareaName_py
    
    GetSubareaName_py: generated wrapper function for API function GetSubareaName
    
    Args:
        simulation ('Simulation'): simulation
        index (int): index
    
    Returns:
        (str): returned result
    
    """
    simulation_xptr = wrap_as_pointer_handle(simulation)
    result = _GetSubareaName_native(simulation_xptr.ptr, index)
    return char_array_to_py(result, dispose=True)


@_s_wrap.check_exceptions
def _GetNodeIdentifier_native(simulation, index):
    result = swift_so.GetNodeIdentifier(simulation, index)
    return result

def GetNodeIdentifier_py(simulation:'Simulation', index:int) -> str:
    """GetNodeIdentifier_py
    
    GetNodeIdentifier_py: generated wrapper function for API function GetNodeIdentifier
    
    Args:
        simulation ('Simulation'): simulation
        index (int): index
    
    Returns:
        (str): returned result
    
    """
    simulation_xptr = wrap_as_pointer_handle(simulation)
    result = _GetNodeIdentifier_native(simulation_xptr.ptr, index)
    return char_array_to_py(result, dispose=True)


@_s_wrap.check_exceptions
def _GetLinkIdentifier_native(simulation, index):
    result = swift_so.GetLinkIdentifier(simulation, index)
    return result

def GetLinkIdentifier_py(simulation:'Simulation', index:int) -> str:
    """GetLinkIdentifier_py
    
    GetLinkIdentifier_py: generated wrapper function for API function GetLinkIdentifier
    
    Args:
        simulation ('Simulation'): simulation
        index (int): index
    
    Returns:
        (str): returned result
    
    """
    simulation_xptr = wrap_as_pointer_handle(simulation)
    result = _GetLinkIdentifier_native(simulation_xptr.ptr, index)
    return char_array_to_py(result, dispose=True)


@_s_wrap.check_exceptions
def _GetSubareaIdentifier_native(simulation, index):
    result = swift_so.GetSubareaIdentifier(simulation, index)
    return result

def GetSubareaIdentifier_py(simulation:'Simulation', index:int) -> str:
    """GetSubareaIdentifier_py
    
    GetSubareaIdentifier_py: generated wrapper function for API function GetSubareaIdentifier
    
    Args:
        simulation ('Simulation'): simulation
        index (int): index
    
    Returns:
        (str): returned result
    
    """
    simulation_xptr = wrap_as_pointer_handle(simulation)
    result = _GetSubareaIdentifier_native(simulation_xptr.ptr, index)
    return char_array_to_py(result, dispose=True)


@_s_wrap.check_exceptions
def _GetElementVarIdentifier_native(simulation, elementId, index):
    result = swift_so.GetElementVarIdentifier(simulation, elementId, index)
    return result

def GetElementVarIdentifier_py(simulation:'Simulation', elementId:str, index:int) -> str:
    """GetElementVarIdentifier_py
    
    GetElementVarIdentifier_py: generated wrapper function for API function GetElementVarIdentifier
    
    Args:
        simulation ('Simulation'): simulation
        elementId (str): elementId
        index (int): index
    
    Returns:
        (str): returned result
    
    """
    simulation_xptr = wrap_as_pointer_handle(simulation)
    elementId_c_charp = wrap_as_pointer_handle(as_bytes(elementId))
    result = _GetElementVarIdentifier_native(simulation_xptr.ptr, elementId_c_charp.ptr, index)
    # no cleanup for const char*
    return char_array_to_py(result, dispose=True)


