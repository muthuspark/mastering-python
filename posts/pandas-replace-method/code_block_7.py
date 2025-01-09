data = {'col1': [1, 2, float('nan'), 4]}
df = pd.DataFrame(data)

df['col1'] = df['col1'].replace(float('nan'), 0)
print(df)