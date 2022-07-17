import csv

import numpy as np
from typing import List, Optional, Tuple
from loss import Information_gain


class Dataset:
    def __init__(self, dataset: np.array, labels_index: int):
        self._data = dataset
        self._labels_index = labels_index

    # Idea for the loading data: creating another module which allows to generalize the format of the data imported
    # Using for example an abstract class for the loading package.

    @staticmethod
    def load_from_csv(path: str, csv_limiter: str, label_name: str, new_line: str = '') -> 'Dataset':

        with open(path, newline=new_line) as csvfile:
            data = []
            reader = csv.reader(csvfile, delimiter=csv_limiter)
            for row in reader:
                data.append(row)

            label_index = data[0].index(label_name)
            data = np.asarray(data)
            data = data[1:]

        dataset = Dataset(dataset=data, labels_index=label_index)
        return dataset

    @staticmethod
    def load_from_array(data: np.array, label_index: int) -> 'Dataset':
        dataset = Dataset(dataset=data, labels_index=label_index)
        return dataset

    def _get_possible_split(self):
        all_possibilites = {}

        for i in range(self._data.shape[0]):
            if i == self._labels_index:
                continue

            all_possibilites[i] = np.unique(self._data[:, i])
        return all_possibilites

    def _best_split_for_each_feature(self, purity_evaluation: Information_gain):
        ig_gain_by_feature = {}
        possibilites = self._get_possible_split()

        for i in range(self._data.shape[0]):
            ig_gain_max = -np.inf
            best_value = None
            best_feature_index = None
            if i == self._labels_index:
                continue

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

# TODO : Need all the function of this file. Just wrote and did no apply any test.
