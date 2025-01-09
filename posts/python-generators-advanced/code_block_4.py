def square(nums):
    for num in nums:
        yield num**2

def add_one(nums):
    for num in nums:
        yield num + 1


numbers = range(1, 5)
pipeline = add_one(square(numbers))  

for num in pipeline:
    print(num) # Output: 2, 5, 10, 17
