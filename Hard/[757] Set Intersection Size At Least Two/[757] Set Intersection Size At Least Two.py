"""
Accepted
757 [Hard]
Runtime: 16 ms, faster than 17.93% of Python3 online submissions for Set Intersection Size At Least Two.
Memory Usage: 18.86 MB, less than 93.10% of Python3 online submissions for Set Intersection Size At Least Two.
"""
# Sorting + Greedy Solution
# TC: O(nlog(n)), SC: O(1)
class Solution:
    def intersectionSizeTwo(self, intervals: List[List[int]]) -> int:
        res = 0
        p1 = p2 = -1
        # Sort start asc
        # Sort end desc
        intervals.sort(key=lambda interval: (interval[1], -interval[0]))
        for start, end in intervals:
            if p2 < start:
                res += 2
                p1, p2 = end - 1, end
            elif p1 < start:
                res += 1
                p1, p2 = p2, end
            else:
                continue
        return res



"""
Runtime: 16 ms, faster than 17.93% of Python3 online submissions for Set Intersection Size At Least Two.
Memory Usage: 18.91 MB, less than 79.31% of Python3 online submissions for Set Intersection Size At Least Two.
"""
# TC: O(nlog(n)), SC: O(n)
class Solution:
    def intersectionSizeTwo(self, intervals: List[List[int]]) -> int:
        res = []
        intervals.sort(key=lambda interval: (interval[1], -interval[0]))
        for start, end in intervals:
            if res:
                if res[-1] < start:
                    res.append(end - 1)
                    res.append(end)
                elif res[-2] < start:
                    res.append(end)
                else:
                    continue
            else:
                res.append(end - 1)
                res.append(end)
        return len(res)