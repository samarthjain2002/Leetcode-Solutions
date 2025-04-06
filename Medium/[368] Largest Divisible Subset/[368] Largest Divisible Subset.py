"""
Accepted
368 [Medium]
Runtime: 227 ms, faster than 52.07% of Python3 online submissions for Largest Divisible Subset.
Memory Usage:  16.90 MB, less than 76.96% of Python3 online submissions for Largest Divisible Subset.
"""
class Solution:
    def largestDivisibleSubset(self, nums: List[int]) -> List[int]:
        nums.sort()
        dp = [[num] for num in nums]
        
        N = len(nums)
        res = []
        for i in range(N):
            for j in range(0, i):
                if nums[i] % nums[j] == 0:
                    if len(dp[j] + [nums[i]]) > len(dp[i]):
                        dp[i] = dp[j] + [nums[i]]

            if len(res) < len(dp[i]):
                res = dp[i]

        return res



"""
Runtime: 2005 ms, faster than 5.88% of Python3 online submissions for Largest Divisible Subset.
Memory Usage:  154.92 MB, less than 5.08% of Python3 online submissions for Largest Divisible Subset.
"""
# DFS + Memoization approach
# TC: O(n^2)
# SC: O(n^2)
class Solution:
    def largestDivisibleSubset(self, nums: List[int]) -> List[int]:
        nums.sort()

        cache = {}
        def dfs(i, prev):
            if i == len(nums):
                return []
            if (i, prev) in cache:
                return cache[(i, prev)]

            res = dfs(i + 1, prev)
            if nums[i] % prev == 0:
                temp = [nums[i]] + dfs(i + 1, nums[i])
                res = temp if len(temp) > len(res) else res

            cache[(i, prev)] = res
            return res


        return dfs(0, 1)