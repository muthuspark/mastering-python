import pandas as pd

data = {'Name': ['Alice', 'Bob', 'Charlie'],
        'Age': [25, 30, 28],
        'City': ['New York', 'London', 'Paris']}
df = pd.DataFrame(data)
print("DataFrame:\n", df)

print("\nAge column:\n", df['Age'])

print("\nRow for Alice:\n", df.loc[df['Name'] == 'Alice'])

print("\nFirst row:\n", df.iloc[0])

#Adding a new column
df['Country'] = ['USA', 'UK', 'France']
print("\nDataFrame with added column:\n", df)