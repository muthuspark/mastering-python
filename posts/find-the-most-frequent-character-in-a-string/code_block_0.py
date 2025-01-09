from collections import Counter

def most_frequent_char_counter(text):
  """Finds the most frequent character in a string using collections.Counter.

  Args:
    text: The input string.

  Returns:
    The most frequent character, or None if the string is empty.
  """
  if not text:
    return None
  char_counts = Counter(text)
  return char_counts.most_common(1)[0][0]


example_string = "abracadabra"
most_frequent = most_frequent_char_counter(example_string)
print(f"The most frequent character in '{example_string}' is: {most_frequent}") # Output: a

empty_string = ""
result = most_frequent_char_counter(empty_string)
print(f"Most frequent character in empty string: {result}") # Output: None
