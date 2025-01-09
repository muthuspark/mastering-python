arr_2d = np.array([[1, 2, 3], [4, 5, 6]])
flattened_copy = arr_2d.flatten()
flattened_copy[0] = 100

print("Modified Flattened Copy:", flattened_copy)
print("\nOriginal Array (Unchanged):\n", arr_2d)
