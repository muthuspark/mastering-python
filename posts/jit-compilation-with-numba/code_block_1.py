from numba import jit

@jit(nopython=True)
def add_arrays(a, b):
    c = [0] * len(a)
    for i in range(len(a)):
        c[i] = a[i] + b[i]
    return c


a = [1, 2, 3, 4, 5]
b = [6, 7, 8, 9, 10]
result = add_arrays(a,b)
print(result) # Output: [7, 9, 11, 13, 15]