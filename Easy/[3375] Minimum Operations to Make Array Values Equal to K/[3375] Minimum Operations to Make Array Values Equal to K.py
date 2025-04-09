"""
Accepted
3375 [Easy]
Runtime: 70 ms, faster than 35.38% of Python3 online submissions for Minimum Operations to Make Array Values Equal to K.
Memory Usage: 17.64 MB, less than 75.47% of Python3 online submissions for Minimum Operations to Make Array Values Equal to K.
"""
class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        nums.sort()

        if min(nums) < k:
            return -1

        if nums[0] == k:
            return len(set(nums)) - 1
        else:
            return len(set(nums))