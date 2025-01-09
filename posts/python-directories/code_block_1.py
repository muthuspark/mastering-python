import os

os.chdir("/path/to/your/directory")  
new_directory = os.getcwd()
print(f"New working directory: {new_directory}")

#Returning to previous directory is not covered in this example but would be done by assigning getcwd() to a variable before changing directories