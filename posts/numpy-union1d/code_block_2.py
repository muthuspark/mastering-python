array7 = np.array([1, 2, 2, 3, 3, 3, 4])
array8 = np.array([3, 4, 4, 5, 6])

union_array = np.union1d(array7, array8)
print(union_array) # Output: [1 2 3 4 5 6]