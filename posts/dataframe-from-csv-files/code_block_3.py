data_missing = pd.read_csv("data_missing.csv", na_values=['NA', ''])
print(data_missing.isnull().sum()) #Check for missing values after import