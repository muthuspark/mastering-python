cities_of_interest = ['London', 'Paris']
customers_in_cities = df[df['City'].isin(cities_of_interest)]
print(customers_in_cities)