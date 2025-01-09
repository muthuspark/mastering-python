def count_vowels_comprehension(input_string):
  """Counts vowels using list comprehension.

  Args:
    input_string: The string to process.

  Returns:
    The number of vowels in the string.
  """
  vowels = "aeiouAEIOU"
  return sum(1 for char in input_string if char in vowels)

string = "Hello, World!"
vowel_count = count_vowels_comprehension(string)
print(f"The number of vowels in '{string}' is: {vowel_count}")