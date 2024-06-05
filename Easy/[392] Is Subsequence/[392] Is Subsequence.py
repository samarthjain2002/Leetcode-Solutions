"""
Accepted
392 [Easy]
Runtime: 39 ms, faster than 33.25% of Python3 online submissions for Is Subsequence.
Memory Usage: 16.46 MB, less than 98.04% of Python3 online submissions for Is Subsequence.
"""
class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        N = len(s)
        pointer = 0
        for i in range(len(t)):
            if pointer == N:
                return True
            if t[i] == s[pointer]:
                pointer += 1
        return True if pointer == N else False