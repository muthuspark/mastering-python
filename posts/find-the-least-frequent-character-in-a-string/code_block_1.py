def least_frequent_char_dict(text):
    """Finds the least frequent character in a string using a dictionary.

    Args:
        text: The input string.

    Returns:
        The least frequent character. Returns None if the string is empty.
    """
    if not text:
        return None
    char_counts = {}
    for char in text:
        char_counts[char] = char_counts.get(char, 0) + 1

    min_count = float('inf')
    least_frequent = None
    for char, count in char_counts.items():
        if count < min_count:
            min_count = count
            least_frequent = char
    return least_frequent

string1 = "programming"
least_frequent = least_frequent_char_dict(string1)
print(f"The least frequent character in '{string1}' is: {least_frequent}")

string2 = "abcabcabc"
least_frequent = least_frequent_char_dict(string2)
print(f"The least frequent character in '{string2}' is: {least_frequent}")

string3 = ""
least_frequent = least_frequent_char_dict(string3)
print(f"The least frequent character in '{string3}' is: {least_frequent}")