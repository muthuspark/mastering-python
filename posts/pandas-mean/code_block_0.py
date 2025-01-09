import pandas as pd

data = {'Sales': [10, 20, 15, 25, 30, None, 40]}
df = pd.DataFrame(data)

mean_sales = df['Sales'].mean()
print(f"The mean of Sales is: {mean_sales}")