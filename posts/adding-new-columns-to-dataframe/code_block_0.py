import pandas as pd

data = {'col1': [1, 2, 3], 'col2': [4, 5, 6]}
df = pd.DataFrame(data)
print("Original DataFrame:\n", df)

df['col3'] = [7, 8, 9] 
print("\nDataFrame after adding 'col3':\n", df)

#Adding a column from a list of the same size
df['col4'] = [10,11,12]
print("\nDataFrame after adding 'col4':\n", df)

#Adding a new column with a scalar value (same value for all rows)
df['col5'] = 100
print("\nDataFrame after adding 'col5':\n", df)