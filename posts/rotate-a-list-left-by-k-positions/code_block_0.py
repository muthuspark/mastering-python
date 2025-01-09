def rotate_left_slice(lst, k):
  """Rotates a list to the left by k positions using slicing.

  Args:
    lst: The list to be rotated.
    k: The number of positions to rotate.

  Returns:
    The rotated list.
  """
  k %= len(lst)  # Handle k larger than list length
  return lst[k:] + lst[:k]

my_list = [1, 2, 3, 4, 5]
rotated_list = rotate_left_slice(my_list, 2)
print(f"Original list: {my_list}")
print(f"Rotated list: {rotated_list}") 