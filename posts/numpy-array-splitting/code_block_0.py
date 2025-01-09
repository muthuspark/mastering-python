import numpy as np

arr = np.arange(12)
print("Original array:\n", arr)

split_arr = np.split(arr, 3)
print("\nSplit array:\n", split_arr)

split_arr_indices = np.split(arr, [3, 7])
print("\nSplit array at indices:\n", split_arr_indices)

arr_2d = np.arange(12).reshape(3, 4)
print("\nOriginal 2D array:\n", arr_2d)

split_arr_2d_axis1 = np.split(arr_2d, 2, axis=1)
print("\nSplit 2D array along axis 1:\n", split_arr_2d_axis1)
