def unique_chars_manual(input_string):
  """
  Checks if a string contains only unique characters using manual comparison.  (Less efficient)

  Args:
    input_string: The string to check.

  Returns:
    True if the string contains only unique characters, False otherwise.
  """
  for i in range(len(input_string)):
    for j in range(i + 1, len(input_string)):
      if input_string[i] == input_string[j]:
        return False  # Duplicate character found
  return True

string1 = "abcdefg"
string2 = "abacdefg"

print(f"'{string1}' has only unique characters: {unique_chars_manual(string1)}")  # Output: True
print(f"'{string2}' has only unique characters: {unique_chars_manual(string2)}")  # Output: False