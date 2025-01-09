from collections import Counter

def most_frequent_char_case_insensitive(text):
    """Finds the most frequent character, ignoring case."""
    text = text.lower()
    return most_frequent_char_counter(text) # reuse the efficient counter method

example_string = "Programming"
most_frequent = most_frequent_char_case_insensitive(example_string)
print(f"The most frequent character in '{example_string}' (case-insensitive) is: {most_frequent}") #Output: g
