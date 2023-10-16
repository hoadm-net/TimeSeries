import numpy as np


def find_min_point(ts: np.ndarray, i: int, n: int, r: float) -> tuple:
    """
        Find the significant minimum point of the time series from index i with compression rate r
    :param ts: Time series object
    :param i: Start index
    :param n: Timeseries length
    :param r: Compression rate
    :return: Index of the first significant minimum point
    """
    min_idx = i
    while i < n and ts[i] / ts[min_idx] < r:
        if ts[i] < ts[min_idx]:
            min_idx = i
        i += 1

    return i, min_idx


def find_max_point(ts: np.ndarray, i: int, n: int, r: float) -> tuple:
    """
        Find the significant maximum point of the time series from index i with compression rate r
    :param ts: Time series object
    :param i: Start index
    :param n: Timeseries length
    :param r: Compression rate
    :return: Index of the first significant maximum point
    """
    max_idx = i
    while i < n and ts[max_idx] / ts[i] < r:
        if ts[i] > ts[max_idx]:
            max_idx = i

        i += 1

    return i, max_idx


def find_first_two(ts: np.ndarray, n: int, r: float) -> tuple:
    """
        Find the first and the second significant pont
    :param ts: Time series object
    :param n: Timeseries length
    :param r: Compression rate
    :return: A tuple of Index of the 2 first significant point
    """
    i = 0
    i_min = 0
    i_max = 0

    while (i < n) and (ts[i] / ts[i_min] < r) or (ts[i_max] / ts[i] < r):
        if ts[i] < ts[i_min]:
            i_min = i

        if ts[i] > ts[i_max]:
            i_max = i

        i += 1

    if i_min < i_max:
        return i, i_min, i_max
    else:
        return i, i_max, i_min


def get_compression_rate(ts: np.ndarray) -> float:
    """
        Calculate the compression rate for each time series object
    :param ts: Time series object
    :return: Compression rate
    """
    return ts.mean() / (ts.mean() - (ts.std() / 4))


def get_significant_points(ts: np.ndarray) -> list:
    n = ts.shape[0]
    r = get_compression_rate(ts)
    significant_points = []

    i, fp, sp = find_first_two(ts, n, r)
    significant_points.append(fp)
    significant_points.append(sp)

    while i < n:
        i, max_i = find_max_point(ts, i, n, r)
        if max_i < n:
            significant_points.append(max_i)

        i, min_i = find_min_point(ts, i, n, r)
        if max_i < n:
            significant_points.append(min_i)

    return significant_points
