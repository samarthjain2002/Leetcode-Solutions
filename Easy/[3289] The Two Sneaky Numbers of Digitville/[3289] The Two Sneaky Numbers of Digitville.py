"""
Accepted
3289 [Easy]
Runtime: 7 ms, faster than 15.33% of Python3 online submissions for The Two Sneaky Numbers of Digitville.
Memory Usage: 17.94 MB, less than 20.87% of Python3 online submissions for The Two Sneaky Numbers of Digitville.
"""
# Bit Manipulation
# TC: O(n), SC: O(1)
class Solution:
    def getSneakyNumbers(self, nums: List[int]) -> List[int]:
        n = len(nums) - 2
        xor = 0
        for num in nums:
            xor = xor ^ num
        for i in range(n):
            xor = xor ^ i
        
        diff_bit = xor & -xor
        xor1 = xor2 = 0
        for num in nums:
            if num & diff_bit:
                xor1 = xor1 ^ num
            else:
                xor2 = xor2 ^ num
        for i in range(n):
            if i & diff_bit:
                xor1 = xor1 ^ i
            else:
                xor2 = xor2 ^ i
        
        return [xor1, xor2]