import numpy as np

A = np.array([[1, 2],
              [3, 4],
              [5, 6]])

U, s, Vh = np.linalg.svd(A)

print("U:\n", U)
print("\nsingular values:\n", s)
print("\nVh:\n", Vh)