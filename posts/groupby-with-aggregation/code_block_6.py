def range_fn(x):
  return x.max() - x.min()

region_range = df.groupby('Region')['Sales'].agg(range_fn)
print(region_range)