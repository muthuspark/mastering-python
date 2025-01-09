try:
    with open("my_file.txt", 'r', encoding='utf-8') as file:
        contents = file.read()
        print(contents)
except FileNotFoundError:
    print(f"Error: File '{file_path}' not found.")
except UnicodeDecodeError:
    print("Error: Could not decode file. Check the encoding.")