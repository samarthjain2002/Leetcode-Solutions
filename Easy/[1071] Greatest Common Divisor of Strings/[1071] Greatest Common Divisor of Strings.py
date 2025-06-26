"""
Accepted
1071 [Easy]
Runtime: 0 ms, faster than 100.00% of Python3 online submissions for Greatest Common Divisor of Strings.
Memory Usage: 17.81 MB, less than 46.70% of Python3 online submissions for Greatest Common Divisor of Strings.
"""
class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        def isDivisor(length):
            if len(str1) % length or len(str2) % length:
                return False

            factor1, factor2 = len(str1) // length, len(str2) // length
            return str1 == str1[ : length] * factor1 and str2 == str1[ : length] * factor2
            

        for i in range(min(len(str1), len(str2)), 0, -1):
            if isDivisor(i):
                return str1[ : i]
        return ""