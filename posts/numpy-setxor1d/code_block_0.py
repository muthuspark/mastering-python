import numpy as np

array1 = np.array([1, 2, 3, 4])
array2 = np.array([3, 4, 5, 6])

symmetric_difference = np.setxor1d(array1, array2)
print(symmetric_difference)  # Output: [1 2 5 6]