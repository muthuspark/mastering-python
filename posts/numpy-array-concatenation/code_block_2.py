import numpy as np

arr1 = np.array([[[1,2],[3,4]]])
arr2 = np.array([[[5,6],[7,8]]])
depth_stack = np.dstack((arr1, arr2))
print("\nDepth Stack using dstack:\n", depth_stack)
