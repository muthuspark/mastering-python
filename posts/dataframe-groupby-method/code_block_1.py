#Calculate the mean of 'Value' for each category
mean_values = grouped['Value'].mean()
print("\nMean of 'Value' by Category:\n", mean_values)


#Calculate multiple aggregates at once
aggregate_results = grouped['Value'].agg(['mean', 'sum', 'count'])
print("\nMultiple Aggregates:\n", aggregate_results)
