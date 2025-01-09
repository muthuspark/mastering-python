def factorial_iterative(n):
  """
  Calculates the factorial of a non-negative integer using iteration.

  Args:
    n: The non-negative integer.

  Returns:
    The factorial of n.  Returns 1 if n is 0.
    Raises ValueError if n is negative.
  """
  if n < 0:
    raise ValueError("Factorial is not defined for negative numbers.")
  elif n == 0:
    return 1
  else:
    result = 1
    for i in range(1, n + 1):
      result *= i
    return result

print(factorial_iterative(5))  # Output: 120
print(factorial_iterative(0))  # Output: 1