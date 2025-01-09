region_sales = df.groupby('Region')['Sales'].sum()
print(region_sales)