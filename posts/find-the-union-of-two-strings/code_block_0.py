def string_union_sets(str1, str2):
  """Finds the union of two strings using sets.

  Args:
    str1: The first string.
    str2: The second string.

  Returns:
    A string containing the unique characters from both input strings, 
    preserving the original order as much as possible.  Returns an empty
    string if both inputs are empty.
  """
  combined_set = set(str1) | set(str2) #Union operation on sets
  union_string = "".join(sorted(combined_set, key=lambda x: str1.find(x) if x in str1 else str2.find(x)))
  return union_string


string1 = "hello"
string2 = "world"
result = string_union_sets(string1, string2)
print(f"The union of '{string1}' and '{string2}' is: {result}") # Output will vary slightly depending on Python implementation


string3 = ""
string4 = "test"
result = string_union_sets(string3, string4)
print(f"The union of '{string3}' and '{string4}' is: {result}") # Output: test

string5 = "apple"
string6 = "banana"
result = string_union_sets(string5, string6)
print(f"The union of '{string5}' and '{string6}' is: {result}") # Output will vary slightly depending on Python implementation
