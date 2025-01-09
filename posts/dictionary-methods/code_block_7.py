my_dict = {"a": 1, "b": 2, "c": 3}
removed_item = my_dict.popitem()
print(removed_item) # Output will vary depending on Python version prior to 3.7, but will be a (key,value) tuple
print(my_dict)