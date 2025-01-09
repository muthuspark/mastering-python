def longest_palindrome_dp(s):
    n = len(s)
    if n < 2:
        return s
    dp = [[False] * n for _ in range(n)]
    start = 0
    max_len = 1
    for i in range(n):
        dp[i][i] = True  # Single characters are palindromes
    for i in range(n - 1):
        if s[i] == s[i + 1]:
            dp[i][i + 1] = True
            start = i
            max_len = 2
    for k in range(3, n + 1):
        for i in range(n - k + 1):
            j = i + k - 1
            if s[i] == s[j] and dp[i + 1][j - 1]:
                dp[i][j] = True
                if k > max_len:
                    start = i
                    max_len = k
    return s[start:start + max_len]


#Example Usage
string = "babad"
result = longest_palindrome_dp(string)
print(f"The longest palindromic substring of '{string}' is: {result}") # Output: bab or aba (both are correct)
