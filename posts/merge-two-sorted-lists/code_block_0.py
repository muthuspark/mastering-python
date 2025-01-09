def merge_sorted_lists_iterative(list1, list2):
    """Merges two sorted lists iteratively.

    Args:
        list1: The first sorted list.
        list2: The second sorted list.

    Returns:
        A new sorted list containing all elements from list1 and list2.
    """
    merged_list = []
    i = j = 0
    while i < len(list1) and j < len(list2):
        if list1[i] < list2[j]:
            merged_list.append(list1[i])
            i += 1
        else:
            merged_list.append(list2[j])
            j += 1
    merged_list.extend(list1[i:])  # Add remaining elements from list1
    merged_list.extend(list2[j:])  # Add remaining elements from list2
    return merged_list

list1 = [2, 5, 8, 12]
list2 = [1, 3, 6, 9, 11]
merged_list = merge_sorted_lists_iterative(list1, list2)
print(f"Merged list (iterative): {merged_list}") #Output: Merged list (iterative): [1, 2, 3, 5, 6, 8, 9, 11, 12]
