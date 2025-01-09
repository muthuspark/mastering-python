def calculate_median(data):
    n = len(data)
    sorted_data = sorted(data)
    midpoint = n // 2

    if n % 2 == 1:  # Odd number of elements
        return sorted_data[midpoint]
    else:  # Even number of elements
        return (sorted_data[midpoint - 1] + sorted_data[midpoint]) / 2

data = [1, 3, 5, 2, 4]
median = calculate_median(data)
print(f"The median is: {median}")  # Output: The median is: 3

data2 = [1, 3, 5, 2, 4, 6]
median2 = calculate_median(data2)
print(f"The median is: {median2}") # Output: The median is: 3.5