import pandas as pd

data = {'Name': ['Alice', 'Bob', 'Charlie', 'David'],
        'Age': [25, 30, 22, 28],
        'City': ['New York', 'London', 'Paris', 'Tokyo']}

df = pd.DataFrame(data)
print(df)

print("\nRow labeled 'Alice':\n", df.loc['Alice'])

#Select single column
print("\n'Age' column:\n",df.loc[:,"Age"])


#Select multiple columns
print("\n'Age' and 'City' columns:\n",df.loc[:,['Age','City']])

