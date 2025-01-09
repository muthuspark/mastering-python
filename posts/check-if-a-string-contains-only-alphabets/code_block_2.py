def is_alphabetical_loop(text):
  """Checks if a string contains only alphabets using a loop.

  Args:
    text: The input string.

  Returns:
    True if the string contains only alphabets, False otherwise.
  """
  for char in text:
    if not char.isalpha():
      return False
  return True


#Examples (same as above for comparison)
string1 = "HelloWorld"
string2 = "Hello123World"
string3 = "hello world"

print(f"'{string1}' contains only alphabets: {is_alphabetical_loop(string1)}") #True
print(f"'{string2}' contains only alphabets: {is_alphabetical_loop(string2)}") #False
print(f"'{string3}' contains only alphabets: {is_alphabetical_loop(string3)}") #False