my_string = "hello world"
uppercase_string = ""
for char in my_string:
    if 'a' <= char <= 'z':
        uppercase_string += chr(ord(char) - 32)
    else:
        uppercase_string += char
print(uppercase_string)  # Output: HELLO WORLD