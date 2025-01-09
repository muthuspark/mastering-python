import datetime

file_path = "my_log.txt"

try:
  with open(file_path, 'a') as file:
    current_time = datetime.datetime.now()
    file.write(f"Log entry at: {str(current_time)}\n")
    data_point = 123.45
    file.write(f"Data point: {str(data_point)}\n")
except Exception as e:
  print(f"An error occurred: {e}")