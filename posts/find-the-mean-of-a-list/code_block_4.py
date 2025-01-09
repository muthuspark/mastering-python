import statistics

my_list = [10, 20, 'a', 30, 40, 50]
numeric_list = [x for x in my_list if isinstance(x, (int, float))]
if numeric_list:
    mean = statistics.mean(numeric_list)
    print(f"The mean of the numeric elements is: {mean}") # Output: The mean of the numeric elements is: 30.0
else:
    print("The list contains no numeric elements.")
