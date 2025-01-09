import pandas as pd

df1 = pd.DataFrame({
    'CustomerID': [1, 2, 3],
    'Name': ['Alice', 'Bob', 'Charlie'],
    'City': ['New York', 'London', 'Paris']
})

df2 = pd.DataFrame({
    'CustomerID': [1, 2, 4],
    'OrderID': [101, 102, 104],
    'OrderDate': ['2024-03-08', '2024-03-10', '2024-03-15']
})

print("DataFrame 1:\n", df1)
print("\nDataFrame 2:\n", df2)