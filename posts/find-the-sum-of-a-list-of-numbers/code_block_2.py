from functools import reduce
import operator

numbers = [1, 2, 3, 4, 5]
total = reduce(operator.add, numbers)
print(f"The sum is: {total}")  # Output: The sum is: 15