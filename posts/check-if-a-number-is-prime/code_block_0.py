def is_prime_naive(n):
  """Checks if a number is prime using a naive approach.

  Args:
    n: The number to check.

  Returns:
    True if n is prime, False otherwise.
  """
  if n <= 1:
    return False
  for i in range(2, n):
    if n % i == 0:
      return False
  return True

print(is_prime_naive(7))  # Output: True
print(is_prime_naive(15)) # Output: False