"""
Accepted
1143 [Medium]
Runtime: 1526 ms, faster than 8.77% of Python3 online submissions for Longest Common Subsequence.
Memory Usage:  310.15 MB, less than 8.15% of Python3 online submissions for Longest Common Subsequence.
"""
class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        M, N = len(text1), len(text2)
        dp = {}
        
        def rec(i, j):
            if i == M or j == N:
                return 0
            if (i, j) in dp:
                return dp[(i, j)]

            if text1[i] == text2[j]:
                dp[(i, j)] = 1 + rec(i + 1, j + 1)
                return dp[(i, j)]
            else:
                dp[(i, j)] = max(rec(i + 1, j), rec(i, j + 1))
                return dp[(i, j)]

        return rec(0, 0)
    


"""
Runtime: 411 ms, faster than 85.90% of Python3 online submissions for Longest Common Subsequence.
Memory Usage:  42.78 MB, less than 45.28% of Python3 online submissions for Longest Common Subsequence.
"""
class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        M, N = len(text1), len(text2)
        dp = [[0] * (N + 1) for _ in range(M + 1)]

        for row in range(M - 1, -1, -1):
            for col in range(N - 1, -1, -1):
                if text1[row] == text2[col]:
                    dp[row][col] = 1 + dp[row + 1][col + 1]
                else:
                    dp[row][col] = max(dp[row + 1][col], dp[row][col + 1])
        return dp[0][0]