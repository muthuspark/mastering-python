import numpy as np

A = np.array([[2, 1],
              [1, 1]])

A_inv = np.linalg.inv(A)

print("The inverse of A is:\n", A_inv)

print("\nA * A_inv:\n", np.dot(A, A_inv))