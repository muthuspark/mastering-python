import re

text = "The cat sat on the mat, and another cat was nearby."
pattern = r"cat"  # r"" denotes a raw string, preventing backslash escaping issues

matches = re.findall(pattern, text)
print(matches)  # Output: ['cat', 'cat']