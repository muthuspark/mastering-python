from scipy import linalg
import numpy as np

A = np.array([[2, 1], [1, -1]])
b = np.array([8, 1])

x = linalg.solve(A, b)
print(f"The solution is: {x}")