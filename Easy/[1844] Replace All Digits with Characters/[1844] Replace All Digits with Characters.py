"""
Accepted
1844 [Easy]
Runtime: 41 ms, faster than 40.32% of Python3 online submissions for Replace All Digits with Characters.
Memory Usage: 16.2 MB, less than 70.79% of Python3 online submissions for Replace All Digits with Characters.
"""
class Solution:
    def replaceDigits(self, s: str) -> str:
        newS = ""
        for i in range(0,len(s)):
            if i%2 != 0:
                newS += chr(ord(s[i-1]) + int(s[i]))
            else:
                newS += s[i]

        return newS