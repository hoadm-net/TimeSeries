import math

import numpy as np
from sklearn.preprocessing import MinMaxScaler


def min_max_scale(ts: np.ndarray) -> np.ndarray:
    min_value = 1
    max_value = ts.max() - ts.min()
    scaler = MinMaxScaler(feature_range=(min_value, max_value))
    return scaler.fit_transform(ts)


def homothety_transform(ts: np.ndarray, new_length: int) -> np.ndarray:
    """

    :param ts:
    :param new_length:
    :return: New timeseries with new length
    """
    n = ts.shape[0]

    if n == new_length:
        return ts

    y_min = ts.min()
    y_max = ts.max()
    x_center = n // 2
    y_center = (y_max + y_min) // 2
    k = new_length / n
    data = []

    for i in np.arange(-(new_length / 2) + x_center, (new_length / 2) + x_center):
        xx = math.floor((i - x_center) / k + x_center)
        yy = ts[xx] - y_center / k + y_center
        data.append(yy)

    return np.array(data).reshape((new_length, 1))
