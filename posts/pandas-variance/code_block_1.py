import pandas as pd

data = {'A': [1, 2, 3, 4, 5], 'B': [6, 7, 8, 9, 10], 'C': [11, 12, 13, 14, 15]}
df = pd.DataFrame(data)

variances = df.var()
print(f"Variances:\n{variances}")