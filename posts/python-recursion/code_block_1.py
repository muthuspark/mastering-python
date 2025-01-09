def fibonacci(n):
  """
  This function calculates the nth Fibonacci number using recursion.
  """
  if n <= 1:  # Base case: 0th and 1st Fibonacci numbers are 0 and 1 respectively.
    return n
  else:
    return fibonacci(n-1) + fibonacci(n-2)  # Recursive step

print(fibonacci(6))  # Output: 8