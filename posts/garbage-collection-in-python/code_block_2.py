import gc
import sys

#Allocate some large objects.

large_list = [i for i in range(1000000)]
large_dict = {i: i**2 for i in range(1000000)}

print(f"Memory usage before garbage collection: {sys.getsizeof(large_list) + sys.getsizeof(large_dict)} bytes")

gc.collect()

print(f"Memory usage after garbage collection: {sys.getsizeof(large_list) + sys.getsizeof(large_dict)} bytes") #Note that size difference might be less than expected due to how Python manages memory.


del large_list
del large_dict

gc.collect()

