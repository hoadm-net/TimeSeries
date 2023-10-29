from hmd import *
import matplotlib.pyplot as plt


if __name__ == '__main__':
    train_path = "../datasets/BeetleFly/BeetleFly_TRAIN.arff"
    df = arff_to_df(train_path)

    ts = df['ts'][0]
    plt.plot(ts)
    plt.title('Timeseries')
    plt.show()
