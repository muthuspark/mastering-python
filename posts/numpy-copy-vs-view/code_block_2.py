import numpy as np

original_array = np.array([1, 2, 3, 4, 5])
array_copy = original_array.copy()

array_copy[0] = 100

print("Original array:", original_array)  # Output: [1  2  3  4  5]
print("Array copy:", array_copy)       # Output: [100   2   3   4   5]