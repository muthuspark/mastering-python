text = "This is a sample string. This string contains multiple instances."
new_text = text.replace("string", "sentence", 1) #Only replaces the first occurrence
print(new_text) # Output: This is a sample sentence. This string contains multiple instances.