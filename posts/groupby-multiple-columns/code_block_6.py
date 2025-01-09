aggregated = grouped['Sales'].agg(['sum', 'mean', 'count'])
print(aggregated)