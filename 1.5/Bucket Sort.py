import math
import time
import numpy as np

lst = [97, 3, 100, 55, 6]
lst1 = list(np.random.randint(50000, size=30000))
lst2 = list(np.arange(30000))
lst2.reverse()

def makeLists(n):
    lsts = []
    for lst in range(n):
        lsts.append([])
    for i in range(len(lsts)):
        lsts[i] = []
    return lsts


def bucketSort(arr):
    bucket = makeLists(10)
    sortedList = np.zeros(len(arr))
    N = len(str(max(arr)))

    for n in range(1, N+1):
        counter = 0
        for i in range(len(arr)):
            num = arr[i]
            index = math.floor((num%10**n)/10**(n-1))
            bucket[index].append(num)
        for x in range(len(bucket)):
            for y in range(len(bucket[x])):
                if bucket[x][y]:
                    sortedList[counter] = bucket[x][y]
                    counter += 1
        bucket = makeLists(10)
        arr = sortedList
    return arr

start = time.time()
bucketSort(lst2)
stop = time.time()
print(stop-start)

