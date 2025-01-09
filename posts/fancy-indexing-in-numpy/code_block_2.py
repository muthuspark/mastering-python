arr = np.array([1, 2, 3, 4, 5, 6])
bool_arr = np.array([True, False, True, False, True, False])

print(arr[bool_arr]) # Output: [1 3 5]

#Even better: Create the boolean array directly using a condition
print(arr[arr > 3]) # Output: [4 5 6]
