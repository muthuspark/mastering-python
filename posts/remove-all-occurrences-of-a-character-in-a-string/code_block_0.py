def remove_char_replace(text, char):
  """Removes all occurrences of a character from a string using replace().

  Args:
    text: The input string.
    char: The character to remove.

  Returns:
    The string with all occurrences of the character removed.
  """
  return text.replace(char, "")

string = "Hello, World!"
new_string = remove_char_replace(string, "o")
print(f"Original string: {string}")
print(f"String after removing 'o': {new_string}") # Output: Hell, Wrld!

string2 = "This is a test string!!!"
new_string2 = remove_char_replace(string2, "!")
print(f"Original string: {string2}")
print(f"String after removing '!': {new_string2}") # Output: This is a test string