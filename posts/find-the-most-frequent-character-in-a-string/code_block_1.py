def most_frequent_char_dict(text):
  """Finds the most frequent character using a dictionary.

  Args:
    text: The input string.

  Returns:
    The most frequent character, or None if the string is empty.
  """
  if not text:
    return None
  char_counts = {}
  for char in text:
    char_counts[char] = char_counts.get(char, 0) + 1

  max_char = None
  max_count = 0
  for char, count in char_counts.items():
    if count > max_count:
      max_count = count
      max_char = char
  return max_char

example_string = "programming"
most_frequent = most_frequent_char_dict(example_string)
print(f"The most frequent character in '{example_string}' is: {most_frequent}") # Output: g
