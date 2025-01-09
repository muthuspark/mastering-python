import csv

def process_csv_chunks(filepath, chunksize=1000):
    with open(filepath, 'r') as file:
        reader = csv.reader(file)
        next(reader)  # Skip header row if present

        for chunk in iter(lambda: list(itertools.islice(reader, chunksize)), []):
            # Process each chunk here
            print(f"Processing chunk of size: {len(chunk)}")
            for row in chunk:
                #Your data processing logic goes here. Example:
                #print(row)
                #Process each row
                pass

import itertools
process_csv_chunks("large_dataset.csv", chunksize=1000)