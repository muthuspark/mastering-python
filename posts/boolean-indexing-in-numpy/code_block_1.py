arr = np.array([10, 20, 30, 40, 50])

greater_than_25 = arr > 25
print(greater_than_25)  # Output: [False False  True  True  True]

result = arr[greater_than_25]
print(result)  # Output: [30 40 50]

within_range = (arr >= 20) & (arr <= 40) # Combining conditions with & (and) and | (or)
print(within_range) # Output: [False  True  True  True False]
result = arr[within_range]
print(result) # Output: [20 30 40]