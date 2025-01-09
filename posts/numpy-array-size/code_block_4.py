import numpy as np

arr = np.array([[1, 2, 3], [4, 5, 6]], dtype=np.int32)
print(arr.itemsize)  # Output: 4
print(arr.itemsize * arr.size) #Output: 24