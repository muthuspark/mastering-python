def fibonacci_recursive(n):
  """
  Calculates the nth Fibonacci number recursively.

  Args:
    n: The index of the desired Fibonacci number (starting from 0).

  Returns:
    The nth Fibonacci number.
  """
  if n <= 1:
    return n
  else:
    return fibonacci_recursive(n-1) + fibonacci_recursive(n-2)

print(fibonacci_recursive(6))  # Output: 8