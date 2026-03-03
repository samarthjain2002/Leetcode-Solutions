"""
Accepted
1689 [Medium]
Runtime: 87 ms, faster than 7.77% of Python3 online submissions for Partitioning Into Minimum Number Of Deci-Binary Numbers.
Memory Usage: 19.88 MB, less than 88.51% of Python3 online submissions for Partitioning Into Minimum Number Of Deci-Binary Numbers.
"""
class Solution:
    def minPartitions(self, n: str) -> int:
        res = 0
        for dig in n:
            res = max(res, int(dig))
        return res