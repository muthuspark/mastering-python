def intersection_using_loops(str1, str2):
  """Finds the intersection of two strings using nested loops.

  Args:
    str1: The first string.
    str2: The second string.

  Returns:
    A string containing the common characters, sorted alphabetically. Returns an empty string if no common characters are found.
  """
  common_chars = ""
  for char1 in str1:
    if char1 in str2 and char1 not in common_chars:
      common_chars += char1
  return "".join(sorted(common_chars))

string1 = "hello"
string2 = "world"
result = intersection_using_loops(string1, string2)
print(f"The intersection of '{string1}' and '{string2}' is: {result}") # Output: lo