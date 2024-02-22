"""
Accepted
268 [Easy]
Runtime: 1028 ms, faster than 14.11% of Python3 online submissions for Missing Number.
Memory Usage: 17.84 MB, less than 49.34% of Python3 online submissions for Missing Number.
"""
class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        for num in nums:
            if num != 0 and num - 1 not in nums:
                return num - 1
        return len(nums)