arr1 = np.array([1, 2, 3, 4, 5])
arr2 = np.array([3, 5, 6, 7, 8])
symmetric_difference = np.setxor1d(arr1, arr2)
print(symmetric_difference)  # Output: [1 2 4 6 7 8]