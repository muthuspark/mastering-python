import re

def replace_vowels_regex(input_string, replacement_char):
  """Replaces vowels using regular expressions."""
  return re.sub(r"[aeiouAEIOU]", replacement_char, input_string)


input_str = "Hello, World!"
replaced_str = replace_vowels_regex(input_str, '*')
print(f"Original string: {input_str}")
print(f"Modified string: {replaced_str}")