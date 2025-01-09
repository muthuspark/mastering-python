my_list = [10, 20, 30, 40]
my_iterator = iter(my_list) # Built-in iter() function creates an iterator

print(next(my_iterator)) # Output: 10
print(next(my_iterator)) # Output: 20


my_string = "Hello"
for char in my_string: # Strings are also iterable
    print(char) # Output: H e l l o