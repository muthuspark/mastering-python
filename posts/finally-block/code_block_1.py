file_handle = None
try:
    file_handle = open("my_file.txt", "r")
    contents = file_handle.read()
    # Process the file contents
    print(contents)
except FileNotFoundError:
    print("File not found!")
finally:
    if file_handle:
        file_handle.close()
        print("File closed successfully!")