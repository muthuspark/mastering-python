data = {'Name and Age': ['Alice', 'Bob'],
        'City of Residence': ['New York', 'London']}

df2 = pd.DataFrame(data)
result = df2.query('`Name and Age` == "Alice"')
print(result)