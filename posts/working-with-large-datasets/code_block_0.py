import pandas as pd

chunksize = 10000  # Adjust based on your system's memory

for chunk in pd.read_csv("large_dataset.csv", chunksize=chunksize):
    # Process each chunk individually
    print(chunk.head())  # Example: print the first few rows of each chunk
    # Perform calculations, aggregations, etc. on the chunk
    # ... your code here ...