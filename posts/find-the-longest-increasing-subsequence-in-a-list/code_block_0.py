def longest_increasing_subsequence(nums):
    if not nums:
        return []

    tails = []  # Stores the smallest tail of all increasing subsequences of a given length
    predecessors = {} #Keeps track of predecessors for reconstructing the subsequence

    for num in nums:
        if not tails or num > tails[-1]:
            if tails:
                predecessors[num] = tails[-1]
            tails.append(num)
        else:
            # Find the rightmost tail that is greater than or equal to the current number
            idx = 0
            l, r = 0, len(tails) -1
            while l <= r:
                mid = (l+r)//2
                if tails[mid] < num:
                    idx = mid + 1
                    l = mid + 1
                else:
                    r = mid -1

            if idx > 0:
                predecessors[num] = tails[idx-1]
            tails[idx] = num

    #Reconstruct the LIS by backtracking from the last element of tails
    lis = []
    current = tails[-1]
    while current is not None:
        lis.append(current)
        current = predecessors.get(current)

    return lis[::-1] # Reverse to get the correct order


#Example
nums = [10, 9, 2, 5, 3, 7, 101, 18]
print(longest_increasing_subsequence(nums)) # Output: [2, 3, 7, 101]

nums = [0,1,0,3,2,3]
print(longest_increasing_subsequence(nums)) # Output: [0, 1, 2, 3]

nums = [7,7,7,7,7,7,7]
print(longest_increasing_subsequence(nums)) # Output: [7]