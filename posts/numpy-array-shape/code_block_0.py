import numpy as np

arr_1d = np.array([1, 2, 3, 4, 5])
print("Shape of 1D array:", arr_1d.shape)  # Output: (5,)

arr_2d = np.array([[1, 2, 3, 4],
                   [5, 6, 7, 8],
                   [9, 10, 11, 12]])
print("Shape of 2D array:", arr_2d.shape)  # Output: (3, 4)

arr_3d = np.array([[[1, 2], [3, 4]],
                   [[5, 6], [7, 8]]])
print("Shape of 3D array:", arr_3d.shape)  # Output: (2, 2, 2)