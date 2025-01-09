text = "apple, banana, apple, orange"
pattern = r"apple"
replaced_text = re.sub(pattern, "grape", text)
print(replaced_text)  # Output: grape, banana, grape, orange