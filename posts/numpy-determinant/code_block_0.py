import numpy as np

matrix_2x2 = np.array([[1, 2],
                      [3, 4]])

determinant_2x2 = np.linalg.det(matrix_2x2)

print(f"The determinant of the 2x2 matrix is: {determinant_2x2}")