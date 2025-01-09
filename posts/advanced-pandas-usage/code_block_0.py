import pandas as pd
import numpy as np

data = {'col1': [1, 2, 3, 4, 5], 
        'col2': [6, 7, 8, 9, 10], 
        'col3': ['A', 'B', 'C', 'D', 'E']}
df = pd.DataFrame(data)

print("Rows where col1 > 2:\n", df[df['col1'] > 2])

print("\nRows where col1 > 2 and col2 < 9 using .query():\n", df.query('col1 > 2 and col2 < 9'))

print("\nSelecting first two rows and col1 and col3:\n", df.iloc[:2, [0,2]])

df.at[0, 'col1'] = 100
print("\nDataFrame after changing value at position 0, 'col1':\n", df)

