import re

def is_all_uppercase_regex(input_string):
  """Checks if a string contains only uppercase letters using regular expressions.

  Args:
    input_string: The string to check.

  Returns:
    True if the string contains only uppercase letters, False otherwise. Returns True for empty strings.
  """
  return bool(re.fullmatch(r"[A-Z]*", input_string))

string1 = "HELLO"
string2 = "Hello World"
string3 = "123ABC"
string4 = ""

print(f"'{string1}' is all uppercase: {is_all_uppercase_regex(string1)}") # Output: True
print(f"'{string2}' is all uppercase: {is_all_uppercase_regex(string2)}") # Output: False
print(f"'{string3}' is all uppercase: {is_all_uppercase_regex(string3)}") # Output: False
print(f"'{string4}' is all uppercase: {is_all_uppercase_regex(string4)}") # Output: True