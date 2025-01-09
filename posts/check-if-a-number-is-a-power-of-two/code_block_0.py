def is_power_of_two_bitwise(n):
  """Checks if n is a power of two using bit manipulation.

  Args:
    n: The number to check.

  Returns:
    True if n is a power of two, False otherwise.
  """
  if n <= 0:
    return False
  return (n & (n - 1)) == 0

print(is_power_of_two_bitwise(16))  # True
print(is_power_of_two_bitwise(10))  # False
print(is_power_of_two_bitwise(0))   # False
print(is_power_of_two_bitwise(-8))  # False
