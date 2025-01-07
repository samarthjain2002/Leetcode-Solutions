"""
Accepted
312 [Hard]
Runtime: 8001 ms, faster than 30.40% of Python3 online submissions for Burst Balloons.
Memory Usage: 34.10 MB, less than 20.09% of Python3 online submissions for Burst Balloons.
"""
# TC: O(n * n!), SC: O(n^2)
# TLE
class Solution:
    def maxCoins(self, nums: List[int]) -> int:
        def rec(nums):
            if len(nums) == 2:
                return 0
            elif len(nums) == 3:
                return nums[1]
            elif len(nums) == 4:
                return (nums[1] * nums[2]) + max(nums[1], nums[2])

            maxCoins = 0
            for i in range(1, len(nums) - 1):
                coins = nums[i - 1] * nums[i] * nums[i + 1]
                maxCoins = max(maxCoins, coins + rec(nums[ : i] + nums[i + 1 : ]))
            return maxCoins

        return rec([1] + nums + [1])



# TC: O(n * 2^n), SC: O(n * 2^n)
# TLE
class Solution:
    def maxCoins(self, nums: List[int]) -> int:
        dp = {}

        def rec(nums):
            if tuple(nums) in dp:
                return dp[tuple(nums)]

            if len(nums) == 2:
                return 0
            elif len(nums) == 3:
                return nums[1]
            elif len(nums) == 4:
                return (nums[1] * nums[2]) + max(nums[1], nums[2])

            maxCoins = 0
            for i in range(1, len(nums) - 1):
                coins = nums[i - 1] * nums[i] * nums[i + 1]
                maxCoins = max(maxCoins, coins + rec(nums[ : i] + nums[i + 1 : ]))
            dp[tuple(nums)] = maxCoins
            return dp[tuple(nums)]

        return rec([1] + nums + [1])



# TC: O(n^3), SC: O(n^2)
class Solution:
    def maxCoins(self, nums: List[int]) -> int:
        nums = [1] + nums + [1]
        dp = {}

        def rec(left, right):
            if left > right:
                return 0
            if (left, right) in dp:
                return dp[(left, right)]

            maxCoins = 0
            for i in range(left, right + 1):
                coins = nums[left - 1] * nums[i] * nums[right + 1]
                maxCoins = max(maxCoins, coins + rec(left, i - 1) + rec(i + 1, right))
            dp[(left, right)] = maxCoins
            return dp[(left, right)]

        return rec(1, len(nums) - 2)