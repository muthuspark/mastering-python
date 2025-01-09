array3 = np.array([1, 1, 2, 3, 3, 4])
array4 = np.array([1, 3, 5])

difference = np.setdiff1d(array3, array4)
print(difference)  # Output: [2 4]