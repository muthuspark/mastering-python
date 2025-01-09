import re

text = "This string contains numbers like 123, 456, and 789."
new_text = re.sub(r"\d+", "number", text) #Replaces all numbers with "number"
print(new_text) # Output: This string contains numbers like number, number, and number.

#More complex example with capturing groups
text = "Error code: 123, message: 'File not found'"
new_text = re.sub(r"Error code: (\d+), message: '(.+)'", r"Error: \2, code: \1", text)
print(new_text) #Output: Error: File not found, code: 123