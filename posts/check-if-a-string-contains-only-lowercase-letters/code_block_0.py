def check_lowercase_islower(input_string):
  """Checks if a string contains only lowercase letters using islower().

  Args:
    input_string: The string to check.

  Returns:
    True if the string contains only lowercase letters, False otherwise.
  """
  return input_string.islower()

print(check_lowercase_islower("hello"))  # Output: True
print(check_lowercase_islower("Hello"))  # Output: False
print(check_lowercase_islower("hello world")) # Output: False
print(check_lowercase_islower("123")) # Output: False