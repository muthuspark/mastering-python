string = "Hello, world!"
character_to_count = "l"
count = 0
for char in string:
    if char == character_to_count:
        count += 1
print(f"The character '{character_to_count}' appears {count} times in the string.")