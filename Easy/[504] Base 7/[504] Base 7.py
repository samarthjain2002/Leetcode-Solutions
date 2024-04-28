"""
Accepted
504 [Easy]
Runtime: 32 ms, faster than 76.94% of Python3 online submissions for Base 7.
Memory Usage: 16.60 MB, less than 65.49% of Python3 online submissions for Base 7.
"""
class Solution:
    def convertToBase7(self, num: int) -> str:
        if num == 0:
            return "0"
        negFlag = True if num < 0 else False
        num = abs(num)
        res = ""
        while num:
            rem = num % 7
            res = str(rem) + res
            num = num // 7
        return '-' + res if negFlag else res