def check_lowercase_loop(input_string):
  """Checks if a string contains only lowercase letters using a loop.

  Args:
    input_string: The string to check.

  Returns:
    True if the string contains only lowercase letters, False otherwise.
  """
  for char in input_string:
    if not char.islower():
      return False
  return True

print(check_lowercase_loop("hello"))  # Output: True
print(check_lowercase_loop("Hello"))  # Output: False
print(check_lowercase_loop("hello world")) # Output: False
print(check_lowercase_loop("123")) # Output: False
