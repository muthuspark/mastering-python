strings = ["apple pie", "banana bread", "cherry cake"]
new_strings = [s.replace("pie", "tart") for s in strings]
print(new_strings) # Output: ['apple tart', 'banana bread', 'cherry cake']