data2 = {'col1': [1, 2, 3, 4, 5], 'col2': [6, 7, 8, 9, 10]}
df2 = pd.DataFrame(data2)
print(f"Shape of df2: {df2.shape}")  # Output: Shape of df2: (5, 2)


data3 = {'col1': [1, 2, 3]}
df3 = pd.DataFrame(data3)
print(f"Shape of df3: {df3.shape}")  # Output: Shape of df3: (3, 1)


df4 = pd.DataFrame()
print(f"Shape of df4: {df4.shape}")  # Output: Shape of df4: (0, 0)
