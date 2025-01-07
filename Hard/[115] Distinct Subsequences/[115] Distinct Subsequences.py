"""
Accepted
115 [Hard]
Runtime: 1056 ms, faster than 6.16% of Python3 online submissions for Distinct Subsequences.
Memory Usage: 225.82 MB, less than 17.43% of Python3 online submissions for Distinct Subsequences.
"""
class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        dp = {}

        def rec(i, j):
            if j == len(t):
                return 1
            if i == len(s):
                return 0

            if (i, j) in dp:
                return dp[(i, j)]
            
            if s[i] == t[j]:
                dp[(i, j)] = rec(i + 1, j + 1) + rec(i + 1, j)
            else:
                dp[(i, j)] = rec(i + 1, j)
            return dp[(i, j)]

        return rec(0, 0)