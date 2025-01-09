words_with_spaces = ['  apple  ', ' banana ', ' cherry ']
cleaned_words = [word.strip() for word in words_with_spaces]
joined_string = ", ".join(cleaned_words)
print(joined_string) # Output: apple, banana, cherry
