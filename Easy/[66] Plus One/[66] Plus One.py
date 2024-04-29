"""
Accepted
66 [Easy]
Runtime: 39 ms, faster than 40.34% of Python3 online submissions for Plus One.
Memory Usage: 16.52 MB, less than 40.06% of Python3 online submissions for Plus One.
"""
class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        num = ""
        for i in digits:
            num += str(i)
        num = str(int(num) + 1)
        digits = []
        for i in num:
            digits.append(int(i))
        return digits