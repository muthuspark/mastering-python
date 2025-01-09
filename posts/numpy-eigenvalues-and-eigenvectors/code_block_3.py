C = np.array([[0, 1],
              [-1, 0]])

eigenvalues_C, eigenvectors_C = np.linalg.eig(C)

print("\nEigenvalues of C:", eigenvalues_C)
print("Eigenvectors of C:\n", eigenvectors_C)