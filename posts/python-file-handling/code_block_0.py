try:
    with open("my_file.txt", "r") as file:
        contents = file.read()
        print(contents)
except FileNotFoundError:
    print("File not found.")


try:
    with open("output.txt", "w") as file:
        file.write("This is some text.\n")
        file.write("This is another line.")
except Exception as e:
    print(f"An error occurred: {e}")

try:
    with open("output.txt", "a") as file:
        file.write("\nThis is appended text.")
except Exception as e:
    print(f"An error occurred: {e}")
