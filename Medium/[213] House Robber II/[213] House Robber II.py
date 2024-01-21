"""
Accepted
213 [Medium]
Runtime: 45 ms, faster than 23.16% of Python3 online submissions for House Robber II.
Memory Usage:  16.53 MB, less than 57.92% of Python3 online submissions for House Robber II.
"""
class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
            
        def iterate(nums):
            N = len(nums)

            if N == 1:
                return nums[0]
            elif N == 2:
                return max(nums)
            elif N == 3:
                return max(nums[0] + nums[2], nums[1])
            else:
                nums[2] += nums[0]

            for i in range(3, N):
                nums[i] += max(nums[i - 2], nums[i - 3])

            return max(nums[-1], nums[-2])

        amount1 = iterate(nums[ : -1])
        amount2 = iterate(nums[1 : ])

        return max(amount1, amount2)