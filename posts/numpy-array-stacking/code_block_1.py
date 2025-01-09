import numpy as np

a = np.array([1, 2, 3])
b = np.array([4, 5, 6])

stacked_array = np.hstack((a, b))
print(stacked_array)

c = np.array([[1,2],[3,4]])
d = np.array([[5,6],[7,8]])
stacked_array_2d = np.hstack((c,d))
print(stacked_array_2d)