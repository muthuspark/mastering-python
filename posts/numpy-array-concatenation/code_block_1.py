import numpy as np

arr1 = np.array([1, 2, 3])
arr2 = np.array([4, 5, 6])

vertical_stack = np.vstack((arr1, arr2))
print("Vertical Stack using vstack:\n", vertical_stack)

arr3 = np.array([[1],[2],[3]])
arr4 = np.array([[4],[5],[6]])

horizontal_stack = np.hstack((arr3, arr4))
print("\nHorizontal Stack using hstack:\n", horizontal_stack)
