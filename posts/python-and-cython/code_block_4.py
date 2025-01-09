import numpy as np

def py_numpy_sum(arr):
    total = 0
    for i in range(len(arr)):
        total += arr[i]
    return total

arr = np.arange(1000000)
print(py_numpy_sum(arr))