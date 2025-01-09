arr_2d = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])

row1 = arr_2d[0, :]
print(row1)  # Output: [1 2 3]

col2 = arr_2d[:, 1]
print(col2)  # Output: [2 5 8]

sub_array = arr_2d[1:3, 0:2]
print(sub_array) # Output: [[4 5] [7 8]]