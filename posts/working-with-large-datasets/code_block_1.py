import dask.dataframe as dd

ddf = dd.read_csv("large_dataset.csv")

average_value = ddf["column_name"].mean().compute() # .compute() triggers computation
print(average_value)
