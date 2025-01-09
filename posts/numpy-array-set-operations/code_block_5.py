arr1 = np.array([1, 2, 3, 4, 5])
arr2 = np.array([3, 5, 6, 7, 8])
difference = np.setdiff1d(arr1, arr2)
print(difference)  # Output: [1 2 4]