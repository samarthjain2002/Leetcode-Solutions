"""
Accepted
40 [Medium]
Runtime: 28 ms, faster than 32.88% of Python3 online submissions for Combination Sum II.
Memory Usage:  17.75 MB, less than 9.86% of Python3 online submissions for Combination Sum II.
"""
class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()

        res = []
        def dfs(i, combo, total):
            if total == target:
                res.append(combo.copy())
                return

            if i >= len(candidates) or total > target:
                return

            # Subset with x candidate
            combo.append(candidates[i])
            dfs(i + 1, combo, total + candidates[i])
            combo.pop()
            # Shifting until we find a candidate that is not x
            while i + 1 < len(candidates) and candidates[i] == candidates[i + 1]:
                i += 1
            # Subset without x candidate
            dfs(i + 1, combo, total)

        dfs(0, [], 0)
        return res