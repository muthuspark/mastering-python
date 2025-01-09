filtered_df = df[(df['Age'] > 25) & (df['City'] == 'London')]
print(filtered_df)

filtered_df = df[(df['Age'] > 25) | (df['City'] == 'Paris')]
print(filtered_df)

filtered_df = df[~(df['City'] == 'New York')]
print(filtered_df)