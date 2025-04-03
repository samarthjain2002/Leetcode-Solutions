"""
Accepted
2874 [Easy]
Runtime: 183 ms, faster than 53.92% of Python3 online submissions for Maximum Value of an Ordered Triplet II.
Memory Usage: 28.87 MB, less than 100.00% of Python3 online submissions for Maximum Value of an Ordered Triplet II.
"""
class Solution:
    def maximumTripletValue(self, nums: List[int]) -> int:
        prefixMax = nums[0]
        maxDiff = 0
        res = 0
        for k in range(1, len(nums)):
            res = max(res, maxDiff * nums[k])
            
            prefixMax = max(prefixMax, nums[k])
            maxDiff = max(maxDiff, prefixMax - nums[k])
        return res