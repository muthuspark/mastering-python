import math

def is_prime_optimized(n):
  """Checks if a number is prime with optimization up to the square root.

  Args:
    n: The number to check.

  Returns:
    True if n is prime, False otherwise.
  """
  if n <= 1:
    return False
  if n == 2:
    return True
  if n % 2 == 0:
    return False
  for i in range(3, int(math.sqrt(n)) + 1, 2):
    if n % i == 0:
      return False
  return True

print(is_prime_optimized(97)) # Output: True
print(is_prime_optimized(100))# Output: False
