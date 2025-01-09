def is_palindrome_recursive(text):
  """Checks if a string is a palindrome recursively.

  Args:
    text: The input string.

  Returns:
    True if the string is a palindrome, False otherwise. Case-insensitive.
  """
  processed_text = text.lower().replace(" ", "")
  if len(processed_text) <= 1:
    return True
  if processed_text[0] != processed_text[-1]:
    return False
  return is_palindrome_recursive(processed_text[1:-1])

#Example Usage (same output as Method 1 & 2)
print(f"'{string1}' is a palindrome: {is_palindrome_recursive(string1)}")
print(f"'{string2}' is a palindrome: {is_palindrome_recursive(string2)}")
print(f"'{string3}' is a palindrome: {is_palindrome_recursive(string3)}")