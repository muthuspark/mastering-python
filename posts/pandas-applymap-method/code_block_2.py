data = {'A': ['apple', 'banana', 'cherry'], 'B': ['dog', 'cat', 'bird']}
df = pd.DataFrame(data)

uppercase_df = df.applymap(str.upper)
print(uppercase_df)