def sum_digits_iterative(n):
  """
  Calculates the sum of digits of a non-negative integer iteratively.

  Args:
    n: The non-negative integer.

  Returns:
    The sum of the digits of n.  Returns 0 if n is negative.
  """
  if n < 0:
    return 0
  sum_of_digits = 0
  while n > 0:
    digit = n % 10
    sum_of_digits += digit
    n //= 10
  return sum_of_digits

#Example Usage
number = 12345
result = sum_digits_iterative(number)
print(f"The sum of digits of {number} is: {result}") #Output: 15

number = -123
result = sum_digits_iterative(number)
print(f"The sum of digits of {number} is: {result}") #Output: 0
