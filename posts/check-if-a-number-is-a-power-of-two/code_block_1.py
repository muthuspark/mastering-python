import math

def is_power_of_two_log(n):
  """Checks if n is a power of two using logarithms.

  Args:
    n: The number to check.

  Returns:
    True if n is a power of two, False otherwise.
  """
  if n <= 0:
      return False
  return math.log2(n).is_integer()

print(is_power_of_two_log(16))  # True
print(is_power_of_two_log(10))  # False
print(is_power_of_two_log(0))   # False
print(is_power_of_two_log(-8))  # ValueError
