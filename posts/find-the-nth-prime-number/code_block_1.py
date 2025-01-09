def find_nth_prime_sieve(n):
  """Finds the nth prime number using the Sieve of Eratosthenes."""
  limit = n * 20  # Adjust limit as needed for larger n; this is a heuristic
  primes = [True] * (limit + 1)
  primes[0] = primes[1] = False

  for i in range(2, int(limit**0.5) + 1):
    if primes[i]:
      for j in range(i * i, limit + 1, i):
        primes[j] = False

  count = 0
  for i in range(2, limit + 1):
    if primes[i]:
      count += 1
      if count == n:
        return i

nth = 100
prime = find_nth_prime_sieve(nth)
print(f"The {nth}th prime number is: {prime}")
