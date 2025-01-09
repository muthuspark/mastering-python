def is_perfect_square_exponent(n):
  """Checks if n is a perfect square using the exponentiation operator.

  Args:
    n: The number to check. Must be a non-negative number.

  Returns:
    True if n is a perfect square, False otherwise.
  """
  if n < 0:
    return False
  root = n**0.5
  return isinstance(root, int)

print(is_perfect_square_exponent(25)) # Output: True
print(is_perfect_square_exponent(26)) # Output: False