"""
Accepted
1547 [Hard]
Runtime: 1306 ms, faster than 20.02% of Python3 online submissions for Minimum Cost to Cut a Stick.
Memory Usage: 21.64 MB, less than 22.53% of Python3 online submissions for Minimum Cost to Cut a Stick.
"""
class Solution:
    def minCost(self, n: int, cuts: List[int]) -> int:
        cuts += [0, n]
        cuts.sort()

        cache = {}
        def helper(low, high):
            if high - low <= 1:
                return 0

            if (low, high) in cache:
                return cache[(low, high)]

            min_cost = float("inf")
            for i in range(low + 1, high):
                cost = cuts[high] - cuts[low] + helper(low, i) + helper(i, high)
                min_cost = min(min_cost, cost)
            cache[(low, high)] = min_cost
            return min_cost


        return helper(0, len(cuts) - 1)