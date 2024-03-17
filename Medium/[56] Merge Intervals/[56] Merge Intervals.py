"""
Accepted
56 [Medium]
Runtime: 121 ms, faster than 70.42% of Python3 online submissions for Merge Intervals.
Memory Usage: 20.71 MB, less than 41.13% of Python3 online submissions for Merge Intervals.
"""
class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        N = len(intervals)
        intervals.sort()
        res = [intervals[0]]
        for i in range(1, N):
            if intervals[i][0] > res[-1][1]:
                res.append(intervals[i])
            else:
                if intervals[i][1] > res[-1][1]:
                    res[-1][1] = intervals[i][1]

        return res