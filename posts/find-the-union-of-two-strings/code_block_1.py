def string_union_iterative(str1, str2):
    """Finds the union of two strings iteratively.

    Args:
      str1: The first string.
      str2: The second string.

    Returns:
      A string containing the unique characters from both input strings, in order of first appearance.
    """
    union_string = ""
    seen_chars = set()

    for char in str1:
        if char not in seen_chars:
            union_string += char
            seen_chars.add(char)

    for char in str2:
        if char not in seen_chars:
            union_string += char
            seen_chars.add(char)

    return union_string

string1 = "hello"
string2 = "world"
result = string_union_iterative(string1, string2)
print(f"The union of '{string1}' and '{string2}' is: {result}") # Output: helloworld

