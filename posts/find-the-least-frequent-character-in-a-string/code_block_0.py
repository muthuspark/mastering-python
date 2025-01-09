from collections import Counter

def least_frequent_char_counter(text):
    """Finds the least frequent character in a string using Counter.

    Args:
        text: The input string.

    Returns:
        The least frequent character.  Returns None if the string is empty.
    """
    if not text:
        return None
    char_counts = Counter(text)
    least_frequent = min(char_counts, key=char_counts.get)
    return least_frequent

#Example Usage
string1 = "programming"
least_frequent = least_frequent_char_counter(string1)
print(f"The least frequent character in '{string1}' is: {least_frequent}") #Output: The least frequent character in 'programming' is: g


string2 = "abcabcabc"
least_frequent = least_frequent_char_counter(string2)
print(f"The least frequent character in '{string2}' is: {least_frequent}") #Output: The least frequent character in 'abcabcabc' is: a

string3 = ""
least_frequent = least_frequent_char_counter(string3)
print(f"The least frequent character in '{string3}' is: {least_frequent}") #Output: The least frequent character in '' is: None
