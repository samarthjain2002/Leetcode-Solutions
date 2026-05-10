"""
Accepted
2770 [Medium]
Runtime: 539 ms, faster than 16.34% of Python3 online submissions for Maximum Number of Jumps to Reach the Last Index.
Memory Usage: 22.52 MB, less than 16.99% of Python3 online submissions for Maximum Number of Jumps to Reach the Last Index.
"""
class Solution:
    def maximumJumps(self, nums: List[int], target: int) -> int:
        cache = {}

        def rec(i):
            if i == len(nums) - 1:
                return 0

            if i in cache:
                return cache[(i)]

            res = float("-inf")
            for j in range(i + 1, len(nums)):
                if abs(nums[j] - nums[i]) <= target:
                    res = max(res, rec(j) + 1)

            cache[(i)] = res
            return cache[(i)]

        return max(-1, rec(0))



"""
Runtime: 2640 ms, faster than 5.23% of Python3 online submissions for Maximum Number of Jumps to Reach the Last Index.
Memory Usage: 602.33 MB, less than 9.15% of Python3 online submissions for Maximum Number of Jumps to Reach the Last Index.
"""
class Solution:
    def maximumJumps(self, nums: List[int], target: int) -> int:
        cache = {}

        def rec(i, prev):
            if i == len(nums):
                if prev == len(nums) - 1:
                    return 0
                return float("-inf")

            if (i, prev) in cache:
                return cache[(i, prev)]

            take = float("-inf")
            if abs(nums[i] - nums[prev]) <= target:
                take = 1 + rec(i + 1, i)
            skip = rec(i + 1, prev)

            cache[(i, prev)] = max(take, skip)
            return cache[(i, prev)]

        return max(-1, rec(1, 0))