print(df['2024-10-26'])

print(df.loc['2024-10-26 09:00:00':'2024-10-26 11:00:00'])

print(df[df.index.hour >= 10]) # all entries where the hour is 10 or greater