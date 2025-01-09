import cProfile
import time

def my_slow_function(n):
    result = 0
    for i in range(n):
        for j in range(n):
            result += i * j
    return result

cProfile.run('my_slow_function(1000)')