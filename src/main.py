from dataset import Dataset, LoadDataset
import pandas as pd


if __name__ == '__main__':
    df = pd.read_csv('../Iris.csv').values

    d = LoadDataset()
    dataset = d.load_from_array(df[:,1:5], label_values=df[:,5])
    print(dataset._feature)
    data_right, data_left = dataset.make_split(feature = 1, feature_value=3.0)
