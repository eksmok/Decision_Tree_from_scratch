from typing import Optional, Union

class Leaf:
    def __init__(self, label_value: Optional[Union[str, float]], depth: int):
        self._label_value = label_value
        self._depth = depth