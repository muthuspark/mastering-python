def sum_of_cubes_iterative(n):
  """Calculates the sum of cubes of first n natural numbers iteratively.

  Args:
    n: The number of natural numbers to consider.

  Returns:
    The sum of the cubes of the first n natural numbers.  Returns 0 if n is 0 or negative.
  """
  if n <= 0:
    return 0
  total = 0
  for i in range(1, n + 1):
    total += i**3
  return total

n = 5
result = sum_of_cubes_iterative(n)
print(f"The sum of cubes of first {n} natural numbers (iterative): {result}")  # Output: 225