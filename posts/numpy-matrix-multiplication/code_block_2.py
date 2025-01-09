import numpy as np

matrix_a = np.array([[1, 2], [3, 4]])
matrix_b = np.array([[5, 6, 7], [8, 9, 10]])  # Incompatible dimensions

try:
    result = matrix_a @ matrix_b
    print(result)
except ValueError as e:
    print(f"Error: {e}") #Output: Error: matmul: Input operand 1 has a mismatch in its inner dimension