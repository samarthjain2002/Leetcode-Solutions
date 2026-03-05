"""
Accepted
1545 [Medium]
Runtime: 0 ms, faster than 100.00% of Python3 online submissions for Find Kth Bit in Nth Binary String.
Memory Usage: 19.16 MB, less than 95.57% of Python3 online submissions for Find Kth Bit in Nth Binary String.
"""
# Recursion Solution
# TC: O(n), SC: O(n)
class Solution:
    # Input parameters are 1-indexed
    def findKthBit(self, n: int, k: int) -> str:
        # Base case
        if n == 1:
            return '0'

        # Length of the string
        length = 2**n - 1
        if k - 1 < length // 2:     # k in the first half of the string
            return self.findKthBit(n - 1, k)
        elif k - 1 == length // 2:  # k exactly in the middle of the string
            return '1'
        else:                       # k in the second half of the string
            # Reverse k, invert bit
            corresponding_bit = self.findKthBit(n - 1, length - k + 1)
            return '0' if corresponding_bit == '1' else '1'



"""
Runtime: 1067 ms, faster than 8.68% of Python3 online submissions for Find Kth Bit in Nth Binary String.
Memory Usage: 24.76 MB, less than 28.60% of Python3 online submissions for Find Kth Bit in Nth Binary String.
"""
# Brute Force Solution
# TC: O(2^n), SC: O(2^n)
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