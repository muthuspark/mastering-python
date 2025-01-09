import pandas as pd

data = {'col1': [1, 5, 2, 8, 3]}
df = pd.DataFrame(data)

max_value = df['col1'].max()
print(f"The maximum value in 'col1' is: {max_value}")