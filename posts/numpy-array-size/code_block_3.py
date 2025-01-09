import numpy as np

arr = np.array([[1, 2, 3], [4, 5, 6]], dtype=np.int32)  # 32-bit integers
print(arr.nbytes)  # Output: 24 (6 elements * 4 bytes/element)

arr_float = np.array([[1.1, 2.2, 3.3], [4.4, 5.5, 6.6]], dtype=np.float64) # 64-bit floats
print(arr_float.nbytes) # Output: 48 (6 elements * 8 bytes/element)
