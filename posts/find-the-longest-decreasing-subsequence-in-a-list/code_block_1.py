def longest_decreasing_subsequence_with_reconstruction(nums):
    """
    Finds the longest decreasing subsequence and reconstructs the subsequence itself using dynamic programming.

    Args:
        nums: A list of numbers.

    Returns:
        A tuple containing (length, subsequence) of the longest decreasing subsequence.

    """
    n = len(nums)
    if n == 0:
        return 0, []

    dp = [1] * n
    predecessors = [-1] * n #to track predecessors in the subsequence

    for i in range(1, n):
        for j in range(i):
            if nums[i] < nums[j] and dp[i] < dp[j] + 1:
                dp[i] = dp[j] + 1
                predecessors[i] = j

    max_length = max(dp)
    max_index = dp.index(max_length)

    subsequence = []
    while max_index != -1:
        subsequence.insert(0, nums[max_index])
        max_index = predecessors[max_index]

    return max_length, subsequence

#Example
nums = [10, 9, 2, 5, 3, 7, 101, 18]
length, subsequence = longest_decreasing_subsequence_with_reconstruction(nums)
print(f"Length of the longest decreasing subsequence: {length}") #Output: 4
print(f"Longest decreasing subsequence: {subsequence}") #Output: [10, 9, 5, 3]
