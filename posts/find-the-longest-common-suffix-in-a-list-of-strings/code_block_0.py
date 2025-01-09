def longest_common_suffix_iterative(strings):
    """
    Finds the longest common suffix of a list of strings using an iterative approach.

    Args:
        strings: A list of strings.

    Returns:
        The longest common suffix string.  Returns an empty string if no common suffix exists.
    """
    if not strings:
        return ""

    shortest_string = min(strings, key=len)  # Start with the shortest string
    suffix = ""
    for i in range(len(shortest_string) - 1, -1, -1):
        char = shortest_string[i]
        is_common = all(string[i] == char for string in strings) #check if character at index 'i' is common to all strings
        if is_common:
            suffix = char + suffix # add the common character to the beginning of the suffix
        else:
            break  # Stop if a character is not common

    return suffix


strings1 = ["flowerpower", "superpower", "waterpower"]
print(f"Longest common suffix of {strings1}: {longest_common_suffix_iterative(strings1)}")  # Output: power

strings2 = ["apple", "banana", "orange"]
print(f"Longest common suffix of {strings2}: {longest_common_suffix_iterative(strings2)}")  # Output: 

strings3 = ["coding", "codingisfun", "codingisawesome"]
print(f"Longest common suffix of {strings3}: {longest_common_suffix_iterative(strings3)}") # Output: coding

strings4 = []
print(f"Longest common suffix of {strings4}: {longest_common_suffix_iterative(strings4)}") #Output: ""