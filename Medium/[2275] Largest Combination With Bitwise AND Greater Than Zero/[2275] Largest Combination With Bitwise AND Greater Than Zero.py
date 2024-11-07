"""
Accepted
2275 [Medium]
Runtime: 598 ms, faster than 30.00% of Python3 online submissions for Largest Combination With Bitwise AND Greater Than Zero.
Memory Usage:  26.79 MB, less than 81.82% of Python3 online submissions for Largest Combination With Bitwise AND Greater Than Zero.
"""
class Solution:
    def largestCombination(self, candidates: List[int]) -> int:
        res = 0
        for i in range(32):
            cnt = 0
            for candidate in candidates:
                if (1 << i) & candidate:
                    cnt += 1
            res = max(res, cnt)

        return res