"""
Accepted
57 [Medium]
Runtime: 78 ms, faster than 41.35% of Python3 online submissions for Insert Interval.
Memory Usage: 19.80 MB, less than 79.86% of Python3 online submissions for Insert Interval.
"""
class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        intervals.append(newInterval)
        intervals.sort()
        N = len(intervals)
        res = [intervals[0]]
        for i in range(1, N):
            if intervals[i][0] > res[-1][1]:
                res.append(intervals[i])
            else:
                if intervals[i][1] > res[-1][1]:
                    res[-1][1] = intervals[i][1]

        return res