numbers = [1, 2, 3, 4, 5]
squared_numbers_generator = (number**2 for number in numbers)
for num in squared_numbers_generator:
    print(num) #Output: 1 4 9 16 25
