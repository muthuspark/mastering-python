file_path = "my_file.txt"  # Replace with your file path

try:
    with open(file_path, 'r') as file:
        contents = file.read()  # Reads the entire file into a single string
        print(contents)
except FileNotFoundError:
    print(f"Error: File '{file_path}' not found.")