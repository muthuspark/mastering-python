import numpy as np

a = np.array([1, 2, 3])
b = np.array([4, 5, 6])

stacked_array = np.stack((a, b))
print(stacked_array)

stacked_array_axis1 = np.stack((a,b), axis=1)
print(stacked_array_axis1)