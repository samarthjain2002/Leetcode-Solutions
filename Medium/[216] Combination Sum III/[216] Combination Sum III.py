"""
Accepted
216 [Medium]
Runtime: 0 ms, faster than 100.00% of Python3 online submissions for Combination Sum III.
Memory Usage:  17.70 MB, less than 11.19% of Python3 online submissions for Combination Sum III.
"""
class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        res = []
        def dfs(i, combo, total):
            if total == n and len(combo) == k:
                res.append(combo.copy())
                return
            elif total > n or len(combo) > k:
                return
            elif i > 9:
                return

            combo.append(i)
            dfs(i + 1, combo, total + i)
            combo.pop()
            dfs(i + 1, combo, total)

        dfs(1, [], 0)
        return res