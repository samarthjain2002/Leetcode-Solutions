"""
Accepted
1637 [Medium]
Runtime: 730 ms, faster than 85.98% of Python3 online submissions for Widest Vertical Area Between Two Points Containing No Points.
Memory Usage: 60.49 MB, less than 5.86% of Python3 online submissions for Widest Vertical Area Between Two Points Containing No Points.
"""
class Solution:
    def maxWidthOfVerticalArea(self, points: List[List[int]]) -> int:
        points.sort()
        widestArea = 0
        for i in range(len(points)-1):
            if points[i + 1][0] - points[i][0] > widestArea:
                widestArea = points[i + 1][0] - points[i][0]
        
        return widestArea