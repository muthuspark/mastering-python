import numpy as np

arr = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])

print(arr[[0, 1, 2], [0, 2, 1]])  # Output: [1 6 8]

rows = np.array([0, 2])
cols = np.array([1, 2])
print(arr[rows, cols]) # Output: [2 9]

print(arr[1:, [0,2]]) # Output: [[4 6] [7 9]]