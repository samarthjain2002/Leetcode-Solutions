"""
Accepted
3110 [Easy]
Runtime: 31 ms, faster than 88.69% of Python3 online submissions for Score of a String.
Memory Usage: 16.42 MB, less than 82.79% of Python3 online submissions for Score of a String.
"""
class Solution:
    def scoreOfString(self, s: str) -> int:
        res = 0
        for i in range(1,len(s)):
            res += abs(ord(s[i]) - ord(s[i - 1]))
        return res