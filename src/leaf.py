from typing import Optional



class Leaf:
    def __init__(self, target_value: Optional[str, float, int], depth: int):
        self.target_value = target_value
        self.depth = depth
