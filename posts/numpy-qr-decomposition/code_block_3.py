A = np.array([[1+1j, 2-1j], [3j, 4]])

Q, R = np.linalg.qr(A)

print("Q:\n", Q)
print("\nR:\n", R)
