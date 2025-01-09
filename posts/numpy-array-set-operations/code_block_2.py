arr = np.array([1, 2, 2, 3, 4, 4, 5, 1])
unique_elements, counts = np.unique(arr, return_counts=True)
print(unique_elements)       # Output: [1 2 3 4 5]
print(counts)              # Output: [2 2 1 2 1]