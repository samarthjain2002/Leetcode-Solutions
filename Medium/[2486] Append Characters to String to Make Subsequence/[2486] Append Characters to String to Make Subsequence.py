"""
Accepted
2486 [Medium]
Runtime: 73 ms, faster than 22.52% of Python3 online submissions for Append Characters to String to Make Subsequence.
Memory Usage: 16.85 MB, less than 100% of Python3 online submissions for Append Characters to String to Make Subsequence.
"""
class Solution:
    def appendCharacters(self, s: str, t: str) -> int:
        pointer = 0
        for i in range(len(s)):
            if pointer == len(t):
                return 0
            elif s[i] == t[pointer]:
                pointer += 1
        return len(t) - pointer