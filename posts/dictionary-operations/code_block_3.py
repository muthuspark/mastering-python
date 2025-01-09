del my_dict["city"]
print(my_dict)  # Output: {'name': 'Alice', 'age': 31, 'occupation': 'Engineer'}

popped_value = my_dict.pop("occupation") #Removes and returns the value associated with the key
print(popped_value) #Output: Engineer
print(my_dict) # Output: {'name': 'Alice', 'age': 31}

my_dict.popitem() #Removes and returns an arbitrary key-value pair (last inserted in CPython)
print(my_dict) #Output will vary based on insertion order, likely: {}

#Removes a key only if it is present in the dictionary
my_dict.setdefault("name", "Bob") # No change since key exists
print(my_dict)

my_dict.setdefault("country", "USA") # Key added since it doesn't exist
print(my_dict)