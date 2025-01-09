df_sales = pd.read_excel("data.xlsx", sheet_name="Sales Data")
print(df_sales)

#Reading multiple sheets
xls = pd.ExcelFile("data.xlsx")
df_sheet1 = pd.read_excel(xls, 'Sheet1')
df_sheet2 = pd.read_excel(xls, 'Sheet2')
print(df_sheet1)
print(df_sheet2)