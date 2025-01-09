from collections import deque

def rotate_left_deque(lst, k):
  """Rotates a list to the left by k positions using deque.

  Args:
    lst: The list to be rotated.
    k: The number of positions to rotate.

  Returns:
    The rotated list.
  """
  d = deque(lst)
  d.rotate(-k) # Negative k rotates left
  return list(d)

my_list = [1, 2, 3, 4, 5]
rotated_list = rotate_left_deque(my_list, 2)
print(f"Original list: {my_list}")
print(f"Rotated list: {rotated_list}")