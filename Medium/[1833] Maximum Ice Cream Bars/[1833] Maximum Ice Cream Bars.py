"""
Accepted
1833 [Medium]
Runtime: 137 ms, faster than 5.89% of Python3 online submissions for Maximum Ice Cream Bars.
Memory Usage: 31.97 MB, less than 66.20% of Python3 online submissions for Maximum Ice Cream Bars.
"""
# Stable Counting Sort Solution
# TC: O(n + k), SC: O(n + k)
class Solution:
    def maxIceCream(self, costs: List[int], coins: int) -> int:
        # Stable Counting Sort: Ensures relative order of equal elements
        max_ele = max(costs)

        count = [0] * (max_ele + 1)
        for cost in costs:
            count[cost] += 1

        cumulative_count = [0] * (max_ele + 1)
        cur = 0
        for i, c in enumerate(count):
            cur += c
            cumulative_count[i] = cur

        sorted_costs = [0] * len(costs)
        # Loop backwards to preserve order of equal elements
        for i in range(len(costs) - 1, -1, -1):
            cost = costs[i]
            cumulative_count[cost] -= 1
            index = cumulative_count[cost]
            sorted_costs[index] = costs[i]
        
        res = 0
        for cost in sorted_costs:
            if cost > coins:
                break
            coins -= cost
            res += 1
        return res



"""
Runtime: 102 ms, faster than 13.33% of Python3 online submissions for Maximum Ice Cream Bars.
Memory Usage: 30.92 MB, less than 81.86% of Python3 online submissions for Maximum Ice Cream Bars.
"""
# Unstable Counting Sort Solution
# TC: O(n + k), SC: O(n + k)
class Solution:
    def maxIceCream(self, costs: List[int], coins: int) -> int:
        # Unstable Counting Sort: Does not ensure relative order of equal elements
        max_ele = max(costs)

        count = [0] * (max_ele + 1)
        for cost in costs:
            count[cost] += 1

        sorted_costs = []
        for i, c in enumerate(count):
            for _ in range(c):
                sorted_costs.append(i)
        
        res = 0
        for cost in sorted_costs:
            if cost > coins:
                break
            coins -= cost
            res += 1
        return res



"""
Runtime: 79 ms, faster than 69.30% of Python3 online submissions for Maximum Ice Cream Bars.
Memory Usage: 32.04 MB, less than 44.03% of Python3 online submissions for Maximum Ice Cream Bars.
"""
# Sorting Solution
# TC: O(nlog(n)), SC: O(n)
class Solution:
    def maxIceCream(self, costs: List[int], coins: int) -> int:
        costs.sort()
        
        res = 0
        for cost in costs:
            if cost > coins:
                break
            coins -= cost
            res += 1
        return res