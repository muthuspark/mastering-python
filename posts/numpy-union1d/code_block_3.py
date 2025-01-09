array9 = np.array([1, 2, 3])
array10 = np.array([3, 4, 5])
array11 = np.array([5, 6, 7])

union_array = np.union1d(array9, array10, array11)
print(union_array) # Output: [1 2 3 4 5 6 7]