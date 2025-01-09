def counter():
    count = 0  # Free variable

    def increment():
        nonlocal count # Important! This declares that we are modifying the outer count, not creating a new one.
        count += 1
        return count

    return increment

my_counter = counter()
print(my_counter())  # Output: 1
print(my_counter())  # Output: 2
print(my_counter())  # Output: 3