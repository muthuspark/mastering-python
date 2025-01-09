def factorial_recursive(n):
  """
  Calculates the factorial of a non-negative integer using recursion.

  Args:
    n: The non-negative integer.

  Returns:
    The factorial of n. Returns 1 if n is 0.
    Raises ValueError if n is negative.
  """
  if n < 0:
    raise ValueError("Factorial is not defined for negative numbers.")
  elif n == 0:
    return 1
  else:
    return n * factorial_recursive(n - 1)

print(factorial_recursive(5))  # Output: 120
print(factorial_recursive(0))  # Output: 1