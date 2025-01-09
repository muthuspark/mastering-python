def range_fn(x):
    return x.max() - x.min()

custom_aggregation = grouped['Value'].agg(range_fn)
print("\nCustom Aggregation:\n", custom_aggregation)
