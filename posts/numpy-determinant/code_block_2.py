matrix_3x3 = np.array([[1, 2, 3],
                      [4, 5, 6],
                      [7, 8, 9]])

determinant_3x3 = np.linalg.det(matrix_3x3)

print(f"The determinant of the 3x3 matrix is: {determinant_3x3}")