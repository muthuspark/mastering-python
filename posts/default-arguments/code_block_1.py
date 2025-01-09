def add_item(item, my_list=[]):
  my_list.append(item)
  return my_list

print(add_item(1))  # Output: [1]
print(add_item(2))  # Output: [1, 2]  Unexpected!