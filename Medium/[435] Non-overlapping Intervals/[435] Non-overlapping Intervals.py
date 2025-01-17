"""
Accepted
435 [Medium]
Runtime: 180 ms, faster than 25.08% of Python3 online submissions for Non-overlapping Intervals.
Memory Usage: 51.53 MB, less than 13.63% of Python3 online submissions for Non-overlapping Intervals.
"""
class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort()
        i = 0
        res = 0
        for j in range(1, len(intervals)):
            if intervals[i][1] > intervals[j][0]:
                res += 1
                if intervals[i][1] > intervals[j][1]:
                    i = j
            else:
                i = j
        return res