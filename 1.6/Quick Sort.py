import math
import time
import numpy as np

lst = [97, 3, 100, 55, 6]
lst1 = list(np.random.uniform(size=30000))
lst2 = list(np.arange(30000))
#lst2.reverse()

def Partition(arr, start, end):
    pos = start

    for i in range(start, end):
        if arr[i] < arr[end]:
            arr[i], arr[pos] = arr[pos], arr[i]
            pos += 1

    arr[pos], arr[end] = arr[end], arr[pos]
    return pos

def QuickSort(arr, start, end):
    if start < end:
        pos = Partition(arr, start, end)
        QuickSort(arr, start, pos - 1)
        QuickSort(arr, pos + 1, end)


start = time.time()
QuickSort(lst2, 0, len(lst2)-1)
stop = time.time()
print(stop-start)