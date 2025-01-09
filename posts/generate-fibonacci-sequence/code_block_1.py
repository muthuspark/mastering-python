def fibonacci_recursive(n):
  """
  Generates a Fibonacci sequence recursively.

  Args:
    n: The nth Fibonacci number to generate (starting from 0).

  Returns:
    The nth Fibonacci number.
  """
  if n <= 1:
    return n
  else:
    return fibonacci_recursive(n-1) + fibonacci_recursive(n-2)

for i in range(10):
  print(fibonacci_recursive(i)) # Output: 0 1 1 2 3 5 8 13 21 34
