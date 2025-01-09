def is_all_uppercase(input_string):
  """Checks if a string contains only uppercase letters using isupper().

  Args:
    input_string: The string to check.

  Returns:
    True if the string contains only uppercase letters, False otherwise.
  """
  return input_string.isupper()

string1 = "HELLO"
string2 = "Hello World"
string3 = "123ABC"

print(f"'{string1}' is all uppercase: {is_all_uppercase(string1)}") # Output: True
print(f"'{string2}' is all uppercase: {is_all_uppercase(string2)}") # Output: False
print(f"'{string3}' is all uppercase: {is_all_uppercase(string3)}") # Output: False