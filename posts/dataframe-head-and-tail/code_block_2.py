import pandas as pd

data = {'col1': range(100), 'col2': [chr(i+65) for i in range(100)]} # Generates 100 rows
df_large = pd.DataFrame(data)

print("First 5 rows:\n", df_large.head())
print("\nLast 5 rows:\n", df_large.tail())