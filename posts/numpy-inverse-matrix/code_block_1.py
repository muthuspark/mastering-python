import numpy as np

B = np.array([[1, 2],
              [2, 4]])  # This matrix is singular (determinant is 0)

try:
    B_inv = np.linalg.inv(B)
    print("Inverse of B:\n", B_inv)
except np.linalg.LinAlgError:
    print("Matrix B is singular and does not have an inverse.")