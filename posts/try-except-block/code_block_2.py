try:
    file = open("my_file.txt", "r")
    data = file.read()
except FileNotFoundError:
    print("Error: File not found.")
else:
    print("File opened successfully:", data)
finally:
    file.close() # This will always run, even if errors occur