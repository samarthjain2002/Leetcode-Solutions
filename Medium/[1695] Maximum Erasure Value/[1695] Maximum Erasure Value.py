"""
Accepted
1695 [Medium]
Runtime: 199 ms, faster than 71.68% of Python3 online submissions for Maximum Erasure Value.
Memory Usage: 28.79 MB, less than 78.00% of Python3 online submissions for Maximum Erasure Value.
"""
class Solution:
    def maximumUniqueSubarray(self, nums: List[int]) -> int:
        left = 0
        curSum = 0
        res = 0
        uniq = set()
        for right in range(len(nums)):
            while nums[right] in uniq and nums[left] != nums[right]:
                curSum -= nums[left]
                uniq.remove(nums[left])
                left += 1
            if left < right and nums[left] == nums[right]:
                curSum -= nums[left]
                left += 1
            
            uniq.add(nums[right])
            curSum += nums[right]
            res = max(res, curSum)
        return res