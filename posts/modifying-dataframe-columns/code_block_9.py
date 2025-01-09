import pandas as pd

data = {'col1': [1, 2, 3], 'col2': [4, 5, 6], 'col3':[7,8,9]}
df = pd.DataFrame(data)

df = df.drop(columns=['col3']) #Drop 'col3' column
print(df)
