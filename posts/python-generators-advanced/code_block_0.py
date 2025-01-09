squares = [x**2 for x in range(10)] 

squares_gen = (x**2 for x in range(10))

for i in squares_gen:
    print(i)

large_numbers = (i for i in range(10000000)) # No memory issue