A = np.array([[1, 2], [3, 4], [5, 6]])

Q, R = np.linalg.qr(A, mode='reduced') # Reduced Q (m x n)

print("Reduced Q:\n", Q)
print("\nR:\n", R)