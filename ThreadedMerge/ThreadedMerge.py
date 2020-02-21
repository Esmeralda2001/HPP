import threading
import numpy as np
import time
import statistics
import matplotlib.pyplot as plt

def merge_sort(arr):
    if len(arr) < 2:
        return arr
    mid = int(len(arr) / 2)
    x = merge_sort(arr[:mid])
    y = merge_sort(arr[mid:])

    return merge(x, y)


def merge(A, B):
    i = 0
    j = 0
    C = []

    while i < len(A) and j < len(B):
        if A[i] < B[j]:
            C.append(A[i])
            i += 1
        else:
            C.append(B[j])
            j += 1
    return C + A[i:] + B[j:]



class WorkerThread(threading.Thread):

    def __init__(self, args):
        threading.Thread.__init__(self, args=args)
        self.arr = args[0]

    def run(self):
        self.arr = merge_sort(self.arr)

    def get(self):
        return self.arr

def threaded_mergesort(arr, threads):
    if len(arr) < threads:
        return "Error amount of threads exceeds array length"
    if threads == 1:
        return merge_sort(arr)

    arrs = list(np.array_split(arr, threads))

    threadList = []
    for i in range(threads):
        W = WorkerThread([list(arrs[i])])
        threadList.append(W)
        W.start()

    result = []
    for j in range(0, len(threadList)-1, 2):
        threadList[j].join()
        threadList[j+1].join()
        result.append(merge(threadList[j].get(), threadList[j+1].get()))

    resultCount = len(result)
    while resultCount >= 2:
        resultCopy = []
        for x in range(0, resultCount-1, 2):
            resultCopy.append(merge(result[x], result[x+1]))
        result = resultCopy
        resultCount = len(result)

    return result[0]


print(threaded_mergesort([3, 2, 8, 6, 7, 1, 5, 10, 4, 7, 11, 9, 20, 21, 25, 30, 2], 2))

num_threads = [1, 2, 4, 8]
arrs = [np.random.randint(100, size=16), np.random.randint(100, size=8), np.random.randint(100, size=32), np.random.randint(100, size=25), np.random.randint(100, size=30)]

timesPerThread = []
for num in num_threads:
    timer = []
    for arr in arrs:
        start = time.time()
        threaded_mergesort(list(arr), num)
        stop = time.time()
        timer.append(stop - start)
    timesPerThread.append(statistics.mean(timer))

plt.plot([1, 2, 4, 8], timesPerThread)
plt.xlabel("Threads")
plt.ylabel("Time in seconds")
plt.xticks([1, 2, 4, 8])
plt.show()