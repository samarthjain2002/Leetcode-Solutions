"""
Accepted
274 [Medium]
Runtime: 42 ms, faster than 52.16% of Python3 online submissions for H-Index.
Memory Usage:  16.86 MB, less than 76.08% of Python3 online submissions for H-Index.
"""
class Solution:
    def hIndex(self, citations: List[int]) -> int:
        N = len(citations)
        citations.sort()
        hashMap = defaultdict(int)
        res = 0
        for i, c in enumerate(citations):
            if N - i >= c:
                res = c
            else:
                res = max(res, N - i)
        return res