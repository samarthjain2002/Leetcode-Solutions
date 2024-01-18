"""
Accepted
70 [Easy]
Runtime: 33 ms, faster than 81.50% of Python3 online submissions for Climbing Stairs.
Memory Usage: 17.44 MB, less than 15.77% of Python3 online submissions for Climbing Stairs.
"""
class Solution:
    def climbStairs(self, n: int) -> int:
        step_dp = []
        for i in range(1, n + 1):
            count = 0
            if i == 1:
                step_dp.append(1)
            elif i == 2:
                step_dp.append(2)
            else:
                step_dp.append(step_dp[i - 2] + step_dp[i - 3])

        return step_dp[-1]