"""
Accepted
2864 [Easy]
Runtime: 43 ms, faster than 27.91% of Python3 online submissions for Maximum Odd Binary Number.
Memory Usage: 16.56 MB, less than 75.75% of Python3 online submissions for Maximum Odd Binary Number.
"""
class Solution:
    def maximumOddBinaryNumber(self, s: str) -> str:
        N = len(s)
        count = -1
        for bit in s:
            if bit == '1':
                count += 1
        
        newS = ""
        for i in range(N - 1):
            if count:
                newS += '1'
                count -= 1
            else:
                newS += '0'

        return newS + '1'