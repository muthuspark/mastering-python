def count_vowels_loop(input_string):
  """Counts vowels (a, e, i, o, u) in a string using a loop.

  Args:
    input_string: The string to process.

  Returns:
    The number of vowels in the string.
  """
  vowels = "aeiouAEIOU"
  vowel_count = 0
  for char in input_string:
    if char in vowels:
      vowel_count += 1
  return vowel_count

string = "Hello, World!"
vowel_count = count_vowels_loop(string)
print(f"The number of vowels in '{string}' is: {vowel_count}")