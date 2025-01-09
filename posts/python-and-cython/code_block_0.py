def py_sum_squares(n):
    total = 0
    for i in range(n):
        total += i*i
    return total

print(py_sum_squares(1000000))