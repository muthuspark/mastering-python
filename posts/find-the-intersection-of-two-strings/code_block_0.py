def intersection_using_sets(str1, str2):
  """Finds the intersection of two strings using sets.

  Args:
    str1: The first string.
    str2: The second string.

  Returns:
    A string containing the common characters, sorted alphabetically.  Returns an empty string if no common characters are found.
  """
  set1 = set(str1)
  set2 = set(str2)
  common_chars = set1 & set2
  return "".join(sorted(common_chars))

string1 = "hello"
string2 = "world"
result = intersection_using_sets(string1, string2)
print(f"The intersection of '{string1}' and '{string2}' is: {result}") # Output: lo

string3 = "python"
string4 = "programming"
result = intersection_using_sets(string3, string4)
print(f"The intersection of '{string3}' and '{string4}' is: {result}") #Output: gnopr
