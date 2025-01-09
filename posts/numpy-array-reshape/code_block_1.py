import numpy as np

arr = np.arange(12)

reshaped_arr = arr.reshape(3, -1)
print("\nReshaped array using -1:\n", reshaped_arr)

reshaped_arr_alt = arr.reshape(-1, 3)
print("\nReshaped array using -1 (alternative):\n", reshaped_arr_alt)