squares = []
for i in range(1000):
    squares.append(i**2)

squares = [i**2 for i in range(1000)]

squares_gen = (i**2 for i in range(1000))