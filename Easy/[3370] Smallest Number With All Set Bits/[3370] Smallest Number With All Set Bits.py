"""
Accepted
3370 [Easy]
Runtime: 50 ms, faster than 47.34% of Python3 online submissions for Smallest Number With All Set Bits.
Memory Usage: 17.95 MB, less than 26.92% of Python3 online submissions for Smallest Number With All Set Bits.
"""
class Solution:
    def smallestNumber(self, n: int) -> int:
        num = 0
        for i in range(10):
            num += 2**i
            if n <= num:
                return num