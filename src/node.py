from function import information_gain
from typing import List, Dict, Union, Tuple
import numpy as np
import pandas as pd

class Node:
    # TODO : All attribute are not written yet. I have to think by building the build_tree function
    def __init__(self, depth: int, labels_splitted: str = None, value_chosen_to_split: Union[str, float, int] = None):
        self._left_node = None
        self._right_node = None
        self._depth = depth
        self._labels_splitted = labels_splitted
        self._value_chosen_to_split = value_chosen_to_split


    # TODO Change the way is is coded he np.unique.
    def is_pure(self,target: np.array) -> bool:
        if np.unique(target).shape[0] == 1:
            return True
        return False

    def set_node(self, node_left: 'Node', node_right: 'Node'):
        self._left_node = node_left
        self._right_node = node_right

    @property
    def value_chosen_to_split(self):
        return self._value_chosen_to_split

    @value_chosen_to_split.setter
    def value_chosen_to_split(self, value):
        self._value_chosen_to_split = value

    # TODO : Make the attribute private
    @property
    def label(self, label):
        self.label = label