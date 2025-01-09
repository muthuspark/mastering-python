def sum_n_iterative(n):
  """
  Calculates the sum of the first n natural numbers using a for loop.

  Args:
    n: The number of natural numbers to sum.

  Returns:
    The sum of the first n natural numbers. Returns 0 if n is 0 or negative.
  """
  if n <= 0:
    return 0
  total = 0
  for i in range(1, n + 1):
    total += i
  return total

print(sum_n_iterative(5))  # Output: 15
print(sum_n_iterative(100)) # Output: 5050