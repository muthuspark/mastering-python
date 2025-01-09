import pandas as pd

data = {'Name': ['Alice', 'Bob', 'Charlie'],
        'Age': [25, 30, 28],
        'City': ['New York', 'London', 'Paris']}
df = pd.DataFrame(data)

df.to_csv('data.csv', index=False) # index=False prevents writing the DataFrame index