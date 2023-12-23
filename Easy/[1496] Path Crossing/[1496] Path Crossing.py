"""
Accepted
1496 [Easy]
Runtime: 35 ms, faster than 77.06% of Python3 online submissions for Path Crossing.
Memory Usage: 17.58 MB, less than 5.49% of Python3 online submissions for Path Crossing.
"""
class Solution:
    def isPathCrossing(self, path: str) -> bool:
        points = [[0,0]]
        for direction in path:
            if direction == 'N':
                newPoint = [points[-1][0] + 1, points[-1][1]]
                if newPoint in points:
                    return True
                else:
                    points.append(newPoint)
            elif direction == 'S':
                newPoint = [points[-1][0] - 1, points[-1][1]]
                if newPoint in points:
                    return True
                else:
                    points.append(newPoint)
            elif direction == 'E':
                newPoint = [points[-1][0], points[-1][1] + 1]
                if newPoint in points:
                    return True
                else:
                    points.append(newPoint)
            else:
                newPoint = [points[-1][0], points[-1][1] - 1]
                if newPoint in points:
                    return True
                else:
                    points.append(newPoint)
                    
        return False