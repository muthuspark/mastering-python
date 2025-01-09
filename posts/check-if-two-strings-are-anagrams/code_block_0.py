def are_anagrams_dict(str1, str2):
  """Checks if two strings are anagrams using dictionaries.

  Args:
    str1: The first string.
    str2: The second string.

  Returns:
    True if the strings are anagrams, False otherwise.
  """
  if len(str1) != len(str2):
    return False

  char_count1 = {}
  char_count2 = {}

  for char in str1:
    char_count1[char] = char_count1.get(char, 0) + 1

  for char in str2:
    char_count2[char] = char_count2.get(char, 0) + 1

  return char_count1 == char_count2

#Example usage
print(are_anagrams_dict("listen", "silent"))  # Output: True
print(are_anagrams_dict("hello", "world"))  # Output: False
