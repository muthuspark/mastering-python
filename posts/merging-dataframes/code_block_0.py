import pandas as pd

df1 = pd.DataFrame({'key': ['A', 'B', 'C', 'D'], 'value1': [1, 2, 3, 4]})
df2 = pd.DataFrame({'key': ['B', 'D', 'E', 'F'], 'value2': [5, 6, 7, 8]})

print("DataFrame 1:\n", df1)
print("\nDataFrame 2:\n", df2)