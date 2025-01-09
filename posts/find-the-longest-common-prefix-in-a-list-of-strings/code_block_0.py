def longestCommonPrefix_charByChar(strs):
    """
    Finds the longest common prefix using character-by-character comparison.

    Args:
        strs: A list of strings.

    Returns:
        The longest common prefix string.
    """
    if not strs:
        return ""

    prefix = ""
    shortest_str = min(strs, key=len)  # Find the shortest string for efficiency

    for i in range(len(shortest_str)):
        char = shortest_str[i]
        match = all(s[i] == char for s in strs) #Check if all strings match at index i

        if match:
            prefix += char
        else:
            break

    return prefix


strings1 = ["flower","flow","flight"]
print(f"Longest common prefix of {strings1}: {longestCommonPrefix_charByChar(strings1)}") # Output: fl

strings2 = ["dog","racecar","car"]
print(f"Longest common prefix of {strings2}: {longestCommonPrefix_charByChar(strings2)}") # Output: ""

strings3 = ["apple", "app", "appetizer"]
print(f"Longest common prefix of {strings3}: {longestCommonPrefix_charByChar(strings3)}") # Output: ap

strings4 = []
print(f"Longest common prefix of {strings4}: {longestCommonPrefix_charByChar(strings4)}") # Output: ""