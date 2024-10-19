"""
Accepted
1545 [Medium]
Runtime: 1067 ms, faster than 8.68% of Python3 online submissions for Find Kth Bit in Nth Binary String.
Memory Usage: 24.76 MB, less than 28.60% of Python3 online submissions for Find Kth Bit in Nth Binary String.
"""
class Solution:
    def findKthBit(self, n: int, k: int) -> str:
        s = "0"
        for i in range(n):
            invert = ""
            for bit in s:
                invert += '1' if bit == '0' else '0'

            reverse = invert[ : : -1]

            s = s + "1" + reverse
        
        return s[k - 1]