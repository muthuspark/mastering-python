with open("my_file.txt", "r") as file:
    for line in file:
        print(line.strip()) # strip() removes leading/trailing whitespace