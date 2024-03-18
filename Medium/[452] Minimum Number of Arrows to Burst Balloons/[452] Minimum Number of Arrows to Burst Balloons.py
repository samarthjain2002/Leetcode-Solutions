"""
Accepted
452 [Medium]
Runtime: 1096 ms, faster than 37.65% of Python3 online submissions for Minimum Number of Arrows to Burst Balloons.
Memory Usage:  62.11 MB, less than 91.41% of Python3 online submissions for Minimum Number of Arrows to Burst Balloons.
"""
class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        points.sort()
        N = len(points)
        res = 1
        end = points[0][1]
        for i in range(1, N):
            if points[i][0] <= end:
                end = min(end, points[i][1])
            else:
                res += 1
                end = points[i][1]

        return res