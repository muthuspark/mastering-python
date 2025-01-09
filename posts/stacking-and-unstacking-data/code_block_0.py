import pandas as pd

data = {'Category': ['A', 'A', 'B', 'B'],
        'Subcategory': ['X', 'Y', 'X', 'Y'],
        'Value': [10, 15, 20, 25]}
df = pd.DataFrame(data)

print("Original DataFrame:\n", df)

stacked_df = df.set_index(['Category', 'Subcategory']).stack()
print("\nStacked DataFrame:\n", stacked_df)

stacked_df = df.set_index(['Category', 'Subcategory']).stack().rename('Value_stacked')
print("\nStacked DataFrame with renamed column:\n", stacked_df)

