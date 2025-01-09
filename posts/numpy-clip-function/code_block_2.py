import numpy as np

arr = np.array([-2, 0, 1, 5, -1, 8, 3])
clipped_arr = np.clip(arr, -1, 5)
print(f"Original array: {arr}")
print(f"Clipped array: {clipped_arr}")