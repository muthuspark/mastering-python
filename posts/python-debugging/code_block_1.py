import pdb

def buggy_function(x, y):
    pdb.set_trace() # Debugging starts here
    result = x / y
    return result

buggy_function(10, 0)