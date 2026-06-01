"""
Accepted
2144 [Easy]
Runtime: 0 ms, faster than 100.00% of Python3 online submissions for Minimum Cost of Buying Candies With Discount.
Memory Usage: 19.22 MB, less than 48.06% of Python3 online submissions for Minimum Cost of Buying Candies With Discount.
"""
class Solution:
    def minimumCost(self, cost: List[int]) -> int:
        cost.sort(reverse=True)

        res = 0
        for i in range(len(cost)):
            if i % 3 != 2:
                res += cost[i]
        return res



"""
Runtime: 0 ms, faster than 100.00% of Python3 online submissions for Minimum Cost of Buying Candies With Discount.
Memory Usage: 19.22 MB, less than 48.06% of Python3 online submissions for Minimum Cost of Buying Candies With Discount.
"""
class Solution:
    def minimumCost(self, cost: List[int]) -> int:
        cost.sort(reverse=True)

        res = 0
        i = 0
        while i < len(cost):
            res += cost[i]
            if i + 1 < len(cost):
                res += cost[i + 1]
            i = i + 3
        return res