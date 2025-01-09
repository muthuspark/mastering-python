def cy_sum_squares(int n):
    cdef int i
    cdef long long total = 0  # Specify data types for optimization
    for i in range(n):
        total += i*i
    return total