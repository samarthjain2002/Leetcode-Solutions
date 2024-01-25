"""
Accepted
583 [Medium]
Runtime: 190 ms, faster than 55.20% of Python3 online submissions for Delete Operation for Two Strings.
Memory Usage:  18.40 MB, less than 86.74% of Python3 online submissions for Delete Operation for Two Strings.
"""
class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        M, N = len(word1), len(word2)
        dp = [[0 for i in range(N + 1)] for j in range(M + 1)]
        for row in range(M + 1):
            for col in range(N + 1):
                if row == 0 or col == 0:
                    continue
                if word1[row - 1] == word2[col - 1]:
                    dp[row][col] = dp[row - 1][col - 1] + 1
                else:
                    dp[row][col] = max(dp[row - 1][col], dp[row][col - 1])

        return (M - dp[-1][-1]) + (N - dp[-1][-1])
