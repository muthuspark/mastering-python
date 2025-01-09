import numpy as np

A = np.array([[4, 12, -16], [12, 37, -43], [-16, -43, 98]])
L = np.linalg.cholesky(A)
print("Original Matrix A:\n", A)
print("\nLower Triangular Matrix L:\n", L)
print("\nL x L.T:\n", np.dot(L, L.T)) #Verify the decomposition


B = np.array([[1, 2], [2, 1]]) #Not positive definite
try:
    L_B = np.linalg.cholesky(B)
    print(L_B)
except np.linalg.LinAlgError as e:
    print("Error:", e)
