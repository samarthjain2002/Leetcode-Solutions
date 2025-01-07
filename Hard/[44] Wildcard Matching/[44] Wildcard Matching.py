"""
Accepted
44 [Hard]
Runtime: 498 ms, faster than 18.16% of Python3 online submissions for Wildcard Matching.
Memory Usage: 134.04 MB, less than 10.22% of Python3 online submissions for Wildcard Matching.
"""
class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        dp = {}

        def rec(i, j):
            if i == len(s) and j == len(p):
                return True
            elif j == len(p):
                return False
            elif i == len(s):
                while j < len(p):
                    if p[j] != '*':
                        return False
                    j += 1
                return True

            if (i, j) in dp:
                return dp[(i, j)]

            if s[i] == p[j] or p[j] == '?':
                dp[(i, j)] = rec(i + 1, j + 1)
            elif p[j] == '*':
                dp[(i, j)] = rec(i + 1, j) or rec(i, j + 1)
            else:
                dp[(i, j)] = False
            return dp[(i, j)]

        return rec(0, 0)