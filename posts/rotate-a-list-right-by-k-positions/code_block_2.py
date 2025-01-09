def rotate_list_inplace(lst, k):
    """Rotates a list in-place by k positions."""
    n = len(lst)
    k %= n  # Handle k larger than list length

    def reverse(arr, start, end):
        while start < end:
            arr[start], arr[end] = arr[end], arr[start]
            start += 1
            end -= 1

    reverse(lst, 0, n - 1)
    reverse(lst, 0, k - 1)
    reverse(lst, k, n - 1)


my_list = [1, 2, 3, 4, 5]
rotate_list_inplace(my_list, 2)
print(f"Rotated list: {my_list}")  # Output: Rotated list: [4, 5, 1, 2, 3]
