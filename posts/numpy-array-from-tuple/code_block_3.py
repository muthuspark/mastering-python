import numpy as np

my_tuple = (1, 2.5, '3')
my_array = np.array(my_tuple)
print(my_array)  #Output: ['1' '2.5' '3']  All elements become strings
print(my_array.dtype) # Output: <U32 (Unicode string of length 32)