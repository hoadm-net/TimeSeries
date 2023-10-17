from hmd import *
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
from collections import Counter
import statistics


if __name__ == '__main__':
    # train_path = "datasets/BeetleFly/BeetleFly_TRAIN.arff"
    # df = arff_to_df(train_path)
    #
    # ts = df['ts'][0]
    # ts = min_max_scale(ts)
    # significant_points = get_significant_points(ts)
    # candidate_motifs = get_candidate_motifs(ts, significant_points)
    # std_candidate_motifs = standardize_motifs(candidate_motifs)
    #
    # X = [ts_2_list(ts) for ts in std_candidate_motifs]
    # cluster_no = math.floor(len(std_candidate_motifs) / 1.5)
    # kmeans = KMeans(n_clusters=cluster_no, random_state=0, n_init="auto").fit(X)
    #
    # print(kmeans.labels_)
    #
    # motif_num = len(std_candidate_motifs)
    # fig, axes = plt.subplots(motif_num, 1)
    # for i in range(motif_num):
    #     axes[i].plot(std_candidate_motifs[i])
    # plt.show()

    a = [5, 0, 2, 3, 1, 0, 5, 4, 2, 4]
    mode = statistics.mode(a)
    print(a.index(mode))
