vectors_a = np.array([[1, 2, 3],
                     [4, 5, 6],
                     [7, 8, 9]])

vectors_b = np.array([[10, 11, 12],
                     [13, 14, 15],
                     [16, 17, 18]])

cross_products = np.cross(vectors_a, vectors_b, axisa=0, axisb=0)
print(cross_products)

#Output will be an array where each row represents the cross product of the corresponding rows from vectors_a and vectors_b