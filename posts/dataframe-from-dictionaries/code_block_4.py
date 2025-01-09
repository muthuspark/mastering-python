data = [{'Name': 'Alice', 'Age': 25, 'City': 'New York'},
        {'Name': 'Bob', 'Age': 30, 'City': 'London'},
        {'Name': 'Charlie', 'Age': 28, 'City': 'Paris'}]

df = pd.DataFrame(data, columns=['City', 'Name', 'Age'])
print(df)