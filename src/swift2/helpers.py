import pandas as pd

import swift2.parameteriser as sp

from swift2.classes import CompositeParameteriser, HypercubeParameteriser, Simulation

from swift2.utils import c, mk_full_data_id, paste0


def parameteriser_lag_and_route():
    d = pd.DataFrame(
        dict(
            Name=c("alpha", "inverse_velocity"),
            Value=c(1, 1),
            Min=c(1e-3, 1e-3),
            Max=c(1e2, 1e2),
        )
    )
    p = HypercubeParameteriser.from_dataframe("Generic links", d)
    return p


# Lag and route has several discrete storage type modes. One way to set up the modeP
def lag_and_route_linear_storage_type(simulation):
    d = pd.DataFrame(
        dict(
            Name=["storage_type"],
            Value=[1.0],
            Min=[1.0],
            Max=[1.0],
        )
    )
    p = HypercubeParameteriser.from_dataframe("Generic links", d)
    p.apply_sys_config(simulation)


def set_reach_lengths_lag_n_route(simulation: "Simulation"):
    # transfer reach lengths to the Lag and route model
    link_ids = simulation.get_link_ids()
    keys = mk_full_data_id("link", link_ids, "Length")
    reach_lengths = simulation.get_state_value(keys)
    reach_lengths = [reach_lengths[x] for x in keys]
    simulation.set_state_value(
        paste0("link.", link_ids, ".reach_length"), reach_lengths
    )
