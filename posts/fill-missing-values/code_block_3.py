df_ffill = df.fillna(method='ffill')
df_bfill = df.fillna(method='bfill')
print(df_ffill)
print(df_bfill)