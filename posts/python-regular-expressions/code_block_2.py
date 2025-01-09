text = "This is a sample string with 123 numbers and some words."
pattern = r"\b\w{4}\b" # \b matches word boundaries, \w{4} matches four word characters

matches = re.findall(pattern, text)
print(matches) # Output: ['This', 'with', 'some', 'words']