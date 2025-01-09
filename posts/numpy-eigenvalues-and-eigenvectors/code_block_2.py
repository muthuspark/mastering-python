B = np.array([[2, -1, 0],
              [-1, 2, -1],
              [0, -1, 2]])

eigenvalues_B, eigenvectors_B = np.linalg.eig(B)

print("\nEigenvalues of B:", eigenvalues_B)
print("Eigenvectors of B:\n", eigenvectors_B)