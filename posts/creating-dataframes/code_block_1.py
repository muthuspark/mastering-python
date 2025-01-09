names = ['Alice', 'Bob', 'Charlie']
ages = [25, 30, 28]
cities = ['New York', 'London', 'Paris']

df = pd.DataFrame(list(zip(names, ages, cities)), columns=['Name', 'Age', 'City'])
print(df)


#Alternative using a list of lists:
data_list = [[ 'Alice', 25, 'New York'], ['Bob', 30, 'London'], ['Charlie', 28, 'Paris']]
df_list = pd.DataFrame(data_list, columns=['Name', 'Age', 'City'])
print(df_list)