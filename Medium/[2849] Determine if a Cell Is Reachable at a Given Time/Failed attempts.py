"""
486 / 806 testcases passed
Input:
sx = 1
sy = 1
fx = 1
fy = 3
t = 2
Output: False
Expected: True
"""

class Solution:
    def isReachableAtTime(self, sx: int, sy: int, fx: int, fy: int, t: int) -> bool:
        while sy != fy:
            if t == 0:
                return False
            t -= 1
            #Moving diagonally
            if sx < fx:     #Start is to the left of Finish
                if sy < fy:     #Start is North-West of Finish
                    sx += 1
                    sy += 1
                else:           #Start is South-West Finish
                    sx += 1
                    sy -= 1
            elif sx > fx:   #Start is to the right of Finish 
                if sy < fy:     #Start is North-East of Finish
                    sx -= 1
                    sy += 1
                else:           #Start is South-East of Finish
                    sx -= 1
                    sy -= 1
            #Moving downwards
            else:           #Start is vertically alligned with Finsih
                if sy < fy:     #Start is directly above Finish
                    sy += 1
                else:           #Start is directly below Finish
                    sy -= 1

        while sx != sy:
            if t == 0:
                return False
            t -= 1
            #Start is horizontally alligned with Finish
            if sx < sy:     #Start is left of Finish
                sx += 1
            else:           #Start is right of Finish
                sx -= 1
    
        return True
    


"""
548 / 806 testcases passedInput:
sx = 1
sy = 1
fx = 2
fy = 1
t = 2
Output: False
Expected: True
"""
class Solution:
    def isReachableAtTime(self, sx: int, sy: int, fx: int, fy: int, t: int) -> bool:
        while sy != fy:
            print(sx,sy,t)
            if t == 0:
                print("NO")
                return False
            t -= 1
            #Moving diagonally
            if sx < fx:     #Start is to the left of Finish
                if sy < fy:     #Start is North-West of Finish
                    sx += 1
                    sy += 1
                else:           #Start is South-West Finish
                    sx += 1
                    sy -= 1
            elif sx > fx:   #Start is to the right of Finish 
                if sy < fy:     #Start is North-East of Finish
                    sx -= 1
                    sy += 1
                else:           #Start is South-East of Finish
                    sx -= 1
                    sy -= 1
            #Moving downwards
            else:           #Start is vertically alligned with Finsih
                print("YES")
                if sy < fy:     #Start is directly above Finish
                    sy += 1
                else:           #Start is directly below Finish
                    sy -= 1

        while sx != fx:
            if t == 0:
                print(sx,sy,t)
                print("NO")
                return False
            t -= 1
            #Start is horizontally alligned with Finish
            if sx < sy:     #Start is left of Finish
                sx += 1
            else:           #Start is right of Finish
                sx -= 1
    
        return True
    



"""
623 / 806 testcases passedInput:
sx = 1
sy = 2
fx = 1
fy = 2
t = 1
Output: True
Expected: False
"""
class Solution:
    def isReachableAtTime(self, sx: int, sy: int, fx: int, fy: int, t: int) -> bool:
        while sy != fy:
            print(sx,sy,t)
            if t == 0:
                print("NO")
                return False
            t -= 1
            #Moving diagonally
            if sx < fx:     #Start is to the left of Finish
                if sy < fy:     #Start is North-West of Finish
                    sx += 1
                    sy += 1
                else:           #Start is South-West Finish
                    sx += 1
                    sy -= 1
            elif sx > fx:   #Start is to the right of Finish 
                if sy < fy:     #Start is North-East of Finish
                    sx -= 1
                    sy += 1
                else:           #Start is South-East of Finish
                    sx -= 1
                    sy -= 1
            #Moving downwards
            else:           #Start is vertically alligned with Finsih
                print("YES")
                if sy < fy:     #Start is directly above Finish
                    sy += 1
                else:           #Start is directly below Finish
                    sy -= 1

        while sx != fx:
            if t == 0:
                print(sx,sy,t)
                print("NO")
                return False
            t -= 1
            #Start is horizontally alligned with Finish
            if sx < fx:     #Start is left of Finish
                sx += 1
            else:           #Start is right of Finish
                sx -= 1
    
        return True
    



class Solution:
    def isReachableAtTime(self, sx: int, sy: int, fx: int, fy: int, t: int) -> bool:
        while sy != fy:
            print(sx,sy,t)
            if t == 0:
                return False
            t -= 1
            #Moving diagonally
            if sx < fx:     #Start is to the left of Finish
                if sy < fy:     #Start is North-West of Finish
                    sx += 1
                    sy += 1
                else:           #Start is South-West Finish
                    sx += 1
                    sy -= 1
            elif sx > fx:   #Start is to the right of Finish 
                if sy < fy:     #Start is North-East of Finish
                    sx -= 1
                    sy += 1
                else:           #Start is South-East of Finish
                    sx -= 1
                    sy -= 1
            #Moving downwards
            else:           #Start is vertically alligned with Finsih
                if sy < fy:     #Start is directly above Finish
                    sy += 1
                else:           #Start is directly below Finish
                    sy -= 1

        while sx != fx:
            if t == 0:
                print(sx,sy,t)
                return False
            t -= 1
            #Start is horizontally alligned with Finish
            if sx < fx:     #Start is left of Finish
                sx += 1
            else:           #Start is right of Finish
                sx -= 1
    
        return True
    



"""
613 / 806 testcases passed
Input:
sx = 1
sy = 1
fx = 1
fy = 1
t = 3
Output: False
Expected: True
"""
class Solution:
    def isReachableAtTime(self, sx: int, sy: int, fx: int, fy: int, t: int) -> bool:
        if sx == fx and sy == fy and t != 0:       #Start is Finish
            return False
        while sy != fy:
            print(sx,sy,t)
            if t == 0:
                return False
            t -= 1
            #Moving diagonally
            if sx < fx:     #Start is to the left of Finish
                if sy < fy:     #Start is North-West of Finish
                    sx += 1
                    sy += 1
                else:           #Start is South-West Finish
                    sx += 1
                    sy -= 1
            elif sx > fx:   #Start is to the right of Finish 
                if sy < fy:     #Start is North-East of Finish
                    sx -= 1
                    sy += 1
                else:           #Start is South-East of Finish
                    sx -= 1
                    sy -= 1
            #Moving downwards
            else:           #Start is vertically alligned with Finsih
                if sy < fy:     #Start is directly above Finish
                    sy += 1
                else:           #Start is directly below Finish
                    sy -= 1

        while sx != fx:
            if t == 0:
                print(sx,sy,t)
                return False
            t -= 1
            #Start is horizontally alligned with Finish
            if sx < fx:     #Start is left of Finish
                sx += 1
            else:           #Start is right of Finish
                sx -= 1
    
        return True
    



"""
627 / 806 testcases passed
Output Limit Exceeded
Input:
sx = 870744264
sy = 360311537
fx = 820090827
fy = 890107308
t = 274809225
Output: False
Expected: True
"""
class Solution:
    def isReachableAtTime(self, sx: int, sy: int, fx: int, fy: int, t: int) -> bool:
        if sx == fx and sy == fy and t == 1:       #Start is Finish
            return False
        while sy != fy:
            print(sx,sy,t)
            if t == 0:
                return False
            t -= 1
            #Moving diagonally
            if sx < fx:     #Start is to the left of Finish
                if sy < fy:     #Start is North-West of Finish
                    sx += 1
                    sy += 1
                else:           #Start is South-West Finish
                    sx += 1
                    sy -= 1
            elif sx > fx:   #Start is to the right of Finish 
                if sy < fy:     #Start is North-East of Finish
                    sx -= 1
                    sy += 1
                else:           #Start is South-East of Finish
                    sx -= 1
                    sy -= 1
            #Moving downwards
            else:           #Start is vertically alligned with Finsih
                if sy < fy:     #Start is directly above Finish
                    sy += 1
                else:           #Start is directly below Finish
                    sy -= 1

        while sx != fx:
            if t == 0:
                print(sx,sy,t)
                return False
            t -= 1
            #Start is horizontally alligned with Finish
            if sx < fx:     #Start is left of Finish
                sx += 1
            else:           #Start is right of Finish
                sx -= 1
    
        return True
    



"""
Time Limit Exceeded
"""
class Solution:
    def isReachableAtTime(self, sx: int, sy: int, fx: int, fy: int, t: int) -> bool:
        if sx == fx and sy == fy and t == 1:       #Start is Finish
            return False
        while sy != fy:
            if t == 0:
                return False
            t -= 1
            #Moving diagonally
            if sx < fx:     #Start is to the left of Finish
                if sy < fy:     #Start is North-West of Finish
                    sx += 1
                    sy += 1
                else:           #Start is South-West Finish
                    sx += 1
                    sy -= 1
            elif sx > fx:   #Start is to the right of Finish 
                if sy < fy:     #Start is North-East of Finish
                    sx -= 1
                    sy += 1
                else:           #Start is South-East of Finish
                    sx -= 1
                    sy -= 1
            #Moving downwards
            else:           #Start is vertically alligned with Finsih
                if sy < fy:     #Start is directly above Finish
                    sy += 1
                else:           #Start is directly below Finish
                    sy -= 1

        while sx != fx:
            if t == 0:
                return False
            t -= 1
            #Start is horizontally alligned with Finish
            if sx < fx:     #Start is left of Finish
                sx += 1
            else:           #Start is right of Finish
                sx -= 1
    
        return True
    



"""
674 / 806 testcases passed
Input:
sx = 1
sy = 2
fx = 4
fy = 1
t = 0
Output: True
Expected: False
"""
class Solution:
    def isReachableAtTime(self, sx: int, sy: int, fx: int, fy: int, t: int) -> bool:
        if sx == fx and sy == fy and t == 1:       #Start is Finish
            return False
        
        if sx < fx:
            if sy < fy:
                minimum = min(fx - sx, fy - sy)
                sx += minimum
                sy += minimum
            else:
                minimum = min(fx - sx, fy - sy)
                sx += minimum
                sy -= minimum
            t -= minimum
        if sx > fx:
            if sy < fy:
                minimum = min(sx - fx, fy - sy)
                sx -= minimum
                sy += minimum
            else:
                minimum = min(fx - sx, fy - sy)
                sx -= minimum
                sy -= minimum
            t -= minimum

        if sx == fx:
            if sy > fy:
                t -= (sy - fy)
            else:
                t -= (fy -sy)
        
        if sy == fy:
            if sx > fx:
                t -= (sx - fx)
            else:
                t -= (fx - sx)

        if t < 0:
            return False
        else:
            return True
        



"""
727 / 806 testcases passed
Input:
sx = 2
sy = 5
fx = 1
fy = 1
t = 0
Output: True
Expected: False
"""
class Solution:
    def isReachableAtTime(self, sx: int, sy: int, fx: int, fy: int, t: int) -> bool:
        if sx == fx and sy == fy and t == 1:       #Start is Finish
            return False
        if sx < fx:
            if sy < fy:
                #If Finish is South-East of Start
                minimum = min(fx - sx, fy - sy)
                sx += minimum
                sy += minimum
            else:
                #If Finish is North-East of Start
                minimum = min(fx - sx, sy - fy)
                sx += minimum
                sy -= minimum
            t -= minimum
        if sx > fx:
            if sy < fy:
                #If Finish is South-West of Start
                minimum = min(sx - fx, fy - sy)
                sx -= minimum
                sy += minimum
            else:
                #If Finish is North-West of Start
                minimum = min(fx - sx, fy - sy)
                sx -= minimum
                sy -= minimum
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