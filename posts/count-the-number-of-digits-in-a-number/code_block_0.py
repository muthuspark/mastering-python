def count_digits_loop(n):
  """Counts the number of digits in a number using a loop.

  Args:
    n: The input integer (must be non-negative).

  Returns:
    The number of digits in n.  Returns 1 if n is 0.  Raises ValueError if n is negative.
  """
  if n < 0:
    raise ValueError("Input must be a non-negative integer.")
  if n == 0:
    return 1
  count = 0
  while n > 0:
    n //= 10  # Integer division
    count += 1
  return count

#Example usage
number = 12345
digit_count = count_digits_loop(number)
print(f"The number of digits in {number} is: {digit_count}") #Output: 5

number = 0
digit_count = count_digits_loop(number)
print(f"The number of digits in {number} is: {digit_count}") #Output: 1
