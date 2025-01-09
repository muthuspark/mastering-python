import pandas as pd

data = {'Name': ['Alice', 'Bob', 'Charlie'],
        'Age': [25, 30, 28],
        'City': ['New York', 'London', 'Paris']}
df = pd.DataFrame(data)

print(df)

print(df['Name'])

print(df[df['Age'] > 28])

print(df.groupby('City')['Age'].mean())