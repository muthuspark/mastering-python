def factorial(n):
  """
  This function calculates the factorial of a non-negative integer using recursion.
  """
  if n == 0:  # Base case: factorial of 0 is 1
    return 1
  else:
    return n * factorial(n - 1)  # Recursive step

print(factorial(5))  # Output: 120