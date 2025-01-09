import numpy as np

array1 = np.array([1, 2, 2, 3])
array2 = np.array([2, 3, 3, 4])

symmetric_difference = np.setxor1d(array1, array2)
print(symmetric_difference)  # Output: [1 4]