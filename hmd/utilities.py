import matplotlib.pyplot as plt
from .s_points import get_significant_points


def plot_ts_with_significant_point(ts) -> None:
    """
        Plot the timeseries object with the significant points
    :param ts: Timeseries object
    :return: None
    """
    significant_points = get_significant_points(ts)

    fig, ax = plt.subplots()
    ax.plot(ts, color='b')

    for sp in significant_points[:-1]:
        ax.plot(sp - 1, ts[sp], 'or', fillstyle='none', ms=10)

    plt.show()
