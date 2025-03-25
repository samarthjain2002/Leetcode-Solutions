"""
Accepted
3394 [Medium]
Runtime: 407 ms, faster than 71.62% of Python3 online submissions for Check if Grid can be Cut into Sections.
Memory Usage: 83.60 MB, less than 70.72% of Python3 online submissions for Check if Grid can be Cut into Sections.
"""
class Solution:
    def checkValidCuts(self, n: int, rectangles: List[List[int]]) -> bool:
        horizontal = sorted([(r[1], r[3]) for r in rectangles])
        vertical = sorted([(r[0], r[2]) for r in rectangles])

        curPos = 0
        count1 = -1
        for rec in horizontal:
            if curPos <= rec[0]:
                count1 += 1
            curPos = max(curPos, rec[1])
        
        curPos = 0
        count2 = -1
        for rec in vertical:
            if curPos <= rec[0]:
                count2 += 1
            curPos = max(curPos, rec[1])
            
        return count1 >= 2 or count2 >= 2