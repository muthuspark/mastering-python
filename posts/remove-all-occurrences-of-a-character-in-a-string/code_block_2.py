def remove_char_filter(text, char):
  """Removes all occurrences of a character from a string using filter().

  Args:
    text: The input string.
    char: The character to remove.

  Returns:
    The string with all occurrences of the character removed.
  """
  return "".join(filter(lambda c: c != char, text))

string = "Hello, World!"
new_string = remove_char_filter(string, ",")
print(f"Original string: {string}")
print(f"String after removing ',': {new_string}") # Output: Hello World!

string2 = "This is a test string!!!"
new_string2 = remove_char_filter(string2, "t")
print(f"Original string: {string2}")
print(f"String after removing 't': {new_string2}") # Output: This i a es string!!!