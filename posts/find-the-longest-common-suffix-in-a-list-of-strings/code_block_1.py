import os

def longest_common_suffix_os(strings):
    """Finds the longest common suffix using os.path.commonprefix on reversed strings."""
    if not strings:
        return ""
    reversed_strings = [s[::-1] for s in strings]
    common_prefix = os.path.commonprefix(reversed_strings)
    return common_prefix[::-1]

strings1 = ["flowerpower", "superpower", "waterpower"]
print(f"Longest common suffix of {strings1}: {longest_common_suffix_os(strings1)}")  # Output: power

strings2 = ["apple", "banana", "orange"]
print(f"Longest common suffix of {strings2}: {longest_common_suffix_os(strings2)}")  # Output: 