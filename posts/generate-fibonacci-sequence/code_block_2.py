def fibonacci_generator(n):
  """
  Generates a Fibonacci sequence using a generator.

  Args:
    n: The number of Fibonacci numbers to generate.

  Yields:
    The next Fibonacci number in the sequence.
  """
  a, b = 0, 1
  for _ in range(n):
    yield a
    a, b = b, a + b

for i in fibonacci_generator(10):
  print(i) # Output: 0 1 1 2 3 5 8 13 21 34