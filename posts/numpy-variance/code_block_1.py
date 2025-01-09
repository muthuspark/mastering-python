import numpy as np

data_2d = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])

variance_all = np.var(data_2d)
print(f"Variance across the entire array: {variance_all}")

variance_axis0 = np.var(data_2d, axis=0)
print(f"Variance along axis 0: {variance_axis0}")

variance_axis1 = np.var(data_2d, axis=1)
print(f"Variance along axis 1: {variance_axis1}")