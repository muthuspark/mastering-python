region_product_sales = df.groupby(['Region', 'Product'])['Sales'].sum()
print(region_product_sales)