import numpy as np

arr = np.array([10, 20, 30, 40, 50])

print(arr[0])  # Output: 10
print(arr[1:3]) # Output: [20 30]

indices = np.array([0, 2, 4])
print(arr[indices])  # Output: [10 30 50]

indices = np.array([1, 3, 0])
print(arr[indices])  # Output: [20 40 10]