from abc import ABC
import numpy as np
from collections import Counter

class AbstractPurityFunction(ABC):

    def purity_score(self, label_values: np.ndarray, label_split: np.ndarray) -> float:
        pass


class InformationGain(AbstractPurityFunction):

    def _entropy(self, label: np.ndarray):
        entropy = 0
        label_counts = Counter(label)
        for label in label_counts:
            prob_of_label = label_counts[label] / len(label)
            entropy -= prob_of_label * np.log2(prob_of_label)
        return entropy

    def information_gain(self,label: np.ndarray, split_label: np.ndarray):
        if len(label) or len(split_label):
            return 0
        else:
            purity_score = self._entropy(label)
            for branched_subset in split_label:
                purity_score -= len(branched_subset) * self._entropy(branched_subset) / len(label)
        return purity_score
