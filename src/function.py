import numpy as np
from typing import Dict, List

def entropy(data):
    _, uniqueClassesCounts = np.unique(data, return_counts=True)
    probabilities = uniqueClassesCounts / uniqueClassesCounts.sum()
    return sum(probabilities * -np.log2(probabilities))


def information_gain(y, mask, func=entropy):
    # TODO : (Optional) Create a loss class
    a = sum(mask)
    b = mask.shape[0] - a

    if (a == 0 or b == 0):
        ig = 0
    else:
        ig = func(y) - a / (a + b) * func(y[mask]) - b / (a + b) * func(y[~mask])

    return ig

def all_possibilites_from_array1D(arr: np.array):
    print(arr)
    arr_unique = np.unique(arr)

    return arr_unique


def get_possible_split(data: np.array, labels) -> Dict[str, np.array]:
    all_possibilites = {}
    for i in range(len(labels)):
        all_possibilites[labels[i]] = np.unique(data[:,i])
    return all_possibilites

def best_split_for_each_label(data: np.array, labels: List[str], target: np.array):
    ig_gain_by_label = {}
    possibilites = get_possible_split(data=data, labels=labels)
    # TODO : Change feature -> col_number
    for i in range(len(labels)):
        ig_gain_max = -np.inf
        best_value = None
        best_label = None
    # TODO : Handle the case of the boolean
    # TODO : Create a function which handle the split condition
    # TODO : Create Another Class dataset
        if isinstance(data[:,i][0], str):
                for possibility in possibilites[labels[i]]:
                    mask = data[:,i] == possibility
                    ig_gain_new = information_gain(y=target, mask=mask)
                    if ig_gain_new > ig_gain_max:
                        ig_gain_max = ig_gain_new
                        best_value = possibility
                        best_label = labels[i]
        else:
            for possibility in possibilites[labels[i]]:
                mask = data[:, i] < possibility
                ig_gain_new = information_gain(y=target, mask=mask)
                if ig_gain_new > ig_gain_max:
                    ig_gain_max = ig_gain_new
                    best_value = possibility
                    best_label = labels[i]
        ig_gain_by_label[labels[i]] = [ig_gain_max, best_value, best_label]
    return ig_gain_by_label


def best_split(data: np.array, labels: List[str], target: np.array):
    ig_dict = best_split_for_each_label(data=data, labels=labels, target=target)
    max_ig = 0
    split = None
    for value in ig_dict.values():
        if value[0] > max_ig:
            split = value
            max_ig = value[0]
    return split


def make_split(split: list, data: np.array, labels: List[str]):
    index = labels.index(split[2])
    if isinstance(split[1], str):
        mask = data[:,index] == split[1]
    else:
        mask = data[:, index] < split[1]

    data_right = data[mask]
    data_left = data[~mask]
    return data_left, data_right

# if __name__ == '__main__':
#     import pandas as pd
#     data = pd.read_csv('../useless/data.csv')
#     y = (data.Index >= 4).astype('int').values
#     labels = list(data.columns.values)
#     del labels[labels.index('Index')]
#     data = data.values
#     print(data)
#     print(data.shape)
#     split = best_split(data=data, labels = labels, target=y)