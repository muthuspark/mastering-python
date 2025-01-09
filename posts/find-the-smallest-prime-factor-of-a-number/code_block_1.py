def is_prime(n):
    """Checks if a number is prime."""
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def smallest_prime_factor_optimized(n):
  """Finds the smallest prime factor using optimized iteration and prime checking."""
  if not isinstance(n, int) or n <= 0:
      raise ValueError("Input must be a positive integer.")
  if n == 1:
      return 1
  for i in range(2, n + 1):
      if is_prime(i) and n % i == 0:
          return i

print(smallest_prime_factor_optimized(12))  # Output: 2
print(smallest_prime_factor_optimized(35))  # Output: 5
print(smallest_prime_factor_optimized(17))  # Output: 17
print(smallest_prime_factor_optimized(1)) # Output: 1