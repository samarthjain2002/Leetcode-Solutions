"""
Accepted
58 [Easy]
Runtime: 38 ms, faster than 32.39% of Python3 online submissions for Length of Last Word.
Memory Usage: 16.59 MB, less than 82.28% of Python3 online submissions for Length of Last Word.
"""
class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        res = 0
        for char in s[::-1]:
            if char != ' ':
                res += 1
            elif char == ' ' and res > 0:
                return res
        return res