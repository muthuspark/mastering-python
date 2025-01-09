#Select rows where column 'A' is greater than 1
selected_rows = df[df['A'] > 1]
print(selected_rows)

#Combine multiple conditions
selected_rows = df[(df['A'] > 1) & (df['B'] < 6)]
print(selected_rows)