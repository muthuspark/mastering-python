def is_power_of_two_division(n):
  """Checks if n is a power of two using repeated division.

  Args:
    n: The number to check.

  Returns:
    True if n is a power of two, False otherwise.
  """
  if n <= 0:
    return False
  while n % 2 == 0:
    n //= 2
  return n == 1

print(is_power_of_two_division(16))  # True
print(is_power_of_two_division(10))  # False
print(is_power_of_two_division(0))   # False
print(is_power_of_two_division(-8))  # False