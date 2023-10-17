from hmd import *
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
from collections import Counter
import statistics


if __name__ == '__main__':
    train_path = "datasets/BeetleFly/BeetleFly_TRAIN.arff"
    df = arff_to_df(train_path)

    ts = df['ts'][8]
    ts = min_max_scale(ts)
    significant_points = get_significant_points(ts)
    candidate_motifs = get_candidate_motifs(ts, significant_points)
    std_candidate_motifs = standardize_motifs(candidate_motifs)

    X = [ts_2_list(ts) for ts in std_candidate_motifs]
    cluster_no = math.floor(len(std_candidate_motifs) / 1.5)
    kmeans = KMeans(n_clusters=cluster_no, random_state=0, n_init="auto").fit(X)
    points = list(kmeans.labels_)
    mode = statistics.mode(points)
    idx = points.index(mode)

    motif = std_candidate_motifs[idx]
    plt.plot(motif)
    plt.show()
