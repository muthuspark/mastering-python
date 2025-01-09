import math

def is_perfect_square_isqrt(n):
  """Checks if n is a perfect square using math.isqrt().

  Args:
    n: The number to check.  Must be a non-negative integer.

  Returns:
    True if n is a perfect square, False otherwise.
  """
  if n < 0:
    return False  # Handle negative numbers
  root = math.isqrt(n)
  return root * root == n

print(is_perfect_square_isqrt(16))  # Output: True
print(is_perfect_square_isqrt(17))  # Output: False
print(is_perfect_square_isqrt(0))   # Output: True
print(is_perfect_square_isqrt(-4))  # Output: False
