import math

def count_digits_log(n):
  """Counts the number of digits in a number using logarithms.

  Args:
    n: The input integer (must be positive).

  Returns:
    The number of digits in n. Raises ValueError if n is not positive.
  """
  if n <= 0:
    raise ValueError("Input must be a positive integer.")
  return math.floor(math.log10(n)) + 1

number = 12345
digit_count = count_digits_log(number)
print(f"The number of digits in {number} is: {digit_count}") # Output: 5
