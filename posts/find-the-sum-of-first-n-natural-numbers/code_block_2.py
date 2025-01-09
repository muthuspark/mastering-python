def sum_n_recursive(n):
  """
  Calculates the sum of the first n natural numbers recursively.

  Args:
    n: The number of natural numbers to sum.

  Returns:
    The sum of the first n natural numbers. Returns 0 if n is 0 or negative.
  """
  if n <= 0:
    return 0
  elif n == 1:
    return 1
  else:
    return n + sum_n_recursive(n - 1)

print(sum_n_recursive(5))  # Output: 15
print(sum_n_recursive(100)) # Output: 5050
