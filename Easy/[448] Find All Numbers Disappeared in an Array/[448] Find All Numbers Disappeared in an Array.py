"""
Accepted
448 [Easy]
Runtime: 48 ms, faster than 17.37% of Python3 online submissions for Find All Numbers Disappeared in an Array.
Memory Usage: 31.06 MB, less than 39.24% of Python3 online submissions for Find All Numbers Disappeared in an Array.
"""
class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        for num in nums:
            i = abs(num) - 1
            nums[i] = -1 * abs(nums[i])

        res = []
        for i, num in enumerate(nums):
            if num > 0:
                res.append(i + 1)
        return res