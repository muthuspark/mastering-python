import pandas as pd

data = {'col1': [10, 5, 20, 15], 'col2': [25, 12, 8, 18], 'col3': ['A', 'B', 'C', 'A']}
df = pd.DataFrame(data)

#Minimum value in 'col1' where 'col3' is 'A'
minimum_conditional = df[df['col3'] == 'A']['col1'].min()
print(f"Minimum value in col1 where col3 is 'A': {minimum_conditional}")