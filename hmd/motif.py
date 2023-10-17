import numpy as np
from .preprocessing import homothety_transform


def get_candidate_motifs(ts: np.ndarray, significant_points: list) -> list:
    """
        Get all candidate motif of the timeseries by significant point list
    :param ts: Timeseries object
    :param significant_points: List of significant point
    :return:
    """
    candidates = []

    for i in range(len(significant_points) - 2):
        s = significant_points[i]
        e = significant_points[i+2]
        candidates.append(ts[s:e+1])

    return candidates


def standardize_motifs(motifs: list) -> list:
    """
        Standardize all motifs in the input list, use the method homothety_transform parses all
        candidate motifs into same length
    :param motifs: list timeseries
    :return: list new motifs in the same length
    """

    min_length = sum([ts.shape[0] for ts in motifs]) // len(motifs)
    filtered_motifs = [ts for ts in motifs if ts.shape[0] >= min_length]
    new_length = sum([ts.shape[0] for ts in filtered_motifs]) // len(filtered_motifs)
    new_motifs = []
    for m in filtered_motifs:
        ts = homothety_transform(m, new_length)
        new_motifs.append(ts)

    return new_motifs
