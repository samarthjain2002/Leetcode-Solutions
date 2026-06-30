"""
Accepted
1770 [Hard]
Runtime: 579 ms, faster than 17.29% of Python3 online submissions for Maximum Score from Performing Multiplication Operations.
Memory Usage: 169.94 MB, less than 45.24% of Python3 online submissions for Maximum Score from Performing Multiplication Operations.
"""
# Dynamic Programming + Memoization Solution
# TC: O(m^2), SC: O(m^2)
class Solution:
    def maximumScore(self, nums: List[int], multipliers: List[int]) -> int:
        n, m = len(nums), len(multipliers)

        cache = {}
        def rec(i, left):
            if i == m:
                return 0

            if (i, left) in cache:
                return cache[(i, left)]

            right = (n - 1) - (i - left)

            cache[(i, left)] = max(
                multipliers[i] * nums[left] + rec(i + 1, left + 1),
                multipliers[i] * nums[right] + rec(i + 1, left)
            )
            return cache[(i, left)]

        return rec(0, 0)