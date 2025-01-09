import pandas as pd

data = {'description': ['Product price: $19.99', 'Item cost: $29.95', 'Price: $49.99']}
df = pd.DataFrame(data)

df['price'] = pd.to_numeric(df['description'].str.replace(r'\$', '', regex=True).str.extract(r'(\d+\.\d+)'))
print(df)

