try:
    with open('my_file.txt', 'x') as f:
        f.write("This might fail if file exists")
except FileExistsError:
    print("File already exists!")
except Exception as e:
    print(f"An error occurred: {e}")