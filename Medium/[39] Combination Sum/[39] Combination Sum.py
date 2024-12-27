"""
Accepted
39 [Medium]
Runtime: 15 ms, faster than 32.54% of Python3 online submissions for Combination Sum.
Memory Usage:  17.80 MB, less than 8.34% of Python3 online submissions for Combination Sum.
"""
class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []

        def dfs(i, combo, total):
            if total == target:
                res.append(combo.copy())
                return

            if i >= len(candidates) or total > target:
                return

            combo.append(candidates[i])
            dfs(i, combo, total + candidates[i])
            combo.pop()
            dfs(i + 1, combo, total)

        dfs(0, [], 0)
        return res