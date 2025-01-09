my_dict = {(1,2): "value1", (3,4): "value2"}
print(my_dict) #This works because tuples are hashable
#my_dict = {[1,2]: "value1", [3,4]: "value2"} #this would raise an error because lists are not hashable.
