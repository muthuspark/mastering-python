text = "This is a sample string."

uppercase_text = text.upper()
print(f"Uppercase: {uppercase_text}")

lowercase_text = text.lower()
print(f"Lowercase: {lowercase_text}")

words = text.split()
print(f"Words: {words}")

new_text = text.replace("sample", "example")
print(f"Replaced: {new_text}")

contains_sample = "sample" in text
print(f"Contains 'sample': {contains_sample}")