"""
Accepted
812 [Easy]
Runtime: 47 ms, faster than 56.26% of Python3 online submissions for Largest Triangle Area.
Memory Usage: 17.96 MB, less than 30.76% of Python3 online submissions for Largest Triangle Area.
"""
class Solution:
    def largestTriangleArea(self, points: List[List[int]]) -> float:
        res = 0
        for i in range(len(points)):
            x1, y1 = points[i][0], points[i][1]
            for j in range(i + 1, len(points)):
                x2, y2 = points[j][0], points[j][1]
                for k in range(j + 1, len(points)):
                    x3, y3 = points[k][0], points[k][1]
                    res = max(res, 0.5 * abs((x1 * (y2 - y3)) + (x2 * (y3 - y1)) + (x3 * (y1 - y2))))
        return res