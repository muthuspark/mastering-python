age_threshold = 26
city_to_find = 'Paris'

filtered_df = df.query('Age > @age_threshold or City == @city_to_find')
print(filtered_df)