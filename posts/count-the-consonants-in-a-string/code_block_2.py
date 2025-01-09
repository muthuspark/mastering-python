def count_consonants_filter(input_string):
    vowels = set('aeiouAEIOU')
    consonants = filter(lambda char: char.isalpha() and char not in vowels, input_string)
    return len(list(consonants))

#Example
string3 = "Data Science"
consonant_count = count_consonants_filter(string3)
print(f"The number of consonants in '{string3}' is: {consonant_count}") # Output: 7
