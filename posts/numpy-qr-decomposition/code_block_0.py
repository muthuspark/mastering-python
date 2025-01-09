import numpy as np

A = np.array([[1, 2], [3, 4], [5, 6]])

Q, R = np.linalg.qr(A)

print("Original Matrix A:\n", A)
print("\nOrthogonal Matrix Q:\n", Q)
print("\nUpper Triangular Matrix R:\n", R)
print("\nReconstructed Matrix A (Q*R):\n", np.dot(Q, R))