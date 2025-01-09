import string

def remove_punctuation_string(text):
  """Removes punctuation from a string using string.punctuation and translate().

  Args:
    text: The input string.

  Returns:
    The string with punctuation removed.
  """
  translator = str.maketrans('', '', string.punctuation)
  return text.translate(translator)

text = "Hello, world! This is a test string."
cleaned_text = remove_punctuation_string(text)
print(f"Original text: {text}")
print(f"Cleaned text: {cleaned_text}")