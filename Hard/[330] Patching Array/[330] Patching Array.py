"""
Accepted
330 [Hard]
Runtime: 60 ms, faster than 36.71% of Python3 online submissions for Patching Array.
Memory Usage: 16.73 MB, less than 27.97% of Python3 online submissions for Patching Array.
"""
class Solution:
    def minPatches(self, nums: List[int], n: int) -> int:
        N = len(nums)
        index = 0
        upto = 0
        res = 0
        while upto < n:
            if index < N and nums[index] <= upto + 1:
                upto += nums[index]
                index += 1
            else:
                res += 1
                upto = upto + (upto + 1)
        return res