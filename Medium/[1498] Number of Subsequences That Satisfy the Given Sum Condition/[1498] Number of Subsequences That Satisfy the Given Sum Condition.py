"""
Accepted
1498 [Medium]
Runtime: 6427 ms, faster than 5.99% of Python online submissions for Number of Subsequences That Satisfy the Given Sum Condition.
Memory Usage: 28.42 MB, less than 9.17% of Python online submissions for Number of Subsequences That Satisfy the Given Sum Condition.
"""
class Solution:
    def numSubseq(self, nums: List[int], target: int) -> int:
        MOD = 10**9 + 7
        nums.sort()

        left, right = 0, len(nums) - 1
        res = 0
        while left <= right:
            if nums[left] + nums[right] <= target:
                res += (2**(right - left))
                res = res % MOD
                left += 1
            else:
                right -= 1
        return res