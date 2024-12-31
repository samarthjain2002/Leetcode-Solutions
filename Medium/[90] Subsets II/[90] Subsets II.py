"""
Accepted
90 [Medium]
Runtime: 3 ms, faster than 29.31% of Python3 online submissions for Subsets II.
Memory Usage: 18.08 MB, less than 7.92% of Python3 online submissions for Subsets II.
"""
class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        
        res = set()
        subset = []

        def backtrack(i):
            if i >= len(nums):
                res.add(tuple(subset))
                return

            subset.append(nums[i])
            backtrack(i + 1)

            subset.pop()
            backtrack(i + 1)

        backtrack(0)
        return [list(subset) for subset in res]