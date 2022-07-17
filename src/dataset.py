import csv

import numpy as np
from typing import List, Optional, Tuple
from loss import AbstractPurityFunction


class Dataset:
    def __init__(self, feature: np.ndarray, labels_values: np.ndarray):
        self._feature = feature
        self._label_values = labels_values

    def _get_possible_split(self):
        all_possibilites = {}

        for col in range(self._feature.shape[1]):
            all_possibilites[col] = np.unique(self._feature[:, col])
        return all_possibilites

    def _best_split_for_each_feature(self, purity_evaluation: AbstractPurityFunction):
        purity_score_by_feature = {}
        possible_split_values = self._get_possible_split()

        for feature in range(self._feature.shape[0]):
            max_purity_score = -np.inf
            best_value = None
            feat = None
            for possible_split_value in possible_split_values[feature]:
                mask = self._get_condition()
                label_values_splitted = self._label_values[mask]
                new_purity_score = purity_evaluation.purity_score(label_values=label_values_splitted)
                if new_purity_score > max_purity_score:
                    max_purity_score = new_purity_score
                    best_value = possible_split_value
                    feat = feature
            purity_score_by_feature[feature] = [max_purity_score, best_value, feature]
        return purity_score_by_feature

    def chose_best_split(self, purity_evaluation: AbstractPurityFunction):
        purity_score_by_features = self._best_split_for_each_feature(purity_evaluation)
        max_purity_score = None
        split = None
        for purity_score_by_feature in purity_score_by_features.values():
            if purity_score_by_feature[0] > max_purity_score:
                split = purity_score_by_feature
                max_purity_score = purity_score_by_feature[0]
        return split

    def make_split(self, feature: int, feature_value):

        mask = self._get_condition(feat=feature, feature_value=feature_value)

        return Dataset(feature=self._feature[mask], labels_values=self._label_values[mask]),\
               Dataset(feature=self._feature[~mask], labels_values=self._label_values[~mask])

    # TODO : Have to find the argument and the understand how to get a condition.
    def _get_condition(self, feat: int, feature_value) -> bool:
        print(feat)
        print(feature_value)
        mask = self._feature[:, feat] < feature_value
        print(mask)
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



