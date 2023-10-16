from hmd import *


if __name__ == '__main__':
    train_path = "datasets/BeetleFly/BeetleFly_TRAIN.arff"
    df = arff_to_df(train_path)

    ts = df['ts'][2]
    scaled_ts = min_max_scale(ts)
    plot_ts_with_significant_point(scaled_ts)
