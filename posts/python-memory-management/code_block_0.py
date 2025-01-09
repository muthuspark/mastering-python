import gc

a = [1, 2, 3]  # Reference count is 1
b = a          # Reference count becomes 2
del a          # Reference count is now 1
del b          # Reference count is now 0. The list is garbage collected.

print(gc.collect()) # forces garbage collection, may print the number of collected objects.