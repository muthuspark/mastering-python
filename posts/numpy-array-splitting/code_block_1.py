import numpy as np

arr_2d = np.arange(12).reshape(3, 4)

hsplit_arr = np.hsplit(arr_2d, 2)
print("\nHorizontally split array:\n", hsplit_arr)