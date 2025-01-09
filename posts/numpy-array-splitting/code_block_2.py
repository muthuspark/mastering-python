import numpy as np

arr_2d = np.arange(12).reshape(3, 4)

vsplit_arr = np.vsplit(arr_2d, 3)
print("\nVertically split array:\n", vsplit_arr)