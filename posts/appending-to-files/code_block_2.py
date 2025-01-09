my_list = ["apple", "banana", "cherry"]
file_path = "my_fruit_list.txt"

try:
  with open(file_path, 'a') as file:
    for item in my_list:
      file.write(item + "\n")
except Exception as e:
  print(f"An error occurred: {e}")