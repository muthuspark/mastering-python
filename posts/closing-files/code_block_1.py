f = open("my_file.txt", "w")
try:
    f.write("This is some more text.")
    # ... other file operations ...
finally:
    f.close()