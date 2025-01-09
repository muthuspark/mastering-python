large_squares = [x**2 for x in range(1000000)]

large_squares_gen = (x**2 for x in range(1000000))

for sq in large_squares_gen:
    #Process each square efficiently
    pass # replace pass with your processing logic.