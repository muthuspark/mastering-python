years = dates.astype('datetime64[Y]')
months = dates.astype('datetime64[M]')
days = dates.astype('datetime64[D]')
print(years)
print(months)
print(days)


#Extracting year,month,day individually using .astype
years = dates.astype('datetime64[Y]').astype(int) + 1970 #Adding 1970 to get actual year
months = dates.astype('datetime64[M]').astype(int) % 12 +1 #Getting month number
days = dates.astype('datetime64[D]').astype(int) %365 +1 #Getting Day number


print(years)
print(months)
print(days)
