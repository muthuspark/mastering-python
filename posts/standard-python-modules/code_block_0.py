import os

current_directory = os.getcwd()
print(f"Current directory: {current_directory}")

os.makedirs("my_new_directory", exist_ok=True)

files = os.listdir(".")
print(f"Files in current directory: {files}")

#Rename a file
os.rename("old_file.txt", "new_file.txt") #Requires old_file.txt to exist

#Remove a file
os.remove("new_file.txt") #Requires new_file.txt to exist
