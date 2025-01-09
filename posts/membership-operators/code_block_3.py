my_dict = {"a": 1, "b": 2, "c": 3}
if "b" in my_dict:
    print("'b' is a key in the dictionary")

#Output: 'b' is a key in the dictionary

if 2 in my_dict: # Note: This checks for keys, not values
    print("2 is a key in the dictionary") #This will not print
