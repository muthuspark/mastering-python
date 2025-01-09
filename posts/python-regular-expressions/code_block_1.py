text = "My phone number is 123-456-7890 and another is 987-654-3210."
pattern = r"\d{3}-\d{3}-\d{4}"  # \d matches digits, {n} matches n repetitions

matches = re.findall(pattern, text)
print(matches) # Output: ['123-456-7890', '987-654-3210']