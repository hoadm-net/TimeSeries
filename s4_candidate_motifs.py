from hmd import *
import matplotlib.pyplot as plt


if __name__ == '__main__':
    train_path = "datasets/BeetleFly/BeetleFly_TRAIN.arff"
    df = arff_to_df(train_path)

    ts = df['ts'][15]
    ts = min_max_scale(ts)
    significant_points = get_significant_points(ts)
    candidate_motifs = get_candidate_motifs(ts, significant_points)
    max_len = 0
    for candid in candidate_motifs:
        if candid.shape[0] > max_len:
            max_len = candid.shape[0]

    new_ts = homothety_transform(candidate_motifs[2], max_len)

    fig, axes = plt.subplots(1, 2)
    axes[0].plot(candidate_motifs[2])
    axes[1].plot(new_ts)
    plt.show()
