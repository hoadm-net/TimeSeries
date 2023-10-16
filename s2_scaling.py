from hmd import *
import matplotlib.pyplot as plt


if __name__ == '__main__':
    train_path = "datasets/BeetleFly/BeetleFly_TRAIN.arff"
    df = arff_to_df(train_path)

    ts = df['ts'][0]
    scaled_ts = min_max_scale(ts)
    fig, axes = plt.subplots(1, 2, sharey=True)

    axes[0].plot(ts)
    axes[1].plot(scaled_ts)
    plt.show()
