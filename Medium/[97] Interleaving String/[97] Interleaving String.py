"""
Accepted
97 [Medium]
Runtime: 49 ms, faster than 26.11% of Python3 online submissions for Interleaving String.
Memory Usage: 18.65 MB, less than 9.78% of Python3 online submissions for Interleaving String.
"""
class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        dp = {}

        def rec(i, j, k):
            if k == len(s3):
                if i == len(s1) and j == len(s2):
                    return True
                else:
                    return False
            if (i, j) in dp:
                return dp[(i, j)]

            res = False
            if i < len(s1) and s1[i] == s3[k]:
                res = rec(i + 1, j, k + 1)
            if not res and j < len(s2) and s2[j] == s3[k]:
                res = rec(i, j + 1, k + 1)
            dp[(i, j)] = res
            return dp[(i, j)]

        return rec(0, 0, 0)