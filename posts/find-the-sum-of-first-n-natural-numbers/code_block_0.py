def sum_n_mathematical(n):
  """
  Calculates the sum of the first n natural numbers using the mathematical formula.

  Args:
    n: The number of natural numbers to sum.

  Returns:
    The sum of the first n natural numbers.  Returns 0 if n is 0 or negative.
  """
  if n <= 0:
    return 0
  return n * (n + 1) // 2

#Example Usage
print(sum_n_mathematical(5))  # Output: 15
print(sum_n_mathematical(100)) # Output: 5050