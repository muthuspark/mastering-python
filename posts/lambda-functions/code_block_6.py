points = [(1, 2), (4, 1), (9, 10)]
sorted_points = sorted(points, key=lambda point: point[0]) #Sort by the first element of the tuple
print(sorted_points) # Output: [(1, 2), (4, 1), (9, 10)]

sorted_points_y = sorted(points, key=lambda point: point[1]) #Sort by the second element of the tuple

print(sorted_points_y) # Output: [(4, 1), (1, 2), (9, 10)]
