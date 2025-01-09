nested_list = [[1, 2, 3], [4, [5, 6]], 7]
flat_list = []

for sublist in nested_list:
    if isinstance(sublist, list):
        for item in sublist:
            flat_list.append(item)
    else:
        flat_list.append(sublist)

print(flat_list)  # Output: [1, 2, 3, 4, 5, 6, 7]