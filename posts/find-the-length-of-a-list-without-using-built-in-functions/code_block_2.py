def list_length_while(data):
    """Calculates list length using a while loop."""
    count = 0
    i = 0
    while i < len(data): #We are using len here to illustrate the while loop approach.  In a real-world scenario without built-in functions, you would need to find another way to check for the end of the list.  One such method would involve modifying the list itself, but that's less desirable.
        count += 1
        i += 1
    return count

my_list = [1,2,3,4,5]
length = list_length_while(my_list)
print(f"The length of the list is: {length}") #Output: The length of the list is: 5