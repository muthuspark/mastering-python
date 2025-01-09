chunksize = 1000  # Process 1000 rows at a time
for chunk in pd.read_csv("large_file.csv", chunksize=chunksize):
    # Process each chunk individually
    # ... your data processing logic here ...
    print(chunk.head())