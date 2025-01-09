list1 = [1, 2, 3, 4, 5]
list2 = [3, 5, 6, 7, 8]

common_elements = []
for x in list1:
    for y in list2:
        if x == y:
            common_elements.append(x)
            break #Optimization: avoid unnecessary checks after a match

print(f"Common elements using nested loops: {common_elements}")