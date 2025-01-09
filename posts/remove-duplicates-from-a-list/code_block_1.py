my_list = [1, 2, 2, 3, 4, 4, 5, 1]
unique_list = []
seen = set()

for item in my_list:
    if item not in seen:
        unique_list.append(item)
        seen.add(item)

print(f"Original list: {my_list}")
print(f"List with duplicates removed (order preserved): {unique_list}")