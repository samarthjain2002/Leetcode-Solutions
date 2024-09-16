"""
Accepted
539 [Medium]
Runtime: 67 ms, faster than 73.57% of Python3 online submissions for Minimum Time Difference.
Memory Usage:  19.53 MB, less than 79.74% of Python3 online submissions for Minimum Time Difference.
"""
class Solution:
    def findMinDifference(self, timePoints: List[str]) -> int:
        for i, time in enumerate(timePoints):
            hours = int(time[ : 2])
            minutes = int(time[3 : ])
            timePoints[i] = hours * 60 + minutes

        timePoints.sort()
        res = float("inf")
        for i in range(len(timePoints) - 1):
            res = min(res, timePoints[i + 1] - timePoints[i])

        res = min(res, 1440 - timePoints[-1] + timePoints[0])
        return res