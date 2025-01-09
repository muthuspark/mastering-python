first_two_rows = df.iloc[:2, :]
print(first_two_rows)

first_two_cols = df.iloc[:, :2]
print(first_two_cols)

specific_selection = df.iloc[1:3, [0, 2]]
print(specific_selection)