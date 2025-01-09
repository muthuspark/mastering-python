try:
    with open(file_path, 'r') as file:
        for line in file:
            # Process each line individually
            print(line.strip()) # strip() removes leading/trailing whitespace
except FileNotFoundError:
    print(f"Error: File '{file_path}' not found.")