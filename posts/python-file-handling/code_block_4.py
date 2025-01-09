try:
    with open("nonexistent_file.txt", "r") as file:
        contents = file.read()
except FileNotFoundError:
    print("File not found.  Check the file path.")
except Exception as e:
    print(f"An error occurred: {e}")