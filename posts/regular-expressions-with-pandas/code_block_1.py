import pandas as pd

data = {'product': ['Apple iPhone 13 Pro Max 256GB', 'Samsung Galaxy S23 512GB', 'Google Pixel 7 128GB']}
df = pd.DataFrame(data)

pattern = r"(\w+\s\w+)\s(\w+)\s(\d+GB)"
df[['model', 'brand', 'storage']] = df['product'].str.extract(pattern)
print(df)
