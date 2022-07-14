from abc import ABC
import numpy as np


class Purity_function(ABC):
    def __init__(self):
        pass

    def purity_value(self, label_values: np.array, mask) -> float:
        pass


class Information_gaing(Purity_function):
    super().__init__()



    def _entropy(self, label_values: np.array) -> float:
        _, uniqueClassesCounts = np.unique(label_values, return_counts=True)
        probabilities = uniqueClassesCounts / uniqueClassesCounts.sum()
        return sum(probabilities * -np.log2(probabilities))

    def purity_value(self, labels_values: np.array, mask) -> float:
        a = sum(mask)
        b = mask.shape[0] - a

        if (a == 0 or b == 0):
            ig = 0
        else:
            ig = self._entropy(labels_values) - a / (a + b) * self._entropy(labels_values[mask]) - b / (a + b) * self._entropy(labels_values[~mask])

        return ig
