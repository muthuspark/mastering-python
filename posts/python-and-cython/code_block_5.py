import numpy as np
cimport numpy as np

def cy_numpy_sum(np.ndarray[np.int64_t] arr): # Specify NumPy array type
    cdef long long total = 0
    cdef int i
    cdef int n = arr.shape[0]
    for i in range(n):
        total += arr[i]
    return total

arr = np.arange(1000000, dtype=np.int64)
print(cy_numpy_sum(arr))