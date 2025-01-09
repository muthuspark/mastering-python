data = [('apple', 10), ('banana', 5), ('cherry', 15), ('date', 2)]
indices = [1, 0, 3, 2] # index of a tuple

def sort_by_index_tuple(item):
  return indices[data.index(item)]

sorted_data = sorted(data, key=sort_by_index_tuple)

print(sorted_data) # Output: [('banana', 5), ('apple', 10), ('date', 2), ('cherry', 15)]