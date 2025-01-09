cities_to_include = ['New York', 'London']
filtered_df = df[df['City'].isin(cities_to_include)]
print(filtered_df)