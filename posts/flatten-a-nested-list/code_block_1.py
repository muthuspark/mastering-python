def flatten(nested_list):
    flat_list = []
    for item in nested_list:
        if isinstance(item, list):
            flat_list.extend(flatten(item))  # Recursive call
        else:
            flat_list.append(item)
    return flat_list

nested_list = [[1, 2, [3, 4]], [5, [6, [7, 8]]]]
flat_list = flatten(nested_list)
print(flat_list)  # Output: [1, 2, 3, 4, 5, 6, 7, 8]