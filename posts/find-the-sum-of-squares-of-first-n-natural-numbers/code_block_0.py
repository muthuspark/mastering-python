def sum_of_squares_iterative(n):
  """
  Calculates the sum of squares of the first n natural numbers iteratively.

  Args:
    n: A positive integer.

  Returns:
    The sum of squares.  Returns 0 if n is not a positive integer.
  """
  if not isinstance(n, int) or n <= 0:
    return 0
  total = 0
  for i in range(1, n + 1):
    total += i**2
  return total

n = 5
result = sum_of_squares_iterative(n)
print(f"The sum of squares of the first {n} natural numbers is: {result}") # Output: 55