data = {'Category': ['A', 'A', 'B', 'B', 'C', 'C'],
        'Subcategory': ['X', 'Y', 'X', 'Y', 'X', 'Y'],
        'Value': [10, 15, 20, 25, 30, 35]}

df = pd.DataFrame(data)
grouped_multiple = df.groupby(['Category', 'Subcategory'])['Value'].mean()
print("\nGrouping by Multiple Columns:\n", grouped_multiple)