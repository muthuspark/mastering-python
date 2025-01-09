text = "The quick brown fox jumps over the lazy dog."
pattern = r"fox"
match = re.search(pattern, text)
if match:
    print(match.group(0))  # Output: fox