import re

def is_digit_string_regex(input_string):
  """Checks if a string contains only digits using regular expressions.

  Args:
    input_string: The string to check.

  Returns:
    True if the string contains only digits, False otherwise.
  """
  return bool(re.fullmatch(r"\d+", input_string))

print(is_digit_string_regex("12345"))  # Output: True
print(is_digit_string_regex("123a45")) # Output: False
print(is_digit_string_regex("12 345")) # Output: False
print(is_digit_string_regex(""))       # Output: False