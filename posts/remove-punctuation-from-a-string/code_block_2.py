import re

def remove_punctuation_regex(text):
  """Removes punctuation from a string using regular expressions.

  Args:
    text: The input string.

  Returns:
    The string with punctuation removed.
  """
  return re.sub(r'[^\w\s]', '', text)

text = "Hello, world! This is a test string."
cleaned_text = remove_punctuation_regex(text)
print(f"Original text: {text}")
print(f"Cleaned text: {cleaned_text}")