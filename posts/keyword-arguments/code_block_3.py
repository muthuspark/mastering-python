def print_info(name, age, *, city="Unknown", country="Unknown"):
    print(f"Name: {name}, Age: {age}, City: {city}, Country: {country}")

print_info("Eve", 28, city="Paris", country="France")  #Correct
#print_info("Eve", 28, "Paris", "France") #Incorrect - city and country must be passed as keyword arguments