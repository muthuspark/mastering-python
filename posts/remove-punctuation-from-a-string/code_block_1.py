def remove_punctuation_loop(text):
  """Removes punctuation from a string using a loop and isalnum().

  Args:
    text: The input string.

  Returns:
    The string with punctuation removed.
  """
  result = ''
  for char in text:
    if char.isalnum() or char.isspace():
      result += char
  return result

text = "Hello, world! This is a test string."
cleaned_text = remove_punctuation_loop(text)
print(f"Original text: {text}")
  print(f"Cleaned text: {cleaned_text}")