import csv
import numpy as np


class Dataset:
    def __init__(self, feature: np.ndarray, label: np.ndarray):
        self._feature = feature
        self._label = label

    @property
    def feature(self):
        return self._feature

    @feature.setter
    def feature(self, feature: np.ndarray):
        self._feature = feature

    @property
    def label(self):
        return self._label

    @label.setter
    def label(self, label: np.ndarray):
        self._label = label

    def make_split(self, feature: int, feature_value):
        mask = self.get_condition(feature=feature, feature_value=feature_value)

        return Dataset(feature=self.feature[mask], label=self.label[mask]),\
            Dataset(feature=self.feature[~mask], label=self.label[~mask])

    # TODO : Have to find the argument and the understand how to get a condition.
    def get_condition(self, feature: int, feature_value) -> bool:
        mask = self.feature[:, feature] < feature_value
        return mask

    class LoadDataset:
        def __init__(self):
            pass

        @staticmethod
        def load_from_csv(feature_path: str, csv_limiter: str, label_path: str, new_line: str = '') -> 'Dataset':

            # Feature importation
            with open(feature_path, newline=new_line) as csvfile:
                data = []
                reader = csv.reader(csvfile, delimiter=csv_limiter)
                for row in reader:
                    data.append(row)
                data = np.asarray(data)

                data = data[1:]
            # Label importation
            with open(label_path, newline=new_line) as csvfile:
                label = []
                reader = csv.reader(csvfile, delimiter=csv_limiter)
                for row in reader:
                    label.append(row)

                label = np.asarray(label)

            dataset = Dataset(feature=data, label=label)
            return dataset

        @staticmethod
        def load_from_array(data: np.ndarray, label: np.ndarray) -> 'Dataset':
            dataset = Dataset(feature=data, label=label)
            return dataset
        