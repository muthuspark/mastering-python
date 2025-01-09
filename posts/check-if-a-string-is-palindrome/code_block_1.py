def is_palindrome_loop(text):
  """Checks if a string is a palindrome using a loop.

  Args:
    text: The input string.

  Returns:
    True if the string is a palindrome, False otherwise. Case-insensitive.
  """
  processed_text = text.lower().replace(" ", "")
  left = 0
  right = len(processed_text) - 1

  while left < right:
    if processed_text[left] != processed_text[right]:
      return False
    left += 1
    right -= 1
  return True

#Example Usage (same output as Method 1)
print(f"'{string1}' is a palindrome: {is_palindrome_loop(string1)}")
print(f"'{string2}' is a palindrome: {is_palindrome_loop(string2)}")
print(f"'{string3}' is a palindrome: {is_palindrome_loop(string3)}")