data_types = {'column1': int, 'column2': str, 'column3': float}
data_typed = pd.read_csv("data.csv", dtype=data_types)
print(data_typed.dtypes)