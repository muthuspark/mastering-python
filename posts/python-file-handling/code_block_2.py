data = ["Line 1\n", "Line 2\n", "Line 3"]

with open("new_file.txt", "w") as file:
    file.writelines(data) #Write a list of strings

with open("new_file.txt", "a") as file:
  file.write("This is appended on a new line.")
