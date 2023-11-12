"""
Accepted
2849 [Medium]
Runtime: 33 ms, faster than 91.31% of Python3 online submissions for Determine if a Cell Is Reachable at a Given Time.
Memory Usage: 16.36 MB, less than 12.00% of Python3 online submissions for Determine if a Cell Is Reachable at a Given Time.
"""
class Solution:
    def isReachableAtTime(self, sx: int, sy: int, fx: int, fy: int, t: int) -> bool:
        if sx == fx and sy == fy and t == 1:
            #Start is Finish
            return False

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
            t -= minimum
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
            t -= minimum

        if sx == fx:
            if sy > fy:
                #When Finish is North of Start
                t -= (sy - fy)
            else:
                #When Finish is South of Start
                t -= (fy -sy)
        
        if sy == fy:
            if sx > fx:
                #When Finish is West of Start
                t -= (sx - fx)
            else:
                #When Finish is East of Start
                t -= (fx - sx)

        if t < 0:
            return False
        else:
            return True