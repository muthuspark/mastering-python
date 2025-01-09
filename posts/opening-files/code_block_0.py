try:
    with open("my_file.txt", "r") as file:
        contents = file.read()
        print(contents)
except FileNotFoundError:
    print("File not found.")