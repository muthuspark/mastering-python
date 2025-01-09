data_list = [(1, 'a'), (2, 'b'), (3, 'c')]
for key, value in data_list:  # Linear search for each element
    if key == 2:
        print(value)

data_dict = {1: 'a', 2: 'b', 3: 'c'}
print(data_dict[2]) # O(1) lookup