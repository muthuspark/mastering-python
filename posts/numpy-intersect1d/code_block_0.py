import numpy as np

array1 = np.array([1, 2, 3, 4, 5])
array2 = np.array([3, 5, 6, 7, 8])

intersection = np.intersect1d(array1, array2)
print(intersection)  # Output: [3 5]