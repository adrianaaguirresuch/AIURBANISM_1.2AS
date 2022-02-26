import numpy as np


def rank_of_array(tug):
    return np.ndim(tug)
x = np.array([1, 2, 3])
y = np.array([[1,2,3],[4,5,6]])
print(rank_of_array(x))
print(rank_of_array(y))

