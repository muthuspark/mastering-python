import os

directory_contents = os.listdir(".")  # "." represents the current directory
print(f"Contents of the current directory: {directory_contents}")

specific_directory = "/path/to/your/directory" #replace with your directory
contents = os.listdir(specific_directory)
print(f"Contents of {specific_directory}: {contents}")