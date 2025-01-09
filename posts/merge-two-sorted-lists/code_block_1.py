def merge_sorted_lists_recursive(list1, list2):
    """Merges two sorted lists recursively.

    Args:
        list1: The first sorted list.
        list2: The second sorted list.

    Returns:
        A new sorted list containing all elements from list1 and list2.
    """
    if not list1:
        return list2
    if not list2:
        return list1
    if list1[0] < list2[0]:
        return [list1[0]] + merge_sorted_lists_recursive(list1[1:], list2)
    else:
        return [list2[0]] + merge_sorted_lists_recursive(list1, list2[1:])

#Example usage
list1 = [2, 5, 8, 12]
list2 = [1, 3, 6, 9, 11]
merged_list = merge_sorted_lists_recursive(list1, list2)
print(f"Merged list (recursive): {merged_list}") # Output: Merged list (recursive): [1, 2, 3, 5, 6, 8, 9, 11, 12]