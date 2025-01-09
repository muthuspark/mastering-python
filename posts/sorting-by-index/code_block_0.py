data = ['apple', 'banana', 'cherry', 'date']
indices = [3, 0, 2, 1]

zipped = zip(indices, data)

sorted_data = [item for _, item in sorted(zipped)]

print(sorted_data)  # Output: ['date', 'apple', 'cherry', 'banana']