import random

random_integer = random.randint(1, 10)
print(f"Random integer: {random_integer}")

random_float = random.random()
print(f"Random float: {random_float}")

my_list = [1, 2, 3, 4, 5]
random.shuffle(my_list)
print(f"Shuffled list: {my_list}")