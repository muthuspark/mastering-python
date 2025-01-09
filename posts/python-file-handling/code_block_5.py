import os

current_directory = os.getcwd()
print(f"Current directory: {current_directory}")

file_path = os.path.join(current_directory, "my_file.txt")
print(f"File path: {file_path}")

if os.path.exists(file_path):
    print(f"File '{file_path}' exists.")
else:
    print(f"File '{file_path}' does not exist.")
