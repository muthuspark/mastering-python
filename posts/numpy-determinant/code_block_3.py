non_square_matrix = np.array([[1, 2],
                              [3, 4],
                              [5, 6]])

try:
    determinant_non_square = np.linalg.det(non_square_matrix)
    print(determinant_non_square)
except np.linalg.LinAlgError as e:
    print(f"Error: {e}")