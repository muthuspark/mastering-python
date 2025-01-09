def fibonacci_iterative(n):
  """
  Generates a Fibonacci sequence iteratively up to n terms.

  Args:
    n: The number of Fibonacci numbers to generate.

  Returns:
    A list containing the Fibonacci sequence.
  """
  if n <= 0:
    return []
  elif n == 1:
    return [0]
  else:
    list_fib = [0, 1]
    while len(list_fib) < n:
      next_fib = list_fib[-1] + list_fib[-2]
      list_fib.append(next_fib)
    return list_fib

print(fibonacci_iterative(10))  # Output: [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]