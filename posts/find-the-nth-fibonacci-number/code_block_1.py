def fibonacci_iterative(n):
  """
  Calculates the nth Fibonacci number iteratively.

  Args:
    n: The index of the desired Fibonacci number (starting from 0).

  Returns:
    The nth Fibonacci number.
  """
  a, b = 0, 1
  for _ in range(n):
    a, b = b, a + b
  return a

print(fibonacci_iterative(6))  # Output: 8