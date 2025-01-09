def longest_decreasing_subsequence_dp(nums):
    """
    Finds the longest decreasing subsequence using dynamic programming.

    Args:
        nums: A list of numbers.

    Returns:
        The length of the longest decreasing subsequence.
    """
    n = len(nums)
    if n == 0:
        return 0

    dp = [1] * n  # Initialize dp array with 1 (each element is a subsequence of length 1)

    for i in range(1, n):
        for j in range(i):
            if nums[i] < nums[j]:
                dp[i] = max(dp[i], dp[j] + 1)

    return max(dp)


#Example
nums = [10, 9, 2, 5, 3, 7, 101, 18]
length = longest_decreasing_subsequence_dp(nums)
print(f"Length of the longest decreasing subsequence: {length}") #Output: 4
