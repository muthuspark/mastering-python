import pandas as pd

data = {'col1': [1, 2, 3], 'col2': [4, 5, 6]}
df = pd.DataFrame(data, index=['A', 'B', 'C'])

print(df.at['B', 'col2'])  # Output: 5
print(df.iat[1, 1])       # Output: 5