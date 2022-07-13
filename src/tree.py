from node import Node
from leaf import Leaf
from dataset import Dataset
from typing import Dict, List, Union
import numpy as np
from function import best_split, make_split
# TODO : Utils.py
class Tree:
    def __init__(self, max_depth: int, min_length = 0):
        self.max_depth = max_depth
        self._depth = 0
        self._min_length = min_length
        self.list_node = {}
        self.root_node = Node(depth=0)


    def fit(self, data: np.array, labels: list, root_node: Node, target: str) -> Leaf:

        # Exit condition
        index_target = labels.index(target)
        target_values = data[:,index_target]
        if root_node.is_pure(target=target_values) or data.shape[0] < self._min_length:
            print(target_values)
            return Leaf(target_values[0], self.list_node)

        #Splitting Part
        split = best_split(data=data, labels=labels, target=target_values)
        data_left, data_right = make_split(split=split, data=data, labels=labels)
        self._depth += 1
        root_node.set_value(split[1])
        root_node.set_label(split[2])
        node_left = Node(depth=self._depth)
        node_right = Node(depth=self._depth)
        root_node.set_node(node_left=node_left, node_right=node_right)

        #For visualisation
        self.list_node[root_node] = [node_left, node_right]


        # Recursive Part
        self.fit(data=data_left, target=target, root_node=node_left, labels=labels)
        self.fit(data=data_right, target=target, root_node=node_right, labels=labels)

    def predict(self, new_dataset: Dataset):
        # TODO : After building the tree i have to predict the result of the prediction. second step.
        pass


if __name__ == '__main__':
    import pandas as pd
    import sklearn.datasets
    import pandas as pd

    data = sklearn.datasets.load_iris(as_frame=True).frame
    labels = list(data.columns)
    target = "target"
    tree = Tree(max_depth=5)
    root_node = Node(depth=0)
    leaf = tree.fit(root_node=root_node,data=data.values, labels=labels, target=target)




