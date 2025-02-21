from datetime import datetime
from typing import (
    TYPE_CHECKING,
    Any,
    Callable,
    Dict,
    List,
    Optional,
    OrderedDict,
    Sequence,
    Union,
)

import numpy as np
import pandas as pd
import uchronia.classes as uc
import xarray as xr
from cffi import FFI
from cinterop.timeseries import ConvertibleToTimestamp, TimeSeriesLike
from refcount.interop import CffiData, CffiWrapperFactory, DeletableCffiNativeHandle

import swift2.model_definitions as smd
import swift2.parameteriser as sp
import swift2.play_record as spr
import swift2.simulation as ss
import swift2.statistics as ssf
import swift2.wrap.swift_wrap_custom as swc
import swift2.wrap.swift_wrap_generated as swg
from swift2.const import CATCHMENT_FLOWRATE_VARID
from swift2.utils import parameter_df

if TYPE_CHECKING:
    from uchronia.classes import TimeSeriesLibrary

    from swift2.const import RecordToSignature, VecNum, VecScalars, VecStr


class SimulationMixin:
    """A parent class for simulation objects. Most users are unlikely to explicitly use it."""

    def __init__(
        self,
    ):
        super(SimulationMixin, self).__init__()

    def record_state(
        self,
        var_ids: "VecStr" = CATCHMENT_FLOWRATE_VARID,
        recording_provider: Optional["TimeSeriesLibrary"] = None,
        data_ids: Optional["VecStr"] = None,
    ) -> None:
        """
        Record a time series of one of the state of the model

        Args:
            var_ids (VecStr, optional): identifier(s) of the output variable recorded to a time series, e.g. 'Catchment|StreamflowRate' or 'subcatchment.Subarea.runoff'. Defaults to CATCHMENT_FLOWRATE_VARID.
            recording_provider (TimeSeriesLibrary, optional): _description_. Defaults to None.
            data_ids (VecStr, optional): _description_. Defaults to None.

        Raises:
            ValueError: _description_
        """
        spr.record_state(self, var_ids, recording_provider, data_ids)

    def get_recorded_varnames(self) -> List[str]:
        """
        Gets all the names of the recorded states

        Returns:
            List[str]: The names of the state variables being recorded into time series
        """
        return spr.get_recorded_varnames(self)

    def get_played_varnames(self) -> List[str]:
        """
        Gets all the names of states fed an input time series

        Returns:
            List[str]: The names of the state variables fed over the simulation with values from a time series
        """
        return spr.get_played_varnames(self)

    def exec_simulation(self, reset_initial_states: bool = True) -> None:
        """
        Execute a simulation

        Args:
            reset_initial_states (bool): logical, should the states of the model be reinitialized before the first time step.

        """
        ss.exec_simulation(self, reset_initial_states)


class Simulation(DeletableCffiNativeHandle, SimulationMixin):
    """Wrapper around single dimension simulation objects"""

    def __init__(
        self,
        handle: CffiData,
        release_native: Callable[[CffiData], None],
        type_id: Optional[str] = None,
        prior_ref_count: int = 0,
    ):
        super(Simulation, self).__init__(
            handle, release_native, type_id, prior_ref_count
        )

    @staticmethod
    def from_json_file(file_path:str) -> "Simulation":
        """Create a model simulation from a file with a JSON serialisation.

        Args:
            file_path (str): valid file path.

        Returns:
            Simulation: a catchment simulation.
        """
        return smd.model_from_json_file(file_path)

    def to_json_file(self, file_path:str) -> None:
        """Save a model simulation from a file with a JSON serialisation.

        Args:
            file_path (str): file path to save to
        """
        smd.model_to_json_file(self, file_path)

    def clone(self) -> "Simulation":
        """Clone this simulation (deep copy)

        Returns:
            Simulation: A new simulation object
        """
        return swg.CloneModel_py(self)

    def __str__(self):
        """string representation"""
        tid = self.type_id if self.type_id is not None else ""
        return f'Simulation wrapper for a CFFI pointer handle to a native pointer of type id "{tid}"'

    def get_simulation_span(self) -> Dict[str, Any]:
        """Gets the simulation span of this simulation

        Returns:
            Dict[str,Any]: information on start, end, time step
        """
        return swc.get_simulation_span_pkg(self)

    def set_simulation_span(
        self, start: ConvertibleToTimestamp, end: ConvertibleToTimestamp
    ) -> None:
        """
        Sets the simulation span

        Args:
            start (ConvertibleToTimestamp): the start date of the simulation. The time zone will be forced to UTC.
            end (ConvertibleToTimestamp): the end date of the simulation. The time zone will be forced to UTC.
        """
        ss.set_simulation_span(self, start, end)

    def set_simulation_time_step(self, name: str) -> None:
        """
        Sets the time step of this simulation

        Args:
            name (str): a time step identifier, currently 'daily' or 'hourly' are supported. The identifier is made lower case in the function.
        """
        ss.set_simulation_time_step(self, name)

    def check_simulation(self) -> Dict:
        """
        Checks whether a simulation is configured to a state where it is executable
        """
        return ss.check_simulation(self)

    def swap_model(self, model_id: str, what: str = "runoff") -> "Simulation":
        """
        Clone and change a simulation, using another model

        Args:
            model_id (str): the identifier of the new model to use, e.g. 'GR4J'
            what (str): character identifying the type of structure replaced: 'runoff', 'channel_routing'

        Returns:
            Simulation: A SWIFT simulation object, clone of the simulation but with a new model type in use.

        """
        return ss.swap_model(self, model_id, what)

    def set_error_correction_model(
        self, model_id: str, element_id: str, length: int = 1, seed: int = 0
    ) -> None:
        """
        Add an error correction model to an element in a catchment

        Args:
            model_id (str): the identifier of the new model to use, e.g. 'ERRIS'
            element_id (str): the identifier of the catchment element (node, link, subcatchment) whose outflow rate is corrected.
            length (int): other parameters to pass to the creation of the error correction model. Currently length of the AR model only supported.
            seed (int): other parameters to pass to the creation of the error correction model. Currently length of the AR model only supported.

        """
        ss.set_error_correction_model(self, model_id, element_id, length, seed)

    def sort_by_execution_order(
        self, split_element_ids: Sequence[str], sorting_option: str = ""
    ) -> List[str]:
        """
        Sort the specified element ids according to the execution order of the simulation

        Args:
            split_element_ids (Sequence[str]): a character vector with element identifiers such as 'node.n1', 'link.linkId_2'
            sorting_option (str): a character - for future options. Ignored for now.

        Returns:
            List[str]: values in split_element_ids sorted by simulation execution order

        """
        return ss.sort_by_execution_order(self, split_element_ids, sorting_option)

    def get_link_names(self) -> List[str]:
        """
        Gets all the names of the links in the catchment
        """
        return ss.get_link_names(self)

    def get_node_names(self) -> List[str]:
        """
        Gets all the names of the nodes in the catchment
        """
        return ss.get_node_names(self)

    def get_subarea_names(self) -> List[str]:
        """
        Gets all the names of the subareas in the catchment
        """
        return ss.get_subarea_names(self)

    def get_link_ids(self) -> List[str]:
        """
        Gets all the identifiers of the links in the catchment
        """
        return ss.get_link_ids(self)

    def get_node_ids(self) -> List[str]:
        """
        Gets all the identifiers of the nodes in the catchment
        """
        return ss.get_node_ids(self)

    def get_subarea_ids(self) -> List[str]:
        """
        Gets all the identifiers of the subareas in the catchment
        """
        return ss.get_subarea_ids(self)

    def get_variable_ids(
        self, element_id: Optional[str] = None, full_id: bool = True
    ) -> List[str]:
        """
        Gets all the names of the variables of an element (link, node, subarea) within a catchment

        Args:
            element_id (Optional[str]): a character, identifier of the element within the catchment
            full_id (bool): boolean, if TRUE return the full hierarchical identifier

        """
        return ss.get_variable_ids(self, element_id, full_id)

    def is_variable_id(self, var_id: "VecStr") -> Union[Dict[str, bool], bool]:
        """Are one or more model state identifier(s) valid

        Args:
            var_id (VecStr): model identifier(s)

        Returns:
            Union[Dict[str, bool], bool]: whether the identifier(s) are valid. A dictionary is returned if the input is vectorised rather than scalar.
        """
        return ss.is_variable_id(self, var_id)

    def get_state_value(self, var_id: "VecStr") -> Union[Dict[str, float], float]:
        """
        Gets the value(s) of a model state(s)

        Args:
            var_id (VecStr): string or sequence of str, model variable state identifier(s)

        Returns:
            value(s) of the requested model states
        """
        return ss.get_state_value(self, var_id)

    def set_state_value(
        self,
        var_id: Union[str, Sequence[str]],
        value: Union[float, int, bool, Sequence] = None,
    ) -> None:
        """
        Sets the value of a model state

        Args:
            var_id (Any): character, model variable state identifier(s)
            value (Any): numeric value(s)

        """
        ss.set_state_value(self, var_id, value)

    def snapshot_state(self) -> "MemoryStates":
        """Take a snapshot of the memory states of a simulation

        Returns:
            MemoryStates: memory states, that can be stored and reapplied
        """
        return ss.snapshot_state(self)

    def set_states(self, states: "MemoryStates") -> None:
        """Apply memory states to a simulation

        Args:
            states (MemoryStates): memory states
        """
        ss.set_states(self, states)

    def set_reservoir_model(self, new_model_id: str, element_id: str) -> None:
        """Sets a new reservoir model on an element

        Args:
            new_model_id (str): Currently one of: "ControlledReleaseReservoir", "LevelVolumeAreaReservoir", "FarmDamReservoir";
            element_id (str): _description_
        """
        swg.SetReservoirModel_py(self, new_model_id, element_id)

    def set_reservoir_geometry(
        self, element_id: str, level: np.ndarray, storage: np.ndarray, area: np.ndarray
    ) -> None:
        """Sets the geometry of a reservoir

        Args:
            element_id (str): Element with a suitable reservoir supporting a geometry description
            level (np.ndarray): array of water surface levels, in S.I. units (m) TO BE CONFIRMED
            storage (np.ndarray): array of volume storages, in S.I. units (m3) TO BE CONFIRMED
            area (np.ndarray): array of surfce areas, in S.I. units (m2) TO BE CONFIRMED
        """
        num_entries = len(level)
        assert len(storage) == num_entries
        assert len(area) == num_entries
        swg.SetReservoirGeometry_py(self, element_id, num_entries, level, storage, area)

    def set_reservoir_min_discharge(
        self, element_id: str, level: np.ndarray, discharge: np.ndarray
    ) -> None:
        """Sets a reservoir operating curve, minimum release for a given level

        Args:
            element_id (str): Element with a suitable reservoir supporting a geometry description
            level (np.ndarray): array of levels (m)
            discharge (np.ndarray): array of minimum discharges (m3/s)
        """
        num_entries = len(level)
        swg.SetReservoirMinDischarge_py(self, element_id, num_entries, level, discharge)

    def set_reservoir_max_discharge(
        self, element_id: str, level: np.ndarray, discharge: np.ndarray
    ) -> None:
        """Sets a reservoir operating curve, maximum release for a given level

        Args:
            element_id (str): Element with a suitable reservoir supporting a geometry description
            level (np.ndarray): array of levels (m)
            discharge (np.ndarray): array of maximum discharges (m3/s)
        """
        num_entries = len(level)
        swg.SetReservoirMaxDischarge_py(self, element_id, num_entries, level, discharge)

    def use_state_initialises(self, state_initialiser: "StateInitialiser"):
        """Sets the state initialiser to use for a simulation. This forces the removal of any prior state initialiser.

        Args:
            state_initialiser (StateInitialiser): the new state initialiser to use
        """
        swg.UseStateInitializerModelRunner_py(self, state_initialiser)

    def remove_state_initialisers(self):
        """Forces the removal of any state initialiser."""
        swg.RemoveStateInitializerModelRunner_py(self)

    def add_state_initialiser(self, state_initialiser: "StateInitialiser"):
        """Adds a state initialiser to any prior list of state initialisers"""
        swg.AddStateInitializerModelRunner_py(self, state_initialiser)

    def reset_model_states(self) -> None:
        """Reset the model states of a simulation, and apply one or more state initialers if the simulation is configured with any."""
        ss.reset_model_states(self)

    def describe(self, verbosity=None) -> Dict:
        """Describe the catchment model structure using simple python representations"""
        return ss.describe(self, verbosity)

    def create_ensemble_forecast_simulation(
        self,
        data_library,
        start: ConvertibleToTimestamp,
        end: ConvertibleToTimestamp,
        input_map: Dict[str, List[str]],
        lead_time: int,
        ensemble_size: int,
        n_time_steps_between_forecasts: int,
    ) -> "EnsembleForecastSimulation":
        """
        Create an ensemble forecast simulation

        Args:
            data_library (Any): external pointer type ENSEMBLE_DATA_SET_PTR, or a Python class wrapper around it 
            start (ConvertibleToTimestamp): the start date of the simulation. The time zone will be forced to UTC.
            end (ConvertibleToTimestamp): the end date of the simulation. The time zone will be forced to UTC.
            input_map (dict): a named list were names are the data library data identifiers, and values are character vectors with model state identifiers.
            lead_time (int): integer, the length in time steps of the forecasts.
            ensemble_size (int): ensemble size
            n_time_steps_between_forecasts (int): nTimeStepsBetweenForecasts

        Returns:
            An external pointer

        """
        return ss.create_ensemble_forecast_simulation(
            self,
            data_library,
            start,
            end,
            input_map,
            lead_time,
            ensemble_size,
            n_time_steps_between_forecasts,
        )

    def ensemble_simulation(self, ensemble_size: int) -> "EnsembleSimulation":
        """Create an ensemble simulation templated from this simulation

        Args:
            ensemble_size (int): The size of the ensemble dimension

        Returns:
            EnsembleSimulation: Ensemble simulation (ensemble simulation runner)
        """        
        return swg.CreateEnsembleModelRunner_py(self, ensembleSize=ensemble_size)

    def erris_ensemble_simulation(
        self,
        warmup_start: ConvertibleToTimestamp,
        warmup_end: ConvertibleToTimestamp,
        observed_ts: TimeSeriesLike,
        error_model_element_id: str,
    ) -> "EnsembleSimulation":
        """Creates an ensemble simulation templated on this simulation, with an ERRIS model on one of the network element

        Args:
            warmup_start (ConvertibleToTimestamp): start time stamp for the warmup period
            warmup_end (ConvertibleToTimestamp): end time stamp for the warmup period
            observed_ts (TimeSeriesLike): Time series of observations to correct prediction against
            error_model_element_id (str): model element identifier where to set up an ERRIS correction model

        Returns:
            EnsembleSimulation: Ensemble simulation (ensemble simulation runner)
        """
        from cinterop.timeseries import as_pydatetime

        from swift2.internal import to_interop_univariate_series
        warmup_start = as_pydatetime(warmup_start)
        warmup_end = as_pydatetime(warmup_end)
        values, ts_geom = to_interop_univariate_series(observed_ts)
        return swg.PrepareEnsembleModelRunner_py(
            self, warmup_start, warmup_end, values, ts_geom, error_model_element_id
        )

    def play_inputs(
        self,
        data_library: uc.TimeSeriesLibrary,
        model_var_id: "VecStr",
        data_id: "VecStr",
        resample: "VecStr" = "",
    ) -> None:
        """
        Assign input time series from a time series library to a model simulation

        Args:
            data_library (TimeSeriesLibrary): external pointer type ENSEMBLE_DATA_SET_PTR, or a Python class wrapper around it 
            model_var_id (str or sequence of str): model state variable unique identifier(s)
            data_id (str or sequence of str): identifier(s) for data in the data_library. If length is not the same as model_var_id, the elements of data_id are reused to match it
            resample (str or sequence of str): identifier(s) for how the series is resampled (aggregated or disaggregated). If length is not the same as model_var_id, the elements of resample are reused to match it

        """
        spr.play_inputs(self, data_library, model_var_id, data_id, resample)

    def play_subarea_input(
        self, input: TimeSeriesLike, subarea_name: str, input_name: str
    ) -> None:
        """
        Sets time series as input to a simulation

        Args:
            input (TimeSeriesLike): univariate time series.
            subarea_name (str): a valid name of the subarea
            input_name (str): the name of the input variable to the model (i.e. 'P' for the precip of GR5H)

        """
        spr.play_subarea_input(self, input, subarea_name, input_name)

    def play_input(
        self, input_ts: TimeSeriesLike, var_ids: Optional["VecStr"] = None
    ) -> None:
        """
        Sets one or more time series as input(s) to a simulation

        Args:
            input_ts (TimeSeriesLike): univariate time series. If an xts time series column names must be valid model variable identifiers, unless explicitely provided via varIds
            var_ids (optional str or sequence of str): optional character, the variable identifiers to use, overriding the column names of the inputTs. If not NULL, must be of length equal to the number of columns in inputTs
        """
        spr.play_singular_simulation(self, input_ts, var_ids)

    def get_played(
        self,
        var_ids: Optional["VecStr"] = None,
        start_time: Optional[ConvertibleToTimestamp] = None,
        end_time: Optional[ConvertibleToTimestamp] = None,
    ) -> xr.DataArray:
        """
        Retrieves one or more played (input) time series from a simulation

        Args:
            var_ids (optional str or sequence of str): name(s) of the model variable(s) into which a time series is played as input. e.g. 'Catchment.StreamflowRate'. If missing, a multivariate time series of all played states is returned; this may be a large amount of data.
            start_time (datetime like): An optional parameter, the start of a period to subset the time series
            end_time (datetime like): An optional parameter, the end of a period to subset the time series

        Returns:
            xr.DataArray: a time series, possibly multivariate.

        """
        return spr.get_played(self, var_ids, start_time, end_time)

    def get_played_varnames(self) -> List[str]:
        """
        Gets all the names of model states fed an input time series
        """
        return spr.get_played_varnames(self)

    def get_recorded(
        self,
        var_ids: Optional["VecStr"] = None,
        start_time: Optional[ConvertibleToTimestamp] = None,
        end_time: Optional[ConvertibleToTimestamp] = None,
    ) -> xr.DataArray:
        """
        Retrieves a recorded time series from a simulation

        Args:
            var_ids (optional str or sequence of str): name(s) of the model variable(s) recorded to a time series. e.g. 'Catchment.StreamflowRate'. If missing, a multivariate time series of all played states is returned; this may be a large amount of data.
            start_time (datetime like): An optional parameter, the start of a period to subset the time series
            end_time (datetime like): An optional parameter, the end of a period to subset the time series

        Returns:
            xr.DataArray: a time series, possibly multivariate.

        """
        return spr.get_recorded(self, var_ids, start_time, end_time)

    def get_all_recorded(self) -> xr.DataArray:
        """Gets all the time series of models variables recorded from"""
        return spr.get_all_recorded(self)

    def get_all_played(self) -> xr.DataArray:
        """Gets all the time series of models variables into which input time sereis is/are played"""
        return spr.get_all_played(self)

    def apply_recording_function(
        self,
        recording_func: Optional["RecordToSignature"],
        var_ids: "VecStr",
        recording_provider,
        data_ids: "VecStr",
    ) -> None:
        """DRAFT Advanced/technical. Record states to a record provider using a callable function. 
        
        Likely not for end users. This is used by methods such as 
        [`EnsembleSimulation.record_ensemble_state`][swift2.classes.EnsembleSimulation.record_ensemble_state].
        
        """
        spr.apply_recording_function(
            self, recording_func, var_ids, recording_provider, data_ids
        )

    def record_singular_state(
        self,
        var_ids: "VecStr" = CATCHMENT_FLOWRATE_VARID,
        recording_provider: Optional["TimeSeriesLibrary"] = None,
        data_ids: Optional["VecStr"] = None,
    ) -> None:
        """DRAFT Advanced/technical. Record states to a record provider. 
        
        Likely not for end users.
        """
        spr.record_singular_state(self, var_ids, recording_provider, data_ids)

    def cookie_cut_dendritic_catchment(
        self, bottom_element_id: str, top_element_ids: "VecStr"
    ):
        """cookie cut a dendritic catchment (without confluences)

        Args:
            bottom_element_id (str): identifier of the most downstream element to keep
            top_element_ids (str): identifier(s) of the most upstream element(s) to keep

        Returns:
            Simulation: a subcatchment simulation, cookie cut from the base simulation. Deep clone of objects.
        """
        return smd.cookie_cut_dendritic_catchment(
            self, bottom_element_id, top_element_ids
        )

    def subset_catchment(self, element_id: str, action: str = "keep_above"):
        """Subsets a catchment, keeping only a portion above or below a node, link or subarea.

        Args:
            element_id (str): id of the element to cut at.
            action (str): how to cut; currently limited to 'keep_above'

        Returns:
            Simulation: a subcatchment simulation, cookie cut from the base simulation. Deep clone of objects.
        """
        return smd.subset_catchment(self, element_id, action)

    def split_to_subcatchments(
        self, split_element_ids: Sequence[str], include_upstream: Sequence[bool] = None
    ) -> OrderedDict[str, "Simulation"]:
        """Split a catchment in subcatchments, given a list of node/link element identifiers

        Args:
            split_element_ids (str): element identifiers such as 'node.n1', 'link.linkId_2'
            include_upstream (bool, optional): indicates whether for each element in split_element_ids it should be including in the upstream portion of the subcatchment. Defaults to None.

        Returns:
            OrderedDict: list of subcatchments resulting from the split

        Examples:
            >>> _, simulation = sdh.create_test_catchment_structure()
            >>> e_ids = ['node.n2', 'node.n4']
            >>> sub_sims = simulation.split_to_subcatchments(e_ids)
            >>> for k in sub_sims:
            >>>     print(k)
            >>>     print(sub_sims[k].get_node_ids())
            >>>     print(sub_sims[k].get_node_names())
            node.n4
            ['n4', 'n3', 'n1']
            ['n4_name', 'n3_name', 'n1_name']
            node.n2
            ['n2', 'n5']
            ['n2_name', 'n5_name']
            remainder
            ['n6']
            ['n6_name']
        """
        return smd.split_to_subcatchments(self, split_element_ids, include_upstream)

    def get_catchment_structure(self) -> Dict[str, Any]:
        """Gets the essential connective structure of a catchment

        Args:
            simulation (Simulation): base catchment simulation

        Returns:
            Dict[str, Any]: A nested dictionary describing the catchment connectivity of subareas, links, and nodes

        Examples:
            >>> _, simulation = sdh.create_test_catchment_structure()
            >>> simulation.get_catchment_structure()
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
        """
        return smd.get_catchment_structure(self)

    def create_multisite_objective(
        self,
        statspec: pd.DataFrame,
        observations: Sequence[TimeSeriesLike],
        weights: Dict[str, float],
    ) -> "ObjectiveEvaluator":
        """
        Creates an objective that combines multiple statistics. Used for joined, "whole of catchment" calibration

        Args:
            statspec (pd.DataFrame): dataframe defining the objectives used. See function [`multi_statistic_definition`][swift2.statistics.multi_statistic_definition] to help build this dataframe.
            observations (Sequence[TimeSeriesLike]): A list of (time series) observations to calculated the statistics. Must be of same length as the number of rows of statspec.
            weights (Dict[str, float]): numeric vector of weights to ponderate each objective.

        Returns:
            ObjectiveEvaluator: an objective evaluator

        Examples:
            >>> _, ms = sdh.create_test_catchment_structure()
            >>> from swift2.utils import mk_full_data_id
            >>> 
            >>> nodeids = ['node.n2', 'node.n4']
            >>> mvids = mk_full_data_id(nodeids, 'OutflowRate')
            >>> 
            >>> sdh.configure_test_simulation(
            ...     ms,
            ...     data_id='MMH',
            ...     simul_start='1990-01-01',
            ...     simul_end='2005-12-31',
            ...     tstep='daily',
            ...     varname_rain='P',
            ...     varname_pet='E',
            ...     varname_data_rain='rain',
            ...     varname_data_pet='evap',
            ... )
            >>> 

            >>> ms.record_state(mvids)
            >>> ms.exec_simulation()
            >>> 
            >>> modFlows = ms.get_recorded()
            >>> 

            >>> w = dict(zip(mvids, [1.0, 2.0]))
            >>> w
            {'node.n2.OutflowRate': 1.0, 'node.n4.OutflowRate': 2.0}
            >>> span = ms.get_simulation_span()
            >>> 

            >>> from swift2.utils import rep
            >>> statspec = sst.multi_statistic_definition(mvids, rep('nse', 2), mvids, mvids, rep(span['start'], 2), rep(span['end'], 2) )
            >>> 
            >>> statspec
                        ModelVarId StatisticId          ObjectiveId        ObjectiveName      Start        End
            0  node.n2.OutflowRate         nse  node.n2.OutflowRate  node.n2.OutflowRate 1990-01-01 2005-12-31
            1  node.n4.OutflowRate         nse  node.n4.OutflowRate  node.n4.OutflowRate 1990-01-01 2005-12-31
            >>> 
            >>> # Create synthetic observations
            >>> observations = [
            ...     modFlows.sel(variable_identifiers=mvids[0]) * 0.33,
            ...     modFlows.sel(variable_identifiers=mvids[1]) * 0.77
            ... ]
            >>> 
            >>> obj = ms.create_multisite_objective(statspec, observations, w)
            >>> 

            >>> dummy = sp.create_parameteriser()
            >>> obj.get_scores(dummy)
            {'node.n2.OutflowRate': -4.152338377267432, 'node.n4.OutflowRate': 0.8884789439301954}
            >>> 

            >>> obj.get_score(dummy)
            {'scores': {'MultisiteObjectives': 0.7917934964690136}, 'sysconfig': Empty DataFrame
            Columns: [Name, Value, Min, Max]
            Index: []}
            >>> 
        """
        return ssf.create_multisite_objective(self, statspec, observations, weights)

    def create_objective(
        self,
        state_name: str,
        observation: TimeSeriesLike,
        statistic: str,
        start_date: ConvertibleToTimestamp,
        end_date: ConvertibleToTimestamp,
    ) -> "ObjectiveEvaluator":
        """
        Creates an objective calculator

        Args:
            state_name (str): The name identifying the model state variable to calibrate against the observation
            observation (TimeSeriesLike): an xts
            statistic (str): statistic identifier, e.g. "NSE"
            start_date (ConvertibleToTimestamp): start date of the period to calculate statistics on
            end_date (ConvertibleToTimestamp): end date of the period to calculate statistics on
        
        Returns:
            ObjectiveEvaluator: single objective evaluator
        """
        return ssf.create_objective(
            self, state_name, observation, statistic, start_date, end_date
        )

    def muskingum_param_constraints(
        self,
        inner_parameters: "HypercubeParameteriser",
        delta_t: float = 1.0,
        param_name_k: str = "K",
        param_name_x: str = "X",
    ) -> "ConstraintParameteriser":
        """Create a parameteriser with Muskingum-type constraints. 
        
        Given an existing parameteriser, create a wrapper that adds constraints on two of its parameters.

        Args:
            inner_parameters (HypercubeParameteriser): A SWIFT parameteriser object that contains two Muskingum-type attenuation  and delay parameters.
            delta_t (int, optional): the simulation time step in HOURS. Defaults to 1.
            param_name_k (str, optional): the variable identifier to use for the delay parameter of the Muskingum routing. Defaults to "K".
            param_name_x (str, optional): the variable identifier to use for the attenuation parameter of the Muskingum routing. Defaults to "X".

        Returns:
            ConstraintParameteriser: A parameteriser with constraints on the feasibility of the attenuation / delay parameters

        Examples:
           >>> todo()
        """
        return sp.create_muskingum_param_constraints(
            inner_parameters, delta_t, param_name_k, param_name_x, self
        )

    def prepare_erris_forecasting(
        self,
        observation: TimeSeriesLike,
        error_model_element_id: str,
        warmup_start: ConvertibleToTimestamp,
        warmup_end: ConvertibleToTimestamp,
    ) -> 'EnsembleSimulation':
        """Create an ensemble simulation for forecasting with ERRIS

        Args:
            observation (TimeSeriesLike): Time series of observations to correct prediction against
            error_model_element_id (str): model element identifier where to set up an ERRIS correction model
            warmup_start (ConvertibleToTimestamp): start time stamp for the warmup period
            warmup_end (ConvertibleToTimestamp): end time stamp for the warmup period

        Returns:
            EnsembleSimulation: Ensemble simulation (ensemble simulation runner)
        """
        from swift2.internal import to_interop_univariate_series

        values, ts_geom = to_interop_univariate_series(
            observation, warmup_start, warmup_end
        )
        return swg.PrepareERRISForecasting_py(
            self, values, ts_geom, error_model_element_id, warmup_start, warmup_end
        )

    def prepare_dual_pass_forecasting(
        self,
        observation: TimeSeriesLike,
        error_model_element_id: str,
        warmup_start: ConvertibleToTimestamp,
        warmup_end: ConvertibleToTimestamp,
        required_windows_percentage: float,
    ) -> 'EnsembleSimulation':
        """Create an ensemble simulation for forecasting with the Dual Pass error correction method 

        Args:
            observation (TimeSeriesLike): Time series of observations to correct prediction against
            error_model_element_id (str): model element identifier where to set up an ERRIS correction model
            warmup_start (ConvertibleToTimestamp): start time stamp for the warmup period
            warmup_end (ConvertibleToTimestamp): end time stamp for the warmup period
            required_windows_percentage (float): required_windows_percentage

        Returns:
            EnsembleSimulation: Ensemble simulation (ensemble simulation runner)
        """    
        from swift2.internal import to_interop_univariate_series

        values, ts_geom = to_interop_univariate_series(
            observation, warmup_start, warmup_end
        )
        return swg.PrepareDualPassForecasting_py(
            self,
            values,
            ts_geom,
            error_model_element_id,
            warmup_start,
            warmup_end,
            required_windows_percentage,
        )


class Parameteriser(DeletableCffiNativeHandle):
    """Wrapper around a native parameteriser.

    Note:
        This is a parent class for more common types such as 
        [swift2.classes.HypercubeParameteriser][]

    """
    def __init__(
        self,
        handle: CffiData,
        release_native: Callable[[CffiData], None],
        type_id: Optional[str] = None,
        prior_ref_count: int = 0,
    ):
        super(Parameteriser, self).__init__(
            handle, release_native, type_id, prior_ref_count
        )

    def score_for_objective(self, objective: "ObjectiveEvaluator") -> Dict[str, Any]:
        """Computes the value of an objective for this given set of parameters"""
        return sp.evaluate_score_for_parameters(objective, self)

    # def _sapply_parameter_set(self, variable_name, value, api_func):
    #     sp._sapply_parameter_set(self, variable_name, value, api_func)

    def subcatchment_parameteriser(self, subcatchment):
        """Create a parameteriser that gets applied to a subset of a whole catchment

        Args:
            subcatchment (Simulation): the subcatchment, subset of a whole catchment, identifying which elements (subareas, nodes, links) will be parameterised by the new parameteriser. Other catchment elements are untouched.

        Returns:
            HypercubeParameteriser: New parameteriser whose application is limited to the subcatchment.

        Examples:
            >>> sub_cats = simulation.split_to_subcatchments(["node.node_7", "node.node_10"])
            >>> sc = sub_cats["node.node_7"]
            >>> p = sp.create_parameteriser('generic subarea')
            >>> p.add_parameter_to_hypercube("x1", 32, 1, 6e3)
            >>> sp = p.subcatchment_parameteriser(sc)
            >>> sp.apply_sys_config(simulation)

        """
        return sp.subcatchment_parameteriser(self, subcatchment)

    def apply_sys_config(self, simulation:"Simulation"):
        """Apply a model configuration to a simulation

        Args:
            simulation (Simulation): simulation
        """
        sp.apply_sys_config(self, simulation)

    def supports_thread_safe_cloning(self) -> bool:
        """Is this parameteriser clonable as a deep copy, safe for multi-threading?"""
        return swg.SupportsThreadSafeCloning_py(self)


class HypercubeParameteriser(Parameteriser):
    def __init__(
        self,
        handle: CffiData,
        release_native: Callable[[CffiData], None],
        type_id: Optional[str] = None,
        prior_ref_count: int = 0,
    ):
        super(HypercubeParameteriser, self).__init__(
            handle, release_native, type_id, prior_ref_count
        )

    def __str__(self):
        """string representation"""
        return str(self.as_dataframe())

    def __repr__(self):
        """representation"""
        return repr(self.as_dataframe())

    def as_dataframe(self) -> pd.DataFrame:
        """Convert this hypercube parameteriser to a pandas data frame representation

        Returns:
            pd.DataFrame: pandas data frame
        """
        return sp.parameteriser_as_dataframe(self)

    def num_free_parameters(self) -> int:
        """Number of free parameters in this hypercube parameteriser

        Returns:
            int: Number of free parameters
        """
        return sp.num_free_parameters(self)

    def set_parameter_value(self, variable_name: "VecStr", value: "VecScalars"):
        """Sets the value(s) of one or more parameter(s)

        Args:
            variable_name (VecStr): one or more parameter name(s)
            value (VecScalars): one or more parameter value(s)
        """
        sp.set_parameter_value(self, variable_name, value)

    def set_max_parameter_value(self, variable_name: "VecStr", value: "VecScalars"):
        """Sets the value(s) of the upper bound of one or more parameter(s)

        Args:
            variable_name (VecStr): one or more parameter name(s)
            value (VecScalars): one or more parameter value(s)
        """
        sp.set_max_parameter_value(self, variable_name, value)

    def set_min_parameter_value(self, variable_name: "VecStr", value: "VecScalars"):
        """Sets the value(s) of the lower bound of one or more parameter(s)

        Args:
            variable_name (VecStr): one or more parameter name(s)
            value (VecScalars): one or more parameter value(s)
        """
        sp.set_min_parameter_value(self, variable_name, value)

    def set_parameter_definition(
        self, variable_name: str, min: float, max: float, value: float
    ):
        """Sets the feasible range and value for a parameter

        Args:
            variable_name (str): parameter name
            min (float): min
            max (float): max
            value (float): value
        """    
        swg.SetParameterDefinition_py(self, variable_name, min, max, value)

    def create_parameter_sampler(self, seed: int = 0, type: str = "urs") -> "CandidateFactorySeed":
        """Creates a sampler for this parameteriser

        Args:
            seed (int, optional): a seed for the sampler. Defaults to 0.
            type (str, optional): the type of sampler. Defaults to "urs". Only option supported as of 2023-01.

        Returns:
            CandidateFactorySeed: a sampler, aka candidate factory
        """        
        return sp.create_parameter_sampler(seed, self, type)

    def make_state_init_parameteriser(self) -> "StateInitParameteriser":
        """Create a parameteriser used for model state initialisation
        
        This allows to define tied parameters where, for instance, pval = a * modelStateVal. 
        A more concrete use case is to define an initial soil moisture store 'S0',
        as a fraction of the model store capacity 'Smax'. 
        The model state to initialise is 'S'

        Note:
            See also [swift2.classes.ScalingParameteriser][] for typical joint usage.

        Returns:
            StateInitParameteriser: state initialisation parameteriser
        
        Examples:
            >>> todo()
        """
        return sp.make_state_init_parameteriser(self)

    def filtered_parameters(self) -> "FilteringParameteriser":
        """Wrap a parameteriser in a filter that can hide some parameters"""
        return sp.filtered_parameters(self)

    def hide_parameters(self, patterns, regex=False, starts_with=False, strict=False):
        """Hide some parameters (from the outside e.g. optimisers) in a filter parameteriser

        Args:
            patterns ([type]):  character, one or more pattern to match and hide matching parameters. Match according to other parameters.
            regex (bool, optional): logical, defaults False, should the patterns be used as regular expressions.. Defaults to False.
            starts_with (bool, optional): logical, defaults False. Ignored if regex is True. Should the patterns be used as starting strings in the parameter names.. Defaults to False.
            strict (bool, optional): logical, default False. Used only if regex and starts_with are False. If True, raises an error if one of the "patterns" has no exact match in the parameters.. Defaults to False.
        """
        sp.hide_parameters(self, patterns, regex, starts_with, strict)

    def show_parameters(self, patterns, regex=False, starts_with=False):
        """Show some parameters (from the outside e.g. optimisers) in a filter parameteriser

        Args:
            patterns ([type]):  character, one or more pattern to match and show matching parameters. Match according to other parameters
            regex (bool, optional): should the patterns be used as regular expressions. Defaults to False.
            starts_with (bool, optional): should the patterns be used as starting strings in the parameter names. Defaults to False.
        """
        sp.show_parameters(self, patterns, regex, starts_with)

    def wrap_transform(self) -> "TransformParameteriser":
        """Create a parameteriser for which parameter transformations can be defined.

        This allows to define e.g. a virtual parameter log_X instead of calibrating on the parameter X.

        Returns:
            TransformParameteriser: A new parameteriser (TransformParameteriser) which has methods to define parameter transforms
        """
        return sp.wrap_transform(self)

    def backtransform(self) -> "HypercubeParameteriser":
        """Get the parameteriser values in the untransformed space

        Get the parameteriser values in the untransformed space, i.e. remove any 
        transform added via [`HypercubeParameteriser.wrap_transform`][HypercubeParameteriser.wrap_transform].
        This allows to transform back e.g. from a virtual parameter log_X
        to the underlying model (or even virtual/meta) parameter X.

        Returns:
            HypercubeParameteriser: The parameters definitions without the transforms (if there are any)

        Examples:
            >>> ref_area = 250
            >>> time_span = 3600
            >>> ptrans = sdh.define_gr4j_scaled_parameter(ref_area, time_span)
            >>> ptrans
                Name     Value       Min       Max
            0    log_x4  0.305422  0.000000  2.380211
            1    log_x1  0.506690  0.000000  3.778151
            2    log_x3  0.315425  0.000000  3.000000
            3  asinh_x2  2.637752 -3.989327  3.989327
            >>> ptrans.backtransform()
            Name    Value   Min     Max
            0   x2  6.95511 -27.0    27.0
            1   x3  2.06740   1.0  1000.0
            2   x4  2.02033   1.0   240.0
            3   x1  3.21137   1.0  6000.0
            >>> 
        """
        return sp.backtransform(self)

    @staticmethod
    def from_dataframe(
        type="Generic subareas", definition: Optional[pd.DataFrame] = None
    ) -> "HypercubeParameteriser":
        """Create a parameteriser

        Args:
            type (str, optional): A string identifying the type of parameteriser to use. Recognised types are (case insensitive) 'log-likelihood', 'generic', 'subareas', 'links', 'nodes' and 'muskingum'. Defaults to "Generic subareas".
            specs (pd.DataFrame, optional): An optional data frame description of the parameter set, with at least columns Name, Min, Max, Value. Defaults to None.

        Returns:
            HypercubeParameteriser: new parameteriser

        Examples:
            >>> d = pd.DataFrame(
            ...     dict(
            ...         Name=c("alpha", "inverse_velocity"),
            ...         Value=c(1, 1),
            ...         Min=c(1e-3, 1e-3),
            ...         Max=c(1e2, 1e2),
            ...     )
            ... )
            >>> p = HypercubeParameteriser.from_dataframe("Generic links", d)
            >>> p
        """
        return sp.create_parameteriser(type, specs=definition)

    def add_to_hypercube(self, specs: pd.DataFrame):
        """Add entries to a hypercube. Must be a type of object that is expandable, otherwise may raise an exception.

        Args:
            specs (pd.DataFrame): An optional data frame description of the parameter set, with at least columns Name, Min, Max, Value.
        """
        sp.add_to_hypercube(self, specs)

    def add_parameter_to_hypercube(
        self, name: str, value: float, min: float, max: float
    ):
        """Add a parameter to a hypercube. Must be a type of object that is expandable, otherwise may raise an exception"""
        specs = parameter_df(name, value, min, max)
        sp.add_to_hypercube(self, specs)

    def set_hypercube(self, specs: pd.DataFrame):
        """Set the properties of a hypercube parameteriser

        Args:
            specs (pd.DataFrame): An optional data frame description of the parameter set, with at least columns Name, Min, Max, Value.
        """
        sp.set_hypercube(self, specs)

    def clone(self) -> "HypercubeParameteriser":
        return swg.CloneHypercubeParameterizer_py(self)


class CompositeParameteriser(HypercubeParameteriser):
    """A parameteriser defined as the concatenation of several parameterisers"""
    def __init__(
        self,
        handle: CffiData,
        release_native: Callable[[CffiData], None],
        type_id: Optional[str] = None,
        prior_ref_count: int = 0,
    ):
        super(CompositeParameteriser, self).__init__(
            handle, release_native, type_id, prior_ref_count
        )

    @staticmethod
    def empty_composite() -> "CompositeParameteriser":
        """Creates an empty parameteriser to be populated with other parameterisers

        Returns:
            CompositeParameteriser: composite parameteriser
        """        
        return swg.CreateCompositeParameterizer_py()

    @staticmethod
    def concatenate(
        *args: Sequence["HypercubeParameteriser"], strategy: str = ""
    ) -> "CompositeParameteriser":
        """Concatenates some hypercubes to a single parameteriser

        Args:
            strategy (str, optional): The strategy to contatenate. Defaults to "", equivalent to "composite", the only available. May have other options in the future.

        Returns:
            CompositeParameteriser: A concatenated parameteriser
        """
        return sp.concatenate_parameterisers(*args, strategy=strategy)

    def append(self, p: "HypercubeParameteriser"):
        """Append a parameteriser to this composite parameteriser

        Args:
            p (HypercubeParameteriser): hypercube to append to this
        """        
        swg.AddToCompositeParameterizer_py(self, p)


class ObjectiveEvaluator(DeletableCffiNativeHandle):
    """Objective Evaluator"""
    def __init__(
        self,
        handle: CffiData,
        release_native: Callable[[CffiData], None],
        type_id: Optional[str] = None,
        prior_ref_count: int = 0,
    ):
        super(ObjectiveEvaluator, self).__init__(
            handle, release_native, type_id, prior_ref_count
        )

    def create_sce_optim_swift(
        self,
        termination_criterion: Optional["SceTerminationCondition"] = None,
        sce_params: Optional[Dict[str, float]] = None,
        population_initialiser: Optional[Union["CandidateFactorySeed", "HypercubeParameteriser"]] = None,
    ) -> "Optimiser":
        """Creates a shuffled complex optimiser for this objective

        Args:
            termination_criterion (Optional[&quot;SceTerminationCondition&quot;], optional): A termination criterion for the optimiser. Defaults to None, in which case an arbitrary "relative standard deviation" is set up.
            sce_params (Optional[Dict[str, float]], optional): hyperparameters controlling SCE. Defaults to None, in which case [`swift2.parameteriser.get_default_sce_parameters`][swift2.parameteriser.get_default_sce_parameters] is used.
            population_initialiser (Optional[&quot;CandidateFactorySeed&quot;], optional): A candidate factory to initialise the population of parameters the optimiser starts from, or a hypercube. In the latter case, uniform random sampling is used. Defaults to None, which leads to an error (for legacy reasons). 

        Returns:
            Optimiser: SCE optimiser
        """    
        return sp.create_sce_optim_swift(
            self, termination_criterion, sce_params, population_initialiser
        )

    # CreateOptimizerWila?

    def get_score(self, p_set: "HypercubeParameteriser") -> Dict[str,Any]:
        """Evaluate this objective for a given parameterisation

        Args:
            p_set (HypercubeParameteriser): parameteriser

        Returns:
            Dict[str,Any]: score(s), and a data frame representation of the input parameters.
        """
        return ssf.get_score(self, p_set)

    def get_scores(self, p_set: "HypercubeParameteriser") -> Dict[str,float]:
        """Evaluate this objective for a given parameterisation

        Args:
            p_set (HypercubeParameteriser): parameteriser

        Returns:
            Dict[str,float]: score(s)
        """
        return swg.EvaluateScoresForParametersWila_py(self, p_set)

    # EvaluateScoreForParametersWilaInitState?

    @staticmethod
    def create_composite_objective(
        objectives: Sequence["ObjectiveEvaluator"],
        weights: Sequence[float],
        names: Sequence[str],
    ) -> "ObjectiveEvaluator":
        """Creates a composite objective, weighted average of several objectives

        Args:
            objectives (Sequence[&quot;ObjectiveEvaluator&quot;]): objective evaluators, for instance measures at several points in the catchment
            weights (Sequence[float]): Weights to use to average the objectives. This may not add to one, but must not sum to zero
            names (Sequence[str]): Names of individual objectives

        Returns:
            ObjectiveEvaluator: An objective evaluator that can be use by an optimiser
        """    
        return ssf.create_composite_objective(objectives, weights, names)


class EnsembleSimulation(DeletableCffiNativeHandle):
    """A simulation designed to facilitate model runs over ensemble of inputs"""
    def __init__(
        self,
        handle: CffiData,
        release_native: Callable[[CffiData], None],
        type_id: Optional[str] = None,
        prior_ref_count: int = 0,
    ):
        super(EnsembleSimulation, self).__init__(
            handle, release_native, type_id, prior_ref_count
        )

    def setup(self, forecast_start: datetime, ensemble_size: int, forecast_horizon_length: int) -> None:
        """Sets up this ensemble simulation

        Args:
            forecast_start (datetime): Start date for the simulation
            ensemble_size (int): size of the ensemble
            forecast_horizon_length (int): length of the simulation in numbers of time steps.
        """        
        swg.SetupEnsembleModelRunner_py(
            self, forecast_start, ensemble_size, forecast_horizon_length
        )

    def record(self, variable_id:str) -> None:
        """Records a state variable of the simualtion

        Args:
            variable_id (str): state variable identifier
        """        
        swg.RecordEnsembleModelRunner_py(self, variable_id)

    def get_simulation_span(self) -> Dict[str, Any]:
        """Gets the span of the simulation: start, end, time step

        Returns:
            Dict[str, Any]: simulation span
        """        
        return swc.get_simulation_span_pkg(self)

    def record_ensemble_state(
        self,
        var_ids: "VecStr" = CATCHMENT_FLOWRATE_VARID,
        recording_provider: Optional["TimeSeriesLibrary"] = None,
        data_ids: Optional["VecStr"] = None,
    ) -> None:
        """Records one or more state values from an ensemble simulation

        Args:
            var_ids (VecStr, optional): Model variable identierfier(s). Defaults to CATCHMENT_FLOWRATE_VARID.
            recording_provider (Optional[TimeSeriesLibrary], optional): An optional time series library to record to. Defaults to None.
            data_ids (Optional[VecStr], optional): Data identifier(s). Defaults to None.
        """    
        spr.record_ensemble_state(self, var_ids, recording_provider, data_ids)


class FunctionsParameteriser(HypercubeParameteriser):
    def __init__(
        self,
        handle: CffiData,
        release_native: Callable[[CffiData], None],
        type_id: Optional[str] = None,
        prior_ref_count: int = 0,
    ):
        super(FunctionsParameteriser, self).__init__(
            handle, release_native, type_id, prior_ref_count
        )


class FilteringParameteriser(HypercubeParameteriser):
    def __init__(
        self,
        handle: CffiData,
        release_native: Callable[[CffiData], None],
        type_id: Optional[str] = None,
        prior_ref_count: int = 0,
    ):
        super(FilteringParameteriser, self).__init__(
            handle, release_native, type_id, prior_ref_count
        )


class StateInitParameteriser(HypercubeParameteriser):
    def __init__(
        self,
        handle: CffiData,
        release_native: Callable[[CffiData], None],
        type_id: Optional[str] = None,
        prior_ref_count: int = 0,
    ):
        super(StateInitParameteriser, self).__init__(
            handle, release_native, type_id, prior_ref_count
        )


class TransformParameteriser(HypercubeParameteriser):
    def __init__(
        self,
        handle: CffiData,
        release_native: Callable[[CffiData], None],
        type_id: Optional[str] = None,
        prior_ref_count: int = 0,
    ):
        super(TransformParameteriser, self).__init__(
            handle, release_native, type_id, prior_ref_count
        )

    def add_transform(
        self,
        param_name: str,
        inner_param_name: str,
        transform_id: str,
        a: float = 1.0,
        b: float = 0.0,
    ):
        """Create a parameteriser for which parameter transformations can be defined

            This allows to define e.g. a virtual parameter log_X instead of calibrating on the parameter X.

        Args:
            param_name (str): the name of the meta-parameter. Note that it can be the same value as inner_param_name, but this is NOT recommended.
            inner_param_name (str): the name of the parameter being transformed
            transform_id (str): identifier for a known bijective univariate function
            a (float, optional): parameter in Y = F(ax+b). Defaults to 1.0.
            b (float, optional): parameter in Y = F(ax+b). Defaults to 0.0.
        """
        sp.add_transform(self, param_name, inner_param_name, transform_id, a, b)


class ConstraintParameteriser(HypercubeParameteriser):
    def __init__(
        self,
        handle: CffiData,
        release_native: Callable[[CffiData], None],
        type_id: Optional[str] = None,
        prior_ref_count: int = 0,
    ):
        super(ConstraintParameteriser, self).__init__(
            handle, release_native, type_id, prior_ref_count
        )


class ScalingParameteriser(TransformParameteriser):
    def __init__(
        self,
        handle: CffiData,
        release_native: Callable[[CffiData], None],
        type_id: Optional[str] = None,
        prior_ref_count: int = 0,
    ):
        super(ScalingParameteriser, self).__init__(
            handle, release_native, type_id, prior_ref_count
        )

    @staticmethod
    def linear_parameteriser_from(
        data_frame: pd.DataFrame, selector_type: str = "subareas"
    ):
        """Create a scaled linear parameteriser, tying by a linear transformation a (resp several) model state to a (resp several) parameter values
        This allows to define tied parameters where pval = a * modelStateVal + intercept. The intent in particular is to define virtual model parameters such as initial store value as a fraction of the maximum storage capacity.

        Args:
            data_frame (pd.DataFrame): data frame with columns "param_name", "state_name", "scaling_var_name", "min_value", "max_value", "value", "intercept",
            selector_type (str, optional): [description]. Defaults to "subareas".

        Returns:
            ScalingParameteriser: ScalingParameteriser
        """
        return sp.linear_parameteriser_from(data_frame, selector_type)

    @staticmethod
    def linear_parameteriser(
        param_name: "VecStr",
        state_name: "VecStr",
        scaling_var_name: "VecStr",
        min_p_val: "VecNum",
        max_p_val: "VecNum",
        value: "VecNum",
        selector_type: str = "subareas",
        intercept: "VecNum" = 0.0,
    ):
        """Create a scaled linear parameteriser, tying by a linear transformation a (resp several) model state to a (resp several) parameter values

        This allows to define tied parameters where pval = a * modelStateVal + intercept.
        The intent in particular is to define virtual model parameters such as initial store value as a fraction of the maximum storage capacity.

        Args:

            param_name (VecStr): the name of the meta-parameter. Note that it can be the same value as inner_param_name without interference, though this may be confusing a choice.
            state_name (VecStr): the name of the model state to modify, based on the value of the meta-parameter and the state found in 'scalingVarName'
            scaling_var_name (VecStr): the name of the parameter for each subarea model, to which to apply the area scaled value.
            min_p_val (VecNum): minimum value allowed for the meta-parameter
            max_p_val (VecNum): minimum value allowed for the meta-parameter
            value (VecNum): value for the meta parameter.
            selector_type (str, optional): an identifier to define to which catchment element(s) the parameteriser will be applied. Defaults to "subareas".
            intercept (VecNum, optional): [description]. Defaults to 0.0.

        Returns:
            ScalingParameteriser: new ScalingParameteriser
        """
        return sp.linear_parameteriser(
            param_name,
            state_name,
            scaling_var_name,
            min_p_val,
            max_p_val,
            value,
            selector_type,
            intercept,
        )

    def add_linear_scaled_parameter(
        self,
        param_name: str,
        state_name: str,
        scaling_var_name: str,
        min_p_val: float,
        max_p_val: float,
        value: float,
        intercept: float = 0.0,
    ):
        swg.AddLinearScalingParameterizer_py(
            self,
            param_name,
            state_name,
            scaling_var_name,
            intercept,
            min_p_val,
            max_p_val,
            value,
        )


class Optimiser(DeletableCffiNativeHandle):
    def __init__(
        self,
        handle: CffiData,
        release_native: Callable[[CffiData], None],
        type_id: Optional[str] = None,
        prior_ref_count: int = 0,
    ):
        super(Optimiser, self).__init__(
            handle, release_native, type_id, prior_ref_count
        )

    def set_calibration_logger(self, type:str=""):
        return sp.set_calibration_logger(self, type)

    def execute_optimisation(self):
        return sp.execute_optimisation(self)

    def extract_optimisation_log(self, fitness_name:str="log.likelihood") -> Dict[str,Any]:
        return sp.extract_optimisation_log(self, fitness_name)

    def set_maximum_threads(self, n_threads: int = -1):
        swg.SetMaxThreadsOptimizerWila_py(self, n_threads)

    @staticmethod
    def set_default_maximum_threads(n_threads: int):
        swg.SetDefaultMaxThreadsWila_py(n_threads)

    @staticmethod
    def get_default_maximum_threads() -> int:
        return swg.GetDefaultMaxThreadsWila_py()


class SceTerminationCondition(DeletableCffiNativeHandle):
    def __init__(
        self,
        handle: CffiData,
        release_native: Callable[[CffiData], None],
        type_id: Optional[str] = None,
        prior_ref_count: int = 0,
    ):
        super(SceTerminationCondition, self).__init__(
            handle, release_native, type_id, prior_ref_count
        )


class CandidateFactorySeed(DeletableCffiNativeHandle):
    def __init__(
        self,
        handle: CffiData,
        release_native: Callable[[CffiData], None],
        type_id: Optional[str] = None,
        prior_ref_count: int = 0,
    ):
        super(CandidateFactorySeed, self).__init__(
            handle, release_native, type_id, prior_ref_count
        )


class ObjectiveScores(DeletableCffiNativeHandle):
    def __init__(
        self,
        handle: CffiData,
        release_native: Callable[[CffiData], None],
        type_id: Optional[str] = None,
        prior_ref_count: int = 0,
    ):
        super(ObjectiveScores, self).__init__(
            handle, release_native, type_id, prior_ref_count
        )

    def as_py_structure(self):
        return sp.as_py_structure(self)

    def apply_sys_config(self, simulation):
        sp.apply_sys_config(self, simulation)

    @property
    def parameteriser(self) -> "HypercubeParameteriser":
        return sp.parameteriser_for_score(self)

    @property
    def scores(self) -> Dict[str, float]:
        return swc.fitnesses_as_rpy_dict(self)

    @property
    def num_scores(self) -> int:
        return swg.GetNumScoresWila_py(self)


class VectorObjectiveScores(DeletableCffiNativeHandle):
    def __init__(
        self,
        handle: CffiData,
        release_native: Callable[[CffiData], None],
        type_id: Optional[str] = None,
        prior_ref_count: int = 0,
    ):
        super(VectorObjectiveScores, self).__init__(
            handle, release_native, type_id, prior_ref_count
        )

    def get_score_at_index(self, index):
        return sp.get_score_at_index(self, index)

    def get_parameters_at_index(self, index):
        return sp.get_score_at_index(self, index).parameteriser

    def get_best_score(self, score_name="NSE", convert_to_py=False):
        return sp.get_best_score(self, score_name, convert_to_py)

    def sort_by_score(self, score_name="NSE"):
        return sp.sort_by_score(self, score_name)

    def as_dataframe(self):
        return sp.scores_as_dataframe(self)

    @property
    def size(self) -> int:
        return swg.GetLengthSetOfScores_py(self)


# TODO consider whether inheriting from Optimiser is sound. Not reflecting C++, but may make sense in python.
class ErrisStagedCalibration(DeletableCffiNativeHandle):
    def __init__(
        self,
        handle: CffiData,
        release_native: Callable[[CffiData], None],
        type_id: Optional[str] = None,
        prior_ref_count: int = 0,
    ):
        super(ErrisStagedCalibration, self).__init__(
            handle, release_native, type_id, prior_ref_count
        )

    def extract_optimisation_log(self, fitness_name="log.likelihood"):
        return sp.extract_optimisation_log(self, fitness_name)


class MaerrisStagedCalibration(DeletableCffiNativeHandle):
    def __init__(
        self,
        handle: CffiData,
        release_native: Callable[[CffiData], None],
        type_id: Optional[str] = None,
        prior_ref_count: int = 0,
    ):
        super(MaerrisStagedCalibration, self).__init__(
            handle, release_native, type_id, prior_ref_count
        )

    def extract_optimisation_log(self, fitness_name="log.likelihood"):
        return sp.extract_optimisation_log(self, fitness_name)


class StateInitialiser(DeletableCffiNativeHandle):
    def __init__(
        self,
        handle: CffiData,
        release_native: Callable[[CffiData], None],
        type_id: Optional[str] = None,
        prior_ref_count: int = 0,
    ):
        super(StateInitialiser, self).__init__(
            handle, release_native, type_id, prior_ref_count
        )

    def clone(self) -> "StateInitialiser":
        return swg.CloneStateInitializer_py(self)

    def is_dictionary_like(self) -> bool:
        return swg.IsDictionaryStateInitializer_py(self)

    def __getitem__(self, key):
        return swg.GetValueStateInitializer_py(self, key)

    def __setitem__(self, key, value):
        return swg.SetValueStateInitializer_py(self, key, value)

    # def clear(self):
    #     return self.__dict__.clear()

    # def copy(self):
    #     return self.__dict__.copy()

    # def has_key(self, k):
    #     return k in self.__dict__

    # def update(self, *args, **kwargs):
    #     return self.__dict__.update(*args, **kwargs)

    # def keys(self):
    #     return self.__dict__.keys()

    # def values(self):
    #     return self.__dict__.values()

    # def items(self):
    #     return self.__dict__.items()

    # def pop(self, *args):
    #     return self.__dict__.pop(*args)

    # def __cmp__(self, dict_):
    #     return self.__cmp__(self.__dict__, dict_)

    # def __contains__(self, item):
    #     return item in self.__dict__

    # def __iter__(self):
    #     return iter(self.__dict__)

    # def __unicode__(self):
    #     return unicode(repr(self.__dict__))

    # def __delitem__(self, key):
    #     raise NotImplementedError()

    # def __contains__(self, key):
    #     raise NotImplementedError()

    # def __len__(self):
    #     raise NotImplementedError()
    #     return len(self.__dict__)

    # def __repr__(self):
    #     raise NotImplementedError()
    #     return repr(self.__dict__)


class MemoryStates(DeletableCffiNativeHandle):
    def __init__(
        self,
        handle: CffiData,
        release_native: Callable[[CffiData], None],
        type_id: Optional[str] = None,
        prior_ref_count: int = 0,
    ):
        super(MemoryStates, self).__init__(
            handle, release_native, type_id, prior_ref_count
        )


class EnsembleForecastSimulation(DeletableCffiNativeHandle, SimulationMixin):
    def __init__(
        self,
        handle: CffiData,
        release_native: Callable[[CffiData], None],
        type_id: Optional[str] = None,
        prior_ref_count: int = 0,
    ):
        super(EnsembleForecastSimulation, self).__init__(
            handle, release_native, type_id, prior_ref_count
        )

    def get_simulation_span(self):
        return swc.get_simulation_span_pkg(self)

    def get_recorded_ensemble_forecast(
        self,
        var_id: str,
        start_time: ConvertibleToTimestamp = None,
        end_time: ConvertibleToTimestamp = None,
    ) -> uc.EnsembleForecastTimeSeries:
        return spr.get_recorded_ensemble_forecast(self, var_id, start_time, end_time)

    def record_ensemble_forecast_state(
        self,
        var_ids: "VecStr" = CATCHMENT_FLOWRATE_VARID,
        recording_provider: Optional["TimeSeriesLibrary"] = None,
        data_ids: Optional["VecStr"] = None,
    ) -> None:
        spr.record_ensemble_forecast_state(self, var_ids, recording_provider, data_ids)

    # def PlayDatasetSingleInput(self, dataLibrary, identifiers, dataId, size): pass
    # def PlayDatasetEnsembleForecastInput(self, dataLibrary, identifiers, dataId, size): pass
    # def ExecuteEnsembleForecastSimulation(self): pass
    # def GetEnsembleForecastSingleRecorded(self, variableIdentifier, leadTimeIndex, ensembleIndex, values): pass
    # def GetEnsembleForecastEnsembleRecorded(self, variableIdentifier, leadTimeIndex, values): pass
    # def GetEnsembleForecastLeadLength(self): pass
    # def GetEnsembleForecastEnsembleSize(self): pass
    # def PlayEnsembleForecastTimeSeries(self, series, variableIdentifier): pass
    # def RecordEnsembleForecastTimeSeries(self, variableIdentifier): pass
    # def GetRecordedEnsembleForecastTimeSeries(self, variableIdentifier): pass
    # def RecordEnsembleForecastToRecorder(self, variableIdentifiers, dataLibrary, dataIdentifiers, size): pass


_api_type_wrapper = {
    "MODEL_SIMULATION_PTR": Simulation,
    "ENSEMBLE_SIMULATION_PTR": EnsembleSimulation,
    "HYPERCUBE_PTR": HypercubeParameteriser,
    "COMPOSITE_PARAMETERIZER_PTR": CompositeParameteriser,
    "FUNCTIONS_PARAMETERIZER_PTR": FunctionsParameteriser,
    "FILTERING_PARAMETERIZER_PTR": FilteringParameteriser,
    "OBJECTIVE_EVALUATOR_WILA_PTR": ObjectiveEvaluator,
    "OBJECTIVE_EVALUATOR_PTR": None,
    "STATE_INIT_PARAMETERIZER_PTR": StateInitParameteriser,
    "TRANSFORM_PARAMETERIZER_PTR": TransformParameteriser,
    "CONSTRAINT_PARAMETERIZER_PTR": ConstraintParameteriser,
    "SCALING_PARAMETERIZER_PTR": ScalingParameteriser,
    "SUBAREAS_SCALING_PARAMETERIZER_PTR": None,
    "OPTIMIZER_PTR": Optimiser,
    "SCE_TERMINATION_CONDITION_WILA_PTR": SceTerminationCondition,
    "CANDIDATE_FACTORY_SEED_WILA_PTR": CandidateFactorySeed,
    "OBJECTIVE_SCORES_WILA_PTR": ObjectiveScores,
    "VEC_OBJECTIVE_SCORES_PTR": VectorObjectiveScores,
    "ERRIS_STAGED_CALIBRATION_PTR": ErrisStagedCalibration,
    "MAERRIS_STAGED_CALIBRATION_PTR": MaerrisStagedCalibration,
    "STATE_INITIALIZER_PTR": StateInitialiser,
    "MEMORY_STATES_PTR": MemoryStates,
    "ENSEMBLE_FORECAST_SIMULATION_PTR": EnsembleForecastSimulation,
    "ENSEMBLE_FORECAST_TIME_SERIES_PTR": uc.EnsembleForecastTimeSeries,
    "TIME_SERIES_PROVIDER_PTR": uc.TimeSeriesProvider,
    # 'CatchmentStructure*': None,
    # 'OptimizerLogData*', DisposeOptimizerLogDataWila_py
}

_STRICT_WRAPPING = False

_wrapper_factory = CffiWrapperFactory(_api_type_wrapper, _STRICT_WRAPPING)


def _create_wrapper(obj: Any, type_id: str, release_native: Callable):
    return _wrapper_factory.create_wrapper(obj, type_id, release_native)


def wrap_cffi_native_handle(obj: Any, type_id: str, release_native: Callable):
    if not isinstance(obj, FFI.CData):
        return obj
    return _create_wrapper(obj, type_id, release_native)


swg.set_wrap_cffi_native_handle(wrapper_function=wrap_cffi_native_handle)
