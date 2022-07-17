from abc import ABC
import numpy as np


class AbstractPurityFunction(ABC):

    def purity_score(self, label_values: np.ndarray) -> float:
        pass


class InformationGain(AbstractPurityFunction):

    def _entropy(self, label_values: np.ndarray) -> float:
        _, number_of_unique_elements_per_class  = np.unique(label_values, return_counts=True)
        probabilities = number_of_unique_elements_per_class / number_of_unique_elements_per_class.sum()
        return sum(probabilities * -np.log2(probabilities))

    def purity_score(self, labels_values: np.ndarray) -> float:
        return 1 - self._entropy(labels_values)