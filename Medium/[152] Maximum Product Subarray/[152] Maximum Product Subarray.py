"""
Accepted
152 [Medium]
Runtime: 11 ms, faster than 52.06% of Python3 online submissions for Maximum Product Subarray.
Memory Usage:  18.32 MB, less than 20.26% of Python3 online submissions for Maximum Product Subarray.
"""
class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        res = max(nums)
        curMin = curMax = 1

        for num in nums:
            temp = curMin * num
            curMin = min(curMin * num, curMax * num, num)
            curMax = max(temp, curMax * num, num)
            res = max(res, curMax)
        return res