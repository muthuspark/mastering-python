from collections import Counter

string = "Hello, world!"
char_counts = Counter(string)
print(f"Character counts: {char_counts}")
print(f"Count of 'l': {char_counts['l']}")