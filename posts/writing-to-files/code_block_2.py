my_list = ['apple', 'banana', 'cherry']

with open('my_list.txt', 'w') as f:
    for item in my_list:
        f.write(item + '\n')