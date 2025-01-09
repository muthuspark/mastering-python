try:
    with open("my_file.txt", "r") as f:
        contents = f.read()
        # Process the file contents
        print(contents)
except FileNotFoundError:
    print("File not found!")
except Exception as e:
    print(f"An error occurred: {e}")