def string_length_recursive(input_string):
  """Calculates the length of a string recursively.

  Args:
    input_string: The string whose length needs to be determined.

  Returns:
    The length of the string as an integer. Returns 0 for an empty string.
  """
  if not input_string:
    return 0
  else:
    return 1 + string_length_recursive(input_string[1:])

my_string = "Python"
length = string_length_recursive(my_string)
print(f"The length of '{my_string}' is: {length}")  # Output: The length of 'Python' is: 6