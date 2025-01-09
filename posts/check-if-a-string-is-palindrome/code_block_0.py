def is_palindrome_slicing(text):
  """Checks if a string is a palindrome using string slicing.

  Args:
    text: The input string.

  Returns:
    True if the string is a palindrome, False otherwise.  Case-insensitive.
  """
  processed_text = text.lower().replace(" ", "") #ignore case and spaces
  return processed_text == processed_text[::-1]

string1 = "racecar"
string2 = "A man, a plan, a canal: Panama"
string3 = "hello"

print(f"'{string1}' is a palindrome: {is_palindrome_slicing(string1)}") #True
print(f"'{string2}' is a palindrome: {is_palindrome_slicing(string2)}") #True
print(f"'{string3}' is a palindrome: {is_palindrome_slicing(string3)}") #False
