import random

random_integer = random.randint(1, 10)
print(f"A random integer between 1 and 10: {random_integer}")

random_float = random.random()
print(f"A random float between 0 and 1: {random_float}")

my_list = [1, 2, 3, 4, 5]
random.shuffle(my_list)
print(f"Shuffled list: {my_list}")