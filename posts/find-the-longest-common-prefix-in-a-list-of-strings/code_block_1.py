import os

def longestCommonPrefix_os(strs):
    """
    Finds the longest common prefix using os.path.commonprefix.

    Args:
        strs: A list of strings.

    Returns:
        The longest common prefix string.
    """
    if not strs:
        return ""
    return os.path.commonprefix(strs)


strings1 = ["flower","flow","flight"]
print(f"Longest common prefix of {strings1}: {longestCommonPrefix_os(strings1)}") # Output: fl

strings2 = ["dog","racecar","car"]
print(f"Longest common prefix of {strings2}: {longestCommonPrefix_os(strings2)}") # Output: ""

strings3 = ["apple", "app", "appetizer"]
print(f"Longest common prefix of {strings3}: {longestCommonPrefix_os(strings3)}") # Output: ap

strings4 = []
print(f"Longest common prefix of {strings4}: {longestCommonPrefix_os(strings4)}") # Output: ""