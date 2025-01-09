def replace_vowels_simple(input_string, replacement_char):
  """Replaces vowels (a, e, i, o, u) in a string with a specified character.

  Args:
    input_string: The string to modify.
    replacement_char: The character to replace vowels with.

  Returns:
    The modified string with vowels replaced.
  """
  vowels = "aeiouAEIOU"
  for vowel in vowels:
    input_string = input_string.replace(vowel, replacement_char)
  return input_string

input_str = "Hello, World!"
replaced_str = replace_vowels_simple(input_str, '*')
print(f"Original string: {input_str}")
print(f"Modified string: {replaced_str}")