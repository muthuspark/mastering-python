num = 0
bool_num = bool(num)
print(bool_num)  # Output: False

num2 = 10
bool_num2 = bool(num2)
print(bool_num2) # Output: True

empty_list = []
bool_list = bool(empty_list)
print(bool_list) # Output: False

non_empty_list = [1,2,3]
bool_list2 = bool(non_empty_list)
print(bool_list2) # Output: True