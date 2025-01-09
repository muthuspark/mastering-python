import pandas as pd

data = {'col1': [1, 2, 3], 'col2': [4, 5, 6], 'col3': [7, 8, 9]}
df = pd.DataFrame(data)

shape = df.shape
print(f"The shape of the DataFrame is: {shape}")  # Output: The shape of the DataFrame is: (3, 3)