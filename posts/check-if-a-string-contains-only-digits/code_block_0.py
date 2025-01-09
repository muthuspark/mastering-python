def is_digit_string_isdigit(input_string):
  """Checks if a string contains only digits using isdigit().

  Args:
    input_string: The string to check.

  Returns:
    True if the string contains only digits, False otherwise.
  """
  return input_string.isdigit()

print(is_digit_string_isdigit("12345"))  # Output: True
print(is_digit_string_isdigit("123a45")) # Output: False
print(is_digit_string_isdigit("12 345")) # Output: False
print(is_digit_string_isdigit(""))       # Output: False
