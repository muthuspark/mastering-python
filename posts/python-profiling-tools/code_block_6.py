@profile
def memory_intensive_function(n):
    data = [i * i for i in range(n)] # Create large list
    return data

memory_intensive_function(1000000)