def remove_char_comprehension(text, char):
  """Removes all occurrences of a character from a string using list comprehension.

  Args:
    text: The input string.
    char: The character to remove.

  Returns:
    The string with all occurrences of the character removed.
  """
  return "".join([c for c in text if c != char])

string = "Hello, World!"
new_string = remove_char_comprehension(string, "l")
print(f"Original string: {string}")
print(f"String after removing 'l': {new_string}") # Output: Heo, Word!

string2 = "This is a test string!!!"
new_string2 = remove_char_comprehension(string2, "s")
print(f"Original string: {string2}")
print(f"String after removing 's': {new_string2}") # Output: Thi i a tet tring!!!