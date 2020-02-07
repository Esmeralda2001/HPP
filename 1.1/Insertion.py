from typing import List
import numpy as np
import time

lst1 = list(np.arange(30000))
lst2 = list(np.random.uniform(size=30000))
#lst1.reverse()
print(lst1)

def insertion_sort(data: List[int]) -> None:
    """Sorting an array in place using insertion sort."""
    # loop over len(data) - 1 elements
    for next in range(1, len(data)):
        insert = data[next] # value to insert
        move_item = next    # location to place element

        # search for place to put current element
        while move_item > 0 and data[move_item - 1] > insert:
            # shift element right one slot
            data[move_item] = data[move_item - 1]
            move_item -= 1

        data[move_item] = insert # place inserted element

start = time.time()
insertion_sort(lst2)
stop = time.time()
print(stop-start)