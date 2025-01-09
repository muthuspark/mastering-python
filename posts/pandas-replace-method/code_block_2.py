data = {'col1': [1, 2, 3, 2, 1], 'col2': ['A', 'B', 'C', 'B', 'A']}
df = pd.DataFrame(data)

df.replace({'col1': {1: 100, 3: 300}, 'col2': {'A': 'X', 'B': 'Y'}}, inplace=True)
print(df)