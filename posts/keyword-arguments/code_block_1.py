def create_profile(name, age, city, country="USA"):
  profile = {
      "name": name,
      "age": age,
      "city": city,
      "country": country
  }
  return profile

profile1 = create_profile("Charlie", 30, "New York")
print(profile1) #Output: {'name': 'Charlie', 'age': 30, 'city': 'New York', 'country': 'USA'}

profile2 = create_profile(city="London", age=25, name="David", country="UK")
print(profile2) # Output: {'name': 'David', 'age': 25, 'city': 'London', 'country': 'UK'}