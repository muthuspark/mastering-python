import dask.dataframe as dd

def process_with_dask(filepath):
    df = dd.read_csv(filepath)
    # Perform computations on the Dask DataFrame
    # Example: Calculate the mean of a column
    mean_value = df['column_name'].mean().compute()
    print(f"Mean of 'column_name': {mean_value}")

process_with_dask("large_dataset.csv")