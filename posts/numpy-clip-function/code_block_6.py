import numpy as np

arr_2d = np.array([[1, 10, 3], [-5, 2, 8]])
clipped_arr_2d = np.clip(arr_2d, -2, 7)
print(f"Original 2D array:\n{arr_2d}")
print(f"Clipped 2D array:\n{clipped_arr_2d}")