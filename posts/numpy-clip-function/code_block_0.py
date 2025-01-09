import numpy as np

arr = np.array([1, 5, 2, 8, 3, 9, 4, 7, 6])
clipped_arr = np.clip(arr, 3, 7) 
print(f"Original array: {arr}")
print(f"Clipped array: {clipped_arr}")