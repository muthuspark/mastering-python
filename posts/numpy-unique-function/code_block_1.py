import numpy as np

arr = np.array([1, 2, 2, 3, 4, 4, 4, 5, 1])
unique_elements, indices, counts = np.unique(arr, return_index=True, return_counts=True)

print("Unique elements:", unique_elements)  # Output: [1 2 3 4 5]
print("Indices:", indices)  # Output: [0 1 3 4 7]
print("Counts:", counts)  # Output: [2 2 1 3 1]