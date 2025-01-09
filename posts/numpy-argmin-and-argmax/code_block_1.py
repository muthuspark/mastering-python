import numpy as np

arr = np.array([3, 1, 4, 1, 5, 9, 2, 6])

max_index = np.argmax(arr)
print(f"The index of the maximum value is: {max_index}")  # Output: 5

#argmax on a 2D array
arr_2d = np.array([[1, 5, 2], [8, 3, 9], [4, 7, 6]])
max_index_row = np.argmax(arr_2d, axis=0) #maximum index along each column
print(f"The indices of the maximum value along each column are: {max_index_row}") # Output: [1 0 1]

max_index_col = np.argmax(arr_2d, axis=1) #maximum index along each row
print(f"The indices of the maximum value along each row are: {max_index_col}") # Output: [1 2 2]
