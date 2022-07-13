import numpy as np
from typing import Dict


class Dataset:
    def __init__(self, dataset: Dict[str, np.ndarray]):
        self._data = dataset

    def load_from_csv(self, path) -> 'Dataset':
        pass

    def load_from_array(self, data: np.array) -> 'Dataset':
        pass


    def chose_best_split(self):
        # TODO : This function contains the algo which allows us to take the split from the dataset. I have to think about the link of a condition
        pass

    def split_condition(self, condition):
        # TODO : This function allows us to split the dataset given a condition. The format of the conditon is still unknown
        pass


