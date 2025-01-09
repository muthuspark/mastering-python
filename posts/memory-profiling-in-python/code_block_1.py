@profile
def my_function(n):
    data = []
    for i in range(n):
        data.append(i * 2)
    return data

my_function(1000000)