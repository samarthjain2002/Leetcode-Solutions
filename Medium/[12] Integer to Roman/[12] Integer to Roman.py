"""
Accepted
12 [Medium]
Runtime: 53 ms, faster than 26.12% of Python3 online submissions for Integer to Roman.
Memory Usage: 16.59 MB, less than 58.10% of Python3 online submissions for Integer to Roman.
"""
class Solution:
    def intToRoman(self, num: int) -> str:
        symList = [['I', 1], ['IV', 4], ['V', 5], ['IX', 9], ['X', 10],
            ['XL', 40], ['L', 50], ['XC', 90], ['C', 100],
            ['CD', 400], ['D', 500], ['CM', 900], ['M', 1000]]

        res = ""
        for sym, val in reversed(symList):
            if num // val:
                count = num // val
                res += sym * count
                num %= val
                
        return res