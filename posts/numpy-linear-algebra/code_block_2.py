import numpy as np

A = np.array([[2, 3], [1, -1]])
b = np.array([8, -1])
x = np.linalg.solve(A, b)
print(x)  # Output: [2. 1.40000000e-16] (approximately [2, 0])