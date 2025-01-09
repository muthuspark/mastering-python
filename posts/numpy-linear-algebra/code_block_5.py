A = np.array([[2, 1], [1, -1]])
inverse_A = np.linalg.inv(A)
determinant_A = np.linalg.det(A)

print("Inverse of A:\n", inverse_A)
print("Determinant of A:", determinant_A)