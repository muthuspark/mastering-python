import numpy as np

arr_1d = np.arange(12)
print("Original 1D array:\n", arr_1d)

arr_2d = arr_1d.reshape(3, 4)
print("\nReshaped 2D array:\n", arr_2d)

arr_2d_alt = arr_1d.reshape(4,3)
print("\nReshaped 2D array (alternative):\n", arr_2d_alt)

arr_3d = arr_1d.reshape(2, 3, 2)
print("\nReshaped 3D array:\n", arr_3d)
