v = eigenvectors[:, 0]  # First eigenvector
λ = eigenvalues[0]       # Corresponding eigenvalue

print("Verification:")
print(np.dot(A, v))     # Matrix-vector multiplication
print(λ * v)           # Scalar multiplication of the eigenvector