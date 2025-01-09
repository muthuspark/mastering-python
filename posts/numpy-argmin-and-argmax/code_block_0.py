import numpy as np

arr = np.array([3, 1, 4, 1, 5, 9, 2, 6])

min_index = np.argmin(arr)
print(f"The index of the minimum value is: {min_index}")  # Output: 1

#argmin on a 2D array
arr_2d = np.array([[1, 5, 2], [8, 3, 9], [4, 7, 6]])
min_index_row = np.argmin(arr_2d, axis=0) #minimum index along each column
print(f"The indices of the minimum value along each column are: {min_index_row}") # Output: [0 1 0]

min_index_col = np.argmin(arr_2d, axis=1) #minimum index along each row
print(f"The indices of the minimum value along each row are: {min_index_col}") # Output: [0 1 0]