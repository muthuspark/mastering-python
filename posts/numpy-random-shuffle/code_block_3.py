import numpy as np

np.random.seed(42) # Set the seed

my_array = np.array([1, 2, 3, 4, 5])
np.random.shuffle(my_array)
print(my_array)

np.random.seed(42) # Same seed, same shuffle
my_array = np.array([1, 2, 3, 4, 5])
np.random.shuffle(my_array)
print(my_array)