import numpy as np
import pandas as pd


def _df_from_dict(**kwargs):
    return pd.DataFrame.from_dict(dict(**kwargs))


def _npf(x):
    return np.array(x, dtype=float)
