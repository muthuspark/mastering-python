data = {'col1': ['1a', '2b', '3c']}
df = pd.DataFrame(data)

#Clean data using method chaining
df['col1'] = df['col1'].str.replace('[a-z]', '', regex=True).astype(int)
print(df)