"""
Accepted
10 [Hard]
Runtime: 3 ms, faster than 94.54% of Python3 online submissions for Regular Expression Matching.
Memory Usage: 18.16 MB, less than 6.82% of Python3 online submissions for Regular Expression Matching.
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
                # Rest of p pattern should match an "" string (Ex: "x*.*y*")
                if j + 1 < len(p) and p[j + 1] == '*':
                    return rec(i, j + 2)
                else:
                    return False

            if (i, j) in dp:
                return dp[(i, j)]

            if s[i] == p[j]:
                if j + 1 < len(p) and p[j + 1] == '*':
                    dp[(i, j)] = rec(i, j + 2) or rec(i + 1, j + 2) or rec(i + 1, j)
                else:
                    dp[(i, j)] = rec(i + 1, j + 1)
            elif p[j] == '.':
                # Matches everything ahead
                if j + 1 < len(p) and p[j + 1] == '*' and j + 2 == len(p):
                    dp[(i, j)] = True
                elif j + 1 < len(p) and p[j + 1] == '*':
                    dp[(i, j)] = rec(i, j + 2) or rec(i + 1, j)
                else:
                    dp[(i, j)] = rec(i + 1, j + 1)
            else:
                if j + 1 < len(p) and p[j + 1] == '*':
                    dp[(i, j)] = rec(i, j + 2)
                else:
                    dp[(i, j)] = False
            return dp[(i, j)]

        return rec(0, 0)