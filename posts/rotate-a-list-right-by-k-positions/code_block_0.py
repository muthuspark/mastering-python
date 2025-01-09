def rotate_list_slicing(lst, k):
  """Rotates a list to the right by k positions using slicing.

  Args:
    lst: The list to rotate.
    k: The number of positions to rotate.

  Returns:
    The rotated list.
  """
  k %= len(lst)  # Handle k larger than list length
  return lst[-k:] + lst[:-k]

my_list = [1, 2, 3, 4, 5]
rotated_list = rotate_list_slicing(my_list, 2)
print(f"Rotated list: {rotated_list}")  # Output: Rotated list: [4, 5, 1, 2, 3]