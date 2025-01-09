def sum_odd_numbers_filter(numbers):
    """Calculates the sum of odd numbers in a list using filter and sum.

    Args:
      numbers: A list of integers.

    Returns:
      The sum of odd numbers in the list. Returns 0 if the list is empty or contains no odd numbers.
    """
    return sum(filter(lambda x: x % 2 != 0, numbers))

my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
odd_sum = sum_odd_numbers_filter(my_list)
print(f"The sum of odd numbers is: {odd_sum}") # Output: The sum of odd numbers is: 25