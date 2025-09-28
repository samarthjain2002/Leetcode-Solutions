"""
Accepted
976 [Medium]
Runtime: 7 ms, faster than 97.69% of Python3 online submissions for Largest Perimeter Triangle.
Memory Usage: 18.97 MB, less than 45.57% of Python3 online submissions for Largest Perimeter Triangle.
"""
class Solution:
    def largestPerimeter(self, nums: List[int]) -> int:
        nums.sort()
        for i in range(len(nums) - 3, -1, -1):
            if nums[i] + nums[i + 1] > nums[i + 2]:
                return nums[i] + nums[i + 1] + nums[i + 2]
        return 0