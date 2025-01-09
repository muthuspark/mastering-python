my_tuple = (10, 20, 30, 40, 30)
index_of_30 = my_tuple.index(30)
print(f"The first occurrence of 30 is at index: {index_of_30}")  # Output: The first occurrence of 30 is at index: 2

try:
    index_of_50 = my_tuple.index(50)
    print(index_of_50)
except ValueError:
    print("Element not found in the tuple") # Output: Element not found in the tuple
