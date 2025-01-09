try:
    file = open("nonexistent_file.txt", "r")
    data = file.read()
except FileNotFoundError:
    print("Error: File not found.")
except IOError as e:
    print(f"An IO error occurred: {e}")