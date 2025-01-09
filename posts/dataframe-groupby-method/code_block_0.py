import pandas as pd

data = {'Category': ['A', 'A', 'B', 'B', 'C', 'C'],
        'Value': [10, 15, 20, 25, 30, 35]}

df = pd.DataFrame(data)
print("Original DataFrame:\n", df)

grouped = df.groupby('Category')
print("\nGrouped DataFrame:\n", grouped)

#Note that the output of groupby is not the aggregated data yet. It is a GroupBy object.