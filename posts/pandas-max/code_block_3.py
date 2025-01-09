import pandas as pd

data = {'col1': [1, 5, 2, 8, 3], 'col2': ['A', 'B', 'A', 'C', 'B']}
df = pd.DataFrame(data)

max_value_condition = df[df['col2'] == 'A']['col1'].max()
print(f"Maximum value in 'col1' where 'col2' is 'A': {max_value_condition}")