df_skipped = pd.read_excel("data.xlsx", skiprows=1)
print(df_skipped)

#Specify header row
df_header = pd.read_excel("data.xlsx", header=2) #Assuming header is in the 3rd row
print(df_header)
