df['D'] = ['X','Y',np.nan,'Z']
df['D'] = df['D'].fillna('Missing')
print(df)
