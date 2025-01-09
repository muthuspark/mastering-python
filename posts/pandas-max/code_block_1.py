import pandas as pd

data = {'col1': [1, 5, 2, 8, 3], 'col2': [10, 2, 15, 4, 6], 'col3': [7, 9, 1, 3, 12]}
df = pd.DataFrame(data)

row_max = df.max(axis=1)
print("Maximum values across each row:\n", row_max)

#Method 2: Using `apply()` with `max` function
row_max_method2 = df.apply(lambda row: row.max(), axis=1)
print("\nMaximum values across each row (using apply):\n", row_max_method2)

overall_max = df.values.max()
print(f"\nThe overall maximum value in the DataFrame is: {overall_max}")