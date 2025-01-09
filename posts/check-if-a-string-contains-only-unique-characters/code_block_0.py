def unique_chars_set(input_string):
  """
  Checks if a string contains only unique characters using sets.

  Args:
    input_string: The string to check.

  Returns:
    True if the string contains only unique characters, False otherwise.
  """
  return len(set(input_string)) == len(input_string)

string1 = "abcdefg"
string2 = "abacdefg"

print(f"'{string1}' has only unique characters: {unique_chars_set(string1)}")  # Output: True
print(f"'{string2}' has only unique characters: {unique_chars_set(string2)}")  # Output: False