import pandas as pd

data = {'Name': ['Alice', 'Bob', 'Charlie', 'David'],
        'Age': [25, 30, 22, 28],
        'City': ['New York', 'London', 'Paris', 'Tokyo']}

df = pd.DataFrame(data)
print("Original DataFrame:\n", df)

df_indexed = df.set_index('Name')
print("\nDataFrame with 'Name' as index:\n", df_indexed)