import numpy as np

my_array = np.arange(10)
print(my_array)  # Output: [0 1 2 3 4 5 6 7 8 9]

my_array = np.arange(2, 12, 2) #start at 2, stop before 12, step of 2
print(my_array)  # Output: [ 2  4  6  8 10]

#Using floats
my_array = np.arange(0.0, 1.0, 0.1)
print(my_array) #Output: [0.  0.1 0.2 0.3 0.4 0.5 0.6 0.7 0.8 0.9]
