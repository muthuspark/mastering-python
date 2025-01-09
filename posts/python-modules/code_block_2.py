import os

current_directory = os.getcwd()
print(f"Current working directory: {current_directory}")

files_directories = os.listdir()
print(f"Files and directories: {files_directories}")

new_directory = "my_new_directory"
os.makedirs(new_directory, exist_ok=True)  # exist_ok prevents errors if the directory already exists