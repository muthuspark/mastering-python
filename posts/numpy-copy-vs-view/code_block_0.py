import numpy as np

original_array = np.array([1, 2, 3, 4, 5])
array_view = original_array.view()

array_view[0] = 10  # Modify the view

print("Original array:", original_array)  # Output: [10  2  3  4  5]
print("Array view:", array_view)       # Output: [10  2  3  4  5]