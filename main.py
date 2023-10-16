from hmd import *
import matplotlib.pyplot as plt


if __name__ == '__main__':
    train_path = "datasets/BeetleFly/BeetleFly_TRAIN.arff"
    df = arff_to_df(train_path)

    ts = df['ts'][0]
    ts = min_max_scale(ts)
    significant_points = get_significant_points(ts)
    candidate_motifs = get_candidate_motifs(ts, significant_points)
    std_candidate_motifs = standardize_motifs(candidate_motifs)
