import numpy as np

arr_2d = np.array([[1, 2], [1, 2], [3, 4]])
unique_rows = np.unique(arr_2d, axis=0)
print(unique_rows) # Output: [[1 2] [3 4]]
