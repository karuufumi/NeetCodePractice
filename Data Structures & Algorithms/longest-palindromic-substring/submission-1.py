class Solution:
    def longestPalindrome(self, s: str) -> str:
        if len(s) == 1:
            return s

        if len(s) == 0:
            return ""

        start = 0
        max_length = 1
        n = len(s)

        dp = [[False] * n for _ in range(n)]

        for i in range(n):
            dp[i][i] = True

        for length in range(2, n + 1):

            for j in range(0, n - length + 1):

                k = j + length - 1
                if s[j] == s[k]:
                    if length == 2:
                        dp[j][k] = True
                    else:
                        dp[j][k] = dp[j + 1][k - 1]
                if dp[j][k] and length > max_length:
                    start = j
                    max_length = length
        return s[start:start + max_length]