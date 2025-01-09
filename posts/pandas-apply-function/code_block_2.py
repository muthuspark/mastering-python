import pandas as pd

data = {'Value': [10, 25, 5, 100, 30]}
df = pd.DataFrame(data)

def categorize_value(value):
    if value < 10:
        return 'Low'
    elif value < 50:
        return 'Medium'
    else:
        return 'High'

df['Category'] = df['Value'].apply(categorize_value)
print(df)