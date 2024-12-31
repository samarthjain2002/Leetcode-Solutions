"""
Accepted
77 [Medium]
Runtime: 140 ms, faster than 43.04% of Python3 online submissions for Combinations.
Memory Usage: 59.56 MB, less than 26.30% of Python3 online submissions for Combinations.
"""
class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        res = []
        def backtrack(start, combo):
            if len(combo) == k:
                res.append(combo.copy())
                return

            for i in range(start, n + 1):
                combo.append(i)
                backtrack(i + 1, combo)
                combo.pop()

        backtrack(1, [])
        return res