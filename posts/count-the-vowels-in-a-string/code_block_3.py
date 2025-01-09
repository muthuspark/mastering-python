import re

def count_vowels_regex(input_string):
    """Counts vowels using regular expressions.

    Args:
      input_string: The string to process.

    Returns:
      The number of vowels in the string.
    """
    return len(re.findall(r'[aeiouAEIOU]', input_string))

string = "Hello, World!"
vowel_count = count_vowels_regex(string)
print(f"The number of vowels in '{string}' is: {vowel_count}")
