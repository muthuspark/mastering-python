list1 = [1, 2, 3, 4, 5]
list2 = [4, 5, 6, 7, 8]

intersection = list(filter(lambda x: x in list2, list1))

print(f"The intersection of the two lists is: {intersection}")