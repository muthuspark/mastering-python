region_summary = df.groupby('Region')['Sales'].agg(['sum', 'mean', 'min', 'max'])
print(region_summary)