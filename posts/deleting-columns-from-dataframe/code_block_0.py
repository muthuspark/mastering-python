import pandas as pd

data = {'Name': ['Alice', 'Bob', 'Charlie', 'David'],
        'Age': [25, 30, 22, 28],
        'City': ['New York', 'London', 'Paris', 'Tokyo'],
        'Salary': [60000, 75000, 55000, 80000]}

df = pd.DataFrame(data)
print(df)