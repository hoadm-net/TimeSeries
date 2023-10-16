from scipy.io.arff import loadarff
import pandas as pd
import numpy as np


def read_arff(path: str) -> np.ndarray:
    """
    Read an arff file and return a time series object.

    :param path: arff path
    :return: Time series data in 2D array
    """
    raw_data, meta = loadarff(path)
    cols = [x for x in meta]
    data2d = np.zeros([raw_data.shape[0], len(cols)])
    for i, col in zip(range(len(cols)), cols):
        data2d[:, i] = raw_data[col]
    return data2d


def arff_to_df(path) -> pd.DataFrame:
    """
    Read an arff file and parse its data into a DataFrame

    :param path: arff path
    :return: DataFrame [timeseries, label]
    """
    raw_data, meta = loadarff(path)
    cols = [x for x in meta]
    ts = []
    lbl = []

    for row in raw_data:
        dt = list(row)
        npa = np.array(dt[:-1]).reshape((len(cols) - 1, 1))
        ts.append(npa)
        lbl.append(int(dt[-1]))

    return pd.DataFrame({
        'ts': ts,
        'lbl': lbl
    })
