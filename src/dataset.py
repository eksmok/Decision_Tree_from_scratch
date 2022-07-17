import csv

import numpy as np
from typing import List, Optional, Tuple
from loss import InformationGain


class Dataset:
    def __init__(self, feature: np.ndarray, labels_values: np.ndarray):
        self._feature = feature
        self._label_values = labels_values

    # Idea for the loading data: creating another module which allows to generalize the format of the data imported
    # Using for example an abstract class for the loading package.

      def _get_possible_split(self):
        all_possibilites = {}

        for row in range(self._feature.shape[0]):
            all_possibilites[row] = np.unique(self._feature[:, row])
        return all_possibilites

    def _best_split_for_each_feature(self, purity_evaluation: InformationGain):
        information_gain_by_feature = {}
        possibilites = self._get_possible_split()

        for row in range(self._feature.shape[0]):
            ig_gain_max = -np.inf
            best_value = None
            best_feature_index = None

            for possibility in possibilites[i]:
                mask = self._get_condition()
                ig_gain_new = purity_evaluation.purity_value(labels_values=self._data[:, self._labels_index], mask=mask)
                if ig_gain_new > ig_gain_max:
                    ig_gain_max = ig_gain_new
                    best_value = possibility
                    best_feature_index = i

            ig_gain_by_feature[i] = [ig_gain_max, best_value, best_feature_index]
        return ig_gain_by_feature

    def chose_best_split(self, purity_evaluation: Information_gain):
        ig_dict = self._best_split_for_each_feature(purity_evaluation)
        max_ig = 0
        split = None
        for value_ig in ig_dict.values():
            if value_ig[0] > max_ig:
                split = value_ig
                max_ig = value_ig[0]
        return split

    def make_split(self, split: List[float, Optional[str, float], int]) -> Tuple['Dataset', 'Dataset']:
        mask = self._get_condition(split=split)

        data_right = self._data[mask]
        data_left = self._data[~mask]

        dataset_left = Dataset(dataset=data_left, labels_index=self._labels_index)
        dataset_right = Dataset(dataset=data_right, labels_index=self._labels_index)

        return dataset_left, dataset_right

    # TODO : Have to find the argument and the understand how to get a condition.
    def _get_condition(self, split) -> bool:
        pass

class LoadDataset:
    def __init__(self, features: np.ndarray, labels_values: np.ndarray):
        self._data = features
        self._labels_values: np.ndarray = labels_values

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
            label_values = []
            reader = csv.reader(csvfile, delimiter= csv_limiter)
            for row in reader:
                label_values.append(row)

            label_values = np.asarray(label_values)

        dataset = Dataset(feature=data, labels_values=label_values)
        return dataset

    @staticmethod
    def load_from_array(data: np.ndarray, label_values: np.ndarray) -> 'Dataset':
        dataset = Dataset(feature=data, labels_values=label_values)
        return dataset



