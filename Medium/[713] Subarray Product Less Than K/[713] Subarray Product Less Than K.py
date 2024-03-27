"""
Accepted
713 [Medium]
Runtime: 470 ms, faster than 99.59% of Python3 online submissions for Subarray Product Less Than K.
Memory Usage:  19.22 MB, less than 50.02% of Python3 online submissions for Subarray Product Less Than K.
"""
class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        N = len(nums)
        res = 0
        left = 0
        product = 1
        for right in range(N):
            product *= nums[right]
            while left <= right and product >= k:
                product = product // nums[left]
                left += 1
            res += (right - left + 1)
        return res