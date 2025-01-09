import pandas as pd

data = {'Column with spaces': [1, 2, 3], 'Column!@#$': [4, 5, 6]}
df = pd.DataFrame(data)

df = df.rename(columns={'Column with spaces': 'Column_with_spaces', 'Column!@#$': 'Column_no_special_chars'})
print("\nDataFrame after handling spaces and special chars:\n", df)