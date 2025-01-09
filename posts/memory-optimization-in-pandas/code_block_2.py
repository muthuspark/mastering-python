chunksize = 10000  # Adjust as needed
for chunk in pd.read_csv('large_file.csv', chunksize=chunksize):
    # Process each chunk individually
    # ... your data processing code ...