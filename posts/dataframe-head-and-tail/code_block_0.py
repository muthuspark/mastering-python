import pandas as pd

data = {'col1': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
        'col2': ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J']}
df = pd.DataFrame(data)

print(df.head())

print(df.head(3))