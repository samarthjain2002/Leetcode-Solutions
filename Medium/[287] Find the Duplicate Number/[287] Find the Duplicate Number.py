"""
Accepted
287 [Medium]
Runtime: 460 ms, faster than 71.59% of Python3 online submissions for Find the Duplicate Number.
Memory Usage:  30.50 MB, less than 57.70% of Python3 online submissions for Find the Duplicate Number.
"""
class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        slow, fast = nums[0], nums[nums[0]]
        while slow != fast:
            slow = nums[slow]
            fast = nums[nums[fast]]

        slow2 = 0
        while slow != slow2:
            slow = nums[slow]
            slow2 = nums[slow2]

        return slow