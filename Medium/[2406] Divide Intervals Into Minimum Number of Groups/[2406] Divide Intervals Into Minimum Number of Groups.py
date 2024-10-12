"""
Accepted
2406 [Medium]
Runtime: 1006 ms, faster than 96.20% of Python3 online submissions for Divide Intervals Into Minimum Number of Groups.
Memory Usage: 55.85 MB, less than 72.15% of Python3 online submissions for Divide Intervals Into Minimum Number of Groups.
"""
class Solution:
    def minGroups(self, intervals: List[List[int]]) -> int:
        N = len(intervals)
        start, end = [], []
        for left, right in intervals:
            start.append(left)
            end.append(right)

        start.sort()
        end.sort()

        left, right = 0, 0
        res = 0
        groups = 0

        while left < N:
            if start[left] <= end[right]:
                groups += 1
                left += 1
            else:
                groups -= 1
                right += 1
            res = max(res, groups)
        return res