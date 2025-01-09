import os

def list_files(directory):
  """
  Recursively lists all files within a given directory and its subdirectories.
  """
  for item in os.listdir(directory):
    path = os.path.join(directory, item)
    if os.path.isfile(path):
      print(path)
    elif os.path.isdir(path):
      list_files(path) #Recursive call for subdirectories

list_files("/path/to/your/directory") # Replace with your directory path.