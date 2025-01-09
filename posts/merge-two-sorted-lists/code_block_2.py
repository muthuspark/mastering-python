import heapq

def merge_sorted_lists_heapq(list1, list2):
    """Merges two sorted lists using heapq.merge.

    Args:
        list1: The first sorted list.
        list2: The second sorted list.

    Returns:
        A new sorted list containing all elements from list1 and list2.

    """
    return list(heapq.merge(list1, list2))


list1 = [2, 5, 8, 12]
list2 = [1, 3, 6, 9, 11]
merged_list = merge_sorted_lists_heapq(list1, list2)
print(f"Merged list (heapq): {merged_list}") # Output: Merged list (heapq): [1, 2, 3, 5, 6, 8, 9, 11, 12]