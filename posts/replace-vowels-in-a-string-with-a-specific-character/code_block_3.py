def replace_vowels_translate(input_string, replacement_char):
    """Replaces vowels using str.maketrans() and translate()."""
    vowels = "aeiouAEIOU"
    translation_table = str.maketrans(vowels, replacement_char * len(vowels))
    return input_string.translate(translation_table)

input_str = "Hello, World!"
replaced_str = replace_vowels_translate(input_str, '*')
print(f"Original string: {input_str}")
print(f"Modified string: {replaced_str}")