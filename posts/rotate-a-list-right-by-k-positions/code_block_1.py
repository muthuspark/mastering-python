from collections import deque

def rotate_list_deque(lst, k):
  """Rotates a list to the right by k positions using deque.

  Args:
    lst: The list to rotate.
    k: The number of positions to rotate.

  Returns:
    The rotated list.
  """
  d = deque(lst)
  d.rotate(k)  # Rotate in-place
  return list(d)

my_list = [1, 2, 3, 4, 5]
rotated_list = rotate_list_deque(my_list, 2)
print(f"Rotated list: {rotated_list}")  # Output: Rotated list: [4, 5, 1, 2, 3]
