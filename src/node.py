from typing import Union
import numpy as np


class Node:
    def __init__(self, depth: int, feature_split: int = None, value_chosen_to_split: Union[str, float, int] = None):
        self._left_node = None
        self._right_node = None
        self._depth = depth
        self._feature_split = feature_split
        self._value_chosen_to_split = value_chosen_to_split

    @staticmethod
    def is_pure(label: np.array) -> bool:
        if np.unique(label).shape[0] == 1:
            return True
        return False

    @property
    def value_chosen_to_split(self):
        return self._value_chosen_to_split

    @value_chosen_to_split.setter
    def value_chosen_to_split(self, value):
        self._value_chosen_to_split = value

    @property
    def left_node(self):
        return self._left_node

    @left_node.setter
    def left_node(self, left_node: 'Node'):
        self._left_node = left_node

    @property
    def right_node(self):
        return self._right_node

    @right_node.setter
    def right_node(self, right_node: 'Node'):
        self._right_node = right_node

    @property
    def depth(self):
        return self._depth

    @depth.setter
    def depth(self, depth: int):
        self._depth = depth

    @property
    def feature_split(self):
        return self._feature_split

    @feature_split.setter
    def feature_split(self, feature_split: np.ndarray):
        self._feature_split = feature_split