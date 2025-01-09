data = {'col1': ['apple pie', 'banana bread', 'apple cake']}
df = pd.DataFrame(data)

df['col1'] = df['col1'].str.replace('apple', 'orange', regex=True)
print(df)