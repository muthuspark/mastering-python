def is_sorted_slice(data):
    """Checks if a list is sorted using slicing and comparison (less readable, potentially more efficient for large lists).

    Args:
        data: The list to check.

    Returns:
        True if the list is sorted, False otherwise.
    """
    return data == sorted(data)


my_list = [1, 2, 3, 4, 5]
print(f"Is {my_list} sorted? {is_sorted_slice(my_list)}")  # Output: True

my_list = [1, 3, 2, 4, 5]
print(f"Is {my_list} sorted? {is_sorted_slice(my_list)}")  # Output: False

my_list = [] #Handle empty list case
print(f"Is {my_list} sorted? {is_sorted_slice(my_list)}")  # Output: True

my_list = [5] #Handle single element list case
print(f"Is {my_list} sorted? {is_sorted_slice(my_list)}")  # Output: True