arr_2d = np.array([[1, 2, 3], [4, 5, 6]])
flattened_arr = arr_2d.ravel()
flattened_arr[0] = 100

print("Modified Flattened Array:", flattened_arr)
print("\nOriginal Array (Modified):\n", arr_2d)