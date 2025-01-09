name = my_dict["name"]
print(name)  # Output: Alice

age = my_dict.get("age")
print(age)  # Output: 30

city = my_dict.get("state", "N/A") #If key not found return default value
print(city) #Output: N/A
