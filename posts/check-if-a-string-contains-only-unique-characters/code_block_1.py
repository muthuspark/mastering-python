def unique_chars_dict(input_string):
  """
  Checks if a string contains only unique characters using dictionaries.

  Args:
    input_string: The string to check.

  Returns:
    True if the string contains only unique characters, False otherwise.
  """
  char_counts = {}
  for char in input_string:
    if char in char_counts:
      return False  # Duplicate character found
    char_counts[char] = 1
  return True

string1 = "abcdefg"
string2 = "abacdefg"

print(f"'{string1}' has only unique characters: {unique_chars_dict(string1)}")  # Output: True
print(f"'{string2}' has only unique characters: {unique_chars_dict(string2)}")  # Output: False