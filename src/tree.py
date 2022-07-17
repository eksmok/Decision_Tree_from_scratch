from node import Node
from leaf import Leaf
from dataset import Dataset
from loss import AbstractPurityFunction
from typing import Union
import numpy as np


# TODO : Utils.py
class Tree:
    def __init__(self, max_depth: int, min_length=0):
        self.max_depth = max_depth
        self._depth = 0
        self._min_length = min_length
        self.list_node = {}
        self.root_node = Node(depth=0)

    def fit(self, dataset: Dataset, root_node: Node, purity_evaluation: AbstractPurityFunction) -> Union[Leaf, Node]:

        # Exit condition
        if root_node.is_pure(label=dataset.label) or dataset.label.shape[0] < self._min_length:
            #print(dataset.label[0])
            return Leaf(label_value=dataset.label, depth=root_node.depth)

        # Splitting Part
        split = self._best_split(purity_evaluation=purity_evaluation, dataset=dataset)
        print('Choix du Split : {}'.format(split))
        dataset_left, dataset_right = dataset.make_split(feature=split[2], feature_value=split[1])
        self._depth += 1

        print(root_node)
        root_node.set_value_chosen_to_split = split[1]
        root_node.feature_split = split[2]

        # Set right and left node on the parent node
        root_node.left_node = Node(depth=self._depth)
        root_node.right_node = Node(depth=self._depth)

        # Recursive Part
        self.fit(dataset=dataset_left, root_node=root_node.left_node, purity_evaluation=purity_evaluation)
        self.fit(dataset=dataset_right, root_node=root_node.right_node, purity_evaluation=purity_evaluation)

    @staticmethod
    def _get_possible_split(feature: np.ndarray):
        all_possible_value_per_each_feature = {}

        for col in range(feature.shape[1]):
            all_possible_value_per_each_feature[col] = np.unique(feature[:, col])
        return all_possible_value_per_each_feature

    def _best_split_for_each_feature(self, purity_evaluation: AbstractPurityFunction, dataset: Dataset):
        purity_score_by_feature = {}
        possible_split_values = self._get_possible_split(feature=dataset.feature)

        for feature in range(dataset.feature.shape[1]):
            max_purity_score = -np.inf
            best_value = None
            feat = None
            for possible_split_value in possible_split_values[feature]:

                mask = dataset.get_condition(feature=feature, feature_value=possible_split_value)
                label_split = dataset.label[mask]
                new_purity_score = purity_evaluation.purity_score(label=dataset.label, mask=label_split)
                if new_purity_score > max_purity_score:
                    max_purity_score = new_purity_score
                    best_value = possible_split_value
                    feat = feature
            purity_score_by_feature[feature] = [max_purity_score, best_value, feat]
        return purity_score_by_feature

    def _best_split(self, purity_evaluation: AbstractPurityFunction, dataset: Dataset):
        purity_score_by_features = self._best_split_for_each_feature(purity_evaluation, dataset=dataset)
        max_purity_score = -np.inf
        split = None
        for purity_score_by_feature in purity_score_by_features.values():
            if purity_score_by_feature[0] > max_purity_score:
                split = purity_score_by_feature
                max_purity_score = purity_score_by_feature[0]
        return split

    def predict(self, new_dataset: Dataset):
        # TODO : After building the tree i have to predict the result of the prediction. second step.
        pass
