"""
Accepted
2914 [Medium]
Runtime: 15 ms, faster than 97.30% of Python3 online submissions for Minimum Number of Changes to Make Binary String Beautiful.
Memory Usage: 17.15 MB, less than 67.89% of Python3 online submissions for Minimum Number of Changes to Make Binary String Beautiful.
"""
class Solution:
    def minChanges(self, s: str) -> int:
        N = len(s)
        res = 0
        for i in range(0, N, 2):
            if s[i] != s[i + 1]:
                res += 1
        return res