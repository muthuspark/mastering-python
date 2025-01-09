import numpy as np

arr = np.arange(12)

try:
    reshaped_arr = arr.reshape(2, 7)  # This will raise a ValueError
    print(reshaped_arr)
except ValueError as e:
    print("\nError:", e)