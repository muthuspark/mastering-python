import pandas as pd


df.to_excel('exported_data.xlsx', sheet_name='Sheet1', index=False)

#For older .xls files (requires xlwt)
#df.to_excel('exported_data.xls', sheet_name='Sheet1', index=False)