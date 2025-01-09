import os

os.mkdir("my_new_directory")

os.makedirs("nested/directories/example", exist_ok=True) #exist_ok prevents error if directory already exists