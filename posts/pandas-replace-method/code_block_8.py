data = {'col1': ['aaabbbccc', 'aaabbb']}
df = pd.DataFrame(data)

#Replace only the first two 'a's with 'x'
df['col1'] = df['col1'].str.replace('a', 'x', n=2, regex=True)
print(df)