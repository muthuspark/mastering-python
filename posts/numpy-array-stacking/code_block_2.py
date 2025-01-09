import numpy as np

a = np.array([1, 2, 3])
b = np.array([4, 5, 6])

stacked_array_vertical = np.concatenate((a,b), axis=0)
print(stacked_array_vertical)
#Output: [1 2 3 4 5 6]

stacked_array_horizontal = np.concatenate((a, b), axis=0)
print(stacked_array_horizontal)
#Output: [1 2 3 4 5 6]

c = np.array([[1,2],[3,4]])
d = np.array([[5,6],[7,8]])
stacked_array_2d_vertical = np.concatenate((c,d), axis=0)
print(stacked_array_2d_vertical)
#Output:

stacked_array_2d_horizontal = np.concatenate((c,d), axis=1)
print(stacked_array_2d_horizontal)