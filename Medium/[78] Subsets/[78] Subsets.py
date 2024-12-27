"""
Accepted
78 [Medium]
Runtime: 4528 ms, faster than 40.68% of Python3 online submissions for Subsets.
Memory Usage:  17.89 MB, less than 7.25% of Python3 online submissions for Subsets.
"""
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []

        subset = []
        def backtrack(i):
            if i >= len(nums):
                res.append(subset.copy())
                return

            subset.append(nums[i])
            backtrack(i + 1)

            subset.pop()
            backtrack(i + 1)

        backtrack(0)
        return res