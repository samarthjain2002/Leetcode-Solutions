"""
Accepted
1266 [Easy]
Runtime: 64 ms, faster than 55.91% of Python3 online submissions for Minimum Time Visiting All Points.
Memory Usage: 16.52 MB, less than 30.54% of Python3 online submissions for Minimum Time Visiting All Points.
"""
class Solution:
    def minTimeToVisitAllPoints(self, points: List[List[int]]) -> int:
        minTime = 0
        for i in range(1,len(points)):
            sx = points[i-1][0]
            fx = points[i][0]
            sy = points[i-1][1]
            fy = points[i][1]
            if sx < fx:
                if sy < fy:
                    #If Finish is South-East of Start
                    minimum = min(fx - sx, fy - sy)
                    sy += minimum
                else:
                    #If Finish is North-East of Start
                    minimum = min(fx - sx, sy - fy)
                    sy -= minimum
                sx += minimum
                minTime += minimum
            if sx > fx:
                if sy < fy:
                    #If Finish is South-West of Start
                    minimum = min(sx - fx, fy - sy)
                    sy += minimum
                else:
                    #If Finish is North-West of Start
                    minimum = min(sx - fx, sy - fy)
                    sy -= minimum
                sx -= minimum
                minTime += minimum

            if sx == fx:
                if sy > fy:
                    #When Finish is North of Start
                    minTime += (sy - fy)
                else:
                    #When Finish is South of Start
                    minTime += (fy -sy)
            
            if sy == fy:
                if sx > fx:
                    #When Finish is West of Start
                    minTime += (sx - fx)
                else:
                    #When Finish is East of Start
                    minTime += (fx - sx)
                    
        return minTime