def count_digits_string(n):
  """Counts the number of digits in a number using string conversion.

  Args:
    n: The input integer (must be non-negative).

  Returns:
    The number of digits in n. Returns 1 if n is 0. Raises ValueError if n is negative.
  """
  if n < 0:
    raise ValueError("Input must be a non-negative integer.")
  return len(str(n))

number = 12345
digit_count = count_digits_string(number)
print(f"The number of digits in {number} is: {digit_count}") # Output: 5

number = 0
digit_count = count_digits_string(number)
print(f"The number of digits in {number} is: {digit_count}") # Output: 1