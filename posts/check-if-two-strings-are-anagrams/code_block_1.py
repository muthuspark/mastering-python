from collections import Counter

def are_anagrams_counter(str1, str2):
  """Checks if two strings are anagrams using Counter.

  Args:
    str1: The first string.
    str2: The second string.

  Returns:
    True if the strings are anagrams, False otherwise.
  """
  return Counter(str1) == Counter(str2)

print(are_anagrams_counter("listen", "silent"))  # Output: True
print(are_anagrams_counter("hello", "world"))  # Output: False