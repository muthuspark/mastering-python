result_add = timedeltas + np.array([4, 5, 6], dtype='timedelta64[D]')
print(result_add)

result_sub = timedeltas - np.array([1, 1, 1], dtype='timedelta64[D]')
print(result_sub)


result_mul = timedeltas * 2
print(result_mul)

result_div = timedeltas / 2 #this will result in a float
print(result_div)
