"""
Accepted
1903 [Easy]
Runtime: 54 ms, faster than 59.03% of Java online submissions for Largest Odd Number in String.
Memory Usage: 17.94 MB, less than 19.52% of Java online submissions for Largest Odd Number in String.
"""
class Solution:
    def largestOddNumber(self, num: str) -> str:
        for i in range(len(num)-1,-1,-1):
            if int(num[i]) % 2 != 0:
                return num[:i+1]
        return ""