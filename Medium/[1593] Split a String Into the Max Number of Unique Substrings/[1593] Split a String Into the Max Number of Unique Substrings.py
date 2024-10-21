"""
Accepted
1593 [Medium]
Runtime: 147 ms, faster than 92.38% of Python3 online submissions for Split a String Into the Max Number of Unique Substrings.
Memory Usage: 16.71 MB, less than 6.28% of Python3 online submissions for Split a String Into the Max Number of Unique Substrings.
"""
class Solution:
    def maxUniqueSplit(self, s: str) -> int:
        N = len(s)

        def backtrack(i, cur_set):
            if i == N:
                return 0

            res = 0
            for j in range(i, N):
                substring = s[i : j + 1]
                if substring not in cur_set:
                    cur_set.add(substring)
                    res = max(res, 1 + backtrack(j + 1, cur_set))
                    cur_set.remove(substring)

            return res            

        return backtrack(0, set())