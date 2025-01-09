import pandas as pd

data = {'col1': [1, 5, 2, 8, 3]}
df = pd.DataFrame(data)

max_index = df['col1'].idxmax()
print(f"The index of the maximum value in 'col1' is: {max_index}")