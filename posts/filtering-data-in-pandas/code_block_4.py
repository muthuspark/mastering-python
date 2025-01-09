#Filter for names containing "a"
filtered_df = df[df['Name'].str.contains('a')]
print(filtered_df)

#Filter for names starting with "A"
filtered_df = df[df['Name'].str.startswith('A')]
print(filtered_df)