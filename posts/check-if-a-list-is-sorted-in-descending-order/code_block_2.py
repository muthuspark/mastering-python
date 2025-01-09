def is_sorted_descending_sorted(data):
    """Checks if a list is sorted in descending order by comparing to a sorted version.

    Args:
      data: The input list.

    Returns:
      True if the list is sorted in descending order, False otherwise.
    """
    return data == sorted(data, reverse=True)

my_list = [9, 7, 5, 3, 1]
print(f"Is {my_list} sorted descending (sorted)? {is_sorted_descending_sorted(my_list)}")  # Output: True

my_list = [9, 7, 10, 3, 1]
print(f"Is {my_list} sorted descending (sorted)? {is_sorted_descending_sorted(my_list)}")  # Output: False

my_list = []
print(f"Is {my_list} sorted descending (sorted)? {is_sorted_descending_sorted(my_list)}")  # Output: True

my_list = [5]
print(f"Is {my_list} sorted descending (sorted)? {is_sorted_descending_sorted(my_list)}")  # Output: True