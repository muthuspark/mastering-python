import pandas as pd

def categorize_sales(sales):
    if sales < 120:
        return "Low"
    elif sales < 160:
        return "Medium"
    else:
        return "High"

df['Sales_Category'] = df['Sales'].transform(categorize_sales)

print(df)