import numpy as np

arr_c = np.empty((2, 2), order='C')
arr_f = np.empty((2, 2), order='F')
print("Row-major (C):\n", arr_c)
print("\nColumn-major (F):\n", arr_f)