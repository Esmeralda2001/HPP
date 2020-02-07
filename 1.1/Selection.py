from typing import List
import numpy as np
import time

lst1 = list(np.arange(30000))
lst1.reverse()
print(lst1)


def selection_sort(data: List[int]) -> None:
    """Sort an array using selection sort"""
    # loop over len(data) -1 elements
    for index1 in range(len(data)-1):
        smallest = index1 # first index of remaining array

        # loop to find index of smallest element
        for index2 in range(index1 + 1, len(data)):
            if data[index2] < data[smallest]:
                smallest = index2

        # swap smallest element into position
        data[smallest], data[index1] = data[index1], data[smallest]


start = time.time()
selection_sort(lst1)
stop = time.time()
print(stop-start)