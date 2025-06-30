"""
Accepted
376 [Medium]
Runtime: 227 ms, faster than 52.07% of Python3 online submissions for Wiggle Subsequence.
Memory Usage: 16.90 MB, less than 76.96% of Python3 online submissions for Wiggle Subsequence.
"""
class Solution:
    def wiggleMaxLength(self, nums: List[int]) -> int:
        cache = {}
        def dfs(i, getBigger, prev):
            if i == len(nums):
                return 0
            if (i, getBigger, prev) in cache:
                return cache[(i, getBigger, prev)]

            optionA = float("-inf")
            if getBigger and prev < nums[i]:
                optionA = 1 + dfs(i + 1, False, nums[i])
            elif not getBigger and prev > nums[i]:
                optionA = 1 + dfs(i + 1, True, nums[i])

            optionB = dfs(i + 1, getBigger, prev)

            cache[(i, getBigger, prev)] = max(optionA, optionB)
            return cache[(i, getBigger, prev)]

        return max(dfs(0, True, float("-inf")), dfs(0, False, float("inf")))