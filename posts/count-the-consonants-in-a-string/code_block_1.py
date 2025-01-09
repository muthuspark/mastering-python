def count_consonants_comprehension(input_string):
    vowels = set('aeiouAEIOU')
    consonant_count = sum(1 for char in input_string if char.isalpha() and char not in vowels)
    return consonant_count


#Example
string2 = "Python Programming"
consonant_count = count_consonants_comprehension(string2)
print(f"The number of consonants in '{string2}' is: {consonant_count}") # Output: 12
