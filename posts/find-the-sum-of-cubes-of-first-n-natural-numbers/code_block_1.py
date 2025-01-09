def sum_of_cubes_formula(n):
  """Calculates the sum of cubes of first n natural numbers using the formula.

  Args:
    n: The number of natural numbers to consider.

  Returns:
    The sum of the cubes of the first n natural numbers. Returns 0 if n is 0 or negative.
  """
  if n <= 0:
    return 0
  return (n * (n + 1) // 2)**2

n = 5
result = sum_of_cubes_formula(n)
print(f"The sum of cubes of first {n} natural numbers (formula): {result}")  # Output: 225

n = 1000
result = sum_of_cubes_formula(n)
print(f"The sum of cubes of first {n} natural numbers (formula): {result}") # Output: 250500250000