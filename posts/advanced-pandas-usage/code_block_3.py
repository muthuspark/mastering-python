grouped = df.groupby('col3')['col1'].mean()
print("\nMean of col1 grouped by col3:\n", grouped)
