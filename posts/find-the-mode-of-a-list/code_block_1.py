import statistics

def find_mode_statistics(data):
    """Finds the mode of a list using the statistics module.

    Args:
      data: A list of numbers.

    Returns:
      The mode of the list. Raises StatisticsError if the list is empty or has no unique mode.
    """
    try:
        return statistics.mode(data)
    except statistics.StatisticsError:
        return None

data = [1, 2, 3, 2, 4, 2, 5]
mode = find_mode_statistics(data)
print(f"The mode of {data} is: {mode}")  # Output: The mode of [1, 2, 3, 2, 4, 2, 5] is: 2

data = [1, 2, 3, 4, 5]
mode = find_mode_statistics(data)
print(f"The mode of {data} is: {mode}") #Output will raise error as no unique mode exists
