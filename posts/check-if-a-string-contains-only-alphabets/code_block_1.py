import re

def is_alphabetical_regex(text):
  """Checks if a string contains only alphabets using regular expressions.

  Args:
    text: The input string.

  Returns:
    True if the string contains only alphabets, False otherwise.
  """
  return bool(re.fullmatch(r"[a-zA-Z]+", text))


#Examples (same as above for comparison)
string1 = "HelloWorld"
string2 = "Hello123World"
string3 = "hello world"

print(f"'{string1}' contains only alphabets: {is_alphabetical_regex(string1)}") #True
print(f"'{string2}' contains only alphabets: {is_alphabetical_regex(string2)}") #False
print(f"'{string3}' contains only alphabets: {is_alphabetical_regex(string3)}") #False
