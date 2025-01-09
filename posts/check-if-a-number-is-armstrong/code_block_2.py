def find_armstrong_numbers_in_range(start, end):
    """Finds all Armstrong numbers within a specified range."""
    armstrong_numbers = []
    for num in range(start, end + 1):
        if is_armstrong_number_efficient(num):  #Use efficient method
            armstrong_numbers.append(num)
    return armstrong_numbers

print(find_armstrong_numbers_in_range(100, 1000))
