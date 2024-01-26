"""
Accepted
516 [Medium]
Runtime: 1804 ms, faster than 21.47% of Python3 online submissions for Longest Palindromic Subsequence.
Memory Usage:  42.42 MB, less than 44.38% of Python3 online submissions for Longest Palindromic Subsequence.
"""
class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        M = len(s)

        revS = ""
        for char in s[::-1]:
            revS += char

        dp = [[0 for i in range(M + 1)] for j in range(M + 1)]
        for row in range(M + 1):
            for col in range(M + 1):
                if row == 0 or col == 0:
                    continue
                if s[row - 1] == revS[col - 1]:
                    dp[row][col] = dp[row - 1][col - 1] + 1
                else:
                    dp[row][col] = max(dp[row - 1][col], dp[row][col - 1])

        return dp[-1][-1]