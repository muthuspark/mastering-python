def is_prime(num):
  """Checks if a number is prime."""
  if num <= 1:
    return False
  for i in range(2, int(num**0.5) + 1):
    if num % i == 0:
      return False
  return True

def find_nth_prime(n):
  """Finds the nth prime number."""
  count = 0
  number = 2
  while count < n:
    if is_prime(number):
      count += 1
    number += 1
  return number - 1

nth = 10
prime = find_nth_prime(nth)
print(f"The {nth}th prime number is: {prime}")