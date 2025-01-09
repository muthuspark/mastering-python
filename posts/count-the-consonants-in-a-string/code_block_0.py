def count_consonants_loop(input_string):
    vowels = set('aeiouAEIOU')
    consonant_count = 0
    for char in input_string:
        if char.isalpha() and char not in vowels:
            consonant_count += 1
    return consonant_count

#Example
string1 = "Hello, World!"
consonant_count = count_consonants_loop(string1)
print(f"The number of consonants in '{string1}' is: {consonant_count}") #Output: 7
