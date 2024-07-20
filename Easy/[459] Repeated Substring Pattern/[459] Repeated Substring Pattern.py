"""
Accepted
459 [Easy]
Runtime: 43 ms, faster than 62.86% of Python3 online submissions for Repeated Substring Pattern.
Memory Usage: 16.58 MB, less than 79.74% of Python3 online submissions for Repeated Substring Pattern.
"""
class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
        string = s + s
        if s in string[1 : -1]:
            return True
        else:
            return False