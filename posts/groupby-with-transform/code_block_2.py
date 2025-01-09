avg_sales_by_region = df.groupby('Region')['Sales'].transform('mean')
df['Avg_Sales_Region'] = avg_sales_by_region
print(df)