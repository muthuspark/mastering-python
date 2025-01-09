col1_iloc = df.iloc[:, 0] # 0 represents the first column
print("\n.iloc for single column:\n", col1_iloc)

cols_iloc = df.iloc[:, [0, 2]] # [0, 2] represents the first and third columns
print("\n.iloc for multiple columns:\n", cols_iloc)