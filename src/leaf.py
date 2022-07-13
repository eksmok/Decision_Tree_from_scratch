from node import Node
from typing import Union



class Leaf:
    def __init__(self, target_value: Union[str, int, float], list_node):
        self.target_value = target_value
        self.list_node = list_node
