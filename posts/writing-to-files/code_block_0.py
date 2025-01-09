file_path = 'my_file.txt'
with open(file_path, 'w') as f:
    f.write("This is the first line.\n")
    f.write("This is the second line.")

with open(file_path, 'a') as f:
    f.write("\nThis line is appended.")