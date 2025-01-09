import numpy as np

def fibonacci_matrix(n):
    """
    Calculates the nth Fibonacci number using matrix exponentiation.

    Args:
        n: The index of the desired Fibonacci number (starting from 0).

    Returns:
        The nth Fibonacci number.
    """
    if n <= 1:
        return n
    matrix = np.array([[1, 1], [1, 0]], dtype=object)  # Use object dtype for large numbers
    result = np.linalg.matrix_power(matrix, n - 1)
    return result[0, 0]

print(fibonacci_matrix(6)) # Output: 8
