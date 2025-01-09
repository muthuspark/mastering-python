def replace_vowels_comprehension(input_string, replacement_char):
  """Replaces vowels using list comprehension."""
  vowels = "aeiouAEIOU"
  return "".join([replacement_char if char in vowels else char for char in input_string])

input_str = "Hello, World!"
replaced_str = replace_vowels_comprehension(input_str, '*')
print(f"Original string: {input_str}")
print(f"Modified string: {replaced_str}")
