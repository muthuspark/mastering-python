import pandas as pd

data = {'col1': [1, 2, 3], 'col2': [4, 5, 6]}
df = pd.DataFrame(data)
print("Default Index:\n", df)

df = pd.DataFrame(data, index=['A', 'B', 'C'])
print("\nCustom Index:\n", df)