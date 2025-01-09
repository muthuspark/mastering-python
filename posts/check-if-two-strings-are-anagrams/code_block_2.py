def are_anagrams_sort(str1, str2):
  """Checks if two strings are anagrams using sorting.

  Args:
    str1: The first string.
    str2: The second string.

  Returns:
    True if the strings are anagrams, False otherwise.
  """
  return sorted(str1) == sorted(str2)

#Example usage
print(are_anagrams_sort("listen", "silent"))  # Output: True
print(are_anagrams_sort("hello", "world"))  # Output: False
