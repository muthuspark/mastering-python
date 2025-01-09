def is_alphabetical(text):
  """Checks if a string contains only alphabets using isalpha().

  Args:
    text: The input string.

  Returns:
    True if the string contains only alphabets, False otherwise.
  """
  return text.isalpha()

#Examples
string1 = "HelloWorld"
string2 = "Hello123World"
string3 = "hello world"


print(f"'{string1}' contains only alphabets: {is_alphabetical(string1)}") #True
print(f"'{string2}' contains only alphabets: {is_alphabetical(string2)}") #False
print(f"'{string3}' contains only alphabets: {is_alphabetical(string3)}") #False
