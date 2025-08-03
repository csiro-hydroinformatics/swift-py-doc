from typing import TYPE_CHECKING, Any, Dict, OrderedDict

if TYPE_CHECKING:
    from swift2.classes import Simulation
    from swift2.const import VecStr

import swift2.wrap.swift_wrap_custom as swc
import swift2.wrap.swift_wrap_generated as swg
from swift2.simulation import get_link_ids, get_node_ids, sort_by_execution_order

## File with functions facilitating the definition of model structure for particular needs (e.g. cookie cutting)

# upstream_calib_nodes = cal_element_ids_upstream[[element_id]]
# top_element_ids = vec_mkfullid('node', upstream_calib_nodes)
# element_id = as.character(element_id)
# bottom_element_id = mk_full_data_id('node', element_id)

def model_from_json_file(file_path:str) -> "Simulation":
    """Create a model simulation from a file with a JSON serialisation.

    Args:
        file_path (str): valid file path.

    Returns:
        Simulation: a catchment simulation.
    """
    from pathlib import Path
    if not Path(file_path).exists():
        raise FileNotFoundError(f"File not found: {file_path}")
    return swg.LoadModelSimulationFromJson_py(file_path)

def model_to_json_file(simulation: "Simulation", file_path:str) -> None:
    """Save a model simulation from a file with a JSON serialisation.

    Args:
        simulation (Simulation): Catchment simulation
        file_path (str): file path to save to
    """
    swg.SaveModelSimulationToJson_py(simulation, file_path)


def cookie_cut_dendritic_catchment(
    simulation: "Simulation", bottom_element_id: str, top_element_ids: "VecStr"
) -> "Simulation":
    """cookie cut a dendritic catchment (without confluences)

    Args:
        simulation (Simulation): base catchment simulation
        bottom_element_id (str): identifier of the most downstream element to keep
        top_element_ids (str): identifier(s) of the most upstream element(s) to keep

    Returns:
        Simulation: a subcatchment simulation, cookie cut from the base simulation. Deep clone of objects.
    """
    top_element_ids = top_element_ids or []
    top_element_ids = [top_element_ids] if isinstance(top_element_ids, str) else top_element_ids
    # stopifnot(element_id %in% as.character(swift_cal_element_ids))
    select_network_above_element = True
    include_element_in_selection = True
    invert_selection = False
    subset_simul = swg.SubsetModel_py(
        simulation,
        bottom_element_id,
        select_network_above_element,
        include_element_in_selection,
        invert_selection,
        top_element_ids,
        len(top_element_ids),
    )
    return subset_simul


def subset_catchment(
    simulation: "Simulation", element_id: str, action: str = "keep_above"
) -> "Simulation":
    """Subsets a catchment, keeping only a portion above or below a node, link or subarea.

    Args:
        simulation (Simulation): an S4 object 'ExternalObjRef' [package "cinterop"] with external pointer type "MODEL_SIMULATION_PTR"
        element_id (str): id of the element to cut at.
        action (str): how to cut; currently limited to 'keep_above'

    Returns:
        Simulation: a subcatchment simulation, cookie cut from the base simulation. Deep clone of objects.
    """
    # if (action != 'keep_above'):stop('Only subset upstream of a node or link is supported for now')}
    # 'keep above'
    # 'keep above exclusive' # above element but element is not in the result;
    # 'keep below'
    # 'keep below exclusive'

    action = action.lower()
    action = action.replace("_", " ")

    select_network_above_element = "above" in action
    include_element_in_selection = not "exclusive" in action
    invert_selection = False  # TOCHECK
    return swc.subset_model_pkg(
        simulation,
        element_id,
        select_network_above_element,
        include_element_in_selection,
        invert_selection,
    )


def split_to_subcatchments(
    simulation, split_element_ids, include_upstream=None
) -> OrderedDict[str, "Simulation"]:
    """Split a catchment in subcatchments, given a list of node/link element identifiers

    Args:
        simulation (Simulation): base catchment simulation
        split_element_ids (str): element identifiers such as 'node.n1', 'link.linkId_2'
        include_upstream (bool, optional): indicates whether for each element in split_element_ids it should be including in the upstream portion of the subcatchment. Defaults to None.

    Returns:
        OrderedDict: list of subcatchments resulting from the split

    Examples:
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
    """
    from swift2.utils import rep

    if include_upstream is None:
        include_upstream = rep(True, len(split_element_ids))
    assert len(split_element_ids) == len(include_upstream)
    # It is conceivable that we'd cut out on the same link or node (i.e. keep one link+its catchment or just a node
    # , but for the time being not supported - unnecessary complication
    if len(split_element_ids) != len(set(split_element_ids)):
        raise ValueError(
            "split_element_ids has some duplicate elements - they must be unique"
        )
    # TODO check that all elements are valid identifiers

    e_ids_sorted = sort_by_execution_order(simulation, split_element_ids)
    # include_upstreamSorted = sort_by(include_upstream, split_element_ids, e_ids_sorted)

    n = len(e_ids_sorted)
    result = OrderedDict()

    remaining_catchment = simulation
    for i in range(n):
        e_id = e_ids_sorted[i]
        action_up = (
            "keep_above_inclusive" if include_upstream[i] else "keep_above_exclusive"
        )
        action_down = (
            "keep_below_exclusive" if include_upstream[i] else "keep_below_inclusive"
        )
        up_stream = subset_catchment(remaining_catchment, e_id, action=action_up)
        remaining_catchment = subset_catchment(
            remaining_catchment, e_id, action=action_down
        )
        result[e_ids_sorted[i]] = up_stream
    # We have n to n+1 outputs, depending on whether we have a remainder subcatchment at the bottom of the catchment.
    if len(get_node_ids(remaining_catchment) + get_link_ids(remaining_catchment)) > 0:
        if "remainder" in result.keys():
            raise ValueError(
                "There is already a key 'remainder'; cannot add the remaining downstream catchment"
            )
        result["remainder"] = remaining_catchment
    return result


def get_catchment_structure(simulation) -> Dict:
    """Gets the essential connective structure of a catchment

    Args:
        simulation (Simulation): base catchment simulation

    Returns:
        [type]: [description]

    Examples:
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
    """
    return swc.get_catchment_structure_pkg(simulation)


# #' Gets the catchment elements connecting directly to a given catchment element.
# #'
# #' Gets the catchment elements connecting directly to a given catchment element.
# #'
# #' @param catchmentStructure list as output by getCatchmentStructure, or an S4 object 'ExternalObjRef' [package "cinterop"] with external pointer type "MODEL_SIMULATION_PTR"
# #' @param element_id element identifier such as 'link.lnk1'
# #' @return list or data frame depending on the element (list if link, and it has both a subarea and nodes connected to it)
# #' @examples
# #' \dontrun{
# #' simulation = createTestCatchment()
# #' (cs = getCatchmentStructure(simulation))
# #' elementConnectivity(cs, 'link.lnk2')
# #' elementConnectivity(cs, 'node.n2')
# #' elementConnectivity(cs, 'subarea.lnk2')
# #' }
# #' @export
# elementConnectivity(catchmentStructure, element_id)
# {
#   stopifnot(len(element_id) == 1)
#   if (isSingularSimulation(catchmentStructure)):
#     catchmentStructure = getCatchmentStructure(catchmentStructure)
#   }
#   nl = catchmentStructure$NodeLink
#   # DownstreamId UpstreamId LinkId
#   sl = catchmentStructure$SubareaLink
#   # LinkId SubareaId
#   x = stringr::str_split(element_id, '\\.')[[1]]
#   stopifnot(len(x) >= 2)
#   eltType = x[1]
#   eltId = x[2]
#   stopifnot(eltType %in% c('node','link','subarea'))
#   if (eltType == 'link'):
#     i = which(nl$LinkId == eltId)
#     if(len(i) == 0) stop(paste0('not found: ', element_id))
#     if(len(i) > 1) stop(paste0('unexpected duplicate entries found: ', element_id))
#     j = which(sl$LinkId == eltId)
#     return(list(NodeLink=nl[i,], SubareaLink=sl[j,]))
#   } else if ( eltType == 'node' ):
#     i = c(which(nl$UpstreamId == eltId), which(nl$DownstreamId == eltId))
#     return(nl[i,])
#   } else if ( eltType == 'subarea' ):
#     i = which(sl$SubareaId == eltId)
#     return(sl[i,])
#   }
# }

# #' Gets the catchment element downstream of a given catchment element.
# #'
# #' Gets the catchment element downstream of a given catchment element.
# #'
# #' @param catchmentStructure list as output by getCatchmentStructure, or an S4 object 'ExternalObjRef' [package "cinterop"] with external pointer type "MODEL_SIMULATION_PTR"
# #' @param element_id element identifier such as 'link.lnk1'
# #' @return list or data frame depending on the element (list if link, and it has both a subarea and nodes connected to it)
# #' @examples
# #' \dontrun{
# #' simulation = createTestCatchment()
# #' (cs = getCatchmentStructure(simulation))
# #' downstreamElements(cs, 'link.lnk2')
# #' downstreamElements(cs, 'node.n2')
# #' downstreamElements(cs, 'subarea.lnk2')
# #' }
# #' @export
# downstreamElements(catchmentStructure, element_id)
# {
#   cx = elementConnectivity(catchmentStructure, element_id)
#   x = stringr::str_split(element_id, '\\.')[[1]]
#   stopifnot(len(x) >= 2)
#   eltType = x[1]
#   eltId = x[2]
#   if (eltType == 'link'):
#     nodeid = cx$NodeLink$DownstreamId
#     if (is.na(nodeid) || (len(nodeid)==0)) return(NA_character_)
#     return(paste0('node.', nodeid))
#   } else if ( eltType == 'node' ):
#     i = which(cx$UpstreamId == eltId)
#     if (len(i) == 0) return(NA_character_)
#     link_ids = as.character(cx[i,]$LinkId) # there may be several downstream links used someday...
#     return(paste0('link.', link_ids))
#   } else if ( eltType == 'subarea' ):
#     i = which(cx$SubareaId == eltId)
#     if (len(i) == 0) return(NA_character_)
#     return(paste0('link.', cx[i,]$LinkId))
#   }
# }
