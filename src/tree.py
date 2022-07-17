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