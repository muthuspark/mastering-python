def process_file(filename):
  try:
    with open(filename, 'r') as f:
      # ... file processing logic ...
      pass
  except FileNotFoundError as e:
    raise FileNotFoundError(f"File not found: {filename}") from e


try:
    process_file("nonexistent_file.txt")
except FileNotFoundError as e:
    print(f"An error occurred: {e}")