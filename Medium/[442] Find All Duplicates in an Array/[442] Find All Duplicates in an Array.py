"""
Accepted
442 [Medium]
Runtime: 269 ms, faster than 48.16% of Python3 online submissions for Find All Duplicates in an Array.
Memory Usage:  24.66 MB, less than 67.78% of Python3 online submissions for Find All Duplicates in an Array.
"""
class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        N = len(nums)
        res = []
        for i, num in enumerate(nums):
            if nums[abs(num) - 1] < 0:
                res.append(abs(num))
            else:
                nums[abs(num) - 1] *= -1
        return res