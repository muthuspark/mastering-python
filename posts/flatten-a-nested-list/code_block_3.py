from itertools import chain

nested_list = [[1, 2, 3], [4, 5, 6]]
flat_list = list(chain.from_iterable(nested_list))
print(flat_list)  # Output: [1, 2, 3, 4, 5, 6]
