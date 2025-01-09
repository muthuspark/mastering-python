def sum_digits_string(n):
  """
  Calculates the sum of digits of a non-negative integer using string conversion.

  Args:
    n: The non-negative integer.

  Returns:
    The sum of the digits of n. Returns 0 if n is negative.
  """
  if n < 0:
    return 0
  return sum(int(digit) for digit in str(n))

#Example Usage
number = 9876
result = sum_digits_string(number)
print(f"The sum of digits of {number} is: {result}") # Output: 30