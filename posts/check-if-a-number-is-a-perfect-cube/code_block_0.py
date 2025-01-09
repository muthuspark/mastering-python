import math

def is_perfect_cube_method1(n):
  """
  Checks if a number is a perfect cube using the round() function.

  Args:
    n: The number to check.

  Returns:
    True if n is a perfect cube, False otherwise.
  """
  if n < 0:
    return False # Negative numbers cannot be perfect cubes of positive integers.
  cube_root = round(n**(1/3))
  return cube_root**3 == n

print(is_perfect_cube_method1(8))   # Output: True
print(is_perfect_cube_method1(27))  # Output: True
print(is_perfect_cube_method1(10))  # Output: False
print(is_perfect_cube_method1(-8)) # Output: False
