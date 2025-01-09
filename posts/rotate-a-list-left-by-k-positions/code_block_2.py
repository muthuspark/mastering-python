def rotate_left_inplace(lst, k):
  """Rotates a list to the left by k positions in-place.

  Args:
    lst: The list to be rotated.
    k: The number of positions to rotate.
  """
  k %= len(lst)
  lst[:] = lst[k:] + lst[:k] #In place modification using slicing

my_list = [1, 2, 3, 4, 5]
rotate_left_inplace(my_list, 2)
print(f"Rotated list (in-place): {my_list}")
