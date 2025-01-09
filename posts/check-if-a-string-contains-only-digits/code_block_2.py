def is_digit_string_loop(input_string):
  """Checks if a string contains only digits using a loop and isdigit().

  Args:
    input_string: The string to check.

  Returns:
    True if the string contains only digits, False otherwise.
  """
  for char in input_string:
    if not char.isdigit():
      return False
  return True

print(is_digit_string_loop("12345"))  # Output: True
print(is_digit_string_loop("123a45")) # Output: False
print(is_digit_string_loop("12 345")) # Output: False
print(is_digit_string_loop(""))       # Output: True