"""
Accepted
1232 [Easy]
Runtime: 0 ms, faster than 100.00% of Python3 online submissions for Check If It Is a Straight Line.
Memory Usage: 18.36 MB, less than 12.18% of Python3 online submissions for Check If It Is a Straight Line.
"""
class Solution:
    def checkStraightLine(self, coordinates: List[List[int]]) -> bool:
        xDiff = coordinates[1][0] - coordinates[0][0]
        yDiff = coordinates[1][1] - coordinates[0][1]

        for i in range(len(coordinates) - 1):
            curXDiff = coordinates[i + 1][0] - coordinates[i][0]
            curYDiff = coordinates[i + 1][1] - coordinates[i][1]
            
            if yDiff * curXDiff != curYDiff * xDiff:
                return False
        return True