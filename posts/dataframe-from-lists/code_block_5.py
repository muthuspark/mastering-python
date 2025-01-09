import pandas as pd

data = [[1, 'Alice', 25.5, True], [2, 'Bob', 30, False], [3, 'Charlie', 22, True]]
df = pd.DataFrame(data, columns=['ID', 'Name', 'Age', 'Status'])
print(df)