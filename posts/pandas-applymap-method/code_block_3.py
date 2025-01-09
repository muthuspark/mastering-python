data = {'A': [1, 2, 3], 'B': [4, 5, 6]}
df = pd.DataFrame(data)

added_df = df.applymap(lambda x: x + 10)
print(added_df)
