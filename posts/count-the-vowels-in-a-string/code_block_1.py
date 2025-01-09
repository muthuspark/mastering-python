def count_vowels_count(input_string):
    """Counts vowels using the string count() method.

    Args:
      input_string: The string to process.

    Returns:
      The number of vowels in the string.
    """
    vowels = "aeiouAEIOU"
    total_vowels = 0
    for vowel in vowels:
        total_vowels += input_string.lower().count(vowel) #Lowercase for case-insensitivity
    return total_vowels


#Example Usage
string = "Hello, World!"
vowel_count = count_vowels_count(string)
print(f"The number of vowels in '{string}' is: {vowel_count}")