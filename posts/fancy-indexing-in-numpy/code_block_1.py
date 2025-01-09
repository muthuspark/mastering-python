arr_2d = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])

row_indices = np.array([0, 2])
col_indices = np.array([1, 2])

print(arr_2d[row_indices, col_indices])  # Output: [2 9]