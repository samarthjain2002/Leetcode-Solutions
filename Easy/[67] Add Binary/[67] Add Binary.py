"""
Accepted
67 [Easy]
Runtime: 45 ms, faster than 11.71% of Python3 online submissions for Length of Add Binary.
Memory Usage: 16.52 MB, less than 70.04% of Python3 online submissions for Length of Add Binary.
"""
class Solution:
    def addBinary(self, a: str, b: str) -> str:
        su = 0
        val = 1
        for i in a[::-1]:
            if i == '1':
                su += val
            val *= 2
        val = 1
        for i in b[::-1]:
            if i == '1':
                su += val
            val *= 2
        return bin(su)[2:]