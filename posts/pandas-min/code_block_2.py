import pandas as pd

data = {'col1': [10, 5, 20, 15], 'col2': [25, 12, 8, 18], 'col3': [3, 17, 9, 2]}
df = pd.DataFrame(data)

column_minimums = df.min()
print("Minimum values in each column:\n", column_minimums)

overall_minimum = df.min().min()
print(f"\nThe overall minimum value in the DataFrame is: {overall_minimum}")