def is_all_uppercase_loop(input_string):
  """Checks if a string contains only uppercase letters using a loop and isupper().

  Args:
    input_string: The string to check.

  Returns:
    True if the string contains only uppercase letters, False otherwise.  Returns True for empty strings.
  """
  for char in input_string:
    if not char.isupper():
      return False
  return True

string1 = "HELLO"
string2 = "Hello World"
string3 = "123ABC"
string4 = ""

print(f"'{string1}' is all uppercase: {is_all_uppercase_loop(string1)}") # Output: True
print(f"'{string2}' is all uppercase: {is_all_uppercase_loop(string2)}") # Output: False
print(f"'{string3}' is all uppercase: {is_all_uppercase_loop(string3)}") # Output: False
print(f"'{string4}' is all uppercase: {is_all_uppercase_loop(string4)}") # Output: True
