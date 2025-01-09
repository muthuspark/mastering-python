import gc

a = [1, 2, 3]  # Reference count is 1
b = a         # Reference count becomes 2
del a         # Reference count goes back to 1
del b         # Reference count becomes 0; object is garbage collected