import pandas as pd

data = [[1, 'Alice', 25], [2, 'Bob', 30], [3, 'Charlie', 22]]
df = pd.DataFrame(data, columns=['ID', 'Name', 'Age'])
print(df)