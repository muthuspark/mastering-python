A = np.array([[1, 1], [1, 2], [1, 3]])
b = np.array([1, 3, 2])

Q, R = np.linalg.qr(A)

x = np.linalg.solve(R, np.dot(Q.T, b))

print("Solution x:", x)