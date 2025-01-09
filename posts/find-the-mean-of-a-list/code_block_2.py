import statistics

my_list = []
try:
    mean = statistics.mean(my_list)
    print(f"The mean is: {mean}")
except statistics.StatisticsError:
    print("Cannot calculate the mean of an empty list.") # Output: Cannot calculate the mean of an empty list.
