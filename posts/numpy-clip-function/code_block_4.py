import numpy as np

arr = np.array([-2, 0, 1, 5, -1, 8, 3])
clipped_arr = np.clip(arr, -1, np.inf) # Clip only the lower bound.
print(f"Clipped array (lower bound only): {clipped_arr}")

clipped_arr = np.clip(arr, -np.inf, 5) # Clip only the upper bound.
print(f"Clipped array (upper bound only): {clipped_arr}")