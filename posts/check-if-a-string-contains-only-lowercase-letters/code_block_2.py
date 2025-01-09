import re

def check_lowercase_regex(input_string):
  """Checks if a string contains only lowercase letters using regular expressions.

  Args:
    input_string: The string to check.

  Returns:
    True if the string contains only lowercase letters, False otherwise.
  """
  return bool(re.fullmatch(r"[a-z]+", input_string))


print(check_lowercase_regex("hello"))  # Output: True
print(check_lowercase_regex("Hello"))  # Output: False
print(check_lowercase_regex("hello world")) # Output: False
print(check_lowercase_regex("123")) # Output: False