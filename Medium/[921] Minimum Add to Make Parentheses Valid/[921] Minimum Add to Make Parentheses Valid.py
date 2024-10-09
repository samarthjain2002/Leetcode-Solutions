"""
Accepted
921 [Medium]
Runtime: 35 ms, faster than 55.22% of Python3 online submissions for Minimum Add to Make Parentheses Valid.
Memory Usage: 16.56 MB, less than 30.64% of Python3 online submissions for Minimum Add to Make Parentheses Valid.
"""
class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        openPar = 0
        res = 0
        for par in s:
            if par == ')':
                if openPar:
                    openPar -= 1
                else:
                    res += 1
            else:
                openPar += 1
        return res + openPar