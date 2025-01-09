import pandas as pd

def process_csv_with_pandas(filepath, chunksize=1000):
    for chunk in pd.read_csv(filepath, chunksize=chunksize):
        # Process each chunk here
        print(f"Processing chunk of shape: {chunk.shape}")
        # Example processing: Calculate the mean of a column
        #mean_value = chunk['column_name'].mean()
        #print(f"Mean of 'column_name': {mean_value}")

process_csv_with_pandas("large_dataset.csv", chunksize=1000)