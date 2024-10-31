"""
Accepted
2463 [Hard]
Runtime: 2361 ms, faster than 8.00% of Python3 online submissions for Minimum Total Distance Traveled.
Memory Usage: 116.07 MB, less than 19.73% of Python3 online submissions for Minimum Total Distance Traveled.
"""
class Solution:
    def minimumTotalDistance(self, robot: List[int], factory: List[List[int]]) -> int:
        robot.sort()
        factory.sort()

        expandedFactory = []
        for pos, limit in factory:
            for _ in range(limit):
                expandedFactory.append(pos)
        M, N = len(robot), len(expandedFactory)

        dp = [[-1 for _ in range(N)] for _ in range(M)]

        def minDistance(curRobot, curFactory):
            if curRobot == M:
                return 0
            if curFactory == N:
                return float("inf")

            if dp[curRobot][curFactory] != -1:
                return dp[curRobot][curFactory]

            repair = abs(robot[curRobot] - expandedFactory[curFactory]) + minDistance(curRobot + 1, curFactory + 1)
            skip = minDistance(curRobot, curFactory + 1)

            dp[curRobot][curFactory] = min(repair, skip)
            return dp[curRobot][curFactory]

        return minDistance(0, 0)