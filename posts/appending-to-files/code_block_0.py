file_path = "my_file.txt"

try:
    with open(file_path, 'a') as file:
        file.write("This is some new text.\n")
        file.write("This is even more new text.\n")
except FileNotFoundError:
    print(f"Error: File '{file_path}' not found.")
except Exception as e:
    print(f"An error occurred: {e}")
