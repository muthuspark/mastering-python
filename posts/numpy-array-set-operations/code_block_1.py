arr = np.array([1, 2, 2, 3, 4, 4, 5, 1])
unique_elements, indices = np.unique(arr, return_index=True)
print(unique_elements)       # Output: [1 2 3 4 5]
print(indices)             # Output: [0 1 3 4 6]