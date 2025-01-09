data = {'col1': [1, 2, 2, 3, 3, 3], 'col2': ['A', 'B', 'B', 'C', 'C', 'C']}
df = pd.DataFrame(data)
print("DataFrame:\n", df)
print("\nMode of col1:", df['col1'].mode())
print("\nMode of col2:", df['col2'].mode())
