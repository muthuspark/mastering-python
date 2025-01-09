def sum_digits_recursive(n):
  """
  Calculates the sum of digits of a non-negative integer recursively.

  Args:
    n: The non-negative integer.

  Returns:
    The sum of the digits of n. Returns 0 if n is negative.
  """
  if n < 0:
    return 0
  if n < 10:
    return n
  else:
    return (n % 10) + sum_digits_recursive(n // 10)

#Example Usage
number = 54321
result = sum_digits_recursive(number)
print(f"The sum of digits of {number} is: {result}") # Output: 15
