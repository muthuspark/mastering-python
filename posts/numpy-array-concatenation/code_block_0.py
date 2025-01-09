import numpy as np

arr1 = np.array([[1, 2], [3, 4]])
arr2 = np.array([[5, 6], [7, 8]])
vertical_stack = np.concatenate((arr1, arr2), axis=0)
print("Vertical Concatenation:\n", vertical_stack)

arr3 = np.array([[1, 2], [3, 4]])
arr4 = np.array([[5, 6], [7, 8]])
horizontal_stack = np.concatenate((arr3, arr4), axis=1)
print("\nHorizontal Concatenation:\n", horizontal_stack)

arr5 = np.array([1,2,3])
arr6 = np.array([[4],[5],[6]])
vertical_stack_diff = np.concatenate((arr5.reshape(1,3), arr6), axis=0)
print("\nConcatenating arrays of different shapes:\n", vertical_stack_diff)