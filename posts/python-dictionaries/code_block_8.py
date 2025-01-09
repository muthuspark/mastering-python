age = my_dict.pop("age")
print(age) # Output: 31
print(my_dict) # Output: {'name': 'Alice', 'occupation': 'Engineer'}

country = my_dict.pop("country", "Not specified")
print(country) # Output: Not specified