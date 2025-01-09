london_and_older = (df['Age'] > 25) & (df['City'] == 'London')
print(df[london_and_older])