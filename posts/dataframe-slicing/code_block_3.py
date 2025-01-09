print(df[df['col1'] > 2])

#Select rows where col1 is greater than 2 and col2 is less than 9
print(df[(df['col1'] > 2) & (df['col2'] < 9)])

print(df[df['col1'].isin([1, 5])])