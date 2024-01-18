"""
Accepted
746 [Easy]
Runtime: 55 ms, faster than 78.39% of Python3 online submissions for Min Cost Climbing Stairs.
Memory Usage:  17.56 MB, less than 27.29% of Python3 online submissions for Min Cost Climbing Stairs.
"""
class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        cost.append(0)
        minCost = 0
        step_dp = [cost[0], cost[1]]
        for i in range(2, len(cost)):
            curStep = min(step_dp[i - 1], step_dp[i - 2]) + cost[i]
            step_dp.append(curStep)

        return step_dp[-1]