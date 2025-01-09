import csv

try:
    with open("data.csv", 'r', newline='') as file: # newline='' is important to avoid extra blank lines
        reader = csv.reader(file)
        # Skip the header row (if present)
        next(reader, None)  
        for row in reader:
            print(row) # each row is a list of strings
except FileNotFoundError:
    print("Error: File 'data.csv' not found.")
