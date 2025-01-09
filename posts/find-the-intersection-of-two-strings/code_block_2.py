def intersection_using_comprehension(str1, str2):
    """Finds the intersection using list comprehension."""
    common_chars = sorted(list(set([char for char in str1 if char in str2])))
    return "".join(common_chars)

#Example Usage
string1 = "hello"
string2 = "world"
result = intersection_using_comprehension(string1, string2)
print(f"The intersection of '{string1}' and '{string2}' is: {result}") # Output: lo