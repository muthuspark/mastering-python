import numpy as np

arr_2d = np.array([[1, 2, 3], [4, 5, 6]])

flattened_arr = arr_2d.flatten()
raveled_arr = arr_2d.ravel()

flattened_arr[0] = 100  # Modifying the flattened array

raveled_arr[0] = 200   # Modifying the raveled array

print("Original Array after flattening modification:\n", arr_2d)
print("\nOriginal Array after ravel modification:\n", arr_2d)

print("\nFlattened Array:\n", flattened_arr)
print("\nRaveled Array:\n", raveled_arr)