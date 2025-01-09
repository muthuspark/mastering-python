a = 10
b = a  # b now refers to the same object as a
print(id(a), id(b))  # id() returns the memory address of the object
a = 20  # a now refers to a different object; b remains unchanged
print(id(a), id(b))