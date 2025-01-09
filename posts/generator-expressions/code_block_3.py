nested_gen = ((x, y) for x in range(3) for y in range(3))
for pair in nested_gen:
    print(pair) #Output: (0,0), (0,1), (0,2), (1,0), (1,1), (1,2), (2,0), (2,1), (2,2)