my_dict = {"a": 1, "b": 2}
value = my_dict.setdefault("c", 3) # adds key 'c' with value 3
print(value)  # Output: 3
print(my_dict)  # Output: {'a': 1, 'b': 2, 'c': 3}

value = my_dict.setdefault("a", 10) #'a' already exists, so its value is returned
print(value) #Output: 1