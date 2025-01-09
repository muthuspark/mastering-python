def sum_of_squares_formula(n):
  """
  Calculates the sum of squares of the first n natural numbers using a formula.

  Args:
    n: A positive integer.

  Returns:
    The sum of squares. Returns 0 if n is not a positive integer.
  """
  if not isinstance(n, int) or n <= 0:
    return 0
  return n * (n + 1) * (2 * n + 1) // 6

n = 5
result = sum_of_squares_formula(n)
print(f"The sum of squares of the first {n} natural numbers is: {result}") # Output: 55