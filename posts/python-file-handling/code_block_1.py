with open("my_file.txt", "r") as file:
    # Read the entire file
    all_content = file.read()
    print(f"All content:\n{all_content}")

    file.seek(0) #reset the file pointer to the beginning

    # Read line by line
    line = file.readline()
    while line:
        print(f"Line: {line.strip()}")
        line = file.readline()


    file.seek(0) #reset the file pointer to the beginning

    #Read all lines into a list
    all_lines = file.readlines()
    print(f"All lines as list: {all_lines}")
