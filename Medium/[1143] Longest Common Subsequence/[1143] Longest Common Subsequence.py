"""
Accepted
1143 [Medium]
Runtime: 537 ms, faster than 68.98% of Python3 online submissions for Longest Common Subsequence.
Memory Usage:  42.49 MB, less than 61.98% of Python3 online submissions for Longest Common Subsequence.
"""
class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        M, N = len(text1), len(text2)
        dp = [[0 for i in range(N + 1)] for j in range(M + 1)]
        for row in range(M + 1):
            for col in range(N + 1):
                if row == 0 or col == 0:
                    continue
                if text1[row - 1] == text2[col - 1]:
                    dp[row][col] = dp[row - 1][col - 1] + 1
                else:
                    dp[row][col] = max(dp[row - 1][col], dp[row][col - 1])

        return dp[-1][-1]