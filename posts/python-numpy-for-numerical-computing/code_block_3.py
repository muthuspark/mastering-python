array = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])

print(array[0, 1])  # Output: 2

print(array[1, :])  # Output: [4 5 6]

print(array[:, 2])  # Output: [3 6 9]

print(array[0:2, 1:3]) # Output: [[2 3], [5 6]]